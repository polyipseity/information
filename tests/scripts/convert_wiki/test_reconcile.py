"""Tests for scripts/convert_wiki/reconcile.py.

These tests cover the redirect symlink reconciliation engine.  The live
API probe (``_fetch_redirect_status``) is stubbed; only the scan, decision,
symlink mutation, and cache-update logic is exercised.
"""

import json
from os import PathLike
from typing import cast

import pytest
from aiohttp import ClientSession
from anyio import Path as AnyioPath

from scripts.convert_wiki import reconcile as _mod
from scripts.convert_wiki.types import _RedirectStatus

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class _MockSession:
    """Stub aiohttp ClientSession (unused; the probe is patched)."""


def _stub_probe(
    monkeypatch: pytest.MonkeyPatch, statuses: dict[str, _RedirectStatus]
) -> None:
    """Replace the live API probe with a fixed status mapping."""

    async def fake_fetch(
        session: ClientSession, titles: list[str]
    ) -> dict[str, _RedirectStatus]:
        """Return the stubbed status for every requested title."""
        return {
            title: statuses.get(title, _RedirectStatus(to=title, missing=True))
            for title in titles
        }

    monkeypatch.setattr(_mod, "_fetch_redirect_status", fake_fetch)


class TestReconcile:
    """Tests for reconcile_redirect_symlinks."""

    @pytest.mark.anyio
    async def test_retargets_stale_redirect(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should retarget a symlink whose redirect target changed."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("old target.md", target_is_directory=False)
        mirror = wiki_dir / "from page.md"
        await mirror.symlink_to("eng/from page.md", target_is_directory=False)
        cache_path = wiki_dir / "cache.json"
        _stub_probe(monkeypatch, {"from page": _RedirectStatus(to="New target")})

        report = await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
        )

        assert str(await lang_link.readlink()) == "new target.md"
        assert await mirror.is_symlink()
        assert report.retargeted == 1
        assert report.removed == 0
        assert report.changed == ("from page",)

    @pytest.mark.anyio
    async def test_removes_redirect_when_article(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should remove symlinks when the title became a full article."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("old target.md", target_is_directory=False)
        mirror = wiki_dir / "from page.md"
        await mirror.symlink_to("eng/from page.md", target_is_directory=False)
        cache_path = wiki_dir / "cache.json"
        _stub_probe(monkeypatch, {"from page": _RedirectStatus(to="from page")})

        report = await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
        )

        assert not await lang_link.exists()
        assert not await mirror.exists()
        assert report.removed == 1
        assert report.retargeted == 0
        assert report.changed == ("from page",)

    @pytest.mark.anyio
    async def test_keeps_missing_page(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should keep a symlink when the page is missing."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("target.md", target_is_directory=False)
        cache_path = wiki_dir / "cache.json"
        _stub_probe(
            monkeypatch,
            {"from page": _RedirectStatus(to="from page", missing=True)},
        )

        report = await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
        )

        assert await lang_link.is_symlink()
        assert str(await lang_link.readlink()) == "target.md"
        assert report.kept == 1
        assert report.changed == ()

    @pytest.mark.anyio
    async def test_keeps_unchanged_redirect(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should leave a symlink with the correct target untouched."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("time series.md", target_is_directory=False)
        cache_path = wiki_dir / "cache.json"
        _stub_probe(monkeypatch, {"from page": _RedirectStatus(to="Time series")})

        report = await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
        )

        assert str(await lang_link.readlink()) == "time series.md"
        assert report.kept == 1
        assert report.changed == ()

    @pytest.mark.anyio
    async def test_real_file_not_scanned(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should ignore real files; only symlinks are scanned."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        real_file = lang_dir / "from page.md"
        await real_file.write_text("precious content")
        cache_path = wiki_dir / "cache.json"
        _stub_probe(monkeypatch, {})

        report = await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
        )

        assert await real_file.read_text() == "precious content"
        assert report.scanned == 0

    @pytest.mark.anyio
    async def test_chain_prefers_final_when_first_hop_absent(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should retarget to the final target when the first hop is absent."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("middle.md", target_is_directory=False)
        # First hop absent locally; final target present.
        await (lang_dir / "end.md").write_text("final article")
        cache_path = wiki_dir / "cache.json"
        _stub_probe(
            monkeypatch,
            {"from page": _RedirectStatus(to="Middle", final_to="End")},
        )

        report = await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
        )

        assert str(await lang_link.readlink()) == "end.md"
        assert report.retargeted == 1
        assert report.changed == ("from page",)

    @pytest.mark.anyio
    async def test_chain_uses_first_hop_when_present(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should retarget to the first hop when it is ingested locally."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("old target.md", target_is_directory=False)
        await (lang_dir / "middle.md").write_text("intermediate article")
        await (lang_dir / "end.md").write_text("final article")
        cache_path = wiki_dir / "cache.json"
        _stub_probe(
            monkeypatch,
            {"from page": _RedirectStatus(to="Middle", final_to="End")},
        )

        report = await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
        )

        assert str(await lang_link.readlink()) == "middle.md"
        assert report.retargeted == 1
        assert report.changed == ("from page",)

    @pytest.mark.anyio
    async def test_cache_written_with_status(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should write fresh cache entries for every scanned title."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("target.md", target_is_directory=False)
        cache_path = wiki_dir / "cache.json"
        _stub_probe(
            monkeypatch,
            {"from page": _RedirectStatus(to="New target", tofragment="sec")},
        )

        await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
        )

        with open(cache_path, "r", encoding="UTF-8") as f:  # noqa: ASYNC230
            data = json.load(f)
        assert data["from page"]["to"] == "New target"
        assert data["from page"]["tofragment"] == "sec"
        assert data["from page"]["cached_at"]

    @pytest.mark.anyio
    async def test_missing_writes_self_cache_entry(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should record missing pages as self-maps in the cache."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        await (lang_dir / "from page.md").symlink_to(
            "target.md", target_is_directory=False
        )
        cache_path = wiki_dir / "cache.json"
        _stub_probe(
            monkeypatch,
            {"from page": _RedirectStatus(to="from page", missing=True)},
        )

        await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
        )

        with open(cache_path, "r", encoding="UTF-8") as f:  # noqa: ASYNC230
            data = json.load(f)
        assert data["from page"]["to"] == "from page"
        assert data["from page"]["cached_at"]

    @pytest.mark.anyio
    async def test_dry_run_changes_nothing(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should report actions without mutating symlinks or the cache."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("old target.md", target_is_directory=False)
        cache_path = wiki_dir / "cache.json"
        _stub_probe(monkeypatch, {"from page": _RedirectStatus(to="New target")})

        report = await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
            dry_run=True,
        )

        assert str(await lang_link.readlink()) == "old target.md"
        assert not await cache_path.exists()
        assert report.retargeted == 1
        assert report.changed == ("from page",)

    @pytest.mark.anyio
    async def test_multilang_scan(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should scan every language subdirectory."""
        wiki_dir = AnyioPath(tmp_path)
        eng_dir = wiki_dir / "eng"
        zho_dir = wiki_dir / "zho"
        await eng_dir.mkdir()
        await zho_dir.mkdir()
        eng_link = eng_dir / "from page.md"
        await eng_link.symlink_to("old target.md", target_is_directory=False)
        zho_link = zho_dir / "某页.md"
        await zho_link.symlink_to("旧目标.md", target_is_directory=False)
        cache_path = wiki_dir / "cache.json"
        _stub_probe(
            monkeypatch,
            {
                "from page": _RedirectStatus(to="New target"),
                "某页": _RedirectStatus(to="新目标"),
            },
        )

        report = await _mod.reconcile_redirect_symlinks(  # noqa: SLF001
            cast(ClientSession, _MockSession()),
            wiki_dir=wiki_dir,
            cache_path=cache_path,
        )

        assert str(await eng_link.readlink()) == "new target.md"
        assert str(await zho_link.readlink()) == "新目标.md"
        assert report.scanned == 2
        assert report.retargeted == 2
