"""Unit tests for utility routines in the academic-notes checker.

These exercises verify core parsing helpers used by the validator.
"""

from os import PathLike

import pytest
from anyio import Path
from check_mods.utils import (
    ast_collect_text,
    ast_headings,
    ast_sections,
    filter_ast,
    get_excerpt,
    has_flash_tag,
    iter_ast,
    locate,
    locate_range,
    parse_frontmatter,
)

"""Public symbols exported by this module (none)."""
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


@pytest.mark.anyio
async def test_get_excerpt(tmp_path: PathLike[str]):
    """Exercise get_excerpt behaviour with a simple two-line file."""
    p = Path(tmp_path) / "file.md"
    await p.write_text("first line\nsecond line\nthird")
    excerpt, caret = await get_excerpt(p, "some message", line=2, col=1)
    assert "second line" in excerpt
    assert caret is not None


@pytest.mark.anyio
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


@pytest.mark.anyio
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


@pytest.mark.anyio
async def test_get_excerpt_file_missing(tmp_path: PathLike[str]):
    """get_excerpt should handle missing files gracefully."""
    p = Path(tmp_path) / "nope.md"
    # nonexistent file should return the placeholder rather than raise
    excerpt, caret = await get_excerpt(p, "msg", line=1, col=1)
    assert "no preview" in excerpt
    assert caret is None


# AST helper tests -----------------------------------------------------------

# Minimal AST node factories


def _text(raw: str) -> dict:
    return {"type": "text", "raw": raw}


def _heading(level: int, text: str) -> dict:
    return {
        "type": "heading",
        "attrs": {"level": level},
        "style": "atx",
        "children": [_text(text)],
    }


def _para(text: str) -> dict:
    return {"type": "paragraph", "children": [_text(text)]}


def _blank() -> dict:
    return {"type": "blank_line"}


def _list_item(text: str) -> dict:
    return {"type": "list_item", "children": [_text(text)]}


def _list(items: list[dict]) -> dict:
    return {"type": "list", "tight": True, "children": items}


class TestIterAst:
    """Exercises for iter_ast()."""

    def test_empty(self):
        assert list(iter_ast([])) == []

    def test_flat_list(self):
        nodes = [_heading(1, "A"), _para("hello")]
        result = list(iter_ast(nodes))
        # iter_ast recursively yields children, so heading + text + paragraph + text = 4
        assert len(result) == 4
        assert result[0]["type"] == "heading"
        assert result[1]["type"] == "text"
        assert result[2]["type"] == "paragraph"
        assert result[3]["type"] == "text"

    def test_nested_children(self):
        nested = _para("x")
        nested["children"].append({"type": "emphasis", "children": [_text("em")]})
        ast = [nested]
        result = list(iter_ast(ast))
        # paragraph -> text("x") -> emphasis -> text("em") = 4
        assert len(result) == 4
        assert result[0]["type"] == "paragraph"
        assert result[1]["type"] == "text"
        assert result[2]["type"] == "emphasis"
        assert result[3]["type"] == "text"


class TestFilterAst:
    """Exercises for filter_ast()."""

    def test_filter_heading(self):
        ast = [_heading(1, "A"), _para("x"), _heading(2, "B")]
        result = list(filter_ast(ast, "heading"))
        assert len(result) == 2
        assert all(n["type"] == "heading" for n in result)

    def test_filter_nonexistent(self):
        ast = [_para("x")]
        assert list(filter_ast(ast, "code")) == []


class TestAstCollectText:
    """Exercises for ast_collect_text()."""

    def test_plain_text(self):
        assert ast_collect_text(_text("hello")) == "hello"

    def test_heading_text(self):
        assert ast_collect_text(_heading(1, "Title")) == "Title"

    def test_paragraph_with_inline(self):
        para = {
            "type": "paragraph",
            "children": [
                _text("a "),
                {"type": "strong", "children": [_text("b")]},
                _text(" c"),
            ],
        }
        assert ast_collect_text(para) == "a b c"

    def test_nested_formatting(self):
        outer = {
            "type": "emphasis",
            "children": [{"type": "strong", "children": [_text("bold+italic")]}],
        }
        assert ast_collect_text(outer) == "bold+italic"


class TestAstHeadings:
    """Exercises for ast_headings()."""

    def test_no_headings(self):
        assert ast_headings([_para("x")]) == []

    def test_multiple_headings(self):
        ast = [_heading(1, "A"), _para("x"), _heading(2, "B"), _heading(3, "C")]
        heads = ast_headings(ast)
        assert len(heads) == 3
        assert heads[0] == {"type": "heading", "level": 1, "text": "A", "node": ast[0]}
        assert heads[1] == {"type": "heading", "level": 2, "text": "B", "node": ast[2]}
        assert heads[2] == {"type": "heading", "level": 3, "text": "C", "node": ast[3]}

    def test_heading_level_default(self):
        node = {"type": "heading", "children": [_text("X")]}
        heads = ast_headings([node])
        assert heads[0]["level"] == 1  # default


class TestAstSections:
    """Exercises for ast_sections()."""

    def test_empty(self):
        assert ast_sections([]) == []

    def test_preamble_only(self):
        sects = ast_sections([_para("a"), _para("b")])
        assert len(sects) == 1
        assert sects[0]["heading"] is None
        assert len(sects[0]["children"]) == 2

    def test_one_heading(self):
        sects = ast_sections([_heading(1, "A"), _para("body")])
        # First element is a heading, so no preamble section — just one section
        assert len(sects) == 1
        assert sects[0]["heading"] is not None
        assert ast_collect_text(sects[0]["heading"]) == "A"
        assert len(sects[0]["children"]) == 1
        assert sects[0]["children"][0]["type"] == "paragraph"

    def test_two_sections(self):
        ast = [_heading(1, "A"), _para("body a"), _heading(2, "B"), _para("body b")]
        sects = ast_sections(ast)
        assert len(sects) == 2
        assert ast_collect_text(sects[0]["heading"]) == "A"
        assert ast_collect_text(sects[1]["heading"]) == "B"
        assert len(sects[0]["children"]) == 1
        assert len(sects[1]["children"]) == 1

    def test_blank_lines_skipped(self):
        ast = [_heading(1, "A"), _blank(), _para("x")]
        sects = ast_sections(ast)
        assert len(sects) == 1  # header + content, blank skipped
        assert len(sects[0]["children"]) == 1
        assert sects[0]["children"][0]["type"] == "paragraph"

    def test_preamble_with_content(self):
        ast = [_para("preamble"), _heading(1, "A"), _para("body")]
        sects = ast_sections(ast)
        assert len(sects) == 2
        assert sects[0]["heading"] is None
        assert len(sects[0]["children"]) == 1
        assert sects[0]["children"][0] == ast[0]
        assert len(sects[1]["children"]) == 1
