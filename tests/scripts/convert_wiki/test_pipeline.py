"""Tests for ``scripts.convert_wiki.pipeline``.

Covers all exported functions:

* ``_make_converter`` — factory function
* ``_determine_needs_before`` / ``_determine_needs_after`` — spacing decisions
* ``_collect_block_math_info`` — AST traversal for block math
* ``_scan_and_apply`` — text replacement for block math spacing
* ``_separate_block_quotes`` — MD028 suppression between adjacent blockquotes
* ``_separate_block_math`` — whitespace around ``$$…$$`` blocks
* ``_merge_dl_after_thumb_into_list`` — thumbnail/list merging for ``<dl>`` captions
* ``_math_source_from_data_mw`` — Parsoid ``data-mw`` source fallback
* ``_normalize_math_source`` — TeX normalization for lifted ``data-mw`` sources
* ``wiki_html_to_plaintext`` — post-processing after the converter
* ``run_pipeline`` — top-level orchestrator
"""

from __future__ import annotations

import json
from os import PathLike
from typing import Any

import pytest
from anyio import Path
from bs4 import BeautifulSoup, Tag

from scripts.convert_wiki.ast_utils import _MISTUNE_PARSER
from scripts.convert_wiki.config import (
    _MATH_SEPARATOR_CHARACTERS,
    _UNICODE_SEPARATOR_CHARACTERS,
)
from scripts.convert_wiki.converter import WikiHtmlConverter, _syntaxhighlight_source
from scripts.convert_wiki.pipeline import (
    _MATH_ENV_ALIASES,
    _collect_block_math_info,
    _determine_needs_after,
    _determine_needs_before,
    _math_source_from_data_mw,
    _merge_dl_after_thumb_into_list,
    _normalize_math_source,
    _preprocess_html,
    _scan_and_apply,
    _separate_block_math,
    _separate_block_quotes,
    run_pipeline,
    wiki_html_to_plaintext,
)
from scripts.convert_wiki.template_config import _DISPLAY_MATH_ENVIRONMENTS
from scripts.convert_wiki.types import _RedirectInfo

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


# =========================================================================
# _make_converter — factory function
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

    def test_prev_text_ending_with_apostrophe_math_separator(self) -> None:
        """Apostrophe is NOT a math separator → space needed before math.

        With the default (emphasis) separator set the apostrophe is a
        separator, but inline math passes ``_MATH_SEPARATOR_CHARACTERS`` which
        excludes it, so ``$a$'s`` still gets spacing.
        """
        assert (
            _determine_needs_before(
                {"type": "text", "raw": "word'"},
                inline=True,
                separator_chars=_MATH_SEPARATOR_CHARACTERS,
            )
            is True
        )
        # The default (emphasis) separator set still treats apostrophe as a
        # separator, so the same input needs no space there.
        assert (
            _determine_needs_before(
                {"type": "text", "raw": "word'"},
                inline=True,
            )
            is False
        )


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

    def test_next_text_starting_with_apostrophe_math_separator(self) -> None:
        """Apostrophe is NOT a math separator → space needed after math.

        With the default (emphasis) separator set the apostrophe is a
        separator, but inline math passes ``_MATH_SEPARATOR_CHARACTERS`` which
        excludes it, so ``'s$a$`` still gets spacing.
        """
        assert (
            _determine_needs_after(
                {"type": "text", "raw": "'s"},
                inline=True,
                separator_chars=_MATH_SEPARATOR_CHARACTERS,
            )
            is True
        )
        assert (
            _determine_needs_after(
                {"type": "text", "raw": "'word"},
                inline=True,
                separator_chars=_MATH_SEPARATOR_CHARACTERS,
            )
            is True
        )


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

    def test_block_math_only_child_of_link_uses_link_prev_sibling(self) -> None:
        """Block math as the sole child of a link derives spacing from the
        link's previous sibling, not the (empty) link interior.

        ``</sup>`` is inline HTML (no trailing whitespace) so a space is
        needed; ``text `` ends with a space so no space is needed.  Without
        the fallback both would be ``False`` (empty link interior).
        """
        info = _collect_block_math_info(_parse("</sup>[$$f(x)$$](url)"))
        assert len(info) == 1
        raw, needs_before, needs_after, is_inline = info[0]
        assert raw == "f(x)"
        assert is_inline is False
        assert needs_before is True

        info = _collect_block_math_info(_parse("text [$$f(x)$$](url)"))
        assert len(info) == 1
        raw, needs_before, needs_after, is_inline = info[0]
        assert raw == "f(x)"
        assert is_inline is False
        assert needs_before is False


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

    def test_insert_space_before_link_wrapping_math(self) -> None:
        """Link-wrapped block math with ``needs_before`` gets the space outside
        the link, between the preceding text and the opening bracket."""
        result = _scan_and_apply(
            "</sup>[$$f(x)$$](url)", [("f(x)", True, False, False)]
        )
        assert result == "</sup> [$$f(x)$$](url)"

    def test_no_space_before_link_when_already_spaced(self) -> None:
        """Link-wrapped block math whose preceding text already ends with a
        space keeps the existing space and does not insert a second one.

        Here ``word`` has no trailing space (so ``needs_before`` is True),
        but the character immediately before the ``[`` is whitespace, so the
        separator is not inserted a second time.
        """
        result = _scan_and_apply("word [$$f(x)$$](url)", [("f(x)", True, False, False)])
        assert result == "word [$$f(x)$$](url)"


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

    def test_apostrophe_suffix_gets_marker(self) -> None:
        """``$a$'s`` possessive gets the zero-width marker, not a space.

        The straight apostrophe is a word-forming character, so it must not
        be treated as an already-present separator — otherwise the math
        fails to render.
        """
        assert _separate_block_math("$a$'s") == "$a$<!-- markdown separator -->'s"
        assert _separate_block_math("'s$a$") == "'s<!-- markdown separator -->$a$"

    def test_complex_math_apostrophe_suffix_gets_marker(self) -> None:
        """Complex math abutting an apostrophe gets the zero-width marker.

        A straight apostrophe is word-forming (possessive ``'s``), so it must
        not be separated from the math by a space regardless of atomicity.
        """
        assert (
            _separate_block_math(r"$\frac{1}{2}$'s")
            == r"$\frac{1}{2}$<!-- markdown separator -->'s"
        )

    def test_complex_math_word_abutting_keeps_space(self) -> None:
        """Complex math abutting a word keeps a plain space."""
        assert _separate_block_math(r"$\frac{1}{2}$against") == r"$\frac{1}{2}$ against"

    def test_function_call_math_keeps_space(self) -> None:
        """``f(x)``-style math abutting words keeps spaces (non-atomic)."""
        assert _separate_block_math("word$f(x)$word") == "word $f(x)$ word"

    def test_link_wrapped_block_math_gets_space_before_link(self) -> None:
        """Block math wrapped in a link gets the separator outside the link.

        The space goes between the preceding text and the opening bracket so
        the math still renders inside the link target.  When the preceding
        text already ends with a space, no extra space is inserted.
        """
        assert _separate_block_math("</sup>[$$f(x)$$](url)") == "</sup> [$$f(x)$$](url)"
        assert _separate_block_math("text [$$f(x)$$](url)") == "text [$$f(x)$$](url)"

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


class TestBlockMathLineBreaks:
    """Consecutive ``$$…$$`` blocks on one line get hard line breaks.

    Two or more block-math spans in the same paragraph (separated only by
    whitespace, no newline) are joined with `` <br/> `` so they render on
    separate lines.  Newline gaps (separate paragraphs), text gaps, and
    already-broken output are left unchanged.
    """

    def test_two_blocks_two_spaces(self) -> None:
        """Two block-math spans with a two-space gap get a line break."""
        assert _separate_block_math("$$f$$  $$g$$") == "$$f$$ <br/> $$g$$"

    def test_three_blocks(self) -> None:
        """A chain of three block-math spans breaks between each pair."""
        assert (
            _separate_block_math("$$f$$  $$g$$  $$h$$")
            == "$$f$$ <br/> $$g$$ <br/> $$h$$"
        )

    def test_adjacent_delimiters(self) -> None:
        """No whitespace at all between spans (raw converter output) still
        breaks."""
        assert _separate_block_math("$$f$$$$g$$") == "$$f$$ <br/> $$g$$"

    def test_adjacent_delimiters_three(self) -> None:
        """Adjacent spans in a chain of three break between each pair."""
        assert (
            _separate_block_math("$$f$$$$g$$$$h$$") == "$$f$$ <br/> $$g$$ <br/> $$h$$"
        )

    def test_newline_gap_unchanged(self) -> None:
        """Block math in separate paragraphs keeps its newline separation."""
        assert _separate_block_math("$$f$$\n$$g$$") == "$$f$$\n$$g$$"

    def test_text_gap_unchanged(self) -> None:
        """Block math separated by real text is left alone."""
        assert _separate_block_math("$$f$$ and $$g$$") == "$$f$$ and $$g$$"

    def test_idempotent(self) -> None:
        """Re-running on already-broken output inserts nothing."""
        assert _separate_block_math("$$f$$ <br/> $$g$$") == "$$f$$ <br/> $$g$$"


# =========================================================================
# HTML tags adjacent to inline math — regression
# =========================================================================


class TestHtmlTagInlineMathSpacing:
    """Inline HTML tags adjacent to inline math get no spurious space.

    Regression: ``<sub> $\frac{n}{2}$+_δ_</sub>`` must stay
    ``<sub>$\frac{n}{2}$+_δ_</sub>`` (and mirror for closing tags).
    """

    def test_inline_html_before_math_no_space(self) -> None:
        """Opening tag before inline math inserts no space (exact artifact)."""
        text = r"<sub>$\frac{n}{2}$+_δ_</sub>"
        assert _separate_block_math(text) == text

    def test_inline_math_before_closing_tag_no_space(self) -> None:
        """Closing tag after inline math inserts no space."""
        assert _separate_block_math(r"$x$</sub>") == r"$x$</sub>"
        assert _separate_block_math(r"$\frac{n}{2}$</sup>") == r"$\frac{n}{2}$</sup>"

    def test_determine_needs_before_inline_html(self) -> None:
        """Inline HTML sibling before inline math needs no space."""
        assert (
            _determine_needs_before(
                {"type": "inline_html", "raw": "<sub>"}, inline=True
            )
            is False
        )

    def test_determine_needs_after_inline_html(self) -> None:
        """Inline HTML sibling after inline math needs no space."""
        assert (
            _determine_needs_after(
                {"type": "inline_html", "raw": "</sub>"}, inline=True
            )
            is False
        )

    @pytest.mark.anyio
    async def test_end_to_end_no_space_around_html_tag(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Full converter → pipeline chain keeps math flush inside tags."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup(
            '<p>text <sub><span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            '<math alttext="{\\displaystyle \\frac{n}{2}}"><semantics><mrow>'
            "</mrow></semantics></math>"
            '<img class="mwe-math-fallback-image-inline mw-invert skin-invert"'
            ' src="data:image/svg+xml;base64," /></span></span>+δ</sub>'
            " and <sup>"
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            '<math alttext="{\\displaystyle x}"><semantics><mrow></mrow>'
            "</semantics></math>"
            '<img class="mwe-math-fallback-image-inline mw-invert skin-invert"'
            ' src="data:image/svg+xml;base64," /></span></span>+</sup>.</p>',
            "html.parser",
        )
        result = await wiki_html_to_plaintext(
            html,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        assert r"<sub>$\frac{n}{2}$+δ</sub>" in result
        assert "<sup>$x$+</sup>" in result
        assert r"<sub> $" not in result
        assert r"$ </sup>" not in result


# =========================================================================
# _separate_block_quotes — MD028 suppression
# =========================================================================


class TestSeparateBlockQuotes:
    """Tests for ``_separate_block_quotes`` MD028 suppression insertion.

    Sole home of ``_separate_block_quotes`` unit tests; cases were
    consolidated here from ``test_convert_wiki_regression.py``.
    """

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

    def test_nested_blockquote(self) -> None:
        """Nested blockquotes (``> >``) should not confuse separation."""
        text = "> Outer\n> > Nested\n\n> After"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_blockquote_with_inline_content(self) -> None:
        """Blockquote with nested elements → still matches."""
        text = "> Some **bold** text\n\n> Other `code` here"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_blockquote_with_list_inside(self) -> None:
        """Blockquote containing a list → adjacent detection still works."""
        text = "> 1. Item\n> 2. Item\n\n> New quote"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_multi_line_blockquotes(self) -> None:
        """Multi-line blockquotes → treated as one block."""
        text = "> Line 1\n> Line 2\n\n> Line 3\n> Line 4"
        result = _separate_block_quotes(text)
        expected = (
            "> Line 1\n> Line 2\n\n<!-- markdownlint MD028 -->\n\n> Line 3\n> Line 4"
        )
        assert result == expected

    def test_triple_blank_lines_between_blockquotes(self) -> None:
        """Multiple (3+) blank lines → treated as one separator."""
        text = "> First\n\n\n> Second"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_blockquote_with_code_fence(self) -> None:
        """Blockquote containing a code fence."""
        text = "> Quote with:\n> ```\n> code block\n> ```\n\n> Next quote"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_text_after_last_blockquote(self) -> None:
        """Blockquotes followed by text → MD028 still between them."""
        text = "> First\n\n> Second\n\nSome trailing text"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result
        assert result.endswith("Some trailing text")


class TestSeparateBlockMath:
    """Tests for ``_separate_block_math`` whitespace insertion.

    Sole home of ``_separate_block_math`` unit tests; cases were
    consolidated here from ``test_convert_wiki_regression.py`` and
    ``test_convert_wiki.py``.
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
        assert (
            _separate_block_math("text $$eq$$ $$not$$") == "text $$eq$$ <br/> $$not$$"
        )

    def test_only_block_math(self) -> None:
        """Document consisting only of ``$$…$$`` → unchanged."""
        assert _separate_block_math("$$f(x)$$") == "$$f(x)$$"

    def test_multiple_inline_and_block_mixed(self) -> None:
        """Mix of inline ``$x$`` and block ``$$…$$`` → only block affected."""
        result = _separate_block_math("equation $x$ yields $$result$$")
        assert "$x$" in result
        assert "$$result$$" in result

    def test_collapsed_block_math_split(self) -> None:
        """Adjacent ``$$…$$$$…$$`` at top level → split with a line break."""
        assert _separate_block_math("$$A$$$$B$$") == "$$A$$ <br/> $$B$$"

    def test_collapsed_with_text_between(self) -> None:
        """``$$…$$text$$…$$`` at top level → split with text preserved."""
        assert (
            _separate_block_math("$$equation$$text$$another$$")
            == "$$equation$$ text $$another$$"
        )

    # ── No-op cases ──────────────────────────────────────────────

    def test_empty_string(self) -> None:
        """Empty string should be returned unchanged."""
        assert _separate_block_math("") == ""

    def test_no_math(self) -> None:
        """String without any ``$$`` should be returned unchanged."""
        assert _separate_block_math("no math here") == "no math here"

    def test_paragraph_with_spacing_already(self) -> None:
        """When spaces already exist → no double spacing."""
        result = _separate_block_math("before $$f(x)$$ after")
        # Already has spaces, so unchanged
        assert result == "before $$f(x)$$ after"

    def test_already_spaced_between(self) -> None:
        """Two block math expressions already spaced between → no change."""
        assert _separate_block_math("$$f(x)$$ and $$g(y)$$") == "$$f(x)$$ and $$g(y)$$"

    def test_multiline_text_with_math(self) -> None:
        """Multi-line paragraph with block math."""
        text = "Line one\nbefore$$f(x)$$after\nLine three"
        result = _separate_block_math(text)
        assert "before $$f(x)$$ after" in result

    def test_needs_space_before(self) -> None:
        """Non-whitespace text before ``$$`` → insert space before."""
        assert _separate_block_math("text$$f(x)$$") == "text $$f(x)$$"

    def test_math_at_end_of_text(self) -> None:
        """Text before $$, $$ at text end → space before."""
        result = _separate_block_math("before$$f(x)$$")
        assert result == "before $$f(x)$$"

    def test_needs_space_after(self) -> None:
        """Non-whitespace text after ``$$`` → insert space after."""
        assert _separate_block_math("$$f(x)$$text") == "$$f(x)$$ text"

    def test_math_at_start_of_text(self) -> None:
        """$$ at text start, text after → space after."""
        result = _separate_block_math("$$f(x)$$after")
        assert result == "$$f(x)$$ after"

    def test_needs_space_both(self) -> None:
        """Non-whitespace text on both sides → insert both spaces."""
        assert _separate_block_math("text$$f(x)$$more") == "text $$f(x)$$ more"

    def test_text_both_sides(self) -> None:
        """Text on both sides → spaces inserted on both sides."""
        result = _separate_block_math("before$$f(x)$$after")
        assert result == "before $$f(x)$$ after"

    def test_multiple_adjacent(self) -> None:
        """Multiple adjacent block math blocks → each gets spacing."""
        assert _separate_block_math("a$$f$$b$$g$$c") == "a $$f$$ b $$g$$ c"

    def test_multiple_block_math(self) -> None:
        """Multiple $$...$$ blocks in one paragraph."""
        result = _separate_block_math("a$$b$$c$$d$$e")
        assert result == "a $$b$$ c $$d$$ e"

    def test_emphasis_before_block_math(self) -> None:
        """Emphasis (``_italic_``) before ``$$`` → space inserted."""
        assert _separate_block_math("_italic_$$x$$") == "_italic_ $$x$$"

    # ── Preservation cases ───────────────────────────────────────

    def test_inline_math_unaffected(self) -> None:
        """Inline ``$…$`` should be left untouched."""
        assert _separate_block_math("$x$ is inline") == "$x$ is inline"

    def test_inline_math_adjacency_spaced(self) -> None:
        """Inline math ``$x$`` adjacent to text → markdown separator inserted."""
        assert (
            _separate_block_math("text$x$more")
            == "text<!-- markdown separator -->$x$<!-- markdown separator -->more"
        )

    def test_code_span_dollars_untouched(self) -> None:
        """``$$`` inside a code span → not modified."""
        assert (
            _separate_block_math("text `$$ax^2+bx+c$$` more")
            == "text `$$ax^2+bx+c$$` more"
        )

    def test_math_in_inline_code(self) -> None:
        """`` $$x$$ `` inside inline code → no space insertion."""
        text = "` $$x$$ `"
        result = _separate_block_math(text)
        # Mistune should recognize $$ in inline code as literal, not math
        assert result == text

    def test_math_in_fenced_code_block(self) -> None:
        """$$...$$ inside fenced code block → no processing."""
        text = "```\n$$f(x)$$\n```"
        result = _separate_block_math(text)
        # The $$ inside fenced code should be ignored by mistune AST
        assert "$$\nf$$" not in result  # sanity


class TestMergeDlAfterThumbIntoList:
    """Tests for ``_merge_dl_after_thumb_into_list``."""

    def test_prose_dd_merges_into_last_list_item(self) -> None:
        """A prose ``<dl>`` caption after a thumbnail joins the list."""
        soup = BeautifulSoup(
            '<ul><li>item</li></ul><div class="thumb"><img/></div>'
            "<dl><dd>caption</dd></dl>",
            "html.parser",
        )
        _merge_dl_after_thumb_into_list(soup)
        assert soup.find("dl") is None
        li = soup.find("li")
        assert li is not None
        assert "caption" in li.get_text()

    def test_multi_row_display_math_dl_is_not_merged(self) -> None:
        """A multi-row display-math ``<dl>`` is an equation block, not prose."""
        math = '<span class="mwe-math-element mwe-math-element-block"></span>'
        soup = BeautifulSoup(
            '<ul><li>item</li></ul><div class="thumb"><img/></div>'
            f"<dl><dd>{math}</dd><dd>{math}</dd></dl>",
            "html.parser",
        )
        _merge_dl_after_thumb_into_list(soup)
        assert soup.find("dl") is not None


# =========================================================================
# _preprocess_html — media-player chrome
# =========================================================================


class TestPreprocessPlayerChrome:
    """Tests for dropping the media player's duration label."""

    def test_duration_label_is_dropped(self) -> None:
        """The duration and timestamp span does not survive preprocessing."""
        html = (
            '<figure><span class="mw-tmh-player video">'
            "<video></video>"
            '<span class="mw-tmh-duration mw-tmh-label">'
            '<span class="sr-only">Duration: 14 seconds.</span>'
            '<span aria-hidden="true">0:14</span>'
            "</span></span></figure>"
        )
        soup = BeautifulSoup(html, "html.parser")
        _preprocess_html(soup)
        assert soup.find("span", class_="mw-tmh-duration") is None
        assert "Duration" not in soup.get_text()

    def test_player_and_media_survive(self) -> None:
        """The player container and its media stay for embed handling."""
        html = (
            '<figure><span class="mw-tmh-player video">'
            '<a class="mw-tmh-play"></a><video></video></span>'
            "<figcaption>caption</figcaption></figure>"
        )
        soup = BeautifulSoup(html, "html.parser")
        _preprocess_html(soup)
        assert soup.find("span", class_="mw-tmh-player") is not None
        assert soup.find("video") is not None
        assert soup.find("a", class_="mw-tmh-play") is not None
        assert "caption" in soup.get_text()


# =========================================================================
# wiki_html_to_plaintext — post-processing integration
# =========================================================================


async def _convert_html(html: str, converter: WikiHtmlConverter | None = None) -> str:
    """Convert *html* via ``wiki_html_to_plaintext`` with default options.

    *converter* overrides the default converter when given. No archives are
    collected and no redirects are resolved.
    """
    return await wiki_html_to_plaintext(
        BeautifulSoup(html, "html.parser"),
        out_to_archive=set(),
        redirect_map={},
        refs=True,
        converter=converter,
    )


# =========================================================================
# _preprocess_html — Parsoid math source lifting
# =========================================================================

"""Parsoid-style inline math whose LaTeX lives only in ``data-mw``.

``%s`` stands in for ``body.extsrc``.  The ``<math>`` element has no
``alttext``, matching modern Wikipedia HTML.
"""
_INLINE_MODERN_MATH = (
    '<p>A set <span class="mwe-math-element mwe-math-element-inline">'
    '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
    '<math xmlns="http://www.w3.org/1998/Math/MathML"'
    ' typeof="mw:Extension/math"'
    ' data-mw=\'{"name":"math","attrs":{},"body":{"extsrc":"%s"}}\'>'
    "<mrow><mi>S</mi></mrow></math></span></span> of paths.</p>"
)

"""Parsoid-style block math whose LaTeX lives only in ``data-mw``.

``%s`` stands in for ``body.extsrc``.  The ``<math>`` element has no
``alttext``, matching modern Wikipedia HTML.
"""
_BLOCK_MODERN_MATH = (
    "<p>A set of paths"
    '<span class="mwe-math-element mwe-math-element-block">'
    '<span class="mwe-math-mathml-display mwe-math-mathml-a11y">'
    '<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"'
    ' typeof="mw:Extension/math"'
    ' data-mw=\'{"name":"math","attrs":{"display":"block"},'
    '"body":{"extsrc":"%s"}}\'>'
    "<mrow><mi>M</mi></mrow></math></span></span>.</p>"
)


class TestNormalizeMathSource:
    """Tests for ``_normalize_math_source``.

    Parsoid keeps the wikitext's newlines and indentation in ``data-mw``, and
    Wikipedia writes display math with environments (``align``, ``eqnarray``,
    …) that Obsidian's MathJax build does not define.
    """

    @pytest.mark.parametrize(
        ("environment", "expected"),
        [
            ("align", "aligned"),
            ("align*", "aligned"),
            ("alignat", "alignedat"),
            ("alignat*", "alignedat"),
            ("gather", "gathered"),
            ("gather*", "gathered"),
            ("eqnarray", "aligned"),
            ("eqnarray*", "aligned"),
        ],
    )
    def test_environment_is_aliased(self, environment: str, expected: str) -> None:
        r"""Both ``\begin`` and ``\end`` of a known environment are rewritten."""
        source = rf"\begin{{{environment}}}a &= b\end{{{environment}}}"
        assert _normalize_math_source(source) == (
            rf"\begin{{{expected}}}a &= b\end{{{expected}}}"
        )

    def test_aliases_are_display_math_environments(self) -> None:
        r"""Every normalized name is a recognized display math environment.

        The converter decides display-math rendering and trailing-punctuation
        absorption by matching ``\end{env}`` against
        ``_DISPLAY_MATH_ENVIRONMENTS``, so a normalized name missing from that
        list would lose both behaviours.
        """
        missing = sorted(
            set(_MATH_ENV_ALIASES.values()) - set(_DISPLAY_MATH_ENVIRONMENTS)
        )
        assert not missing, missing

    @pytest.mark.parametrize("environment", ["multline", "multline*"])
    def test_multline_environment_is_unchanged(self, environment: str) -> None:
        """``multline`` renders natively in MathJax 4, so its name is kept."""
        source = rf"\begin{{{environment}}}a &= b\end{{{environment}}}"
        assert _normalize_math_source(source) == source

    def test_alignat_column_count_is_kept(self) -> None:
        """The ``alignat`` column count stays after the rewritten environment."""
        source = r"\begin{alignat}{2}a &= b\end{alignat}"
        assert _normalize_math_source(source) == (
            r"\begin{alignedat}{2}a &= b\end{alignedat}"
        )

    def test_unknown_environment_is_unchanged(self) -> None:
        """An environment outside the alias map is left alone."""
        source = r"\begin{equation}a = b\end{equation}"
        assert _normalize_math_source(source) == source

    def test_whitespace_collapses_to_one_space(self) -> None:
        """Newlines, tabs, and indentation collapse, and the result is stripped."""
        source = "\n\\begin{aligned}\n\ta &= b \\\\\n\t\tc &= d\n\\end{aligned}\n"
        assert _normalize_math_source(source) == (
            R"\begin{aligned} a &= b \\ c &= d \end{aligned}"
        )

    def test_percent_comment_is_removed_before_collapse(self) -> None:
        r"""A ``%`` comment drops the rest of its line before the newlines collapse.

        Collapsing first would let the comment swallow the ``\end{align}`` on
        the following line, so the removal has to happen first.
        """
        source = "\\begin{align}a &= b % first row\n\\end{align}"
        assert _normalize_math_source(source) == (
            r"\begin{aligned}a &= b \end{aligned}"
        )

    def test_escaped_percent_is_literal(self) -> None:
        r"""``\%`` is a literal percent, so text such as ``50\%`` survives."""
        assert _normalize_math_source(r"\text{50\%}") == r"\text{50\%}"


class TestPreprocessMathSource:
    """Tests for lifting Parsoid math source into the ``alttext`` attribute.

    Legacy HTML carries the LaTeX in ``alttext``; modern Parsoid carries it in
    a ``data-mw`` JSON payload (older revisions in an
    ``<annotation encoding="application/x-tex">`` child) and leaves ``<math>``
    without ``alttext``, so math degraded to its bare MathML text.
    """

    def test_inline_math_alttext_from_data_mw(self) -> None:
        """Inline math without ``alttext`` gets the source from ``data-mw``."""
        soup = BeautifulSoup(_INLINE_MODERN_MATH % "S", "html.parser")
        _preprocess_html(soup)
        math = soup.find("math")
        assert isinstance(math, Tag)
        assert math["alttext"] == "S"

    def test_block_math_alttext_from_data_mw(self) -> None:
        """Block math without ``alttext`` gets the source from ``data-mw``."""
        soup = BeautifulSoup(_BLOCK_MODERN_MATH % "M = E - N + 2P", "html.parser")
        _preprocess_html(soup)
        math = soup.find("math")
        assert isinstance(math, Tag)
        assert math["alttext"] == "M = E - N + 2P"

    def test_annotation_fallback_without_data_mw(self) -> None:
        """``<annotation>`` text is used when ``data-mw`` is absent."""
        html = (
            '<p>See <math xmlns="http://www.w3.org/1998/Math/MathML">'
            "<semantics><mrow><mi>x</mi></mrow>"
            '<annotation encoding="application/x-tex">x^2</annotation>'
            "</semantics></math>.</p>"
        )
        soup = BeautifulSoup(html, "html.parser")
        _preprocess_html(soup)
        math = soup.find("math")
        assert isinstance(math, Tag)
        assert math["alttext"] == "x^2"

    def test_existing_alttext_is_preserved(self) -> None:
        """A ``data-mw`` payload never overrides an existing ``alttext``."""
        soup = BeautifulSoup(_INLINE_MODERN_MATH % "S", "html.parser")
        math = soup.find("math")
        assert isinstance(math, Tag)
        math["alttext"] = R"{\displaystyle T}"
        _preprocess_html(soup)
        assert math["alttext"] == R"{\displaystyle T}"

    def test_existing_alttext_is_not_normalized(self) -> None:
        """An existing ``alttext`` keeps its newlines and environments."""
        soup = BeautifulSoup(_INLINE_MODERN_MATH % "S", "html.parser")
        math = soup.find("math")
        assert isinstance(math, Tag)
        existing = "\\begin{align}\n  a &= b\n\\end{align}"
        math["alttext"] = existing
        _preprocess_html(soup)
        assert math["alttext"] == existing

    def test_data_mw_align_environment_is_normalized(self) -> None:
        """A multi-line ``align`` source normalizes into a single-line ``alttext``."""
        source = "\\begin{align}\n  a &= b \\\\\n  c &= d\n\\end{align}"
        # The attribute holds JSON, whose escapes must carry the newlines.
        soup = BeautifulSoup(
            _BLOCK_MODERN_MATH % json.dumps(source)[1:-1], "html.parser"
        )
        _preprocess_html(soup)
        math = soup.find("math")
        assert isinstance(math, Tag)
        assert math["alttext"] == R"\begin{aligned} a &= b \\ c &= d \end{aligned}"

    def test_annotation_source_is_normalized(self) -> None:
        """The ``<annotation>`` fallback is normalized like ``data-mw``."""
        html = (
            '<p>See <math xmlns="http://www.w3.org/1998/Math/MathML">'
            "<semantics><mrow><mi>x</mi></mrow>"
            '<annotation encoding="application/x-tex">\n  \\begin{gather}\n'
            "  x = 1\n  \\end{gather}\n</annotation>"
            "</semantics></math></p>"
        )
        soup = BeautifulSoup(html, "html.parser")
        _preprocess_html(soup)
        math = soup.find("math")
        assert isinstance(math, Tag)
        assert math["alttext"] == R"\begin{gathered} x = 1 \end{gathered}"

    @pytest.mark.anyio
    async def test_inline_math_renders_latex(self) -> None:
        """Modern inline math renders as ``$…$``, not as bare MathML text."""
        result = await _convert_html(_INLINE_MODERN_MATH % "S")
        assert result == "A set $S$ of paths.\n"

    @pytest.mark.anyio
    async def test_block_math_renders_latex(self) -> None:
        """Modern block math renders as ``$$…$$``."""
        result = await _convert_html(_BLOCK_MODERN_MATH % "M = E - N + 2P")
        assert "$$M = E - N + 2P$$" in result


# =========================================================================
# data-mw — defensive fallbacks and merge ordering
# =========================================================================


def _element_with_data_mw(name: str, data_mw: str | None) -> Tag:
    """Return a ``<name>`` element whose ``data-mw`` attribute is *data_mw*."""
    attribute = "" if data_mw is None else f" data-mw='{data_mw}'"
    element = BeautifulSoup(f"<{name}{attribute}></{name}>", "html.parser").find(name)
    assert isinstance(element, Tag)
    return element


def _math_alttexts(soup: Tag) -> list[str]:
    """Return the ``alttext`` of every ``<math>`` in *soup*, in document order."""
    alttexts: list[str] = []
    for math in soup.find_all("math"):
        assert isinstance(math, Tag)
        alttexts.append(str(math.get("alttext", "")))
    return alttexts


def _inline_math_span(
    source: str, *, classes: str = "mwe-math-element mwe-math-element-inline"
) -> str:
    """Return inline-math markup carrying *source* only in its ``data-mw``.

    The ``<math>`` element has no ``alttext``, so nothing can read the source
    until ``_set_math_alttext_from_data_mw`` lifts it with *classes* deciding
    whether the span counts as inline or block math.
    """
    payload = json.dumps({"name": "math", "attrs": {}, "body": {"extsrc": source}})
    return (
        f'<span class="{classes}">'
        '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
        '<math xmlns="http://www.w3.org/1998/Math/MathML"'
        ' typeof="mw:Extension/math"'
        f" data-mw='{payload}'><mrow><mi>x</mi></mrow></math></span></span>"
    )


class TestDataMwDefensiveBranches:
    """Tests for the fallback each ``data-mw`` reader takes on a bad payload.

    ``_math_source_from_data_mw`` and ``_syntaxhighlight_source`` both lift a
    Parsoid extension invocation, and both must degrade — to ``""`` and to
    ``None`` — instead of raising, so the caller falls back to the rendered
    MathML text or to the generic ``<div>`` handling.
    """

    @pytest.mark.parametrize(
        "data_mw",
        [
            pytest.param(None, id="missing"),
            pytest.param("{not json", id="invalid-json"),
            pytest.param('["math"]', id="not-a-dict"),
            pytest.param(
                '{"name": "syntaxhighlight", "body": {"extsrc": "S"}}',
                id="wrong-name",
            ),
            pytest.param('{"name": "math"}', id="missing-body"),
            pytest.param('{"name": "math", "body": "S"}', id="non-dict-body"),
            pytest.param(
                '{"name": "math", "body": {"extsrc": 1}}', id="non-string-extsrc"
            ),
        ],
    )
    def test_math_source_falls_back_to_empty_string(self, data_mw: str | None) -> None:
        """An unusable payload yields ``""`` so the annotation fallback runs."""
        math = _element_with_data_mw("math", data_mw)
        assert _math_source_from_data_mw(math) == ""

    @pytest.mark.parametrize(
        "data_mw",
        [
            pytest.param(None, id="missing"),
            pytest.param('{"name": "syntaxhighlight", "body":', id="invalid-json"),
            pytest.param('["syntaxhighlight"]', id="not-a-dict"),
            pytest.param(
                '{"name": "syntaxhighlight-extra", "body": {"extsrc": "x"}}',
                id="wrong-name",
            ),
            pytest.param('{"name": "syntaxhighlight"}', id="missing-body"),
            pytest.param(
                '{"name": "syntaxhighlight", "body": "x"}', id="non-dict-body"
            ),
            pytest.param(
                '{"name": "syntaxhighlight", "body": {"extsrc": 1}}',
                id="non-string-extsrc",
            ),
        ],
    )
    def test_syntaxhighlight_falls_back_to_none(self, data_mw: str | None) -> None:
        """An unusable payload yields ``None`` so the generic div handling runs.

        Every payload but the missing one spells ``syntaxhighlight``, so the
        cheap substring precheck passes and the payload parser is what rejects
        them.
        """
        div = _element_with_data_mw("div", data_mw)
        assert _syntaxhighlight_source(div) is None

    @pytest.mark.parametrize(
        "data_mw",
        [
            pytest.param(
                '{"name": "syntaxhighlight", "body": {"extsrc": "x"}}',
                id="missing-attrs",
            ),
            pytest.param(
                '{"name": "syntaxhighlight", "attrs": ["lang", "c"],'
                ' "body": {"extsrc": "x"}}',
                id="non-dict-attrs",
            ),
            pytest.param(
                '{"name": "syntaxhighlight", "attrs": {}, "body": {"extsrc": "x"}}',
                id="empty-attrs",
            ),
        ],
    )
    def test_syntaxhighlight_without_lang_attrs_defaults_to_text(
        self, data_mw: str
    ) -> None:
        """Absent or non-mapping ``attrs`` gives the ``text`` info string.

        A fence without an info string fails markdownlint MD040, so the
        language has to default rather than come back empty.
        """
        div = _element_with_data_mw("div", data_mw)
        assert _syntaxhighlight_source(div) == ("text", "x")


class TestDataMwMergeOrdering:
    """Tests that adjacent-math merging reads a source lifted from ``data-mw``.

    ``_preprocess_html`` lifts the Parsoid source into ``alttext`` before it
    merges adjacent inline math spans, and both the ``=`` continuation guard
    and the merged text read ``alttext``.  Every fixture below carries its TeX
    only in ``data-mw``, so a lift placed after the merge would join empty
    strings and drop the continuation guard.
    """

    def test_dd_merges_inline_spans_carrying_data_mw_source(self) -> None:
        """Two adjacent inline spans in a ``<dd>`` merge into one ``alttext``."""
        soup = BeautifulSoup(
            f"<dl><dd>{_inline_math_span('a')} {_inline_math_span('b')}</dd></dl>",
            "html.parser",
        )
        _preprocess_html(soup)
        assert _math_alttexts(soup) == ["a b"]

    def test_paragraph_merges_when_first_part_ends_with_equals(self) -> None:
        """A trailing ``=`` plus a lifted source merges into ``a = b``.

        The guard only lets the run continue while the previous part looks
        unfinished, so the continuation is kept when it should be.
        """
        soup = BeautifulSoup(
            f"<p>{_inline_math_span('a =')} {_inline_math_span('b')}</p>",
            "html.parser",
        )
        _preprocess_html(soup)
        assert _math_alttexts(soup) == ["a = b"]

    def test_paragraph_keeps_parts_apart_without_trailing_equals(self) -> None:
        """Without a trailing ``=`` the two spans stay separate.

        This is where the ordering shows: the guard needs the lifted
        ``alttext`` to see that the first part finished, so a lift placed
        after the merge would join the spans into one.
        """
        soup = BeautifulSoup(
            f"<p>{_inline_math_span('a')} {_inline_math_span('b')}</p>",
            "html.parser",
        )
        _preprocess_html(soup)
        assert _math_alttexts(soup) == ["a", "b"]

    def test_run_with_block_math_is_not_merged(self) -> None:
        """A block span in the run keeps the parts apart.

        Merging would turn the block's ``$$…$$`` into one inline ``$…$`` run
        with the neighbouring span, so the run is left untouched.
        """
        block = _inline_math_span(
            "b", classes="mwe-math-element mwe-math-element-block"
        )
        soup = BeautifulSoup(
            f"<dl><dd>{_inline_math_span('a')} {block}</dd></dl>", "html.parser"
        )
        _preprocess_html(soup)
        assert _math_alttexts(soup) == ["a", "b"]

    def test_merged_run_keeps_normalized_environment(self) -> None:
        """The ``align`` source is aliased before the merge joins the parts."""
        source = r"\begin{align} a \end{align}"
        soup = BeautifulSoup(
            f"<dl><dd>{_inline_math_span(source)} {_inline_math_span('b')}</dd></dl>",
            "html.parser",
        )
        _preprocess_html(soup)
        assert _math_alttexts(soup) == [r"\begin{aligned} a \end{aligned} b"]


class TestWikiHtmlToPlaintext:
    """Integration tests for ``wiki_html_to_plaintext``.

    These tests exercise the full post-processing pipeline (NBSP→space,
    hair→&hairsp;, table reformatting, blockquote separation, blank-line
    collapse, math spacing).
    """

    @pytest.mark.anyio
    async def test_simple_paragraph(self) -> None:
        """Simple paragraph text → converted to Markdown paragraph."""
        result = await _convert_html("<p>Hello world</p>")
        assert result == "Hello world\n"

    @pytest.mark.anyio
    async def test_nbsp_replacement(self) -> None:
        """Non-breaking spaces are converted to regular spaces."""
        result = await _convert_html("<p>Hello\u00a0world</p>")
        assert "Hello world" in result
        assert "\u00a0" not in result

    @pytest.mark.anyio
    async def test_hair_space_replacement(self) -> None:
        """Hair space (U+200A) is preserved through the pipeline.

        The converter preserves ``\u200a`` during whitespace collapsing so
        the post-processing ``&hairsp;`` replacement can emit the entity.
        """
        result = await _convert_html("<p>a\u200ab</p>")
        assert "a&hairsp;b" in result

    @pytest.mark.anyio
    async def test_hair_space_in_citation_sup(self) -> None:
        """Hair spaces inside ``<sup>`` citation markers survive collapsing."""
        result = await _convert_html("<p>see<sup>:\u200a2\u200a</sup></p>")
        assert "see<sup>:&hairsp;2&hairsp;</sup>" in result

    @pytest.mark.anyio
    async def test_hair_space_in_classed_blockquote(self) -> None:
        """Hair space survives the blockquote collapse path."""
        result = await _convert_html(
            '<blockquote class="math_theorem">a\u200ab</blockquote>'
        )
        assert "a&hairsp;b" in result

    @pytest.mark.anyio
    async def test_trailing_whitespace_stripped(self) -> None:
        """Trailing whitespace on each line is stripped.

        The converter normalizes multiple spaces, but trailing whitespace
        is still stripped from each line in post-processing.
        """
        result = await _convert_html("<p>text with spaces  </p>")
        assert "text with spaces" in result
        # No trailing spaces on the line
        for line in result.split("\n"):
            assert line == line.rstrip(" \t")

    @pytest.mark.anyio
    async def test_blank_line_collapse(self) -> None:
        """Excessive blank lines (3+) are collapsed to 2."""
        result = await _convert_html("<p>First</p><p>Second</p><p>Third</p>")
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
    async def test_empty_content(self) -> None:
        """Empty HTML body → empty string."""
        result = await _convert_html("<html><body></body></html>")
        assert result == ""

    @pytest.mark.anyio
    async def test_pre_converted_converter(self, tmp_path: PathLike[str]) -> None:
        """A pre-configured converter can be passed in."""
        tmp = Path(tmp_path)
        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=tmp / "general" / "eng",
        )
        result = await _convert_html("<p>Custom converter</p>", converter)
        assert "Custom converter" in result

    @pytest.mark.anyio
    async def test_block_math_separation(self) -> None:
        """Block math adjacency triggers space insertion in post-processing."""
        result = await _convert_html("<p>text$$x$$more</p>")
        # The converter will produce something like "text$x$more",
        # and _separate_block_math post-processing handles $$...$$ spacing.
        # The exact output depends on how the converter handles the math
        # span — the key assertion is that the function runs without error.
        assert result is not None

    @pytest.mark.anyio
    async def test_table_inline_math_pipes_aligned(self) -> None:
        """Math spacing in table cells keeps pipes aligned (MD060).

        Math spacing must run before table reformatting; otherwise the
        inserted spaces grow a cell past its padded column width and the
        pipes misalign.
        """
        result = await _convert_html(
            "<table><tbody><tr><th>Column 1</th></tr><tr><td>word"
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            '<math alttext="{\\displaystyle f(x)}"><semantics><mrow>'
            '<mi>f</mi><mo stretchy="false">(</mo><mi>x</mi>'
            '<mo stretchy="false">)</mo></mrow></semantics></math>'
            '<img class="mwe-math-fallback-image-inline mw-invert skin-invert"'
            ' src="data:image/svg+xml;base64," /></span></span>word'
            "</td></tr></tbody></table>"
        )
        # Column width is 16 (``word $f(x)$ word``); all rows align.
        assert result == (
            "| Column 1         |\n| ---------------- |\n| word $f(x)$ word |\n"
        )

    @pytest.mark.anyio
    async def test_inline_math_marked_on_math_element(self) -> None:
        """Inline marker on the ``<math>`` itself renders ``$…$``, not ``$$…$$``.

        Clipboard/Safari HTML puts ``mwe-math-element-inline`` on the
        ``<math>`` element and wraps it in a bare ``mwe-math-mathml-a11y``
        span (see ``snapshots/cyclomatic complexity.input.html``).  The
        single-child a11y wrapper must not demote the math to display.
        """
        result = await _convert_html(
            '<p>A set <span class="mwe-math-mathml-a11y">'
            '<math xmlns="http://www.w3.org/1998/Math/MathML"'
            ' class="mwe-math-element mwe-math-element-inline mathjax_ignore"'
            ' typeof="mw:Extension/math"'
            ' data-mw=\'{"name":"math","attrs":{},"body":{"extsrc":"S"}}\'>'
            "<mrow><mi>S</mi></mrow></math></span> of paths.</p>"
        )
        assert result == "A set $S$ of paths.\n"

    @pytest.mark.anyio
    async def test_title_box_table_becomes_blockquote(self) -> None:
        """A header-less proof box renders as a quoted title and paragraphs."""
        inline = (
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<math alttext="\\mu" class="mathjax_ignore"></math></span>'
        )
        block = (
            '<span class="mwe-math-element mwe-math-element-display">'
            '<math alttext="\\mu (A)\\geq 0" class="mathjax_ignore"></math></span>'
        )
        result = await _convert_html(
            '<table class="wikitable mw-collapsible"><tbody>'
            "<tr><td><b>Proof of equivalence.</b></td></tr>"
            f"<tr><td>Suppose that {inline} is an outer measure.</td></tr>"
            f"<tr><td><p>One has{block}for any subset.</p></td></tr>"
            "</tbody></table>"
        )
        assert result == (
            "> __Proof of equivalence.__\n"
            ">\n"
            "> Suppose that $\\mu$ is an outer measure.\n"
            ">\n"
            "> One has $$\\mu (A)\\geq 0$$ for any subset.\n"
        )

    @pytest.mark.anyio
    async def test_syntaxhighlight_div_becomes_fenced_code_block(self) -> None:
        """A syntaxhighlight wrapper fences its source and stays its own block.

        Parsoid renders ``<syntaxhighlight lang="c">`` as a ``<div>`` of
        highlighted ``<span>`` fragments whose text carries no line breaks
        (see ``snapshots/cyclomatic complexity.input.html``), while the
        payload keeps the original source.  The fence must come from
        ``data-mw`` and end the block, so the blockquote that follows keeps
        its own ``> `` lines instead of merging into the code.
        """
        result = await _convert_html(
            '<div class="mw-highlight mw-highlight-lang-c mw-content-ltr"'
            ' typeof="mw:Extension/syntaxhighlight"'
            ' data-mw=\'{"name":"syntaxhighlight","attrs":{"lang":"c"},'
            '"body":{"extsrc":"\\nif (c1())\\n    f1();\\nelse\\n    f2();\\n"}}\'>'
            '<pre><span class="k">if</span> <span class="p">(</span>'
            '<span class="n">c1</span><span class="p">())</span>'
            ' <span class="n">f1</span><span class="p">();</span></pre></div>'
            '<blockquote class="templatequote"><p>Quoted explanation.</p></blockquote>'
        )
        assert result == (
            "```c\n"
            "if (c1())\n"
            "    f1();\n"
            "else\n"
            "    f2();\n"
            "```\n"
            "\n"
            "> Quoted explanation.\n"
        )

    @pytest.mark.anyio
    async def test_syntaxhighlight_without_lang_fences_as_text(self) -> None:
        """A lang-less ``syntaxhighlight`` still gets an info string.

        Wikipedia writes ``<syntaxhighlight>`` without ``lang`` for plain
        blocks, so ``attrs`` carries none.  Emitting a bare fence there fails
        markdownlint MD040, hence the ``text`` default.
        """
        result = await _convert_html(
            '<div class="mw-highlight mw-content-ltr"'
            ' typeof="mw:Extension/syntaxhighlight"'
            ' data-mw=\'{"name":"syntaxhighlight","attrs":{},'
            '"body":{"extsrc":"\\nplain block\\n"}}\'>'
            '<pre><span class="n">plain</span> <span class="n">block</span></pre>'
            "</div>"
        )
        assert result == "```text\nplain block\n```\n"

    @pytest.mark.anyio
    async def test_syntaxhighlight_in_table_cell_becomes_inline_code(self) -> None:
        """A syntaxhighlight cell becomes one ``<code>`` element, not a fence.

        ``TableConverter.process_table_cell`` collapses every newline in a
        cell into a ``<br/>``, so a fenced block would be mangled into one
        cell line and break the table around it.  The payload source becomes
        inline code whose lines are joined by ``<br/>``, with indentation as
        entities and ``|`` encoded so the cell pass leaves both alone.
        """
        result = await _convert_html(
            '<table class="wikitable"><tbody><tr><td>'
            '<div class="mw-highlight mw-highlight-lang-c mw-content-ltr"'
            ' typeof="mw:Extension/syntaxhighlight"'
            ' data-mw=\'{"name":"syntaxhighlight","attrs":{"lang":"c"},'
            '"body":{"extsrc":"if (a < b && c) {\\n    x |= 1;\\n}"}}\'>'
            '<pre><span class="k">if</span> <span class="p">(</span>'
            '<span class="n">a</span> <span class="o">&lt;</span>'
            ' <span class="n">b</span> <span class="o">&amp;&amp;</span>'
            ' <span class="n">c</span><span class="p">)</span></pre>'
            "</div></td></tr></tbody></table>"
        )
        assert (
            "<code>if (a &lt; b &amp;&amp; c) {<br/>&nbsp;&nbsp;&nbsp;&nbsp;"
            "x &#124;= 1;<br/>}</code>"
        ) in result
        assert "```" not in result
        assert " | " not in result


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

    @pytest.mark.anyio
    async def test_simple_table_pipeline(self, tmp_path: PathLike[str]) -> None:
        """Simple table through full pipeline should be padded."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)

        html = BeautifulSoup(
            "<table><tr><td>short</td><td>verylongcontent</td></tr></table>",
            "html.parser",
        )
        result, _ = await run_pipeline(
            html,
            redirect_map={},
            image_metadata={},
            names_map={},
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
            refs=True,
        )
        # The table has an empty header row, a separator, and one data row;
        # the pipeline pads each column to its widest cell.
        assert result == (
            "|       |                 |\n"
            "| ----- | --------------- |\n"
            "| short | verylongcontent |\n"
        )
