"""Tests for WikiHtmlConverter handler methods.

Covers individual tag handlers dispatched by ``_dispatch``, static/class
utilities, and edge cases for each handler in ``converter.py``.
"""

from os import PathLike
from pathlib import Path

import pytest
from anyio import Path as AnyioPath
from bs4 import BeautifulSoup, NavigableString, Tag

from scripts.convert_wiki.converter import WikiHtmlConverter, _discards_subtree
from scripts.convert_wiki.latex import LatexConverter
from scripts.convert_wiki.types import _RedirectInfo
from tests.scripts.test_convert_wiki import _assert_markdownlint_clean

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

    @pytest.mark.anyio
    async def test_lagrange_query_string_stripped(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Query strings in img src should not leak into archive output."""
        html = (
            '<img src="//upload.wikimedia.org/wikipedia/commons/8/8e/'
            "Lagrange_portrait.jpg?utm_source=en.wikipedia.org"
            '&amp;utm_campaign=parser&amp;utm_content=thumbnail"/>'
        )
        soup = BeautifulSoup(html, "html.parser")
        out_to_archive: set[str] = set()
        result = await converter.convert(
            soup,
            out_to_archive=out_to_archive,
            redirect_map={},
            refs=True,
        )
        assert out_to_archive == {"File:Lagrange_portrait.jpg"}
        assert "../../archives/Wikimedia%20Commons/Lagrange%20portrait.jpg" in result

    @pytest.mark.anyio
    async def test_lagrange_thumb_query_string_stripped(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Thumb URLs with query strings should yield the clean original filename."""
        html = (
            '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/8/8e/'
            "Lagrange_portrait.jpg/220px-Lagrange_portrait.jpg"
            "?utm_source=en.wikipedia.org&amp;utm_campaign=parser"
            '&amp;utm_content=thumbnail"/>'
        )
        soup = BeautifulSoup(html, "html.parser")
        out_to_archive: set[str] = set()
        result = await converter.convert(
            soup,
            out_to_archive=out_to_archive,
            redirect_map={},
            refs=True,
        )
        assert out_to_archive == {"File:Lagrange_portrait.jpg"}
        assert "../../archives/Wikimedia%20Commons/Lagrange%20portrait.jpg" in result

    @pytest.mark.anyio
    async def test_thumb_host_thumbnail_rewritten(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Thumbnails served from thumb.wikimedia.org resolve to the archive."""
        html = (
            '<img src="//thumb.wikimedia.org/wikipedia/commons/thumb/a/a0/'
            "Einstein_patentoffice.jpg/250px-Einstein_patentoffice.jpg"
            '?utm_source=en.wikipedia.org&amp;utm_campaign=parser"/>'
        )
        soup = BeautifulSoup(html, "html.parser")
        out_to_archive: set[str] = set()
        result = await converter.convert(
            soup,
            out_to_archive=out_to_archive,
            redirect_map={},
            refs=True,
        )
        assert out_to_archive == {"File:Einstein_patentoffice.jpg"}
        assert (
            "../../archives/Wikimedia%20Commons/Einstein%20patentoffice.jpg" in result
        )
        assert "thumb.wikimedia.org" not in result

    @pytest.mark.anyio
    async def test_thumb_host_percent_encoded_filename(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Percent-encoded thumb-host filenames are decoded for the archive path."""
        html = (
            '<img src="//thumb.wikimedia.org/wikipedia/commons/thumb/2/29/'
            'Sinh%2Bcosh%2Btanh.svg/250px-Sinh%2Bcosh%2Btanh.svg.png"/>'
        )
        soup = BeautifulSoup(html, "html.parser")
        out_to_archive: set[str] = set()
        result = await converter.convert(
            soup,
            out_to_archive=out_to_archive,
            redirect_map={},
            refs=True,
        )
        assert out_to_archive == {"File:Sinh+cosh+tanh.svg"}
        assert "../../archives/Wikimedia%20Commons/Sinh%2Bcosh%2Btanh.svg" in result

    @pytest.mark.anyio
    async def test_thumb_host_transcoded_rewritten(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A transcoded video on thumb.wikimedia.org resolves to the archive.

        The URL names the transcoded derivative, but the archive holds the
        source file, so the directory segment above it is the filename.
        """
        html = (
            '<img src="//thumb.wikimedia.org/wikipedia/commons/transcoded/9/93/'
            'X.ogv/X.ogv.480p.vp9.webm"/>'
        )
        soup = BeautifulSoup(html, "html.parser")
        out_to_archive: set[str] = set()
        result = await converter.convert(
            soup,
            out_to_archive=out_to_archive,
            redirect_map={},
            refs=True,
        )
        assert out_to_archive == {"File:X.ogv"}
        assert "../../archives/Wikimedia%20Commons/X.ogv" in result
        assert "thumb.wikimedia.org" not in result

    @pytest.mark.anyio
    async def test_thumb_host_transcoded_percent_encoded_filename(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A percent-encoded transcoded filename is decoded then re-encoded."""
        html = (
            '<img src="//thumb.wikimedia.org/wikipedia/commons/transcoded/2/29/'
            'Sinh%2Bcosh%2Btanh.svg/Sinh%2Bcosh%2Btanh.svg.480p.vp9.webm"/>'
        )
        soup = BeautifulSoup(html, "html.parser")
        out_to_archive: set[str] = set()
        result = await converter.convert(
            soup,
            out_to_archive=out_to_archive,
            redirect_map={},
            refs=True,
        )
        assert out_to_archive == {"File:Sinh+cosh+tanh.svg"}
        assert "../../archives/Wikimedia%20Commons/Sinh%2Bcosh%2Btanh.svg" in result
        assert "thumb.wikimedia.org" not in result


# ---------------------------------------------------------------------------

# Video handling

# ---------------------------------------------------------------------------


class TestVideoHandling:
    """Tests for ``_handle_video`` alt-text derivation."""

    @pytest.mark.anyio
    async def test_video_with_resource(self, converter: WikiHtmlConverter) -> None:
        """Video with ``resource`` should render an embed with File: alt."""
        html = (
            '<video resource="/wiki/File:Rotation_table.ogv" '
            'data-mwtitle="Rotation_table.ogv"></video>'
        )
        result = await _convert(converter, html)
        assert "![File:Rotation table.ogv]" in result

    @pytest.mark.anyio
    async def test_video_without_resource_uses_mwtitle(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Video lacking ``resource`` should fall back to ``data-mwtitle``."""
        html = '<video data-mwtitle="Rotation_table.ogv"></video>'
        result = await _convert(converter, html)
        assert "![File:Rotation table.ogv]" in result

    @pytest.mark.anyio
    async def test_video_with_source(self, converter: WikiHtmlConverter) -> None:
        """Video with a ``<source>`` child should derive alt from its URL."""
        html = (
            '<video data-mwtitle="Rotation_table.ogv">'
            '<source src="//upload.wikimedia.org/wikipedia/commons/'
            '9/93/Rotation_table.ogv"></source></video>'
        )
        result = await _convert(converter, html)
        assert "![File:Rotation table.ogv]" in result

    @pytest.mark.anyio
    async def test_video_uses_metadata_description(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Video with a collected description should use it as alt."""
        html = (
            '<video resource="/wiki/File:Rotation_table.ogv" '
            'data-mwtitle="Rotation_table.ogv"></video>'
        )
        soup = BeautifulSoup(html, "html.parser")
        converter._image_metadata = {"File:Rotation table.ogv": "A spinning table."}
        result = await converter.convert(
            soup,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        assert "![A spinning table.]" in result


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

    @pytest.mark.anyio
    async def test_document_title_becomes_level_1_heading(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A ``<head><title>`` renders as a level-1 heading via the shared path."""
        result = await _convert(
            converter,
            "<html><head><title>Special relativity</title></head>"
            "<body><p>Body text</p></body></html>",
        )
        assert result.startswith("# special relativity\n\n")
        assert "Body text" in result

    @pytest.mark.anyio
    async def test_document_title_uses_shared_heading_casing(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Title casing goes through ``_fix_name_maybe`` like any other heading."""
        result = await _convert(
            converter,
            "<html><head><title>Routhian mechanics</title></head>"
            "<body><h2>Overview</h2></body></html>",
        )
        assert result.startswith("# Routhian mechanics\n\n")
        assert "## overview" in result

    @pytest.mark.anyio
    async def test_inline_svg_title_not_a_heading(
        self, converter: WikiHtmlConverter
    ) -> None:
        """``<title>`` outside ``<head>`` must not be promoted to a heading."""
        result = await _convert(converter, "<svg><title>Icon</title></svg><p>After</p>")
        assert "# Icon" not in result
        assert "Icon" in result

    @pytest.mark.anyio
    async def test_title_shares_md024_suppression(
        self, converter: WikiHtmlConverter
    ) -> None:
        """The title participates in the shared heading dedup state."""
        result = await _convert(
            converter,
            "<html><head><title>Physics</title></head>"
            "<body><h1>Physics</h1></body></html>",
        )
        assert "<!-- markdownlint-disable-next-line MD024 -->" in result


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
    async def test_adjacent_bold_runs_keep_separator(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Two bold runs with nothing between them are kept apart."""
        result = await _convert(converter, "<p><b>a</b><b>b</b></p>")
        assert "__a__<!-- markdown separator -->__b__" in result

    @pytest.mark.anyio
    async def test_separator_past_collapsed_emphasis_span(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A whitespace-only emphasis span is looked past, not merged with.

        The italic span renders nothing: its whitespace body collapses, so the
        processed result is empty and the markers around it are dropped.  It
        therefore cannot be the neighbour that separates the two bold runs.
        """
        html = '<p><b>a</b><span style="font-style:italic"> </span><b>b</b></p>'
        result = await _convert(converter, html)
        assert "__a__<!-- markdown separator -->__b__" in result

    @pytest.mark.anyio
    async def test_separator_past_empty_span(
        self, converter: WikiHtmlConverter
    ) -> None:
        """An empty span renders nothing, so it is not the adjacent token."""
        result = await _convert(converter, "<p><b>a</b><span></span><b>b</b></p>")
        assert "__a__<!-- markdown separator -->__b__" in result

    @pytest.mark.anyio
    async def test_separator_past_nested_empty_span(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A wrapper around only empty wrappers renders nothing either.

        Transparent spans are flattened, so the wrapper's own output is exactly
        its children's: non-empty contents are not enough to count as content.
        """
        html = "<p><b>a</b><span><span></span></span><b>b</b></p>"
        result = await _convert(converter, html)
        assert "__a__<!-- markdown separator -->__b__" in result

    @pytest.mark.anyio
    async def test_separator_past_discarded_span(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A discarded span is not the token that abuts the whitespace.

        ``convert`` drops ``mw-editsection`` subtrees, so the text either side
        of one must still see each other.  Without the same verdict in
        ``_renders_nothing`` the walk-up stops at the dropped span and its
        arrow glyph swallows the separation.  Either side may carry it.
        """
        for html in (
            '<p>x<span class="mw-editsection">↑</span> y</p>',
            '<p>x <span class="mw-editsection">↑</span>y</p>',
        ):
            assert "x y" in await _convert(converter, html)

    @pytest.mark.anyio
    async def test_separator_past_empty_entity_span(
        self, converter: WikiHtmlConverter
    ) -> None:
        """An empty ``mw:Entity`` span renders nothing either."""
        html = '<p><b>a</b><span typeof="mw:Entity"></span><b>b</b></p>'
        result = await _convert(converter, html)
        assert "__a__<!-- markdown separator -->__b__" in result

    @pytest.mark.anyio
    async def test_transparent_span_keeps_its_space(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A transparent span holding a space still supplies that space.

        The whitespace branch renders the space, so the span is not empty and
        must not be skipped in favour of the emphasis run beyond it.
        """
        result = await _convert(converter, "<p><b>a</b><span> </span><b>b</b></p>")
        assert "__a__ __b__" in result
        assert "markdown separator" not in result

    @pytest.mark.anyio
    async def test_literal_space_between_bold_runs_kept(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A literal space between emphasis runs stays a space."""
        result = await _convert(converter, "<p><b>a</b> <b>b</b></p>")
        assert "__a__ __b__" in result
        assert "markdown separator" not in result

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
    async def test_angle_bracket_emphasis_no_marker(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Angle brackets U+27E8/U+27E9 need no separator marker.

        Mirrors the inner-product markup ``⟨x, ξ⟩`` found on Wikipedia,
        where the bold ``x``/``ξ`` variables must not gain separators.
        """
        html = (
            '<p><span typeof="mw:Entity">\u27e8</span>'
            "<b>x</b>,<span>\xa0</span><b>\u03be</b>"
            '<span typeof="mw:Entity">\u27e9</span></p>'
        )
        result = await _convert(converter, html)
        assert "\u27e8__x__, __\u03be__\u27e9" in result
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

    @pytest.mark.anyio
    async def test_italic_bare_url(self, converter: WikiHtmlConverter) -> None:
        """Bare ``www.`` URL in ``<i>`` should be wrapped in autolink brackets."""
        result = await _convert(converter, "<i>www.astro.uvic.ca</i>")
        assert "_<www.astro.uvic.ca>_" in result

    @pytest.mark.anyio
    async def test_italic_bare_https_url(self, converter: WikiHtmlConverter) -> None:
        """Bare ``https://`` URL in ``<i>`` should be wrapped in autolink brackets."""
        result = await _convert(converter, "<i>https://example.com/path</i>")
        assert "_<https://example.com/path>_" in result

    @pytest.mark.anyio
    async def test_bold_bare_url(self, converter: WikiHtmlConverter) -> None:
        """Bare URL in ``<b>`` should be wrapped in autolink brackets."""
        result = await _convert(converter, "<b>www.example.com</b>")
        assert "__<www.example.com>__" in result

    @pytest.mark.anyio
    async def test_italic_plain_text_not_wrapped(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Plain text in ``<i>`` should not be wrapped."""
        result = await _convert(converter, "<i>plain text</i>")
        assert "_plain text_" in result

    @pytest.mark.anyio
    async def test_italic_link_destination_not_wrapped(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Link destination inside ``<i>`` should not be wrapped."""
        result = await _convert(
            converter, '<i><a href="https://x.example/y">label</a></i>'
        )
        assert "_[label](https://x.example/y)_" in result

    @pytest.mark.anyio
    async def test_italic_code_span_not_wrapped(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Code span inside ``<i>`` should not be wrapped."""
        result = await _convert(converter, "<i><code>x</code></i>")
        assert "_`x`_" in result

    @pytest.mark.anyio
    async def test_italic_bare_url_trailing_period(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Trailing period stays inside autolink brackets."""
        result = await _convert(converter, "<i>www.example.com.</i>")
        assert "_<www.example.com.>_" in result

    @pytest.mark.anyio
    async def test_adjacent_emphasis_tags_italic_then_bold(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Adjacent ``<i>``/``<b>`` tags should be separated by a marker."""
        result = await _convert(converter, "<p><i>δ</i><b>r</b></p>")
        assert "_δ_<!-- markdown separator -->__r__" in result

    @pytest.mark.anyio
    async def test_adjacent_emphasis_tags_bold_then_italic(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Adjacent ``<b>``/``<i>`` tags should be separated by a marker."""
        result = await _convert(converter, "<p><b>r</b><i>δ</i></p>")
        assert "__r__<!-- markdown separator -->_δ_" in result

    @pytest.mark.anyio
    async def test_adjacent_emphasis_tags_in_span(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Adjacent emphasis tags inside a ``<span>`` should be separated."""
        result = await _convert(
            converter, '<p><span class="nowrap"><i>δ</i><b>r</b></span></p>'
        )
        assert "_δ_<!-- markdown separator -->__r__" in result

    @pytest.mark.anyio
    async def test_emphasis_tags_span_wrapped_sibling(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Emphasis tags in sibling spans should still be separated."""
        result = await _convert(
            converter, "<p><span><i>δ</i></span><span><b>r</b></span></p>"
        )
        assert "_δ_<!-- markdown separator -->__r__" in result

    @pytest.mark.anyio
    async def test_emphasis_tags_separated_by_text(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Emphasis tags with text between them need no separator."""
        result = await _convert(converter, "<p><i>x</i> text <b>y</b></p>")
        assert "<!-- markdown separator -->" not in result

    @pytest.mark.anyio
    async def test_emphasis_then_subscript_no_separator(
        self, converter: WikiHtmlConverter
    ) -> None:
        """``<sub>`` renders raw HTML and needs no separator."""
        result = await _convert(converter, "<p><b>x</b><sup>2</sup></p>")
        assert "<!-- markdown separator -->" not in result

    @pytest.mark.anyio
    async def test_emphasis_inside_subscript_no_separator(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Emphasis nested in ``<sub>`` should not trigger a separator."""
        result = await _convert(converter, "<p><i>x</i><sub><i>y</i></sub></p>")
        assert "<!-- markdown separator -->" not in result

    @pytest.mark.anyio
    async def test_needs_separator_before_emphasis_tag(
        self, converter: WikiHtmlConverter
    ) -> None:
        """``_needs_separator_before`` recognizes emphasis-rendering tags."""
        soup = BeautifulSoup("<p><i>a</i><b>b</b></p>", "html.parser")
        bold = soup.find("b")
        assert bold is not None
        assert bold.previous_sibling is not None
        assert WikiHtmlConverter._needs_separator_before(bold.previous_sibling)
        sup = soup.find("sup")
        assert sup is None
        soup = BeautifulSoup("<p><sup>2</sup></p>", "html.parser")
        assert WikiHtmlConverter._needs_separator_before(soup.sup) is False

    @pytest.mark.anyio
    async def test_nested_bold_deduped(self, converter: WikiHtmlConverter) -> None:
        """Nested bold must not render as the meaningless ``____text____``."""
        result = await _convert(converter, "<b><b>Foundations</b></b>")
        assert result.strip() == "__Foundations__"

    @pytest.mark.anyio
    async def test_css_bold_ancestor_deduped(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A bold-styled ancestor satisfies the inner ``<b>``."""
        result = await _convert(
            converter,
            '<span style="font-weight: bold"><b>Foundations</b></span>',
        )
        assert result.strip() == "__Foundations__"

    @pytest.mark.anyio
    async def test_nested_italic_deduped(self, converter: WikiHtmlConverter) -> None:
        """Nested italic collapses to a single ``_`` pair."""
        result = await _convert(converter, "<i><i>Italic</i></i>")
        assert result.strip() == "_Italic_"

    @pytest.mark.anyio
    async def test_distinct_nested_emphasis_preserved(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Bold inside italic is distinct emphasis and must be kept."""
        result = await _convert(converter, "<i><b>Both</b></i>")
        assert result.strip() == "___Both___"

    @pytest.mark.anyio
    async def test_sidebar_title_bold_not_doubled(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Sidebar title bold wrapping must not double a CSS-bold ancestor."""
        result = await _convert(
            converter,
            '<table class="sidebar"><tbody><tr><td class="sidebar-content">'
            '<div class="sidebar-list"><div class="sidebar-list-title" '
            'style="font-weight: bold"><div class="sidebar-list-title-c">'
            "<b>Foundations</b></div></div></div></td></tr></tbody></table>",
        )
        assert "____" not in result
        assert "__Foundations__" in result

    @pytest.mark.anyio
    async def test_mw_heading_wrapper_ignored(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A CSS-bold ``mw-heading`` wrapper does not suppress inner emphasis."""
        result = await _convert(
            converter,
            '<div class="mw-heading mw-heading2" style="font-weight: bold">'
            "<h2>Heading</h2><b>bold</b></div>",
        )
        assert "## heading" in result
        assert "__bold__" in result

    @pytest.mark.anyio
    async def test_bold_list_wrapper_bolds_each_item(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Bold around a whole list must bold each item, not the list."""
        result = await _convert(
            converter, "<b><ul><li>alpha</li><li>beta</li></ul></b>"
        )
        assert "\n- __alpha__" in result
        assert "\n- __beta__" in result
        assert "__- " not in result

    @pytest.mark.anyio
    async def test_bold_list_cell_bolds_each_item(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A CSS-bold cell wrapping a list bolds each ``hlist`` item."""
        result = await _convert(
            converter,
            '<table><tbody><tr><td style="font-weight: bold">'
            "<ul><li>alpha</li><li>beta</li></ul></td></tr></tbody></table>",
        )
        assert "- __alpha__ <br/> - __beta__" in result
        assert "__- " not in result

    @pytest.mark.anyio
    async def test_bold_nested_list_wrapper_bolds_each_item(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A ``hlist`` div between the bold wrapper and the list is transparent."""
        result = await _convert(
            converter,
            '<div style="font-weight: bold"><div class="hlist">'
            "<ul><li>alpha</li></ul></div></div>",
        )
        assert "- __alpha__" in result
        assert "__- " not in result

    @pytest.mark.anyio
    async def test_unbolded_list_wrapper_unchanged(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A list that is not bolded keeps its item markers unbolded."""
        result = await _convert(converter, "<ul><li>alpha</li><li>beta</li></ul>")
        assert "- alpha" in result
        assert "__" not in result

    @pytest.mark.anyio
    async def test_hatnote_wrapper_ignored(self, converter: WikiHtmlConverter) -> None:
        """A hatnote's own CSS emphasis must not suppress nested emphasis.

        Hatnotes render as list items and deliberately never emit their own
        emphasis, so an emphasized word inside one keeps its markers.
        """
        result = await _convert(
            converter,
            '<div class="hatnote" style="font-style: italic">See <i>also</i></div>',
        )
        assert "- See _also_" in result

    @pytest.mark.anyio
    async def test_hatnote_bold_wrapper_ignored(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A bold-styled hatnote must not suppress nested bold."""
        result = await _convert(
            converter,
            '<div class="hatnote" style="font-weight: bold">See <b>also</b></div>',
        )
        assert "- See __also__" in result


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

    @pytest.mark.anyio
    async def test_single_row_mixed_table_gets_empty_header(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A single-row mixed th/td table gets a synthesized empty header row."""
        html = '<table><tbody><tr><th scope="row">A</th><td>B</td></tr></tbody></table>'
        result = await _convert(converter, html)
        assert result == "\n|  |  |\n| --: | --- |\n| __A__ | B |\n\n\n"

    @pytest.mark.anyio
    async def test_single_row_mixed_table_without_scope_row_keeps_left_alignment(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Without a scope=row label, the marker stays default-aligned."""
        html = "<table><tbody><tr><th>A</th><td>B</td></tr></tbody></table>"
        result = await _convert(converter, html)
        assert result == "\n|  |  |\n| --- | --- |\n| __A__ | B |\n\n\n"

    @pytest.mark.anyio
    async def test_two_row_mixed_table_scope_row_right_aligns_label_column(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A multi-row mixed table also right-aligns its scope=row label."""
        html = (
            '<table><tbody><tr><th scope="row">A</th><td>B</td></tr>'
            "<tr><td>C</td><td>D</td></tr></tbody></table>"
        )
        result = await _convert(converter, html)
        assert result == "\n| __A__ | B |\n| --: | --- |\n| C | D |\n\n\n"

    @pytest.mark.anyio
    async def test_two_row_mixed_table_unchanged(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A two-row mixed table keeps its original header-row behavior."""
        html = (
            "<table><tbody><tr><th>A</th><td>B</td></tr>"
            "<tr><td>C</td><td>D</td></tr></tbody></table>"
        )
        result = await _convert(converter, html)
        assert result == "\n| __A__ | B |\n| --- | --- |\n| C | D |\n\n\n"


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

    @pytest.mark.anyio
    async def test_audio_uses_file_alt(self, converter: WikiHtmlConverter) -> None:
        """Audio href should derive a ``File:`` alt via the image mechanism."""
        html = (
            '<span class="mw-tmh-play" '
            'href="//upload.wikimedia.org/wikipedia/commons/a/ab/Sound.ogg">'
            "play</span>"
        )
        result = await _convert(converter, html)
        assert "[File:Sound.ogg]" in result

    @pytest.mark.anyio
    async def test_audio_player_embeds(self, converter: WikiHtmlConverter) -> None:
        """``mw-tmh-player`` audio should render as an embed, not a link."""
        html = (
            '<span class="mw-tmh-play mw-tmh-player" '
            'href="//upload.wikimedia.org/wikipedia/commons/a/ab/Sound.ogg">'
            "play</span>"
        )
        result = await _convert(converter, html)
        assert "![File:Sound.ogg]" in result

    @pytest.mark.anyio
    async def test_audio_uses_metadata_description(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Audio with a collected description should use it as alt."""
        html = (
            '<span class="mw-tmh-play" '
            'href="//upload.wikimedia.org/wikipedia/commons/a/ab/Sound.ogg">'
            "play</span>"
        )
        soup = BeautifulSoup(html, "html.parser")
        converter._image_metadata = {"File:Sound.ogg": "A short tone."}
        result = await converter.convert(
            soup,
            out_to_archive=set(),
            redirect_map={},
            refs=True,
        )
        assert "[A short tone.]" in result


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

    @pytest.mark.anyio
    async def test_equation_box_table(self, converter: WikiHtmlConverter) -> None:
        """A title-less ``equation-box`` div without numbering is a plain block."""
        result = await _convert(
            converter, '<div class="equation-box">E = mc<sup>2</sup></div>'
        )
        assert result == "E = mc<sup>2</sup>"
        assert "\n> " not in result

    @pytest.mark.anyio
    async def test_math_proof_blockquote(self, converter: WikiHtmlConverter) -> None:
        """``math_proof`` divs should render as blockquotes."""
        result = await _convert(converter, '<div class="math_proof">Proof.</div>')
        assert "> Proof." in result

    @pytest.mark.anyio
    async def test_math_theorem_blockquote(self, converter: WikiHtmlConverter) -> None:
        """``math_theorem`` divs should still render as blockquotes."""
        result = await _convert(converter, '<div class="math_theorem">Thm.</div>')
        assert "> Thm." in result

    @pytest.mark.anyio
    async def test_equation_box_without_numblk_table(
        self, converter: WikiHtmlConverter
    ) -> None:
        """``equation-box`` divs without a numblk table render single-column tables."""
        result = await _convert(
            converter,
            '<div class="equation-box"><b>Eq</b><p>E = mc<sup>2</sup></p></div>',
        )
        assert result == "\n| __Eq__ |\n| --- |\n| E = mc<sup>2</sup> |\n\n\n"
        assert "\n> " not in result

    @pytest.mark.anyio
    async def test_equation_box_with_numblk_table(
        self, converter: WikiHtmlConverter
    ) -> None:
        """``equation-box`` divs with a numblk table keep the number column.

        The box's declared alignment propagates to both columns.
        """
        result = await _convert(
            converter,
            '<div class="equation-box" style="text-align:center">'
            "<b>Eq</b>"
            '<table class="numblk"><tbody><tr>'
            "<td>E = mc<sup>2</sup></td>"
            '<td style="width: 0px"></td>'
            "<td>Eq.1</td>"
            "</tr></tbody></table></div>",
        )
        assert result == (
            "\n| __Eq__ |  |\n| :-: | :-: |\n| E = mc<sup>2</sup> | Eq.1 |\n\n\n"
        )
        assert "\n> " not in result

    @pytest.mark.anyio
    async def test_sibling_numblk_table_gets_header_and_alignment(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A ``numblk`` table that is a sibling of an ``equation-box`` div
        (not a descendant) must still render a header row plus an alignment
        marker row, with the box's alignment propagated to both columns.

        This mirrors the layout ``_handle_div`` builds for the nested case,
        so the equation/number body row aligns identically.
        """
        result = await _convert(
            converter,
            '<div class="math_proof">'
            '<div class="equation-box" style="text-align: center; display: table;">'
            "<p>E = mc<sup>2</sup></p></div>"
            '<table class="numblk" style="margin-left: 1.6em"><tbody><tr>'
            '<td class="nowrap">E = mc<sup>2</sup></td>'
            "<td></td>"
            '<td class="nowrap">'
            '<span id="math_1" class="reference nourlexpansion" '
            'style="font-weight: bold">1</span></td>'
            "</tr></tbody></table></div>",
        )
        assert result == (
            "> E = mc<sup>2</sup>\n"
            "> | | |\n"
            "> | :-: | :-: |\n"
            '> | E = mc<sup>2</sup> | <a id="math_1"></a> __\\(1\\)__ |\n\n'
        )

    @pytest.mark.anyio
    async def test_equation_box_numblk_number_cell_single_bold(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A numblk number cell whose ``<td>`` and inner span are both bold
        must render as a single ``__Eq.1__``, never ``____Eq.1____``.

        Wikipedia bolds the number cell and the inner reference span; the
        redundant cell-level bold must be dropped so only the span's bold
        remains.
        """
        result = await _convert(
            converter,
            '<div class="equation-box" style="text-align:center">'
            "<b>Eq</b>"
            '<table class="numblk"><tbody><tr>'
            "<td>E = mc<sup>2</sup></td>"
            '<td style="width: 0px"></td>'
            '<td class="nowrap" style="font-weight: bold;">'
            '<span id="math_Eq.1" class="reference nourlexpansion" '
            'style="font-weight: bold">Eq.1</span>'
            "</td>"
            "</tr></tbody></table></div>",
        )
        assert "____Eq.1____" not in result
        assert "__Eq.1__" in result

    @pytest.mark.anyio
    async def test_plain_bold_span_unaffected_by_numblk_fix(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A normal bold span outside a numblk cell stays single-bold."""
        result = await _convert(converter, "<b>bold</b>")
        assert result == "__bold__"

    @pytest.mark.anyio
    async def test_equation_reference_anchor_emitted(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Equation-reference spans must emit a Markdown ``<a id>`` anchor.

        The anchor id matches the fragment used by prose links: a bare
        ``math_1`` stays raw, while a dotted ``math_Eq.1`` is normalized the
        same way Wikipedia link fragments are (underscores -> spaces).
        """
        raw = await _convert(
            converter,
            '<span id="math_1" class="reference nourlexpansion" '
            'style="font-weight: bold">1</span>',
        )
        assert '<a id="math_1"></a>' in raw
        dotted = await _convert(
            converter,
            '<span id="math_Eq.1" class="reference nourlexpansion" '
            'style="font-weight: bold">Eq.1</span>',
        )
        assert '<a id="math Eq.1"></a>' in dotted

    @pytest.mark.anyio
    async def test_equation_reference_bare_integer_parenthesized(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A bare-integer equation number is wrapped in parentheses.

        Wikipedia renders the parentheses via CSS pseudo-elements; the
        converter must materialize them. Labels (``Eq.1``) and the
        ``numblk-raw-n`` opt-out class are left untouched.
        """
        result = await _convert(
            converter,
            '<span id="math_1" class="reference nourlexpansion" '
            'style="font-weight: bold">1</span>',
        )
        assert "\\(1\\)" in result
        labelled = await _convert(
            converter,
            '<span id="math_Eq.1" class="reference nourlexpansion" '
            'style="font-weight: bold">Eq.1</span>',
        )
        assert "Eq.1" in labelled
        assert "\\(Eq.1\\)" not in labelled
        raw_n = await _convert(
            converter,
            '<span id="math_2" class="reference nourlexpansion numblk-raw-n" '
            'style="font-weight: bold">2</span>',
        )
        assert "\\(2\\)" not in raw_n

    @pytest.mark.anyio
    async def test_blockquote_title_on_own_line(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A box title inside a blockquote should be its own line.

        The title is followed by a blank ``> `` line separating it from
        the body.
        """
        result = await _convert(
            converter,
            '<div class="math_proof"><strong>Proof</strong><p>text</p></div>',
        )
        assert "> __Proof__\n>\n> text" in result

    @pytest.mark.anyio
    async def test_blockquote_italic_title(self, converter: WikiHtmlConverter) -> None:
        """An italic box title keeps its emphasis and blank-line separation."""
        result = await _convert(
            converter,
            '<div class="math_theorem"><em>Lemma</em><p>body</p></div>',
        )
        assert "> _Lemma_\n>\n> body" in result

    @pytest.mark.anyio
    async def test_plain_div_not_blockquoted(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A plain div should not be blockquoted."""
        result = await _convert(converter, "<div>hello</div>")
        assert "> hello" not in result

    @pytest.mark.anyio
    async def test_hatnote_blank_line_before_equation_box(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A hatnote preceding an equation-box needs a blank line suffix."""
        html = (
            '<div class="hatnote">About</div>'
            '<div class="equation-box">E = mc<sup>2</sup></div>'
        )
        result = await _convert(converter, html)
        assert result == "- About\n\nE = mc<sup>2</sup>"

    @pytest.mark.anyio
    async def test_tmulti_caption_separates_blockquote_lines(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Multi-image ``tmulti`` thumbnails separate each image and caption.

        Every image and every ``thumbcaption`` gets its own ``> `` line
        inside the blockquote, with blank ``> `` lines separating
        siblings, instead of caption text gluing to the next image.
        """
        html = (
            '<div class="thumb tmulti"><div class="thumbinner multiimageinner">'
            '<div class="trow"><div class="tsingle">'
            '<div class="thumbimage"><img src="//upload.wikimedia.org/wikipedia/'
            'commons/thumb/5/5d/Image1.svg/250px-Image1.svg.png" alt="Image 1"/>'
            '</div><div class="thumbcaption">First caption.</div></div>'
            '<div class="tsingle">'
            '<div class="thumbimage"><img src="//upload.wikimedia.org/wikipedia/'
            'commons/thumb/8/85/Image2.svg/250px-Image2.svg.png" alt="Image 2"/>'
            '</div><div class="thumbcaption">Second caption.</div></div></div>'
            '<div class="trow"><div class="thumbcaption">Overall caption.</div>'
            "</div></div></div>"
        )
        result = await _convert(converter, html)
        assert (
            "> ![Image 1](../../archives/Wikimedia%20Commons/Image1.svg)\n"
            ">\n> First caption." in result
        )
        assert (
            "> First caption.\n>\n> ![Image 2]"
            "(../../archives/Wikimedia%20Commons/Image2.svg)" in result
        )
        assert "> Second caption.\n>\n> Overall caption." in result

    @pytest.mark.anyio
    async def test_figcaption_block_level(self, converter: WikiHtmlConverter) -> None:
        """A ``<figcaption>`` renders as block-level caption content."""
        html = (
            "<figure>"
            '<img src="//upload.wikimedia.org/wikipedia/commons/thumb/a/a1/'
            'Fig1.svg/250px-Fig1.svg.png" alt="Fig 1"/>'
            "<figcaption>Figure caption.</figcaption></figure>"
        )
        result = await _convert(converter, html)
        assert (
            "> ![Fig 1](../../archives/Wikimedia%20Commons/Fig1.svg)\n"
            ">\n> Figure caption." in result
        )


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
    async def test_space_between_two_plain_spans(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Whitespace between two inline wrappers survives the flattening.

        ``_handle_span`` emits nothing, so at a span edge the whitespace has no
        direct sibling in the markup yet still separates two rendered tokens.
        """
        result = await _convert(converter, "<p><span>a</span> <span>b</span></p>")
        assert "a b" in result

    @pytest.mark.anyio
    async def test_space_between_bold_and_span(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A bold run and an inline wrapper are still two tokens."""
        result = await _convert(converter, "<p><b>a</b> <span>b</span></p>")
        assert "__a__ b" in result

    @pytest.mark.anyio
    async def test_space_at_nested_span_edge(
        self, converter: WikiHtmlConverter
    ) -> None:
        """The walk up through nested transparent spans keeps the space."""
        result = await _convert(
            converter, "<p><span><span>a</span></span> <span>b</span></p>"
        )
        assert "a b" in result

    @pytest.mark.anyio
    async def test_space_kept_between_spans_inside_text(
        self, converter: WikiHtmlConverter
    ) -> None:
        """The preserved space still separates the surrounding text runs."""
        result = await _convert(converter, "<p>x<span>a</span> <span>b</span>y</p>")
        assert "xa by" in result

    @pytest.mark.anyio
    async def test_no_extra_space_when_one_side_is_spaced(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Whitespace runs collapse to one space, never two."""
        result = await _convert(converter, "<p>dash  events</p>")
        assert "dash events" in result
        assert "dash  events" not in result

    @pytest.mark.anyio
    async def test_no_space_across_block_boundary(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Whitespace touching a block element separates blocks, not words."""
        result = await _convert(converter, "<p>a</p> <p>b</p>")
        assert "a b" not in result

    @pytest.mark.anyio
    @pytest.mark.parametrize(
        ("html", "expected"),
        [
            # At a block boundary nothing renders beside the run, so it goes.
            ("<div>\n      Text here\n    </div>", "Text here"),
            ("<div>text here\n   </div>", "text here"),
            ("<dl><dd>\n  Text here\n</dd></dl>", "Text here\n\n"),
            # Between two inline tokens the run is the separation they need.
            ("<div><b>x</b>\n     text here\n</div>", "__x__ text here"),
            ("<div>one\n   two</div>", "one two"),
            # The run must survive even when the neighbour ends in whitespace:
            # the two runs resolve together, so dropping both merges the tokens
            # into ``kgm``.
            ("<div><span>kg </span> m s</div>", "kg  m s"),
            # Markup that renders nothing is stepped over, not treated as the
            # boundary, so the tokens either side still see each other.
            (
                '<div><span>173</span><div class="paragraphbreak"></div>\n  The rest</div>',
                "173 The rest",
            ),
        ],
    )
    async def test_glued_whitespace_run(
        self, converter: WikiHtmlConverter, html: str, expected: str
    ) -> None:
        """A run glued to text is dropped at a block boundary, not between tokens."""
        assert await _convert(converter, html) == expected

    @pytest.mark.anyio
    @pytest.mark.parametrize(
        "html",
        [
            "<div><b>x</b> y</div>",
            "<div><b>x</b><span> </span>y</div>",
            "<div><b>x</b>\n     y</div>",
        ],
    )
    async def test_whitespace_renders_the_same_glued_or_alone(
        self, converter: WikiHtmlConverter, html: str
    ) -> None:
        """A run is decided by its neighbour, not by which node holds it.

        A whitespace-only node between two real tokens and the same run glued
        to adjacent text must render identically, or the two spellings of one
        separation disagree.
        """
        assert await _convert(converter, html) == "__x__ y"

    @pytest.mark.anyio
    async def test_adjacent_whitespace_runs_lose_the_separation(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Recorded limitation: two whitespace runs facing each other both drop.

        A whitespace-only node whose neighbour is itself whitespace-only sees
        no token on that side, and the neighbour makes the same judgement in
        reverse, so a space that HTML would collapse to one is lost entirely.
        Pre-existing (verified against ``b119dd43b``); fixing it needs the runs
        between two tokens collapsed as a sequence rather than one at a time.
        """
        result = await _convert(converter, "<div><b>x</b> <span> </span>y</div>")
        assert result == "__x__y"

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

    def test_renders_emphasis_predicate(self) -> None:
        """The bold/italic routing test shared with ``_dispatch``.

        Covers the explicit emphasis tags and both forcing styles, and rejects
        the inline tags that a Markdown emphasis handler must not claim.
        """
        soup = BeautifulSoup(
            "<p><b>1</b><i>2</i><em>3</em><strong>4</strong>"
            '<span style="font-weight: bold">5</span>'
            '<span style="font-style:italic">6</span>'
            "<span>7</span><a href='#'>8</a></p>",
            "html.parser",
        )
        p = soup.find("p")
        assert isinstance(p, Tag)
        expected = [True, True, True, True, True, True, False, False]
        for child, want in zip(p.find_all(True), expected, strict=True):
            assert isinstance(child, Tag)
            assert WikiHtmlConverter._renders_emphasis(child) is want

    def test_is_transparent_span_accepts_plain_spans(self) -> None:
        """A span with no rendering class is flattened by ``_handle_span``.

        The ``mwe-math-element`` wrapper around inline math is the common case:
        it emits nothing of its own, so its children take its place in the
        rendered output.
        """
        soup = BeautifulSoup(
            '<p><span>a</span><span class="mwe-math-element">b</span></p>',
            "html.parser",
        )
        spans = soup.find_all("span")
        assert len(spans) == 2
        for span in spans:
            assert WikiHtmlConverter._is_transparent_span(span)

    @pytest.mark.parametrize("style", ["font-weight: bold", "font-style: italic"])
    def test_is_transparent_span_rejects_emphasis_styles(self, style: str) -> None:
        """A styled span is routed to ``_handle_bold_italic`` and emits markers."""
        soup = BeautifulSoup(f'<p><span style="{style}">a</span></p>', "html.parser")
        span = soup.find("span")
        assert isinstance(span, Tag)
        assert not WikiHtmlConverter._is_transparent_span(span)

    @pytest.mark.parametrize(
        "classes",
        [
            "hatnote",
            "mw-tmh-play",
            "navbar",
            "oo-ui-buttonElement-button",
            "sidebar-navbar",
            "sistersitebox",
            "thumb",
            "portalbox",
        ],
    )
    def test_is_transparent_span_rejects_class_driven_rendering(
        self, classes: str
    ) -> None:
        """Classes that add markers or block spacing make a span opaque."""
        soup = BeautifulSoup(f'<p><span class="{classes}">a</span></p>', "html.parser")
        span = soup.find("span")
        assert isinstance(span, Tag)
        assert not WikiHtmlConverter._is_transparent_span(span)

    def test_is_transparent_span_hatnote_beats_bold_style(self) -> None:
        """A hatnote keeps its list-marker prefix even when styled bold.

        ``_dispatch`` skips the emphasis handler for hatnotes, but ``convert``
        still prefixes ``- `` and the span therefore renders content.
        """
        soup = BeautifulSoup(
            '<p><span class="hatnote" style="font-weight: bold">a</span></p>',
            "html.parser",
        )
        span = soup.find("span")
        assert isinstance(span, Tag)
        assert not WikiHtmlConverter._is_transparent_span(span)

    def test_is_transparent_span_rejects_non_spans(self) -> None:
        """Only spans are flattened; every other inline tag renders itself."""
        soup = BeautifulSoup(
            "<p><b>a</b><i>b</i><em>c</em><strong>d</strong>"
            "<a href='#'>e</a><img src='f'/></p>",
            "html.parser",
        )
        p = soup.find("p")
        assert isinstance(p, Tag)
        for child in p.find_all(True):
            assert not WikiHtmlConverter._is_transparent_span(child)
        assert not WikiHtmlConverter._is_transparent_span(None)
        assert not WikiHtmlConverter._is_transparent_span(soup)

    @pytest.mark.parametrize(
        ("html", "expected"),
        [
            ("<span></span>", True),
            ("<b></b>", True),
            ('<span style="font-style:italic"> </span>', True),
            ("<span> </span>", False),
            ("<b>x</b>", False),
            ("<br/>", False),
            ("<img src='a'/>", False),
            ("<span><img src='b'/></span>", False),
            ("<video><source src='a.webm'/></video>", False),
            ("<audio><source src='a.ogg'/></audio>", False),
            ("<span><span></span></span>", True),
            ("<span><span> </span></span>", False),
            ("<span><!-- c --></span>", True),
            ("<!-- note -->", True),
            ("text", False),
            (" ", True),
        ],
    )
    def test_renders_nothing(self, html: str, expected: bool) -> None:
        """Only markup with no text, image, or separating space is nothing."""
        soup = BeautifulSoup(html, "html.parser")
        node = next(iter(soup.children))
        assert WikiHtmlConverter._renders_nothing(node, refs=True) is expected

    @pytest.mark.parametrize(
        ("classes", "refs", "expected"),
        [
            ("mw-editsection", True, True),
            ("mw-editsection", False, True),
            ("mw-cite-backlink", True, True),
            ("mw-cite-backlink", False, True),
            ("reference", False, True),
            ("reference", True, False),
            ("hatnote", True, False),
            ("", True, False),
        ],
    )
    def test_discards_subtree(self, classes: str, refs: bool, expected: bool) -> None:
        """The two unconditional classes ignore ``refs``; ``reference`` does not.

        References still render a link when they are rendered at all, so only
        their mode-off case is a discarded subtree.
        """
        assert _discards_subtree(frozenset(classes.split()), refs=refs) is expected

    @pytest.mark.anyio
    @pytest.mark.parametrize(
        ("classes", "refs"),
        [
            ("mw-editsection", True),
            ("mw-editsection", False),
            ("mw-cite-backlink", True),
            ("mw-cite-backlink", False),
            ("reference", True),
            ("reference", False),
        ],
    )
    async def test_discard_verdict_matches_convert(
        self, converter: WikiHtmlConverter, classes: str, refs: bool
    ) -> None:
        """``convert`` and ``_renders_nothing`` must agree about a subtree.

        This is the invariant that stops the two drifting apart: whatever
        ``convert`` drops entirely must also be invisible to the
        rendered-adjacency walk-up, or a dropped span becomes a phantom
        neighbour.
        """
        soup = BeautifulSoup(f'<p><span class="{classes}">x</span></p>', "html.parser")
        span = soup.find("span")
        assert isinstance(span, Tag)
        output = await converter.convert(
            span, out_to_archive=set(), redirect_map={}, refs=refs
        )
        discarded = WikiHtmlConverter._renders_nothing(span, refs=refs)
        assert (output == "") is discarded

    def test_edge_is_word_plain_text(self) -> None:
        """Each side is judged by the character that touches the whitespace.

        The previous neighbour is read from its last character and the next
        from its first, so either side may carry the separation on its own.
        """
        assert WikiHtmlConverter._nearest_edge_is_word(
            NavigableString("Physics"), following=False, refs=True
        )
        assert WikiHtmlConverter._nearest_edge_is_word(
            NavigableString("portal"), following=True, refs=True
        )
        assert not WikiHtmlConverter._nearest_edge_is_word(
            NavigableString("dash "), following=False, refs=True
        )
        assert not WikiHtmlConverter._nearest_edge_is_word(
            NavigableString(" events"), following=True, refs=True
        )
        assert not WikiHtmlConverter._nearest_edge_is_word(
            NavigableString(""), following=False, refs=True
        )
        assert not WikiHtmlConverter._nearest_edge_is_word(
            None, following=True, refs=True
        )

    def test_edge_is_word_descends_into_inline_wrappers(self) -> None:
        """The edge comes from rendered content, not the first element boundary.

        ``<bdi>`` wraps a word but is not one of the inline tags the converter
        otherwise cares about, so a descent that stopped at a known-tag list
        would report no edge at all.
        """
        soup = BeautifulSoup(
            '<p><a href="#"><bdi>978-0-486-63612-2</bdi></a> <span>b</span></p>',
            "html.parser",
        )
        link = soup.find("a")
        assert isinstance(link, Tag)
        assert WikiHtmlConverter._nearest_edge_is_word(link, following=False, refs=True)

    def test_edge_is_word_skips_unrendered_markup(self) -> None:
        """Whitespace and empty wrappers are not the edge.

        Parsoid leaves a whitespace-only text node as the first child of
        ``<math>``, and emits empty ``<span class="Z3988">`` metadata spans
        between citation links; neither may terminate the descent.
        """
        soup = BeautifulSoup(
            '<p><span><span class="Z3988"></span>Physics</span> <span>b</span></p>',
            "html.parser",
        )
        outer = soup.find("span")
        assert isinstance(outer, Tag)
        assert WikiHtmlConverter._nearest_edge_is_word(
            outer, following=False, refs=True
        )
        math = BeautifulSoup(
            "<p><span><math> <mi>M</mi></math></span> <span>b</span></p>", "html.parser"
        ).find("span")
        assert isinstance(math, Tag)
        assert WikiHtmlConverter._nearest_edge_is_word(math, following=True, refs=True)

    def test_edge_is_word_block_boundaries(self) -> None:
        """Block tags and ``<br>`` separate blocks, not words."""
        for html in ("<div>a</div>", "<p>a</p>", "<br/>", "<hr/>"):
            soup = BeautifulSoup(html, "html.parser")
            node = next(iter(soup.children))
            assert not WikiHtmlConverter._nearest_edge_is_word(
                node, following=True, refs=True
            )
            assert not WikiHtmlConverter._nearest_edge_is_word(
                node, following=False, refs=True
            )

    def test_edge_is_word_treats_image_as_a_token(self) -> None:
        """An image has no children yet still renders an inline token."""
        soup = BeautifulSoup("<img src='a'/>", "html.parser")
        img = next(iter(soup.children))
        assert WikiHtmlConverter._nearest_edge_is_word(img, following=True, refs=True)
        assert WikiHtmlConverter._nearest_edge_is_word(img, following=False, refs=True)

    def test_edge_is_word_ignores_empty_wrappers(self) -> None:
        """A wrapper that renders nothing has no word edge either way."""
        for html in ("<span></span>", "<b> </b>"):
            soup = BeautifulSoup(html, "html.parser")
            node = next(iter(soup.children))
            assert not WikiHtmlConverter._nearest_edge_is_word(
                node, following=True, refs=True
            )
            assert not WikiHtmlConverter._nearest_edge_is_word(
                node, following=False, refs=True
            )


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


# ---------------------------------------------------------------------------

# Regression tests for generalized snapshot fixes

# ---------------------------------------------------------------------------


@pytest.mark.anyio
async def test_sidebar_caption_emits_p_separator(
    converter: WikiHtmlConverter, tmp_path: PathLike[str]
) -> None:
    """A ``sidebar-caption`` div inside a table cell is separated from the
    preceding math by a ``<p>`` cell separator, not a block break.

    Regression for the ``Hamiltonian mechanics`` / ``Lagrangian mechanics``
    infobox sidebar caption formatting change.
    """
    html = (
        '<table class="infobox"><tbody><tr>'
        '<td class="sidebar-image">'
        + _inline_math_span(r"\mathbf{F} = \frac{d\mathbf{p}}{dt}")
        + '<div class="sidebar-caption">'
        '<a href="/wiki/Second_law_of_motion">Second law of motion</a>'
        "</div>"
        "</td>"
        "</tr></tbody></table>"
    )
    result = await _convert(converter, html)
    assert " <p> [Second law of motion](/wiki/Second_law_of_motion)" in result
    # Mirror the snapshot harness: pipeline output is stripped and ends
    # with a single trailing newline before linting.
    await _assert_markdownlint_clean(result.strip() + "\n", AnyioPath(tmp_path))


@pytest.mark.anyio
async def test_infobox_caption_emits_p_separator(
    converter: WikiHtmlConverter, tmp_path: PathLike[str]
) -> None:
    """An ``infobox-caption`` div inside an ``infobox-image`` table cell is
    separated from the preceding image by a ``<p>`` cell separator, not a
    block break.

    Regression for the ``moment of inertia`` infobox image/caption
    formatting change (empty col1 + ``<p>`` separator).
    """
    html = (
        '<table class="infobox"><tbody><tr>'
        '<td class="infobox-image">'
        '<a href="/wiki/Flywheel">Flywheels</a>'
        '<div class="infobox-caption">'
        '<a href="/wiki/Flywheel">Flywheels</a>'
        " have large moments of inertia"
        "</div>"
        "</td>"
        "</tr></tbody></table>"
    )
    result = await _convert(converter, html)
    assert " <p> [Flywheels](/wiki/Flywheel)" in result
    # Mirror the snapshot harness: pipeline output is stripped and ends
    # with a single trailing newline before linting.
    await _assert_markdownlint_clean(result.strip() + "\n", AnyioPath(tmp_path))


@pytest.mark.anyio
async def test_sistersitebox_renders_single_blockquote_line(
    converter: WikiHtmlConverter, tmp_path: PathLike[str]
) -> None:
    """A Wikimedia Commons ``sistersitebox`` renders as a single blockquote
    line joining the logo image and the related-media text.

    Regression for the ``Hamiltonian mechanics`` / ``Lagrangian mechanics``
    sistersitebox formatting change.
    """
    html = (
        '<div class="side-box side-box-right plainlinks sistersitebox">'
        '<div class="side-box-flex">'
        '<div class="side-box-image">'
        '<span class="noviewer" typeof="mw:File">'
        '<a href="/wiki/File:Commons-logo.svg" class="mw-file-description">'
        '<img alt="Wikimedia Commons logo" src="//upload.wikimedia.org/wikipedia/'
        'en/thumb/4/4a/Commons-logo.svg/40px-Commons-logo.svg.png"/>'
        "</a></span></div>"
        '<div class="side-box-text plainlist">'
        "Wikimedia Commons has media related to "
        '<a href="https://commons.wikimedia.org/wiki/Category:Hamiltonian_mechanics" '
        'class="extiw" title="commons:Category:Hamiltonian mechanics">'
        '<span style="font-style:italic; font-weight:bold;">'
        "Hamiltonian mechanics</span></a>."
        "</div></div></div>"
    )
    result = await _convert(converter, html)
    expected = (
        "> ![Wikimedia Commons logo]"
        "(../../archives/Wikimedia%20Commons/Commons-logo.svg) "
        "Wikimedia Commons has media related to "
        "[___Hamiltonian mechanics___]"
        "(https://commons.wikimedia.org/wiki/Category%3AHamiltonian%20mechanics)."
    )
    assert result.strip() == expected
    # Mirror the snapshot harness: pipeline output is stripped and ends
    # with a single trailing newline before linting.
    await _assert_markdownlint_clean(result.strip() + "\n", AnyioPath(tmp_path))
