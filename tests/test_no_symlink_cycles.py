"""Tests that no symlink tracked in the repository closes a cycle.

A self-referential link once reached CI and broke the checkout with ``ELOOP``,
where nothing inspects the index for cycles.  These tests scan the tracked
symlinks with the same detector the writer uses, so a loop is reported in the
test suite instead of during a checkout.
"""

import os
import subprocess
from os import PathLike

import pytest
from anyio import Path, run_process

from scripts.convert_wiki.utils import _symlink_would_loop  # noqa: SLF001

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

"""Index mode git records for a symbolic link."""
_SYMLINK_MODE = "120000"


async def _tracked_symlinks() -> list[Path]:
    """Return the symlinks recorded in the git index.

    Reading the index rather than walking the tree skips ignored directories
    such as ``node_modules/`` and ``.venv/``, and matches what CI checks out.
    """
    root = Path(__file__).parent.parent  # repo root
    proc = await run_process(
        ["git", "ls-files", "-s", "-z"],
        cwd=str(root),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    links: list[Path] = []
    for entry in proc.stdout.decode().split("\0"):
        if not entry:
            continue
        meta, _, name = entry.partition("\t")
        if meta.split()[0] == _SYMLINK_MODE:
            links.append(root / name)
    return links


@pytest.mark.anyio
async def test_detector_flags_a_self_loop(tmp_path: PathLike[str]) -> None:
    """The cycle detector reports a link that points at itself."""
    base = Path(os.fspath(tmp_path))
    loop = base / "loop.md"
    await loop.symlink_to("loop.md")

    assert await _symlink_would_loop(base, "loop.md", "loop.md") is True


@pytest.mark.anyio
async def test_detector_allows_a_forward_link(tmp_path: PathLike[str]) -> None:
    """The cycle detector accepts a link whose target is a real file."""
    base = Path(os.fspath(tmp_path))
    real = base / "real.md"
    await real.write_text("real\n")
    hop = base / "hop.md"
    await hop.symlink_to("real.md")

    assert await _symlink_would_loop(base, "hop.md", "real.md") is False


@pytest.mark.anyio
async def test_no_tracked_symlink_closes_a_cycle() -> None:
    """No tracked symlink resolves back into its own chain."""
    offenders: list[str] = []
    for path in await _tracked_symlinks():
        target = os.readlink(path)
        if await _symlink_would_loop(path.parent, path.name, target):
            offenders.append(str(path))
    assert offenders == [], f"tracked symlinks close a cycle: {offenders}"
