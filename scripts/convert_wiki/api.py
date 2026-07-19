"""MediaWiki API interaction for redirect resolution and image metadata.

Provides functions for batch-resolving Wikipedia redirects and fetching
image description metadata from Wikimedia Commons.
"""

from collections.abc import MutableMapping
from contextlib import suppress
from datetime import datetime, timezone
from json import JSONDecodeError
from os import replace as os_replace
from pathlib import Path, PurePath

import anyio
from aiohttp import ClientSession
from bs4 import BeautifulSoup, Tag
from yarl import URL

from . import config as _cfg
from .types import _RedirectInfo
from .utils import _get_image_filename

"""Exported names from this module."""
__all__ = ()

"""Type alias for the API response body of a MediaWiki ``action=query``
request, to be unpacked before type narrowing."""
_ApiResponse = dict


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
        if title in _cfg._BAD_TITLES:
            continue
        if any(title.startswith(prefix) for prefix in _cfg._PRESERVED_PAGE_PREFIXES):
            continue
        titles.add(title)
    return titles


def _collect_image_filenames(html: Tag) -> set[str]:
    """Collect all image file titles from ``<img>`` elements in the HTML tree.

    Returns a set of ``File:XXX`` titles (e.g. ``File:Modernphysicsfields.svg``).
    """
    filenames: set[str] = set()
    for img in html.find_all("img"):
        if filename := _get_image_filename(img):
            filenames.add(f"File:{filename}")
    return filenames


def _load_redirect_cache(
    cache_path: PurePath,
) -> dict[str, _RedirectInfo]:
    """Load the redirect cache, respecting TTL.

    Parameters
    ----------
    cache_path:
        Path to the cache JSON file.
    """
    path = cache_path
    try:
        with open(path, "r", encoding="UTF-8") as f:
            data = _cfg._json_load(f)
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
            if now - cached_at > _cfg._CACHE_TTL:
                continue  # expired
            unpacked[k] = _RedirectInfo(
                to=to, tofragment=tofragment, cached_at=cached_at_str
            )
        return unpacked
    except (FileNotFoundError, JSONDecodeError, OSError):
        return {}


def _save_redirect_cache(
    cache: MutableMapping[str, _RedirectInfo],
    cache_path: PurePath,
) -> None:
    """Atomically save the redirect cache.

    Parameters
    ----------
    cache:
        Redirect info by page title.
    cache_path:
        Path to the cache JSON file.
    """
    data = {
        k: {
            "to": v.to,
            "tofragment": v.tofragment,
            "cached_at": v.cached_at or datetime.now(timezone.utc).isoformat(),
        }
        for k, v in cache.items()
    }
    resolved_path = Path(cache_path)
    tmp = resolved_path.with_suffix(".tmp")
    try:
        with open(tmp, "w", encoding="UTF-8") as f:
            _cfg._json_dump(data, f, ensure_ascii=False, indent=2)
        os_replace(tmp, resolved_path)
    except BaseException:
        with suppress(FileNotFoundError):
            Path(tmp).unlink()
        raise


async def _api_request(
    session: ClientSession,
    params: dict[str, str | int],
    host: URL = _cfg._WIKI_HOST_URL,
) -> _ApiResponse:
    """Make a MediaWiki API request with retry on HTTP 429."""
    url = URL.build(
        scheme=host.scheme,
        host=str(host.host),
        path="/w/api.php",
        query=params,  # pyright: ignore[reportArgumentType]
    )
    backoff = _cfg._API_INITIAL_BACKOFF
    for attempt in range(_cfg._API_MAX_RETRIES):
        async with session.get(url) as req:
            if req.status == 429 and attempt < _cfg._API_MAX_RETRIES - 1:
                retry_after_str = req.headers.get("Retry-After")
                if retry_after_str is not None:
                    try:
                        backoff = float(retry_after_str)
                    except ValueError:
                        pass
                await anyio.sleep(min(backoff, _cfg._API_MAX_BACKOFF))
                backoff = min(
                    backoff * _cfg._API_BACKOFF_MULTIPLIER, _cfg._API_MAX_BACKOFF
                )
                continue
            return await req.json()
    raise AssertionError("unreachable")


async def _resolve_redirects(
    session: ClientSession,
    titles: set[str],
    cache: MutableMapping[str, _RedirectInfo],
    cache_path: PurePath,
) -> MutableMapping[str, _RedirectInfo]:
    """Resolve redirects for uncached titles via batched API queries.

    Results are merged into *cache* and persisted to disk atomically.

    Parameters
    ----------
    cache_path:
        Path to persist the updated cache.
    """
    uncached = titles - cache.keys()
    if not uncached:
        return cache

    titles_list = list(uncached)
    now_iso = datetime.now(timezone.utc).isoformat()
    for i in range(0, len(titles_list), _cfg._API_MAX_TITLES_PER_REQUEST):
        batch = titles_list[i : i + _cfg._API_MAX_TITLES_PER_REQUEST]
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
                cache.setdefault(
                    title, _RedirectInfo(to=title, cached_at=now_iso)
                )
    _save_redirect_cache(cache, cache_path=cache_path)
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

    for i in range(0, len(titles_list), _cfg._API_MAX_TITLES_PER_REQUEST):
        batch = titles_list[i : i + _cfg._API_MAX_TITLES_PER_REQUEST]
        params: dict[str, str | int] = {
            "format": "json",
            "formatversion": 2,
            "action": "query",
            "prop": "imageinfo",
            "titles": "|".join(batch),
            "iiprop": "extmetadata",
        }
        api_result = await _api_request(session, params, host=_cfg._COMMONS_HOST_URL)

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
                # Lazy import to avoid circular dependency:
                # api.py ⟶ converter.py but converter.py ⟶ types.py (not api.py).
                from .converter import WikiHtmlConverter  # noqa: PLC0415

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
