"""Read-only collection of the working tree's uncommitted changes.

The change audit compares the working tree against ``HEAD``.  Nothing in this
module writes to the repository: it only runs ``git rev-parse``, ``git
status``, ``git diff --name-status``, and ``git diff -U0``.

Only the facts the change rules need are collected: per file status, added
and deleted bytes, added and deleted lines, and whether the file is binary.
Bytes are counted from the unified patch, because a line count cannot tell a
rewrapped paragraph from a new one.
"""

from collections.abc import Sequence
from dataclasses import dataclass
from enum import StrEnum
from os.path import abspath, realpath

from anyio import run_process

"""Public symbols exported by this module."""
__all__ = (
    "ChangeSet",
    "ChangeStatus",
    "FileChange",
    "added_lines",
    "collect",
    "head_text",
)


class ChangeStatus(StrEnum):
    """What an uncommitted edit did to one file."""

    ADDED = "added"
    DELETED = "deleted"
    MODIFIED = "modified"
    RENAMED = "renamed"
    UNTRACKED = "untracked"


@dataclass(frozen=True)
class FileChange:
    """One changed file, measured against ``HEAD``.

    ``path`` is relative to the repository root and uses forward slashes.
    ``old_path`` is set only for a rename.  ``binary`` files carry zero byte
    counts, because a patch has no content lines to weigh.
    """

    path: str
    status: ChangeStatus
    added_bytes: int
    deleted_bytes: int
    added_lines: int
    deleted_lines: int
    added_h2: int = 0
    deleted_h2: int = 0
    added_h3: int = 0
    old_path: str | None = None
    binary: bool = False

    @property
    def is_new(self) -> bool:
        """Whether every byte in this file is an addition."""
        return self.status in (ChangeStatus.ADDED, ChangeStatus.UNTRACKED)

    @property
    def growth(self) -> int:
        """Net byte growth of this file."""
        return self.added_bytes - self.deleted_bytes


@dataclass(frozen=True)
class ChangeSet:
    """Every uncommitted change under one repository root."""

    root: str
    changes: tuple[FileChange, ...]

    def under(self, roots: Sequence[str]) -> tuple[FileChange, ...]:
        """Return the changes that sit under any of *roots*.

        *roots* are paths as the CLI received them, absolute or relative to
        the repository root.  A root may name a single file.
        """
        wanted = tuple(_normalize_root(root, self.root) for root in roots)
        return tuple(
            change
            for change in self.changes
            if any(_is_under(change.path, prefix) for prefix in wanted)
        )


def _normalize_root(root: str, repo_root: str) -> str:
    """Return *root* as a forward-slash path relative to *repo_root*.

    Both an absolute path and a path relative to the current directory are
    accepted, so the audit stays correct when the tool is run from a
    subdirectory.
    """
    text = abspath(root).replace("\\", "/")
    for candidate in (repo_root, realpath(repo_root)):
        base = candidate.replace("\\", "/").rstrip("/")
        if text == base:
            return ""
        if text.startswith(base + "/"):
            return text[len(base) + 1 :].rstrip("/")
    return text.rstrip("/")


def _is_under(path: str, prefix: str) -> bool:
    """Whether *path* equals *prefix* or sits inside it."""
    if not prefix:
        return True
    return path == prefix or path.startswith(prefix + "/")


async def _git(root: str, *args: str) -> tuple[int, bytes]:
    """Run one read-only git command inside *root* and return its output."""
    result = await run_process(("git", "-C", root, *args), check=False)
    return result.returncode, result.stdout


def _decode_path(raw: bytes) -> str:
    """Decode a NUL-terminated path from ``git`` machine output."""
    return raw.decode("utf-8", errors="surrogateescape")


def _num(value: bytes) -> int:
    """Return a byte or line count, treating a binary marker as zero."""
    return 0 if value == b"-" else int(value)


def _parse_name_status(data: bytes) -> dict[str, tuple[ChangeStatus, str | None]]:
    """Parse ``git diff --name-status -z`` into ``path -> (status, old)``."""
    tokens = data.split(b"\0")
    result: dict[str, tuple[ChangeStatus, str | None]] = {}
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if not token:
            index += 1
            continue
        code = token.decode("ascii", errors="replace")
        if code[0] in ("R", "C") and index + 2 < len(tokens):
            old = _decode_path(tokens[index + 1])
            new = _decode_path(tokens[index + 2])
            index += 3
            result[new] = (
                ChangeStatus.RENAMED if code[0] == "R" else ChangeStatus.ADDED,
                old,
            )
            continue
        if index + 1 >= len(tokens):
            break
        path = _decode_path(tokens[index + 1])
        index += 2
        result[path] = (_status_for(code[0]), None)
    return result


def _status_for(code: str) -> ChangeStatus:
    """Map a ``--name-status`` code letter to a :class:`ChangeStatus`."""
    return {
        "A": ChangeStatus.ADDED,
        "D": ChangeStatus.DELETED,
    }.get(code, ChangeStatus.MODIFIED)


def _parse_patch(
    data: bytes,
) -> dict[str, tuple[int, int, int, int, int, int, int, bool]]:
    """Parse a ``-U0`` patch into per-path byte, line, and heading counts.

    Returns ``path -> (added_bytes, deleted_bytes, added_lines,
    deleted_lines, added_h2, deleted_h2, added_h3, binary)``.  A byte count
    adds the one byte the newline would occupy, so a line weighs its content
    plus its terminator.  Heading counts feed the section-growth rule.
    """
    counts: dict[str, list[int | bool]] = {}
    current: str | None = None
    previous: str | None = None
    for raw in data.split(b"\n"):
        if raw.startswith(b"diff --git "):
            current = None
            previous = None
        elif raw.startswith(b"--- "):
            target = raw[4:].strip()
            previous = (
                None
                if target == b"/dev/null"
                else _decode_path(target[2:] if target.startswith(b"a/") else target)
            )
        elif raw.startswith(b"+++ "):
            target = raw[4:].strip()
            if target == b"/dev/null":
                current = previous
            else:
                current = _decode_path(
                    target[2:] if target.startswith(b"b/") else target
                )
            if current is not None and current not in counts:
                counts[current] = [0] * 7
        elif raw.startswith(b"+"):
            if current is not None:
                row = counts[current]
                row[0] += len(raw)
                row[2] += 1
                level = _heading_level(raw[1:])
                if level == 2:
                    row[4] += 1
                elif level == 3:
                    row[6] += 1
        elif raw.startswith(b"-"):
            if current is not None:
                row = counts[current]
                row[1] += len(raw)
                row[3] += 1
                if _heading_level(raw[1:]) == 2:
                    row[5] += 1
    return {
        path: (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        for path, row in counts.items()
    }


def _binary_paths(data: bytes) -> set[str]:
    """Return the paths ``git diff --numstat -z`` reports as binary."""
    found: set[str] = set()
    for token in data.split(b"\0"):
        parts = token.split(b"\t")
        if len(parts) == 3 and parts[0] == b"-" and parts[2]:
            found.add(_decode_path(parts[2]))
    return found


def _heading_level(line: bytes) -> int:
    """Return the ``#`` level of a patch content line, or 0."""
    stripped = line.lstrip(b" ")
    level = len(stripped) - len(stripped.lstrip(b"#"))
    return level if 1 <= level <= 6 and stripped[level : level + 1] == b" " else 0


async def _untracked(root: str) -> set[str]:
    """Return the untracked files, as repository-relative paths."""
    code, data = await _git(
        root, "status", "--porcelain=v1", "-z", "--untracked-files=all"
    )
    if code != 0:
        return set()
    found: set[str] = set()
    for entry in data.split(b"\0"):
        if entry.startswith(b"?? "):
            found.add(_decode_path(entry[3:]))
    return found


async def _file_size(
    root: str, path: str, binary_probe: int = 8192
) -> tuple[int, int, bool]:
    """Return ``(bytes, lines, binary)`` for an untracked file."""
    try:
        with open(f"{root}/{path}", "rb") as handle:
            data = handle.read()
    except OSError:
        return (0, 0, True)
    binary = b"\0" in data[:binary_probe]
    lines = data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)
    return (len(data), 0 if binary else lines, binary)


async def collect(cwd: str | None = None) -> ChangeSet | None:
    """Collect the uncommitted changes of the work tree containing *cwd*.

    Returns ``None`` when *cwd* is not inside a git work tree, or when the
    repository has no commit yet and so has no baseline to compare against.
    """
    probe = cwd if cwd is not None else "."
    code, data = await _git(probe, "rev-parse", "--show-toplevel")
    if code != 0:
        return None
    root = data.decode("utf-8", errors="surrogateescape").strip()
    code, _ = await _git(root, "rev-parse", "--verify", "HEAD")
    if code != 0:
        return None

    code, status_data = await _git(
        root, "diff", "--name-status", "-z", "-M", "HEAD", "--"
    )
    named = _parse_name_status(status_data) if code == 0 else {}
    code, patch_data = await _git(root, "diff", "-U0", "--no-color", "-M", "HEAD", "--")
    counts = _parse_patch(patch_data) if code == 0 else {}
    code, numstat_data = await _git(root, "diff", "--numstat", "-z", "-M", "HEAD", "--")
    binary_paths = _binary_paths(numstat_data) if code == 0 else set()

    changes: list[FileChange] = []
    for path, (status, old_path) in named.items():
        stats = counts.get(path, (0, 0, 0, 0, 0, 0, 0))
        changes.append(
            FileChange(
                path=path,
                status=status,
                added_bytes=stats[0],
                deleted_bytes=stats[1],
                added_lines=stats[2],
                deleted_lines=stats[3],
                added_h2=stats[4],
                deleted_h2=stats[5],
                added_h3=stats[6],
                old_path=old_path,
                binary=path in binary_paths,
            )
        )

    for path in sorted(await _untracked(root)):
        size, lines, binary = await _file_size(root, path)
        changes.append(
            FileChange(
                path=path,
                status=ChangeStatus.UNTRACKED,
                added_bytes=size,
                deleted_bytes=0,
                added_lines=lines,
                deleted_lines=0,
                binary=binary,
            )
        )

    changes.sort(key=lambda change: change.path)
    return ChangeSet(root=root, changes=tuple(changes))


async def head_text(root: str, path: str) -> str | None:
    """Return the committed content of *path*, or ``None`` if it is absent."""
    code, data = await _git(root, "show", f"HEAD:{path}")
    if code != 0:
        return None
    return data.decode("utf-8", errors="replace")


async def added_lines(root: str, path: str) -> tuple[str, ...]:
    """Return the lines an uncommitted edit added to *path*."""
    code, data = await _git(root, "diff", "-U0", "--no-color", "HEAD", "--", path)
    if code != 0:
        return ()
    lines: list[str] = []
    for raw in data.split(b"\n"):
        if raw.startswith(b"+++ ") or not raw.startswith(b"+"):
            continue
        lines.append(raw[1:].decode("utf-8", errors="replace"))
    return tuple(lines)
