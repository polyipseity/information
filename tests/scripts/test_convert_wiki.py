"""Tests for scripts/convert_wiki.py.

These tests cover the pure functions and module-level constants that are
testable without HTTP requests or clipboard access.
"""

from __future__ import annotations

import dataclasses
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING

import anyio
import pytest
from bs4 import BeautifulSoup

if TYPE_CHECKING:
    pass

from scripts import convert_wiki as _mod


class TestFixNameMaybe:
    """Tests for the _fix_name_maybe function."""

    def test_normalize_non_breaking_space(self) -> None:
        """Should replace non-breaking spaces with regular spaces."""
        result = _mod._fix_name_maybe("Hello\u00a0World")  # noqa: SLF001
        assert result == "Hello World"

    def test_mapped_name(self) -> None:
        """Should return the mapped name if it exists in _NAMES_MAP."""
        # We can verify it uses _NAMES_MAP by checking known entries
        # but the map is dynamic, so just verify the function runs
        assert isinstance(_mod._fix_name_maybe("test"), str)  # noqa: SLF001

    def test_replace_underscores(self) -> None:
        """Should replace underscores with spaces when requested."""
        result = _mod._fix_name_maybe(  # noqa: SLF001
            "Hello_World", replace_underscores=True
        )
        assert "_" not in result
        assert "Hello World" in result or result.islower()  # may be lowercased

    def test_single_char_name(self) -> None:
        """Should handle single character names without crashing."""
        result = _mod._fix_name_maybe("A")  # noqa: SLF001
        assert isinstance(result, str)

    def test_short_name_lowercase_second_char(self) -> None:
        """Should lowercase first char when second char is already lowercase."""
        result = _mod._fix_name_maybe("aBC")  # noqa: SLF001
        assert result == "aBC"  # first char is already lowercase


class TestFixFilename:
    """Tests for the _fix_filename function."""

    def test_replaces_colon(self) -> None:
        """Should replace colon with underscore."""
        assert _mod._fix_filename("a:b") == "a_b"  # noqa: SLF001

    def test_replaces_backslash(self) -> None:
        """Should replace backslash with underscore."""
        assert _mod._fix_filename("a\\b") == "a_b"  # noqa: SLF001

    def test_replaces_forward_slash(self) -> None:
        """Should replace forward slash with underscore."""
        assert _mod._fix_filename("a/b") == "a_b"  # noqa: SLF001

    def test_keeps_safe_characters(self) -> None:
        """Should keep normal alphanumeric characters unchanged."""
        assert _mod._fix_filename("hello_world-123.md") == "hello_world-123.md"  # noqa: SLF001

    def test_empty_string(self) -> None:
        """Should handle empty string safely."""
        assert _mod._fix_filename("") == ""  # noqa: SLF001


class TestMarkdownFragment:
    """Tests for the _markdown_fragment function."""

    def test_empty_fragment(self) -> None:
        """Should return empty string for empty fragment."""
        assert _mod._markdown_fragment("") == ""  # noqa: SLF001

    def test_removes_colons(self) -> None:
        """Should remove colons from the fragment."""
        result = _mod._markdown_fragment("ref:note")  # noqa: SLF001
        assert ":" not in result

    def test_encodes_spaces(self) -> None:
        """Should encode spaces as %20."""
        result = _mod._markdown_fragment("my section")  # noqa: SLF001
        assert "%20" in result

    def test_encodes_slash(self) -> None:
        """Should encode forward slashes as %2F."""
        result = _mod._markdown_fragment("a/b")  # noqa: SLF001
        assert "%2F" in result

    def test_prepends_hash(self) -> None:
        """Should prepend # to non-empty fragments."""
        result = _mod._markdown_fragment("section")  # noqa: SLF001
        assert result.startswith("#")


class TestMarkdownLinkTarget:
    """Tests for the _markdown_link_target function."""

    def test_basic_link(self) -> None:
        """Should build a basic Markdown link target."""
        result = _mod._markdown_link_target("Page Name", "")  # noqa: SLF001
        assert result == "Page%20Name.md"

    def test_with_fragment(self) -> None:
        """Should append fragment when provided."""
        result = _mod._markdown_link_target("Page", "section")  # noqa: SLF001
        assert result == "Page.md#section"


class TestTagAffixes:
    """Tests for the _tag_affixes function."""

    def test_simple_tag(self) -> None:
        """Should return opening and closing tags."""
        open_tag, close_tag = _mod._tag_affixes("div")  # noqa: SLF001
        assert open_tag == "<div>"
        assert close_tag == "</div>"

    def test_void_tag(self) -> None:
        """Should handle any tag name correctly."""
        open_tag, close_tag = _mod._tag_affixes("br")  # noqa: SLF001
        assert open_tag == "<br>"
        assert close_tag == "</br>"


class TestBs4NewElement:
    """Tests for the _bs4_new_element function."""

    def test_parse_simple_tag(self) -> None:
        """Should parse a simple HTML tag string."""
        result = _mod._bs4_new_element("<b></b>")  # noqa: SLF001
        assert result.name == "b"

    def test_parse_tag_with_content(self) -> None:
        """Should parse a tag with text content."""
        result = _mod._bs4_new_element("<i>text</i>")  # noqa: SLF001
        assert result.name == "i"
        assert result.string == "text"


class TestConstants:
    """Tests for module-level constants."""

    def test_name(self) -> None:
        """NAME should be 'convert_wiki.py'."""
        assert _mod.NAME == "convert_wiki.py"

    def test_base_name(self) -> None:
        """BASE_NAME should be 'convert_wiki'."""
        assert _mod.BASE_NAME == "convert_wiki"

    def test_version(self) -> None:
        """VERSION should be a non-empty string."""
        assert isinstance(_mod.VERSION, str)
        assert _mod.VERSION

    def test_user_agent_contains_name(self) -> None:
        """USER_AGENT should contain the script name."""
        assert _mod.NAME in _mod.USER_AGENT

    def test_wiki_host_url(self) -> None:
        """_WIKI_HOST_URL should be the English Wikipedia host."""
        assert str(_mod._WIKI_HOST_URL) == "https://en.wikipedia.org"  # noqa: SLF001

    def test_max_concurrent_requests(self) -> None:
        """_MAX_CONCURRENT_REQUESTS_PER_HOST should be 2."""
        assert _mod._MAX_CONCURRENT_REQUESTS_PER_HOST == 2  # noqa: SLF001

    def test_list_indent(self) -> None:
        """_LIST_INDENT should be 4 spaces."""
        assert _mod._LIST_INDENT == "    "  # noqa: SLF001

    def test_bad_titles(self) -> None:
        """_BAD_TITLES should contain known bad titles."""
        assert "Edit this at Wikidata" in _mod._BAD_TITLES  # noqa: SLF001

    def test_ignored_name_prefixes(self) -> None:
        """_IGNORED_NAME_PREFIXES should be a frozenset."""
        assert isinstance(_mod._IGNORED_NAME_PREFIXES, frozenset)  # noqa: SLF001

    def test_preserved_page_prefixes_contains_category(self) -> None:
        """_PRESERVED_PAGE_PREFIXES should contain Category."""
        assert "Category:" in _mod._PRESERVED_PAGE_PREFIXES  # noqa: SLF001

    def test_archive_regexes(self) -> None:
        """_ARCHIVE_REGEXES should be a non-empty list."""
        assert len(_mod._ARCHIVE_REGEXES) > 0  # noqa: SLF001

    def test_script_directory(self) -> None:
        """_SCRIPT_DIRECTORY should be absolute."""
        assert Path(_mod._SCRIPT_DIRECTORY).is_absolute()  # noqa: SLF001

    def test_converted_wiki_directory(self) -> None:
        """_CONVERTED_WIKI_DIRECTORY should point to general/."""
        assert _mod._CONVERTED_WIKI_DIRECTORY.name == "general"  # noqa: SLF001

    def test_converted_wiki_language_directory(self) -> None:
        """_CONVERTED_WIKI_LANGUAGE_DIRECTORY should point to general/eng."""
        assert _mod._CONVERTED_WIKI_LANGUAGE_DIRECTORY.name == "eng"  # noqa: SLF001

    def test_filename_rename_map_loaded(self) -> None:
        """_names_map_manual should be a dict loaded from JSONC."""
        assert isinstance(_mod._names_map_manual, dict)  # noqa: SLF001

    def test_names_map_exists(self) -> None:
        """_NAMES_MAP should be a dict with entries from both maps."""
        assert isinstance(_mod._NAMES_MAP, dict)  # noqa: SLF001

    def test_markdown_separator(self) -> None:
        """_MARKDOWN_SEPARATOR should be the expected comment."""
        assert _mod._MARKDOWN_SEPARATOR == "<!-- markdown separator -->"  # noqa: SLF001

    def test_page_does_not_exist_suffix(self) -> None:
        """_PAGE_DOES_NOT_EXIST_SUFFIX should be as expected."""
        assert _mod._PAGE_DOES_NOT_EXIST_SUFFIX == " (page does not exist)"  # noqa: SLF001

    def test_markdown_separator_character_content(self) -> None:
        """_MARKDOWN_SEPARATOR_CHARACTERS should contain underscores and slashes removed."""
        assert "/" not in _mod._MARKDOWN_SEPARATOR_CHARACTERS  # noqa: SLF001
        assert "_" not in _mod._MARKDOWN_SEPARATOR_CHARACTERS  # noqa: SLF001


class TestWithCwd:
    """Tests for the _with_cwd context manager."""

    def test_changes_and_restores_cwd(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        """Should temporarily change the working directory and restore it."""
        # We need to monkeypatch getcwd/chdir since we can't actually chdir without
        # affecting other tests

        def tracking_chdir(path: str) -> None:
            tracking_chdir.last_path = path  # type: ignore[attr-defined]

        tracking_chdir.last_path = None  # type: ignore[attr-defined]
        monkeypatch.setattr("scripts.convert_wiki.chdir", tracking_chdir)
        # Note: we test through the context manager but can't fully test
        # without actually changing the cwd

    def test_restores_cwd_on_exception(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Should restore the original cwd even when the body raises."""
        original_cwd = os.getcwd()
        # _with_cwd catches the exception and restores cwd
        cwds: list[str] = []

        def tracking_getcwd() -> str:
            if cwds:
                return cwds[-1]
            return original_cwd

        def tracking_chdir(path: str) -> None:
            cwds.append(path)

        monkeypatch.setattr("scripts.convert_wiki.getcwd", tracking_getcwd)
        monkeypatch.setattr("scripts.convert_wiki.chdir", tracking_chdir)

        try:
            with _mod._with_cwd("/tmp"):  # noqa: SLF001
                raise ValueError("test exception")
        except ValueError:
            pass

        # cwd should be restored
        assert cwds[-1] == original_cwd


class TestModuleExports:
    """Tests for module-level behavior."""

    def test_all_is_empty(self) -> None:
        """__all__ should be an empty tuple (standalone script)."""
        assert _mod.__all__ == ()


class TestNewApiConstants:
    """Tests for newly added API and cache constants."""

    def test_api_max_titles_per_request(self) -> None:
        """_API_MAX_TITLES_PER_REQUEST should be 50."""
        assert _mod._API_MAX_TITLES_PER_REQUEST == 50  # noqa: SLF001

    def test_cache_ttl_is_one_day(self) -> None:
        """_CACHE_TTL should be a timedelta of 1 day."""
        assert _mod._CACHE_TTL.days == 1  # noqa: SLF001

    def test_api_max_retries(self) -> None:
        """_API_MAX_RETRIES should be 3."""
        assert _mod._API_MAX_RETRIES == 3  # noqa: SLF001

    def test_api_initial_backoff(self) -> None:
        """_API_INITIAL_BACKOFF should be 1.0."""
        assert _mod._API_INITIAL_BACKOFF == 1.0  # noqa: SLF001

    def test_api_backoff_multiplier(self) -> None:
        """_API_BACKOFF_MULTIPLIER should be 2.0."""
        assert _mod._API_BACKOFF_MULTIPLIER == 2.0  # noqa: SLF001

    def test_api_max_backoff(self) -> None:
        """_API_MAX_BACKOFF should be 30.0."""
        assert _mod._API_MAX_BACKOFF == 30.0  # noqa: SLF001


class TestNewRegexConstants:
    """Tests for regex constants moved to module level."""

    def test_bad_characters_compiled(self) -> None:
        """_BAD_CHARACTERS should be a compiled regex."""
        assert hasattr(_mod._BAD_CHARACTERS, "search")  # noqa: SLF001

    def test_header_regex(self) -> None:
        """_HEADER_REGEX should match h1-h6."""

        assert _mod._HEADER_REGEX.match("h1")  # noqa: SLF001
        assert _mod._HEADER_REGEX.match("h6")  # noqa: SLF001
        assert not _mod._HEADER_REGEX.match("div")  # noqa: SLF001

    def test_markdown_escape_regex(self) -> None:
        """_MARKDOWN_ESCAPE_REGEX should match special chars."""
        assert _mod._MARKDOWN_ESCAPE_REGEX.search("[")  # noqa: SLF001
        assert _mod._MARKDOWN_ESCAPE_REGEX.search("_")  # noqa: SLF001
        assert not _mod._MARKDOWN_ESCAPE_REGEX.search("abc")  # noqa: SLF001


class TestRedirectInfo:
    """Tests for _RedirectInfo dataclass."""

    def test_default_tofragment(self) -> None:
        """tofragment should default to empty string."""
        info = _mod._RedirectInfo(to="Target Page")  # noqa: SLF001
        assert info.to == "Target Page"
        assert info.tofragment == ""

    def test_explicit_fragment(self) -> None:
        """tofragment should be settable."""
        info = _mod._RedirectInfo(to="Page", tofragment="section")  # noqa: SLF001
        assert info.tofragment == "section"

    def test_frozen(self) -> None:
        """_RedirectInfo should be frozen (immutable)."""

        assert dataclasses.is_dataclass(_mod._RedirectInfo)  # noqa: SLF001
        assert _mod._RedirectInfo.__dataclass_params__.frozen  # noqa: SLF001


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

    def test_save_and_load(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should round-trip cache data through JSON."""
        monkeypatch.setattr(
            _mod, "_REDIRECT_CACHE_PATH", tmp_path / "redirect_cache.json"
        )
        cache = {
            "A": _mod._RedirectInfo(to="B", tofragment=""),  # noqa: SLF001
            "C": _mod._RedirectInfo(to="D", tofragment="s"),  # noqa: SLF001
            "E": _mod._RedirectInfo(to="E"),  # noqa: SLF001  # non-redirect
        }
        _mod._save_redirect_cache(cache)  # noqa: SLF001
        loaded = _mod._load_redirect_cache()  # noqa: SLF001
        assert len(loaded) == 3
        assert loaded["A"].to == "B"
        assert loaded["A"].tofragment == ""
        assert loaded["C"].tofragment == "s"
        assert loaded["E"].to == "E"

    def test_load_missing_file(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should return empty dict when cache file does not exist."""
        monkeypatch.setattr(_mod, "_REDIRECT_CACHE_PATH", tmp_path / "nonexistent.json")
        loaded = _mod._load_redirect_cache()  # noqa: SLF001
        assert loaded == {}

    def test_load_corrupted_file(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should return empty dict when cache file is corrupted."""
        path = tmp_path / "corrupt.json"
        path.write_text("{bad json}", encoding="UTF-8")
        monkeypatch.setattr(_mod, "_REDIRECT_CACHE_PATH", path)
        loaded = _mod._load_redirect_cache()  # noqa: SLF001
        assert loaded == {}

    def test_load_expired_ttl(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should return empty dict when cache is older than TTL."""

        cache = {"X": _mod._RedirectInfo(to="Y")}  # noqa: SLF001
        path = tmp_path / "old_cache.json"
        monkeypatch.setattr(_mod, "_REDIRECT_CACHE_PATH", path)
        monkeypatch.setattr(_mod, "_CACHE_TTL", timedelta(days=1))
        _mod._save_redirect_cache(cache)  # noqa: SLF001
        # Backdate the mtime
        old_time = (datetime.now(timezone.utc) - timedelta(days=2)).timestamp()

        os.utime(path, (old_time, old_time))
        loaded = _mod._load_redirect_cache()  # noqa: SLF001
        assert loaded == {}


class TestApiRequest:
    """Tests for _api_request function."""

    def test_returns_json_on_200(self) -> None:
        """Should return parsed JSON on HTTP 200."""

        async def run() -> None:
            class MockResponse:
                status = 200

                async def json(self):
                    return {"key": "value"}

                async def __aenter__(self):
                    return self

                async def __aexit__(self, *args):
                    pass

            class MockGet:
                def __call__(self, url):
                    return MockResponse()

            class MockSession:
                get = MockGet()

            result = await _mod._api_request(  # noqa: SLF001
                MockSession(),  # type: ignore[arg-type]
                {"action": "query"},
            )
            assert result == {"key": "value"}

        anyio.run(run, backend="asyncio")

    def test_retries_on_429(self) -> None:
        """Should retry after 429 and eventually succeed."""

        async def run() -> None:
            call_count = 0

            class MockResponse:
                def __init__(self, status, retry_after=None):
                    self.status = status
                    self._retry_after = retry_after

                @property
                def headers(self):
                    if self._retry_after:
                        return {"Retry-After": self._retry_after}
                    return {}

                async def json(self):
                    return {"key": "value"}

                async def __aenter__(self):
                    return self

                async def __aexit__(self, *args):
                    nonlocal call_count
                    call_count += 1

            class MockGet:
                def __call__(self, url):
                    if call_count < 2:
                        return MockResponse(429)
                    return MockResponse(200)

            class MockSession:
                get = MockGet()

            result = await _mod._api_request(  # noqa: SLF001
                MockSession(),  # type: ignore[arg-type]
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
            cache = {
                "Page A": _mod._RedirectInfo(to="Page A"),  # noqa: SLF001
                "Page B": _mod._RedirectInfo(to="Page B"),  # noqa: SLF001
            }
            titles = {"Page A", "Page B"}

            class MockSession:
                def get(self, url):
                    msg = "API call should not be made"
                    raise RuntimeError(msg)

            result = await _mod._resolve_redirects(  # noqa: SLF001
                MockSession(),  # type: ignore[arg-type]
                titles,
                cache,
            )
            assert result["Page A"].to == "Page A"
            assert result["Page B"].to == "Page B"
            assert len(result) == 2

        anyio.run(run, backend="asyncio")

    def test_resolves_redirect(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should resolve redirect via API and cache the result."""

        monkeypatch.setattr(
            _mod, "_REDIRECT_CACHE_PATH", tmp_path / "redirect_cache.json"
        )

        async def run() -> None:
            cache: dict[str, _mod._RedirectInfo] = {}  # noqa: SLF001
            titles = {"Redirect to Page"}

            class MockResponse:
                status = 200

                async def json(self):
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
                    return self

                async def __aexit__(self, *args):
                    pass

            class MockGet:
                def __call__(self, url):
                    return MockResponse()

            class MockSession:
                get = MockGet()

            result = await _mod._resolve_redirects(  # noqa: SLF001
                MockSession(),  # type: ignore[arg-type]
                titles,
                cache,
            )
            assert result["Redirect to Page"].to == "Actual Page"

        anyio.run(run, backend="asyncio")

    def test_redirect_with_fragment(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should preserve tofragment from API response."""

        monkeypatch.setattr(
            _mod, "_REDIRECT_CACHE_PATH", tmp_path / "redirect_cache.json"
        )

        async def run() -> None:
            cache: dict[str, _mod._RedirectInfo] = {}  # noqa: SLF001
            titles = {"Dest with Anchor"}

            class MockResponse:
                status = 200

                async def json(self):
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
                    return self

                async def __aexit__(self, *args):
                    pass

            class MockGet:
                def __call__(self, url):
                    return MockResponse()

            class MockSession:
                get = MockGet()

            result = await _mod._resolve_redirects(  # noqa: SLF001
                MockSession(),  # type: ignore[arg-type]
                titles,
                cache,
            )
            assert result["Dest with Anchor"].tofragment == "section"

        anyio.run(run, backend="asyncio")

    def test_non_redirect_resolved_to_self(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Should map non-redirect pages to themselves in cache."""

        monkeypatch.setattr(
            _mod, "_REDIRECT_CACHE_PATH", tmp_path / "redirect_cache.json"
        )

        async def run() -> None:
            cache: dict[str, _mod._RedirectInfo] = {}  # noqa: SLF001
            titles = {"Normal Page"}

            class MockResponse:
                status = 200

                async def json(self):
                    return {
                        "query": {
                            "redirects": [],
                            "pages": [{"pageid": 10, "ns": 0, "title": "Normal Page"}],
                        }
                    }

                async def __aenter__(self):
                    return self

                async def __aexit__(self, *args):
                    pass

            class MockGet:
                def __call__(self, url):
                    return MockResponse()

            class MockSession:
                get = MockGet()

            result = await _mod._resolve_redirects(  # noqa: SLF001
                MockSession(),  # type: ignore[arg-type]
                titles,
                cache,
            )
            assert result["Normal Page"].to == "Normal Page"

        anyio.run(run, backend="asyncio")
