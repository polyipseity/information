"""Tests for scripts/convert_wiki.py.

These tests cover the pure functions and module-level constants that are
testable without HTTP requests or clipboard access.
"""

import json
import os
import re
import subprocess
from os import PathLike
from pathlib import Path as PathlibPath

import json5
import pytest
from anyio import Path, run_process
from bs4 import BeautifulSoup, Tag

from scripts.convert_wiki import config
from scripts.convert_wiki.api import _collect_image_filenames
from scripts.convert_wiki.converter import WikiHtmlConverter
from scripts.convert_wiki.pipeline import run_pipeline
from scripts.convert_wiki.table import TableConverter
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
    """Tests for symlink creation in _handle_anchor.

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
    async def test_real_lang_file_kept_but_mirror_created(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should keep a real FROM file but still create the top-level mirror."""
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

        # FROM file should remain a regular file (never replaced)
        assert await (lang_dir / "From Page.md").is_file()
        assert not await (lang_dir / "From Page.md").is_symlink()
        assert (
            await (lang_dir / "From Page.md").read_text(encoding="UTF-8")
            == "existing content"
        )
        # Top-level mirror should still be created
        from_symlink = top_dir / "From Page.md"
        assert await from_symlink.is_symlink()
        assert str(await from_symlink.readlink()) == "eng/From Page.md"

    @pytest.mark.anyio
    async def test_broken_symlink_retargeted(self, tmp_path: PathLike[str]) -> None:
        """Should retarget a broken FROM symlink to the new target."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        top_dir = tmp / "general"
        await lang_dir.mkdir(parents=True)

        # Create a broken symlink at FROM path
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

        await converter.convert(
            html,
            out_to_archive=set(),
            redirect_map=redirect_map,
            refs=True,
        )

        # Broken symlink should be retargeted
        from_symlink = lang_dir / "From Page.md"
        assert await from_symlink.is_symlink()
        assert str(await from_symlink.readlink()) == "To Page.md"
        # Top-level mirror should also be created
        top_symlink = top_dir / "From Page.md"
        assert await top_symlink.is_symlink()
        assert str(await top_symlink.readlink()) == "eng/From Page.md"


"""Absolute path to the snapshot test fixtures directory."""
_SNAPSHOT_DIR = (
    PathlibPath(__file__).resolve(strict=True).with_name("convert_wiki") / "snapshots"
)

"""Absolute path to the repository root (markdownlint invocation cwd)."""
_REPO_ROOT = PathlibPath(__file__).resolve(strict=True).parents[2]


def _discover_snapshot_cases() -> list[str]:
    """Return fixture names by scanning ``*.input.html`` files."""
    if not _SNAPSHOT_DIR.is_dir():
        return []
    return sorted(
        f.stem.removesuffix(".input")
        for f in sorted(_SNAPSHOT_DIR.glob("*.input.html"))
    )


def _load_snapshot_names_map() -> dict[str, str]:
    """Load the shared snapshot name map (symlink to production JSONC)."""
    path = _SNAPSHOT_DIR / "name_map.jsonc"
    with path.open(encoding="UTF-8") as names_map_file:
        return json5.load(names_map_file)


def _categorize_block_math_blocks(output: str) -> dict[str, int]:
    """Count block math paragraph affiliation categories in converter output.

    Returns a dict with keys ``"both"``, ``"before_only"``, ``"after_only"``,
    and ``"neither"``. Each ``$$...$$`` occurrence in the output is classified
    by whether non-whitespace text appears before and/or after it on the same
    line.
    """
    counts: dict[str, int] = {
        "both": 0,
        "before_only": 0,
        "after_only": 0,
        "neither": 0,
    }
    for line in output.splitlines():
        for match in re.finditer(r"\$\$(.+?)\$\$", line):
            before = line[: match.start()]
            after = line[match.end() :]
            has_before = bool(before.strip())
            has_after = bool(after.strip())
            if has_before and has_after:
                counts["both"] += 1
            elif has_before and not has_after:
                counts["before_only"] += 1
            elif not has_before and has_after:
                counts["after_only"] += 1
            else:
                counts["neither"] += 1
    return counts


async def _assert_markdownlint_clean(output: str, tmp: Path) -> None:
    """Assert generated ``output`` is markdownlint-clean under the snapshots config chain.

    Writes ``output`` and a temporary config extending the snapshots
    directory's own config (by absolute path, so the whole config chain
    applies regardless of where the tmp dir lives) into ``tmp``, then runs
    the repository-pinned markdownlint-cli2 on the written file.
    """
    out_path = tmp / "lint.md"
    config_path = tmp / ".markdownlint.jsonc"
    await out_path.write_text(output, encoding="UTF-8")
    await config_path.write_text(
        json.dumps({"extends": os.fspath(_SNAPSHOT_DIR / ".markdownlint.jsonc")}),
        encoding="UTF-8",
    )
    proc = await run_process(
        ["bun", "x", "markdownlint-cli2", "--no-globs", os.fspath(out_path)],
        cwd=os.fspath(_REPO_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert proc.returncode == 0, (
        f"converter output failed markdownlint:\n"
        f"{proc.stdout.decode()}{proc.stderr.decode()}"
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
        shared_name_map = _load_snapshot_names_map()
        aux_path = _SNAPSHOT_DIR / f"{name}.aux.json"
        aux = json.loads(aux_path.read_text(encoding="UTF-8"))

        input_path = _SNAPSHOT_DIR / f"{name}.input.html"
        expected_path = _SNAPSHOT_DIR / f"{name}.expected.md"

        # Read fixture files
        html_text = input_path.read_text(encoding="UTF-8")
        expected = expected_path.read_text(encoding="UTF-8").lstrip()

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
        await _assert_markdownlint_clean(output, tmp)


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

    The outer ``mwe-math-element-inline`` class alone is not authoritative:
    punct absorption and the sibling guard still force block classification.
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

    def test_inline_math_whitespace_siblings_not_counted(self) -> None:
        """Prettified block containers must not count whitespace-only siblings."""
        html = BeautifulSoup(
            "<dd>\n"
            '  <span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            "<math></math></span></span>\n"
            "</dd>",
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert WikiHtmlConverter._is_inline_math(math_ele) is False

    def test_dd_external_period_sole_formula_row_is_block(self) -> None:
        """External punct on sole formula rows in ``<dd>`` should classify as block."""
        html = BeautifulSoup(
            "<dd>"
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            '<math alttext="{\\displaystyle R(X,Y)}"></math>'
            "</span></span>."
            "</dd>",
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert WikiHtmlConverter._is_inline_math(math_ele, alt_text="R(X,Y)") is False

    def test_dt_external_period_sole_formula_row_is_block(self) -> None:
        """Sole-formula ``<dt>`` rows with external punct classify as block."""
        html = BeautifulSoup(
            "<dt>"
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            '<math alttext="{\\displaystyle b}"></math>'
            "</span></span>."
            "</dt>",
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert WikiHtmlConverter._is_inline_math(math_ele, alt_text="b") is False

    def test_outer_inline_class_ignored_when_absorption_fires(self) -> None:
        """Outer inline class does not override punct absorption for aligned envs."""
        html = BeautifulSoup(
            "<p>"
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            '<math alttext="{\\displaystyle \\begin{aligned}x&=1\\end{aligned}}"></math>'
            "</span></span>."
            "</p>",
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert (
            WikiHtmlConverter._is_inline_math(
                math_ele, alt_text=r"\begin{aligned}x&=1\end{aligned}"
            )
            is False
        )

    def test_dd_external_period_with_prose_stays_inline(self) -> None:
        """``<dd>`` rows with prose before the formula keep inline classification."""
        html = BeautifulSoup(
            "<dd>therefore "
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            '<math alttext="{\\displaystyle f(x)}"></math>'
            "</span></span>."
            "</dd>",
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert WikiHtmlConverter._is_inline_math(math_ele, alt_text="f(x)") is True

    def test_sfrac_like_math_without_outer_wrapper_stays_inline(self) -> None:
        """sfrac-style inline math should use the legacy sibling container walk."""
        html = BeautifulSoup(
            "<body><p>intro</p>"
            "<p>before "
            '<span class="mwe-math-mathml-inline">'
            '<math alttext="{\\displaystyle \\frac{a}{2\\pi}}"></math>'
            "</span>, after</p></body>",
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert (
            WikiHtmlConverter._is_inline_math(math_ele, alt_text=r"\frac{a}{2\pi}")
            is True
        )


class TestExternalMathPunctuationPipeline:
    """End-to-end regression for external math punctuation through ``run_pipeline``."""

    @staticmethod
    def _inline_math_span(alttext: str) -> str:
        """Build an inline-math HTML span containing the given alt text."""
        return (
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-inline mwe-math-mathml-a11y">'
            f'<math display="inline" alttext="{alttext}">'
            "<semantics><mrow></mrow></semantics></math>"
            "</span></span>"
        )

    @pytest.mark.anyio
    async def test_pipeline_absorbs_dd_external_period(
        self, tmp_path: PathLike[str]
    ) -> None:
        """``run_pipeline`` should emit block math with ``\\,``-prefixed absorbed punct."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        body = (
            "<p>For vector fields $X,Y$ by</p>"
            f"<dl><dd>{self._inline_math_span(r'{\displaystyle R(X,Y)}')}.</dd></dl>"
        )
        html = BeautifulSoup(f"<body>{body}</body>", "html.parser")
        output, _ = await run_pipeline(
            html,
            redirect_map={},
            image_metadata={},
            names_map={},
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
            refs=False,
        )
        assert "$$R(X,Y)\\,.$$" in output
        assert "$R(X,Y)$." not in output
        assert output.count("$$R(X,Y)\\,.$$") == 1

    @pytest.mark.anyio
    async def test_pipeline_absorbs_dt_external_period(
        self, tmp_path: PathLike[str]
    ) -> None:
        """``run_pipeline`` emits block math with absorbed punct in ``<dt>`` rows."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        body = (
            "<p>For vector fields $X,Y$ by</p>"
            f"<dl><dt>{self._inline_math_span(r'{\displaystyle R(X,Y)}')}.</dt></dl>"
        )
        html = BeautifulSoup(f"<body>{body}</body>", "html.parser")
        output, _ = await run_pipeline(
            html,
            redirect_map={},
            image_metadata={},
            names_map={},
            wiki_dir=tmp / "general",
            wiki_lang_dir=lang_dir,
            refs=False,
        )
        assert "$$R(X,Y)\\,.$$" in output
        assert "$R(X,Y)$." not in output
        assert output.count("$$R(X,Y)\\,.$$") == 1


class TestBlockMathCategoryBreakdown:
    """Verify block math paragraph affiliation category counts in a real article.

    Uses the "Fourier transform" snapshot fixture as a regression baseline
    for the distribution of BOTH, BEFORE_ONLY, AFTER_ONLY, and NEITHER
    categories.
    """

    _SNAPSHOT_NAME = "Fourier transform"

    @staticmethod
    async def _run_and_categorize(tmp_path: PathLike[str]) -> dict[str, int]:
        """Run the Fourier transform pipeline and categorize block math output.

        Mirrors the snapshot test setup (aux.json, name_map.jsonc, etc.)
        but returns category counts instead of comparing to expected output.
        """
        tmp = Path(tmp_path)
        isolated_lang = tmp / "general" / "eng"
        await isolated_lang.mkdir(parents=True)

        shared_name_map = _load_snapshot_names_map()
        aux_path = (
            _SNAPSHOT_DIR / f"{TestBlockMathCategoryBreakdown._SNAPSHOT_NAME}.aux.json"
        )
        aux = json.loads(aux_path.read_text(encoding="UTF-8"))

        input_path = (
            _SNAPSHOT_DIR
            / f"{TestBlockMathCategoryBreakdown._SNAPSHOT_NAME}.input.html"
        )
        html_text = input_path.read_text(encoding="UTF-8")
        html = BeautifulSoup(html_text, "html.parser")

        redirect_map = {
            k: _RedirectInfo(to=v["to"], tofragment=v.get("tofragment", ""))
            for k, v in aux["redirect_cache"].items()
        }
        names_map = shared_name_map | aux["name_map_overrides"]

        output, _ = await run_pipeline(
            html,
            redirect_map=redirect_map,
            image_metadata=aux["image_metadata"],
            names_map=names_map,
            wiki_dir=tmp / "general",
            wiki_lang_dir=isolated_lang,
            refs=True,
        )
        return _categorize_block_math_blocks(output)

    @staticmethod
    def _assert_counts(counts: dict[str, int], **expected: int) -> None:
        """Assert that *counts* match all specified *expected* categories."""
        for category, expected_value in expected.items():
            actual = counts.get(category, 0)
            assert actual == expected_value, (
                f"Category {category!r}: expected {expected_value}, got {actual}"
            )

    @pytest.mark.anyio
    async def test_category_counts(self, tmp_path: PathLike[str]) -> None:
        """All four categories should match the known Fourier transform distribution."""
        counts = await self._run_and_categorize(tmp_path)
        self._assert_counts(
            counts,
            both=308,
            before_only=50,
            after_only=3,
            neither=4,
        )


class TestInlineMathIndependence:
    """Verify inline math is correctly delimited and has no orphaned ``$`` signs.

    Uses the "Fourier transform" snapshot fixture as a regression baseline
    for inline math count and delimiter hygiene.
    """

    _SNAPSHOT_NAME = "Fourier transform"

    @staticmethod
    def _count_inline_math_blocks(output: str) -> int:
        """Count ``$...$`` inline math blocks (excluding ``$$...$$`` block math)."""
        return len(re.findall(r"(?<!\$)\$(?!\$).+?(?<!\$)\$(?!\$)", output))

    @staticmethod
    def _has_orphaned_dollar_signs(output: str) -> bool:
        """Return ``True`` if any ``$`` is not part of a valid math delimiter pair.

        Strips all ``$$...$$`` blocks and ``$...$`` pairs, then checks
        whether any ``$`` characters remain.
        """
        # Remove block math $$...$$
        cleaned = re.sub(r"\$\$.+?\$\$", "", output)
        # Iteratively remove inline math $...$ pairs
        prev = None
        while prev != cleaned:
            prev = cleaned
            cleaned = re.sub(r"(?<!\$)\$(?!\$).+?(?<!\$)\$(?!\$)", "", cleaned)
        return "$" in cleaned

    @staticmethod
    async def _run_and_analyze(tmp_path: PathLike[str]) -> str:
        """Run the Fourier transform pipeline and return the output."""
        tmp = Path(tmp_path)
        isolated_lang = tmp / "general" / "eng"
        await isolated_lang.mkdir(parents=True)

        shared_name_map = _load_snapshot_names_map()
        aux_path = (
            _SNAPSHOT_DIR / f"{TestInlineMathIndependence._SNAPSHOT_NAME}.aux.json"
        )
        aux = json.loads(aux_path.read_text(encoding="UTF-8"))

        input_path = (
            _SNAPSHOT_DIR / f"{TestInlineMathIndependence._SNAPSHOT_NAME}.input.html"
        )
        html_text = input_path.read_text(encoding="UTF-8")
        html = BeautifulSoup(html_text, "html.parser")

        redirect_map = {
            k: _RedirectInfo(to=v["to"], tofragment=v.get("tofragment", ""))
            for k, v in aux["redirect_cache"].items()
        }
        names_map = shared_name_map | aux["name_map_overrides"]

        output, _ = await run_pipeline(
            html,
            redirect_map=redirect_map,
            image_metadata=aux["image_metadata"],
            names_map=names_map,
            wiki_dir=tmp / "general",
            wiki_lang_dir=isolated_lang,
            refs=True,
        )
        return output

    @pytest.mark.anyio
    async def test_inline_math_count(self, tmp_path: PathLike[str]) -> None:
        """The Fourier transform article should have 381 inline math blocks."""
        output = await self._run_and_analyze(tmp_path)
        count = self._count_inline_math_blocks(output)
        assert count == 381, f"Expected 381 inline math blocks, got {count}"

    @pytest.mark.anyio
    async def test_no_orphaned_dollar_signs(self, tmp_path: PathLike[str]) -> None:
        """Every ``$`` in the output should be part of a valid math delimiter pair."""
        output = await self._run_and_analyze(tmp_path)
        assert not self._has_orphaned_dollar_signs(output), (
            "Output contains $ signs not paired as $$...$$ or $...$"
        )

    @pytest.mark.anyio
    async def test_inline_math_count_block_math_fixture(
        self,
        tmp_path: PathLike[str],
    ) -> None:
        """The block math paragraph fixture should have 0 inline math blocks."""
        tmp = Path(tmp_path)
        isolated_lang = tmp / "general" / "eng"
        await isolated_lang.mkdir(parents=True)

        converter = TestBlockMathParagraphAffiliation._make_converter(tmp_path)
        html = BeautifulSoup(
            "<p>before "
            + TestBlockMathParagraphAffiliation._block_math_span(
                r"{\displaystyle f(x)}"
            )
            + " after</p>",
            "html.parser",
        )
        output = await converter.convert(
            html, out_to_archive=set(), redirect_map={}, refs=True
        )
        count = self._count_inline_math_blocks(output)
        assert count == 0, f"Expected 0 inline math blocks, got {count}"


class TestPipeInMathTableIntegration:
    """End-to-end: ``|`` inside a math element in an HTML table cell is
    converted to ``\\vert`` in the pipeline output.
    """

    @pytest.mark.anyio
    async def test_pipe_in_math_table_integration(
        self, tmp_path: PathLike[str]
    ) -> None:
        """End-to-end: HTML table cell with ``|`` in math → Markdown with ``\\vert``."""
        tmp = Path(tmp_path)
        isolated_lang = tmp / "general" / "eng"
        await isolated_lang.mkdir(parents=True)

        converter = WikiHtmlConverter(
            converted_wiki_dir=tmp / "general",
            converted_wiki_lang_dir=isolated_lang,
        )

        html_text = (
            "<table><tbody><tr><td>text "
            '<span class="mwe-math-element mwe-math-element-block">'
            '<span class="mwe-math-mathml-display mwe-math-mathml-a11y">'
            '<math display="block" alttext="{\\displaystyle x|y}">'
            "<semantics><mrow><mi>x</mi><mo>|</mo><mi>y</mi></mrow></semantics></math>"
            '<img class="mwe-math-fallback-image-display mw-invert skin-invert"/>'
            "</span></span>"
            " more</td></tr></tbody></table>"
        )
        html = BeautifulSoup(html_text, "html.parser")
        for st in html.find_all("style"):
            st.decompose()

        output = await converter.convert(
            html, out_to_archive=set(), redirect_map={}, refs=True
        )
        assert r"$$x\vert y$$" in output, f"Expected \\vert in output, got: {output!r}"
        # Also verify no bare | inside math blocks in output
        assert "$$x|y$$" not in output, "Bare pipe inside math should be replaced"


class TestTexHtmlToLatexRadical:
    """Regression tests for radical detection in sfrac → ``\\frac{}`` conversion.

    See ``_replace_sfrac_with_math`` which must use
    ``_texhtml_to_latex_sfrac`` (``\\frac``) instead of
    ``_texhtml_to_latex_sfrac_inline`` (slash division) for ``sfrac``
    elements containing radicals.  Wikipedia's ``{{sfrac}}`` always renders
    a horizontal-bar fraction.
    """

    @pytest.mark.anyio
    async def test_simple_sqrt(self, tmp_path: PathLike[str]) -> None:
        """``√2`` → ``\\sqrt{2}``."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = TestBlockMathParagraphAffiliation._make_converter(tmp_path)
        html = BeautifulSoup(
            '<span class="nowrap">'
            '<span typeof="mw:Entity">√</span>'
            '<span style="border-top: 1px solid">2</span>'
            "</span>",
            "html.parser",
        )
        assert html.span is not None
        result = converter._texhtml_to_latex(html.span)
        assert result == r"\sqrt{2}", f"Expected \\sqrt{{2}}, got {result!r}"

    @pytest.mark.anyio
    async def test_sqrt_with_greek(self, tmp_path: PathLike[str]) -> None:
        """``√σ`` → ``\\sqrt{\\sigma}`` (Greek letter in radicand)."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = TestBlockMathParagraphAffiliation._make_converter(tmp_path)
        html = BeautifulSoup(
            '<span class="nowrap">'
            '<span typeof="mw:Entity">√</span>'
            '<span style="border-top: 1px solid"><i>σ</i></span>'
            "</span>",
            "html.parser",
        )
        assert html.span is not None
        result = converter._texhtml_to_latex(html.span)
        assert result == r"\sqrt{{\sigma}}", (
            f"Expected \\sqrt{{\\sigma{{}}}}, got {result!r}"
        )

    @pytest.mark.anyio
    async def test_radical_with_index(self, tmp_path: PathLike[str]) -> None:
        """``⁴√2`` → ``\\sqrt[4]{2}`` (radical with index)."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = TestBlockMathParagraphAffiliation._make_converter(tmp_path)
        html = BeautifulSoup(
            '<span class="nowrap">'
            "<sup>4</sup>"
            '<span typeof="mw:Entity">√</span>'
            '<span style="border-top: 1px solid">2</span>'
            "</span>",
            "html.parser",
        )
        assert html.span is not None
        result = converter._texhtml_to_latex(html.span)
        assert result == r"\sqrt[4]{2}", f"Expected \\sqrt[4]{{2}}, got {result!r}"

    @pytest.mark.anyio
    async def test_sfrac_with_radical(self, tmp_path: PathLike[str]) -> None:
        """``sfrac`` with radicals → ``\\frac{\\sqrt[4]{2}}{\\sqrt{\\sigma}}``."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = TestBlockMathParagraphAffiliation._make_converter(tmp_path)
        html = BeautifulSoup(
            '<span class="sfrac"><span class="tion">'
            '<span class="num" style="border-bottom:1px solid">'
            '<span class="nowrap">'
            "<sup>4</sup>"
            '<span typeof="mw:Entity">√</span>'
            '<span style="border-top:1px solid;padding:0 0.1em">2</span>'
            "</span></span>"
            '<span class="sr-only">/</span>'
            '<span class="den" style="line-height:1.5em">'
            '<span class="nowrap">'
            '<span typeof="mw:Entity">√</span>'
            '<span style="border-top:1px solid;padding:0 0.1em"><i>σ</i></span>'
            "</span></span></span></span>",
            "html.parser",
        )
        assert html.span is not None
        result = converter._texhtml_to_latex_sfrac(html.span)
        assert result == r"\frac{\sqrt[4]{2}}{\sqrt{{\sigma}}}", (
            f"Expected \\frac{{\\sqrt[4]{{2}}}}{{\\sqrt{{\\sigma{{}}}}}}, got {result!r}"
        )

    @pytest.mark.anyio
    async def test_sfrac_radical_end_to_end(self, tmp_path: PathLike[str]) -> None:
        """Full pipeline: texhtml span with sfrac/radical → inline math."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        await lang_dir.mkdir(parents=True)
        converter = TestBlockMathParagraphAffiliation._make_converter(tmp_path)
        html_content = (
            "<p>"
            '<span class="texhtml">'
            '<span class="sfrac"><span class="tion">'
            '<span class="num" style="border-bottom:1px solid">'
            '<span class="nowrap">'
            "<sup>4</sup>"
            '<span typeof="mw:Entity">√</span>'
            '<span style="border-top:1px solid;padding:0 0.1em">2</span>'
            "</span></span>"
            '<span class="sr-only">/</span>'
            '<span class="den" style="line-height:1.5em">'
            '<span class="nowrap">'
            '<span typeof="mw:Entity">√</span>'
            '<span style="border-top:1px solid;padding:0 0.1em"><i>σ</i></span>'
            "</span></span></span></span>"
            "</span></p>"
        )
        html = BeautifulSoup(html_content, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), redirect_map={}, refs=True
        )
        assert r"\frac{\sqrt[4]{2} }{\sqrt{ {\sigma} } }" in result, (
            f"Expected \\frac in output, got: {result!r}"
        )


class TestFilterTableCells:
    """Unit tests for ``TableConverter._filter_table_cells``.

    Ensures that cell strings are correctly split, padded, and
    re-joined without dropping empty cells.
    """

    @pytest.mark.parametrize(
        ("input_str", "total_colspan", "expected"),
        [
            # No padding needed (3 cells, colspan 3)
            ("a | b | c", 3, "a | b | c"),
            # Fewer cells than colspan — pad with empties
            ("a | b", 3, "a | b | "),
            # Single cell, padded
            ("a", 3, "a |  | "),
            # Leading empty cell (the Fourier bug fix)
            (" | a | b", 3, " | a | b"),
            # All empty cells preserved
            (" |  | ", 3, " |  | "),
            # Empty string → all empty
            ("", 3, " |  | "),
            # colspan 1
            ("x", 1, "x"),
            # colspan 0 — empty string
            ("", 0, ""),
            # Trailing empty preserved
            ("a |  | ", 3, "a |  | "),
        ],
    )
    def test_filter_cells(
        self, input_str: str, total_colspan: int, expected: str
    ) -> None:
        """Filter cells according to the parametrized case."""
        result = TableConverter._filter_table_cells(
            input_str, total_colspan=total_colspan
        )
        assert result == expected, (
            f"Input {input_str!r} with colspan={total_colspan}: "
            f"expected {expected!r}, got {result!r}"
        )
