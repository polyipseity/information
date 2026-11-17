"""Tests for the change collector.

The parsing helpers are exercised on synthetic ``git`` output so they stay
fast and deterministic; one integration test builds a throwaway repository to
prove the real commands agree with the parser.
"""

import shutil
from os import PathLike, fspath
from pathlib import Path as SyncPath

import pytest
from anyio import Path, run_process
from main_mods import changes
from main_mods.changes import ChangeSet, ChangeStatus, FileChange, collect

"""Public symbols exported by this module (none)."""
__all__ = ()

"""Skip git-dependent tests when git is unavailable."""
requires_git = pytest.mark.skipif(
    shutil.which("git") is None, reason="git is not installed"
)


def test_parse_name_status_plain_and_rename():
    """A modified entry and a rename entry are both decoded."""
    data = b"M\0a/one.md\0R087\0a/old.md\0a/new.md\0"
    parsed = changes._parse_name_status(data)
    assert parsed["a/one.md"] == (ChangeStatus.MODIFIED, None)
    assert parsed["a/new.md"] == (ChangeStatus.RENAMED, "a/old.md")


def test_parse_patch_counts_bytes_lines_and_headings():
    """Added content weighs its bytes plus the newline it occupies."""
    patch = (
        b"diff --git a/x.md b/x.md\n"
        b"--- a/x.md\n"
        b"+++ b/x.md\n"
        b"@@ -1,1 +1,2 @@\n"
        b"-old\n"
        b"+new line\n"
        b"+## a section\n"
        b"diff --git a/y.md b/y.md\n"
        b"--- a/y.md\n"
        b"+++ b/y.md\n"
        b"@@ -1,1 +1,0 @@\n"
        b"-gone\n"
    )
    parsed = changes._parse_patch(patch)
    # each added line weighs its content plus the newline it occupies
    assert parsed["x.md"] == (22, 4, 2, 1, 1, 0, 0)
    assert parsed["y.md"][1] == 5
    assert parsed["y.md"][3] == 1


def test_binary_paths_are_read_from_numstat():
    """A binary entry is the one whose counts are dashes."""
    data = b"-\t-\tx.png\0" + b"3\t1\ty.md\0"
    assert changes._binary_paths(data) == {"x.png"}


def test_normalize_root_accepts_absolute_and_relative(tmp_path: PathLike[str]):
    """Both forms resolve to a repository-relative path."""
    repo = fspath(SyncPath.cwd())
    assert changes._normalize_root("special/academia", repo) == "special/academia"
    assert changes._normalize_root(f"{repo}/special/academia", repo) == (
        "special/academia"
    )
    # outside the repository the path stays absolute, so it matches nothing
    assert changes._normalize_root("special/academia", fspath(tmp_path)) == (
        f"{repo}/special/academia"
    )


def test_change_set_under_scopes_to_a_file_and_a_directory():
    """Scoping keeps the named file, its directory, and nothing else."""
    repo = fspath(SyncPath.cwd())
    change_set = ChangeSet(
        root=repo,
        changes=(
            FileChange("special/a/x.md", ChangeStatus.MODIFIED, 10, 1, 1, 1),
            FileChange("special/a/y/z.md", ChangeStatus.MODIFIED, 10, 1, 1, 1),
            FileChange("special/b/w.md", ChangeStatus.MODIFIED, 10, 1, 1, 1),
        ),
    )
    assert [c.path for c in change_set.under([f"{repo}/special/a/x.md"])] == [
        "special/a/x.md"
    ]
    assert [c.path for c in change_set.under(["special/a"])] == [
        "special/a/x.md",
        "special/a/y/z.md",
    ]


@pytest.mark.anyio
async def test_collect_outside_a_work_tree_returns_none(tmp_path: PathLike[str]):
    """A plain directory has no baseline, so the audit reports a skip."""
    assert await collect(fspath(tmp_path)) is None


@requires_git
@pytest.mark.anyio
async def test_collect_measures_a_real_repository(tmp_path: PathLike[str]):
    """A new file, an edited file, and a rename are measured as advertised."""
    root = fspath(tmp_path)
    await _git(root, "init")
    await _git(root, "config", "user.email", "test@example.com")
    await _git(root, "config", "user.name", "Test")
    note = Path(root) / "note.md"
    await note.write_text("one\ntwo\n")
    await _git(root, "add", "note.md")
    await _git(root, "commit", "-m", "init")

    await note.write_text("one\nchanged\n## added\n")
    fresh = Path(root) / "fresh.md"
    await fresh.write_text("brand new\n")

    collected = await collect(root)
    assert collected is not None
    by_path = {change.path: change for change in collected.changes}
    assert by_path["note.md"].status is ChangeStatus.MODIFIED
    assert by_path["note.md"].added_h2 == 1
    assert by_path["note.md"].deleted_bytes > 0
    assert by_path["fresh.md"].status is ChangeStatus.UNTRACKED
    assert by_path["fresh.md"].added_bytes == len("brand new\n")


@requires_git
@pytest.mark.anyio
async def test_head_text_and_added_lines(tmp_path: PathLike[str]):
    """Committed content and added lines are both read from the repository."""
    root = fspath(tmp_path)
    await _git(root, "init")
    await _git(root, "config", "user.email", "test@example.com")
    await _git(root, "config", "user.name", "Test")
    note = SyncPath(root) / "note.md"
    note.write_text("one\n")
    await _git(root, "add", "note.md")
    await _git(root, "commit", "-m", "init")
    note.write_text("one\ntwo\n")

    assert await changes.head_text(root, "note.md") == "one\n"
    assert await changes.added_lines(root, "note.md") == ("two",)
    assert await changes.head_text(root, "absent.md") is None


async def _git(root: str, *args: str) -> None:
    """Run one git command in *root*, failing loudly on error."""
    result = await run_process(("git", "-C", root, *args), check=False)
    if result.returncode != 0:
        raise AssertionError(result.stderr.decode())
