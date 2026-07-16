#!/usr/bin/env python
"""Convert Wikipedia HTML from the clipboard into a Markdown note.

Reads HTML from the system clipboard, normalises it to Markdown,
downloads referenced media to ``archives/Wikimedia Commons/``,
and outputs the result.  Supports four output modes: clipboard
(default), stdout, stderr, or append to a specified file.
"""

import argparse
import re
from collections.abc import (
    Awaitable,
    Callable,
    Iterator,
    Mapping,
    MutableMapping,
    MutableSet,
    Set,
)
from contextlib import contextmanager, suppress
from copy import copy
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from json import JSONDecodeError
from json import dump as json_dump
from json import load as json_load
from logging import INFO, basicConfig, getLogger
from os import PathLike, chdir, getcwd, scandir, symlink
from os import replace as os_replace
from pathlib import Path as PathlibPath
from pathlib import PurePath
from re import DOTALL, MULTILINE, Pattern, compile
from string import punctuation, whitespace
from sys import stderr, stdin, version
from typing import NotRequired, TypedDict
from urllib.parse import quote, unquote

import anyio
import json5
from aiohttp import ClientSession, TCPConnector
from anyio import Path
from asyncer import SoonValue, create_task_group, runnify
from bs4 import BeautifulSoup, Tag
from bs4.element import NavigableString, PageElement, PreformattedString
from country_converter import convert
from jaraco.clipboard import paste_html
from pyarchivist import ArchiveResult, Args
from pyarchivist.Wikimedia_Commons import archive as pyarchivist_archive
from pyperclip import copy as clip_copy
from yarl import URL

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()


@contextmanager
def _with_cwd(cwd: PathLike[str]):
    """Temporarily change the current working directory."""
    old_cwd = getcwd()
    chdir(cwd)
    try:
        yield
    finally:
        chdir(old_cwd)


"Script filename."
NAME = PurePath(__file__).name
"Script name without extension."
BASE_NAME = PurePath(__file__).stem
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

"HTML child tag names for table cells."
_TD_OR_TH: Set[str] = frozenset({"td", "th"})
"HTML child tag names for bold/italic inline elements."
_BOLD_OR_ITALIC: Set[str] = frozenset({"b", "em", "i", "strong"})

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
"HTML comment used as a Markdown formatting separator."
_MARKDOWN_SEPARATOR = "<!-- markdown separator -->"
"Constant mapping table column alignment specifiers to string justification methods."
_JUSTIFY_MAP: dict[str, Callable[[str, int], str]] = {
    "---": str.ljust,
    ":--": str.ljust,
    "--:": str.rjust,
    ":-:": str.center,
}

# File paths
"Script directory for resolving relative data files."
_SCRIPT_DIRECTORY = PathlibPath(__file__).resolve(strict=True).parent
"Data directory for auxiliary data files (rename maps, caches, etc.)."
_DATA_DIRECTORY = _SCRIPT_DIRECTORY / "assets"
"Directory where converted Wikipedia Markdown notes are stored."
_CONVERTED_WIKI_DIRECTORY = _SCRIPT_DIRECTORY.parent / "general"
"Subdirectory for language-specific Wikipedia notes (will be made dynamic in Phase 7)."
_CONVERTED_WIKI_LANGUAGE_DIRECTORY = _CONVERTED_WIKI_DIRECTORY / "eng"

"Combined filename rename map merging auto-detected and manual entries."
_NAMES_MAP: dict[str, str]


def _build_names_map(
    name_map_path: PurePath | None = None,
    wiki_dir: PathlibPath | None = None,
) -> dict[str, str]:
    """Build the combined filename rename map from the JSONC file and wiki directory scan.

    Parameters
    ----------
    name_map_path:
        Path to the manual name map JSONC file.
        Defaults to ``_DATA_DIRECTORY / f\"{BASE_NAME}.name_map.jsonc\"``.
    wiki_dir:
        Wiki directory to scan for Markdown files.
        Defaults to ``_CONVERTED_WIKI_DIRECTORY``.
    """
    path = name_map_path or _DATA_DIRECTORY / f"{BASE_NAME}.name_map.jsonc"
    with open(path, "rt", encoding="UTF-8") as f:
        names_map_manual = json5.load(f)
    wiki_dir = wiki_dir or _CONVERTED_WIKI_DIRECTORY
    names_map = {
        key: val
        for entry in scandir(wiki_dir)
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
_REDIRECT_CACHE_PATH = _DATA_DIRECTORY / f"{BASE_NAME}.redirect_cache.json"
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


def _bs4_new_element(tag_str: str) -> PageElement:
    """Parse an HTML tag string and return the first element."""
    soup = BeautifulSoup(tag_str, "html.parser")
    return soup.contents[0].extract()


def _fix_name_maybe(
    name: str,
    *,
    normalize: bool = True,
    replace_underscores: bool = False,
    names_map: Mapping[str, str] | None = None,
) -> str:
    """Normalise and map a Wikipedia page name to the local filename stem."""
    names_map = names_map or _NAMES_MAP
    if normalize:
        name = name.replace("\u00a0", " ")
    if (ret := names_map.get(name)) is not None:
        return ret
    if replace_underscores:
        name = name.replace("_", " ")
    ret = names_map.get(
        name,
        (
            f"{name[:1].lower()}{name[1:]}"
            if len(name) <= 1 or name[1:].islower()
            else name
        ),
    )
    return ret


def _fix_filename(filename: str) -> str:
    """Replace filesystem-unsafe characters in a filename with underscores."""
    return _BAD_CHARACTERS.sub("_", filename)


def _markdown_fragment(fragment: str) -> str:
    """Return a URL fragment string suitable for a Markdown link anchor."""
    return (
        fragment
        and f"#{fragment.replace(':', '').replace(' ', '%20').replace('/', '%2F')}"
    )


def _markdown_link_target(page: str, fragment: str) -> str:
    """Build a relative Markdown link target for a given page name and fragment."""
    return f"{_fix_filename(page).replace(' ', '%20')}.md{_markdown_fragment(fragment)}"


def _tag_affixes(name: str) -> tuple[str, str]:
    """Return the opening and closing HTML tag strings for the given tag name."""
    return f"<{name}>", f"</{name}>"


def _get_image_filename(ele: Tag) -> str | None:
    """Extract the original uploaded filename from an ``<img>`` element.

    Returns the filename without ``File:`` prefix (e.g. ``Modernphysicsfields.svg``)
    or ``None`` if it cannot be determined from either ``resource`` or ``src``.
    """
    if resource := ele.get("resource"):
        src_url = _WIKI_HOST_URL.join(URL(str(resource)))
        src_url_str = src_url.human_repr()
        for regex in _ARCHIVE_REGEXES:
            if match := regex.search(src_url_str):
                return unquote(match[1]).replace("_", " ")
    if src := ele.get("src"):
        src_url = _WIKI_HOST_URL.join(URL(str(src)))
        src_url_str = src_url.human_repr()
        for regex in _ARCHIVE_REGEXES:
            if match := regex.search(src_url_str):
                return unquote(match[1]).replace("_", " ")
    return None


def _collect_image_filenames(html: Tag) -> set[str]:
    """Collect all image file titles from ``<img>`` elements in the HTML tree.

    Returns a set of ``File:XXX`` titles (e.g. ``File:Modernphysicsfields.svg``).
    """
    filenames = set[str]()
    for img in html.find_all("img"):
        if filename := _get_image_filename(img):
            filenames.add(f"File:{filename}")
    return filenames


@dataclass(frozen=True)
class _RedirectInfo:
    """Resolved redirect information for a Wikipedia page title."""

    to: str
    tofragment: str = ""
    cached_at: str = ""


"""Type alias for a single redirect entry from the MediaWiki API response."""
_RedirectItem = TypedDict(
    "_RedirectItem",
    {
        "from": str,  # Original page title (required)
        "to": NotRequired[str],  # Redirect target title
        "tofragment": NotRequired[str],  # Section fragment
    },
)


class _ApiQueryBody(TypedDict, total=False):
    """The ``query`` section of a MediaWiki API response."""

    redirects: list[_RedirectItem]


class _ApiResponse(TypedDict, total=False):
    """A MediaWiki ``action=query`` API response with redirects."""

    query: _ApiQueryBody


def _collect_link_titles(html: Tag) -> set[str]:
    """Collect all link titles that need redirect resolution."""
    titles = set[str]()
    for a in html.find_all("a", title=True):
        classes = frozenset(a.get_attribute_list("class"))
        # Skip links that do not need (or cannot have) redirect resolution
        if {"mw-file-description", "mw-selflink"} & classes:
            continue
        if "extiw" in classes:
            continue
        if "new" in classes:
            continue
        title = str(a["title"])
        if title in _BAD_TITLES:
            continue
        if any(title.startswith(prefix) for prefix in _PRESERVED_PAGE_PREFIXES):
            continue
        titles.add(title)
    return titles


def _load_redirect_cache(
    cache_path: PurePath | None = None,
) -> dict[str, _RedirectInfo]:
    """Load the redirect cache, respecting TTL.

    Parameters
    ----------
    cache_path:
        Path to the cache JSON file (default: ``_REDIRECT_CACHE_PATH``).
    """
    path = _REDIRECT_CACHE_PATH if cache_path is None else cache_path
    try:
        with open(path, "r", encoding="UTF-8") as f:
            data = json_load(f)
        if not isinstance(data, dict):
            return {}
        now = datetime.now(timezone.utc)
        unpacked: dict[str, _RedirectInfo] = {}
        for k, v in data.items():
            if not (isinstance(k, str) and isinstance(v, dict)):
                continue
            to = v.get("to", k)
            tofragment = v.get("tofragment", "")
            if not (isinstance(to, str) and isinstance(tofragment, str)):
                continue
            cached_at_str = v.get("cached_at", "")
            if not cached_at_str:
                # Old-format entry — stamp with current time.
                cached_at_str = now.isoformat()
            try:
                cached_at = datetime.fromisoformat(cached_at_str)
            except ValueError:
                continue  # malformed → skip
            if now - cached_at > _CACHE_TTL:
                continue  # expired
            unpacked[k] = _RedirectInfo(
                to=to, tofragment=tofragment, cached_at=cached_at_str
            )
        return unpacked
    except (FileNotFoundError, JSONDecodeError, OSError):
        return {}


def _save_redirect_cache(
    cache: MutableMapping[str, _RedirectInfo],
    cache_path: PurePath | None = None,
) -> None:
    """Atomically save the redirect cache.

    Parameters
    ----------
    cache:
        Redirect info by page title.
    cache_path:
        Path to the cache JSON file (default: ``_REDIRECT_CACHE_PATH``).
    """
    data = {
        k: {
            "to": v.to,
            "tofragment": v.tofragment,
            "cached_at": v.cached_at or datetime.now(timezone.utc).isoformat(),
        }
        for k, v in cache.items()
    }
    resolved_path = (
        _REDIRECT_CACHE_PATH if cache_path is None else PathlibPath(cache_path)
    )
    tmp = resolved_path.with_suffix(".tmp")
    try:
        with open(tmp, "w", encoding="UTF-8") as f:
            json_dump(data, f, ensure_ascii=False, indent=2)
        os_replace(tmp, resolved_path)
    except BaseException:
        with suppress(FileNotFoundError):
            PathlibPath(tmp).unlink()
        raise


async def _api_request(
    session: ClientSession,
    params: dict[str, str | int],
    host: URL = _WIKI_HOST_URL,
) -> _ApiResponse:
    """Make a MediaWiki API request with retry on HTTP 429."""
    url = URL.build(
        scheme=host.scheme,
        host=str(host.host),
        path="/w/api.php",
        query=params,
    )
    backoff = _API_INITIAL_BACKOFF
    for _attempt in range(_API_MAX_RETRIES):
        async with session.get(url) as req:
            if req.status == 429:
                retry_after_str = req.headers.get("Retry-After")
                if retry_after_str is not None:
                    try:
                        backoff = float(retry_after_str)
                    except ValueError:
                        pass
                await anyio.sleep(min(backoff, _API_MAX_BACKOFF))
                backoff = min(backoff * _API_BACKOFF_MULTIPLIER, _API_MAX_BACKOFF)
                continue
            return await req.json()
    # last attempt — raise on any non-200 status
    async with session.get(url) as req:
        return await req.json()


async def _resolve_redirects(
    session: ClientSession,
    titles: set[str],
    cache: MutableMapping[str, _RedirectInfo],
    cache_path: PurePath | None = None,
) -> MutableMapping[str, _RedirectInfo]:
    """Resolve redirects for uncached titles via batched API queries.

    Results are merged into *cache* and persisted to disk atomically.

    Parameters
    ----------
    cache_path:
        Path to persist the updated cache (default: ``_REDIRECT_CACHE_PATH``).
    """
    uncached = titles - cache.keys()
    if not uncached:
        return cache

    titles_list = list(uncached)
    now_iso = datetime.now(timezone.utc).isoformat()
    for i in range(0, len(titles_list), _API_MAX_TITLES_PER_REQUEST):
        batch = titles_list[i : i + _API_MAX_TITLES_PER_REQUEST]
        params: dict[str, str | int] = {
            "format": "json",
            "formatversion": 2,
            "action": "query",
            "titles": "|".join(batch),
            "redirects": "",
        }
        result = await _api_request(session, params)
        redirected_from = set[str]()
        if (query_body := result.get("query")) is not None:
            for r in query_body.get("redirects") or []:
                cache[r["from"]] = _RedirectInfo(
                    to=r.get("to", r["from"]),
                    tofragment=r.get("tofragment", ""),
                    cached_at=now_iso,
                )
                redirected_from.add(r["from"])
        for title in batch:
            if title not in redirected_from:
                cache.setdefault(title, _RedirectInfo(to=title, cached_at=now_iso))

    resolved_cache_path = _REDIRECT_CACHE_PATH if cache_path is None else cache_path
    _save_redirect_cache(cache, cache_path=resolved_cache_path)
    return cache


async def _resolve_image_metadata(
    session: ClientSession,
    filenames: set[str],
) -> dict[str, str]:
    """Fetch image description metadata from Wikimedia Commons API.

    Returns a mapping of ``File:XXX`` titles to their ``ImageDescription``
    text.  Files without descriptions or with API errors are omitted.
    """
    if not filenames:
        return {}

    result: dict[str, str] = {}
    titles_list = list(filenames)

    for i in range(0, len(titles_list), _API_MAX_TITLES_PER_REQUEST):
        batch = titles_list[i : i + _API_MAX_TITLES_PER_REQUEST]
        params: dict[str, str | int] = {
            "format": "json",
            "formatversion": 2,
            "action": "query",
            "prop": "imageinfo",
            "titles": "|".join(batch),
            "iiprop": "extmetadata",
        }
        api_result = await _api_request(session, params, host=_COMMONS_HOST_URL)

        if (query_body := api_result.get("query")) is None:
            continue

        for page in query_body.get("pages") or []:
            title = page.get("title", "")
            imageinfo = page.get("imageinfo") or []
            if not imageinfo:
                continue
            extmetadata = imageinfo[0].get("extmetadata") or {}
            description_obj = extmetadata.get("ImageDescription") or {}
            if description_value := description_obj.get("value", ""):
                # Commons API returns HTML — convert through the converter
                # pipeline to produce proper Markdown formatting.  Strip
                # ``title`` attributes from ``<a>`` tags first so the
                # converter treats them as external links (preserving the
                # original ``href`` URL) rather than resolving them as
                # internal Wikipedia interwiki links.
                fragment = BeautifulSoup(
                    f"<div>{description_value}</div>", "html.parser"
                )
                for a_tag in fragment.find_all("a"):
                    if a_tag.has_attr("title"):
                        del a_tag["title"]
                desc_converter = WikiHtmlConverter()
                desc = fragment.div
                if desc is not None:
                    converted = await desc_converter.convert(
                        desc,
                        out_to_archive=set(),
                        redirect_map={},
                        refs=False,
                    )
                    result[title] = converted.strip()

    return result


@dataclass
class _HandlerConfig:
    """Configuration returned by a tag handler for processing element children content."""

    joiner: str = ""
    prefix: str = ""
    suffix: str = ""
    process_strings: Callable[[str], str] = lambda s: s
    full_result: bool = False
    list_stack: tuple[int, ...] | None = None


class WikiHtmlConverter:
    """Converts Wikipedia HTML elements to Markdown text.

    Parameters
    ----------
    converted_wiki_dir:
        Directory where converted Wikipedia Markdown notes are stored
        (used for symlink creation on redirects).
    converted_wiki_lang_dir:
        Language-specific subdirectory for converted notes.
    """

    def __init__(
        self,
        *,
        converted_wiki_dir: PathlibPath = _CONVERTED_WIKI_DIRECTORY,
        converted_wiki_lang_dir: PathlibPath = _CONVERTED_WIKI_LANGUAGE_DIRECTORY,
        image_metadata: Mapping[str, str] | None = None,
        names_map: Mapping[str, str] | None = None,
    ) -> None:
        """Initialize converter with directory paths and name map."""
        self._converted_wiki_dir = converted_wiki_dir
        self._converted_wiki_lang_dir = converted_wiki_lang_dir
        self._image_metadata = image_metadata or {}
        self._names_map = names_map or _NAMES_MAP

    async def convert(
        self,
        ele: PageElement,
        *,
        out_to_archive: MutableSet[str],
        list_stack: tuple[int, ...] = (),
        escape: bool = True,
        refs: bool,
        redirect_map: Mapping[str, _RedirectInfo],
    ) -> str:
        """Convert a Wikipedia HTML element tree to a Markdown string."""

        # ---- Formatting-agnostic principle ----
        # HTML-to-Markdown conversion must be invariant under formatting
        # whitespace in the HTML source. All NavigableString text nodes
        # must have their interior formatting whitespace (newlines, tabs,
        # carriage returns) normalized to a single space before any
        # further processing. Structural whitespace from <br>, <p>, <li>,
        # block-level suffixes, and similar semantic elements is injected
        # by the tag handler configs, not the text nodes. Keeping
        # normalization in the NavigableString handler and ensuring all
        # process_strings callbacks downstream only react to structural
        # newlines guarantees this property.

        def escape_markdown(text: str) -> str:
            """Escape Markdown special characters in text."""
            return _MARKDOWN_ESCAPE_REGEX.sub(lambda match: Rf"\{match[0]}", text)

        if not isinstance(ele, Tag):
            if (
                isinstance(ele, NavigableString)
                and not isinstance(ele, PreformattedString)
                and not isinstance(ele.parent, BeautifulSoup)
            ):
                text = escape_markdown(ele) if escape else str(ele)
                # See the formatting-agnostic principle documented above.
                # Collapse formatting whitespace (indentation and line breaks
                # between tags) to spaces. Translate all ASCII formatting
                # whitespace to handle varying line-ending conventions across
                # HTML sources, then collapse consecutive regular spaces (from
                # indentation) into a single space, matching HTML rendering
                # semantics. Use a character-class regex instead of
                # str.split() to avoid treating non-breaking spaces (\xa0) as
                # whitespace — str.split() eliminates \xa0, but it must be
                # preserved as a meaningful content separator in source text.
                # Only strip ASCII whitespace, but NOT non-breaking spaces.
                text = text.translate(str.maketrans({c: " " for c in "\t\n\r\x0b\x0c"}))
                text = _COLLAPSE_SPACES_REGEX.sub(" ", text)
                if text and not all(c in "\t\n\r\x0b\x0c " for c in text):
                    return text.strip("\t\n\r\x0b\x0c ")
            return ""

        classes = frozenset(ele.get_attribute_list("class"))
        if {"mw-cite-backlink", "mw-editsection"} & classes:
            return ""

        if "reference" in classes:
            if refs:
                ref_str = "".join(ele.stripped_strings)
                if ref_content := _REF_CONTENT_REGEX.search(ref_str):
                    ref_content = ref_content[1]
                    return f"<sup>[{escape_markdown(f'[{ref_content}]')}]({_markdown_fragment(f'^ref-{ref_content}')})</sup>"
            else:
                return ""

        self._out_to_archive = out_to_archive
        self._redirect_map = redirect_map

        config = self._dispatch(ele, classes, list_stack=list_stack)
        if config is None:
            config = _HandlerConfig()

        joiner = config.joiner
        process_strings = config.process_strings
        if config.list_stack is not None:
            list_stack = config.list_stack

        if "hatnote" in classes:
            config.prefix = f"- {config.prefix.removesuffix('_')}"
            config.suffix = f"{config.suffix.removeprefix('_')}\n"
            original_process = process_strings

            def _hatnote_process(strings: str) -> str:
                """Process hatnote text by stripping leading newlines."""
                return original_process(strings).lstrip("\n")

            process_strings = _hatnote_process

        if {"sidebar-navbar", "navbar"} & classes:
            # Suppress comment wrapping for inner navbar/sidebar-navbar
            # elements that are already nested inside an outer sidebar-navbar
            # wrapper (prevents double-wrapping of VTE content).
            parent = ele.parent
            while parent is not None:
                parent_classes = parent.get_attribute_list("class")
                if "sidebar-navbar" in parent_classes or "navbar" in parent_classes:
                    break
                parent = parent.parent
            if parent is None:
                original_process = process_strings

                def process_strings_comment(strings: str) -> str:
                    """Wrap processed text in HTML comment markers."""
                    result = original_process(strings).strip()
                    return f"<!-- {result} --> " if result else result

                process_strings = process_strings_comment
                config.prefix = ""
                config.suffix = ""

        if (
            ele.name == "figure"
            or {
                "catlinks",
                "math_theorem",
                "portalbox",
                "tmulti",
                "unsolved",
            }
            & classes
        ):
            original_process = process_strings
            _catlinks = "catlinks" in classes

            def process_strings_blockquote(strings: str) -> str:
                """Collapse whitespace runs within blockquote content."""
                strings = original_process(strings)
                # Collapse whitespace runs within blockquotes to unwrap
                # HTML formatting newlines while preserving paragraph
                # breaks. For catlinks (category list), preserve single
                # newlines so list items stay on separate lines.
                if _catlinks:
                    strings = "\n\n".join(
                        "\n".join(" ".join(line.split()) for line in para.split("\n"))
                        for para in strings.split("\n\n")
                    )
                else:
                    strings = "\n\n".join(
                        " ".join(para.split()) for para in strings.split("\n\n")
                    )
                result = "".join(
                    f">{line.strip() and ' '}{line}"
                    for line in strings.strip().splitlines(keepends=True)
                )
                return _COLLAPSE_EMPTY_BLOCKQUOTE_RE.sub(">\n", result)

            config.suffix = "\n\n"
            process_strings = process_strings_blockquote

        def process_children() -> Iterator[Awaitable[str]]:
            """Process child elements concurrently using task groups."""
            nonlocal list_stack
            for child in ele.children:
                if (
                    list_stack
                    and list_stack[-1] >= 0
                    and isinstance(child, Tag)
                    and child.name == "li"
                ):
                    list_stack = (*list_stack[:-1], list_stack[-1] + 1)
                yield self.convert(
                    child,
                    out_to_archive=out_to_archive,
                    list_stack=list_stack,
                    escape=escape and ele.name not in {"code", "math"},
                    refs=refs,
                    redirect_map=redirect_map,
                )

        soon_values: list[SoonValue[str]] = []
        async with create_task_group() as tg:
            for coro in process_children():

                async def _run(c=coro) -> str:
                    """Await and return a single coroutine result."""
                    return await c

                soon_values.append(tg.soonify(_run)())

        strings = joiner.join(sv.value for sv in soon_values)
        if config.full_result:
            return process_strings(strings) or ""
        strings = process_strings(strings)
        return strings and f"{config.prefix}{strings}{config.suffix}"

    def _dispatch(
        self,
        ele: Tag,
        classes: Set[str],
        *,
        list_stack: tuple[int, ...],
    ) -> _HandlerConfig | None:
        """Dispatch to a handler for the given element."""
        if header_match := _HEADER_REGEX.match(ele.name):
            return self._handle_header(ele, classes, header_match)

        if ele.name == "a" and "mw-selflink" in classes:
            return self._handle_selflink(ele, classes)

        if (
            ele.name in _BOLD_OR_ITALIC
            or _BOLD_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
            or _ITALIC_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
        ):
            return self._handle_bold_italic(ele, classes)

        if {"mw-tmh-play", "oo-ui-buttonElement-button"} & classes:
            return self._handle_audio(ele, classes)

        if (
            ele.name == "img"
            and not {
                "mwe-math-fallback-image-display",
                "mwe-math-fallback-image-inline",
            }
            & classes
        ):
            return self._handle_image(ele, classes)

        if ele.name == "a" and "mw-file-description" not in classes:
            return self._handle_link(ele, classes)

        if ele.name == "ol":
            return self._handle_ol(ele, classes, list_stack)
        if ele.name == "ul" and "portalbox" in classes:
            return self._handle_portalbox(ele, classes)
        if ele.name == "ul":
            return self._handle_ul(ele, classes, list_stack)
        if ele.name == "li":
            return self._handle_li(ele, classes, list_stack)

        handler = getattr(self, f"_handle_{ele.name}", None)
        if handler is not None:
            return handler(ele, classes)

        return None

    # --- Tag handlers ---

    def _handle_br(self, ele: Tag, classes: Set[str]) -> _HandlerConfig | None:
        """Render a <br> tag as a newline."""

        def process(strings: str) -> str:
            """Append newline to strings."""
            return f"{strings}\n"

        return _HandlerConfig(process_strings=process)

    def _handle_header(
        self, ele: Tag, classes: Set[str], header_match
    ) -> _HandlerConfig:
        """Render a heading with Markdown # markers."""
        level = int(header_match[1] or "1")
        prefix = f"{'#' * level} "
        suffix = "\n\n"

        def process(strings: str) -> str:
            """Fix name casing in heading text."""
            return _fix_name_maybe(strings.strip(), names_map=self._names_map)

        return _HandlerConfig(prefix=prefix, suffix=suffix, process_strings=process)

    def _handle_selflink(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Render a self-link as a relative Markdown link."""
        # Resolve self-link anchor to a proper relative markdown link,
        # extracting the page title from the href attribute.
        href = str(ele.get("href", ""))
        wiki_prefix = f"{_WIKI_HOST_URL}/wiki/"
        if href.startswith(wiki_prefix):
            title = unquote(href[len(wiki_prefix) :].split("#")[0]).replace("_", " ")
        elif href.startswith("/wiki/"):
            title = unquote(href[6:].split("#")[0]).replace("_", " ")
        else:
            return _HandlerConfig()
        info = self._redirect_map.get(title, _RedirectInfo(to=title))
        to = info.to
        to_filename = _fix_name_maybe(
            to, replace_underscores=True, names_map=self._names_map
        )
        target = _markdown_link_target(
            to_filename,
            _fix_name_maybe(
                info.tofragment, replace_underscores=True, names_map=self._names_map
            ),
        )

        def process(strings: str) -> str:
            """Strip and flatten self-link display text."""
            return strings.strip().replace("\n", " <br/> ")

        return _HandlerConfig(
            prefix="[",
            suffix=f"]({target})",
            process_strings=process,
        )

    def _handle_bold_italic(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Render bold/italic text with Markdown emphasis markers."""
        bold = (
            ele.name in {"b", "strong"}
            or _BOLD_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
            and "mw-heading" not in classes
        )
        italic = ele.name in {"em", "i"} or _ITALIC_FONT_STYLE_REGEX.search(
            str(ele.get("style", ""))
        )
        bold_str = "__" if bold else ""
        italic_str = "_" if italic else ""
        prefix = f"{bold_str}{italic_str}"
        suffix = f"{italic_str}{bold_str}"
        # Sidebar title headers get <big> wrapping inside bold markers.
        if "sidebar-title-with-pretitle" in classes:
            prefix = f"{bold_str}<big>"
            suffix = f"</big>{bold_str}"

        if (
            ele.previous_sibling
            and isinstance(ele.previous_sibling, NavigableString)
            and ele.previous_sibling.rstrip(_MARKDOWN_SEPARATOR_CHARACTERS)
            == ele.previous_sibling
        ):
            prefix = f"{_MARKDOWN_SEPARATOR}{prefix}"
        if (
            ele.next_sibling
            and isinstance(ele.next_sibling, NavigableString)
            and ele.next_sibling.lstrip(_MARKDOWN_SEPARATOR_CHARACTERS)
            == ele.next_sibling
        ):
            suffix += _MARKDOWN_SEPARATOR

        config = _HandlerConfig(prefix=prefix, suffix=suffix, full_result=False)

        def process(strings: str) -> str:
            """Handle separator characters around bold/italic regions."""
            match = _PROCESS_STRINGS_BI_REGEX.match(strings)
            if not match:
                return strings
            config.prefix = f"{match[1]}{config.prefix}"
            config.suffix += match[3]
            return match[2]

        config.process_strings = process
        # Apply table cell processing for <th>/<td> elements so that bold
        # headers/cells receive proper cell content processing.
        if ele.name in _TD_OR_TH:
            original_process = config.process_strings

            def cell_process(strings: str) -> str:
                """Apply table cell processing for bold headers/cells."""
                return self._process_table_cell(original_process(strings))

            config.process_strings = cell_process
        return config

    def _handle_s(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Render <s> as strikethrough Markdown."""
        prefix, suffix = _tag_affixes("s")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _handle_sub(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Render <sub> as subscript Markdown."""
        prefix, suffix = _tag_affixes("sub")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _handle_sup(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Render <sup> as superscript Markdown."""
        prefix, suffix = _tag_affixes("sup")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _handle_u(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Render <u> as underline."""
        prefix, suffix = _tag_affixes("u")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _handle_big(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Render <big> text."""
        prefix, suffix = _tag_affixes("big")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    @staticmethod
    def _merge_header_rows(ele: Tag) -> None:
        """Merge consecutive header rows in <tbody> into a single row.

        Markdown pipe tables only support a single header row before the
        |---| separator. When a <tbody> has multiple consecutive rows at
        the start that are header rows (all-<th> rows plus any <td> rows
        before the first all-<th> row), they are collapsed into the last
        all-<th> row.
        """
        trs = [c for c in ele.children if isinstance(c, Tag) and c.name == "tr"]
        header_trs: list[Tag] = []
        target_tr: Tag | None = None
        seen_th = False

        for tr in trs:
            cells = [
                c for c in tr.children if isinstance(c, Tag) and c.name in _TD_OR_TH
            ]
            if not cells:
                continue
            all_th = all(c.name == "th" for c in cells)
            if all_th:
                header_trs.append(tr)
                target_tr = tr
                seen_th = True
            elif not seen_th:
                # Rows before the first all-<th> row (e.g. pretitle <td> rows)
                # are also part of the header block.
                header_trs.append(tr)
            else:
                break

        if target_tr is None or len(header_trs) <= 1:
            return

        # Merge each extra header row's cells into the target row.
        for tr in header_trs:
            if tr is target_tr:
                continue
            extra_cells = [
                c for c in tr.children if isinstance(c, Tag) and c.name in _TD_OR_TH
            ]
            target_cells = [
                c
                for c in target_tr.children
                if isinstance(c, Tag) and c.name in _TD_OR_TH
            ]

            for i, extra_cell in enumerate(extra_cells):
                if i < len(target_cells):
                    target_cell = target_cells[i]
                    children = list(extra_cell.children)
                    if children:
                        br = _bs4_new_element("<br/>")
                        target_cell.insert(0, br)
                        for child in reversed(children):
                            target_cell.insert(0, child.extract())

            tr.decompose()

    @staticmethod
    def _in_table_cell(ele: Tag) -> bool:
        """Check if element is nested inside a <td> or <th>."""
        return any(isinstance(p, Tag) and p.name in _TD_OR_TH for p in ele.parents)

    @staticmethod
    def _in_navbox(ele: Tag) -> bool:
        """Check if element is inside a navbox table."""
        return any(
            isinstance(p, Tag) and "navbox" in (p.get("class") or [])
            for p in ele.parents
        )

    def _handle_block_level(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Handle block-level elements with spacing suffix."""
        suffix = "\n\n" if self._in_table_cell(ele) else ""
        return _HandlerConfig(suffix=suffix)

    _handle_div = _handle_block_level
    _handle_dd = _handle_block_level
    _handle_dt = _handle_block_level

    def _handle_p(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Render a <p> paragraph with appropriate spacing."""

        def process(strings: str) -> str:
            """Collapse whitespace runs in paragraph text."""
            return " ".join(strings.split())

        in_table = self._in_table_cell(ele)
        prefix = "\n" if not in_table else ""
        suffix = "" if in_table else "\n\n"
        return _HandlerConfig(prefix=prefix, suffix=suffix, process_strings=process)

    def _handle_code(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Render inline <code> with backtick markers."""

        def process(strings: str) -> str:
            """Wrap code text in backtick delimiters."""
            delimiter = "`"
            while delimiter in strings:
                delimiter += "`"
            if strings.startswith("`") or strings.endswith("`"):
                strings = f" {strings} "
            return f"{delimiter}{strings}{delimiter}"

        return _HandlerConfig(process_strings=process)

    def _handle_math(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Render <math> elements with LaTeX delimiters."""
        prefix = suffix = ""
        if alt_text := ele.get("alttext"):
            alt_text = str(alt_text).strip()
            for _prefix in (R"{\displaystyle", R"{\textstyle"):
                if alt_text.startswith(_prefix):
                    alt_text = alt_text.removeprefix(_prefix).lstrip()
                    alt_text = alt_text.removesuffix(R"}")
                    break
            if alt_text.endswith(R"\ "):
                alt_text += "{}"
            else:
                alt_text = alt_text.rstrip()
            alt_text = (
                alt_text.replace(R":@:", R": @ :")
                .replace(R"?@?", R"? @ ?")
                .replace(R"{@{", R"{ @ {")
                .replace(R"}@}", R"} @ }")
            )
            while (
                alt_text_2 := alt_text.replace(R"{{", "{ {").replace(R"}}", "} }")
            ) != alt_text:
                alt_text = alt_text_2

            is_not_separate_paragraph = (
                (parent := ele.parent)
                and (parent := parent.parent)
                and (parent := parent.parent)
                and len(parent) > 1
            )
            is_inline = (parent := ele.parent) and "inline" in str(
                parent.get("class", "")
            )
            inline = is_not_separate_paragraph and is_inline

            prefix, suffix = "$" if inline else " $$", "$" if inline else "$$"

            if inline:
                for char in ".,":
                    if alt_text.endswith(R"\,"):
                        continue
                    if alt_text.endswith(char):
                        suffix += alt_text[-1]
                        alt_text = alt_text[:-1]
                alt_text = alt_text.rstrip()

            ele.clear()
            ele.append(alt_text)

        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _list_prefix_suffix(
        self,
        ele: Tag,
        classes: Set[str],
        list_stack: tuple[int, ...],
        *,
        references_override: bool = False,
    ) -> tuple[str, str]:
        """Compute prefix/suffix for list items based on nesting level."""
        if self._in_table_cell(ele):
            is_sub_list = any(
                isinstance(p, Tag) and p.name == "li" for p in ele.parents
            )
            if is_sub_list or (references_override and "references" in classes):
                if references_override and "references" in classes:
                    prefix = ""
                elif list_stack:
                    prefix = "\n"
                else:
                    prefix = "\n\n"
                suffix = ""
            else:
                prefix = ""
                suffix = ""
        else:
            if references_override and "references" in classes:
                prefix = ""
            elif list_stack:
                prefix = "\n"
            else:
                prefix = "\n\n"
            suffix = "\n\n"
        return prefix, suffix

    def _handle_ol(
        self, ele: Tag, classes: Set[str], list_stack: tuple[int, ...]
    ) -> _HandlerConfig:
        """Handle ordered list <ol> elements."""
        prefix, suffix = self._list_prefix_suffix(
            ele, classes, list_stack, references_override=True
        )
        return _HandlerConfig(
            prefix=prefix,
            suffix=suffix,
            list_stack=(*list_stack, 0),
        )

    def _handle_portalbox(self, ele: Tag, classes: Set[str]) -> _HandlerConfig | None:
        """Handle portal box elements as inline content."""
        if ele.name != "ul":
            return None

        # Portalbox items are inline (icon + portal caption on one
        # line), so strip list prefixes and join with a single space.
        def process(strings: str) -> str:
            """Strip list prefixes and join portal items inline."""
            lines = [line.strip() for line in strings.split("\n")]
            parts = [
                line.removeprefix("- ").removeprefix("* ") for line in lines if line
            ]
            return " ".join(parts)

        return _HandlerConfig(process_strings=process)

    def _handle_ul(
        self, ele: Tag, classes: Set[str], list_stack: tuple[int, ...]
    ) -> _HandlerConfig:
        """Handle unordered list <ul> elements."""
        prefix, suffix = self._list_prefix_suffix(ele, classes, list_stack)
        return _HandlerConfig(
            prefix=prefix,
            suffix=suffix,
            list_stack=(*list_stack, -1),
        )

    def _handle_li(
        self, ele: Tag, classes: Set[str], list_stack: tuple[int, ...]
    ) -> _HandlerConfig:
        """Handle list item <li> elements."""
        item = list_stack[-1] if list_stack else -1
        # Suppress suffix in table cells when the <li> contains
        # a sub-list, to prevent the sub-list's last item \n from
        # combining with this <li>'s suffix to create \n\n.
        if self._in_table_cell(ele) and ele.find(("ul", "ol")) is not None:
            li_suffix = ""
        else:
            li_suffix = "\n"
        if item >= 1:
            prefix = f"{_LIST_INDENT * (len(list_stack) - 1)}{item}. "
            if str(ele.get("id", "")).startswith("cite_"):

                def process(strings: str, item: int = item) -> str:
                    """Process citation list items with anchor markers."""
                    strings = strings.lstrip("\t\n\r\x0b\x0c \xa0")
                    try:
                        idx = strings.index("\n")
                    except ValueError:
                        idx = len(strings)
                    return f'{strings[:idx]} <a id="^ref-{item}"></a>^ref-{item}{strings[idx:].rstrip()}'

                return _HandlerConfig(
                    prefix=prefix, suffix=li_suffix, process_strings=process
                )
            return _HandlerConfig(prefix=prefix, suffix=li_suffix)
        else:
            return _HandlerConfig(
                prefix=f"{_LIST_INDENT * (len(list_stack) - 1)}- ",
                suffix=li_suffix,
            )

    def _handle_cite(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Handle <cite> citation elements."""
        prefix = ""
        if id := ele.get("id"):
            id = str(id).replace("_", " ")
            prefix = f'<a id="{id}"></a> '
        return _HandlerConfig(prefix=prefix)

    def _handle_tbody(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Handle <tbody> table body elements."""
        self._normalize_table_cells(ele)
        self._merge_header_rows(ele)
        return _HandlerConfig(prefix="\n", suffix="\n\n")

    def _handle_thead(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Handle <thead> table head elements."""
        self._normalize_table_cells(ele)
        return _HandlerConfig(prefix="\n", suffix="\n\n")

    @staticmethod
    def _normalize_table_cells(ele: Tag) -> None:
        """Normalize table cell layout for consistent column count."""
        for tdh in tuple(ele.find_all(_TD_OR_TH)):
            assert isinstance(tdh, Tag)
            col_span = str(tdh.get("colspan", "1"))
            try:
                col_span = int(col_span)
            except ValueError:
                pass
            else:
                tdh["colspan"] = "1"
                navbox = any(
                    isinstance(p, Tag) and "navbox" in (p.get("class") or [])
                    for p in tdh.parents
                )
                for _ in range(1, col_span):
                    new_tdh = copy(tdh)
                    # Strip style from cloned cells so split cells
                    # don't inherit alignment from the original.
                    if "style" in new_tdh.attrs:
                        del new_tdh.attrs["style"]
                    new_tdh.clear()
                    # Navbox tables use the first column for group labels,
                    # so insert empty clone before the original content cell.
                    if navbox:
                        tdh.insert_before(new_tdh)
                    else:
                        tdh.insert_after(new_tdh)
                # Strip text-align from the original cell after navbox
                # colspan splitting, since its alignment was for the
                # colspan'd span and does not reflect column alignment.
                if navbox and "style" in tdh.attrs:
                    style = str(tdh.get("style", ""))
                    tdh["style"] = re.sub(
                        r"\btext-align\s*:\s*[^;]+;?\s*",
                        "",
                        style,
                    ).strip()
                    if not tdh["style"]:
                        del tdh.attrs["style"]
        for tdh in tuple(ele.find_all(("th", "td"))):
            assert isinstance(tdh, Tag)
            row_span = str(tdh.get("rowspan", "1"))
            try:
                row_span = int(row_span)
            except ValueError:
                pass
            else:
                if (current_row := tdh.parent) is not None:
                    col_idx = current_row.index(tdh)
                    tdh["rowspan"] = "1"
                    for _ in range(1, row_span):
                        if not isinstance(current_row := current_row.next_sibling, Tag):
                            break
                        new_tdh = copy(tdh)
                        new_tdh.clear()
                        current_row.insert(col_idx, new_tdh)

    def _handle_tr(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Handle <tr> table row elements."""
        joiner = " | "
        prefix = "| "
        suffix = " |\n"

        # Strip whitespace-only text nodes to prevent phantom empty cells
        # from newlines/spaces between <td>/<th> tags.
        for child in list(ele.children):
            if isinstance(child, NavigableString) and not child.strip():
                child.extract()

        # Detect navbox context for column layout adjustments.
        is_navbox = self._in_navbox(ele)

        # Count only actual th/td tags, not whitespace text nodes.
        tag_cells = [
            child
            for child in ele.children
            if isinstance(child, Tag) and child.name in _TD_OR_TH
        ]

        # Account for colspan when counting columns.
        total_colspan = sum(int(str(c.get("colspan", "1"))) for c in tag_cells)

        def filter_cells(strings: str) -> str:
            """Filter and pad table cells to match column count."""
            cells = [s.strip() for s in strings.split(" | ")]
            if not is_navbox:
                cells = [c for c in cells if c]
            # Pad with empty cells to match the total column count
            # (needed when a cell has colspan > 1).
            while len(cells) < total_colspan:
                cells.append("")
            result = " | ".join(cells)
            # Rows may have an empty first cell (e.g. from a
            # colspan-split in navboxes). The row prefix "| " followed
            # by the " | " joiner on an empty cell produces "|  |"
            # (two spaces between pipes). Collapse the leading space
            # from the joiner when the first cell is empty to get
            # "| |".
            if cells and not cells[0] and result.startswith(" |"):
                result = "|" + result[2:]
            return result

        if tag_cells and all(child.name == "th" for child in tag_cells):
            # Check if table uses first-column headers (<th scope="row">).
            table = ele.find_parent("table")
            has_scope_row = (
                table is not None and table.find("th", scope="row") is not None
            )

            # Build alignment markers based on each cell's text-align style.
            # GFM markers: --- (left/default), :-- (explicit left),
            # :-: (center), --: (right). Minimum 3 characters including colons.
            alignments: list[str] = []
            for i, child in enumerate(tag_cells):
                style = str(child.get("style", ""))
                ta_match = _TEXT_ALIGN_REGEX.search(style)
                if ta_match:
                    ta = ta_match[1]
                    if ta == "center":
                        alignments.append(":-:")
                    elif ta == "right":
                        alignments.append("--:")
                    else:
                        alignments.append(":--")
                else:
                    alignments.append("---")
            # Override first column to right-aligned when the table uses
            # first-column headers (detected by <th scope="row">).
            if has_scope_row and alignments:
                alignments[0] = "--:"
            suffix += f"| {' | '.join(alignments)} |\n"
        else:
            for child in ele.children:
                if isinstance(child, Tag) and child.name == "th":
                    # Skip <b> wrapping if <th> already has font-weight:bold
                    # styling to avoid doubled bold markers.
                    if not _BOLD_FONT_STYLE_REGEX.search(str(child.get("style", ""))):
                        new_b = _bs4_new_element("<b></b>")
                        assert isinstance(new_b, Tag)
                        for child_child in child.contents[:]:
                            new_b.append(child_child.extract())
                        child.append(new_b)
        return _HandlerConfig(
            joiner=joiner,
            prefix=prefix,
            suffix=suffix,
            process_strings=filter_cells,
        )

    def _handle_td(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Dispatch <td> table cell elements."""
        return _HandlerConfig(process_strings=self._process_table_cell)

    def _handle_th(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Dispatch <th> table header cell elements."""
        if "sidebar-title-with-pretitle" in classes:
            return _HandlerConfig(
                prefix="<big>",
                suffix="</big>",
                process_strings=self._process_table_cell,
            )
        return _HandlerConfig(process_strings=self._process_table_cell)

    @staticmethod
    def _process_table_cell(strings: str) -> str:
        """Process content of a table cell by normalizing whitespace and pipes."""
        strings = strings.strip()
        strings = _CONSECUTIVE_NEWLINES_REGEX.sub("\n\n", strings)
        strings = _CONSECUTIVE_LEADING_WHITESPACES_REGEX.sub(
            lambda match: match[0].replace(" ", "&nbsp;").replace("\t", "&emsp;"),
            strings,
        )
        strings = strings.replace("\xa0", " ")
        strings = strings.replace("| |", "|")
        strings = _TABLE_IN_TABLE_HEADER_REGEX.sub(
            lambda match: f"|{match[1]} <p> ", strings
        )
        strings = strings.replace("|\n|", " <p> ")
        strings = _TABLE_IN_TABLE_LEADING_VERTICAL_REGEX.sub(
            lambda match: match[0][: -len("|")], strings
        )
        strings = _TABLE_IN_TABLE_TRAILING_VERTICAL_REGEX.sub(
            lambda match: match[0][len("|") :], strings
        )
        strings = strings.replace("|", "&#124;")
        strings = strings.strip()
        strings = strings.replace("\n\n", " <br/> <br/> ")
        strings = strings.replace("\n", " <br/> ")
        return strings

    def _process_archive_url(self, src: str) -> str:
        """Resolve a media URL to a local archive path."""
        src_url = _WIKI_HOST_URL.join(URL(str(src)))
        src_url_str = str(src_url)
        for regex, formats in _ARCHIVE_REGEXES.items():
            if not (match := regex.search(src_url.human_repr())):
                continue
            to_archive = unquote(match[1])
            self._out_to_archive.add(formats[0].format(to_archive))
            src_url_str = quote(formats[1].format(to_archive.replace("_", " ")))
        return src_url_str

    def _handle_audio(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Handle <audio> media elements."""
        if src := ele.get("href"):

            def process(strings: str) -> str:
                """Generate Markdown link for audio file."""
                src_url_str = self._process_archive_url(str(src))
                embed = "!" if {"mw-tmh-player"} & classes else ""
                return f"{embed}[{strings.strip()}]({src_url_str})"

            return _HandlerConfig(
                suffix="" if self._in_table_cell(ele) else "\n\n",
                process_strings=process,
            )
        return _HandlerConfig()

    def _handle_image(self, ele: Tag, classes: Set[str]) -> _HandlerConfig:
        """Handle <img> image elements with download and link."""
        if src := ele.get("src"):

            def process(strings: str) -> str:
                """Generate Markdown image syntax with alt text."""
                src_url_str = self._process_archive_url(str(src))
                alt = str(ele.get("alt", "")).strip()
                if not alt:
                    alt = self._fallback_alt(ele)
                    # Level-2 (Commons description) is pre-converted
                    # Markdown — do not escape again.
                    filename = _get_image_filename(ele)
                    if not (filename and f"File:{filename}" in self._image_metadata):
                        # Level-3 (filename) is plain text — escape.
                        alt = _MARKDOWN_ESCAPE_REGEX.sub(lambda m: Rf"\{m[0]}", alt)
                else:
                    # Level-1 (HTML alt attribute) is plain text.
                    alt = _MARKDOWN_ESCAPE_REGEX.sub(lambda m: Rf"\{m[0]}", alt)
                return f"{strings}![{alt}]({src_url_str})"

            return _HandlerConfig(
                suffix="" if self._in_table_cell(ele) else "\n\n",
                process_strings=process,
            )
        return _HandlerConfig()

    def _fallback_alt(self, ele: Tag) -> str:
        """Compute alt text fallback for an ``<img>`` element.

        Uses Wikimedia API descriptions first, then falls back to the plain filename.
        """
        filename = _get_image_filename(ele)
        if not filename:
            return ""
        file_title = f"File:{filename}"
        if desc := self._image_metadata.get(file_title, ""):
            return desc
        return file_title

    def _handle_link(self, ele: Tag, classes: Set[str]) -> _HandlerConfig | None:
        """Handle <a> link elements."""
        if (title := ele.get("title")) and title not in _BAD_TITLES:
            title = str(title)
            if "new" in classes:
                title = title.removesuffix(_PAGE_DOES_NOT_EXIST_SUFFIX)
            href = str(ele.get("href", ""))
            to_fragment = href.split("#", 1)[-1] if "#" in href else ""

            info = self._redirect_map.get(title, _RedirectInfo(to=title))
            to = info.to
            if not to_fragment:
                to_fragment = info.tofragment

            def _process_link_text(s: str) -> str:
                """Strip and flatten link display text."""
                return s.strip().replace("\n", " <br/> ")

            if any(to.startswith(prefix) for prefix in _IGNORED_NAME_PREFIXES):
                pass
            elif url_format := next(
                (
                    (format, to[len(prefix) :])
                    for prefix, format in _PRESERVED_PAGE_PREFIXES.items()
                    if to.startswith(prefix)
                ),
                None,
            ):
                return _HandlerConfig(
                    prefix="[",
                    suffix=f"]({url_format[0].format(f'{quote(url_format[1])}{to_fragment and "#"}{quote(to_fragment, safe="")}')})",
                    process_strings=_process_link_text,
                )
            elif "extiw" in classes:
                lang_code, extiw_page = to.split(":", 1)
                lang_code = str(convert(lang_code, to="ISO3")).casefold()
                from_filename = _fix_name_maybe(
                    extiw_page, replace_underscores=True, names_map=self._names_map
                )

                return _HandlerConfig(
                    prefix="[",
                    suffix=f"](../{lang_code}/{_markdown_link_target(from_filename, _fix_name_maybe(to_fragment, replace_underscores=True, names_map=self._names_map))})",
                    process_strings=_process_link_text,
                )
            else:
                from_filename, to_filename = (
                    _fix_name_maybe(
                        title, replace_underscores=True, names_map=self._names_map
                    ),
                    _fix_name_maybe(
                        to, replace_underscores=True, names_map=self._names_map
                    ),
                )

                config = _HandlerConfig(
                    prefix="[",
                    suffix=f"]({_markdown_link_target(from_filename, _fix_name_maybe(to_fragment, replace_underscores=True, names_map=self._names_map))})",
                    process_strings=_process_link_text,
                )
                from_filename, to_filename = (
                    _fix_filename(from_filename),
                    _fix_filename(to_filename),
                )
                if from_filename != to_filename:
                    redirect_file = (
                        self._converted_wiki_lang_dir / f"{from_filename}.md"
                    )
                    if not redirect_file.exists():
                        with _with_cwd(self._converted_wiki_lang_dir):
                            with suppress(FileExistsError):
                                symlink(
                                    f"{to_filename}.md",
                                    redirect_file.relative_to(
                                        self._converted_wiki_lang_dir
                                    ),
                                    target_is_directory=False,
                                )
                        with _with_cwd(self._converted_wiki_dir):
                            with suppress(FileExistsError):
                                symlink(
                                    redirect_file.relative_to(self._converted_wiki_dir),
                                    f"{from_filename}.md",
                                    target_is_directory=False,
                                )
                return config
        elif href := ele.get("href"):
            href = str(href)
            if href.startswith(f"{_WIKI_HOST_URL}/wiki/") and "#" in href:
                href = _markdown_fragment(
                    _fix_name_maybe(
                        href[href.index("#") + 1 :],
                        replace_underscores=True,
                        names_map=self._names_map,
                    )
                )

            def process(strings: str) -> str:
                """Collapse whitespace in anchor text."""
                return " ".join(strings.split())

            # Wrap authority-control edit icon links in HTML comments.
            # Detect by checking for parent <span typeof="mw:File/Frameless">
            # inside the authority-control navbox.
            if any(
                isinstance(p, Tag) and p.get("typeof") == "mw:File/Frameless"
                for p in ele.parents
            ) and any(
                isinstance(p, Tag) and "authority-control" in (p.get("class") or [])
                for p in ele.parents
            ):
                config = _HandlerConfig(
                    prefix="<!-- [",
                    suffix=f"]({href}) -->",
                    process_strings=process,
                )
            else:
                config = _HandlerConfig(
                    prefix="[", suffix=f"]({href})", process_strings=process
                )
            return config

        return None


"""Regex matching GFM table separator cells (e.g. ``---``, ``:--``, ``--:``, ``:-:``)."""
_SEPARATOR_CELL_RE: Pattern[str] = compile(r":?-+:?")


def _is_separator_cell(cell: str) -> bool:
    """Check if a table cell is a GFM separator (e.g. ---, :--, --:, :-:)."""
    return bool(_SEPARATOR_CELL_RE.fullmatch(cell)) and len(cell) >= 3


def _get_separator_alignment(cell: str) -> str:
    """Extract the GFM alignment marker from a separator cell."""
    if cell.startswith(":") and cell.endswith(":"):
        return ":-:"
    if cell.endswith(":"):
        return "--:"
    if cell.startswith(":"):
        return ":--"
    return "---"


def _format_separator_cell(width: int, alignment: str) -> str:
    """Build a separator cell padded to the given column width."""
    width = max(width, 3)
    if alignment == "---":
        return "-" * width
    if alignment == ":--":
        return ":" + "-" * (width - 1)
    if alignment == "--:":
        return "-" * (width - 1) + ":"
    # :-:
    return ":" + "-" * (width - 2) + ":"


# Characters that are zero-width in terminal display but count as width 1 in
# Python ``len()``.  MD060 (table-column-style) fires when these skew column
# widths.  Strip them from table cell content before computing widths.
_ZERO_WIDTH_CHARS_RE = re.compile("[\u200b\u200c\u200d\u2060\ufeff]")


def _parse_table_row(line: str) -> list[str] | None:
    """Parse a pipe-table row into cell contents.  Returns None if the line
    is not a valid table row."""
    line = line.rstrip("\n")
    if not (line.startswith("|") and line.endswith("|")):
        return None
    inner = line[1:-1]  # strip outer pipes
    return [_ZERO_WIDTH_CHARS_RE.sub("", p.strip()) for p in inner.split(" | ")]


def _pad_table_block(lines: list[str]) -> list[str]:
    """Reformat a pipe-table block with columns padded to the widest cell per
    column.  Expects at least 2 rows including one separator row."""
    if len(lines) < 2:
        return lines

    parsed: list[list[str]] = []
    sep_indices: list[int] = []
    for i, line in enumerate(lines):
        cells = _parse_table_row(line)
        if cells is None:
            return lines  # not a valid table — pass through unchanged
        parsed.append(cells)
        if len(cells) > 0 and all(_is_separator_cell(c) for c in cells):
            sep_indices.append(i)

    if not sep_indices:
        return lines

    ncols = max(len(cells) for cells in parsed)

    # Get alignment per column from the first separator row.
    alignments: list[str] = []
    for j in range(ncols):
        sep_row_idx = sep_indices[0]
        sep_cell = parsed[sep_row_idx][j] if j < len(parsed[sep_row_idx]) else ""
        alignments.append(_get_separator_alignment(sep_cell))

    # Column width = max content width across all content rows (not separators).
    col_widths = [0] * ncols
    for i, cells in enumerate(parsed):
        if i in sep_indices:
            continue
        for j in range(len(cells)):
            col_widths[j] = max(col_widths[j], len(cells[j]))

    # Ensure every column is at least 3 characters wide (GFM minimum).
    col_widths = [max(w, 3) for w in col_widths]

    result: list[str] = []
    for i, cells in enumerate(parsed):
        padded = list(cells)
        while len(padded) < ncols:
            padded.append("")

        if i in sep_indices:
            sep_cells = [
                _format_separator_cell(col_widths[j], alignments[j])
                for j in range(ncols)
            ]
            result.append("| " + " | ".join(sep_cells) + " |")
        else:
            data_cells = [
                _JUSTIFY_MAP[alignments[j]](padded[j], col_widths[j])
                for j in range(ncols)
            ]
            result.append("| " + " | ".join(data_cells) + " |")

    return result


def _pad_table_blocks(text: str) -> str:
    """Find all pipe-table blocks in *text* and pad columns to the widest
    content per column."""
    lines = text.split("\n")
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("|") and line.endswith("|"):
            block: list[str] = [line]
            i += 1
            while (
                i < len(lines) and lines[i].startswith("|") and lines[i].endswith("|")
            ):
                block.append(lines[i])
                i += 1
            result.extend(_pad_table_block(block))
        else:
            result.append(line)
            i += 1
    return "\n".join(result)


async def wiki_html_to_plaintext(
    ele: PageElement,
    *,
    out_to_archive: MutableSet[str],
    list_stack: tuple[int, ...] = (),
    escape: bool = True,
    refs: bool,
    redirect_map: Mapping[str, _RedirectInfo],
    converter: WikiHtmlConverter | None = None,
    image_metadata: Mapping[str, str] | None = None,
) -> str:
    """Convert a Wikipedia HTML element tree to a Markdown string.

    Parameters
    ----------
    converter:
        Optional pre-configured converter instance (e.g. with custom
        paths for testing). Creates a default one if not provided.
    image_metadata:
        Pre-fetched image description metadata (``File:XXX`` → description).
    """
    if converter is None:
        converter = WikiHtmlConverter(image_metadata=image_metadata)
    result = await converter.convert(
        ele,
        out_to_archive=out_to_archive,
        list_stack=list_stack,
        escape=escape,
        refs=refs,
        redirect_map=redirect_map,
    )
    # Replace non-breaking spaces with regular spaces (residues from
    # citation spans, HTML &nbsp; in list items, etc.).
    result = result.replace("\xa0", " ")
    # Pad table columns to the widest content per column.
    result = _pad_table_blocks(result)
    # Insert MD028 suppression comments between adjacent blockquote blocks.
    result = re.sub(
        r"(^(?:>[^\n]*\n)+)\n+(^>(?:[^\n]*\n?)+)",
        r"\1\n<!-- markdownlint MD028 -->\n\n\2",
        result,
        flags=re.MULTILINE,
    )
    # Collapse excessive blank lines.
    result = re.sub(r"\n{3,}", r"\n\n", result)
    return result


async def run_pipeline(
    html: Tag,
    *,
    session: ClientSession | None = None,
    redirect_map: MutableMapping[str, _RedirectInfo] | None = None,
    image_metadata: Mapping[str, str] | None = None,
    cache_path: PurePath | None = None,
    names_map: Mapping[str, str] | None = None,
    wiki_dir: PathlibPath | None = None,
    wiki_lang_dir: PathlibPath | None = None,
    refs: bool = True,
) -> tuple[str, set[str]]:
    """Run the full conversion pipeline on parsed Wikipedia HTML.

    Every external-data dependency can be overridden, making it possible
    to test the full pipeline without HTTP requests or filesystem access.

    Parameters
    ----------
    html:
        Parsed HTML tree to convert.
    session:
        ``aiohttp.ClientSession`` to use for API calls. If not provided and
        needed (when *redirect_map* or *image_metadata* is ``None``), one is
        created automatically.
    redirect_map:
        Pre-resolved redirect map. If provided, skips all redirect
        resolution and session creation.
    image_metadata:
        Pre-resolved image description metadata (``File:XXX`` → description).
        If provided, skips the image-metadata API calls.
    cache_path:
        Alternative path for the redirect cache file.
        Defaults to ``_REDIRECT_CACHE_PATH``.
    names_map:
        Alternative filename rename map. Passed to ``WikiHtmlConverter``.
        ``None``, the module-level ``_NAMES_MAP`` is used.
    wiki_dir:
        Alternative wiki root directory.
        Defaults to ``_CONVERTED_WIKI_DIRECTORY``.
    wiki_lang_dir:
        Alternative language subdirectory.
        Defaults to ``_CONVERTED_WIKI_LANGUAGE_DIRECTORY``.
    refs:
        Whether to include reference citations in the output.

    Returns
    -------
    tuple[str, set[str]]
        ``(output_text, set_of_filenames_to_archive)``.
    """
    out_to_archive = set[str]()

    def _make_converter() -> WikiHtmlConverter:
        """Create a converter for a specific Wikipedia language."""
        return WikiHtmlConverter(
            converted_wiki_dir=wiki_dir or _CONVERTED_WIKI_DIRECTORY,
            converted_wiki_lang_dir=wiki_lang_dir or _CONVERTED_WIKI_LANGUAGE_DIRECTORY,
            image_metadata=image_metadata or {},
            names_map=names_map,
        )

    # If all data is already provided, skip session/API entirely.
    if redirect_map is not None and image_metadata is not None:
        converter = _make_converter()
        output = await wiki_html_to_plaintext(
            html,
            out_to_archive=out_to_archive,
            redirect_map=redirect_map,
            refs=refs,
            converter=converter,
        )
        output = output.replace("\xa0", " ").replace("\u200a", "&hairsp;").strip()
        return output, out_to_archive

    # Need a session for API calls \u2014 create one if not provided.
    if session is None:
        async with ClientSession(
            connector=TCPConnector(limit_per_host=_MAX_CONCURRENT_REQUESTS_PER_HOST),
            headers={
                "Accept-Encoding": "gzip",
                "User-Agent": USER_AGENT,
            },
        ) as created_session:
            return await run_pipeline(
                html,
                session=created_session,
                redirect_map=redirect_map,
                image_metadata=image_metadata,
                cache_path=cache_path,
                names_map=names_map,
                wiki_dir=wiki_dir,
                wiki_lang_dir=wiki_lang_dir,
                refs=refs,
            )

    # Resolve redirects if needed.
    if redirect_map is None:
        titles = _collect_link_titles(html)
        cache = _load_redirect_cache(cache_path=cache_path)
        redirect_map = await _resolve_redirects(
            session, titles, cache, cache_path=cache_path
        )

    # Resolve image metadata if needed.
    if image_metadata is None:
        image_metadata = await _resolve_image_metadata(
            session, _collect_image_filenames(html)
        )

    # Convert.
    converter = _make_converter()
    output = await wiki_html_to_plaintext(
        html,
        out_to_archive=out_to_archive,
        redirect_map=redirect_map,
        refs=refs,
        converter=converter,
    )
    output = output.replace("\xa0", " ").replace("\u200a", "&hairsp;").strip()
    return output, out_to_archive


async def main() -> None:
    """Parse CLI arguments and orchestrate the HTML-to-Markdown conversion pipeline."""
    parser = argparse.ArgumentParser(
        description="Convert Wikipedia HTML to Markdown. Reads from stdin by default."
    )
    parser.add_argument(
        "--no-refs",
        action="store_true",
        help="Omit reference citations.",
    )
    parser.add_argument(
        "--output-mode",
        "-m",
        choices=["clipboard", "stdout", "stderr", "append"],
        default="clipboard",
        help="Output mode (default: clipboard).",
    )
    parser.add_argument(
        "--output-file",
        "-f",
        type=PathlibPath,
        help="File path for append output mode.",
    )
    parser.add_argument(
        "--input-file",
        "-i",
        type=PathlibPath,
        default="-",
        help="Read HTML from file instead of stdin (default: stdin).",
    )
    parser.add_argument(
        "--clipboard",
        "-c",
        action="store_true",
        help="Read HTML from system clipboard (overrides --input-file).",
    )
    args = parser.parse_args()
    refs = not args.no_refs

    if args.output_mode == "append" and args.output_file is None:
        parser.error("--output-file is required when --output-mode is append.")

    basicConfig(level=INFO)
    _logger.info("Starting Wikipedia HTML to Markdown conversion")

    if args.clipboard:
        html_text = paste_html()
        if not isinstance(html_text, str):
            msg = (
                f"Clipboard does not contain HTML text (got {type(html_text).__name__})"
            )
            raise TypeError(msg)
    else:
        source = stdin if args.input_file == PathlibPath("-") else open(args.input_file)
        with source:
            html_text = source.read()

    html = BeautifulSoup(html_text, "html.parser")

    output, out_to_archive = await run_pipeline(html, refs=refs)

    if out_to_archive:
        _logger.info("Archiving %d media files", len(out_to_archive))
        downloaded_so_far = 0

        def _on_progress(current: int, total: int) -> None:
            """Report conversion progress for status output."""
            nonlocal downloaded_so_far
            if current - downloaded_so_far >= 5:
                _logger.info("Archiving progress: %d/%d", current, total)
                downloaded_so_far = current

        result: ArchiveResult = await pyarchivist_archive(
            Args(
                inputs=tuple(out_to_archive),
                dest=Path("../archives/Wikimedia Commons/"),
                index=Path("../archives/Wikimedia Commons/index.md"),
                ignore_individual_errors=True,
                skip_existing=True,
                request_timeout=30.0,
                progress_callback=_on_progress,
            )
        )
        if result.errors:
            for err in result.errors:
                _logger.warning(
                    "Archive error [%s] %s: %s",
                    err.phase,
                    err.title,
                    err.message,
                )
        _logger.info(
            "Archiving done: %d downloaded, %d skipped",
            result.downloaded,
            result.skipped,
        )

    match args.output_mode:
        case "clipboard":
            print(output)
            clip_copy(output)
            print(":)")
        case "stdout":
            print(output)
        case "stderr":
            print(output, file=stderr)
        case "append":
            with open(args.output_file, "a") as f:
                f.write(output)
                f.write("\n")


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
