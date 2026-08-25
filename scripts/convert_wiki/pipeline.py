"""Conversion pipeline orchestration.

Contains ``wiki_html_to_plaintext`` (post-processing after the converter)
and ``run_pipeline`` (the top-level entry point that coordinates redirect
resolution, image metadata fetching, and conversion).
"""

import re
from collections.abc import Mapping, MutableMapping, MutableSet, Sequence
from os import PathLike
from pathlib import PurePath
from typing import Any

from aiohttp import ClientSession, TCPConnector
from bs4 import BeautifulSoup, PageElement

from . import config as _cfg
from .api import (
    _collect_image_filenames,
    _collect_link_titles,
    _load_redirect_cache,
    _resolve_image_metadata,
    _resolve_redirects,
)
from .ast_utils import (
    _MISTUNE_PARSER,
    _find_top_level_adjacent,
    _walk_tokens,
)
from .converter import WikiHtmlConverter
from .types import _RedirectInfo
from .utils import _ZERO_WIDTH_CHARS_RE, _reformat_table

"""Exported names from this module."""
__all__ = ()


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


def _determine_needs_before(
    prev: dict[str, Any] | None,
    *,
    inline: bool = False,
    separator_chars: str = _cfg._MARKDOWN_SEPARATOR_CHARACTERS,
) -> bool:
    """Return ``True`` if a space should be inserted before a math delimiter.

    Examines the AST sibling node immediately before a ``block_math`` (or
    ``inline_math`` when ``inline`` is set) node.  If the sibling is a text
    node ending with a non-whitespace character, the delimiter is directly
    adjacent to text in the source — a space is needed.  If the sibling is a
    non-text node (emphasis, code span, etc.), there is no text-node buffer,
    so the delimiter is adjacent by default.

    For inline math (``inline=True``), zero-width characters are stripped
    from the neighbor text first, then the text is tested against
    ``separator_chars`` (the same list and test as the emphasis separator in
    ``converter._needs_separator_before``, except inline math passes
    ``_MATH_SEPARATOR_CHARACTERS`` so a straight apostrophe is not mistaken
    for a separator), so inline math gets spacing guaranteed in exactly the
    same situations as emphasis.

    Inline HTML siblings (e.g. ``<sub>``/``<sup>`` tags or the marker comment
    inserted by ``_separate_block_math``) do not create word adjacency, so
    they are skipped the same way as line breaks.
    """
    if prev is None:
        return False
    if prev["type"] == "text":
        if inline:
            stripped = _ZERO_WIDTH_CHARS_RE.sub("", prev["raw"])
            return bool(stripped) and (stripped.rstrip(separator_chars) == stripped)
        return bool(prev["raw"]) and not prev["raw"][-1].isspace()
    if inline and prev["type"] in ("softbreak", "linebreak"):
        # A line break is already whitespace separation.
        return False
    if inline and prev["type"] == "inline_html":
        # Inline HTML (e.g. <sub>/<sup> tags or our own separator marker)
        # does not create word adjacency, so no space is needed.
        return False
    return True


def _determine_needs_after(
    next_: dict[str, Any] | None,
    *,
    inline: bool = False,
    separator_chars: str = _cfg._MARKDOWN_SEPARATOR_CHARACTERS,
) -> bool:
    """Return ``True`` if a space should be inserted after a math delimiter.

    Mirror of ``_determine_needs_before`` for the sibling that follows a
    ``block_math`` (or ``inline_math`` when ``inline`` is set) node.  Inline
    HTML siblings (e.g. ``<sub>``/``<sup>`` tags or the marker comment
    inserted by ``_separate_block_math``) do not create word adjacency, so
    they are skipped the same way as line breaks.
    """
    if next_ is None:
        return False
    if next_["type"] == "text":
        if inline:
            stripped = _ZERO_WIDTH_CHARS_RE.sub("", next_["raw"])
            return bool(stripped) and (stripped.lstrip(separator_chars) == stripped)
        return bool(next_["raw"]) and not next_["raw"][0].isspace()
    if inline and next_["type"] in ("softbreak", "linebreak"):
        # A line break is already whitespace separation.
        return False
    if inline and next_["type"] == "inline_html":
        # Inline HTML (e.g. <sub>/<sup> tags or our own separator marker)
        # does not create word adjacency, so no space is needed.
        return False
    return True


def _collect_block_math_info(
    tokens: list[dict[str, Any]],
) -> list[tuple[str, bool, bool, bool]]:
    """Deep-walk the AST and collect info about every math node.

    Both ``block_math`` (``$$…$$``) and ``inline_math`` (``$…$``) nodes are
    collected in document order.  *Standalone* block math (top-level AST,
    not nested inside a paragraph) never gets spacing added — it is already
    separated by newlines.  Only math inside a paragraph or similar
    container is a candidate for whitespace insertion.

    Returns a list of ``(raw, needs_before, needs_after, is_inline)`` tuples
    ordered by document position.
    """
    info: list[tuple[str, bool, bool, bool]] = []

    for token, depth, parents in _walk_tokens(tokens, None):
        if token["type"] not in ("block_math", "inline_math"):
            continue
        is_inline = token["type"] == "inline_math"
        if depth == 0:
            if is_inline:
                continue  # Unreachable: inline math is never top-level.
            if "$$" in token["raw"]:
                # Collapsed node: Mistune merged multiple ``$$…$$`` spans on the
                # same line into one block_math node.  Wrap in paragraph context
                # and re-parse with Mistune to get individually-split spans.
                raw = token["raw"]
                wrapped = "w " + "$$" + raw + "$$" + " w"
                result, _state = _MISTUNE_PARSER.parse(wrapped)
                del _state
                if isinstance(result, str):
                    # Parse error — treat as normal standalone.
                    info.append((raw, False, False, False))
                else:
                    para = result[0] if isinstance(result, list) else None
                    if para is None or para.get("type") != "paragraph":
                        info.append((raw, False, False, False))
                    else:
                        children: list[dict[str, Any]] = para.get("children", [])
                        prev_is_block_math = False
                        for child in children:
                            if child.get("type") != "block_math":
                                prev_is_block_math = False
                                continue
                            idx = children.index(child)
                            prev_sib = children[idx - 1] if idx > 0 else None
                            next_sib = (
                                children[idx + 1] if idx + 1 < len(children) else None
                            )
                            needs_before = _determine_needs_before(prev_sib)
                            if prev_is_block_math:
                                # Previous block_math already adds the
                                # separator space — avoid double spacing.
                                needs_before = False
                            needs_after = _determine_needs_after(next_sib)
                            info.append(
                                (child["raw"], needs_before, needs_after, False)
                            )
                            prev_is_block_math = True
            else:
                info.append((token["raw"], False, False, False))
        else:
            parent = parents[-1]
            parent_children = parent.get("children", [])
            idx = next(i for i, t in enumerate(parent_children) if t is token)
            prev_sib = parent_children[idx - 1] if idx > 0 else None
            next_sib = (
                parent_children[idx + 1] if idx + 1 < len(parent_children) else None
            )
            info.append(
                (
                    token["raw"],
                    _determine_needs_before(
                        prev_sib,
                        inline=is_inline,
                        separator_chars=_cfg._MATH_SEPARATOR_CHARACTERS,
                    ),
                    _determine_needs_after(
                        next_sib,
                        inline=is_inline,
                        separator_chars=_cfg._MATH_SEPARATOR_CHARACTERS,
                    ),
                    is_inline,
                )
            )

    return info


"""Matches inline-math raw text that is a single atomic symbol."""
_IS_ATOMIC_INLINE_MATH_RE = re.compile(r"[^\s\\/()[\]{}^_|]+")


def _inline_math_separator(
    raw: str, *, before_apostrophe: bool = False, after_apostrophe: bool = False
) -> str:
    """Return the separator for an inline-math span.

    Atomic math (a single run of plain characters such as ``n``, ``x``, or a
    Greek letter) abutting a word gets the zero-width markdown separator
    marker; anything else (``\\frac``, ``1/|w|``, ``f(x)``, ``e^{...}``)
    keeps a normal space so the two sides do not visually collide.

    A straight apostrophe is a word-forming character (possessive ``'s``), so
    it must never be separated from the math by a space — when the neighbor on
    either side is an apostrophe the zero-width marker is used regardless of
    atomicity.
    """
    if (
        _IS_ATOMIC_INLINE_MATH_RE.fullmatch(raw)
        or before_apostrophe
        or after_apostrophe
    ):
        return _cfg._MARKDOWN_SEPARATOR
    return " "


def _scan_and_apply(text: str, info: Sequence[tuple[str, bool, bool, bool]]) -> str:
    """Scan *text* for math spans matching each entry in *info*.

    For each entry in *info* (ordered by document position), the source is
    scanned left-to-right for a matching span.  Each entry is a
    ``(raw, needs_before, needs_after, is_inline)`` tuple; ``is_inline``
    selects the separator: inline math that is a single atomic symbol gets
    the zero-width markdown separator marker, everything else gets a space.
    The delimiter is probed directly: ``$${raw}$$`` at a ``$$`` position,
    ``${raw}$`` at a single-``$`` position.  When found, the
    ``needs_before`` / ``needs_after`` flags control whether a separator is
    inserted.  Consecutive block-math spans in the same paragraph (separated
    only by whitespace) are joined with a hard line break so they stay on
    separate lines.  Non-matching ``$$…$$`` regions are skipped whole; stray
    single ``$`` are consumed one at a time.
    """
    parts: list[str] = []
    pos = 0
    prev_is_inline: bool | None = None
    parts_ended_with_sep = False

    for entry in info:
        raw, needs_before, needs_after, is_inline = entry
        target = "$$" + raw + "$$"
        target_len = len(target)
        separator = " "

        while pos < len(text):
            dollar_pos = text.find("$", pos)
            if dollar_pos == -1:
                parts.append(text[pos:])
                return "".join(parts)
            if text[dollar_pos : dollar_pos + 2] == "$$":
                if (
                    dollar_pos + target_len <= len(text)
                    and text[dollar_pos : dollar_pos + target_len] == target
                ):
                    gap = text[pos:dollar_pos]
                    if (
                        prev_is_inline is False
                        and not is_inline
                        and (not gap or gap.isspace())
                        and "\n" not in gap
                    ):
                        # Consecutive block-math spans on one line: split
                        # them onto separate lines with a hard line break.
                        # Undo the separator after the previous span first so
                        # the break replaces the whole whitespace region.
                        if parts_ended_with_sep:
                            parts.pop()
                        parts.append(" <br/> ")
                    else:
                        parts.append(gap)
                        if needs_before and not (gap and gap[-1].isspace()):
                            parts.append(separator)
                    parts.append(target)
                    if needs_after and not (
                        dollar_pos + target_len < len(text)
                        and text[dollar_pos + target_len].isspace()
                    ):
                        parts.append(separator)
                    parts_ended_with_sep = needs_after
                    pos = dollar_pos + target_len
                    break
                close_pos = text.find("$$", dollar_pos + 2)
                if close_pos == -1:
                    parts.append(text[dollar_pos:])
                    return "".join(parts)
                parts.append(text[pos : close_pos + 2])
                parts_ended_with_sep = False
                pos = close_pos + 2
            else:
                target_inline = "$" + raw + "$"
                if text.startswith(target_inline, dollar_pos):
                    if is_inline:
                        before_apostrophe = (
                            needs_before and pos > 0 and text[pos - 1] == "'"
                        )
                        after_apostrophe = (
                            needs_after
                            and dollar_pos + len(target_inline) < len(text)
                            and text[dollar_pos + len(target_inline)] == "'"
                        )
                        separator = _inline_math_separator(
                            raw,
                            before_apostrophe=before_apostrophe,
                            after_apostrophe=after_apostrophe,
                        )
                    parts.append(text[pos:dollar_pos])
                    if needs_before and not (pos > 0 and text[pos - 1].isspace()):
                        parts.append(separator)
                    parts.append(target_inline)
                    if needs_after and not (
                        dollar_pos + len(target_inline) < len(text)
                        and text[dollar_pos + len(target_inline)].isspace()
                    ):
                        parts.append(separator)
                    parts_ended_with_sep = needs_after
                    pos = dollar_pos + len(target_inline)
                    break
                parts.append(text[pos : dollar_pos + 1])
                parts_ended_with_sep = False
                pos = dollar_pos + 1
        else:
            parts.append(text[pos:])
            return "".join(parts)
        prev_is_inline = is_inline

    parts.append(text[pos:])
    return "".join(parts)


def _separate_block_quotes(text: str) -> str:
    """Insert MD028 suppression comments between adjacent blockquote blocks.

    Uses the mistune AST to identify adjacent ``block_quote`` tokens
    separated only by blank lines.  For each adjacent pair, an MD028
    suppression comment is inserted between them (replacing the blank
    line separator).

    This replaces the fragile regex ``_MD028_RE`` that was limited in
    handling nested content and multi-block groups.
    """
    parse_result, _state = _MISTUNE_PARSER.parse(text)
    del _state
    if isinstance(parse_result, str):
        return text  # Parse error, return unchanged.

    pairs = _find_top_level_adjacent(parse_result, "block_quote")
    if not pairs:
        return text

    # Find all block_quote sections in the source text by scanning for
    # consecutive lines starting with ``>``.  This is more reliable than
    # ``_find_token_range`` because ``_reconstruct_token_raw`` does not
    # preserve all formatting details (code span backticks, list item
    # markers, etc.).
    lines = text.split("\n")
    # Build byte offset table: offsets[n] = byte position of line n,
    # offsets[-1] = position after the last newline.
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line) + 1)

    ranges: list[tuple[int, int]] = []
    i = 0
    while i < len(lines):
        if not lines[i].startswith(">"):
            i += 1
            continue
        start = offsets[i]
        while i < len(lines) and lines[i].startswith(">"):
            i += 1
        end = offsets[i]  # byte after the last ``>`` line
        ranges.append((start, end))

    if not ranges:
        return text

    # Map AST block_quote indices (in parse_result) to source ranges
    # (both are in source order, so position in the block_quote token
    # list corresponds to position in the ranges list).
    bq_indices = [
        idx for idx, tok in enumerate(parse_result) if tok["type"] == "block_quote"
    ]
    index_to_range: dict[int, int] = {}
    for n, idx in enumerate(bq_indices):
        if n < len(ranges):
            index_to_range[idx] = n

    for first, second in reversed(pairs):
        first_n = index_to_range.get(first)
        second_n = index_to_range.get(second)
        if first_n is None or second_n is None:
            continue
        _first_start, first_end = ranges[first_n]
        second_start, _second_end = ranges[second_n]
        # Replace the gap (blank line(s)) between the two block_quote
        # sections with the MD028 suppression comment surrounded by
        # blank lines.
        text = (
            text[:first_end] + "\n<!-- markdownlint MD028 -->\n\n" + text[second_start:]
        )

    return text


def _separate_block_math(text: str) -> str:
    """Ensure minimum whitespace separation around math delimiters.

    If non-whitespace text immediately precedes the opening ``$$`` (or the
    opening ``$`` of inline math), a space is inserted before it.  If
    non-whitespace text immediately follows the closing delimiter, a space
    is inserted after it.  Inline math uses the same character list and
    test as the emphasis separator (``converter._needs_separator_before`` /
    ``_needs_separator_after``), with zero-width characters stripped first.

    Uses mistune AST to correctly distinguish ``block_math`` / ``inline_math``
    nodes from ``$`` that appears inside code spans, fenced code blocks, or
    other Markdown constructs where the delimiters are literal text.
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
    # Separate math delimiters from adjacent text.  Run before table
    # reformatting so inserted spaces count toward column widths; running
    # it after would grow cells past their padding and misalign pipes
    # (MD060).
    result = _separate_block_math(result)
    # Pad table columns to the widest content per column.
    result = _reformat_table(result)
    # Insert MD028 suppression comments between adjacent blockquote blocks.
    result = _separate_block_quotes(result)
    # Collapse excessive blank lines.
    result = re.sub(r"\n{3,}", r"\n\n", result)
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
