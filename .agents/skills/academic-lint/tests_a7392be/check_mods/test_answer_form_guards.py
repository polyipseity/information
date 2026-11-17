"""Two answer shapes the tree never wears.

A note used to answer with ``> Solution:``, ``> Explanation:``, ``> Answer:`` or
``> _Explanation._`` under its question.  Those lines are the block's own items
now, ``> ---`` then ``> - solution:`` and ``> - explanation:``.  The validator
reads a leftover lead-in by slot, which is why the first guard exists: a note
keeping one answers to the rules while it looks like prose.

The second: the items of a block sit on adjacent lines, and a blank ``>`` line
between two of them reads as an empty paragraph in the answer.  No single-file
run reports either defect, so both are checked over the whole tree.
"""

import re
from pathlib import Path as SyncPath

"""Public API of this test module: the two guards."""
__all__ = (
    "test_no_answer_item_is_set_off_by_a_blank_line",
    "test_no_note_keeps_a_legacy_answer_lead_in",
)

"""A legacy lead-in line, colon or italic form, as the migration found them."""
LEGACY_LEAD_IN_RE = re.compile(
    r"^>\s*(?:Solution|Explanation|Answer)\s*:|^>\s*_(?:Solution|Explanation)\._",
    re.MULTILINE,
)

"""Two answer items with a blank quote line between them."""
ITEM_GAP_RE = re.compile(
    r"^> - (?:solution|explanation|annotation):[^\n]*\n> *\n"
    r"> - (?:solution|explanation|annotation):",
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


def offences(pattern: re.Pattern[str]) -> list[str]:
    """Return ``path:line`` for every match of *pattern* in the tree."""
    found: list[str] = []
    for note in note_paths():
        text = note.read_text(encoding="utf-8")
        name = note.relative_to(repo_root())
        for match in pattern.finditer(text):
            found.append(f"{name}:{text.count(chr(10), 0, match.start()) + 1}")
    return found


def test_no_note_keeps_a_legacy_answer_lead_in():
    """Every answer in the tree is written as a labelled item of its block."""
    assert not offences(LEGACY_LEAD_IN_RE)


def test_no_answer_item_is_set_off_by_a_blank_line():
    """The items of one block sit on adjacent lines everywhere in the tree."""
    assert not offences(ITEM_GAP_RE)
