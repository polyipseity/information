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
from bs4 import BeautifulSoup

from scripts.convert_wiki import config
from scripts.convert_wiki.api import _collect_link_titles
from scripts.convert_wiki.pipeline import run_pipeline
from scripts.convert_wiki.table import _reformat_table
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
    """Assert generated ``output`` is markdownlint-clean.

    Applies the pipeline's table reflow first so callers may pass raw
    converter output; production output is already reflowed, making this a
    no-op for it.
    """
    out_path = tmp / "lint.md"
    config_path = tmp / ".markdownlint.jsonc"
    await out_path.write_text(_reformat_table(output), encoding="UTF-8")
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
    """Return slow snapshot fixture names."""
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
        "Schrödinger equation",
        "particle in a box",
        "quantum harmonic oscillator",
    }
    return [c for c in all_cases if c in slow]


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
        # The linter harness reflows tables; pipeline output must already be a
        # fixed point so that reflow cannot silently repair a malformed table.
        assert _reformat_table(output) == output
        await _assert_markdownlint_clean(output, tmp)
        await _assert_redirect_symlinks(
            tmp=tmp,
            isolated_lang=isolated_lang,
            redirect_map=redirect_map,
            link_titles=link_titles,
            names_map=names_map,
        )


class TestBlockMathCategoryBreakdown:
    """Verify block math paragraph affiliation category counts in a real article.

    Uses the "Fourier transform" snapshot fixture as a regression baseline
    for the distribution of BOTH, BEFORE_ONLY, AFTER_ONLY, and NEITHER
    categories.
    """

    _SNAPSHOT_NAME = "Fourier transform"

    @staticmethod
    def _get_expected_output() -> str:
        """Read the Fourier transform expected output (no pipeline needed)."""
        expected_path = _SNAPSHOT_DIR / f"{_FOURIER_SNAPSHOT_NAME}.expected.md"
        return expected_path.read_text(encoding="UTF-8").lstrip()

    @staticmethod
    def _run_and_categorize() -> dict[str, int]:
        """Categorize block math in the Fourier transform expected output."""
        return _categorize_block_math_blocks(
            TestBlockMathCategoryBreakdown._get_expected_output()
        )

    @staticmethod
    def _assert_counts(counts: dict[str, int], **expected: int) -> None:
        """Assert that *counts* match all specified *expected* categories."""
        for category, expected_value in expected.items():
            actual = counts.get(category, 0)
            assert actual == expected_value, (
                f"Category {category!r}: expected {expected_value}, got {actual}"
            )

    def test_category_counts(self) -> None:
        """All four categories should have nonzero counts."""
        counts = self._run_and_categorize()
        for category in ("both", "before_only", "after_only", "neither"):
            assert counts.get(category, 0) > 0, (
                f"Category {category!r}: expected > 0, got {counts.get(category, 0)}"
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
    def _get_expected_output() -> str:
        """Read the Fourier transform expected output (no pipeline needed)."""
        expected_path = _SNAPSHOT_DIR / f"{_FOURIER_SNAPSHOT_NAME}.expected.md"
        return expected_path.read_text(encoding="UTF-8").lstrip()

    def test_inline_math_count(self) -> None:
        """The Fourier transform article should have nonzero inline math blocks."""
        output = self._get_expected_output()
        count = self._count_inline_math_blocks(output)
        assert count > 0, f"Expected > 0 inline math blocks, got {count}"

    def test_no_orphaned_dollar_signs(self) -> None:
        """Every ``$`` in the output should be part of a valid math delimiter pair."""
        output = self._get_expected_output()
        assert not self._has_orphaned_dollar_signs(output), (
            "Output contains $ signs not paired as $$...$$ or $...$"
        )
