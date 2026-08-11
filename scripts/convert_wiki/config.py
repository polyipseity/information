"""Configuration constants for the Wikipedia HTML-to-Markdown converter.

This module contains all module-level constants, regex patterns, file paths,
and the filename-rename map loader.  Pure configuration with no conversion
logic.
"""

from collections.abc import Callable, Set
from contextlib import contextmanager
from datetime import timedelta
from logging import getLogger
from os import PathLike, chdir, getcwd
from pathlib import Path as PathlibPath
from re import Pattern, compile
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
"Citation UI anchor titles that must never become redirect cache entries."
_CITATION_UI_TITLES: Set[str] = frozenset({"Jump up"})
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
"Marker comment inserted between adjacent text elements that would otherwise join into one word."
_MARKDOWN_SEPARATOR = "<!-- markdown separator -->"
"""
Unicode math sign and operator characters that separate adjacent text
without needing a space or marker. Contents: minus sign U+2212, plus-minus
U+00B1, minus-or-plus U+2213, multiplication sign U+00D7, division sign
U+00F7, middle dot U+00B7, dot operator U+22C5, and the Latin dashes
U+2010-U+2015 (hyphen, non-breaking hyphen, figure dash, en dash, em dash,
horizontal bar).
"""
_UNICODE_SEPARATOR_CHARACTERS = (
    "\u2212\u00b1\u2213\u00d7\u00f7\u00b7\u22c5\u2010\u2011\u2012\u2013\u2014\u2015"
)
"Characters considered as separators in Markdown formatting."
_MARKDOWN_SEPARATOR_CHARACTERS = (
    f"{punctuation}{whitespace}\xa0{_UNICODE_SEPARATOR_CHARACTERS}"
).translate(
    {
        ord("/"): "",
        ord("_"): "",
    }
)
"Constant mapping table column alignment specifiers to string justification methods."
_JUSTIFY_MAP: dict[str, Callable[[str, int], str]] = {
    "---": str.ljust,  # No alignment specified (renderer default, typically left)
    ":--": str.ljust,  # Explicitly left-aligned
    "--:": str.rjust,  # Right-aligned
    ":-:": str.center,  # Center-aligned
}
"""
Semantic note:

- ``---`` and ``:--`` both use ``str.ljust`` because in GFM they render
  identically (left-aligned).  The distinction is semantic-only:
  ``---`` = "no alignment specified" (renderer chooses, typically left);
  ``:--`` = "explicitly left-aligned".  Do not confuse them or try to
  make ``---`` produce a different visual alignment.

- ``--:`` = right-aligned, ``:-:`` = center-aligned.
"""


# File paths
"Script directory for resolving relative data files."
_SCRIPT_DIRECTORY = PathlibPath(__file__).resolve(strict=True).parent.parent
"Data directory for auxiliary data files (rename maps, caches, etc.)."
_DATA_DIRECTORY = _SCRIPT_DIRECTORY / "assets"
"Directory where converted Wikipedia Markdown notes are stored."
_CONVERTED_WIKI_DIRECTORY = _SCRIPT_DIRECTORY.parent / "general"
"Subdirectory for language-specific Wikipedia notes (will be made dynamic in Phase 7)."
_CONVERTED_WIKI_LANGUAGE_DIRECTORY = _CONVERTED_WIKI_DIRECTORY / "eng"
"Directory where Wikimedia Commons media archives are stored."
_ARCHIVES_COMMONS_DIRECTORY = (
    _SCRIPT_DIRECTORY.parent / "archives" / "Wikimedia Commons"
)
"Index file for the Wikimedia Commons media archive."
_ARCHIVES_COMMONS_INDEX = _ARCHIVES_COMMONS_DIRECTORY / "index.md"

"Filename rename map loaded from JSONC."
_NAMES_MAP_NAME = "convert_wiki"
"Name used for the names map file (``{_NAMES_MAP_NAME}.name_map.jsonc``)."


def _load_names_map(name_map_path: PathLike[str] | None = None) -> dict[str, str]:
    """Load the filename rename map from the JSONC file.

    Parameters
    ----------
    name_map_path:
        Path to the name map JSONC file.
        Defaults to ``_DATA_DIRECTORY / \"{_NAMES_MAP_NAME}.name_map.jsonc\"``.
    """
    path = name_map_path or _DATA_DIRECTORY / f"{_NAMES_MAP_NAME}.name_map.jsonc"
    with open(path, "rt", encoding="UTF-8") as f:
        return json5.load(f)


"""Assigned at module level: loaded from JSONC only."""
_NAMES_MAP = _load_names_map()

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
"Regex for escaping special Markdown characters."
_MARKDOWN_ESCAPE_REGEX: Pattern[str] = compile(r"[#$()*<>\\[\\\]_`|]")
"Regexes mapping Wikimedia upload URLs to archive filename and path formats."
_ARCHIVE_REGEXES = {
    compile(
        r"^https://upload.wikimedia.org/wikipedia/[^/]*/[0-9a-f]/[0-9a-f]{2}/([^/?]*)$"
    ): ("File:{}", "../../archives/Wikimedia Commons/{}"),
    compile(
        r"^https://upload.wikimedia.org/wikipedia/[^/]*/thumb/[0-9a-f]/[0-9a-f]{2}/([^/?#]*)/.*$"
    ): ("File:{}", "../../archives/Wikimedia Commons/{}"),
    compile(
        r"^https://upload.wikimedia.org/wikipedia/[^/]*/transcoded/[0-9a-f]/[0-9a-f]{2}/([^/?#]*)/.*$"
    ): ("File:{}", "../../archives/Wikimedia Commons/{}"),
    compile(r"^https://[^\.]*.?wikipedia.org/wiki/File:([^?#]*)$"): (
        "File:{}",
        "../../archives/Wikimedia Commons/{}",
    ),
}

"Module-level logger."
_logger = getLogger(__name__)
