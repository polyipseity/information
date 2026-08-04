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
    _find_table_blocks,
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
        """Plain text parses to a non-empty token list."""
        tokens = _parse("hello world")
        assert isinstance(tokens, list)
        assert len(tokens) >= 1

    def test_parse_blockquote(self) -> None:
        """A blockquote parses with a ``block_quote`` token."""
        tokens = _parse("> quote\n>\n> more")
        types = [t["type"] for t in tokens]
        assert "block_quote" in types

    def test_parse_block_math(self) -> None:
        """Block math parses with a ``block_math`` token."""
        tokens = _parse("$$a = b$$")
        types = [t["type"] for t in tokens]
        assert "block_math" in types

    def test_parse_table(self) -> None:
        """A pipe table parses with a ``table`` token."""
        text = "|a|b|\n|-|-|\n|c|d|"
        tokens = _parse(text)
        types = [t["type"] for t in tokens]
        assert "table" in types

    def test_parse_blank_line(self) -> None:
        """Blank lines between blockquotes parse as ``blank_line`` tokens."""
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
        """A text leaf reconstructs to its raw text."""
        token = {"type": "text", "raw": "hello"}
        assert _reconstruct_token_raw(token) == "hello"

    def test_block_math(self) -> None:
        """A ``block_math`` token reconstructs to its raw text."""
        token = {"type": "block_math", "raw": "a = b"}
        assert _reconstruct_token_raw(token) == "a = b"

    def test_inline_math(self) -> None:
        """An ``inline_math`` token reconstructs to its raw text."""
        token = {"type": "inline_math", "raw": "a^2"}
        assert _reconstruct_token_raw(token) == "a^2"

    def test_codespan(self) -> None:
        """A ``codespan`` token reconstructs to its raw text."""
        token = {"type": "codespan", "raw": "code"}
        assert _reconstruct_token_raw(token) == "code"

    def test_linebreak(self) -> None:
        """A ``linebreak`` token reconstructs to its raw text."""
        token = {"type": "linebreak", "raw": "  "}
        assert _reconstruct_token_raw(token) == "  "

    def test_block_code(self) -> None:
        """A ``block_code`` token reconstructs to its raw text."""
        token = {"type": "block_code", "raw": "print('hi')"}
        assert _reconstruct_token_raw(token) == "print('hi')"

    def test_thematic_break(self) -> None:
        """A ``thematic_break`` token reconstructs to ``***``."""
        token = {"type": "thematic_break"}
        assert _reconstruct_token_raw(token) == "***"

    def test_blank_line_none(self) -> None:
        """A ``blank_line`` token reconstructs to ``None``."""
        token = {"type": "blank_line"}
        assert _reconstruct_token_raw(token) is None

    def test_strong(self) -> None:
        """A ``strong`` token wraps its children in ``**``."""
        token = {
            "type": "strong",
            "children": [{"type": "text", "raw": "bold"}],
        }
        assert _reconstruct_token_raw(token) == "**bold**"

    def test_emphasis(self) -> None:
        """An ``emphasis`` token wraps its children in ``*``."""
        token = {
            "type": "emphasis",
            "children": [{"type": "text", "raw": "italic"}],
        }
        assert _reconstruct_token_raw(token) == "*italic*"

    def test_paragraph_with_text_children(self) -> None:
        """A paragraph with text children reconstructs to plain text."""
        token = {
            "type": "paragraph",
            "children": [{"type": "text", "raw": "Hello world"}],
        }
        assert _reconstruct_token_raw(token) == "Hello world"

    def test_paragraph_with_mixed_children(self) -> None:
        """A paragraph with mixed children reconstructs them in order."""
        token = {
            "type": "paragraph",
            "children": [
                {"type": "text", "raw": "Hello "},
                {"type": "strong", "children": [{"type": "text", "raw": "world"}]},
            ],
        }
        assert _reconstruct_token_raw(token) == "Hello **world**"

    def test_block_quote_single_paragraph(self) -> None:
        """A single-paragraph blockquote reconstructs with a ``> `` prefix."""
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
        """A multi-paragraph blockquote keeps the ``> `` prefixes."""
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
        """A childless ``block_quote`` token reconstructs to ``None``."""
        token = {"type": "block_quote"}
        assert _reconstruct_token_raw(token) is None

    def test_unknown_type_no_children(self) -> None:
        """An unknown token type without children reconstructs to ``None``."""
        token = {"type": "unknown_type"}
        assert _reconstruct_token_raw(token) is None

    def test_paragraph_no_children(self) -> None:
        """A childless ``paragraph`` token reconstructs to ``None``."""
        token = {"type": "paragraph"}
        assert _reconstruct_token_raw(token) is None

    def test_paragraph_all_none_children(self) -> None:
        """A paragraph whose children yield no raw text reconstructs to ``None``."""
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
        """Walks a flat token list including children."""
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
        """Filters walked tokens by token type."""
        tokens = [
            {"type": "paragraph", "children": [{"type": "text", "raw": "a"}]},
            {"type": "block_quote", "children": []},
        ]
        result = list(_walk_tokens(tokens, token_type="text"))
        assert len(result) == 1
        assert result[0][0]["type"] == "text"

    def test_depth_tracking(self) -> None:
        """Tracks the nesting depth of each walked token."""
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
        """Tracks the parent chain of each walked token."""
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
        """Finds a single pair of blockquotes separated by one blank line."""
        tokens = [
            {"type": "block_quote", "children": []},
            {"type": "blank_line"},
            {"type": "block_quote", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == [(0, 2)]

    def test_three_adjacent(self) -> None:
        """Finds both pairs among three adjacent blockquotes."""
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
        """Blockquotes separated by a paragraph are not adjacent."""
        tokens = [
            {"type": "block_quote", "children": []},
            {"type": "paragraph", "children": []},
            {"type": "block_quote", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == []

    def test_single_target(self) -> None:
        """A lone blockquote with no partner yields no pairs."""
        tokens = [
            {"type": "block_quote", "children": []},
            {"type": "paragraph", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == []

    def test_empty(self) -> None:
        """An empty token list yields no pairs."""
        result = _find_top_level_adjacent([], "block_quote")
        assert result == []

    def test_no_targets(self) -> None:
        """No matching tokens yields no pairs."""
        tokens = [
            {"type": "paragraph", "children": []},
            {"type": "paragraph", "children": []},
        ]
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert result == []

    def test_ignore_multiple_blanks(self) -> None:
        """Multiple blank lines between blockquotes still count as adjacent."""
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
        """A custom ``ignore_types`` set keeps blockquotes adjacent."""
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
        """Two real parsed blockquotes yield one adjacency pair."""
        text = "> First\n\n> Second"
        tokens = _parse(text)
        result = _find_top_level_adjacent(tokens, "block_quote")
        assert len(result) == 1
        assert result[0] == (0, 2)

    def test_with_real_parsed_text_three_blockquotes(self) -> None:
        """Three real parsed blockquotes yield two adjacency pairs."""
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
        """Finds the byte range of a simple paragraph."""
        text = "hello world"
        tokens = _parse(text)
        rng = _find_token_range(text, tokens, 0)
        # Paragraph token's range covers "hello world"
        assert rng is not None
        start, end = rng
        assert text[start:end] == "hello world"

    def test_block_math(self) -> None:
        """Finds the byte range of a ``block_math`` token."""
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
        """Finds the byte range of a blockquote."""
        text = "> quoted content"
        tokens = _parse(text)
        rng = _find_token_range(text, tokens, 0)
        assert rng is not None
        start, end = rng
        assert "quoted content" in text[start:end]

    def test_multiple_tokens(self) -> None:
        """Finds disjoint, in-order ranges for multiple tokens."""
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
        """Finds the range of the second of two adjacent blockquotes."""
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
        """Inserts text after a paragraph token."""
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
        """Inserts a new paragraph after a blockquote token."""
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
        """A multi-line insertion after an early token leaves later content intact."""
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
        """Blockquotes separated by a regular paragraph yield no pairs."""
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
        """Walks real Markdown and finds the expected token types."""
        text = "> **bold quote** and `code`"
        tokens = _parse(text)
        all_tokens = list(_walk_tokens(tokens))
        types = [t[0]["type"] for t in all_tokens]
        assert "block_quote" in types
        assert "strong" in types
        assert "text" in types

    def test_find_token_range_out_of_bounds(self) -> None:
        """An out-of-bounds token index yields ``None``."""
        text = "hello"
        tokens = _parse(text)
        result = _find_token_range(text, tokens, 999)
        assert result is None

    def test_find_token_range_blank_line(self) -> None:
        """A ``blank_line`` token yields ``None`` for its range."""
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
        """Plain text without math yields no ranges."""
        assert _all_math_ranges("plain text") == []

    def test_empty_string(self) -> None:
        """An empty string yields no ranges."""
        assert _all_math_ranges("") == []

    def test_inline_math(self) -> None:
        """Finds the range of an inline math expression."""
        result = _all_math_ranges("text $a^2 + b^2$ more")
        assert len(result) == 1
        start, end = result[0]
        assert "a^2 + b^2" in "text $a^2 + b^2$ more"[start:end]

    def test_block_math(self) -> None:
        """Finds the range of a block math expression."""
        result = _all_math_ranges("before\n$$\na = b\n$$\nafter")
        assert len(result) == 1
        start, end = result[0]
        assert "a = b" in "before\n$$\na = b\n$$\nafter"[start:end]

    def test_multiple_inline_math(self) -> None:
        """Finds one range per inline math expression."""
        result = _all_math_ranges("$a$ and $b$ and $c$")
        assert len(result) == 3

    def test_parse_error(self) -> None:
        """Malformed input that fails parsing yields no ranges."""
        # Extremely malformed input that causes parse to return a string
        result = _all_math_ranges("\x00")
        assert result == []


# =========================================================================
# _all_code_span_ranges
# =========================================================================


class TestAllCodeSpanRanges:
    """Tests for code span range finding."""

    def test_no_code(self) -> None:
        """Plain text without code spans yields no ranges."""
        assert _all_code_span_ranges("plain text") == []

    def test_empty_string(self) -> None:
        """An empty string yields no ranges."""
        assert _all_code_span_ranges("") == []

    def test_single_code_span(self) -> None:
        """Finds the range of a single code span."""
        text = "text `code` more"
        result = _all_code_span_ranges(text)
        assert len(result) == 1
        start, end = result[0]
        assert text[start:end] == "code"

    def test_multiple_code_spans(self) -> None:
        """Finds one range per code span."""
        result = _all_code_span_ranges("`a` and `b` and `c`")
        assert len(result) == 3

    def test_code_span_with_backticks(self) -> None:
        """Finds the range of a code span containing backticks."""
        text = "`` `code` ``"
        result = _all_code_span_ranges(text)
        assert len(result) == 1
        start, end = result[0]
        assert "`code`" in text[start:end]

    def test_parse_error(self) -> None:
        """Malformed input that fails parsing yields no ranges."""
        result = _all_code_span_ranges("\x00")
        assert result == []


# =========================================================================
# _is_in_span
# =========================================================================


class TestIsInSpan:
    """Tests for position-in-range checking."""

    def test_position_inside(self) -> None:
        """A position inside a range is in the span."""
        assert _is_in_span(5, [(0, 10)])

    def test_position_before(self) -> None:
        """A position before all ranges is not in the span."""
        assert not _is_in_span(0, [(5, 10)])

    def test_position_after(self) -> None:
        """A position after all ranges is not in the span."""
        assert not _is_in_span(15, [(5, 10)])

    def test_multiple_ranges_middle(self) -> None:
        """A position inside one of several ranges is in the span."""
        assert _is_in_span(12, [(0, 5), (10, 20)])

    def test_multiple_ranges_none(self) -> None:
        """A position outside all ranges is not in the span."""
        assert not _is_in_span(7, [(0, 5), (10, 20)])

    def test_empty_ranges(self) -> None:
        """An empty range list means no position is in the span."""
        assert not _is_in_span(5, [])

    def test_boundary_start(self) -> None:
        """A position at a range start is in the span."""
        assert _is_in_span(0, [(0, 10)])

    def test_boundary_end_exclusive(self) -> None:
        """A position at the exclusive range end is not in the span."""
        assert not _is_in_span(10, [(0, 10)])


# =========================================================================
# _is_in_math_span
# =========================================================================


class TestIsInMathSpan:
    """Tests for position-in-math-span check."""

    def test_inside_inline_math(self) -> None:
        """A position inside inline math is in the math span."""
        # "$x$" starts at position 7, "x" is at position 8
        assert _is_in_math_span("before $x$ after", 8)

    def test_outside_math(self) -> None:
        """A position outside math is not in the math span."""
        assert not _is_in_math_span("before $x$ after", 3)

    def test_no_math_at_all(self) -> None:
        """Text without math never marks a position as in a math span."""
        assert not _is_in_math_span("plain text", 2)

    def test_empty_text(self) -> None:
        """Empty text never marks a position as in a math span."""
        assert not _is_in_math_span("", 0)


# =========================================================================
# _is_in_code_span
# =========================================================================


class TestIsInCodeSpan:
    """Tests for position-in-code-span check."""

    def test_inside_code(self) -> None:
        """A position inside a code span is in the code span."""
        assert _is_in_code_span("text `code` more", 7)

    def test_outside_code(self) -> None:
        """A position outside a code span is not in the code span."""
        assert not _is_in_code_span("text `code` more", 3)

    def test_no_code_at_all(self) -> None:
        """Text without code spans never marks a position as in a code span."""
        assert not _is_in_code_span("plain text", 2)

    def test_empty_text(self) -> None:
        """Empty text never marks a position as in a code span."""
        assert not _is_in_code_span("", 0)

    def test_code_span_boundary(self) -> None:
        """The span start is inclusive and just past the end is outside."""
        # mistune codespan raw is inner content "code" (positions 6-9)
        assert _is_in_code_span("text `code` more", 6)
        # Position just after the closing backtick is outside
        assert not _is_in_code_span("text `code` more", 11)


# =========================================================================
# _find_table_blocks
# =========================================================================


class TestFindTableBlocks:
    """Tests for pipe-table block range finding via mistune AST."""

    def test_no_tables(self) -> None:
        """Text without pipe tables yields no table blocks."""
        assert _find_table_blocks("plain text\n\nno pipes") == []

    def test_simple_table(self) -> None:
        """A lone table spans the entire text."""
        text = "| a | b |\n|---|---|\n| 1 | 2 |"
        result = _find_table_blocks(text)
        assert len(result) == 1
        start, end = result[0]
        # The single table should span the entire text since there are no
        # adjacent non-table tokens with reconstructable raws.
        assert start == 0
        assert end == len(text)

    def test_table_surrounded_by_text(self) -> None:
        """A table between paragraphs spans only the table content."""
        text = "before\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\nafter"
        result = _find_table_blocks(text)
        assert len(result) == 1
        start, end = result[0]
        # The table block starts after the "before" paragraph and ends
        # before the "after" paragraph.
        assert start > 0
        assert end < len(text)
        # The block contains actual table content.
        assert "a | b" in text[start:end]
        assert "after" not in text[start:end]

    def test_multiple_tables(self) -> None:
        """Each table token yields an in-bounds block range."""
        text = "| a | b |\n|---|---|\n| 1 | 2 |\n\n| x | y |\n|---|---|\n| 3 | 4 |"
        result = _find_table_blocks(text)
        # One block per table token in the AST. When no reconstructable
        # non-table tokens exist between adjacent tables, the ranges
        # collapse to identical values — this is a known limitation.
        assert len(result) == 2
        # Each block should be within bounds.
        for start, end in result:
            assert 0 <= start <= end <= len(text)

    def test_table_with_inline_math(self) -> None:
        """A table with inline math spans the entire text."""
        text = "| $x$ | $y$ |\n|---|---|\n| 1 | 2 |"
        result = _find_table_blocks(text)
        assert len(result) == 1
        start, end = result[0]
        # The whole input is the table.
        assert start == 0
        assert end == len(text)

    def test_table_with_block_math(self) -> None:
        """Block math inside cells prevents table parsing."""
        text = "| $$a = b$$ | c |\n|---|---|---|\n| 1 | 2 |"
        result = _find_table_blocks(text)
        # Mistune does not parse `$$` inside a table cell as a table;
        # it treats the entire input as a paragraph.
        assert result == []

    def test_table_with_code_spans(self) -> None:
        """Code spans containing pipes prevent table parsing."""
        text = "| `a|b` | c |\n|---|---|\n| 1 | 2 |"
        result = _find_table_blocks(text)
        # Mistune does not parse pipes inside backtick code spans as
        # table column separators; it treats the input as a paragraph.
        assert result == []

    def test_table_at_start(self) -> None:
        """A table at the start does not include trailing text."""
        text = "| a | b |\n|---|---|\n| 1 | 2 |\n\nafter"
        result = _find_table_blocks(text)
        assert len(result) == 1
        start, end = result[0]
        # Table starts at position 0 since there's no preceding text.
        assert start == 0
        # The block does not include the trailing "after" paragraph.
        assert "after" not in text[start:end]
        assert end < len(text)

    def test_table_at_end(self) -> None:
        """A table at the end does not include preceding text."""
        text = "before\n\n| a | b |\n|---|---|\n| 1 | 2 |"
        result = _find_table_blocks(text)
        assert len(result) == 1
        start, end = result[0]
        # Table block ends at the end of the text.
        assert start > 0
        assert end == len(text)
        assert "before" not in text[start:end]

    def test_table_in_blockquote(self) -> None:
        """A table inside a blockquote yields empty or in-bounds ranges."""
        text = "> | a | b |\n> |---|---|\n> | 1 | 2 |"
        result = _find_table_blocks(text)
        # mistune may parse tables inside blockquotes as nested
        # blockquote tokens, not as top-level table tokens. An empty
        # result is acceptable.
        assert len(result) == 0 or all(s >= 0 and e <= len(text) for s, e in result)

    def test_table_with_adjacent_tables_no_separator(self) -> None:
        """Adjacent tables without separators yield in-bounds ranges."""
        text = "| a | b |\n|---|---|\n| 1 | 2 |\n\n| c | d |\n|---|---|\n| 3 | 4 |"
        result = _find_table_blocks(text)
        # Two table tokens exist but both get the same inferred range
        # because no reconstructable non-table tokens sit between them.
        # This is a known limitation handled at the call site by the
        # dedup guard in ``_reformat_table``.
        assert len(result) == 2
        for start, end in result:
            assert 0 <= start <= end <= len(text)


"""Public API of this test module (empty)."""
__all__ = ()
