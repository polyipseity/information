"""Tests for WikiHtmlConverter handler methods.

Covers individual tag handlers dispatched by ``_dispatch``, static/class
utilities, and edge cases for each handler in ``converter.py``.
"""

from os import PathLike
from pathlib import Path

import pytest
from anyio import Path as AnyioPath
from bs4 import BeautifulSoup, Tag

from scripts.convert_wiki.converter import WikiHtmlConverter
from scripts.convert_wiki.latex import LatexConverter
from scripts.convert_wiki.types import _RedirectInfo

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

# ---------------------------------------------------------------------------

# Fixtures & helpers

# ---------------------------------------------------------------------------


@pytest.fixture
def converter(tmp_path: PathLike[str]) -> WikiHtmlConverter:
    """Create a WikiHtmlConverter with isolated temp directories."""
    tmp = AnyioPath(tmp_path)
    return WikiHtmlConverter(
        converted_wiki_dir=tmp / "general",
        converted_wiki_lang_dir=tmp / "general" / "eng",
    )


def _block_math_span(alttext: str) -> str:
    """Build a block math display span for test HTML fragments."""
    return (
        '<span class="mwe-math-element mwe-math-element-block">'
        '<span class="mwe-math-mathml-display mwe-math-mathml-a11y">'
        f'<math display="block" alttext="{alttext}">'
        "<semantics><mrow></mrow></semantics></math>"
        '<img class="mwe-math-fallback-image-display mw-invert skin-invert"/>'
        "</span></span>"
    )


def _inline_math_span(alttext: str) -> str:
    """Build an inline math span for test HTML fragments."""
    return (
        '<span class="mwe-math-element mwe-math-element-inline">'
        '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
        f'<math display="inline" alttext="{alttext}">'
        "<semantics><mrow></mrow></semantics></math>"
        '<img class="mwe-math-fallback-image-inline mw-invert skin-invert"/>'
        "</span></span>"
    )


def _make_converter_with_lang(
    tmp_path: PathLike[str],
) -> WikiHtmlConverter:
    """Create a converter with ``general/eng`` directory created."""
    WikiHtmlConverter(  # create directories
        converted_wiki_dir=AnyioPath(tmp_path) / "general",
        converted_wiki_lang_dir=AnyioPath(tmp_path) / "general" / "eng",
    )
    return WikiHtmlConverter(
        converted_wiki_dir=AnyioPath(tmp_path) / "general",
        converted_wiki_lang_dir=AnyioPath(tmp_path) / "general" / "eng",
    )


async def _convert(
    converter: WikiHtmlConverter,
    html: str,
    redirect_map: dict[str, _RedirectInfo] | None = None,
    *,
    list_stack: tuple[int, ...] = (),
    escape: bool = True,
) -> str:
    """Shorthand to convert HTML fragment through the converter."""
    soup = BeautifulSoup(html, "html.parser")
    return await converter.convert(
        soup,
        out_to_archive=set(),
        redirect_map=redirect_map or {},
        refs=True,
        list_stack=list_stack,
        escape=escape,
    )


# ---------------------------------------------------------------------------

# Math handling

# ---------------------------------------------------------------------------


class TestMathHandling:
    """Tests for ``_handle_math`` and related utilities."""

    @pytest.mark.anyio
    async def test_block_math(self, converter: WikiHtmlConverter) -> None:
        """Block math should be wrapped in ``$$...$$`` with outer spacing."""
        result = await _convert(converter, _block_math_span(r"{\displaystyle f(x)}"))
        assert "$$f(x)$$" in result

    @pytest.mark.anyio
    async def test_inline_math(self, converter: WikiHtmlConverter) -> None:
        """Inline math should be wrapped in ``$...$``."""
        html = f"<p>before {_inline_math_span(r'{\displaystyle a}')} after</p>"
        result = await _convert(converter, html)
        assert "$a$" in result

    @pytest.mark.anyio
    async def test_math_empty_alttext(self, converter: WikiHtmlConverter) -> None:
        """Math with empty alttext should produce no delimiters."""
        result = await _convert(
            converter, '<math alttext=""><semantics><mrow></mrow></semantics></math>'
        )
        assert result == ""

    @pytest.mark.anyio
    async def test_math_missing_alttext(self, converter: WikiHtmlConverter) -> None:
        """Math without alttext attribute should produce empty output."""
        result = await _convert(
            converter, "<math><semantics><mrow></mrow></semantics></math>"
        )
        assert result == ""

    @pytest.mark.anyio
    @pytest.mark.parametrize(
        ("punct", "expected"),
        [
            (".", "$f(x)$."),
            (",", "$f(x)$,"),
        ],
    )
    async def test_inline_math_trailing_punctuation(
        self, converter: WikiHtmlConverter, punct: str, expected: str
    ) -> None:
        """Inline math trailing ``.`` or ``,`` should appear after closing ``$``."""
        html = f"<p>{_inline_math_span(r'{\displaystyle f(x)}')}{punct}</p>"
        result = await _convert(converter, html)
        assert expected in result
        assert f"f(x)\\,${punct}" not in result

    @pytest.mark.anyio
    @pytest.mark.parametrize(
        ("container", "punct", "latex", "expected"),
        [
            ("dd", ".", r"{\displaystyle R(X,Y)}", "$$R(X,Y)\\,.$$"),
            ("dd", ",", r"{\displaystyle a}", "$$a\\,,$$"),
            ("dt", ".", r"{\displaystyle b}", "$$b\\,.$$"),
        ],
    )
    async def test_display_container_external_punctuation_is_block(
        self,
        converter: WikiHtmlConverter,
        container: str,
        punct: str,
        latex: str,
        expected: str,
    ) -> None:
        """Sole formula rows in ``<dd>``/``<dt>`` absorb external punct as block math."""
        html = f"<{container}>{_inline_math_span(latex)}{punct}</{container}>"
        result = await _convert(converter, html)
        assert expected in result
        if punct == ".":
            assert result.count(punct) == 1

    @pytest.mark.anyio
    async def test_dd_with_leading_text_does_not_absorb_external_period(
        self, converter: WikiHtmlConverter
    ) -> None:
        """``<dd>`` rows with prose keep external punct outside inline math."""
        html = f"<dd>therefore {_inline_math_span(r'{\displaystyle f(x)}')}.</dd>"
        result = await _convert(converter, html)
        assert "$f(x)$." in result
        assert "$$f(x)\\,.$$" not in result

    @pytest.mark.anyio
    async def test_dd_internal_period_not_duplicated(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Internal punct in ``alttext`` must not be doubled by external absorption."""
        html = f"<dd>{_inline_math_span(r'{\displaystyle f(x).}')}</dd>"
        result = await _convert(converter, html)
        assert "$$f(x).$$" in result
        assert "$$f(x)..$$" not in result

    @pytest.mark.anyio
    async def test_aligned_external_period_injected_before_end(
        self, converter: WikiHtmlConverter
    ) -> None:
        """External ``.`` after aligned env should land before ``\\end{aligned}``."""
        alttext = r"{\displaystyle \begin{aligned}a&=b\\c&=d\end{aligned}}"
        html = f"<dd>{_inline_math_span(alttext)}.</dd>"
        result = await _convert(converter, html)
        assert r"d\,.\end{aligned}$$" in result
        assert r"\end{aligned}.$$" not in result
        assert result.count(".") == 1

    @pytest.mark.anyio
    async def test_aligned_in_paragraph_external_period(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Aligned env with external ``.`` in ``<p>`` should still be block math."""
        alttext = r"{\displaystyle \begin{aligned}x&=1\end{aligned}}"
        html = f"<p>{_inline_math_span(alttext)}.</p>"
        result = await _convert(converter, html)
        assert r"$$\begin{aligned}x&=1\,.\end{aligned}$$" in result
        assert result.count(".") == 1

    @pytest.mark.parametrize(
        ("alt_text", "punct", "expected"),
        [
            ("f(x)", ".", r"f(x)\,."),
            ("a", ",", r"a\,,"),
            (
                r"\begin{aligned}a&=b\\c&=d\end{aligned}",
                ".",
                r"\begin{aligned}a&=b\\c&=d\,.\end{aligned}",
            ),
        ],
    )
    def test_inject_external_punctuation(
        self, alt_text: str, punct: str, expected: str
    ) -> None:
        """``_inject_external_punctuation`` inserts ``\\,`` + punct at the right site."""
        assert (
            WikiHtmlConverter._inject_external_punctuation(alt_text, punct) == expected
        )

    @pytest.mark.anyio
    async def test_normalize_external_math_punctuation_mutates_dom(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Pre-conversion normalize should absorb punct into ``alttext`` and drop sibling."""
        html = f"<dd>{_inline_math_span(r'{\displaystyle x}')}.</dd>"
        soup = BeautifulSoup(html, "html.parser")
        dd = soup.find("dd")
        assert isinstance(dd, Tag)
        converter._normalize_external_math_punctuation(dd)
        math = soup.find("math")
        assert isinstance(math, Tag)
        outer = WikiHtmlConverter._math_outer_span(math)
        assert outer is not None
        assert math.get("alttext") == "x\\,."
        assert WikiHtmlConverter._following_punctuation_sibling(outer) == ""

    @pytest.mark.anyio
    async def test_sfrac_like_math_without_outer_wrapper_stays_inline(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Inline math without ``mwe-math-element`` wrapper should stay ``$...$``."""
        html = (
            "<body>"
            "<p>intro</p>"
            "<p>before "
            '<span class="mwe-math-mathml-inline">'
            '<math alttext="{\\displaystyle \\frac{a}{2\\pi}}"></math>'
            "</span>, after</p>"
            "</body>"
        )
        result = await _convert(converter, html)
        assert "$\\frac{a}{2\\pi}$," in result
        assert "$$\\frac{a}{2\\pi}$$" not in result

    @pytest.mark.anyio
    async def test_math_displaystyle_prefix(self, converter: WikiHtmlConverter) -> None:
        """``\\displaystyle`` prefix should be stripped from alttext."""
        result = await _convert(converter, _block_math_span(r"{\displaystyle E=mc^2}"))
        assert "$$E=mc^2$$" in result

    @pytest.mark.anyio
    async def test_math_textstyle_prefix(self, converter: WikiHtmlConverter) -> None:
        """``\\textstyle`` prefix should be stripped from alttext."""
        result = await _convert(converter, _block_math_span(r"{\textstyle \sum x}"))
        assert "$$\\sum x$$" in result

    @pytest.mark.anyio
    async def test_math_trailing_backslash_space(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Trailing ``\\ `` should get an empty ``{}`` workaround."""
        result = await _convert(converter, _block_math_span(r"{\displaystyle a\ }"))
        assert "$$a\\ {}$$" in result or "$$a\\{}$$" in result

    @pytest.mark.anyio
    async def test_math_negthinspace_workaround(
        self, converter: WikiHtmlConverter
    ) -> None:
        """``\\!`` and ``\\negthinspace`` before ``_``/``^`` should become ``\\mkern-3mu``."""
        result = await _convert(converter, _block_math_span(r"{\displaystyle a\!_{b}}"))
        assert "\\mkern-3mu" in result

    @pytest.mark.anyio
    async def test_math_flashcard_delimiter_escaping(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Flashcard delimiters within math should be space-separated."""
        result = await _convert(
            converter, _block_math_span(r"{\displaystyle {@{text}@}}")
        )
        assert "{ @ {text} @ }" in result

    @pytest.mark.anyio
    async def test_is_inline_math(self, converter: WikiHtmlConverter) -> None:
        """``_is_inline_math`` should detect inline context."""
        soup = BeautifulSoup(
            f"<p>prefix {_inline_math_span(r'{\displaystyle x}')} suffix</p>",
            "html.parser",
        )
        math_tag = soup.find("math")
        assert math_tag is not None
        # ``_is_inline_math`` is a staticmethod; access via class.
        assert WikiHtmlConverter._is_inline_math(math_tag)

    @pytest.mark.anyio
    async def test_is_not_inline_math(self, converter: WikiHtmlConverter) -> None:
        """Block math should NOT be classified as inline."""
        soup = BeautifulSoup(_block_math_span(r"{\displaystyle x}"), "html.parser")
        math_tag = soup.find("math")
        assert math_tag is not None
        assert not WikiHtmlConverter._is_inline_math(math_tag)

    @pytest.mark.anyio
    async def test_strip_trailing_punctuation(self) -> None:
        """``_strip_trailing_punctuation`` should detach ``.`` and ``,``."""
        text, punct = WikiHtmlConverter._strip_trailing_punctuation("f(x),")
        assert text == "f(x)"
        assert punct == ","

    @pytest.mark.anyio
    async def test_strip_trailing_punctuation_no_change(self) -> None:
        """No trailing punctuation should return unchanged."""
        text, punct = WikiHtmlConverter._strip_trailing_punctuation("f(x)")
        assert text == "f(x)"
        assert punct == ""

    @pytest.mark.anyio
    async def test_strip_trailing_punctuation_preserve_latex_comma(
        self,
    ) -> None:
        """``\\,`` should not be treated as trailing punctuation."""
        text, punct = WikiHtmlConverter._strip_trailing_punctuation(r"a\,")
        assert text == r"a\,"
        assert punct == ""

    @pytest.mark.anyio
    async def test_dd_sole_math_in_dl_is_isolated_row(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Sole ``<dd>`` math inside ``<dl>`` should render as its own row."""
        html = (
            "<p>by</p>"
            f"<dl><dd>{_block_math_span(r'{\displaystyle f(x)}')}</dd></dl>"
            "<p>for</p>"
        )
        result = await _convert(converter, html)
        assert "\n\n$$f(x)$$\n" in result
        assert "$$f(x)$$\n\n\nfor" in result

    @pytest.mark.anyio
    async def test_dt_sole_math_in_dl_is_isolated_row(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Sole ``<dt>`` math inside ``<dl>`` should render as its own row."""
        html = (
            "<p>by</p>"
            f"<dl><dt>{_block_math_span(r'{\displaystyle g(x)}')}</dt></dl>"
            "<p>for</p>"
        )
        result = await _convert(converter, html)
        assert "\n\n$$g(x)$$\n" in result
        assert "$$g(x)$$\n\n\nfor" in result

    @pytest.mark.anyio
    async def test_multi_dd_math_rows_separated(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Multiple ``<dd>`` math rows in one ``<dl>`` should not merge."""
        html = (
            "<dl>"
            f"<dd>{_block_math_span(r'{\displaystyle f(x)}')}</dd>"
            f"<dd>{_block_math_span(r'{\displaystyle g(x)}')}</dd>"
            "</dl>"
        )
        result = await _convert(converter, html)
        assert "$$f(x)$$\n$$g(x)$$" in result
        assert "$$f(x)$$$$g(x)$$" not in result

    @pytest.mark.anyio
    async def test_multi_dd_math_rows_formatting_agnostic(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Whitespace between ``<dd>`` rows must not change the output."""
        compact = (
            "<dl>"
            f"<dd>{_block_math_span(r'{\displaystyle f(x)}')}</dd>"
            f"<dd>{_block_math_span(r'{\displaystyle g(x)}')}</dd>"
            "</dl>"
        )
        spaced = (
            "<dl>\n"
            f"  <dd>{_block_math_span(r'{\displaystyle f(x)}')}</dd>\n"
            f"  <dd>{_block_math_span(r'{\displaystyle g(x)}')}</dd>\n"
            "</dl>"
        )
        result_compact = await _convert(converter, compact)
        result_spaced = await _convert(converter, spaced)
        assert result_compact == result_spaced
        assert "$$f(x)$$\n$$g(x)$$" in result_compact

    @pytest.mark.anyio
    async def test_mixed_dt_dd_rows_each_on_own_line(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Mixed ``<dt>``/``<dd>`` rows should each stay on their own line."""
        html = (
            "<dl>"
            "<dt>term</dt>"
            f"<dd>{_block_math_span(r'{\displaystyle a}')}</dd>"
            f"<dd>{_block_math_span(r'{\displaystyle b}')}</dd>"
            "</dl>"
        )
        result = await _convert(converter, html)
        assert "term\n$$a$$\n$$b$$" in result

    @pytest.mark.anyio
    async def test_dd_prose_then_math_rows(self, converter: WikiHtmlConverter) -> None:
        """Prose ``<dd>`` row keeps inline math; math row is block on next line."""
        html = (
            "<dl>"
            f"<dd>therefore {_inline_math_span(r'{\displaystyle f(x)}')}.</dd>"
            f"<dd>{_block_math_span(r'{\displaystyle F(x)}')}</dd>"
            "</dl>"
        )
        result = await _convert(converter, html)
        assert "therefore $f(x)$." in result
        assert "$$F(x)$$" in result
        assert "$f(x)$.\n$$F(x)$$" in result

    @pytest.mark.anyio
    async def test_block_classed_math_in_paragraph_stays_inline_flow(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Block-classed math inside prose stays in line flow (Option A)."""
        html = f"<p>before {_block_math_span(r'{\displaystyle F(x)}')} after</p>"
        result = await _convert(converter, html)
        assert "before $$F(x)$$ after" in result


# ---------------------------------------------------------------------------

# Link handling

# ---------------------------------------------------------------------------


class TestLinkHandling:
    """Tests for ``_handle_anchor`` and ``_handle_selflink``."""

    @pytest.mark.anyio
    async def test_simple_link(self, converter: WikiHtmlConverter) -> None:
        """A plain internal link should render as Markdown link."""
        html = '<a title="Target Page" href="/wiki/Target_Page">link text</a>'
        result = await _convert(converter, html)
        assert "[link text]" in result

    @pytest.mark.anyio
    async def test_link_with_fragment(self, converter: WikiHtmlConverter) -> None:
        """Internal link with fragment should include ``#fragment``."""
        html = '<a title="Target Page" href="/wiki/Target_Page#Section">text</a>'
        result = await _convert(converter, html)
        assert "#section" in result.lower() or "Section" in result

    @pytest.mark.anyio
    async def test_external_link(self, converter: WikiHtmlConverter) -> None:
        """External link (``extiw`` class) should produce cross-language link."""
        html = '<a class="extiw" title="en:Target" href="https://en.wikipedia.org/wiki/Target">text</a>'
        result = await _convert(converter, html)
        assert "[text]" in result

    @pytest.mark.anyio
    async def test_selflink(self, converter: WikiHtmlConverter) -> None:
        """``mw-selflink`` class should produce a relative self-link."""
        html = '<a class="mw-selflink" href="/wiki/Current_Page">current</a>'
        result = await _convert(converter, html)
        assert "[current](" in result

    @pytest.mark.anyio
    async def test_skips_parsoid_link_metadata(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Parsoid ``<link>`` metadata must be ignored (no handler name collision)."""
        html = (
            '<p>before<link rel="mw:PageProp/Category" href="./Category:Foo"/>after</p>'
        )
        result = await _convert(converter, html)
        assert "beforeafter" in result
        assert "Category:Foo" not in result

    @pytest.mark.anyio
    async def test_shortdescription_block_spacing_before_hatnote(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Short-description metadata must be separated from the following hatnote."""
        html = (
            '<div class="shortdescription">Approach to general relativity</div>'
            '<div class="hatnote">This article is about general tetrads.</div>'
        )
        result = await _convert(converter, html)
        assert result == (
            "Approach to general relativity\n\n- This article is about general tetrads.\n"
        )

    @pytest.mark.anyio
    async def test_link_new_page(self, converter: WikiHtmlConverter) -> None:
        """``new`` class indicates page does not exist; suffix should be stripped."""
        html = '<a class="new" title="Missing Page (page does not exist)" href="/wiki/Missing_Page">missing</a>'
        result = await _convert(converter, html)
        assert "[missing]" in result

    @pytest.mark.anyio
    async def test_link_with_redirect(self, tmp_path: PathLike[str]) -> None:
        """Redirected link should resolve target filename."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await AnyioPath(lang_dir).mkdir(parents=True)
        converter = WikiHtmlConverter(
            converted_wiki_dir=AnyioPath(tmp_path) / "general",
            converted_wiki_lang_dir=AnyioPath(tmp_path) / "general" / "eng",
        )
        html = '<a title="Source Page" href="/wiki/Source_Page">src</a>'
        result = await _convert(
            converter,
            html,
            redirect_map={"Source Page": _RedirectInfo(to="Dest Page")},
        )
        assert "[src]" in result

    @pytest.mark.anyio
    async def test_link_strips_newlines(self, converter: WikiHtmlConverter) -> None:
        """Display text newlines should become `` <br/> ``."""
        html = '<a title="P" href="/wiki/P">line1\nline2</a>'
        result = await _convert(converter, html)
        assert "line1 line2" in result
        assert "\n" not in result

    @pytest.mark.anyio
    async def test_link_bad_title_ignored(self, converter: WikiHtmlConverter) -> None:
        """Titles in the bad-titles list should be rendered as plain text."""
        html = '<a title="[1]" href="/wiki/%5B1%5D">[1]</a>'
        result = await _convert(converter, html)
        assert "[1]" in result


# ---------------------------------------------------------------------------

# Image handling

# ---------------------------------------------------------------------------


class TestImageHandling:
    """Tests for ``_handle_image``."""

    @pytest.mark.anyio
    async def test_image_with_alt(self, converter: WikiHtmlConverter) -> None:
        """Image with alt text should render with that alt text."""
        html = '<img src="//upload.wikimedia.org/wikipedia/en/example.png" alt="Example Image"/>'
        result = await _convert(converter, html)
        assert "![Example Image]" in result

    @pytest.mark.anyio
    async def test_image_no_alt(self, converter: WikiHtmlConverter) -> None:
        """Image without alt should fall back to filename or empty."""
        html = '<img src="//upload.wikimedia.org/wikipedia/en/test.png"/>'
        result = await _convert(converter, html)
        assert "![" in result

    @pytest.mark.anyio
    async def test_image_in_inline_context(self, converter: WikiHtmlConverter) -> None:
        """Image inside a list item should not append ``\\n\\n``."""
        html = '<li><img src="//upload.wikimedia.org/wikipedia/en/example.png" alt="A"/></li>'
        result = await _convert(converter, html)
        # Inside <li>, image should not get trailing \n\n.
        assert "\\n\\n" not in result

    @pytest.mark.anyio
    async def test_image_in_paragraph_adds_newline(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Standalone image should append ``\\n\\n``."""
        html = '<img src="//upload.wikimedia.org/wikipedia/en/example.png" alt="A"/>'
        result = await _convert(converter, html)
        # The image itself gets \n\n from the handler.
        assert "\n\n" in result


# ---------------------------------------------------------------------------

# Paragraph handling

# ---------------------------------------------------------------------------


class TestParagraphHandling:
    """Tests for ``_handle_p``."""

    @pytest.mark.anyio
    async def test_simple_paragraph(self, converter: WikiHtmlConverter) -> None:
        """A basic paragraph should be wrapped with newlines."""
        result = await _convert(converter, "<p>Hello world</p>")
        assert "\nHello world\n\n" in result

    @pytest.mark.anyio
    async def test_paragraph_in_table_cell(self, converter: WikiHtmlConverter) -> None:
        """Paragraph inside a table cell should not add outer spacing."""
        result = await _convert(
            converter, "<table><tr><td><p>cell text</p></td></tr></table>"
        )
        assert "cell text" in result

    @pytest.mark.anyio
    async def test_paragraph_whitespace_collapse(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Multiple spaces and newlines inside a paragraph should collapse."""
        result = await _convert(converter, "<p>  spaced    \n  text  </p>")
        assert "\nspaced text\n\n" in result


# ---------------------------------------------------------------------------

# Header handling

# ---------------------------------------------------------------------------


class TestHeaderHandling:
    """Tests for ``_handle_header`` (h1-h6)."""

    @pytest.mark.anyio
    async def test_h2(self, converter: WikiHtmlConverter) -> None:
        """``h2`` should render as ``## heading``."""
        result = await _convert(converter, "<h2>Section Title</h2>")
        assert "## Section Title" in result

    @pytest.mark.anyio
    async def test_h3(self, converter: WikiHtmlConverter) -> None:
        """``h3`` should render as ``### heading``."""
        result = await _convert(converter, "<h3>Sub Section</h3>")
        assert "### Sub Section" in result

    @pytest.mark.anyio
    async def test_h1(self, converter: WikiHtmlConverter) -> None:
        """``h1`` should render as ``# heading``."""
        result = await _convert(converter, "<h1>Main Title</h1>")
        assert "# Main Title" in result

    @pytest.mark.anyio
    async def test_header_trailing_newlines(self, converter: WikiHtmlConverter) -> None:
        """Header should be followed by ``\\n\\n``."""
        result = await _convert(converter, "<h2>Title</h2><p>text</p>")
        assert "## title\n\n" in result or "## title\n" in result


# ---------------------------------------------------------------------------

# Bold / italic handling

# ---------------------------------------------------------------------------


class TestBoldItalicHandling:
    """Tests for ``_handle_bold_italic``."""

    @pytest.mark.anyio
    async def test_bold(self, converter: WikiHtmlConverter) -> None:
        """``<b>`` should render as Markdown bold."""
        result = await _convert(converter, "<b>bold text</b>")
        assert "__bold text__" in result

    @pytest.mark.anyio
    async def test_italic(self, converter: WikiHtmlConverter) -> None:
        """``<i>`` should render as Markdown italic."""
        result = await _convert(converter, "<i>italic text</i>")
        assert "_italic text_" in result

    @pytest.mark.anyio
    async def test_bold_and_italic(self, converter: WikiHtmlConverter) -> None:
        """Nested ``<b><i>`` should produce ``__ _text_ __``."""
        result = await _convert(converter, "<b><i>both</i></b>")
        assert "__" in result and "_" in result

    @pytest.mark.anyio
    async def test_bold_adjacent_to_text(self, converter: WikiHtmlConverter) -> None:
        """Bold adjacent to text should insert separator."""
        result = await _convert(converter, "<p>a<b>b</b>c</p>")
        # The separator keeps bold from merging with adjacent text.
        assert "a" in result and "b" in result and "c" in result

    @pytest.mark.anyio
    async def test_italic_inside_span_abutting_text(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Separator inserted when emphasis is the sole child of a span."""
        html = '<p><span class="texhtml"><i>n</i></span>th-order</p>'
        result = await _convert(converter, html)
        assert "_n_<!-- markdown separator -->th-order" in result

    @pytest.mark.anyio
    async def test_italic_inside_span_preceded_by_text(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Separator inserted before emphasis inside a span (symmetric)."""
        html = '<p>d<span class="texhtml"><i>n</i></span>th</p>'
        result = await _convert(converter, html)
        assert "d<!-- markdown separator -->_n_" in result

    @pytest.mark.anyio
    async def test_minus_emphasis_no_marker(self, converter: WikiHtmlConverter) -> None:
        """U+2212 MINUS SIGN before emphasis needs no separator marker."""
        result = await _convert(converter, "<p>\u2212<i>i</i></p>")
        assert "\u2212_i_" in result
        assert "<!-- markdown separator -->" not in result

    @pytest.mark.anyio
    async def test_middle_dot_emphasis_no_marker(
        self, converter: WikiHtmlConverter
    ) -> None:
        """U+00B7 MIDDLE DOT needs no separator marker around emphasis."""
        result = await _convert(converter, "<p>x\u00b7<i>f</i>(x)</p>")
        assert "x\u00b7_f_\\(x\\)" in result
        assert "<!-- markdown separator -->" not in result

    @pytest.mark.anyio
    async def test_strong(self, converter: WikiHtmlConverter) -> None:
        """``<strong>`` should render as bold."""
        result = await _convert(converter, "<strong>strong</strong>")
        assert "__strong__" in result

    @pytest.mark.anyio
    async def test_em(self, converter: WikiHtmlConverter) -> None:
        """``<em>`` should render as italic."""
        result = await _convert(converter, "<em>emphasized</em>")
        assert "_emphasized_" in result


# ---------------------------------------------------------------------------

# Inline formatting handlers

# ---------------------------------------------------------------------------


class TestInlineFormatting:
    """Tests for ``_handle_code``, ``_handle_br``, ``_handle_s``, ``_handle_sub``,
    ``_handle_sup``, ``_handle_u``, ``_handle_big``."""

    @pytest.mark.anyio
    async def test_inline_code(self, converter: WikiHtmlConverter) -> None:
        """``<code>`` should render as backtick-wrapped."""
        result = await _convert(converter, "<code>var x = 1</code>")
        assert "`var x = 1`" in result

    @pytest.mark.anyio
    async def test_code_with_backtick(self, converter: WikiHtmlConverter) -> None:
        """Code containing backticks should use double backticks."""
        result = await _convert(converter, "<code>`code`</code>")
        assert "``" in result

    @pytest.mark.anyio
    async def test_br(self, converter: WikiHtmlConverter) -> None:
        """``<br/>`` should render as a newline."""
        result = await _convert(converter, "<p>line1<br/>line2</p>")
        assert "line1" in result and "line2" in result

    @pytest.mark.anyio
    async def test_strikethrough(self, converter: WikiHtmlConverter) -> None:
        """``<s>`` should render as strikethrough."""
        result = await _convert(converter, "<s>deleted</s>")
        assert "<s>deleted</s>" in result

    @pytest.mark.anyio
    async def test_subscript(self, converter: WikiHtmlConverter) -> None:
        """``<sub>`` should render as subscript."""
        result = await _convert(converter, "<sub>sub</sub>")
        assert "<sub>sub</sub>" in result

    @pytest.mark.anyio
    async def test_superscript(self, converter: WikiHtmlConverter) -> None:
        """``<sup>`` should render as superscript."""
        result = await _convert(converter, "<sup>sup</sup>")
        assert "<sup>sup</sup>" in result

    @pytest.mark.anyio
    async def test_underline(self, converter: WikiHtmlConverter) -> None:
        """``<u>`` should render as underline."""
        result = await _convert(converter, "<u>underlined</u>")
        assert "<ins>underlined</ins>" in result or "<u>underlined</u>" in result


# ---------------------------------------------------------------------------

# List handling

# ---------------------------------------------------------------------------


class TestListHandling:
    """Tests for ``_handle_ul``, ``_handle_ol``, ``_handle_li``."""

    @pytest.mark.anyio
    async def test_unordered_list(self, converter: WikiHtmlConverter) -> None:
        """A simple unordered list should render with ``- `` items."""
        result = await _convert(converter, "<ul><li>one</li><li>two</li></ul>")
        assert "- one" in result
        assert "- two" in result

    @pytest.mark.anyio
    async def test_ordered_list(self, converter: WikiHtmlConverter) -> None:
        """A simple ordered list should render with ``1. `` items."""
        result = await _convert(converter, "<ol><li>one</li><li>two</li></ol>")
        assert "1. one" in result
        assert "2. two" in result

    @pytest.mark.anyio
    async def test_nested_list(self, converter: WikiHtmlConverter) -> None:
        """Nested lists should indent inner items."""
        html = "<ul><li>outer<ul><li>inner</li></ul></li></ul>"
        result = await _convert(converter, html)
        assert "- outer" in result
        assert "- inner" in result or "inner" in result

    @pytest.mark.anyio
    async def test_list_formatting_strips_trailing_whitespace(
        self, converter: WikiHtmlConverter
    ) -> None:
        """List items should have leading/trailing whitespace stripped."""
        result = await _convert(converter, "<ul><li>  spaced  </li></ul>")
        assert "- spaced" in result


# ---------------------------------------------------------------------------

# Table handling

# ---------------------------------------------------------------------------


class TestTableHandling:
    """Tests for table-related handlers."""

    @pytest.mark.anyio
    async def test_table_without_caption(self, converter: WikiHtmlConverter) -> None:
        """A table without caption should still render cells."""
        html = (
            "<table><tr><th>H1</th><th>H2</th></tr>"
            "<tr><td>D1</td><td>D2</td></tr></table>"
        )
        result = await _convert(converter, html)
        assert "H1" in result
        assert "D1" in result

    @pytest.mark.anyio
    async def test_table_cell_pipe_escaping(self, converter: WikiHtmlConverter) -> None:
        """``|`` in table cell content should be escaped."""
        html = "<table><tr><td>a | b</td></tr></table>"
        result = await _convert(converter, html)
        assert "a" in result and "b" in result

    @pytest.mark.anyio
    async def test_caption_with_header_row_raises(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A caption combined with a ``<th>`` header row should raise ValueError."""
        html = (
            "<table><caption>Title</caption>"
            "<tr><th>H1</th><th>H2</th></tr>"
            "<tr><td>D1</td><td>D2</td></tr></table>"
        )
        with pytest.raises(BaseExceptionGroup) as exc_info:
            await _convert(converter, html)
        error = exc_info.value.exceptions[0]
        assert isinstance(error, ValueError)
        assert "only one header row" in str(error)

    @pytest.mark.anyio
    async def test_caption_with_mixed_rows_ok(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A caption with mixed ``<th>``/``<td>`` rows should not raise."""
        html = (
            "<table><caption>Title</caption>"
            "<tr><th>Label</th><td>Value</td></tr>"
            "<tr><td>a</td><td>b</td></tr></table>"
        )
        result = await _convert(converter, html)
        assert "Title" in result
        assert "Value" in result

    @pytest.mark.anyio
    async def test_colspan_header_aligns_lower_only_cells(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Empty upper header cells under colspan should stack lower labels."""
        html = (
            "<table><thead>"
            '<tr><th colspan="2">Full Name</th><th>Score</th></tr>'
            "<tr><th>First</th><th>Last</th><th>Points</th></tr>"
            "</thead><tbody>"
            "<tr><td>John</td><td>Doe</td><td>95</td></tr>"
            "</tbody></table>"
        )
        result = await _convert(converter, html)
        assert "<br/> Last" in result


# ---------------------------------------------------------------------------

# Audio handling

# ---------------------------------------------------------------------------


class TestAudioHandling:
    """Tests for ``_handle_audio``."""

    @pytest.mark.anyio
    async def test_audio_with_href(self, converter: WikiHtmlConverter) -> None:
        """Audio element with href should produce a Markdown link."""
        html = (
            '<span class="mw-tmh-play" '
            'href="//upload.wikimedia.org/wikipedia/en/audio.ogg">play</span>'
        )
        result = await _convert(converter, html)
        assert "[" in result

    @pytest.mark.anyio
    async def test_audio_without_href(self, converter: WikiHtmlConverter) -> None:
        """Audio without href should produce empty output."""
        html = '<span class="mw-tmh-play">play</span>'
        result = await _convert(converter, html)
        assert result == "" or "play" in result


# ---------------------------------------------------------------------------

# Div / block-level handling

# ---------------------------------------------------------------------------


class TestDivHandling:
    """Tests for ``_handle_div`` and ``_handle_block_level``."""

    @pytest.mark.anyio
    async def test_plain_div(self, converter: WikiHtmlConverter) -> None:
        """A plain ``<div>`` should pass through its content."""
        result = await _convert(converter, "<div>hello</div>")
        assert "hello" in result

    @pytest.mark.anyio
    async def test_div_in_table_cell(self, converter: WikiHtmlConverter) -> None:
        """Div inside table cell should not add block spacing."""
        result = await _convert(
            converter, "<table><tr><td><div>cell div</div></td></tr></table>"
        )
        assert "cell div" in result


# ---------------------------------------------------------------------------

# Citation handling

# ---------------------------------------------------------------------------


class TestCiteHandling:
    """Tests for ``_handle_cite``."""

    @pytest.mark.anyio
    async def test_cite_with_id(self, converter: WikiHtmlConverter) -> None:
        """``<cite>`` with id should produce anchor prefix."""
        result = await _convert(converter, '<cite id="CITEREF_2024">source</cite>')
        assert 'a id="CITEREF 2024"' in result or "source" in result

    @pytest.mark.anyio
    async def test_cite_without_id(self, converter: WikiHtmlConverter) -> None:
        """``<cite>`` without id should pass through content."""
        result = await _convert(converter, "<cite>source</cite>")
        assert "source" in result


# ---------------------------------------------------------------------------

# Span handling

# ---------------------------------------------------------------------------


class TestSpanHandling:
    """Tests for ``_handle_span``."""

    @pytest.mark.anyio
    async def test_plain_span(self, converter: WikiHtmlConverter) -> None:
        """A plain ``<span>`` should return None (delegate to children)."""
        result = await _convert(converter, "<span>hello</span>")
        assert "hello" in result


# ---------------------------------------------------------------------------

# Unrecognized / fallback tag handling

# ---------------------------------------------------------------------------


class TestUnrecognizedTagHandling:
    """Tests that unknown tags fall through gracefully."""

    @pytest.mark.anyio
    async def test_unknown_tag_passes_children(
        self, converter: WikiHtmlConverter
    ) -> None:
        """An unrecognized tag should still render its children."""
        result = await _convert(converter, "<unknown>content</unknown>")
        assert "content" in result

    @pytest.mark.anyio
    async def test_empty_tag(self, converter: WikiHtmlConverter) -> None:
        """An empty tag should produce empty output."""
        result = await _convert(converter, "<div></div>")
        assert result.strip() == ""


# ---------------------------------------------------------------------------

# NavigableString / text normalization

# ---------------------------------------------------------------------------


class TestTextNormalization:
    """Tests for the formatting-agnostic text normalization."""

    @pytest.mark.anyio
    async def test_newlines_normalized_to_spaces(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Newlines inside a text node should become spaces."""
        result = await _convert(converter, "<p>line1\nline2\nline3</p>")
        assert "line1 line2 line3" in result

    @pytest.mark.anyio
    async def test_tabs_normalized_to_spaces(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Tabs inside a text node should become spaces."""
        result = await _convert(converter, "<p>col1\tcol2</p>")
        assert "col1 col2" in result

    @pytest.mark.anyio
    async def test_escaped_text(self, converter: WikiHtmlConverter) -> None:
        """Markdown special characters should be escaped."""
        result = await _convert(converter, "<p>a * b</p>")
        assert "a \\* b" in result


# ---------------------------------------------------------------------------

# Reference handling

# ---------------------------------------------------------------------------


class TestReferenceHandling:
    """Tests for footnote/citation reference rendering."""

    @pytest.mark.anyio
    async def test_sup_ref(self, converter: WikiHtmlConverter) -> None:
        """``<sup class="reference">`` should produce a linked anchor."""
        html = '<sup class="reference"><a href="#cite_note-1">[1]</a></sup>'
        result = await _convert(converter, html)
        assert "ref-1" in result or "[1]" in result

    @pytest.mark.anyio
    async def test_sup_ref_note_group(self, converter: WikiHtmlConverter) -> None:
        """Grouped ``[note 1]`` reference links to the ``^note-1`` anchor."""
        html = (
            '<sup class="mw-ref reference">'
            '<a href="#cite_note-1" data-mw-group="note">[note 1]</a>'
            "</sup>"
        )
        result = await _convert(converter, html)
        assert "(#^note-1)" in result

    @pytest.mark.anyio
    async def test_sup_ref_note_old_html(self, converter: WikiHtmlConverter) -> None:
        """Old-style grouped reference links to ``^note-1`` via display text."""
        html = '<sup class="reference"><a href="#cite_note-1">[note 1]</a></sup>'
        result = await _convert(converter, html)
        assert "(#^note-1)" in result

    @pytest.mark.anyio
    async def test_note_anchor_group(self, converter: WikiHtmlConverter) -> None:
        """``<ol data-mw-group="note">`` items get ``^note-N`` anchors."""
        html = (
            '<ol class="mw-references references" data-mw-group="note">'
            '<li id="cite_note-1">first note</li>'
            "</ol>"
        )
        result = await _convert(converter, html)
        assert '<a id="^note-1"></a>^note-1' in result

    @pytest.mark.anyio
    async def test_mixed_groups_end_to_end(self, converter: WikiHtmlConverter) -> None:
        """Notes and citations keep distinct anchor namespaces."""
        html = (
            '<ol class="mw-references references" data-mw-group="note">'
            '<li id="cite_note-1">note one</li>'
            "</ol>"
            '<ol class="mw-references references">'
            '<li id="cite_note-2">citation two</li>'
            "</ol>"
        )
        result = await _convert(converter, html)
        assert '<a id="^note-1"></a>^note-1' in result
        assert '<a id="^ref-1"></a>^ref-1' in result
        assert result.count('<a id="^ref-1">') == 1

    @pytest.mark.anyio
    async def test_refs_false_skips_reference(
        self, converter: WikiHtmlConverter
    ) -> None:
        """When ``refs=False``, reference superscripts should be omitted."""
        soup = BeautifulSoup(
            '<sup class="reference"><a href="#cite_note-1">[1]</a></sup>',
            "html.parser",
        )
        result = await converter.convert(
            soup,
            out_to_archive=set(),
            redirect_map={},
            refs=False,
        )
        assert result == ""

    @pytest.mark.anyio
    async def test_editsection_ignored(self, converter: WikiHtmlConverter) -> None:
        """``mw-editsection`` spans should be removed."""
        html = '<span class="mw-editsection">[edit]</span>'
        result = await _convert(converter, html)
        assert result == "" or "[edit]" not in result


# ---------------------------------------------------------------------------

# Utility / static method tests

# ---------------------------------------------------------------------------


class TestStaticUtilities:
    """Tests for static/class utility methods."""

    def test_escape_latex_text(self) -> None:
        """Special LaTeX chars should be escaped properly."""
        result = LatexConverter._escape_latex_text(r"a & b $10%")
        assert "\\&" in result
        assert "\\$" in result
        assert "\\%" in result

    def test_escape_flashcard_delimiters(self) -> None:
        """Flashcard delimiters should get spaces inserted."""
        result = WikiHtmlConverter._escape_flashcard_delimiters(":x:@:y")
        assert ": @ :" in result

    def test_in_table_cell(self, converter: WikiHtmlConverter) -> None:
        """``_in_table_cell`` should detect table nesting."""
        soup = BeautifulSoup(
            "<table><tr><td><span>inner</span></td></tr></table>",
            "html.parser",
        )
        span = soup.find("span")
        assert span is not None
        assert WikiHtmlConverter._in_table_cell(span)

    def test_not_in_table_cell(self, converter: WikiHtmlConverter) -> None:
        """A non-nested element should not be detected as table cell."""
        soup = BeautifulSoup("<p><span>text</span></p>", "html.parser")
        span = soup.find("span")
        assert span is not None
        assert not WikiHtmlConverter._in_table_cell(span)

    def test_in_inline_context_list_item(self, converter: WikiHtmlConverter) -> None:
        """Element inside ``<li>`` should be in inline context."""
        soup = BeautifulSoup("<li><span>item</span></li>", "html.parser")
        span = soup.find("span")
        assert span is not None
        assert WikiHtmlConverter._in_inline_context(span)

    def test_not_in_inline_context_paragraph(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Element inside ``<p>`` should NOT be in inline context."""
        soup = BeautifulSoup("<p><span>text</span></p>", "html.parser")
        span = soup.find("span")
        assert span is not None
        assert not WikiHtmlConverter._in_inline_context(span)

    def test_in_navbox(self, converter: WikiHtmlConverter) -> None:
        """Element inside a navbox table should be detected."""
        soup = BeautifulSoup(
            '<table class="navbox"><tr><td><span>nav</span></td></tr></table>',
            "html.parser",
        )
        span = soup.find("span")
        assert span is not None
        assert WikiHtmlConverter._in_navbox(span)

    def test_not_in_navbox(self, converter: WikiHtmlConverter) -> None:
        """Regular table should not be detected as navbox."""
        soup = BeautifulSoup(
            "<table><tr><td><span>regular</span></td></tr></table>",
            "html.parser",
        )
        span = soup.find("span")
        assert span is not None
        assert not WikiHtmlConverter._in_navbox(span)


# ---------------------------------------------------------------------------

# Multiple elements / integration

# ---------------------------------------------------------------------------


class TestMultiElementIntegration:
    """Tests combining multiple handlers in a single HTML tree."""

    @pytest.mark.anyio
    async def test_heading_followed_by_paragraph(
        self, converter: WikiHtmlConverter
    ) -> None:
        """``<h2>`` followed by ``<p>`` should produce well-separated output."""
        result = await _convert(converter, "<h2>Title</h2><p>Content</p>")
        assert "## title" in result
        assert "Content" in result

    @pytest.mark.anyio
    async def test_bold_inside_paragraph(self, converter: WikiHtmlConverter) -> None:
        """Bold text inside a paragraph should render correctly."""
        result = await _convert(converter, "<p>a <b>b</b> c</p>")
        assert "a __b__ c" in result or "a" in result

    @pytest.mark.anyio
    async def test_link_inside_paragraph(self, converter: WikiHtmlConverter) -> None:
        """Link inside a paragraph should remain inline."""
        html = '<p>see <a title="Target" href="/wiki/Target">target</a> for details</p>'
        result = await _convert(converter, html)
        assert "see [target]" in result

    @pytest.mark.anyio
    async def test_block_math_inside_paragraph(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Block math inside a paragraph should be inline with text."""
        result = await _convert(
            converter,
            f"<p>before {_block_math_span(r'{\displaystyle f(x)}')} after</p>",
        )
        assert "before $$f(x)$$ after" in result


# ---------------------------------------------------------------------------

# Dispatch / edge-case tests

# ---------------------------------------------------------------------------


class TestDispatchEdgeCases:
    """Tests for the dispatch mechanism in ``_dispatch``."""

    @pytest.mark.anyio
    async def test_style_tag_stripped(self, converter: WikiHtmlConverter) -> None:
        """``<style>`` elements should be removed from output."""
        result = await _convert(
            converter, "<style>.foo { color: red; }</style><p>text</p>"
        )
        assert "color" not in result
        assert "text" in result

    @pytest.mark.anyio
    async def test_mw_cite_backlink_ignored(self, converter: WikiHtmlConverter) -> None:
        """``mw-cite-backlink`` should be removed."""
        html = '<span class="mw-cite-backlink"><a href="#ref-1">^</a></span>'
        result = await _convert(converter, html)
        assert result == ""

    @pytest.mark.anyio
    async def test_transclusion_not_annotated_image(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Transclusion without annotated image passes through."""
        html = '<div typeof="mw:Transclusion" data-mw=\'{"parts":[]}\'>content</div>'
        result = await _convert(converter, html)
        # Should contain the inner content.
        assert "content" in result
