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


@pytest.mark.asyncio
async def test_get_excerpt_latex_delimiter_shows_next_line(tmp_path: PathLike[str]):
    """If the target line is just "$" or "$$", show the following math.

    The caret should still point at column 1 of the snippet.
    """
    p = Path(tmp_path) / "file.md"
    await p.write_text("$\nmath\n")
    excerpt, caret = await get_excerpt(p, "math msg", line=1, col=1)
    assert excerpt.strip() == "math"
    # caret should span the entire snippet (length of 'math' == 4)
    assert caret.strip() == "^" * len(excerpt.strip())


@pytest.mark.asyncio
async def test_get_excerpt_caret_clamped(tmp_path: PathLike[str]):
    """Caret width should never exceed the displayed snippet length.

    Construct a very long line and request an excerpt with a tiny
    `chars` limit.  The computed width (col_end-col+1) will be larger than
    the available display window, but the caret must be clamped so it does
    not overflow or misalign.
    """
    p = Path(tmp_path) / "file.md"
    # make a long line (120 characters)
    await p.write_text("x" * 120 + "\n")
    # choose a column far to the right with an even farther col_end
    excerpt, caret = await get_excerpt(
        p,
        "msg",
        line=1,
        col=90,
        col_end=115,
        chars=20,
    )
    assert caret is not None
    # caret length should not exceed excerpt length
    assert caret.count("^") <= len(excerpt)
    # caret should start within the excerpt
    assert len(caret) == len(caret.rstrip())


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


def test_locate_range_multiline():
    """When the span crosses a newline col_end is capped at the first line.

    This guards against the oversized caret issue reported for
    ``latex_single_line`` where the dollar-sign match spanned three lines.
    """
    text = "$\nfoo\n$"
    start = 0
    length = len(text)
    # newline occurs at index 1, so col_end should be 1 (start column +0)
    assert locate_range(text, start, length) == (1, 1, 1)


@pytest.mark.asyncio
async def test_get_excerpt_file_missing(tmp_path: PathLike[str]):
    """get_excerpt should handle missing files gracefully."""
    p = Path(tmp_path) / "nope.md"
    # nonexistent file should return the placeholder rather than raise
    excerpt, caret = await get_excerpt(p, "msg", line=1, col=1)
    assert "no preview" in excerpt
    assert caret is None
