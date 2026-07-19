"""Configuration constants for the Wikipedia HTML-to-Markdown converter.

This module contains all module-level constants, regex patterns, file paths,
and the filename-rename map builder.  Pure configuration with no conversion
logic.
"""

from collections.abc import Callable, Set
from contextlib import contextmanager
from datetime import timedelta
from logging import getLogger
from os import PathLike, chdir, getcwd
from pathlib import Path as PathlibPath
from re import DOTALL, MULTILINE, Pattern, compile
from string import punctuation, whitespace
from sys import version

import json5
from yarl import URL

"""Exported names from this module."""
__all__ = ()


@contextmanager
def _with_cwd(cwd: PathLike[str], chdir=chdir, getcwd=getcwd):
    """Temporarily change the current working directory."""
    old_cwd = getcwd()
    chdir(cwd)
    try:
        yield
    finally:
        chdir(old_cwd)


"Script filename."
NAME = "convert_wiki.py"
"""Script name without extension."""
BASE_NAME = "convert_wiki"
"Script authors."
AUTHORS = (
    {
        "name": "William So",
        "email": "polyipseity@gmail.com",
    },
)
"Script version."
VERSION = "∞"
"User agent string for HTTP requests."
USER_AGENT = f"{NAME}/{VERSION} ({AUTHORS[0]['email']}) Python/{version}"

# Wikipedia configuration
"Base URL for the English Wikipedia wiki host."
_WIKI_HOST_URL = URL.build(scheme="https", host="en.wikipedia.org")
"Base URL for Wikimedia Commons API."
_COMMONS_HOST_URL = URL.build(scheme="https", host="commons.wikimedia.org")
"Maximum concurrent HTTP requests per host."
_MAX_CONCURRENT_REQUESTS_PER_HOST = 2
"Set of page titles to ignore when converting links."
_BAD_TITLES: Set[str] = frozenset({"Edit this at Wikidata"})
"Set of name prefixes to ignore when fixing link names."
_IGNORED_NAME_PREFIXES: Set[str] = frozenset()
"Suffix appended to page titles that do not exist."
_PAGE_DOES_NOT_EXIST_SUFFIX = " (page does not exist)"
"Mapping of Wikipedia page prefixes to their external URL formats."
_PRESERVED_PAGE_PREFIXES = {
    "Category:": f"{_WIKI_HOST_URL}/wiki/Category:{{}}",
    "File:": f"{_WIKI_HOST_URL}/wiki/File:{{}}",
    "Help:": f"{_WIKI_HOST_URL}/wiki/Help:{{}}",
    "Portal:": f"{_WIKI_HOST_URL}/wiki/Portal:{{}}",
    "Special:": f"{_WIKI_HOST_URL}/wiki/Special:{{}}",
    "Talk:": f"{_WIKI_HOST_URL}/wiki/Talk:{{}}",
    "Template:": f"{_WIKI_HOST_URL}/wiki/Template:{{}}",
    "Template talk:": f"{_WIKI_HOST_URL}/wiki/Template%20talk:{{}}",
    "Wikipedia:": f"{_WIKI_HOST_URL}/wiki/Wikipedia:{{}}",
    "b:": "https://en.wikibooks.org/wiki/{}",
    "c:": "https://commons.wikimedia.org/wiki/{}",
    "commons:": "https://commons.wikimedia.org/wiki/{}",
    "d:": "https://www.wikidata.org/wiki/{}",
    "n:": "https://en.wikinews.org/wiki/{}",
    "oeis:": "https://oeis.org/{}",
    "planetmath:": "https://planetmath.org/alphabetical.html#{}",
    "q:": "https://en.wikiquote.org/wiki/{}",
    "s:": "https://en.wikisource.org/wiki/{}",
    "v:": "https://en.wikiversity.org/wiki/{}",
    "wikibooks:": "https://en.wikibooks.org/wiki/{}",
    "wikidata:": "https://www.wikidata.org/wiki/{}",
    "wikinvest:": "https://meta.wikimedia.org/wiki/Interwiki_map/discontinued?page={}",
    "wikiversity:": "https://en.wikiversity.org/wiki/{}",
    "wikt:": "https://en.wiktionary.org/wiki/{}",
    "wiktionary:": "https://en.wiktionary.org/wiki/{}",
}


# Markdown formatting constants
"Indentation string for nested Markdown lists."
_LIST_INDENT = "    "
"Characters considered as separators in Markdown formatting."
_MARKDOWN_SEPARATOR_CHARACTERS = f"{punctuation}{whitespace}\xa0".translate(
    {
        ord("/"): "",
        ord("_"): "",
    }
)
"Constant mapping table column alignment specifiers to string justification methods."
_JUSTIFY_MAP: dict[str, Callable[[str, int], str]] = {
    "---": str.ljust,
    ":--": str.ljust,
    "--:": str.rjust,
    ":-:": str.center,
}

# File paths
"Script directory for resolving relative data files."
_SCRIPT_DIRECTORY = PathlibPath(__file__).resolve(strict=True).parent.parent
"Data directory for auxiliary data files (rename maps, caches, etc.)."
_DATA_DIRECTORY = _SCRIPT_DIRECTORY / "assets"
"Directory where converted Wikipedia Markdown notes are stored."
_CONVERTED_WIKI_DIRECTORY = _SCRIPT_DIRECTORY.parent / "general"
"Subdirectory for language-specific Wikipedia notes (will be made dynamic in Phase 7)."
_CONVERTED_WIKI_LANGUAGE_DIRECTORY = _CONVERTED_WIKI_DIRECTORY / "eng"

"Combined filename rename map merging auto-detected and manual entries."
_NAMES_MAP_NAME = "convert_wiki"
"Name used for the names map file (``{_NAMES_MAP_NAME}.name_map.jsonc``)."

_NAMES_MAP: dict[str, str]


def _build_names_map(
    name_map_path: PathLike[str] | None = None,
    wiki_dir: PathLike[str] | None = None,
) -> dict[str, str]:
    """Build the combined filename rename map from the JSONC file and wiki directory scan.

    Parameters
    ----------
    name_map_path:
        Path to the manual name map JSONC file.
        Defaults to ``_DATA_DIRECTORY / \"{_NAMES_MAP_NAME}.name_map.jsonc\"``.
    wiki_dir:
        Wiki directory to scan for Markdown files.
        Defaults to ``_CONVERTED_WIKI_DIRECTORY``.
    """
    path = name_map_path or _DATA_DIRECTORY / f"{_NAMES_MAP_NAME}.name_map.jsonc"
    with open(path, "rt", encoding="UTF-8") as f:
        names_map_manual = json5.load(f)
    wiki_dir = wiki_dir or _CONVERTED_WIKI_DIRECTORY
    names_map = {
        key: val
        for entry in PathlibPath(wiki_dir).iterdir()
        if (filename := entry.name).endswith(".md")
        for key, val in (
            (f"{filename[:1].upper()}{filename[1:-3]}", filename[:-3]),
            (
                f"{filename[:1].upper()}{filename[1:-3]}".replace("'", "’"),
                filename[:-3].replace("'", "’"),
            ),
            (f"{filename[:1].lower()}{filename[1:-3]}", filename[:-3]),
            (
                f"{filename[:1].lower()}{filename[1:-3]}".replace("'", "’"),
                filename[:-3].replace("'", "’"),
            ),
        )
    }
    if overlap := frozenset(names_map).intersection(names_map_manual):
        raise ValueError(overlap)
    return names_map | names_map_manual


"""Assigned at module level: built from auto-discovered files plus manual JSONC overrides."""
_NAMES_MAP = _build_names_map()

# Redirect cache & API configuration
"Path to the redirect resolution cache file."
_REDIRECT_CACHE_PATH = _DATA_DIRECTORY / f"{_NAMES_MAP_NAME}.redirect_cache.json"
"Maximum titles per batch when querying redirects."
_API_MAX_TITLES_PER_REQUEST = 50
"TTL for the redirect cache."
_CACHE_TTL = timedelta(days=1)
"Maximum number of retries for 429 Too Many Requests."
_API_MAX_RETRIES = 3
"Initial backoff in seconds for 429 retry."
_API_INITIAL_BACKOFF = 1.0
"Multiplier for exponential backoff."
_API_BACKOFF_MULTIPLIER = 2.0
"Maximum backoff in seconds."
_API_MAX_BACKOFF = 30.0

# Regex patterns
"Regex for filesystem-unsafe characters in filenames."
_BAD_CHARACTERS: Pattern[str] = compile(r"[/:\\]")
"Regex for matching header tag names (h1-h6)."
_HEADER_REGEX: Pattern[str] = compile(r"h(\d?)")
"Regex for detecting bold font-weight in inline styles."
_BOLD_FONT_STYLE_REGEX: Pattern[str] = compile(r"font-weight: *bold")
"Regex for detecting italic font-style in inline styles."
_ITALIC_FONT_STYLE_REGEX: Pattern[str] = compile(r"font-style: *italic")
"Regex for escaping special Markdown characters."
_MARKDOWN_ESCAPE_REGEX: Pattern[str] = compile(r"[#$()*<>\\[\\\]_`|]")
"Regex for splitting bold/italic strings with surrounding whitespace."
_PROCESS_STRINGS_BI_REGEX: Pattern[str] = compile(r"^( *)(.*?)([\n ]*)$", DOTALL)
"Regex for extracting reference content from citation brackets."
_REF_CONTENT_REGEX: Pattern[str] = compile(r"\[([^]]*)\]")
"Regex for collapsing consecutive newlines."
_CONSECUTIVE_NEWLINES_REGEX: Pattern[str] = compile(r"\n{3,}")
"Regex for extracting text-align values from inline styles."
_TEXT_ALIGN_REGEX: Pattern[str] = compile(r"text-align:\s*(left|center|right)")
"Regex for collapsing consecutive empty blockquote lines."
_COLLAPSE_EMPTY_BLOCKQUOTE_RE: Pattern[str] = compile(r"(?:^>\n){2,}", MULTILINE)
"Regex for collapsing runs of consecutive regular spaces in text nodes."
_COLLAPSE_SPACES_REGEX: Pattern[str] = compile(r" {2,}")
"""Regex for collapsing consecutive leading whitespace characters across multiple lines."""
_CONSECUTIVE_LEADING_WHITESPACES_REGEX: Pattern[str] = compile(r"^[ \t]+", MULTILINE)
"Regex for handling table-in-table headers."
_TABLE_IN_TABLE_HEADER_REGEX: Pattern[str] = compile(r"\| (__.*?__) \|")
"Regex for stripping leading pipes in nested tables."
_TABLE_IN_TABLE_LEADING_VERTICAL_REGEX: Pattern[str] = compile(r"\s*\|")
"Regex for stripping trailing pipes in nested tables."
_TABLE_IN_TABLE_TRAILING_VERTICAL_REGEX: Pattern[str] = compile(r"\|\s*")
"Regexes mapping Wikimedia upload URLs to archive filename and path formats."
_ARCHIVE_REGEXES = {
    compile(
        r"^https://upload.wikimedia.org/wikipedia/[^/]*/[0-9a-f]/[0-9a-f]{2}/([^/]*)$"
    ): ("File:{}", "../../archives/Wikimedia Commons/{}"),
    compile(
        r"^https://upload.wikimedia.org/wikipedia/[^/]*/thumb/[0-9a-f]/[0-9a-f]{2}/([^/]*)/.*$"
    ): ("File:{}", "../../archives/Wikimedia Commons/{}"),
    compile(
        r"^https://upload.wikimedia.org/wikipedia/[^/]*/transcoded/[0-9a-f]/[0-9a-f]{2}/([^/]*)/.*$"
    ): ("File:{}", "../../archives/Wikimedia Commons/{}"),
    compile(r"^https://[^\.]*.?wikipedia.org/wiki/File:(.*)$"): (
        "File:{}",
        "../../archives/Wikimedia Commons/{}",
    ),
}

"Module-level logger."
_logger = getLogger(__name__)
