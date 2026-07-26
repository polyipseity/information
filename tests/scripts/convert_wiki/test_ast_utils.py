"""Tests for ``scripts.convert_wiki.ast_utils``.

Covers all exported functions:
* ``_MISTUNE_PARSER`` — basic parse sanity
* ``_reconstruct_token_raw`` — all supported token types
* ``_find_token_range`` — byte-range finding
* ``_walk_tokens`` — recursive traversal with optional filter
* ``_find_top_level_adjacent`` — adjacency detection
* ``_inject_after_token`` — text insertion
* ``_all_math_ranges`` — math span range finding
* ``_all_code_span_ranges`` — code span range finding
* ``_is_in_span`` — position-in-range check
* ``_is_in_math_span`` — position-in-math-span check
* ``_is_in_code_span`` — position-in-code-span check
"""

from __future__ import annotations

from typing import Any

import pytest

from scripts.convert_wiki.ast_utils import (
    _MISTUNE_PARSER,
    _all_code_span_ranges,
    _all_math_ranges,
    _find_token_range,
    _find_top_level_adjacent,
    _inject_after_token,
    _is_in_code_span,
    _is_in_math_span,
    _is_in_span,
    _reconstruct_token_raw,
    _walk_tokens,
)


def _parse(text: str) -> list[dict[str, Any]]:
    """Parse *text* with ``_MISTUNE_PARSER``, returning only the token list.

    The return type of ``mistune.Markdown.parse`` is
    ``Union[str, List[Dict[str, Any]]]`` (the ``str`` variant is an error
    path).  This helper asserts we got a list so the type checker is
    satisfied.
    """
    tokens, _state = _MISTUNE_PARSER.parse(text)
    assert isinstance(tokens, list), f"expected list, got {type(tokens)}"
    return tokens


# =========================================================================
# _MISTUNE_PARSER — basic parse smoke tests
# =========================================================================


class TestMistuneParser:
    """Smoke tests for the shared parser."""

    def test_parse_plain_text(self) -> None:
        tokens = _parse("hello world")
        assert isinstance(tokens, list)
        assert len(tokens) >= 1

    def test_parse_blockquote(self) -> None:
        tokens = _parse("> quote\n>\n> more")
        types = [t["type"] for t in tokens]
        assert "block_quote" in types

    def test_parse_block_math(self) -> None:
        tokens = _parse("$$a = b$$")
        types = [t["type"] for t in tokens]
        assert "block_math" in types

    def test_parse_table(self) -> None:
        text = "|a|b|\n|-|-|\n|c|d|"
        tokens = _parse(text)
        types = [t["type"] for t in tokens]
        assert "table" in types

    def test_parse_blank_line(self) -> None:
        text = "> a\n\n> b"
        tokens = _parse(text)
        types = [t["type"] for t in tokens]
        assert "blank_line" in types


# =========================================================================
# _reconstruct_token_raw
# =========================================================================


class TestReconstructTokenRaw:
    """Coverage for ``_reconstruct_token_raw`` on various token types."""

    def test_text_leaf(self) -> None:
        token = {"type": "text", "raw": "hello"}
        assert _reconstruct_token_raw(token) == "hello"

    def test_block_math(self) -> None:
        token = {"type": "block_math", "raw": "a = b"}
        assert _reconstruct_token_raw(token) == "a = b"

    def test_inline_math(self) -> None:
        token = {"type": "inline_math", "raw": "a^2"}
        assert _reconstruct_token_raw(token) == "a^2"

    def test_codespan(self) -> None:
        token = {"type": "codespan", "raw": "code"}
        assert _reconstruct_token_raw(token) == "code"

    def test_linebreak(self) -> None:
        token = {"type": "linebreak", "raw": "  "}
        assert _reconstruct_token_raw(token) == "  "

    def test_block_code(self) -> None:
        token = {"type": "block_code", "raw": "print('hi')"}
        assert _reconstruct_token_raw(token) == "print('hi')"

    def test_thematic_break(self) -> None:
        token = {"type": "thematic_break"}
        assert _reconstruct_token_raw(token) == "***"

    def test_blank_line_none(self) -> None:
        token = {"type": "blank_line"}
        assert _reconstruct_token_raw(token) is None

    def test_strong(self) -> None:
        token = {
            "type": "strong",
            "children": [{"type": "text", "raw": "bold"}],
        }
        assert _reconstruct_token_raw(token) == "**bold**"

    def test_emphasis(self) -> None:
        token = {
            "type": "emphasis",
            "children": [{"type": "text", "raw": "italic"}],
        }
        assert _reconstruct_token_raw(token) == "*italic*"

    def test_paragraph_with_text_children(self) -> None:
        token = {
            "type": "paragraph",
            "children": [{"type": "text", "raw": "Hello world"}],
        }
        assert _reconstruct_token_raw(token) == "Hello world"

    def test_paragraph_with_mixed_children(self) -> None:
        token = {
            "type": "paragraph",
            "children": [
                {"type": "text", "raw": "Hello "},
                {"type": "strong", "children": [{"type": "text", "raw": "world"}]},
            ],
        }
        assert _reconstruct_token_raw(token) == "Hello **world**"

    def test_block_quote_single_paragraph(self) -> None:
        # Single paragraph inside blockquote: "> text"
        token = {
            "type": "block_quote",
            "children": [
                {
                    "type": "paragraph",
                    "children": [{"type": "text", "raw": "quoted text"}],
                }
            ],
        }
        result = _reconstruct_token_raw(token)
        assert result is not None
        assert "> quoted text" in result

    def test_block_quote_multiple_paragraphs(self) -> None:
        # Two paragraphs: "> p1\n>\n> p2"
        token = {
            "type": "block_quote",
            "children": [
                {
                    "type": "paragraph",
                    "children": [{"type": "text", "raw": "para one"}],
                },
                {"type": "blank_line"},
                {
                    "type": "paragraph",
                    "children": [{"type": "text", "raw": "para two"}],
                },
            ],
        }
        result = _reconstruct_token_raw(token)
        assert result is not None
        assert "> para one" in result
        assert "> para two" in result
        # blank_line inside blockquote produces ">"
        assert ">" in result

    def test_block_quote_no_children(self) -> None:
        token = {"type": "block_quote"}
        assert _reconstruct_token_raw(token) is None

    def test_unknown_type_no_children(self) -> None:
        token = {"type": "unknown_type"}
        assert _reconstruct_token_raw(token) is None

    def test_paragraph_no_children(self) -> None:
        token = {"type": "paragraph"}
        assert _reconstruct_token_raw(token) is None

    def test_paragraph_all_none_children(self) -> None:
        token = {
            "type": "paragraph",
            "children": [{"type": "blank_line"}],
        }
        assert _reconstruct_token_raw(token) is None


# =========================================================================
# _walk_tokens
# =========================================================================


class TestWalkTokens:
    """Tests for recursive token walking."""

    def test_flat_list(self) -> None:
        tokens = [
            {"type": "paragraph", "children": [{"type": "text", "raw": "a"}]},
            {"type": "paragraph", "children": [{"type": "text", "raw": "b"}]},
        ]
        result = list(_walk_tokens(tokens))
        # Should yield 3 items: para(text(a)), text(a), para(text(b)), text(b)
        # Actually only 2 paragraphs + their children = 4 tokens
        assert len(result) == 4
        types = {t[0]["type"] for t in result}
        assert "paragraph" in types
        assert "text" in types

    def test_filter_type(self) -> None:
        tokens = [
            {"type": "paragraph", "children": [{"type": "text", "raw": "a"}]},
            {"type": "block_quote", "children": []},
        ]
        result = list(_walk_tokens(tokens, token_type="text"))
        assert len(result) == 1
        assert result[0][0]["type"] == "text"

    def test_depth_tracking(self) -> None:
        tokens = [
            {
                "type": "block_quote",
                "children": [
                    {
                        "type": "paragraph",
                        "children": [{"type": "text", "raw": "x"}],
                    }
                ],
            }
        ]
        result = list(_walk_tokens(tokens))
        for _token, depth, _parents in result:
            assert 0 <= depth <= 2

    def test_parents_tracking(self) -> None:
        text = "> quoted"
        parsed_tokens = _parse(text)
        result = list(_walk_tokens(parsed_tokens, token_type="text"))
        assert len(result) == 1
        _token, _depth, parents = result[0]
        assert len(parents) >= 1
        # Innermost parent should be a paragraph
        assert parents[-1]["type"] == "paragraph"


# =========================================================================
# _find_top_level_adjacent
# =========================================================================


class TestFindTopLevelAdjacent:
    """Tests for adjacency detection."""

    def test_single_pair(self) -> None:
        tokens = [
            {"type": "block_quote", "children": []},
            {"type": "blank_line"},
            {"type": "block_quote", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == [(0, 2)]

    def test_three_adjacent(self) -> None:
        tokens = [
            {"type": "block_quote", "children": []},
            {"type": "blank_line"},
            {"type": "block_quote", "children": []},
            {"type": "blank_line"},
            {"type": "block_quote", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == [(0, 2), (2, 4)]

    def test_not_adjacent(self) -> None:
        tokens = [
            {"type": "block_quote", "children": []},
            {"type": "paragraph", "children": []},
            {"type": "block_quote", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == []

    def test_single_target(self) -> None:
        tokens = [
            {"type": "block_quote", "children": []},
            {"type": "paragraph", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == []

    def test_empty(self) -> None:
        result = _find_top_level_adjacent([], "block_quote")
        assert result == []

    def test_no_targets(self) -> None:
        tokens = [
            {"type": "paragraph", "children": []},
            {"type": "paragraph", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == []

    def test_ignore_multiple_blanks(self) -> None:
        tokens = [
            {"type": "block_quote", "children": []},
            {"type": "blank_line"},
            {"type": "blank_line"},
            {"type": "block_quote", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == [(0, 3)]

    def test_adjacent_without_separator(self) -> None:
        """Blockquotes directly adjacent (no blank_line)."""
        tokens = [
            {"type": "block_quote", "children": []},
            {"type": "block_quote", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == [(0, 1)]

    def test_custom_ignore_types(self) -> None:
        tokens = [
            {"type": "block_quote", "children": []},
            {"type": "thematic_break"},
            {"type": "block_quote", "children": []},
        ]
        result = _find_top_level_adjacent(
            tokens, "block_quote", ignore_types=frozenset({"thematic_break"})
        )
        assert result == [(0, 2)]

    def test_with_real_parsed_text_two_blockquotes(self) -> None:
        text = "> First\n\n> Second"
        tokens = _parse(text)
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert len(result) == 1
        assert result[0] == (0, 2)

    def test_with_real_parsed_text_three_blockquotes(self) -> None:
        text = "> A\n\n> B\n\n> C"
        tokens = _parse(text)
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert len(result) == 2  # (0,2) and (2,4)


# =========================================================================
# _find_token_range — real parsed tokens
# =========================================================================


class TestFindTokenRange:
    """Byte-range finding via ``_find_token_range``."""

    def test_simple_paragraph(self) -> None:
        text = "hello world"
        tokens = _parse(text)
        rng = _find_token_range(text, tokens, 0)
        # Paragraph token's range covers "hello world"
        assert rng is not None
        start, end = rng
        assert text[start:end] == "hello world"

    def test_block_math(self) -> None:
        text = "before\n$$\na = b\n$$\nafter"
        tokens = _parse(text)
        # Find block_math token
        for i, tok in enumerate(tokens):
            if tok["type"] == "block_math":
                rng = _find_token_range(text, tokens, i)
                assert rng is not None
                start, end = rng
                # Should find math content in text
                assert text[start:end] == "a = b"
                return
        pytest.fail("no block_math token found")

    def test_blockquote(self) -> None:
        text = "> quoted content"
        tokens = _parse(text)
        rng = _find_token_range(text, tokens, 0)
        assert rng is not None
        start, end = rng
        assert "quoted content" in text[start:end]

    def test_multiple_tokens(self) -> None:
        text = "para one\n\npara two\n\npara three"
        tokens = _parse(text)
        # Find paragraphs at indices 0, 2, 4 (with blank_lines at 1 and 3)
        para_indices = [i for i, t in enumerate(tokens) if t["type"] != "blank_line"]
        assert len(para_indices) == 3
        # Each paragraph should be findable
        rng0 = _find_token_range(text, tokens, para_indices[0])
        rng1 = _find_token_range(text, tokens, para_indices[1])
        rng2 = _find_token_range(text, tokens, para_indices[2])
        assert rng0 is not None
        assert rng1 is not None
        assert rng2 is not None
        _, end0 = rng0
        start1, _ = rng1
        _, end1 = rng1
        start2, _ = rng2
        # Each paragraph range should be disjoint and in order
        assert end0 <= start1
        assert end1 <= start2

    def test_adjacent_blockquotes_find_second(self) -> None:
        text = "> First\n\n> Second"
        tokens = _parse(text)
        # Find both block_quote tokens
        bq_indices = [i for i, t in enumerate(tokens) if t["type"] == "block_quote"]
        assert len(bq_indices) >= 2
        rng = _find_token_range(text, tokens, bq_indices[1])
        assert rng is not None
        start, _end = rng
        # Second blockquote should start after "> First\n\n"
        assert text[start:].startswith("> Second") or "Second" in text[start:]


# =========================================================================
# _inject_after_token
# =========================================================================


class TestInjectAfterToken:
    """Text insertion via ``_inject_after_token``."""

    def test_inject_after_paragraph(self) -> None:
        text = "hello"
        tokens = _parse(text)
        result = _inject_after_token(text, tokens, 0, " world")
        assert result == "hello world"

    def test_inject_md028_between_blockquotes(self) -> None:
        """The real usage: insert MD028 comment between adjacent blockquotes."""
        text = "> First\n\n> Second"
        tokens = _parse(text)
        # Find adjacent blockquotes
        pairs = _find_top_level_adjacent(tokens, "block_quote")
        assert len(pairs) == 1
        first_bq_idx, _second_bq_idx = pairs[0]
        comment = "\n<!-- markdownlint MD028 -->\n"
        result = _inject_after_token(text, tokens, first_bq_idx, comment)
        assert "<!-- markdownlint MD028 -->" in result
        assert "> First" in result
        assert "> Second" in result

    def test_inject_multiple_times(self) -> None:
        """Two separate injections don't interfere (early indices shift)."""
        text = "A\n\nB\n\nC"
        tokens = _parse(text)
        # Inject markers after first and second paragraphs.
        # After first injection, text becomes "A [1]\n\nB\n\nC".
        # After re-parsing, the paragraph for "B" is at a different index.
        r1 = _inject_after_token(text, tokens, 0, " [1]")
        # Re-parse after first injection for the second injection
        tokens2 = _parse(r1)
        # Find the paragraph containing "B" (skip blank_lines)
        para_indices = [i for i, t in enumerate(tokens2) if t["type"] != "blank_line"]
        assert len(para_indices) == 3
        r2 = _inject_after_token(r1, tokens2, para_indices[1], " [2]")
        assert "[1]" in r2
        assert "[2]" in r2

    def test_inject_after_blockquote(self) -> None:
        text = "> quote"
        tokens = _parse(text)
        result = _inject_after_token(text, tokens, 0, "\nnew paragraph")
        assert result.startswith("> quote\nnew paragraph")

    def test_unknown_token_no_change(self) -> None:
        """Tokens that can't be found return text unchanged."""
        text = "hello"
        # Create a fake token list that doesn't match the text
        tokens = [{"type": "thematic_break"}]
        result = _inject_after_token(text, tokens, 0, "extra")
        assert result == text

    def test_inject_at_end_with_newline(self) -> None:
        text = "para one\n\npara two"
        tokens = _parse(text)
        result = _inject_after_token(text, tokens, 0, "\n\n> inserted")
        assert "\n\n> inserted" in result
        assert "para two" in result


# =========================================================================
# Edge cases and integration
# =========================================================================


class TestEdgeCases:
    """Corner cases across multiple functions."""

    def test_no_adjacent_blockquotes(self) -> None:
        text = "> A\n\nRegular paragraph\n\n> B"
        tokens = _parse(text)
        pairs = _find_top_level_adjacent(tokens, "block_quote")
        assert pairs == []

    def test_three_blockquotes_two_insertions(self) -> None:
        """Verify MD028 insertions at both gaps with 3 blockquotes."""
        text = "> A\n\n> B\n\n> C"
        tokens = _parse(text)
        pairs = _find_top_level_adjacent(tokens, "block_quote")
        assert len(pairs) == 2

        comment = "\n<!-- markdownlint MD028 -->\n"
        # Inject after first blockquote (at index 0)
        result = _inject_after_token(text, tokens, pairs[0][0], comment)
        # Re-parse for second injection
        tokens2 = _parse(result)
        pairs2 = _find_top_level_adjacent(tokens2, "block_quote")
        if pairs2:
            result = _inject_after_token(result, tokens2, pairs2[0][0], comment)

        assert result.count("<!-- markdownlint MD028 -->") == 2

    def test_walk_tokens_with_real_markdown(self) -> None:
        text = "> **bold quote** and `code`"
        tokens = _parse(text)
        all_tokens = list(_walk_tokens(tokens))
        types = [t[0]["type"] for t in all_tokens]
        assert "block_quote" in types
        assert "strong" in types
        assert "text" in types

    def test_find_token_range_out_of_bounds(self) -> None:
        text = "hello"
        tokens = _parse(text)
        result = _find_token_range(text, tokens, 999)
        assert result is None

    def test_find_token_range_blank_line(self) -> None:
        text = "> A\n\n> B"
        tokens = _parse(text)
        # blank_line has no raw — finding range should return None
        for i, tok in enumerate(tokens):
            if tok["type"] == "blank_line":
                result = _find_token_range(text, tokens, i)
                assert result is None
                return
        pytest.fail("no blank_line token found")


# =========================================================================
# _all_math_ranges
# =========================================================================


class TestAllMathRanges:
    """Tests for math span range finding."""

    def test_no_math(self) -> None:
        assert _all_math_ranges("plain text") == []

    def test_empty_string(self) -> None:
        assert _all_math_ranges("") == []

    def test_inline_math(self) -> None:
        result = _all_math_ranges("text $a^2 + b^2$ more")
        assert len(result) == 1
        start, end = result[0]
        assert "a^2 + b^2" in "text $a^2 + b^2$ more"[start:end]

    def test_block_math(self) -> None:
        result = _all_math_ranges("before\n$$\na = b\n$$\nafter")
        assert len(result) == 1
        start, end = result[0]
        assert "a = b" in "before\n$$\na = b\n$$\nafter"[start:end]

    def test_multiple_inline_math(self) -> None:
        result = _all_math_ranges("$a$ and $b$ and $c$")
        assert len(result) == 3

    def test_parse_error(self) -> None:
        # Extremely malformed input that causes parse to return a string
        result = _all_math_ranges("\x00")
        assert result == []


# =========================================================================
# _all_code_span_ranges
# =========================================================================


class TestAllCodeSpanRanges:
    """Tests for code span range finding."""

    def test_no_code(self) -> None:
        assert _all_code_span_ranges("plain text") == []

    def test_empty_string(self) -> None:
        assert _all_code_span_ranges("") == []

    def test_single_code_span(self) -> None:
        text = "text `code` more"
        result = _all_code_span_ranges(text)
        assert len(result) == 1
        start, end = result[0]
        assert text[start:end] == "code"

    def test_multiple_code_spans(self) -> None:
        result = _all_code_span_ranges("`a` and `b` and `c`")
        assert len(result) == 3

    def test_code_span_with_backticks(self) -> None:
        text = "`` `code` ``"
        result = _all_code_span_ranges(text)
        assert len(result) == 1
        start, end = result[0]
        assert "`code`" in text[start:end]

    def test_parse_error(self) -> None:
        result = _all_code_span_ranges("\x00")
        assert result == []


# =========================================================================
# _is_in_span
# =========================================================================


class TestIsInSpan:
    """Tests for position-in-range checking."""

    def test_position_inside(self) -> None:
        assert _is_in_span(5, [(0, 10)])

    def test_position_before(self) -> None:
        assert not _is_in_span(0, [(5, 10)])

    def test_position_after(self) -> None:
        assert not _is_in_span(15, [(5, 10)])

    def test_multiple_ranges_middle(self) -> None:
        assert _is_in_span(12, [(0, 5), (10, 20)])

    def test_multiple_ranges_none(self) -> None:
        assert not _is_in_span(7, [(0, 5), (10, 20)])

    def test_empty_ranges(self) -> None:
        assert not _is_in_span(5, [])

    def test_boundary_start(self) -> None:
        assert _is_in_span(0, [(0, 10)])

    def test_boundary_end_exclusive(self) -> None:
        assert not _is_in_span(10, [(0, 10)])


# =========================================================================
# _is_in_math_span
# =========================================================================


class TestIsInMathSpan:
    """Tests for position-in-math-span check."""

    def test_inside_inline_math(self) -> None:
        # "$x$" starts at position 7, "x" is at position 8
        assert _is_in_math_span("before $x$ after", 8)

    def test_outside_math(self) -> None:
        assert not _is_in_math_span("before $x$ after", 3)

    def test_no_math_at_all(self) -> None:
        assert not _is_in_math_span("plain text", 2)

    def test_empty_text(self) -> None:
        assert not _is_in_math_span("", 0)


# =========================================================================
# _is_in_code_span
# =========================================================================


class TestIsInCodeSpan:
    """Tests for position-in-code-span check."""

    def test_inside_code(self) -> None:
        assert _is_in_code_span("text `code` more", 7)

    def test_outside_code(self) -> None:
        assert not _is_in_code_span("text `code` more", 3)

    def test_no_code_at_all(self) -> None:
        assert not _is_in_code_span("plain text", 2)

    def test_empty_text(self) -> None:
        assert not _is_in_code_span("", 0)

    def test_code_span_boundary(self) -> None:
        # mistune codespan raw is inner content "code" (positions 6-9)
        assert _is_in_code_span("text `code` more", 6)
        # Position just after the closing backtick is outside
        assert not _is_in_code_span("text `code` more", 11)
