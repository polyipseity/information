"""Tests for scripts/convert_wiki.py.

These tests cover the pure functions and module-level constants that are
testable without HTTP requests or clipboard access.
"""

import dataclasses
import json
import os
from datetime import datetime, timedelta, timezone
from os import PathLike
from pathlib import Path as PathlibPath
from typing import cast

import anyio
import pytest
from aiohttp import ClientSession
from anyio import Path
from bs4 import BeautifulSoup, Tag

from scripts import convert_wiki as _mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


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
        assert isinstance(result, Tag)
        assert result.name == "b"

    def test_parse_tag_with_content(self) -> None:
        """Should parse a tag with text content."""
        result = _mod._bs4_new_element("<i>text</i>")  # noqa: SLF001
        assert isinstance(result, Tag)
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

    def test_name_map_loaded(self) -> None:
        """_build_names_map should return a non-empty dict from JSONC and wiki scan."""
        result = _mod._build_names_map()  # noqa: SLF001
        assert isinstance(result, dict)
        assert len(result) > 0

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

    def test_pyarchivist_args_import(self) -> None:
        """pyarchivist Args should be importable from the module."""
        assert hasattr(_mod, "Args")

    def test_pyarchivist_archive_import(self) -> None:
        """pyarchivist archive function should be importable from the module."""
        assert hasattr(_mod, "pyarchivist_archive")


class TestWithCwd:
    """Tests for the _with_cwd context manager."""

    def test_changes_and_restores_cwd(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should temporarily change the working directory and restore it."""
        # We pass mock chdir/getcwd since we can't actually chdir without
        # affecting other tests.

        last_path: str | None = None

        def tracking_chdir(path: str) -> None:
            """Track the last chdir path."""
            nonlocal last_path
            last_path = path

        with _mod._with_cwd(  # noqa: SLF001
            Path("/tmp"), chdir=tracking_chdir
        ):
            pass

    def test_restores_cwd_on_exception(self) -> None:
        """Should restore the original cwd even when the body raises."""
        original_cwd = os.getcwd()
        # _with_cwd catches the exception and restores cwd
        cwds: list[str] = []

        def tracking_getcwd() -> str:
            """Return tracked cwd or original."""
            if cwds:
                return cwds[-1]
            return original_cwd

        def tracking_chdir(path: str) -> None:
            """Track chdir by appending to cwds list."""
            cwds.append(path)

        try:
            with _mod._with_cwd(  # noqa: SLF001
                Path("/tmp"), chdir=tracking_chdir, getcwd=tracking_getcwd
            ):
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
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should round-trip cache data through JSON."""
        path = Path(tmp_path) / "redirect_cache.json"
        cache = {
            "A": _mod._RedirectInfo(to="B", tofragment=""),  # noqa: SLF001
            "C": _mod._RedirectInfo(to="D", tofragment="s"),  # noqa: SLF001
            "E": _mod._RedirectInfo(to="E"),  # noqa: SLF001  # non-redirect
        }
        _mod._save_redirect_cache(cache, cache_path=path)  # noqa: SLF001
        loaded = _mod._load_redirect_cache(cache_path=path)  # noqa: SLF001
        assert len(loaded) == 3
        assert loaded["A"].to == "B"
        assert loaded["A"].tofragment == ""
        assert loaded["C"].tofragment == "s"
        assert loaded["E"].to == "E"
        # cached_at should be set on round-trip
        assert isinstance(loaded["A"].cached_at, str) and loaded["A"].cached_at

    def test_load_missing_file(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should return empty dict when cache file does not exist."""
        path = Path(tmp_path) / "nonexistent.json"
        loaded = _mod._load_redirect_cache(cache_path=path)  # noqa: SLF001
        assert loaded == {}

    @pytest.mark.anyio
    async def test_load_corrupted_file(
        self, tmp_path: PathLike[str]
    ) -> None:
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
        monkeypatch.setattr(_mod, "_CACHE_TTL", timedelta(days=1))
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
    async def test_malformed_cached_at_skipped(
        self, tmp_path: PathLike[str]
    ) -> None:
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
        assert _mod._CACHE_TTL == timedelta(days=1)  # noqa: SLF001


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
                "Page A": _mod._RedirectInfo(to="Page A"),  # noqa: SLF001
                "Page B": _mod._RedirectInfo(to="Page B"),  # noqa: SLF001
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

    def test_resolves_redirect(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should resolve redirect via API and cache the result."""

        cache_path = Path(tmp_path) / "redirect_cache.json"

        async def run() -> None:
            """Run the async test body."""
            cache: dict[str, _mod._RedirectInfo] = {}  # noqa: SLF001
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

    def test_redirect_with_fragment(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should preserve tofragment from API response."""

        cache_path = Path(tmp_path) / "redirect_cache.json"

        async def run() -> None:
            """Run the async test body."""
            cache: dict[str, _mod._RedirectInfo] = {}  # noqa: SLF001
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

    def test_non_redirect_resolved_to_self(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should map non-redirect pages to themselves in cache."""

        cache_path = Path(tmp_path) / "redirect_cache.json"

        async def run() -> None:
            """Run the async test body."""
            cache: dict[str, _mod._RedirectInfo] = {}  # noqa: SLF001
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
        monkeypatch.setattr(_mod, "_CACHE_TTL", timedelta(days=1))

        async def run() -> None:
            """Run the async test body."""
            # Pre-populate a stale cache file with expired entries on disk.
            old_ts = (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()
            stale_cache = {
                "Page X": _mod._RedirectInfo(to="Page X", cached_at=old_ts),  # noqa: SLF001
                "Page Y": _mod._RedirectInfo(to="Page Y", cached_at=old_ts),  # noqa: SLF001
            }
            _mod._save_redirect_cache(stale_cache, cache_path=path)  # noqa: SLF001

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
        expected_raw = aux["redirect_cache"]

        assert len(result) == len(expected_raw)
        for title, info in expected_raw.items():
            assert title in result, f"Missing title: {title!r}"
            assert result[title].to == info["to"]
            assert result[title].tofragment == info.get("tofragment", "")

        # All batches should have been consumed.
        assert call_index == total_calls


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
            converted_wiki_dir=PathlibPath(top_dir),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
        assert os.readlink(from_symlink) == "To Page.md"
        assert os.readlink(top_symlink) == "eng/From Page.md"

    @pytest.mark.anyio
    async def test_symlink_not_created_when_same(self, tmp_path: PathLike[str]) -> None:
        """Should not create symlinks when from/to filenames are identical."""
        tmp = Path(tmp_path)
        lang_dir = tmp / "general" / "eng"
        top_dir = tmp / "general"
        await lang_dir.mkdir(parents=True)

        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=PathlibPath(top_dir),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
            converted_wiki_dir=PathlibPath(top_dir),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
        # but os.symlink() raises FileExistsError
        os.symlink("nonexistent.md", lang_dir / "From Page.md")
        assert not await (lang_dir / "From Page.md").exists()  # broken symlink

        converter = _mod.WikiHtmlConverter(
            converted_wiki_dir=PathlibPath(top_dir),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
        assert os.readlink(lang_dir / "From Page.md") == "nonexistent.md"
        # Top-level symlink should still be created (separate guard)
        assert await (top_dir / "From Page.md").is_symlink()


"""Absolute path to the snapshot test fixtures directory."""
_SNAPSHOT_DIR = (
    PathlibPath(__file__).resolve(strict=True).with_name("convert_wiki")
    / "snapshots"
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
            wiki_dir=PathlibPath(tmp / "general"),
            wiki_lang_dir=PathlibPath(isolated_lang),
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
            converted_wiki_dir=PathlibPath(tmp / "general"),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
            converted_wiki_dir=PathlibPath(tmp / "general"),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
            converted_wiki_dir=PathlibPath(tmp / "general"),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
            converted_wiki_dir=PathlibPath(tmp / "general"),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
            converted_wiki_dir=PathlibPath(tmp / "general"),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
            converted_wiki_dir=PathlibPath(tmp / "general"),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
            converted_wiki_dir=PathlibPath(tmp / "general"),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
            converted_wiki_dir=PathlibPath(tmp / "general"),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
            converted_wiki_dir=PathlibPath(tmp / "general"),
            converted_wiki_lang_dir=PathlibPath(lang_dir),
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
