"""Conversion pipeline orchestration.

Contains ``wiki_html_to_plaintext`` (post-processing after the converter)
and ``run_pipeline`` (the top-level entry point that coordinates redirect
resolution, image metadata fetching, and conversion).
"""

import re
from collections.abc import Mapping, MutableMapping, MutableSet
from os import PathLike
from pathlib import PurePath

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


def _separate_block_math(text: str) -> str:
    """Separate ``$$...$$`` block math onto its own lines using mistune AST.

    For each ``block_math`` node in the mistune AST that is NOT inside a
    table cell, ensure there is a blank line (``\n\n``) before and after
    the ``$$...$$`` delimiter area. Skips nodes already separated, nodes
    inside table cells, and math expressions that are already on their
    own line.

    Uses sequential ``str.find`` (not regex) to locate each span in the
    source text, avoiding LaTeX regex escaping issues. Processes spans
    right-to-left so earlier insertions don't shift pending positions.
    """
    ast = _MISTUNE_PARSER(text)

    # Collect block_math raw content in traversal order, tracking ancestor
    # types so we skip block_math inside table cells.
    blocks: list[str] = []

    def _walk(nodes: list[dict], ancestors: list[str]) -> None:
        for node in nodes:
            ntype = node.get("type", "")
            new_ancestors = ancestors + [ntype]
            if ntype == "block_math" and "table_cell" not in new_ancestors:
                blocks.append(node.get("raw", ""))
            children = node.get("children")
            if children:
                _walk(children, new_ancestors)

    _walk(ast, [])

    # Find each span in text via sequential str.find. The AST traversal
    # order matches text order (depth-first left-to-right), so advancing
    # search_pos past each match gives unique positions even for duplicate
    # raw content.
    positions: list[tuple[int, str]] = []  # (pos, search_for)
    search_pos = 0
    for raw in blocks:
        search_for = f"$${raw}$$"
        pos = text.find(search_for, search_pos)
        if pos == -1:
            continue
        positions.append((pos, search_for))
        search_pos = pos + len(search_for)

    # Process right-to-left so insertions at higher positions never shift
    # lower positions that haven't been processed yet.
    for pos, search_for in sorted(positions, key=lambda x: -x[0]):
        end = pos + len(search_for)

        # Check for non-whitespace text before $$ on the same line.
        line_start = text.rfind("\n", 0, pos)
        if line_start == -1:
            line_start = 0
        before_text = text[line_start:pos]
        needs_before = bool(before_text.strip())

        # Check for non-whitespace text after $$ on the same line.
        line_end = text.find("\n", end)
        if line_end == -1:
            line_end = len(text)
        after_text = text[end:line_end]
        needs_after = bool(after_text.strip())

        # Apply insertions right-to-left (do AFTER before BEFORE since
        # after insertion is at a higher position). Strip any trailing
        # whitespace before ``$$`` and leading whitespace after ``$$`` to
        # keep lines clean.
        if needs_after:
            after_non_ws = after_text.lstrip()
            after_strip = len(after_text) - len(after_non_ws)
            text = text[:end] + "\n\n" + text[end + after_strip :]
        if needs_before:
            before_non_ws = before_text.rstrip()
            before_strip = len(before_text) - len(before_non_ws)
            text = text[: pos - before_strip] + "\n\n" + text[pos:]

    return text


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
    # Separate $$...$$ block math onto its own lines.
    result = _separate_block_math(result)
    result = result.strip()
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
