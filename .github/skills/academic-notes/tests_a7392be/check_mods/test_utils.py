"""Unit tests for utility routines in the academic-notes checker.

These exercises verify core parsing helpers used by the validator.
"""

from os import PathLike

import pytest
from anyio import Path
from check_mods.utils import (
    get_excerpt,
    has_flash_tag,
    locate,
    locate_range,
    parse_frontmatter,
)

__all__ = ()


def test_parse_frontmatter():
    """Verify parse_frontmatter returns expected YAML body or None."""
    sample = """---\naliases: [foo]\ntags: [bar]\n---\nHello"""
    assert parse_frontmatter(sample) == "aliases: [foo]\ntags: [bar]"
    assert parse_frontmatter("no frontmatter here") is None


def test_has_flash_tag():
    """Flash tag detection should catch known prefix and ignore others."""
    assert has_flash_tag("tags: [flashcard/active/special/academia/foo]")
    assert not has_flash_tag("tags: [something else]")


def test_locate_helpers():
    """Basic sanity checks for locate() and locate_range()."""
    text = "line1\nline2\n"
    assert locate(text, 0) == (1, 1)
    assert locate(text, 6) == (2, 1)
    assert locate_range(text, 6, 3) == (2, 1, 3)


@pytest.mark.asyncio
async def test_get_excerpt(tmp_path: PathLike[str]):
    """Exercise get_excerpt behaviour with a simple two-line file."""
    p = Path(tmp_path) / "file.md"
    await p.write_text("first line\nsecond line\nthird")
    excerpt, caret = await get_excerpt(p, "some message", line=2, col=1)
    assert "second line" in excerpt
    assert caret is not None


def test_parse_frontmatter_none_and_malformed():
    """Ensure parser handles missing or invalid frontmatter gracefully."""
    assert parse_frontmatter("") is None
    # malformed frontmatter should simply return content between delimiters
    sample = "---\nnot yaml: [\n---\n"
    # carriage return/newline variations may exist; compare stripped
    assert parse_frontmatter(sample).strip() == "not yaml: ["


def test_has_flash_tag_false():
    """has_flash_tag should not false-positive on unrelated tags."""
    assert not has_flash_tag("tags: [flashcard/sky]")


def test_locate_range_boundaries():
    """locate_range should report sane coordinates at boundaries."""
    txt = "abc\ndef\n"
    # range covering both characters
    # the end column is computed as start+length-1
    assert locate_range(txt, 0, 2) == (1, 1, 2)
    # beyond end should still provide sensible values
    assert locate_range(txt, len(txt), 1) == (3, 1, 1)


@pytest.mark.asyncio
async def test_get_excerpt_file_missing(tmp_path: PathLike[str]):
    """get_excerpt should handle missing files gracefully."""
    p = Path(tmp_path) / "nope.md"
    # nonexistent file should return the placeholder rather than raise
    excerpt, caret = await get_excerpt(p, "msg", line=1, col=1)
    assert "no preview" in excerpt
    assert caret is None
