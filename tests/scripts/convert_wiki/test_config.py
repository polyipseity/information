"""Tests for scripts/convert_wiki/config.py.

These tests cover the module-level constants and configuration helpers.
"""

import os
from os import PathLike

from anyio import Path

from scripts.convert_wiki import config as _mod
from scripts.convert_wiki.converter import _HEADER_REGEX, _MARKDOWN_SEPARATOR

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


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
        """_ARCHIVE_REGEXES should be a non-empty dict."""
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
        assert _MARKDOWN_SEPARATOR == "<!-- markdown separator -->"  # noqa: SLF001

    def test_page_does_not_exist_suffix(self) -> None:
        """_PAGE_DOES_NOT_EXIST_SUFFIX should be as expected."""
        assert _mod._PAGE_DOES_NOT_EXIST_SUFFIX == " (page does not exist)"  # noqa: SLF001

    def test_markdown_separator_character_content(self) -> None:
        """_MARKDOWN_SEPARATOR_CHARACTERS should contain underscores and slashes removed."""
        assert "/" not in _mod._MARKDOWN_SEPARATOR_CHARACTERS  # noqa: SLF001
        assert "_" not in _mod._MARKDOWN_SEPARATOR_CHARACTERS  # noqa: SLF001


class TestWithCwd:
    """Tests for the _with_cwd context manager."""

    def test_changes_and_restores_cwd(self, tmp_path: PathLike[str]) -> None:
        """Should temporarily change the working directory and restore it."""
        # We pass mock chdir/getcwd since we can't actually chdir without
        # affecting other tests.

        last_paths: list[str] = []

        def tracking_chdir(path: str) -> None:
            """Track chdir paths in order."""
            last_paths.append(path)

        with _mod._with_cwd(  # noqa: SLF001
            Path("/tmp"), chdir=tracking_chdir
        ):
            pass
        # Two calls: set to /tmp, then restore to original cwd.
        assert len(last_paths) == 2
        assert os.fspath(last_paths[0]) == os.fspath(Path("/tmp"))

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
        """_HEADER_REGEX should match h1-h6 (converter's stricter pattern)."""

        assert _HEADER_REGEX.match("h1")  # noqa: SLF001
        assert _HEADER_REGEX.match("h6")  # noqa: SLF001
        assert not _HEADER_REGEX.match("div")  # noqa: SLF001
        assert not _HEADER_REGEX.match("h")  # noqa: SLF001 — must have digit
        assert not _HEADER_REGEX.match("h12")  # noqa: SLF001 — exactly one digit

    def test_markdown_escape_regex(self) -> None:
        """_MARKDOWN_ESCAPE_REGEX should match special chars."""
        assert _mod._MARKDOWN_ESCAPE_REGEX.search("[")  # noqa: SLF001
        assert _mod._MARKDOWN_ESCAPE_REGEX.search("_")  # noqa: SLF001
        assert not _mod._MARKDOWN_ESCAPE_REGEX.search("abc")  # noqa: SLF001
