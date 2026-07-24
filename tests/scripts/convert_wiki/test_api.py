"""Tests for scripts/convert_wiki/api.py.

These tests cover the API request, redirect resolution, and cache functions.
"""

import json
from dataclasses import replace
from datetime import datetime, timedelta, timezone
from os import PathLike
from pathlib import Path as PathlibPath
from typing import cast

import anyio
import pytest
from aiohttp import ClientSession
from anyio import Path
from bs4 import BeautifulSoup

from scripts.convert_wiki import api as _mod
from scripts.convert_wiki import config
from scripts.convert_wiki.config import _CACHE_TTL
from scripts.convert_wiki.types import _RedirectInfo

_SNAPSHOT_DIR = PathlibPath(__file__).resolve(strict=True).parent / "snapshots"

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestCollectLinkTitles:
    """Tests for _collect_link_titles function."""

    def test_collects_titles(self) -> None:
        """Should collect titles from <a> tags with title attributes."""

        html = BeautifulSoup(
            '<a title="Main Page" href="/wiki/Main_Page">Main</a>'
            '<a title="Python" href="/wiki/Python">Python</a>',
            "html.parser",
        )
        titles = _mod._collect_link_titles(html)  # noqa: SLF001
        assert "Main Page" in titles
        assert "Python" in titles

    def test_skips_selflink_class(self) -> None:
        """Should skip links with mw-selflink class."""

        html = BeautifulSoup(
            '<a class="mw-selflink" title="Same Page" href="/wiki/Same">Same</a>',
            "html.parser",
        )
        titles = _mod._collect_link_titles(html)  # noqa: SLF001
        assert "Same Page" not in titles

    def test_skips_file_description(self) -> None:
        """Should skip links with mw-file-description class."""

        html = BeautifulSoup(
            '<a class="mw-file-description" title="File:Example.jpg" href="..."></a>',
            "html.parser",
        )
        titles = _mod._collect_link_titles(html)  # noqa: SLF001
        assert "File:Example.jpg" not in titles

    def test_skips_extiw(self) -> None:
        """Should skip interwiki links (extiw class)."""

        html = BeautifulSoup(
            '<a class="extiw" title="fr:Bonjour" href="...">Bonjour</a>',
            "html.parser",
        )
        titles = _mod._collect_link_titles(html)  # noqa: SLF001
        assert "fr:Bonjour" not in titles

    def test_skips_new_pages(self) -> None:
        """Should skip links with 'new' class (non-existent pages)."""

        html = BeautifulSoup(
            '<a class="new" title="NonExistent" href="...">missing</a>',
            "html.parser",
        )
        titles = _mod._collect_link_titles(html)  # noqa: SLF001
        assert "NonExistent" not in titles

    def test_skips_no_title(self) -> None:
        """Should skip <a> tags without title attribute."""

        html = BeautifulSoup(
            '<a href="/wiki/Page">Page</a>',
            "html.parser",
        )
        titles = _mod._collect_link_titles(html)  # noqa: SLF001
        assert len(titles) == 0

    def test_returns_set(self) -> None:
        """Should return a set (no duplicates)."""

        html = BeautifulSoup(
            '<a title="Page" href="/wiki/Page">P1</a>'
            '<a title="Page" href="/wiki/Page">P2</a>',
            "html.parser",
        )
        titles = _mod._collect_link_titles(html)  # noqa: SLF001
        assert len(titles) == 1


class TestRedirectCache:
    """Tests for _load_redirect_cache and _save_redirect_cache."""

    @pytest.mark.anyio
    async def test_save_and_load(self, tmp_path: PathLike[str]) -> None:
        """Should round-trip cache data through JSON."""
        path = Path(tmp_path) / "redirect_cache.json"
        cache = {
            "A": _RedirectInfo(to="B", tofragment=""),  # noqa: SLF001
            "C": _RedirectInfo(to="D", tofragment="s"),  # noqa: SLF001
            "E": _RedirectInfo(to="E"),  # noqa: SLF001  # non-redirect
        }
        await _mod._save_redirect_cache(cache, cache_path=path)  # noqa: SLF001
        loaded = _mod._load_redirect_cache(cache_path=path)  # noqa: SLF001
        assert len(loaded) == 3
        assert loaded["A"].to == "B"
        assert loaded["A"].tofragment == ""
        assert loaded["C"].tofragment == "s"
        assert loaded["E"].to == "E"
        # cached_at should be set on round-trip
        assert isinstance(loaded["A"].cached_at, str) and loaded["A"].cached_at

    def test_load_missing_file(self, tmp_path: PathLike[str]) -> None:
        """Should return empty dict when cache file does not exist."""
        path = Path(tmp_path) / "nonexistent.json"
        loaded = _mod._load_redirect_cache(cache_path=path)  # noqa: SLF001
        assert loaded == {}

    @pytest.mark.anyio
    async def test_load_corrupted_file(self, tmp_path: PathLike[str]) -> None:
        """Should return empty dict when cache file is corrupted."""
        path = Path(tmp_path) / "corrupt.json"
        await path.write_text("{bad json}", encoding="UTF-8")
        loaded = _mod._load_redirect_cache(cache_path=path)  # noqa: SLF001
        assert loaded == {}

    @pytest.mark.anyio
    async def test_load_expired_ttl(
        self, tmp_path: PathLike[str], monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should skip entries with expired cached_at."""

        path = Path(tmp_path) / "old_entries.json"
        old_ts = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
        await path.write_text(
            json.dumps({"X": {"to": "Y", "tofragment": "", "cached_at": old_ts}}),
            encoding="UTF-8",
        )
        monkeypatch.setattr(config, "_CACHE_TTL", timedelta(days=1))
        loaded = _mod._load_redirect_cache(cache_path=path)  # noqa: SLF001
        assert loaded == {}

    @pytest.mark.anyio
    async def test_old_format_missing_cached_at_stamped(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should stamp non-empty cached_at for entries without the field."""

        path = Path(tmp_path) / "old_format.json"
        await path.write_text(
            json.dumps({"X": {"to": "Y", "tofragment": ""}}),
            encoding="UTF-8",
        )
        loaded = _mod._load_redirect_cache(cache_path=path)  # noqa: SLF001
        assert len(loaded) == 1
        assert loaded["X"].cached_at  # non-empty string

    @pytest.mark.anyio
    async def test_malformed_cached_at_skipped(self, tmp_path: PathLike[str]) -> None:
        """Should skip entries with malformed cached_at."""

        path = Path(tmp_path) / "malformed.json"
        await path.write_text(
            json.dumps(
                {"X": {"to": "Y", "tofragment": "", "cached_at": "not-a-timestamp"}}
            ),
            encoding="UTF-8",
        )
        loaded = _mod._load_redirect_cache(cache_path=path)  # noqa: SLF001
        assert loaded == {}

    def test_default_ttl_is_one_day(self) -> None:
        """Default cache TTL should be exactly 1 day."""
        assert _CACHE_TTL == timedelta(days=1)  # noqa: SLF001


class TestApiRequest:
    """Tests for _api_request function."""

    def test_returns_json_on_200(self) -> None:
        """Should return parsed JSON on HTTP 200."""

        async def run() -> None:
            """Run the async test body."""

            class MockResponse:
                """Mock aiohttp response returning fixed JSON."""

                status = 200

                async def json(self):
                    """Return fixed JSON data."""
                    return {"key": "value"}

                async def __aenter__(self):
                    """Return self as context manager."""
                    return self

                async def __aexit__(self, *args):
                    """No-op cleanup."""
                    pass

            class MockGet:
                """Mock aiohttp get callable."""

                def __call__(self, url):
                    """Return a mock response."""
                    return MockResponse()

            class MockSession:
                """Mock aiohttp ClientSession."""

                get = MockGet()

            result = await _mod._api_request(  # noqa: SLF001
                cast(ClientSession, MockSession()),
                {"action": "query"},
            )
            assert result == {"key": "value"}

        anyio.run(run, backend="asyncio")

    def test_retries_on_429(self) -> None:
        """Should retry after 429 and eventually succeed."""

        async def run() -> None:
            """Run the async test body."""
            call_count = 0

            class MockResponse:
                """Mock aiohttp response with configurable status."""

                def __init__(self, status, retry_after=None):
                    """Store status and optional retry-after."""
                    self.status = status
                    self._retry_after = retry_after

                @property
                def headers(self):
                    """Return retry-after header if set."""
                    if self._retry_after:
                        return {"Retry-After": self._retry_after}
                    return {}

                async def json(self):
                    """Return fixed JSON data."""
                    return {"key": "value"}

                async def __aenter__(self):
                    """Return self as context manager."""
                    return self

                async def __aexit__(self, *args):
                    """Increment call count on exit."""
                    nonlocal call_count
                    call_count += 1

            class MockGet:
                """Mock aiohttp get callable."""

                def __call__(self, url):
                    """Return 429 for first calls, then 200."""
                    if call_count < 2:
                        return MockResponse(429)
                    return MockResponse(200)

            class MockSession:
                """Mock aiohttp ClientSession."""

                get = MockGet()

            result = await _mod._api_request(  # noqa: SLF001
                cast(ClientSession, MockSession()),
                {"action": "query"},
            )
            assert result == {"key": "value"}
            assert call_count >= 3  # first two attempts fail, third succeeds

        anyio.run(run, backend="asyncio")


class TestResolveRedirects:
    """Tests for _resolve_redirects function."""

    def test_all_cached(self) -> None:
        """Should skip API call when all titles are already in cache."""

        async def run() -> None:
            """Run the async test body."""
            cache = {
                "Page A": _RedirectInfo(to="Page A"),  # noqa: SLF001
                "Page B": _RedirectInfo(to="Page B"),  # noqa: SLF001
            }
            titles = {"Page A", "Page B"}

            class MockSession:
                """Mock aiohttp ClientSession."""

                def get(self, url):
                    """Assert no API call is made (all cached)."""
                    msg = "API call should not be made"
                    raise RuntimeError(msg)

            result = await _mod._resolve_redirects(  # noqa: SLF001
                cast(ClientSession, MockSession()),
                titles,
                cache,
                cache_path=PathlibPath("/tmp/unused.json"),
            )
            assert result["Page A"].to == "Page A"
            assert result["Page B"].to == "Page B"
            assert len(result) == 2

        anyio.run(run, backend="asyncio")

    def test_resolves_redirect(self, tmp_path: PathLike[str]) -> None:
        """Should resolve redirect via API and cache the result."""

        cache_path = Path(tmp_path) / "redirect_cache.json"

        async def run() -> None:
            """Run the async test body."""
            cache: dict[str, _RedirectInfo] = {}  # noqa: SLF001
            titles = {"Redirect to Page"}

            class MockResponse:
                """Mock aiohttp response returning redirect JSON."""

                status = 200

                async def json(self):
                    """Return redirect API response."""
                    return {
                        "query": {
                            "redirects": [
                                {
                                    "from": "Redirect to Page",
                                    "to": "Actual Page",
                                    "tofragment": "",
                                }
                            ],
                            "pages": [{"pageid": 1, "ns": 0, "title": "Actual Page"}],
                        }
                    }

                async def __aenter__(self):
                    """Return self as context manager."""
                    return self

                async def __aexit__(self, *args):
                    """No-op cleanup."""
                    pass

            class MockGet:
                """Mock aiohttp get callable."""

                def __call__(self, url):
                    """Return a mock response."""
                    return MockResponse()

            class MockSession:
                """Mock aiohttp ClientSession."""

                get = MockGet()

            result = await _mod._resolve_redirects(  # noqa: SLF001
                cast(ClientSession, MockSession()),
                titles,
                cache,
                cache_path=cache_path,
            )
            assert result["Redirect to Page"].to == "Actual Page"

        anyio.run(run, backend="asyncio")

    def test_redirect_with_fragment(self, tmp_path: PathLike[str]) -> None:
        """Should preserve tofragment from API response."""

        cache_path = Path(tmp_path) / "redirect_cache.json"

        async def run() -> None:
            """Run the async test body."""
            cache: dict[str, _RedirectInfo] = {}  # noqa: SLF001
            titles = {"Dest with Anchor"}

            class MockResponse:
                """Mock aiohttp response returning fragment redirect JSON."""

                status = 200

                async def json(self):
                    """Return redirect API response with fragment."""
                    return {
                        "query": {
                            "redirects": [
                                {
                                    "from": "Dest with Anchor",
                                    "to": "Destination",
                                    "tofragment": "section",
                                }
                            ],
                            "pages": [{"pageid": 1, "ns": 0, "title": "Destination"}],
                        }
                    }

                async def __aenter__(self):
                    """Return self as context manager."""
                    return self

                async def __aexit__(self, *args):
                    """No-op cleanup."""
                    pass

            class MockGet:
                """Mock aiohttp get callable."""

                def __call__(self, url):
                    """Return a mock response."""
                    return MockResponse()

            class MockSession:
                """Mock aiohttp ClientSession."""

                get = MockGet()

            result = await _mod._resolve_redirects(  # noqa: SLF001
                cast(ClientSession, MockSession()),
                titles,
                cache,
                cache_path=cache_path,
            )
            assert result["Dest with Anchor"].tofragment == "section"

        anyio.run(run, backend="asyncio")

    def test_non_redirect_resolved_to_self(self, tmp_path: PathLike[str]) -> None:
        """Should map non-redirect pages to themselves in cache."""

        cache_path = Path(tmp_path) / "redirect_cache.json"

        async def run() -> None:
            """Run the async test body."""
            cache: dict[str, _RedirectInfo] = {}  # noqa: SLF001
            titles = {"Normal Page"}

            class MockResponse:
                """Mock aiohttp response returning self-redirect JSON."""

                status = 200

                async def json(self):
                    """Return API response with no redirects."""
                    return {
                        "query": {
                            "redirects": [],
                            "pages": [{"pageid": 10, "ns": 0, "title": "Normal Page"}],
                        }
                    }

                async def __aenter__(self):
                    """Return self as context manager."""
                    return self

                async def __aexit__(self, *args):
                    """No-op cleanup."""
                    pass

            class MockGet:
                """Mock aiohttp get callable."""

                def __call__(self, url):
                    """Return a mock response."""
                    return MockResponse()

            class MockSession:
                """Mock aiohttp ClientSession."""

                get = MockGet()

            result = await _mod._resolve_redirects(  # noqa: SLF001
                cast(ClientSession, MockSession()),
                titles,
                cache,
                cache_path=cache_path,
            )
            assert result["Normal Page"].to == "Normal Page"

        anyio.run(run, backend="asyncio")

    def test_expired_cache_triggers_redirect_resolution(
        self, tmp_path: PathLike[str], monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should re-fetch via API and rewrite cache when cache entries have
        expired."""

        path = Path(tmp_path) / "redirect_cache.json"
        monkeypatch.setattr(config, "_CACHE_TTL", timedelta(days=1))

        async def run() -> None:
            """Run the async test body."""
            # Pre-populate a stale cache file with expired entries on disk.
            old_ts = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
            stale_cache = {
                "Page X": _RedirectInfo(to="Page X", cached_at=old_ts),  # noqa: SLF001
                "Page Y": _RedirectInfo(to="Page Y", cached_at=old_ts),  # noqa: SLF001
            }
            await _mod._save_redirect_cache(stale_cache, cache_path=path)  # noqa: SLF001

            # Load cache — expired entries should be skipped.
            loaded = _mod._load_redirect_cache(cache_path=path)  # noqa: SLF001
            assert loaded == {}

            titles = {"Page X", "Page Z"}
            api_call_count = 0

            class MockResponse:
                """Mock aiohttp response with typed interface."""

                status = 200

                def __init__(self, data: dict[str, object]) -> None:
                    """Store response data."""
                    self._data = data

                @property
                def headers(self) -> dict[str, str]:
                    """Return empty headers."""
                    return {}

                async def json(self) -> dict[str, object]:
                    """Return stored response data."""
                    return self._data

                async def __aenter__(self) -> "MockResponse":
                    """Return self as context manager."""
                    return self

                async def __aexit__(self, *args: object) -> None:
                    """No-op cleanup."""
                    pass

            class MockGet:
                """Mock aiohttp get callable."""

                @staticmethod
                def __call__(url: object) -> MockResponse:
                    """Return mock response and increment call count."""
                    nonlocal api_call_count
                    api_call_count += 1
                    return MockResponse(
                        {
                            "query": {
                                "redirects": [],
                                "pages": [
                                    {"pageid": i + 1, "ns": 0, "title": t}
                                    for i, t in enumerate(sorted(titles))
                                ],
                            }
                        }
                    )

            class MockSession:
                """Mock aiohttp ClientSession."""

                get = MockGet()

            result = await _mod._resolve_redirects(  # noqa: SLF001
                cast(ClientSession, MockSession()),
                titles,
                loaded,
                cache_path=path,
            )
            assert api_call_count >= 1
            assert result["Page X"].to == "Page X"
            assert result["Page Z"].to == "Page Z"
            # Cache file should have been rewritten (fresh cached_at).
            reloaded = _mod._load_redirect_cache(cache_path=path)  # noqa: SLF001
            assert "Page X" in reloaded
            assert "Page Z" in reloaded

        anyio.run(run, backend="asyncio")


class TestResolveRedirectsWithRealResponses:
    """Parsing-correctness tests using real Wikipedia API responses.

    These tests verify that ``_resolve_redirects`` correctly parses the
    actual JSON shape returned by the Wikipedia API. The response data
    was captured live and stored alongside the input fixture so these
    tests remain offline.
    """

    @pytest.mark.anyio
    async def test_parses_modern_physics_api_response(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Feed the real modern physics API response through
        _resolve_redirects and verify the output matches the cache file."""

        cache_path = Path(tmp_path) / "redirect_cache.json"

        # Load the raw API responses from the consolidated aux fixture.
        aux_path = _SNAPSHOT_DIR / "modern physics.aux.json"
        aux = json.loads(aux_path.read_text(encoding="UTF-8"))
        raw_batches: list[dict[str, object]] = aux["api_responses"]

        # Build a mock session that returns each batch response in order.
        class MockResponse:
            """Mock aiohttp response with configurable data and status."""

            def __init__(self, data: dict[str, object], status: int = 200) -> None:
                """Store response data and status."""
                self.status = status
                self._data = data

            @property
            def headers(self) -> dict[str, str]:
                """Return empty headers."""
                return {}

            async def json(self) -> dict[str, object]:
                """Return stored response data."""
                return self._data

            async def __aenter__(self) -> "MockResponse":
                """Return self as context manager."""
                return self

            async def __aexit__(self, *args: object) -> None:
                """No-op cleanup."""
                pass

        call_index = 0
        total_calls = len(raw_batches)

        class MockGet:
            """Mock aiohttp get callable."""

            @staticmethod
            def __call__(url: object) -> MockResponse:
                """Return next batch response and advance index."""
                nonlocal call_index
                if call_index >= total_calls:
                    msg = f"Unexpected API call #{call_index} (expected {total_calls})"
                    raise RuntimeError(msg)
                resp = MockResponse(raw_batches[call_index])
                call_index += 1
                return resp

        class MockSession:
            """Mock aiohttp ClientSession."""

            get = MockGet()

        # Collect titles the same way the snapshot test does.
        html_path = _SNAPSHOT_DIR / "modern physics.input.html"
        html = BeautifulSoup(html_path.read_text(encoding="UTF-8"), "html.parser")
        titles = _mod._collect_link_titles(html)  # noqa: SLF001

        result = await _mod._resolve_redirects(  # noqa: SLF001
            cast(ClientSession, MockSession()),
            titles,
            {},
            cache_path=cache_path,
        )

        # Load the expected cache from the consolidated aux fixture.
        # Strips cached_at from both sides — snapshot data has old timestamps
        # and we don't want equality to depend on them.
        expected_raw = aux["redirect_cache"]

        assert len(result) == len(expected_raw)
        for title, info in expected_raw.items():
            assert title in result, f"Missing title: {title!r}"
            expected = _RedirectInfo(
                to=info["to"], tofragment=info.get("tofragment", "")
            )
            actual = replace(result[title], cached_at="")
            assert actual == expected, f"Mismatch for {title!r}"

        # All batches should have been consumed.
        assert call_index == total_calls
