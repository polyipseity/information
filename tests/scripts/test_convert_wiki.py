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

from scripts import convert_wiki as _mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestModuleExports:
    """Tests for module-level behavior."""

    def test_all_is_empty(self) -> None:
        """__all__ should be an empty tuple (standalone script)."""
        assert _mod.__all__ == ()


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

        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=top_dir,
            converted_wiki_lang_dir=lang_dir,
        )
        html = BeautifulSoup(
            '<a title="From Page" href="/wiki/From_Page">link</a>',
            "html.parser",
        )
        redirect_map = {
            "From Page": _mod._RedirectInfo(to="To Page"),  # noqa: SLF001
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

        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=top_dir,
            converted_wiki_lang_dir=lang_dir,
        )
        html = BeautifulSoup(
            '<a title="Same Page" href="/wiki/Same_Page">link</a>',
            "html.parser",
        )
        redirect_map = {
            "Same Page": _mod._RedirectInfo(to="Same Page"),  # noqa: SLF001
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

        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=top_dir,
            converted_wiki_lang_dir=lang_dir,
        )
        html = BeautifulSoup(
            '<a title="From Page" href="/wiki/From_Page">link</a>',
            "html.parser",
        )
        redirect_map = {
            "From Page": _mod._RedirectInfo(to="To Page"),  # noqa: SLF001
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

        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=top_dir,
            converted_wiki_lang_dir=lang_dir,
        )
        html = BeautifulSoup(
            '<a title="From Page" href="/wiki/From_Page">link</a>',
            "html.parser",
        )
        redirect_map = {
            "From Page": _mod._RedirectInfo(to="To Page"),  # noqa: SLF001
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
            k: _mod._RedirectInfo(to=v["to"], tofragment=v.get("tofragment", ""))
            for k, v in aux["redirect_cache"].items()
        }

        # Build the name_map: start with the shared baseline, then apply
        # per-test overrides (for titles not in the global name_map).
        names_map = shared_name_map | aux["name_map_overrides"]

        # run_pipeline handles all post-processing (nbsp→space, hair→&hairsp;, strip).
        output, _ = await _mod.run_pipeline(
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
        html = _mod.BeautifulSoup(
            '<img resource="//en.wikipedia.org/wiki/File:Foo_Bar.svg" src=""/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = _mod._get_image_filename(img)  # noqa: SLF001
        assert result == "Foo Bar.svg"

    def test_get_image_filename_from_src_upload(self) -> None:
        """``_get_image_filename`` should fall back to ``src`` when ``resource`` is missing."""
        # This is a `src` URL matching the first upload regex pattern
        html = _mod.BeautifulSoup(
            '<img src="https://upload.wikimedia.org/wikipedia/en/9/9a/ExampleImage.svg"/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = _mod._get_image_filename(img)  # noqa: SLF001
        assert result == "ExampleImage.svg"

    def test_get_image_filename_from_src_thumb(self) -> None:
        """``_get_image_filename`` should extract filename from thumb ``src`` URL."""
        html = _mod.BeautifulSoup(
            '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Modernphysicsfields.svg/500px-Modernphysicsfields.svg.png"/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = _mod._get_image_filename(img)  # noqa: SLF001
        assert result == "Modernphysicsfields.svg"

    def test_get_image_filename_missing(self) -> None:
        """``_get_image_filename`` should return ``None`` when neither attribute is usable."""
        html = _mod.BeautifulSoup('<img alt="no url"/>', "html.parser")
        img = html.find("img")
        assert isinstance(img, Tag)
        result = _mod._get_image_filename(img)  # noqa: SLF001
        assert result is None

    def test_get_image_filename_non_matching_src(self) -> None:
        """``_get_image_filename`` should return ``None`` when src doesn't match archive patterns."""
        html = _mod.BeautifulSoup(
            '<img src="https://example.com/not/a/wikimedia/url.svg"/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = _mod._get_image_filename(img)  # noqa: SLF001
        assert result is None

    def test_collect_image_filenames(self) -> None:
        """``_collect_image_filenames`` should collect ``File:XXX`` titles from all images."""
        html = _mod.BeautifulSoup(
            """
            <html>
            <img resource="//en.wikipedia.org/wiki/File:First.svg" src=""/>
            <img src="https://upload.wikimedia.org/wikipedia/en/9/9a/Second.svg"/>
            <img alt="no resource"/>
            </html>
            """,
            "html.parser",
        )
        result = _mod._collect_image_filenames(html)  # noqa: SLF001
        assert result == {"File:First.svg", "File:Second.svg"}

    def test_fallback_alt_empty_metadata(self) -> None:
        """``_fallback_alt`` should return ``File:XXX`` when metadata dict is empty."""
        converter = _mod.WikiHtmlConverter(image_metadata={})
        html = _mod.BeautifulSoup(
            '<img resource="//en.wikipedia.org/wiki/File:Foo.svg" src=""/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = converter._fallback_alt(img)  # noqa: SLF001
        assert result == "File:Foo.svg"

    def test_fallback_alt_with_metadata(self) -> None:
        """``_fallback_alt`` should return metadata description when available."""
        converter = _mod.WikiHtmlConverter(
            image_metadata={"File:Foo.svg": "A description of Foo"}
        )
        html = _mod.BeautifulSoup(
            '<img resource="//en.wikipedia.org/wiki/File:Foo.svg" src=""/>',
            "html.parser",
        )
        img = html.find("img")
        assert isinstance(img, Tag)
        result = converter._fallback_alt(img)  # noqa: SLF001
        assert result == "A description of Foo"

    def test_fallback_alt_unmapped_image(self) -> None:
        """``_fallback_alt`` should return empty string when image cannot be mapped to any filename."""
        converter = _mod.WikiHtmlConverter(image_metadata={})
        html = _mod.BeautifulSoup('<img alt="no url"/>', "html.parser")
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
        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = _mod.BeautifulSoup(
            "<ul><li>Multi-line list item.</li></ul>", "html.parser"
        )
        expanded = _mod.BeautifulSoup(
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
        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = _mod.BeautifulSoup("<p>Multi-line paragraph.</p>", "html.parser")
        expanded = _mod.BeautifulSoup(
            "<p>\n  Multi-line\n  paragraph.\n</p>", "html.parser"
        )

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
        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = _mod.BeautifulSoup(
            '<a href="/wiki/Test" title="Test">Multi-line link</a>',
            "html.parser",
        )
        expanded = _mod.BeautifulSoup(
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
        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = _mod.BeautifulSoup("<h2>Multi-line header</h2>", "html.parser")
        expanded = _mod.BeautifulSoup(
            "<h2>\n  Multi-line\n  header\n</h2>", "html.parser"
        )

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
        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = _mod.BeautifulSoup(
            "<table><tr><td>Multi-line cell</td></tr></table>", "html.parser"
        )
        expanded = _mod.BeautifulSoup(
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
        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = _mod.BeautifulSoup(
            "<p>Some <span>inline</span> text.</p>", "html.parser"
        )
        expanded = _mod.BeautifulSoup(
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
        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = _mod.BeautifulSoup(
            "<p><b>Bold</b> and <i>italic</i> text.</p>", "html.parser"
        )
        expanded = _mod.BeautifulSoup(
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
        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        compact = _mod.BeautifulSoup(
            '<a class="mw-selflink" href="/wiki/Test">Multi-line selflink</a>',
            "html.parser",
        )
        expanded = _mod.BeautifulSoup(
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
        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=lang_dir,
        )

        html = _mod.BeautifulSoup(
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
        soup = _mod.BeautifulSoup(
            '<div>a <a href="https://en.wikipedia.org/wiki/Example" class="extiw" title="w:Example">link</a> applied</div>',
            "html.parser",
        )
        div = soup.find("div")
        assert isinstance(div, Tag)
        for a in div.find_all("a"):
            a.attrs.pop("title", None)
        converter = _mod.WikiHtmlConverter()
        result = await converter.convert(
            div, out_to_archive=set(), refs=False, redirect_map={}
        )
        assert "a [link](https://en.wikipedia.org/wiki/Example) applied" in result

    @pytest.mark.anyio
    async def test_preserves_spaces_around_multiple_links(self) -> None:
        """Multiple links in image description must each have correct spacing."""
        soup = _mod.BeautifulSoup(
            '<div>are <a href="https://en.wikipedia.org/wiki/Overtone" class="extiw">overtones</a> and <a href="https://en.wikipedia.org/wiki/Harmonic" class="extiw">harmonics</a> here</div>',
            "html.parser",
        )
        div = soup.find("div")
        assert isinstance(div, Tag)
        for a in div.find_all("a"):
            a.attrs.pop("title", None)
        converter = _mod.WikiHtmlConverter()
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
        soup = _mod.BeautifulSoup(
            '<div><a href="https://en.wikipedia.org/wiki/Graph_of_a_function" class="extiw">Graph</a> of the normalized function</div>',
            "html.parser",
        )
        div = soup.find("div")
        assert isinstance(div, Tag)
        for a in div.find_all("a"):
            a.attrs.pop("title", None)
        converter = _mod.WikiHtmlConverter()
        result = await converter.convert(
            div, out_to_archive=set(), refs=False, redirect_map={}
        )
        assert result.startswith(
            "[Graph](https://en.wikipedia.org/wiki/Graph_of_a_function) of"
        )
