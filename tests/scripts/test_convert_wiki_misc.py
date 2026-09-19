"""Tests for scripts/convert_wiki.py.

These tests cover the pure functions and module-level constants that are
testable without HTTP requests or clipboard access.
"""

import json
import os
import re
import subprocess
from collections.abc import Mapping
from os import PathLike
from pathlib import Path as PathlibPath

import json5
import pytest
from anyio import Path, run_process
from bs4 import BeautifulSoup, Tag

from scripts.convert_wiki import config
from scripts.convert_wiki.api import _collect_link_titles
from scripts.convert_wiki.converter import WikiHtmlConverter
from scripts.convert_wiki.pipeline import _preprocess_html, run_pipeline
from scripts.convert_wiki.table import TableConverter
from scripts.convert_wiki.types import _RedirectInfo
from scripts.convert_wiki.utils import (
    _fix_filename,
    _fix_name_maybe,
)

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


"""Absolute path to the snapshot test fixtures directory."""
_SNAPSHOT_DIR = (
    PathlibPath(__file__).resolve(strict=True).with_name("convert_wiki") / "snapshots"
)

"""Absolute path to the repository root (markdownlint invocation cwd)."""
_REPO_ROOT = PathlibPath(__file__).resolve(strict=True).parents[2]


def _load_snapshot_names_map() -> dict[str, str]:
    """Load the shared snapshot name map (symlink to production JSONC)."""
    path = _SNAPSHOT_DIR / "name_map.jsonc"
    with path.open(encoding="UTF-8") as names_map_file:
        return json5.load(names_map_file)


def _categorize_block_math_blocks(output: str) -> dict[str, int]:
    """Count block math paragraph affiliation categories in converter output."""
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
    """Assert generated ``output`` is markdownlint-clean."""
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


async def _assert_redirect_symlinks(
    *,
    tmp: Path,
    isolated_lang: Path,
    redirect_map: Mapping[str, _RedirectInfo],
    link_titles: set[str],
    names_map: Mapping[str, str],
) -> None:
    """Assert the converter created exactly the redirect symlinks the aux implies."""
    expected: dict[str, str] = {}
    for title, info in redirect_map.items():
        if title not in link_titles:
            continue
        if info.to == title and not info.tofragment:
            continue
        if any(
            info.to.startswith(prefix) for prefix in config._PRESERVED_PAGE_PREFIXES
        ):
            continue
        from_name = _fix_filename(
            _fix_name_maybe(title, replace_underscores=True, names_map=names_map)
        )
        to_name = _fix_filename(
            _fix_name_maybe(info.to, replace_underscores=True, names_map=names_map)
        )
        if from_name != to_name:
            expected[f"{from_name}.md"] = f"{to_name}.md"

    actual: dict[str, str] = {}
    async for entry in isolated_lang.iterdir():
        if await entry.is_symlink():
            actual[entry.name] = str(await entry.readlink())
    assert actual == expected

    mirror_dir = tmp / "general"
    mirrors: dict[str, str] = {}
    async for entry in mirror_dir.iterdir():
        if await entry.is_symlink():
            mirrors[entry.name] = str(await entry.readlink())
    assert set(mirrors) == set(expected)
    for name, target in mirrors.items():
        assert target == f"eng/{name}"


"""Fourier transform snapshot name used by TestBlockMathCategoryBreakdown
and TestInlineMathIndependence to read expected output directly."""
_FOURIER_SNAPSHOT_NAME = "Fourier transform"


def _discover_snapshot_cases() -> list[str]:
    """Return fast snapshot fixture names."""
    all_cases = sorted(
        f.stem.removesuffix(".input")
        for f in sorted(_SNAPSHOT_DIR.glob("*.input.html"))
    )
    slow = {
        "Fourier transform",
        "special relativity",
        "Lagrangian mechanics",
        "Hamiltonian mechanics",
        "moment of inertia",
        "wave\u2013particle duality",
        "Routhian mechanics",
    }
    return [c for c in all_cases if c not in slow]


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

        # Collect the anchors before conversion: ``run_pipeline`` mutates the tree.
        link_titles = _collect_link_titles(html)

        # Load pre-computed data from aux instead of hitting the live API.
        redirect_map = {
            k: _RedirectInfo(to=v["to"], tofragment=v.get("tofragment", ""))
            for k, v in aux["redirect_cache"].items()
        }

        # Build the name_map: start with the shared baseline, then apply
        # per-test overrides (for titles not in the global name_map).
        names_map = shared_name_map | aux["name_map_overrides"]

        # Derive page name from snapshot name for same-page link detection.
        page_name = name[0].upper() + name[1:] if name else name

        # run_pipeline handles all post-processing (nbsp→space, hair→&hairsp;, strip).
        output, _ = await run_pipeline(
            html,
            redirect_map=redirect_map,
            image_metadata=aux["image_metadata"],
            names_map=names_map,
            wiki_dir=tmp / "general",
            wiki_lang_dir=isolated_lang,
            refs=True,
            page_name=page_name,
        )

        assert output == expected
        await _assert_markdownlint_clean(output, tmp)
        await _assert_redirect_symlinks(
            tmp=tmp,
            isolated_lang=isolated_lang,
            redirect_map=redirect_map,
            link_titles=link_titles,
            names_map=names_map,
        )


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

    @pytest.mark.anyio
    async def test_preserves_space_between_adjacent_links(self) -> None:
        """A space between two adjacent links must survive whitespace collapsing.

        Regression: a whitespace-only text node between two ``<a>`` tags was
        collapsed to empty, merging the links (``[a](x)[b](y)``).  The space
        separates two distinct tokens and must be preserved.
        """
        soup = BeautifulSoup(
            '<div><a href="https://en.wikipedia.org/wiki/Natural_frequency" class="extiw">natural</a> '
            '<a href="https://en.wikipedia.org/wiki/Angular_frequency" class="extiw">frequency</a></div>',
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
            "[natural](https://en.wikipedia.org/wiki/Natural_frequency) [frequency](https://en.wikipedia.org/wiki/Angular_frequency)"
            in result
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

    def test_new_parsoid_inline_marker_on_outer_span_returns_true(self) -> None:
        """Newer Parsoid markup marks inline math on the outer wrapper span.

        The ``<math>`` parent span is a bare ``mwe-math-mathml-a11y``; only
        the outer ``mwe-math-element-inline`` carries the inline marker, so
        the classification must consult the wrapper as well.
        """
        html = BeautifulSoup(
            "<p>text "
            '<span class="mwe-math-element mwe-math-element-inline">'
            '<span class="mwe-math-mathml-a11y">'
            "<math></math></span></span></p>",
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert WikiHtmlConverter._is_inline_math(math_ele) is True

    def test_new_parsoid_block_marker_on_outer_span_returns_false(self) -> None:
        """Newer Parsoid markup marks block math on the outer wrapper span."""
        html = BeautifulSoup(
            "<p>text "
            '<span class="mwe-math-element mwe-math-element-block">'
            '<span class="mwe-math-mathml-a11y">'
            '<math display="block"></math></span></span></p>',
            "html.parser",
        )
        math_ele = html.find("math")
        assert isinstance(math_ele, Tag)
        assert WikiHtmlConverter._is_inline_math(math_ele) is False

    def test_bare_outer_span_keeps_inner_inline_marker(self) -> None:
        """A bare ``mwe-math-element`` wrapper must not demote inline math.

        Some Parsoid revisions omit the inline/block modifier on the outer
        span while keeping ``mwe-math-mathml-inline`` on the parent span.
        """
        html = BeautifulSoup(
            "<p>text "
            '<span class="mwe-math-element">'
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
        # sfrac replacement happens in _preprocess_html, not in the converter.
        _preprocess_html(html)
        result = await converter.convert(
            html, out_to_archive=set(), redirect_map={}, refs=True
        )
        assert r"\frac{\sqrt[4]{2} }{\sqrt{ {\sigma} } }" in result, (
            f"Expected \\frac in output, got: {result!r}"
        )


class TestPreprocessMathA11y:
    """Tests for the ``_preprocess_html`` math a11y-span cleanup.

    Wikipedia emits the tail of some long equations as plain text after
    the MathML ``<math>`` element inside the a11y wrapper; the alttext
    already carries the full equation, so the tail must be dropped.
    """

    def test_drops_duplicate_latex_text(self) -> None:
        """Trailing LaTeX text and ``DisplaySpace`` are removed, math kept."""
        html = BeautifulSoup(
            '<p><span class="mwe-math-element mwe-math-element-display">'
            '<span class="mwe-math-mathml-display mwe-math-mathml-a11y">'
            '<math alttext="a=b"><semantics><mrow></mrow></semantics></math>'
            '<img class="mwe-math-fallback-image-display"/>'
            '<span typeof="mw:DisplaySpace">\u00a0</span>;\\quad x}</span>'
            "</span></p>",
            "html.parser",
        )
        _preprocess_html(html)
        a11y = html.find("span", class_="mwe-math-mathml-a11y")
        assert a11y is not None
        assert a11y.find("math") is not None
        assert a11y.find("img") is not None
        assert a11y.find("span", attrs={"typeof": "mw:DisplaySpace"}) is None
        assert "\\quad" not in a11y.get_text()


class TestPreprocessTemplateQuote:
    """Tests for the ``_preprocess_html`` templatequote attribution merge."""

    def test_moves_cite_inside_blockquote(self) -> None:
        """A following ``templatequotecite`` joins the preceding quote."""
        html = BeautifulSoup(
            '<blockquote class="templatequote"><p>Quoted text.</p></blockquote>'
            '<div class="templatequotecite">— Author</div>',
            "html.parser",
        )
        _preprocess_html(html)
        quote = html.find("blockquote")
        assert quote is not None
        assert quote.find("div", class_="templatequotecite") is not None
        assert quote.find_next_sibling() is None


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


@pytest.mark.anyio
async def test_inline_math_count_block_math_fixture(
    tmp_path: PathLike[str],
) -> None:
    """The block math paragraph fixture should have 0 inline math blocks."""
    tmp = Path(tmp_path)
    isolated_lang = tmp / "general" / "eng"
    await isolated_lang.mkdir(parents=True)

    converter = TestBlockMathParagraphAffiliation._make_converter(tmp_path)
    html = BeautifulSoup(
        "<p>before "
        + TestBlockMathParagraphAffiliation._block_math_span(r"{\displaystyle f(x)}")
        + " after</p>",
        "html.parser",
    )
    output = await converter.convert(
        html, out_to_archive=set(), redirect_map={}, refs=True
    )
    count = len(re.findall(r"(?<!\$)\$(?!\$).+?(?<!\$)\$(?!\$)", output))
    assert count == 0, f"Expected 0 inline math blocks, got {count}"
