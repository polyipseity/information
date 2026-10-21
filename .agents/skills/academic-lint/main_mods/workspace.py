"""Workspace rules: checks that need the diff, not one file.

These rules run once per invocation, after every file has been checked, and
they read the uncommitted window between the working tree and ``HEAD``.  Each
one is a warning by construction: :func:`_warning` is the only constructor a
rule may use, so no rule here can report an error.

Because the audit reads an uncommitted window, a warning clears when the
files are committed.  Committing is the user's act.  An agent that believes
an addition is genuine new material ignores the warning and says so in its
report instead of deleting content to silence it.
"""

import re
from collections.abc import Awaitable, Callable, Sequence
from dataclasses import dataclass
from pathlib import Path as SyncPath

from anyio import Path

from .changes import ChangeSet, ChangeStatus, FileChange, added_lines, head_text
from .models import Severity, ValidationMessage
from .utils import has_flash_tag, is_topic_note_location, parse_frontmatter

"""Public symbols exported by this module."""
__all__ = (
    "NON_SUPPRESSIBLE_RULE_IDS",
    "WORKSPACE_RULES",
    "WorkspaceContext",
    "WorkspaceMessage",
    "run_workspace_rules",
)

"""One warning tied to the file that caused it."""
WorkspaceMessage = tuple[Path, ValidationMessage]

"""Rule ids that a suppression comment may never silence.

A directive naming one of these is an error, so a warning about the shape of
an edit cannot be hidden by the file it is about.
"""
NON_SUPPRESSIBLE_RULE_IDS = frozenset(
    {"change_append_bias", "change_flat_section_growth", "change_note_without_index"}
)


@dataclass(frozen=True)
class WorkspaceContext:
    """Everything a workspace rule may read.

    ``changes`` is ``None`` when the audit could not run, which happens
    outside a git work tree.  ``roots`` holds the CLI paths, so a single-file
    run stays scoped to that file.
    """

    changes: ChangeSet
    roots: tuple[str, ...]


"""Signature of a workspace rule."""
WorkspaceRule = Callable[[WorkspaceContext], Awaitable[Sequence[WorkspaceMessage]]]


"""Registered workspace rules, keyed by id."""
WORKSPACE_RULES: dict[str, WorkspaceRule] = {}


def workspace_rule(func: WorkspaceRule) -> WorkspaceRule:
    """Register *func* as a workspace rule under its own name."""
    WORKSPACE_RULES[func.__name__] = func
    return func


def _warning(
    rule_id: str, msg: str, path: Path, line: int | None = None
) -> WorkspaceMessage:
    """Build the only kind of message a workspace rule may emit."""
    return (path, ValidationMessage(rule_id, msg, Severity.WARNING, line=line))


async def _topic_note(root: str, change: FileChange) -> bool:
    """Whether *change* touches a topic note that still exists in the tree."""
    if change.binary or not change.path.endswith(".md"):
        return False
    if change.status is ChangeStatus.DELETED:
        return False
    parts = SyncPath(change.path).parts
    if not is_topic_note_location(parts, SyncPath(change.path).name):
        return False
    try:
        text = await (Path(root) / change.path).read_text()
    except (OSError, UnicodeDecodeError):
        return False
    front = parse_frontmatter(text)
    return front is not None and has_flash_tag(front)


def _ratio(added: int, deleted: int) -> str:
    """Return the added-to-deleted ratio as a short string."""
    if deleted == 0:
        return f"{added}:0"
    return f"{added / deleted:.1f}:1"


@workspace_rule
async def change_append_bias(ctx: WorkspaceContext) -> list[WorkspaceMessage]:
    """Warn when an edit adds far more than it deletes.

    The check is a pair of fixed thresholds rather than a share of the file,
    so it behaves the same on a short note and a long one: at least 300 bytes
    added, and at least three bytes added for every byte deleted.  One
    deleted sentence therefore cannot clear it; integrating the addition and
    cutting what it made redundant can.
    """
    messages: list[WorkspaceMessage] = []
    for change in ctx.changes.under(ctx.roots):
        if change.is_new or not await _topic_note(ctx.changes.root, change):
            continue
        if change.added_bytes < 300 or change.deleted_bytes * 3 >= change.added_bytes:
            continue
        messages.append(
            _warning(
                "change_append_bias",
                (
                    f"this edit added {change.added_bytes} bytes and deleted "
                    f"{change.deleted_bytes} ({_ratio(change.added_bytes, change.deleted_bytes)}). "
                    "Integrate the addition into the existing text and delete what it "
                    "made redundant. Deleting a third of the addition clears this; so "
                    "does committing, which the user does, not the agent."
                ),
                Path(ctx.changes.root) / change.path,
            )
        )
    return messages


@workspace_rule
async def change_flat_section_growth(ctx: WorkspaceContext) -> list[WorkspaceMessage]:
    """Warn when an edit adds top-level sections without nesting any.

    A note that already had six or more ``##`` sections and gains another one,
    with no ``###`` added anywhere, has grown sideways.  The new material
    belongs under a section that already exists, or the note needs a real
    heading level.
    """
    messages: list[WorkspaceMessage] = []
    for change in ctx.changes.under(ctx.roots):
        if not await _topic_note(ctx.changes.root, change):
            continue
        if change.added_h2 == 0 or change.deleted_h2 or change.added_h3:
            continue
        before = await head_text(ctx.changes.root, change.path)
        if before is None:
            continue
        existing = len(re.findall(r"^##\s", before, re.MULTILINE))
        if existing < 6:
            continue
        messages.append(
            _warning(
                "change_flat_section_growth",
                (
                    f"this edit added {change.added_h2} '##' section(s) to a note "
                    f"that already had {existing}, and added no '###'. Nest the new "
                    "material under a section that exists, or give the note the "
                    "heading level it is missing."
                ),
                Path(ctx.changes.root) / change.path,
            )
        )
    return messages


@workspace_rule
async def change_note_without_index(ctx: WorkspaceContext) -> list[WorkspaceMessage]:
    """Warn when a topic note changes and its course index does not.

    The index gains a reference when one of its added lines names the changed
    note, as a ``§`` anchor or a child-list entry, and when the file grows by
    at least 60 bytes.  A whitespace touch satisfies neither.
    """
    messages: list[WorkspaceMessage] = []
    changes = ctx.changes.under(ctx.roots)
    index_changes = {
        change.path: change for change in changes if change.path.endswith("index.md")
    }
    added_by_index: dict[str, tuple[str, ...]] = {}

    for change in changes:
        root = ctx.changes.root
        if not await _topic_note(root, change):
            continue
        index_path = await _nearest_index(root, change.path)
        if index_path is None:
            continue
        if index_path in added_by_index:
            continue
        index_change = index_changes.get(index_path)
        if index_change is not None:
            added_by_index[index_path] = (
                await added_lines(root, index_path) if not index_change.is_new else ()
            )
        else:
            added_by_index[index_path] = ()

    for change in changes:
        root = ctx.changes.root
        if not await _topic_note(root, change):
            continue
        index_path = await _nearest_index(root, change.path)
        if index_path is None:
            continue
        index_change = index_changes.get(index_path)
        if index_change is not None and index_change.added_bytes >= 60:
            if any(_mentions(line, change.path) for line in added_by_index[index_path]):
                continue
        messages.append(
            _warning(
                "change_note_without_index",
                (
                    f"'{SyncPath(change.path).name}' changed but "
                    f"'{SyncPath(index_path).name}' in the same directory did not gain "
                    "a link to it. Add the note, or the sections this edit created, to "
                    "the course index in the same edit."
                ),
                Path(root) / index_path,
            )
        )
    return messages


def _mentions(line: str, note_path: str) -> bool:
    """Whether an added index line points at the changed note.

    Both shapes count: a ``§`` anchor into one of the note's sections, and a
    plain line in the index's child list.  Either way the line has to name
    the note, so a ``§`` link to some other page is not an update.
    """
    name = SyncPath(note_path).name
    return name in line or name.replace(" ", "%20") in line


async def _nearest_index(root: str, path: str) -> str | None:
    """Return the closest ``index.md`` above *path*, relative to *root*."""
    directory = SyncPath(path).parent
    while True:
        candidate = directory / "index.md"
        relative = candidate.as_posix()
        if await (Path(root) / relative).is_file():
            return relative
        if directory.as_posix() in (".", ""):
            return None
        directory = directory.parent


async def run_workspace_rules(
    changes: ChangeSet | None, roots: Sequence[str]
) -> list[WorkspaceMessage]:
    """Run every registered workspace rule and return their messages."""
    if changes is None:
        return []
    context = WorkspaceContext(changes=changes, roots=tuple(roots))
    messages: list[WorkspaceMessage] = []
    for rule in WORKSPACE_RULES.values():
        messages.extend(await rule(context))
    return messages
