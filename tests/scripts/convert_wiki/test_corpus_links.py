"""Corpus guard: no markdown link may name a file no filesystem holds.

The converter writes names Windows cannot hold only for a preserved
namespace or an article title it could not sanitise, and a rewrite leaves
alone what the name map says nothing about, so a bad destination survives
unless someone repairs it. This scans the text rather than the parsed
document, since a destination inside an HTML comment or a code span is
just as unusable once copied out.
"""

from pathlib import Path
from urllib.parse import unquote

from scripts.convert_wiki.ast_utils import _find_link_destination_ranges
from scripts.convert_wiki.markdown_rewrite import _ILLEGAL_NAME_CHARACTERS
from scripts.convert_wiki.stems import _UNUSABLE_STEMS

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


def _names_an_impossible_file(destination: str) -> bool:
    """Return whether a link destination names a file nothing can hold."""
    page = unquote(destination.partition("#")[0])
    if not page.endswith(".md"):
        return False
    name = page.rsplit("/", 1)[-1]
    return name in _UNUSABLE_STEMS or any(
        character in _ILLEGAL_NAME_CHARACTERS or character < " " for character in name
    )


def test_no_markdown_link_names_an_impossible_file() -> None:
    """Every link destination in the corpus can be a filename."""
    offenders: list[str] = []
    for path in sorted(Path("general").rglob("*.md")):
        if path.is_symlink():
            continue
        text = path.read_text(encoding="utf-8")
        for _start, _end, destination in _find_link_destination_ranges(text):
            if _names_an_impossible_file(destination):
                offenders.append(f"{path}: {destination}")
    assert offenders == []
