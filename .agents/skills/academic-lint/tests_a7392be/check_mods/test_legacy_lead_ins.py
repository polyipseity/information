"""The tree holds no legacy answer lead-in.

A note used to answer with ``> Solution:``, ``> Explanation:``, ``> Answer:`` or
``> _Explanation._`` under its question.  Those lines are now written as the
block's own items, ``> ---`` then ``> - solution:`` and ``> - explanation:``, so
the validator reads them by slot.  It reads a leftover lead-in by slot too, which
is why this test exists: a note that keeps one answers to the rules while it
looks like prose, and nothing else would report it.
"""

import re
from pathlib import Path as SyncPath

"""A legacy lead-in line, colon or italic form, as the migration found them."""
LEGACY_LEAD_IN_RE = re.compile(
    r"^>\s*(?:Solution|Explanation|Answer)\s*:|^>\s*_(?:Solution|Explanation)\._",
    re.MULTILINE,
)

"""The trees a note lives in."""
CORPORA: tuple[SyncPath, ...] = (
    SyncPath("special/academia"),
    SyncPath("private/special/academia"),
)


def repo_root() -> SyncPath:
    """Return the repository root, the nearest ancestor carrying ``AGENTS.md``."""
    for parent in SyncPath(__file__).resolve().parents:
        if (parent / "AGENTS.md").is_file():
            return parent
    raise RuntimeError("no AGENTS.md above this test file")


def note_paths() -> list[SyncPath]:
    """Return every academic note, or nothing when this clone carries no corpus."""
    root = repo_root()
    return [
        note for corpus in CORPORA for note in sorted((root / corpus).rglob("*.md"))
    ]


def test_no_note_keeps_a_legacy_answer_lead_in():
    """Every answer in the tree is written as a labelled item of its block."""
    offenders = [
        f"{note.relative_to(repo_root())}:{number}"
        for note in note_paths()
        for number, line in enumerate(note.read_text(encoding="utf-8").splitlines(), 1)
        if LEGACY_LEAD_IN_RE.match(line)
    ]
    assert not offenders, offenders
