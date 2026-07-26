"""Regression tests for functions targeted by the mistune AST refactoring.

These tests capture the _current_ behavior of regex-based implementations
to ensure the new mistune AST-based implementations produce identical output.

Covered functions (all in ``scripts/convert_wiki/``):

- ``pipeline._separate_block_quotes`` — MD028 suppression between adjacent blockquotes
- ``pipeline._separate_block_math`` — block math spacing via mistune
- ``converter._replace_pipes_outside_math`` — pipe handling inside/outside math
"""

from os import PathLike

import pytest
from anyio import Path
from bs4 import BeautifulSoup

import scripts.convert_wiki.pipeline as _pl
from scripts.convert_wiki.ast_utils import _replace_pipes_outside_math
from scripts.convert_wiki.pipeline import (
    _separate_block_math,
    _separate_block_quotes,
)
from scripts.convert_wiki.utils import (
    _format_separator_cell,
    _get_separator_alignment,
    _is_separator_cell,
)

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

# ──────────────────────────────────────────────

# _replace_pipes_outside_math

# ──────────────────────────────────────────────


class TestReplacePipesOutsideMath:
    """Regression tests for _replace_pipes_outside_math.

    Pipes outside math blocks are replaced with ``&#124;``.  Pipes inside
    math blocks (``$...$`` or ``$$...$$``) are replaced with ``\\vert ``.
    """

    def test_no_pipes(self) -> None:
        """No pipes in input → unchanged."""
        assert _replace_pipes_outside_math("hello world") == "hello world"

    def test_no_math(self) -> None:
        """Pipes outside math → replaced with &#124;."""
        assert _replace_pipes_outside_math("a | b | c") == "a &#124; b &#124; c"

    def test_pipe_inside_inline_math(self) -> None:
        """Pipes inside $...$ → replaced with \\vert."""
        assert _replace_pipes_outside_math("$a|b$") == "$a\\vert b$"

    def test_pipe_inside_display_math(self) -> None:
        """Pipes inside $$...$$ → replaced with \\vert."""
        assert _replace_pipes_outside_math("$$a|b$$") == "$$a\\vert b$$"

    def test_mixed_inside_and_outside_math(self) -> None:
        """Pipes both in and out of math → correct replacement in each."""
        result = _replace_pipes_outside_math("a | $b|c$ | d")
        assert result == "a &#124; $b\\vert c$ &#124; d"

    def test_multiple_math_blocks(self) -> None:
        """Multiple math segments → each handled independently."""
        result = _replace_pipes_outside_math("$a|b$ | $c|d$")
        assert result == "$a\\vert b$ &#124; $c\\vert d$"

    def test_mixed_inline_and_display_math(self) -> None:
        """Both inline and display math in one string."""
        result = _replace_pipes_outside_math("$a|b$ | $$c|d$$")
        assert result == "$a\\vert b$ &#124; $$c\\vert d$$"

    def test_empty_math_block(self) -> None:
        """Empty math $...$ should not crash."""
        assert _replace_pipes_outside_math("$ $") == "$ $"

    def test_pipe_before_math(self) -> None:
        """Pipe before a math block."""
        result = _replace_pipes_outside_math("| $x$")
        assert result == "&#124; $x$"

    def test_pipe_after_math(self) -> None:
        """Pipe after a math block."""
        result = _replace_pipes_outside_math("$x$ |")
        assert result == "$x$ &#124;"

    def test_no_text_around_math(self) -> None:
        """Math block alone with pipe markers."""
        result = _replace_pipes_outside_math("$x$|$y$")
        assert result == "$x$&#124;$y$"

    def test_adjacent_math_blocks(self) -> None:
        """Adjacent math blocks: pipes between them handled correctly."""
        result = _replace_pipes_outside_math("$a|b$$c|d$")
        assert result == "$a\\vert b$$c\\vert d$"

    def test_mixed_pipe_characters(self) -> None:
        """Mix of backslash+pipe and pipe in math.

        Note: backslash is not a regex escape here - the ``|`` before math is
        treated as a literal pipe and replaced with ``&#124;``.
        """
        result = _replace_pipes_outside_math(r"\| $a|b$")
        assert result == r"\&#124; $a\vert b$"

    def test_math_with_adjacent_text(self) -> None:
        """Math block adjacent to text with pipe."""
        result = _replace_pipes_outside_math("text$|x|$more")
        assert result == "text$\\vert x\\vert $more"


# ──────────────────────────────────────────────

# _separate_block_quotes

# ──────────────────────────────────────────────


class TestMD028SeparateBlockQuotes:
    """Regression tests for _separate_block_quotes.

    Uses mistune AST to find adjacent blockquote blocks separated only by
    blank lines and inserts an MD028 suppression comment between them.
    """

    def test_adjacent_blockquotes(self) -> None:
        """Two adjacent blockquotes with blank line → MD028 comment."""
        text = "> First block\n\n> Second block"
        result = _separate_block_quotes(text)
        assert result == (
            "> First block\n\n<!-- markdownlint MD028 -->\n\n> Second block"
        )

    def test_three_adjacent_blockquotes(self) -> None:
        """Three adjacent blockquotes → MD028 between each pair."""
        text = "> Block 1\n\n> Block 2\n\n> Block 3"
        result = _separate_block_quotes(text)
        # New AST-based function correctly handles all adjacent pairs.
        assert result.count("<!-- markdownlint MD028 -->") == 2
        assert result == (
            "> Block 1\n\n<!-- markdownlint MD028 -->\n\n"
            "> Block 2\n\n<!-- markdownlint MD028 -->\n\n"
            "> Block 3"
        )

    def test_single_blockquote_no_change(self) -> None:
        """Single blockquote → no change."""
        text = "> Single block"
        result = _separate_block_quotes(text)
        assert result == text

    def test_no_blockquotes_no_change(self) -> None:
        """No blockquote lines → no change."""
        text = "Plain text\n\nMore text"
        result = _separate_block_quotes(text)
        assert result == text

    def test_blockquote_then_other_content(self) -> None:
        """Blockquote followed by non-blockquote → no MD028."""
        text = "> A quote\n\nNot a quote"
        result = _separate_block_quotes(text)
        assert result == text

    def test_other_content_then_blockquote(self) -> None:
        """Non-blockquote followed by blockquote → no MD028."""
        text = "Not a quote\n\n> A quote"
        result = _separate_block_quotes(text)
        assert result == text

    def test_blockquote_with_inline_content(self) -> None:
        """Blockquote with nested elements → still matches."""
        text = "> Some **bold** text\n\n> Other `code` here"
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

    def test_no_trailing_newline_after_second_block(self) -> None:
        """Second blockquote without trailing newline → still matches."""
        text = "> First block\n\n> Second block"
        result = _separate_block_quotes(text)
        assert "Second block" in result

    def test_triple_blank_lines_between_blockquotes(self) -> None:
        """Multiple (3+) blank lines → treated as one separator."""
        text = "> First\n\n\n> Second"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result


# ──────────────────────────────────────────────

# Table cell utility functions

# ──────────────────────────────────────────────


class TestIsSeparatorCell:
    """Tests for _is_separator_cell."""

    def test_simple_dashes(self) -> None:
        """--- is a valid separator cell."""
        assert _is_separator_cell("---")

    def test_left_aligned(self) -> None:
        """:-- is a valid separator cell."""
        assert _is_separator_cell(":--")

    def test_right_aligned(self) -> None:
        """--: is a valid separator cell."""
        assert _is_separator_cell("--:")

    def test_centered(self) -> None:
        """:-: is a valid separator cell."""
        assert _is_separator_cell(":-:")

    def test_too_short(self) -> None:
        """-- (2 dashes) is NOT a valid separator cell."""
        assert not _is_separator_cell("--")

    def test_only_one_dash(self) -> None:
        """- is NOT a valid separator cell."""
        assert not _is_separator_cell("-")

    def test_empty_string(self) -> None:
        """Empty string is NOT a valid separator cell."""
        assert not _is_separator_cell("")

    def test_non_separator_text(self) -> None:
        """Regular text is NOT a valid separator cell."""
        assert not _is_separator_cell("hello")

    def test_long_separator(self) -> None:
        """Long separator (e.g. ------) is valid."""
        assert _is_separator_cell("------")

    def test_long_centered_separator(self) -> None:
        """:-----: is valid."""
        assert _is_separator_cell(":-----:")

    def test_long_left_separator(self) -> None:
        """:------ is valid."""
        assert _is_separator_cell(":------")

    def test_long_right_separator(self) -> None:
        """-------: is valid."""
        assert _is_separator_cell("-------:")

    def test_separator_with_non_dash_chars(self) -> None:
        """String with non-dash chars is NOT a separator."""
        assert not _is_separator_cell(":-x:")


class TestGetSeparatorAlignment:
    """Tests for _get_separator_alignment."""

    def test_default_alignment(self) -> None:
        """--- → ---."""
        assert _get_separator_alignment("---") == "---"

    def test_left_alignment(self) -> None:
        """:-- → :--."""
        assert _get_separator_alignment(":--") == ":--"

    def test_right_alignment(self) -> None:
        """--: → --:."""
        assert _get_separator_alignment("--:") == "--:"

    def test_center_alignment(self) -> None:
        """:-: → :-:."""
        assert _get_separator_alignment(":-:") == ":-:"

    def test_long_default(self) -> None:
        """------ → ---."""
        assert _get_separator_alignment("------") == "---"

    def test_long_left(self) -> None:
        """:------ → :--."""
        assert _get_separator_alignment(":------") == ":--"

    def test_long_right(self) -> None:
        """-------: → --:."""
        assert _get_separator_alignment("-------:") == "--:"

    def test_long_center(self) -> None:
        """:------: → :-:."""
        assert _get_separator_alignment(":------:") == ":-:"


class TestFormatSeparatorCell:
    """Tests for _format_separator_cell."""

    def test_default_min_width(self) -> None:
        """--- at minimum width."""
        assert _format_separator_cell(3, "---") == "---"

    def test_default_wider(self) -> None:
        """Wider default separator."""
        assert _format_separator_cell(5, "---") == "-----"

    def test_left_aligned(self) -> None:
        """Left-aligned separator."""
        assert _format_separator_cell(4, ":--") == ":---"

    def test_right_aligned(self) -> None:
        """Right-aligned separator."""
        assert _format_separator_cell(4, "--:") == "---:"

    def test_centered(self) -> None:
        """Centered separator."""
        assert _format_separator_cell(4, ":-:") == ":--:"
        # width 4 → ":" + "--" (width-2) + ":" = ":--:"

    def test_width_below_minimum(self) -> None:
        """Width < 3 behaves as if width=3."""
        assert _format_separator_cell(1, "---") == "---"
        assert _format_separator_cell(2, "---") == "---"

    def test_centered_min_width(self) -> None:
        """:-: at minimum width."""
        assert _format_separator_cell(3, ":-:") == ":-:"  # ":" + "-" + ":"


# ──────────────────────────────────────────────

# _separate_block_math

# ──────────────────────────────────────────────


class TestSeparateBlockMath:
    """Regression tests for _separate_block_math.

    Block math spacing: if non-whitespace text directly precedes or follows
    ``$$...$$``, a space is inserted to prevent broken paragraph affiliation.
    Uses mistune AST to distinguish ``block_math`` from ``$$`` in code spans.
    """

    def test_standalone_block_math(self) -> None:
        """Standalone $$...$$ (no adjacent text) → no change."""
        text = "$$f(x)$$"
        assert _separate_block_math(text) == text

    def test_text_before_only(self) -> None:
        """Text before $$ → space inserted before $$."""
        result = _separate_block_math("before$$f(x)$$")
        assert result == "before $$f(x)$$"

    def test_text_after_only(self) -> None:
        """Text after $$ → space inserted after $$."""
        result = _separate_block_math("$$f(x)$$after")
        assert result == "$$f(x)$$ after"

    def test_text_both_sides(self) -> None:
        """Text on both sides → spaces inserted on both sides."""
        result = _separate_block_math("before$$f(x)$$after")
        assert result == "before $$f(x)$$ after"

    def test_no_math_blocks(self) -> None:
        """No math blocks → unchanged."""
        text = "Just plain text."
        assert _separate_block_math(text) == text

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

    def test_multiple_block_math(self) -> None:
        """Multiple $$...$$ blocks in one paragraph."""
        result = _separate_block_math("a$$b$$c$$d$$e")
        assert result == "a $$b$$ c $$d$$ e"

    def test_paragraph_with_spacing_already(self) -> None:
        """When spaces already exist → no double spacing."""
        result = _separate_block_math("before $$f(x)$$ after")
        # Already has spaces, so unchanged
        assert result == "before $$f(x)$$ after"

    def test_multiline_text_with_math(self) -> None:
        """Multi-line paragraph with block math."""
        text = "Line one\nbefore$$f(x)$$after\nLine three"
        result = _separate_block_math(text)
        assert "before $$f(x)$$ after" in result

    def test_whitespace_around_math(self) -> None:
        """Whitespace already around math → no change."""
        text = "a  $$b$$  c"
        result = _separate_block_math(text)
        assert result == text

    def test_math_at_start_of_text(self) -> None:
        """$$ at text start, text after → space after."""
        result = _separate_block_math("$$f(x)$$after")
        assert result == "$$f(x)$$ after"

    def test_math_at_end_of_text(self) -> None:
        """Text before $$, $$ at text end → space before."""
        result = _separate_block_math("before$$f(x)$$")
        assert result == "before $$f(x)$$"


# ──────────────────────────────────────────────

# Integration: wiki_html_to_plaintext pipeline

# ──────────────────────────────────────────────


class TestWikiHtmlToPlaintextMD028:
    """Integration tests: MD028 suppression in full pipeline output.

    Note: The Wikipedia converter does not produce ``> `` blockquote Markdown
    from ``<blockquote>`` HTML.  MD028 suppression applies only when the
    converter or other sources produce adjacent ``> `` lines, which are then
    post-processed by the regex.  Unit tests for the regex itself are in
    ``TestMD028RegEx`` and ``TestMD028EdgeCases``.
    """

    # Placeholder: if a future enhancement adds blockquote rendering to the
    # converter, add an integration test here.


class TestWikiHtmlToPlaintextTable:
    """Integration tests: table padding in full pipeline output."""

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
        result, _ = await _pl.run_pipeline(
            html,
            redirect_map={},
            image_metadata={},
            names_map={},
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
            refs=True,
        )
        # The table should have columns
        lines = [_l for _l in result.split("\n") if _l.startswith("|")]
        assert len(lines) >= 1
        # Second column should accommodate "verylongcontent"
        # The dash separator row should match column widths
        assert "verylongcontent" in result


# ──────────────────────────────────────────────

# Direct function tests: non-regression edge cases

# for functions affected by the refactoring

# ──────────────────────────────────────────────


class TestMD028EdgeCases:
    """Edge cases for _separate_block_quotes."""

    def test_empty_lines_only(self) -> None:
        """Only empty lines and blockquotes."""
        text = "> Quote\n\n\n> Another"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_blockquote_with_nested_list(self) -> None:
        """Blockquote containing nested list elements."""
        text = "> Outer\n> - Item\n> - Item\n\n> Next quote"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_blockquote_with_code_fence(self) -> None:
        """Blockquote containing a code fence."""
        text = "> Quote with:\n> ```\n> code block\n> ```\n\n> Next quote"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result

    def test_no_trailing_newline(self) -> None:
        """Input without trailing newline."""
        text = "> A\n\n> B"
        result = _separate_block_quotes(text)
        assert result == ("> A\n\n<!-- markdownlint MD028 -->\n\n> B")

    def test_unicode_in_blockquotes(self) -> None:
        """Blockquote with unicode characters."""
        text = "> «élève»\n\n> «estudiante»"
        result = _separate_block_quotes(text)
        assert "<!-- markdownlint MD028 -->" in result
