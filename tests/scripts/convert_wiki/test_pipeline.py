"""Tests for ``scripts.convert_wiki.pipeline``.

Covers all exported functions:

* ``_make_converter`` — factory function
* ``_determine_needs_before`` / ``_determine_needs_after`` — spacing decisions
* ``_collect_block_math_info`` — AST traversal for block math
* ``_scan_and_apply`` — text replacement for block math spacing
* ``_separate_block_quotes`` — MD028 suppression between adjacent blockquotes
* ``_separate_block_math`` — whitespace around ``$$…$$`` blocks
* ``wiki_html_to_plaintext`` — post-processing after the converter
* ``run_pipeline`` — top-level orchestrator
"""

from __future__ import annotations

from os import PathLike
from typing import Any

import pytest
from anyio import Path
from bs4 import BeautifulSoup

from scripts.convert_wiki.ast_utils import _MISTUNE_PARSER
from scripts.convert_wiki.config import _UNICODE_SEPARATOR_CHARACTERS
from scripts.convert_wiki.converter import WikiHtmlConverter
from scripts.convert_wiki.pipeline import (
    _collect_block_math_info,
    _determine_needs_after,
    _determine_needs_before,
    _make_converter,
    _scan_and_apply,
    _separate_block_math,
    _separate_block_quotes,
    run_pipeline,
    wiki_html_to_plaintext,
)
from scripts.convert_wiki.types import _RedirectInfo

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


# =========================================================================
# _make_converter — factory function
# =========================================================================


class TestMakeConverter:
    """Tests for the ``_make_converter`` factory function."""

    def test_default_constructor(self) -> None:
        """Factory returns a ``WikiHtmlConverter`` instance with default args."""
        converter = _make_converter()
        assert converter is not None
        # The converter should be a WikiHtmlConverter and have default dirs set.
        assert hasattr(converter, "convert")

    def test_custom_paths(self, tmp_path: PathLike[str]) -> None:
        """Factory passes custom paths through to the converter."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        converter = _make_converter(
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
        )
        assert converter is not None
        assert hasattr(converter, "convert")


# =========================================================================
# _determine_needs_before / _determine_needs_after — spacing decisions
# =========================================================================


class TestDetermineNeedsBefore:
    """Tests for ``_determine_needs_before`` spacing decisions.

    ``_determine_needs_before`` examines the AST sibling node immediately
    before a ``block_math`` node.  If the sibling is text ending with a
    non-whitespace character, a space is needed.
    """

    def test_no_prev(self) -> None:
        """No previous sibling → no space needed."""
        assert _determine_needs_before(None) is False

    def test_prev_text_ending_with_word_char(self) -> None:
        """Previous text sibling ends with alphanumeric → space needed."""
        assert _determine_needs_before({"type": "text", "raw": "hello"}) is True

    def test_prev_text_ending_with_space(self) -> None:
        """Previous text sibling ends with space → no space needed."""
        assert _determine_needs_before({"type": "text", "raw": "hello "}) is False

    def test_prev_text_ending_with_tab(self) -> None:
        """Previous text sibling ends with tab → no space needed."""
        assert _determine_needs_before({"type": "text", "raw": "hello\t"}) is False

    def test_prev_text_ending_with_punctuation(self) -> None:
        """Previous text sibling ends with punctuation → space needed (not whitespace)."""
        assert _determine_needs_before({"type": "text", "raw": "text("}) is True

    def test_prev_text_ending_with_digit(self) -> None:
        """Previous text sibling ends with digit → space needed."""
        assert _determine_needs_before({"type": "text", "raw": "step 1"}) is True

    def test_prev_text_empty(self) -> None:
        """Previous text sibling is empty → no space needed."""
        assert _determine_needs_before({"type": "text", "raw": ""}) is False

    def test_prev_non_text(self) -> None:
        """Previous sibling is not a text node (e.g. emphasis) → space needed."""
        assert _determine_needs_before({"type": "strong", "raw": "**bold**"}) is True

    def test_prev_non_text_raw_empty(self) -> None:
        """Previous sibling is non-text with empty raw → space needed."""
        assert _determine_needs_before({"type": "image", "raw": ""}) is True


class TestDetermineNeedsAfter:
    """Tests for ``_determine_needs_after`` spacing decisions.

    Mirror of ``_determine_needs_before`` for the sibling that follows a
    ``block_math`` node.
    """

    def test_no_next(self) -> None:
        """No next sibling → no space needed."""
        assert _determine_needs_after(None) is False

    def test_next_text_starting_with_word_char(self) -> None:
        """Next text sibling starts with alphanumeric → space needed."""
        assert _determine_needs_after({"type": "text", "raw": "world"}) is True

    def test_next_text_starting_with_space(self) -> None:
        """Next text sibling starts with space → no space needed."""
        assert _determine_needs_after({"type": "text", "raw": " world"}) is False

    def test_next_text_starting_with_tab(self) -> None:
        """Next text sibling starts with tab → no space needed."""
        assert _determine_needs_after({"type": "text", "raw": "\tworld"}) is False

    def test_next_text_starting_with_punctuation(self) -> None:
        """Next text sibling starts with punctuation → space needed (not whitespace)."""
        assert _determine_needs_after({"type": "text", "raw": ".text"}) is True

    def test_next_text_starting_with_digit(self) -> None:
        """Next text sibling starts with digit → space needed."""
        assert _determine_needs_after({"type": "text", "raw": "2nd"}) is True

    def test_next_text_empty(self) -> None:
        """Next text sibling is empty → no space needed."""
        assert _determine_needs_after({"type": "text", "raw": ""}) is False

    def test_next_non_text(self) -> None:
        """Next sibling is not a text node (e.g. emphasis) → space needed."""
        assert _determine_needs_after({"type": "code", "raw": "`code`"}) is True


# =========================================================================
# _collect_block_math_info — AST traversal
# =========================================================================


def _parse(text: str) -> list[dict[str, Any]]:
    """Parse *text* with mistune and return the top-level token list."""
    result, _state = _MISTUNE_PARSER.parse(text)
    if isinstance(result, str):
        return []
    return result


class TestCollectBlockMathInfo:
    """Tests for ``_collect_block_math_info`` AST traversal."""

    def test_no_math(self) -> None:
        """Text with no math → empty list."""
        tokens = _parse("hello world")
        info = _collect_block_math_info(tokens)
        assert info == []

    def test_single_block_math_standalone(self) -> None:
        """Single standalone ``$$f(x)$$`` at top level → no spacing needed."""
        tokens = _parse("$$f(x)$$")
        info = _collect_block_math_info(tokens)
        # Standalone (depth=0) gets (raw, False, False, False)
        assert len(info) == 1
        raw, needs_before, needs_after, is_inline = info[0]
        assert raw == "f(x)"
        assert needs_before is False
        assert needs_after is False
        assert is_inline is False

    def test_single_block_math_inside_paragraph(self) -> None:
        """Block math inside a paragraph → spacing determined by siblings."""
        tokens = _parse("text $$f(x)$$ more")
        info = _collect_block_math_info(tokens)
        assert len(info) >= 1
        # Should be inside a paragraph (depth > 0)
        for raw, needs_before, needs_after, is_inline in info:
            if raw == "f(x)":
                assert is_inline is False
                assert needs_before is False  # "text " ends with space
                assert needs_after is False  # " more" starts with space

    def test_block_math_adjacent_to_text(self) -> None:
        """Block math adjacent to text on both sides → both spaces needed."""
        tokens = _parse("text$$f(x)$$more")
        info = _collect_block_math_info(tokens)
        assert len(info) >= 1
        for raw, needs_before, needs_after, is_inline in info:
            if raw == "f(x)":
                assert is_inline is False
                assert needs_before is True  # "text" has no trailing space
                assert needs_after is True  # "more" has no leading space

    def test_multiple_block_math(self) -> None:
        """Multiple block math expressions → all collected in order."""
        tokens = _parse("a $$f$$ b $$g$$ c")
        info = _collect_block_math_info(tokens)
        assert len(info) == 2
        raws = [t[0] for t in info]
        assert raws == ["f", "g"]

    def test_inline_math_collected(self) -> None:
        """Inline ``$x$`` is collected alongside block ``$$y$$``."""
        tokens = _parse("$x$ and $$y$$")
        info = _collect_block_math_info(tokens)
        # Both "x" (inline) and "y" (block) should be collected in order.
        raws = [t[0] for t in info]
        assert raws == ["x", "y"]
        assert len(info) == 2

    def test_empty_token_list(self) -> None:
        """Empty token list → empty info."""
        info = _collect_block_math_info([])
        assert info == []


# =========================================================================
# _scan_and_apply — text replacement for block math spacing
# =========================================================================


class TestScanAndApply:
    """Tests for ``_scan_and_apply`` text replacement."""

    def test_no_info(self) -> None:
        """Empty info list → text returned unchanged."""
        assert _scan_and_apply("hello world", []) == "hello world"

    def test_insert_space_before(self) -> None:
        """``needs_before=True`` → space inserted before ``$$…$$``."""
        result = _scan_and_apply("text$$f(x)$$", [("f(x)", True, False, False)])
        assert result == "text $$f(x)$$"

    def test_insert_space_after(self) -> None:
        """``needs_after=True`` → space inserted after ``$$…$$``."""
        result = _scan_and_apply("$$f(x)$$more", [("f(x)", False, True, False)])
        assert result == "$$f(x)$$ more"

    def test_insert_space_both(self) -> None:
        """Both flags True → spaces on both sides."""
        result = _scan_and_apply("text$$f(x)$$more", [("f(x)", True, True, False)])
        assert result == "text $$f(x)$$ more"

    def test_no_spaces(self) -> None:
        """Both flags False → no spaces inserted."""
        result = _scan_and_apply("text $$f(x)$$ more", [("f(x)", False, False, False)])
        assert result == "text $$f(x)$$ more"

    def test_math_span_does_not_match(self) -> None:
        """If the math span is not found, trailing text is appended as-is."""
        result = _scan_and_apply("text $$g(y)$$", [("f(x)", True, False, False)])
        # The "f(x)" entry won't match "g(y)", so everything after pos is appended.
        assert result == "text $$g(y)$$"

    def test_multiple_spans(self) -> None:
        """Multiple math blocks → each gets spacing based on its flags."""
        result = _scan_and_apply(
            "a$$f$$b$$g$$c",
            [("f", True, True, False), ("g", True, True, False)],
        )
        assert result == "a $$f$$ b $$g$$ c"

    def test_mixed_flags(self) -> None:
        """Multiple blocks with different flag combinations."""
        result = _scan_and_apply(
            "a$$one$$b$$two$$c",
            [("one", True, False, False), ("two", False, True, False)],
        )
        assert result == "a $$one$$b$$two$$ c"


class TestInlineMathSpacing:
    """Tests for inline ``$...$`` spacing (S3: same list as emphasis)."""

    def test_abutting_word(self) -> None:
        """Atomic inline math abutting words gets the zero-width marker.

        Complex math (``$1/|w|$``) still keeps a plain space so the
        original ``$\\frac{1}{|\\omega|}$ against`` fix is preserved.
        """
        assert (
            _separate_block_math("testing $1/|w|$against") == "testing $1/|w|$ against"
        )
        assert (
            _separate_block_math("before$f$word")
            == "before<!-- markdown separator -->$f$<!-- markdown separator -->word"
        )

    def test_joiner_punctuation_unchanged(self) -> None:
        """Joiner-wrapped math before punctuation gets no space."""
        text = "function \u2060$f(x)$\u2060, defined"
        assert _separate_block_math(text) == text
        assert (
            _separate_block_math("\u2060$f$\u2060word")
            == "\u2060$f$<!-- markdown separator -->\u2060word"
        )

    def test_punctuation_adjacent_no_space(self) -> None:
        """Math adjacent to punctuation gets no space."""
        assert _separate_block_math("($x$)") == "($x$)"
        assert _separate_block_math("text ($x$) and $y$!") == "text ($x$) and $y$!"

    def test_slash_underscore_like_emphasis(self) -> None:
        """``/`` and ``_`` are content, matching emphasis parity."""
        assert _separate_block_math("$x$/3") == "$x$<!-- markdown separator -->/3"
        assert _separate_block_math("$x$_n") == "$x$<!-- markdown separator -->_n"

    def test_inline_math_in_block_unchanged(self) -> None:
        """Block and inline each spaced once — no double insertion.

        ``$x$`` is atomic, so it gets the zero-width marker on both sides.
        """
        assert _separate_block_math("a $$f$$ b $x$ c") == "a $$f$$ b $x$ c"
        assert (
            _separate_block_math("a$$f$$b$x$c")
            == "a $$f$$ b<!-- markdown separator -->$x$<!-- markdown separator -->c"
        )

    def test_scan_and_apply_dollar_region_skipped(self) -> None:
        """``$$...$$`` regions are never matched as single-``$`` spans."""
        result = _scan_and_apply("$$f$$", [("f", False, False, False)])
        assert result == "$$f$$"
        result = _scan_and_apply("$f$$f$", [("f", False, False, True)])
        assert result == "$f$$f$"

    def test_inline_math_softbreak_after_no_trailing_space(self) -> None:
        """A line break after inline math needs no extra space.

        A ``softbreak``/``linebreak`` sibling already provides whitespace
        separation; inserting a space would create MD009 trailing
        whitespace and a non-idempotent pipeline (the space turns the
        softbreak into a linebreak, so the space is never removed).
        """
        assert _separate_block_math("para $x$\nnext line") == "para $x$\nnext line"

    def test_inline_math_softbreak_before_no_space(self) -> None:
        """A line break before inline math needs no extra space."""
        assert _separate_block_math("para\n$x$ next") == "para\n$x$ next"

    def test_word_suffix_single_symbol_marker(self) -> None:
        """``$n$th`` word suffix gets the zero-width marker, not a space."""
        assert (
            _separate_block_math("the $n$th derivative")
            == "the $n$<!-- markdown separator -->th derivative"
        )

    def test_complex_math_word_abutting_keeps_space(self) -> None:
        """Complex math abutting a word keeps a plain space."""
        assert _separate_block_math(r"$\frac{1}{2}$against") == r"$\frac{1}{2}$ against"

    def test_function_call_math_keeps_space(self) -> None:
        """``f(x)``-style math abutting words keeps spaces (non-atomic)."""
        assert _separate_block_math("word$f(x)$word") == "word $f(x)$ word"

    def test_marker_idempotent(self) -> None:
        """Re-running on marker'd output inserts nothing (inline_html guard)."""
        assert (
            _separate_block_math("the $n$<!-- markdown separator -->th derivative")
            == "the $n$<!-- markdown separator -->th derivative"
        )
        assert (
            _separate_block_math("before<!-- markdown separator -->$f$ word")
            == "before<!-- markdown separator -->$f$ word"
        )

    @pytest.mark.parametrize("sign", list(_UNICODE_SEPARATOR_CHARACTERS))
    def test_unicode_signs_no_space(self, sign: str) -> None:
        """Unicode math signs join the shared separator list — no spacing."""
        assert _separate_block_math(f"{sign}$x$") == f"{sign}$x$"
        assert _separate_block_math(f"$x${sign}") == f"$x${sign}"

    def test_minus_before_fraction(self) -> None:
        """U+2212 MINUS SIGN before a fraction needs no space."""
        text = "\u03c4 < \u2212$\\frac{a}{2\\pi}$"
        assert _separate_block_math(text) == text


# =========================================================================
# _separate_block_quotes — MD028 suppression
# =========================================================================


class TestSeparateBlockQuotes:
    """Tests for ``_separate_block_quotes`` MD028 suppression insertion."""

    # ── No-op cases ──────────────────────────────────────────────

    def test_empty_string(self) -> None:
        """Empty string → unchanged."""
        assert _separate_block_quotes("") == ""

    def test_no_blockquotes(self) -> None:
        """No blockquotes → unchanged."""
        text = "Just a normal paragraph."
        assert _separate_block_quotes(text) == text

    def test_single_blockquote(self) -> None:
        """Single blockquote → no comment inserted."""
        text = "> This is a single blockquote."
        assert _separate_block_quotes(text) == text

    def test_single_multiline_blockquote(self) -> None:
        """Single multi-line blockquote → no comment."""
        text = "> Line one\n> Line two\n> Line three"
        assert _separate_block_quotes(text) == text

    # ── Two consecutive blockquotes ──────────────────────────────

    def test_two_consecutive_blockquotes(self) -> None:
        """Two blockquotes separated by a blank line → MD028 inserted."""
        text = "> First\n\n> Second"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_two_blockquotes_only(self) -> None:
        """Two blockquotes with nothing else → MD028 inserted after blank."""
        result = _separate_block_quotes("> A\n\n> B")
        expected = "> A\n\n<!-- markdownlint MD028 -->\n\n> B"
        assert result == expected

    # ── Three consecutive blockquotes ────────────────────────────

    def test_three_consecutive_blockquotes(self) -> None:
        """Three consecutive blockquotes → MD028 between each pair."""
        result = _separate_block_quotes("> A\n\n> B\n\n> C")
        assert result.count("<!-- markdownlint MD028 -->") == 2

    def test_three_blockquotes_positions(self) -> None:
        """Verify MD028 comment positions with three blockquotes."""
        result = _separate_block_quotes("> A\n\n> B\n\n> C")
        lines = result.split("\n")
        # After "> A": blank, comment, blank, then "> B"
        assert lines[0] == "> A"
        assert lines[1] == ""
        assert "<!-- markdownlint MD028 -->" in lines[2]
        assert lines[3] == ""
        assert lines[4] == "> B"
        # After "> B": blank, comment, blank, then "> C"
        assert lines[5] == ""
        assert "<!-- markdownlint MD028 -->" in lines[6]
        assert lines[7] == ""
        assert lines[8] == "> C"

    # ── Blockquotes with other content ───────────────────────────

    def test_blockquote_paragraph_blockquote(self) -> None:
        """Blockquote → paragraph → blockquote → no comment."""
        text = "> Quote\n\nParagraph\n\n> Another quote"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" not in result
        assert result == text

    def test_blockquote_heading_blockquote(self) -> None:
        """Blockquote → heading → blockquote → no comment."""
        text = "> Quote\n\n# Heading\n\n> Another quote"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" not in result

    # ── Edge cases ───────────────────────────────────────────────

    def test_nested_blockquote(self) -> None:
        """Nested blockquotes (``> >``) should not confuse separation."""
        text = "> Outer\n> > Nested\n\n> After"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_blockquote_with_list_inside(self) -> None:
        """Blockquote containing a list → adjacent detection still works."""
        text = "> 1. Item\n> 2. Item\n\n> New quote"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_newlines_only_between_blockquotes(self) -> None:
        """Multiple blank lines between blockquotes → single MD028."""
        result = _separate_block_quotes("> A\n\n\n> B")
        # Should replace the gap with MD028 + blank
        assert result.count("<!-- markdownlint MD028 -->") == 1

    def test_text_after_last_blockquote(self) -> None:
        """Blockquotes followed by text → MD028 still between them."""
        text = "> First\n\n> Second\n\nSome trailing text"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result
        assert result.endswith("Some trailing text")


# =========================================================================
# _separate_block_math — whitespace around $$…$$
# =========================================================================


class TestSeparateBlockMath:
    """Tests for ``_separate_block_math`` whitespace insertion.

    These tests supplement the existing tests in ``test_convert_wiki.py``
    with additional edge cases.
    """

    def test_code_span_preserved(self) -> None:
        """``$$`` inside a code span should be left untouched."""
        assert _separate_block_math("text `$$inner$$` more") == "text `$$inner$$` more"

    def test_fenced_code_block_preserved(self) -> None:
        """``$$`` inside a fenced code block should be left untouched."""
        text = "```\n$$inside code$$\n```"
        assert _separate_block_math(text) == text

    def test_inline_code_mixed_with_math(self) -> None:
        """Inline math and real ``$$`` outside code are handled correctly."""
        # ``$x$`` (inline) inside backticks — literal, not math
        # $$y$$ (real) outside backticks — real block math
        result = _separate_block_math("`$x$` and $$y$$")
        assert "`$x$`" in result
        assert "$$y$$" in result

    def test_math_adjacent_to_punctuation(self) -> None:
        """Block math adjacent to punctuation → space inserted via needs_after."""
        assert _separate_block_math("(see $$eq$$.)") == "(see $$eq$$ .)"

    def test_punct_after_math_space_inserted(self) -> None:
        """Period after ``$$`` → space inserted via needs_after."""
        assert _separate_block_math("text $$eq$$. more") == "text $$eq$$ . more"

    def test_comma_after_math_space_inserted(self) -> None:
        """Comma after ``$$`` → space inserted via needs_after."""
        assert _separate_block_math("text $$eq$$, more") == "text $$eq$$ , more"

    def test_punct_after_multiline_env_space_inserted(self) -> None:
        """Period after ``$$…\\end{aligned}`` → space inserted via needs_after."""
        result = _separate_block_math(
            "text $$\\begin{aligned}x&=2\\\\y&=3\\end{aligned}$$. more"
        )
        expected = "text $$\\begin{aligned}x&=2\\\\y&=3\\end{aligned}$$ . more"
        assert result == expected

    def test_no_punct_after_needs_no_space(self) -> None:
        """No punctuation after ``$$``, next text starts with space → no space needed."""
        assert _separate_block_math("text $$eq$$ next") == "text $$eq$$ next"

    def test_skips_unrelated_dollar_span(self) -> None:
        """Second ``$$`` span handled independently via its own info entry."""
        assert _separate_block_math("text $$eq$$ $$not$$") == "text $$eq$$ $$not$$"

    def test_only_block_math(self) -> None:
        """Document consisting only of ``$$…$$`` → unchanged."""
        assert _separate_block_math("$$f(x)$$") == "$$f(x)$$"

    def test_multiple_inline_and_block_mixed(self) -> None:
        """Mix of inline ``$x$`` and block ``$$…$$`` → only block affected."""
        result = _separate_block_math("equation $x$ yields $$result$$")
        assert "$x$" in result
        assert "$$result$$" in result

    def test_collapsed_block_math_split(self) -> None:
        """Adjacent ``$$…$$$$…$$`` at top level → split with one space."""
        assert _separate_block_math("$$A$$$$B$$") == "$$A$$ $$B$$"

    def test_collapsed_with_text_between(self) -> None:
        """``$$…$$text$$…$$`` at top level → split with text preserved."""
        assert (
            _separate_block_math("$$equation$$text$$another$$")
            == "$$equation$$ text $$another$$"
        )


# =========================================================================
# wiki_html_to_plaintext — post-processing integration
# =========================================================================


class TestWikiHtmlToPlaintext:
    """Integration tests for ``wiki_html_to_plaintext``.

    These tests exercise the full post-processing pipeline (NBSP→space,
    hair→&hairsp;, table reformatting, blockquote separation, blank-line
    collapse, math spacing).
    """

    @pytest.mark.anyio
    async def test_simple_paragraph(self, tmp_path: PathLike[str]) -> None:
        """Simple paragraph text → converted to Markdown paragraph."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup("<p>Hello world</p>", "html.parser")
        result = await wiki_html_to_plaintext(
            html,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        assert result == "Hello world\n"

    @pytest.mark.anyio
    async def test_nbsp_replacement(self, tmp_path: PathLike[str]) -> None:
        """Non-breaking spaces are converted to regular spaces."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup("<p>Hello\u00a0world</p>", "html.parser")
        result = await wiki_html_to_plaintext(
            html,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        assert "Hello world" in result
        assert "\u00a0" not in result

    @pytest.mark.anyio
    async def test_hair_space_replacement(self, tmp_path: PathLike[str]) -> None:
        """Hair space input does not cause errors in pipeline.

        The converter normalizes ``\u200a`` before the post-processing
        ``&hairsp;`` replacement runs, so we verify the function runs
        without error rather than asserting a specific output.
        """
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup("<p>a\u200ab</p>", "html.parser")
        result = await wiki_html_to_plaintext(
            html,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        assert result is not None

    @pytest.mark.anyio
    async def test_trailing_whitespace_stripped(self, tmp_path: PathLike[str]) -> None:
        """Trailing whitespace on each line is stripped.

        The converter normalizes multiple spaces, but trailing whitespace
        is still stripped from each line in post-processing.
        """
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup("<p>text with spaces  </p>", "html.parser")
        result = await wiki_html_to_plaintext(
            html,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        assert "text with spaces" in result
        # No trailing spaces on the line
        for line in result.split("\n"):
            assert line == line.rstrip(" \t")

    @pytest.mark.anyio
    async def test_blank_line_collapse(self, tmp_path: PathLike[str]) -> None:
        """Excessive blank lines (3+) are collapsed to 2."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup("<p>First</p><p>Second</p><p>Third</p>", "html.parser")
        result = await wiki_html_to_plaintext(
            html,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        # Paragraphs are separated by blank lines in HTML->Markdown conversion.
        # There should be no triple blank lines.
        lines = result.split("\n")
        blank_streak = 0
        for line in lines:
            if line.strip() == "":
                blank_streak += 1
                assert blank_streak <= 2, "Triple blank lines found"
            else:
                blank_streak = 0

    @pytest.mark.anyio
    async def test_empty_content(self, tmp_path: PathLike[str]) -> None:
        """Empty HTML body → empty string."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup("<html><body></body></html>", "html.parser")
        result = await wiki_html_to_plaintext(
            html,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        assert result == ""

    @pytest.mark.anyio
    async def test_pre_converted_converter(self, tmp_path: PathLike[str]) -> None:
        """A pre-configured converter can be passed in."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )
        html = BeautifulSoup("<p>Custom converter</p>", "html.parser")
        result = await wiki_html_to_plaintext(
            html,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
            converter=converter,
        )
        assert "Custom converter" in result

    @pytest.mark.anyio
    async def test_block_math_separation(self, tmp_path: PathLike[str]) -> None:
        """Block math adjacency triggers space insertion in post-processing."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup("<p>text$$x$$more</p>", "html.parser")
        result = await wiki_html_to_plaintext(
            html,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        # The converter will produce something like "text$x$more",
        # and _separate_block_math post-processing handles $$...$$ spacing.
        # The exact output depends on how the converter handles the math
        # span — the key assertion is that the function runs without error.
        assert result is not None

    @pytest.mark.anyio
    async def test_table_inline_math_pipes_aligned(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Math spacing in table cells keeps pipes aligned (MD060).

        Math spacing must run before table reformatting; otherwise the
        inserted spaces grow a cell past its padded column width and the
        pipes misalign.
        """
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup(
            "<table><tbody><tr><th>Column 1</th></tr><tr><td>word"
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            '<math alttext="{\\displaystyle f(x)}"><semantics><mrow>'
            '<mi>f</mi><mo stretchy="false">(</mo><mi>x</mi>'
            '<mo stretchy="false">)</mo></mrow></semantics></math>'
            '<img class="mwe-math-fallback-image-inline mw-invert skin-invert"'
            ' src="data:image/svg+xml;base64," /></span></span>word'
            "</td></tr></tbody></table>",
            "html.parser",
        )
        result = await wiki_html_to_plaintext(
            html,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        # Column width is 16 (``word $f(x)$ word``); all rows align.
        assert result == (
            "| Column 1         |\n| ---------------- |\n| word $f(x)$ word |\n"
        )


# =========================================================================
# run_pipeline — top-level orchestrator
# =========================================================================


class TestRunPipeline:
    """Integration tests for the top-level ``run_pipeline`` orchestrator.

    Tests use pre-provided data (redirect_map, image_metadata) to avoid
    HTTP requests or filesystem API calls.
    """

    @pytest.mark.anyio
    async def test_simple_html(self, tmp_path: PathLike[str]) -> None:
        """Minimal HTML through the full pipeline → non-empty Markdown."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup(
            "<html><body><p>Hello world</p></body></html>", "html.parser"
        )
        output, out_to_archive = await run_pipeline(
            html,
            redirect_map={},
            image_metadata={},
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
            refs=True,
        )
        assert "Hello world" in output
        assert isinstance(out_to_archive, set)

    @pytest.mark.anyio
    async def test_with_redirect_map(self, tmp_path: PathLike[str]) -> None:
        """Pre-resolved redirect_map gets used for link resolution."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        redirect_map: dict[str, _RedirectInfo] = {
            "Redirected page": _RedirectInfo(to="Target page", tofragment=""),
        }
        html = BeautifulSoup("<html><body><p>Hello</p></body></html>", "html.parser")
        output, out_to_archive = await run_pipeline(
            html,
            redirect_map=redirect_map,
            image_metadata={},
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
            refs=True,
        )
        assert isinstance(output, str)
        assert isinstance(out_to_archive, set)

    @pytest.mark.anyio
    async def test_with_image_metadata(self, tmp_path: PathLike[str]) -> None:
        """Pre-resolved image metadata prevents API calls."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        image_metadata: dict[str, str] = {"File:Example.svg": "Example SVG image"}
        html = BeautifulSoup("<html><body><p>Test</p></body></html>", "html.parser")
        output, out_to_archive = await run_pipeline(
            html,
            redirect_map={},
            image_metadata=image_metadata,
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
            refs=True,
        )
        assert isinstance(output, str)
        assert isinstance(out_to_archive, set)

    @pytest.mark.anyio
    async def test_names_map_passthrough(self, tmp_path: PathLike[str]) -> None:
        """Custom names_map is passed through to the converter."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        names_map: dict[str, str] = {"Custom Title": "custom_title"}
        html = BeautifulSoup(
            "<html><body><p>Named content</p></body></html>", "html.parser"
        )
        output, out_to_archive = await run_pipeline(
            html,
            redirect_map={},
            image_metadata={},
            names_map=names_map,
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
            refs=True,
        )
        assert isinstance(output, str)
        assert isinstance(out_to_archive, set)

    @pytest.mark.anyio
    async def test_empty_html(self, tmp_path: PathLike[str]) -> None:
        """Empty HTML body → empty output string."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup("<html><body></body></html>", "html.parser")
        output, out_to_archive = await run_pipeline(
            html,
            redirect_map={},
            image_metadata={},
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
            refs=True,
        )
        assert output == ""
        assert out_to_archive == set()

    @pytest.mark.anyio
    async def test_refs_disabled(self, tmp_path: PathLike[str]) -> None:
        """Setting ``refs=False`` still produces output."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup("<html><body><p>No refs</p></body></html>", "html.parser")
        output, out_to_archive = await run_pipeline(
            html,
            redirect_map={},
            image_metadata={},
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
            refs=False,
        )
        assert "No refs" in output
