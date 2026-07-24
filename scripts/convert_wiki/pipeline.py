"""Conversion pipeline orchestration.

Contains ``wiki_html_to_plaintext`` (post-processing after the converter)
and ``run_pipeline`` (the top-level entry point that coordinates redirect
resolution, image metadata fetching, and conversion).
"""

import re
from collections.abc import Mapping, MutableMapping, MutableSet
from os import PathLike
from pathlib import PurePath
from typing import Any

import mistune
from aiohttp import ClientSession, TCPConnector
from bs4 import BeautifulSoup, PageElement
from mistune.plugins.math import math as _mistune_math
from mistune.plugins.math import math_in_list as _mistune_math_in_list
from mistune.plugins.math import math_in_quote as _mistune_math_in_quote
from mistune.plugins.table import table as _mistune_table

from . import config as _cfg
from .api import (
    _collect_image_filenames,
    _collect_link_titles,
    _load_redirect_cache,
    _resolve_image_metadata,
    _resolve_redirects,
)
from .converter import WikiHtmlConverter
from .types import _RedirectInfo
from .utils import _pad_table_blocks

"""Exported names from this module."""
__all__ = ()

"""Regex for MD028 suppression between adjacent blockquote blocks."""
_MD028_RE = re.compile(r"(^(?:>[^\n]*\n)+)\n+(^>(?:[^\n]*\n?)+)", re.MULTILINE)

"""Mistune AST parser with math and table support."""
_MISTUNE_PARSER = mistune.create_markdown(
    renderer="ast",
    plugins=[
        _mistune_math,
        _mistune_math_in_list,
        _mistune_math_in_quote,
        _mistune_table,
    ],
)


def _make_converter(
    wiki_dir: PathLike[str] | None = None,
    wiki_lang_dir: PathLike[str] | None = None,
    image_metadata: Mapping[str, str] | None = None,
    names_map: Mapping[str, str] | None = None,
    soup: BeautifulSoup | None = None,
) -> WikiHtmlConverter:
    """Create a WikiHtmlConverter with default path fallbacks."""
    return WikiHtmlConverter(
        converted_wiki_dir=wiki_dir or _cfg._CONVERTED_WIKI_DIRECTORY,
        converted_wiki_lang_dir=wiki_lang_dir
        or _cfg._CONVERTED_WIKI_LANGUAGE_DIRECTORY,
        image_metadata=image_metadata or {},
        names_map=names_map,
        soup=soup,
    )


async def _create_session_and_run(
    html: BeautifulSoup,
    *,
    redirect_map: MutableMapping[str, _RedirectInfo] | None = None,
    image_metadata: Mapping[str, str] | None = None,
    cache_path: PurePath | None = None,
    names_map: Mapping[str, str] | None = None,
    wiki_dir: PathLike[str] | None = None,
    wiki_lang_dir: PathLike[str] | None = None,
    refs: bool = True,
) -> tuple[str, set[str]]:
    """Create a ClientSession and run the full pipeline."""
    async with ClientSession(
        connector=TCPConnector(limit_per_host=_cfg._MAX_CONCURRENT_REQUESTS_PER_HOST),
        headers={
            "Accept-Encoding": "gzip",
            "User-Agent": _cfg.USER_AGENT,
        },
    ) as session:
        return await run_pipeline(
            html,
            session=session,
            redirect_map=redirect_map,
            image_metadata=image_metadata,
            cache_path=cache_path,
            names_map=names_map,
            wiki_dir=wiki_dir,
            wiki_lang_dir=wiki_lang_dir,
            refs=refs,
        )


def _determine_needs_before(prev: dict[str, Any] | None) -> bool:
    """Return ``True`` if a space should be inserted before the opening ``$$``.

    Examines the AST sibling node immediately before a ``block_math`` node.
    If the sibling is a text node ending with a non-whitespace character, the
    ``$$`` is directly adjacent to text in the source — a space is needed.
    If the sibling is a non-text node (emphasis, code span, etc.), there is
    no text-node buffer, so the ``$$`` is adjacent by default.
    """
    if prev is None:
        return False
    if prev["type"] == "text":
        return bool(prev["raw"]) and prev["raw"][-1] not in " \t"
    return True


def _determine_needs_after(next_: dict[str, Any] | None) -> bool:
    """Return ``True`` if a space should be inserted after the closing ``$$``.

    Mirror of ``_determine_needs_before`` for the sibling that follows a
    ``block_math`` node.
    """
    if next_ is None:
        return False
    if next_["type"] == "text":
        return bool(next_["raw"]) and next_["raw"][0] not in " \t"
    return True


def _collect_block_math_info(
    tokens: list[dict[str, Any]],
) -> list[tuple[str, bool, bool]]:
    """Deep-walk the AST and collect info about every ``block_math`` node.

    *Standalone* block math (top-level AST, not nested inside a paragraph)
    never gets spacing added — it is already separated by newlines.  Only
    *inline* block math (inside a paragraph or similar container) is
    candidate for whitespace insertion.

    Returns a list of ``(raw, needs_before, needs_after)`` tuples ordered by
    document position.
    """
    info: list[tuple[str, bool, bool]] = []

    def _walk(children: list[dict[str, Any]], depth: int = 0) -> None:
        for i, child in enumerate(children):
            if child["type"] == "block_math":
                is_inline = depth > 0
                if not is_inline:
                    info.append((child["raw"], False, False))
                else:
                    prev_sib = children[i - 1] if i > 0 else None
                    next_sib = children[i + 1] if i + 1 < len(children) else None
                    info.append(
                        (
                            child["raw"],
                            _determine_needs_before(prev_sib),
                            _determine_needs_after(next_sib),
                        )
                    )
            if "children" in child:
                _walk(child["children"], depth + 1)

    _walk(tokens)
    return info


def _scan_and_apply(text: str, info: list[tuple[str, bool, bool]]) -> str:
    """Scan *text* for ``$$…$$`` spans matching each ``block_math`` entry.

    For each entry in *info* (ordered by document position), the source is
    scanned left-to-right for a ``$${raw}$$`` span.  When found, the
    ``needs_before`` / ``needs_after`` flags control whether a space is
    inserted.  Non-matching ``$$`` spans (e.g. inside code spans) are
    skipped.
    """
    parts: list[str] = []
    pos = 0

    for raw, needs_before, needs_after in info:
        target = "$$" + raw + "$$"
        target_len = len(target)

        while pos < len(text):
            dollar_pos = text.find("$$", pos)
            if dollar_pos == -1:
                parts.append(text[pos:])
                return "".join(parts)
            if (
                dollar_pos + target_len <= len(text)
                and text[dollar_pos : dollar_pos + target_len] == target
            ):
                parts.append(text[pos:dollar_pos])
                if needs_before:
                    parts.append(" ")
                parts.append(target)
                if needs_after:
                    parts.append(" ")
                pos = dollar_pos + target_len
                break
            close_pos = text.find("$$", dollar_pos + 2)
            if close_pos == -1:
                parts.append(text[dollar_pos:])
                return "".join(parts)
            parts.append(text[pos : close_pos + 2])
            pos = close_pos + 2
        else:
            parts.append(text[pos:])
            return "".join(parts)

    parts.append(text[pos:])
    return "".join(parts)


def _separate_block_math(text: str) -> str:
    """Ensure minimum whitespace separation around ``$$…$$`` block math.

    If non-whitespace text immediately precedes the opening ``$$``, a space
    is inserted before it.  If non-whitespace text immediately follows the
    closing ``$$``, a space is inserted after it.

    Uses mistune AST to correctly distinguish ``block_math`` nodes from
    ``$$`` that appears inside code spans, fenced code blocks, or other
    Markdown constructs where the delimiters are literal text.
    """
    parse_result, _state = _MISTUNE_PARSER.parse(text)
    del (
        _state
    )  # Unused but kept in signature for future needs (e.g. position recovery).
    if isinstance(parse_result, str):
        return text  # Parse error, return unchanged.
    info = _collect_block_math_info(parse_result)
    if not info:
        return text
    return _scan_and_apply(text, info)


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
        soup = ele if isinstance(ele, BeautifulSoup) else None
        converter = WikiHtmlConverter(image_metadata=image_metadata, soup=soup)
    result = await converter.convert(
        ele,
        out_to_archive=out_to_archive,
        list_stack=list_stack,
        escape=escape,
        refs=refs,
        redirect_map=redirect_map,
    )
    # Replace non-breaking spaces with regular spaces (residues from
    # citation spans, HTML &nbsp; in list items, etc.). Replace \n\xa0
    # (newline followed by non-breaking space) first to remove leading
    # non-breaking spaces on empty-looking lines, then replace remaining
    # \xa0 with regular spaces.
    result = (
        result.replace("\n\xa0", "\n\n")
        .replace("\xa0", " ")
        .replace("\u200a", "&hairsp;")
    )
    # Strip trailing whitespace from each line.
    result = "\n".join(line.rstrip(" \t") for line in result.split("\n"))
    # Pad table columns to the widest content per column.
    result = _pad_table_blocks(result)
    # Insert MD028 suppression comments between adjacent blockquote blocks.
    result = _MD028_RE.sub(r"\1\n<!-- markdownlint MD028 -->\n\n\2", result)
    # Collapse excessive blank lines.
    result = re.sub(r"\n{3,}", r"\n\n", result)
    result = result.strip()
    result = _separate_block_math(result)
    return result + "\n" if result else result


async def run_pipeline(
    html: BeautifulSoup,
    *,
    session: ClientSession | None = None,
    redirect_map: MutableMapping[str, _RedirectInfo] | None = None,
    image_metadata: Mapping[str, str] | None = None,
    cache_path: PurePath | None = None,
    names_map: Mapping[str, str] | None = None,
    wiki_dir: PathLike[str] | None = None,
    wiki_lang_dir: PathLike[str] | None = None,
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

    # If all data is already provided, skip session/API entirely.
    if redirect_map is not None and image_metadata is not None:
        output = await wiki_html_to_plaintext(
            html,
            out_to_archive=out_to_archive,
            redirect_map=redirect_map,
            refs=refs,
            converter=_make_converter(
                wiki_dir, wiki_lang_dir, image_metadata, names_map, soup=html
            ),
        )
        return output, out_to_archive

    # Create a session if needed for API calls.
    if session is None:
        return await _create_session_and_run(
            html,
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
        resolved_cache_path: PurePath = (
            cache_path if cache_path is not None else _cfg._REDIRECT_CACHE_PATH
        )
        titles = _collect_link_titles(html)
        cache = _load_redirect_cache(cache_path=resolved_cache_path)
        redirect_map = await _resolve_redirects(
            session, titles, cache, cache_path=resolved_cache_path
        )

    # Resolve image metadata if needed.
    if image_metadata is None:
        image_filenames = _collect_image_filenames(html)
        image_metadata = await _resolve_image_metadata(session, image_filenames)

    # Convert.
    output = await wiki_html_to_plaintext(
        html,
        out_to_archive=out_to_archive,
        redirect_map=redirect_map,
        refs=refs,
        converter=_make_converter(wiki_dir, wiki_lang_dir, image_metadata, names_map),
    )
    return output, out_to_archive
