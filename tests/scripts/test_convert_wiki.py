"""Tests for scripts/convert_wiki.py.

These tests cover the pure functions and module-level constants that are
testable without HTTP requests or clipboard access.
"""

import json
from os import PathLike
from pathlib import Path as PathlibPath

import pytest
from anyio import Path
from bs4 import BeautifulSoup, Tag

from scripts.convert_wiki import config
from scripts.convert_wiki.api import _collect_image_filenames
from scripts.convert_wiki.converter import WikiHtmlConverter
from scripts.convert_wiki.pipeline import run_pipeline
from scripts.convert_wiki.types import _RedirectInfo
from scripts.convert_wiki.utils import _get_image_filename

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestModuleExports:
    """Tests for module-level behavior."""

    def test_all_is_empty(self) -> None:
        """__all__ should be an empty tuple (standalone script)."""
        assert config.__all__ == ()


class TestSymlinkCreation:
    """Tests for symlink creation in _handle_link.

    When a Wikipedia page redirects to another page, symlinks are created
    so that both filenames resolve to the same Markdown file.
    """

    @pytest.mark.anyio
    async def test_symlink_created_when_from_missing_and_differs(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should create both symlinks when from/to differ and FROM is missing."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        top_dir = tmp / "general"
        await lang_dir.mkdir(parents=True)

        converter = WikiHtmlConverter(
            converted_wiki_dir=top_dir,
            converted_wiki_lang_dir=lang_dir,
        )
        html = BeautifulSoup(
            '<a title="From Page" href="/wiki/From_Page">link</a>',
            "html.parser",
        )
        redirect_map = {
            "From Page": _RedirectInfo(to="To Page"),
        }

        await converter.convert(
            html,
            out_to_archive=set(),
            redirect_map=redirect_map,
            refs=True,
        )

        from_symlink = lang_dir / "From Page.md"
        top_symlink = top_dir / "From Page.md"
        assert await from_symlink.is_symlink()
        assert await top_symlink.is_symlink()
        assert str(await from_symlink.readlink()) == "To Page.md"
        assert str(await top_symlink.readlink()) == "eng/From Page.md"

    @pytest.mark.anyio
    async def test_symlink_not_created_when_same(self, tmp_path: PathLike[str]) -> None:
        """Should not create symlinks when from/to filenames are identical."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        top_dir = tmp / "general"
        await lang_dir.mkdir(parents=True)

        converter = WikiHtmlConverter(
            converted_wiki_dir=top_dir,
            converted_wiki_lang_dir=lang_dir,
        )
        html = BeautifulSoup(
            '<a title="Same Page" href="/wiki/Same_Page">link</a>',
            "html.parser",
        )
        redirect_map = {
            "Same Page": _RedirectInfo(to="Same Page"),
        }

        await converter.convert(
            html,
            out_to_archive=set(),
            redirect_map=redirect_map,
            refs=True,
        )

        assert not await (lang_dir / "Same Page.md").is_symlink()
        assert not await (top_dir / "Same Page.md").is_symlink()

    @pytest.mark.anyio
    async def test_symlink_not_created_when_from_exists(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should skip symlink creation when FROM file already exists."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        top_dir = tmp / "general"
        await lang_dir.mkdir(parents=True)

        # Pre-create the FROM file
        await (lang_dir / "From Page.md").write_text(
            "existing content", encoding="UTF-8"
        )

        converter = WikiHtmlConverter(
            converted_wiki_dir=top_dir,
            converted_wiki_lang_dir=lang_dir,
        )
        html = BeautifulSoup(
            '<a title="From Page" href="/wiki/From_Page">link</a>',
            "html.parser",
        )
        redirect_map = {
            "From Page": _RedirectInfo(to="To Page"),
        }

        await converter.convert(
            html,
            out_to_archive=set(),
            redirect_map=redirect_map,
            refs=True,
        )

        # FROM file should remain a regular file (not a symlink)
        assert await (lang_dir / "From Page.md").is_file()
        assert not await (lang_dir / "From Page.md").is_symlink()
        # Top-level symlink should not exist
        assert not await (top_dir / "From Page.md").is_symlink()

    @pytest.mark.anyio
    async def test_symlink_file_exists_error_suppressed(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should suppress FileExistsError when FROM is a broken symlink.

        A broken symlink has exists()=False but can't be overwritten by
        os.symlink(), so the suppress() guard handles it.
        """
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        top_dir = tmp / "general"
        await lang_dir.mkdir(parents=True)

        # Create a broken symlink at FROM path: exists() returns False,
        # but symlink_to() raises FileExistsError
        await (lang_dir / "From Page.md").symlink_to("nonexistent.md")
        assert not await (lang_dir / "From Page.md").exists()  # broken symlink

        converter = WikiHtmlConverter(
            converted_wiki_dir=top_dir,
            converted_wiki_lang_dir=lang_dir,
        )
        html = BeautifulSoup(
            '<a title="From Page" href="/wiki/From_Page">link</a>',
            "html.parser",
        )
        redirect_map = {
            "From Page": _RedirectInfo(to="To Page"),
        }

        # Should not crash despite FileExistsError
        await converter.convert(
            html,
            out_to_archive=set(),
            redirect_map=redirect_map,
            refs=True,
        )

        # Broken symlink should remain unchanged
        assert await (lang_dir / "From Page.md").is_symlink()
        assert str(await (lang_dir / "From Page.md").readlink()) == "nonexistent.md"
        # Top-level symlink should still be created (separate guard)
        assert await (top_dir / "From Page.md").is_symlink()


"""Absolute path to the snapshot test fixtures directory."""
_SNAPSHOT_DIR = (
    PathlibPath(__file__).resolve(strict=True).with_name("convert_wiki") / "snapshots"
)


def _discover_snapshot_cases() -> list[str]:
    """Return fixture names by scanning ``*.input.html`` files."""
    if not _SNAPSHOT_DIR.is_dir():
        return []
    return sorted(
        f.stem.removesuffix(".input")
        for f in sorted(_SNAPSHOT_DIR.glob("*.input.html"))
    )


class TestWikiHtmlToPlaintextSnapshot:
    """Snapshot tests for the core wiki_html_to_plaintext function.

    Each pair of ``<name>.input.html`` and ``<name>.expected.md`` files in the
    ``snapshots/`` directory defines one parametrized test case.
    """

    @pytest.mark.anyio
    @pytest.mark.parametrize(
        "name",
        _discover_snapshot_cases(),
    )
    async def test_snapshot(self, name: str, tmp_path: PathLike[str]) -> None:
        """Verify that converting *name*.input.html matches *name*.expected.md.

        Uses ``run_pipeline`` with overridden data to avoid HTTP requests,
        filesystem access, and manual post-processing.
        """
        tmp = Path(tmp_path)
        isolated_lang = tmp / "general" / "eng"
        await isolated_lang.mkdir(parents=True)

        # Load shared name_map and per-test auxiliary data.
        shared_name_map_path = _SNAPSHOT_DIR / "name_map.json"
        shared_name_map = json.loads(shared_name_map_path.read_text(encoding="UTF-8"))
        aux_path = _SNAPSHOT_DIR / f"{name}.aux.json"
        aux = json.loads(aux_path.read_text(encoding="UTF-8"))

        input_path = _SNAPSHOT_DIR / f"{name}.input.html"
        expected_path = _SNAPSHOT_DIR / f"{name}.expected.md"

        # Read fixture files
        html_text = input_path.read_text(encoding="UTF-8")
        expected = expected_path.read_text(encoding="UTF-8").strip()

        # Parse HTML
        html = BeautifulSoup(html_text, "html.parser")

        # Load pre-computed data from aux instead of hitting the live API.
        redirect_map = {
            k: _RedirectInfo(to=v["to"], tofragment=v.get("tofragment", ""))
            for k, v in aux["redirect_cache"].items()
        }

        # Build the name_map: start with the shared baseline, then apply
        # per-test overrides (for titles not in the global name_map).
        names_map = shared_name_map | aux["name_map_overrides"]

        # run_pipeline handles all post-processing (nbsp→space, hair→&hairsp;, strip).
        output, _ = await run_pipeline(
            html,
            redirect_map=redirect_map,
            image_metadata=aux["image_metadata"],
            names_map=names_map,
            wiki_dir=tmp / "general",
            wiki_lang_dir=isolated_lang,
            refs=True,
        )

        assert output == expected


class TestImageAltTextFallback:
    """Tests for image alt text fallback chain (``_get_image_filename``, ``_fallback_alt``, ``_collect_image_filenames``)."""

    def test_get_image_filename_from_resource(self) -> None:
        """``_get_image_filename`` should extract filename from ``resource`` attribute."""
        html = BeautifulSoup(
            '<img resource="//en.wikipedia.org/wiki/File:Foo_Bar.svg" src=""/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = _get_image_filename(img)
        assert result == "Foo Bar.svg"

    def test_get_image_filename_from_src_upload(self) -> None:
        """``_get_image_filename`` should fall back to ``src`` when ``resource`` is missing."""
        # This is a `src` URL matching the first upload regex pattern
        html = BeautifulSoup(
            '<img src="https://upload.wikimedia.org/wikipedia/en/9/9a/ExampleImage.svg"/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = _get_image_filename(img)
        assert result == "ExampleImage.svg"

    def test_get_image_filename_from_src_thumb(self) -> None:
        """``_get_image_filename`` should extract filename from thumb ``src`` URL."""
        html = BeautifulSoup(
            '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Modernphysicsfields.svg/500px-Modernphysicsfields.svg.png"/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = _get_image_filename(img)
        assert result == "Modernphysicsfields.svg"

    def test_get_image_filename_missing(self) -> None:
        """``_get_image_filename`` should return ``None`` when neither attribute is usable."""
        html = BeautifulSoup('<img alt="no url"/>', "html.parser")
        img = html.find("img")
        assert isinstance(img, Tag)
        result = _get_image_filename(img)
        assert result is None

    def test_get_image_filename_non_matching_src(self) -> None:
        """``_get_image_filename`` should return ``None`` when src doesn't match archive patterns."""
        html = BeautifulSoup(
            '<img src="https://example.com/not/a/wikimedia/url.svg"/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = _get_image_filename(img)
        assert result is None

    def test_collect_image_filenames(self) -> None:
        """``_collect_image_filenames`` should collect ``File:XXX`` titles from all images."""
        html = BeautifulSoup(
            """
            <html>
            <img resource="//en.wikipedia.org/wiki/File:First.svg" src=""/>
            <img src="https://upload.wikimedia.org/wikipedia/en/9/9a/Second.svg"/>
            <img alt="no resource"/>
            </html>
            """,
            "html.parser",
        )
        result = _collect_image_filenames(html)
        assert result == {"File:First.svg", "File:Second.svg"}

    def test_fallback_alt_empty_metadata(self) -> None:
        """``_fallback_alt`` should return ``File:XXX`` when metadata dict is empty."""
        converter = WikiHtmlConverter(image_metadata={})
        html = BeautifulSoup(
            '<img resource="//en.wikipedia.org/wiki/File:Foo.svg" src=""/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = converter._fallback_alt(img)  # noqa: SLF001
        assert result == "File:Foo.svg"

    def test_fallback_alt_with_metadata(self) -> None:
        """``_fallback_alt`` should return metadata description when available."""
        converter = WikiHtmlConverter(
            image_metadata={"File:Foo.svg": "A description of Foo"}
        )
        html = BeautifulSoup(
            '<img resource="//en.wikipedia.org/wiki/File:Foo.svg" src=""/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = converter._fallback_alt(img)  # noqa: SLF001
        assert result == "A description of Foo"

    def test_fallback_alt_unmapped_image(self) -> None:
        """``_fallback_alt`` should return empty string when image cannot be mapped to any filename."""
        converter = WikiHtmlConverter(image_metadata={})
        html = BeautifulSoup('<img alt="no url"/>', "html.parser")
        img = html.find("img")
        assert isinstance(img, Tag)
        result = converter._fallback_alt(img)  # noqa: SLF001
        assert result == ""


class TestFormattingAgnostic:
    """Verify that conversion output is invariant under HTML source formatting whitespace.

    HTML-to-Markdown conversion must produce identical output regardless of
    HTML source formatting whitespace (indentation, newlines between tags).
    It must only depend on HTML hierarchy and semantic data (tag names,
    attributes, structure).
    """

    @pytest.mark.anyio
    async def test_list_text_formatting_invariant(
        self, tmp_path: PathLike[str]
    ) -> None:
        """List item text should not be hard-wrapped by source formatting."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = BeautifulSoup(
            "<ul><li>Multi-line list item.</li></ul>", "html.parser"
        )
        expanded = BeautifulSoup(
            "<ul><li>\n  Multi-line\n  list item.\n</li></ul>", "html.parser"
        )

        result_compact = await converter.convert(
            compact, out_to_archive=set(), redirect_map={}, refs=True
        )
        result_expanded = await converter.convert(
            expanded, out_to_archive=set(), redirect_map={}, refs=True
        )
        assert result_compact == result_expanded

    @pytest.mark.anyio
    async def test_paragraph_formatting_invariant(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Paragraph text should not be hard-wrapped by source formatting."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = BeautifulSoup("<p>Multi-line paragraph.</p>", "html.parser")
        expanded = BeautifulSoup("<p>\n  Multi-line\n  paragraph.\n</p>", "html.parser")

        assert await converter.convert(
            compact, out_to_archive=set(), redirect_map={}, refs=True
        ) == await converter.convert(
            expanded, out_to_archive=set(), redirect_map={}, refs=True
        )

    @pytest.mark.anyio
    async def test_link_text_formatting_invariant(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Link display text should be single-line regardless of source formatting."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = BeautifulSoup(
            '<a href="/wiki/Test" title="Test">Multi-line link</a>',
            "html.parser",
        )
        expanded = BeautifulSoup(
            '<a href="/wiki/Test" title="Test">\n  Multi-line\n  link\n</a>',
            "html.parser",
        )

        assert await converter.convert(
            compact, out_to_archive=set(), redirect_map={}, refs=True
        ) == await converter.convert(
            expanded, out_to_archive=set(), redirect_map={}, refs=True
        )

    @pytest.mark.anyio
    async def test_header_formatting_invariant(self, tmp_path: PathLike[str]) -> None:
        """Header text should be single-line regardless of source formatting."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = BeautifulSoup("<h2>Multi-line header</h2>", "html.parser")
        expanded = BeautifulSoup("<h2>\n  Multi-line\n  header\n</h2>", "html.parser")

        assert await converter.convert(
            compact, out_to_archive=set(), redirect_map={}, refs=True
        ) == await converter.convert(
            expanded, out_to_archive=set(), redirect_map={}, refs=True
        )

    @pytest.mark.anyio
    async def test_table_cell_formatting_invariant(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Table cell text should be invariant under source formatting."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = BeautifulSoup(
            "<table><tr><td>Multi-line cell</td></tr></table>", "html.parser"
        )
        expanded = BeautifulSoup(
            "<table><tr><td>\n  Multi-line\n  cell\n</td></tr></table>",
            "html.parser",
        )

        assert await converter.convert(
            compact, out_to_archive=set(), redirect_map={}, refs=True
        ) == await converter.convert(
            expanded, out_to_archive=set(), redirect_map={}, refs=True
        )

    @pytest.mark.anyio
    async def test_span_formatting_invariant(self, tmp_path: PathLike[str]) -> None:
        """Span text should not be affected by source formatting."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = BeautifulSoup("<p>Some <span>inline</span> text.</p>", "html.parser")
        expanded = BeautifulSoup(
            "<p>Some\n<span>inline</span>\ntext.</p>",
            "html.parser",
        )

        assert await converter.convert(
            compact, out_to_archive=set(), redirect_map={}, refs=True
        ) == await converter.convert(
            expanded, out_to_archive=set(), redirect_map={}, refs=True
        )

    @pytest.mark.anyio
    async def test_mixed_bold_italic_formatting_invariant(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Mixed bold/italic formatting should survive source whitespace."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = BeautifulSoup(
            "<p><b>Bold</b> and <i>italic</i> text.</p>", "html.parser"
        )
        expanded = BeautifulSoup(
            "<p>\n  <b>Bold</b>\n  and\n  <i>italic</i>\n  text.\n</p>",
            "html.parser",
        )

        assert await converter.convert(
            compact, out_to_archive=set(), redirect_map={}, refs=True
        ) == await converter.convert(
            expanded, out_to_archive=set(), redirect_map={}, refs=True
        )

    @pytest.mark.anyio
    async def test_selflink_formatting_invariant(self, tmp_path: PathLike[str]) -> None:
        """Self-link display text should be single-line regardless of source formatting."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = BeautifulSoup(
            '<a class="mw-selflink" href="/wiki/Test">Multi-line selflink</a>',
            "html.parser",
        )
        expanded = BeautifulSoup(
            '<a class="mw-selflink" href="/wiki/Test">\n  Multi-line\n  selflink\n</a>',
            "html.parser",
        )

        assert await converter.convert(
            compact, out_to_archive=set(), redirect_map={}, refs=True
        ) == await converter.convert(
            expanded, out_to_archive=set(), redirect_map={}, refs=True
        )

    @pytest.mark.anyio
    async def test_list_text_not_hard_wrapped(self, tmp_path: PathLike[str]) -> None:
        """Regression: hard-wrapped HTML source should not produce hard-wrapped Markdown."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        html = BeautifulSoup(
            "<ul><li>\n    Some text that is hard-wrapped\n    in the HTML source.\n</li></ul>",
            "html.parser",
        )
        result = await converter.convert(
            html, out_to_archive=set(), redirect_map={}, refs=True
        )
        # List item content (after "- " prefix) should be a single line
        assert (
            result == "\n\n- Some text that is hard-wrapped in the HTML source.\n\n\n"
        )


class TestConverterLinkSpacing:
    """Regression tests for link spacing preservation in image descriptions.

    The ``_resolve_image_metadata`` function wraps HTML in a ``<div>`` and
    processes it through ``WikiHtmlConverter.convert()``.  The converter must
    preserve spaces around links — a space before a markdown link ``[...](...)``
    must remain a space, and a space after must remain a space.  The bug was
    that spaces around links in Commons API image descriptions were being
    dropped, producing text like ``a[link](url)applied`` (missing spaces).
    """

    @pytest.mark.anyio
    async def test_preserves_spaces_around_links(self) -> None:
        """Spaces before and after a single link in image description must be preserved."""
        soup = BeautifulSoup(
            '<div>a <a href="https://en.wikipedia.org/wiki/Example" class="extiw" title="w:Example">link</a> applied</div>',
            "html.parser",
        )
        div = soup.find("div")
        assert isinstance(div, Tag)
        for a in div.find_all("a"):
            a.attrs.pop("title", None)
        converter = WikiHtmlConverter()
        result = await converter.convert(
            div, out_to_archive=set(), refs=False, redirect_map={}
        )
        assert "a [link](https://en.wikipedia.org/wiki/Example) applied" in result

    @pytest.mark.anyio
    async def test_preserves_spaces_around_multiple_links(self) -> None:
        """Multiple links in image description must each have correct spacing."""
        soup = BeautifulSoup(
            '<div>are <a href="https://en.wikipedia.org/wiki/Overtone" class="extiw">overtones</a> and <a href="https://en.wikipedia.org/wiki/Harmonic" class="extiw">harmonics</a> here</div>',
            "html.parser",
        )
        div = soup.find("div")
        assert isinstance(div, Tag)
        for a in div.find_all("a"):
            a.attrs.pop("title", None)
        converter = WikiHtmlConverter()
        result = await converter.convert(
            div, out_to_archive=set(), refs=False, redirect_map={}
        )
        assert (
            "are [overtones](https://en.wikipedia.org/wiki/Overtone) and [harmonics](https://en.wikipedia.org/wiki/Harmonic) here"
            in result
        )

    @pytest.mark.anyio
    async def test_preserves_spaces_link_at_start(self) -> None:
        """A link at the start of an image description must have correct spacing after."""
        soup = BeautifulSoup(
            '<div><a href="https://en.wikipedia.org/wiki/Graph_of_a_function" class="extiw">Graph</a> of the normalized function</div>',
            "html.parser",
        )
        div = soup.find("div")
        assert isinstance(div, Tag)
        for a in div.find_all("a"):
            a.attrs.pop("title", None)
        converter = WikiHtmlConverter()
        result = await converter.convert(
            div, out_to_archive=set(), refs=False, redirect_map={}
        )
        assert result.startswith(
            "[Graph](https://en.wikipedia.org/wiki/Graph_of_a_function) of"
        )


class TestBlockMathParagraphAffiliation:
    """Tests that _handle_p and _handle_math produce correct paragraph affiliation.

    Block math inside a <p> should remain on the same line as adjacent text,
    wrapped by \n...\n\n. Whitespace collapse via process_strings keeps
    ``$$...$$`` inline within the paragraph.
    """

    @staticmethod
    def _make_converter(tmp_path: PathLike[str]) -> WikiHtmlConverter:
        """Create a WikiHtmlConverter with isolated lang dir."""
        return WikiHtmlConverter(
            converted_wiki_dir=Path(tmp_path) / "general",
            converted_wiki_lang_dir=Path(tmp_path) / "general" / "eng",
        )

    @staticmethod
    def _block_math_span(alttext: str) -> str:
        """Build a minimal block math DOM span.

        The *alttext* argument should contain the exact string to place
        in the ``alttext`` attribute, including any backslash escapes
        needed for LaTeX. Pass Python raw strings (``r"..."``) for
        reliability.
        """
        return (
            '<span class="mwe-math-element mwe-math-element-block">'
            '<span class="mwe-math-mathml-display mwe-math-mathml-a11y">'
            f'<math display="block" alttext="{alttext}">'
            "<semantics><mrow></mrow></semantics></math>"
            '<img class="mwe-math-fallback-image-display mw-invert skin-invert"/>'
            "</span></span>"
        )

    @pytest.mark.anyio
    async def test_both_text_before_and_after(self, tmp_path: PathLike[str]) -> None:
        """Block math with text before and after should stay inline in the paragraph."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = self._make_converter(tmp_path)
        html = BeautifulSoup(
            f"<p>before {self._block_math_span(r'{\displaystyle f(x)}')} after</p>",
            "html.parser",
        )
        result = await converter.convert(
            html, out_to_archive=set(), redirect_map={}, refs=True
        )
        assert "\nbefore $$f(x)$$ after\n\n" in result

    @pytest.mark.anyio
    async def test_before_only(self, tmp_path: PathLike[str]) -> None:
        """Block math at end of paragraph: text before, no text after."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = self._make_converter(tmp_path)
        html = BeautifulSoup(
            f"<p>before {self._block_math_span(r'{\displaystyle g(y)}')}</p>",
            "html.parser",
        )
        result = await converter.convert(
            html, out_to_archive=set(), redirect_map={}, refs=True
        )
        assert "\nbefore $$g(y)$$\n\n" in result

    @pytest.mark.anyio
    async def test_after_only(self, tmp_path: PathLike[str]) -> None:
        """Block math at start of paragraph: no text before, text after."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = self._make_converter(tmp_path)
        html = BeautifulSoup(
            f"<p>{self._block_math_span(r'{\displaystyle h(z)}')} after</p>",
            "html.parser",
        )
        result = await converter.convert(
            html, out_to_archive=set(), redirect_map={}, refs=True
        )
        assert "\n$$h(z)$$ after\n\n" in result

    @pytest.mark.anyio
    async def test_neither(self, tmp_path: PathLike[str]) -> None:
        """Block math standalone in paragraph (no text before or after)."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = self._make_converter(tmp_path)
        html = BeautifulSoup(
            f"<p>{self._block_math_span(r'{\displaystyle k(w)}')}</p>",
            "html.parser",
        )
        result = await converter.convert(
            html, out_to_archive=set(), redirect_map={}, refs=True
        )
        assert "\n$$k(w)$$\n\n" in result

    @pytest.mark.anyio
    async def test_multiple_block_math_in_one_paragraph(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Multiple block math spans in one paragraph stay inline with text."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = self._make_converter(tmp_path)
        html = BeautifulSoup(
            f"<p>start {self._block_math_span(r'{\displaystyle a(b)}')} "
            f"middle {self._block_math_span(r'{\displaystyle c(d)}')} end</p>",
            "html.parser",
        )
        result = await converter.convert(
            html, out_to_archive=set(), redirect_map={}, refs=True
        )
        assert "\nstart $$a(b)$$ middle $$c(d)$$ end\n\n" in result

    @pytest.mark.anyio
    async def test_block_math_formatting_invariant(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Source whitespace should not affect block math paragraph output."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = self._make_converter(tmp_path)

        math_span = self._block_math_span(r"{\displaystyle f(x)}")
        compact = BeautifulSoup(
            f"<p>before {math_span} after</p>",
            "html.parser",
        )
        expanded = BeautifulSoup(
            f"<p>\n  before\n  {math_span}\n  after\n</p>",
            "html.parser",
        )

        assert await converter.convert(
            compact, out_to_archive=set(), redirect_map={}, refs=True
        ) == await converter.convert(
            expanded, out_to_archive=set(), redirect_map={}, refs=True
        )


class TestBlockMathClassification:
    """Tests for _is_inline_math classification of block vs inline math.

    _is_inline_math checks the parent span's class for "inline", then walks
    up 2 levels to verify the great-grandparent has >1 child (sibling guard).
    Block math returns False; inline math requires both the class and the
    sibling guard to pass.
    """

    def test_block_math_display_class_returns_false(self) -> None:
        """Block math (mwe-math-mathml-display parent) should return False."""
        html = BeautifulSoup(
            '<span class="mwe-math-element mwe-math-element-block">'
            '<span class="mwe-math-mathml-display mwe-math-mathml-a11y">'
            '<math display="block"></math></span></span>',
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert WikiHtmlConverter._is_inline_math(math_ele) is False

    def test_inline_math_inline_class_with_guard_returns_true(self) -> None:
        """Inline math passing sibling guard (>1 children) should return True."""
        html = BeautifulSoup(
            "<p>text "
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            "<math></math></span></span></p>",
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert WikiHtmlConverter._is_inline_math(math_ele) is True

    def test_inline_math_sibling_guard_fails_returns_false(self) -> None:
        """Inline math with single-child ancestor (guard fails) should return False."""
        html = BeautifulSoup(
            "<p>"
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            "<math></math></span></span></p>",
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert WikiHtmlConverter._is_inline_math(math_ele) is False
