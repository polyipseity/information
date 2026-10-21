"""Tests for the workspace (change) rules.

The rules read a diff, so each test builds a small tree on disk and hands the
rules a synthetic :class:`ChangeSet`.  Git itself is exercised in
``test_changes.py``; here the two git helpers are patched, which keeps these
tests about the rules and not about git.
"""

from os import PathLike, fspath
from pathlib import Path as SyncPath

import pytest
from main_mods import workspace
from main_mods.changes import ChangeSet, ChangeStatus, FileChange
from main_mods.models import Severity
from main_mods.workspace import (
    NON_SUPPRESSIBLE_RULE_IDS,
    WORKSPACE_RULES,
    WorkspaceContext,
    change_append_bias,
    change_flat_section_growth,
    change_note_without_index,
    run_workspace_rules,
)

"""Public symbols exported by this module (none)."""
__all__ = ()

"""A note body with enough frontmatter to count as a topic note."""
NOTE_FRONT = "---\ntags:\n  - flashcard/active/special/academia/X/C\n---\n\n# note\n"


def _note(root: SyncPath) -> SyncPath:
    """Create a topic note and return its path."""
    note = root / "special/academia/X/C/note.md"
    note.parent.mkdir(parents=True, exist_ok=True)
    note.write_text(NOTE_FRONT)
    return note


def _index(root: SyncPath) -> SyncPath:
    """Create the course index beside the note and return its path."""
    index = root / "special/academia/X/C/index.md"
    index.parent.mkdir(parents=True, exist_ok=True)
    index.write_text("# C\n")
    return index


def _change(
    path: str,
    root: str,
    added_bytes: int = 900,
    deleted_bytes: int = 100,
    added_lines: int = 20,
    deleted_lines: int = 2,
    added_h2: int = 0,
    deleted_h2: int = 0,
    added_h3: int = 0,
) -> ChangeSet:
    """Build a one-file change set with sane defaults."""
    change = FileChange(
        path=path,
        status=ChangeStatus.MODIFIED,
        added_bytes=added_bytes,
        deleted_bytes=deleted_bytes,
        added_lines=added_lines,
        deleted_lines=deleted_lines,
        added_h2=added_h2,
        deleted_h2=deleted_h2,
        added_h3=added_h3,
    )
    return ChangeSet(root=root, changes=(change,))


def _ctx(root: SyncPath) -> WorkspaceContext:
    """Wrap a one-file change set rooted at *root*."""
    return WorkspaceContext(
        changes=_change("special/academia/X/C/note.md", fspath(root)),
        roots=(fspath(root),),
    )


def test_every_change_rule_is_non_suppressible():
    """The two lists cannot drift apart."""
    assert NON_SUPPRESSIBLE_RULE_IDS == frozenset(WORKSPACE_RULES)


@pytest.mark.anyio
async def test_run_workspace_rules_skips_a_missing_audit():
    """No audit means no messages, not an exception."""
    assert await run_workspace_rules(None, ("special/academia",)) == []


@pytest.mark.anyio
async def test_append_bias_fires_on_a_lopsided_edit(tmp_path: PathLike[str]):
    """Nine bytes added per byte deleted is a lopsided edit."""
    root = SyncPath(fspath(tmp_path))
    _note(root)
    messages = await change_append_bias(_ctx(root))
    assert len(messages) == 1
    path, message = messages[0]
    assert path.name == "note.md"
    assert message.rule_id == "change_append_bias"
    assert message.severity is Severity.WARNING
    assert "900" in message.msg and "100" in message.msg


@pytest.mark.anyio
async def test_append_bias_is_silent_at_exactly_one_third(tmp_path: PathLike[str]):
    """Deleting exactly a third of the addition clears the rule."""
    root = SyncPath(fspath(tmp_path))
    _note(root)
    context = WorkspaceContext(
        changes=_change(
            "special/academia/X/C/note.md", fspath(root), deleted_bytes=300
        ),
        roots=(fspath(root),),
    )
    assert await change_append_bias(context) == []


@pytest.mark.anyio
async def test_append_bias_fires_one_byte_under_a_third(tmp_path: PathLike[str]):
    """The bar is a third, not a quarter, and one byte decides it."""
    root = SyncPath(fspath(tmp_path))
    _note(root)
    context = WorkspaceContext(
        changes=_change(
            "special/academia/X/C/note.md", fspath(root), deleted_bytes=299
        ),
        roots=(fspath(root),),
    )
    assert len(await change_append_bias(context)) == 1


@pytest.mark.anyio
async def test_append_bias_ignores_a_small_addition(tmp_path: PathLike[str]):
    """A 40-byte addition is below the floor however lopsided it is."""
    root = SyncPath(fspath(tmp_path))
    _note(root)
    context = WorkspaceContext(
        changes=_change(
            "special/academia/X/C/note.md",
            fspath(root),
            added_bytes=40,
            deleted_bytes=0,
        ),
        roots=(fspath(root),),
    )
    assert await change_append_bias(context) == []


@pytest.mark.anyio
async def test_append_bias_ignores_new_and_non_topic_files(tmp_path: PathLike[str]):
    """A new note is legitimately all addition, and an index is not a note."""
    root = SyncPath(fspath(tmp_path))
    _note(root)
    _index(root)
    for path, status in (
        ("special/academia/X/C/note.md", ChangeStatus.UNTRACKED),
        ("special/academia/X/C/index.md", ChangeStatus.MODIFIED),
        ("special/academia/X/C/picture.svg", ChangeStatus.MODIFIED),
    ):
        context = WorkspaceContext(
            changes=ChangeSet(
                root=fspath(root),
                changes=(FileChange(path, status, 5000, 0, 90, 0),),
            ),
            roots=(fspath(root),),
        )
        assert await change_append_bias(context) == [], path


@pytest.mark.anyio
async def test_flat_section_growth_fires_above_six_sections(
    tmp_path: PathLike[str], monkeypatch: pytest.MonkeyPatch
):
    """Adding an eighth top-level section with no nesting is the defect."""

    async def eight_sections(root: str, path: str) -> str:
        """Stand in for the committed file."""
        return "".join(f"## s{index}\n" for index in range(8))

    monkeypatch.setattr(workspace, "head_text", eight_sections)
    root = SyncPath(fspath(tmp_path))
    _note(root)
    context = WorkspaceContext(
        changes=_change("special/academia/X/C/note.md", fspath(root), added_h2=1),
        roots=(fspath(root),),
    )
    messages = await change_flat_section_growth(context)
    assert len(messages) == 1
    assert "already had 8" in messages[0][1].msg


@pytest.mark.anyio
async def test_flat_section_growth_stays_quiet_when_nesting_or_short(
    tmp_path: PathLike[str], monkeypatch: pytest.MonkeyPatch
):
    """Nesting, merging, or a note with few sections all clear it."""
    root = SyncPath(fspath(tmp_path))
    _note(root)

    async def eight_sections(root_path: str, path: str) -> str:
        """Stand in for the committed file."""
        return "".join(f"## s{index}\n" for index in range(8))

    async def five_sections(root_path: str, path: str) -> str:
        """A note below the six-section floor."""
        return "".join(f"## s{index}\n" for index in range(5))

    for head_text, overrides in (
        (eight_sections, {"added_h3": 1}),
        (eight_sections, {"deleted_h2": 1}),
        (eight_sections, {"added_h2": 0}),
        (five_sections, {}),
    ):
        monkeypatch.setattr(workspace, "head_text", head_text)
        fields: dict[str, int] = {"added_h2": 1}
        fields.update(overrides)
        context = WorkspaceContext(
            changes=_change(
                "special/academia/X/C/note.md", root=fspath(root), **fields
            ),
            roots=(fspath(root),),
        )
        assert await change_flat_section_growth(context) == [], overrides


@pytest.mark.anyio
async def test_note_without_index_fires_when_the_index_is_untouched(
    tmp_path: PathLike[str],
):
    """A changed note with no index edit at all is the plain case."""
    root = SyncPath(fspath(tmp_path))
    _note(root)
    _index(root)
    messages = await change_note_without_index(_ctx(root))
    assert len(messages) == 1
    path, message = messages[0]
    assert path.name == "index.md"
    assert "note.md" in message.msg


@pytest.mark.anyio
async def test_note_without_index_accepts_a_link_and_rejects_a_touch(
    tmp_path: PathLike[str], monkeypatch: pytest.MonkeyPatch
):
    """An added link clears it; a large edit without one does not."""
    root = SyncPath(fspath(tmp_path))
    _note(root)
    _index(root)

    async def linked(root_path: str, path: str) -> tuple[str, ...]:
        """An index edit that links the note."""
        return ("- [§ energy](note.md#energy)",)

    async def unlinked(root_path: str, path: str) -> tuple[str, ...]:
        """An index edit that changes something else."""
        return ("- [§ other](other.md#other)",)

    index_change = FileChange(
        "special/academia/X/C/index.md", ChangeStatus.MODIFIED, 120, 10, 4, 1
    )
    note_change = FileChange("special/academia/X/C/note.md", "modified", 40, 200, 2, 9)

    monkeypatch.setattr(workspace, "added_lines", linked)
    context = WorkspaceContext(
        changes=ChangeSet(fspath(root), (note_change, index_change)),
        roots=(fspath(root),),
    )
    assert await change_note_without_index(context) == []

    monkeypatch.setattr(workspace, "added_lines", unlinked)
    assert len(await change_note_without_index(context)) == 1

    tiny_index = FileChange("special/academia/X/C/index.md", "modified", 40, 10, 1, 1)
    monkeypatch.setattr(workspace, "added_lines", linked)
    context = WorkspaceContext(
        changes=ChangeSet(fspath(root), (note_change, tiny_index)),
        roots=(fspath(root),),
    )
    assert len(await change_note_without_index(context)) == 1
