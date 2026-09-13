"""Conversion pipeline: preprocess → convert → postprocess.

This module orchestrates the full Wikipedia HTML-to-Markdown pipeline.
The pipeline has three logical phases:

1. **Preprocess** (``_preprocess_html``): mutate the HTML tree before
   conversion — style/CS1 cleanup, numblk table merging, adjacent math
   merging, external math punctuation normalization, sfrac replacement,
   annotated-image cleanup.

2. **Convert** (``WikiHtmlConverter.convert``): walk the (now-clean) HTML
   tree and emit Markdown text.  The converter must not perform tree
   mutations; it only reads the tree and produces text.

3. **Postprocess** (``wiki_html_to_plaintext``): fix Markdown text —
   math spacing, table column padding, blockquote MD028 separation,
   blank-line collapsing.

Key functions:

- ``run_pipeline``: top-level entry point; handles redirect resolution,
  image metadata fetching, and delegates to ``wiki_html_to_plaintext``.
- ``wiki_html_to_plaintext``: converts a parsed HTML tree to Markdown,
  applying preprocessing, conversion, and postprocessing.
- ``_preprocess_html``: all HTML tree mutations before conversion.
"""

import re
from collections.abc import Mapping, MutableMapping, MutableSet, Sequence
from os import PathLike
from pathlib import PurePath
from typing import Any

from aiohttp import ClientSession, TCPConnector
from aiohttp_retry import RetryClient
from aiohttp_retry.types import ClientType
from bs4 import BeautifulSoup, NavigableString, PageElement, Tag

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
from .inline_context import _is_display_math_only_dl
from .latex import LatexConverter
from .table import _reformat_table
from .types import _RedirectInfo
from .utils import _ZERO_WIDTH_CHARS_RE, _create_redirect_symlinks

"""Exported names from this module."""
__all__ = ()


def _merge_adjacent_math_dd(dd: Tag) -> None:
    """Merge consecutive inline math spans in a ``<dd>`` element.

    Wikipedia HTML often splits multi-part equations into separate
    ``<span class="mwe-math-element mwe-math-element-inline">``
    children separated only by whitespace. This method detects runs
    of ≥2 such spans (with only whitespace NavigableStrings between)
    and replaces each run with a single merged span whose alttext is
    the space-joined LaTeX of all parts.
    """
    # Repeat until no more merges are possible.
    while True:
        children = list(dd.children)
        merged_any = False
        i = 0
        while i < len(children):
            child = children[i]
            if not isinstance(child, Tag) or "mwe-math-element" not in " ".join(
                child.get_attribute_list("class")
            ):
                i += 1
                continue
            # Start of a potential run.
            run = [child]
            j = i + 1
            while j < len(children):
                nxt = children[j]
                if isinstance(nxt, NavigableString):
                    if nxt.strip():
                        break  # non-whitespace text ends run
                    j += 1
                    continue
                if isinstance(nxt, Tag) and "mwe-math-element" in " ".join(
                    nxt.get_attribute_list("class")
                ):
                    run.append(nxt)
                    j += 1
                    continue
                break
            if len(run) < 2:
                i = j
                continue
            # Merge the run into a single span.
            parts: list[str] = []
            for span in run:
                math = span.find("math")
                if isinstance(math, Tag):
                    raw = math.get("alttext", "")
                    if raw:
                        parts.append(WikiHtmlConverter._prepare_math_alttext(str(raw)))
            merged_alt = " ".join(parts)
            # Build replacement element.
            new_span = dd.new_tag(
                "span",
                attrs={"class": "mwe-math-element mwe-math-element-inline"},
            )
            new_mathml_span = dd.new_tag(
                "span",
                attrs={"class": "mwe-math-mathml-inline"},
            )
            new_math = dd.new_tag(
                "math",
                attrs={
                    "alttext": merged_alt,
                    "xmlns": "http://www.w3.org/1998/Math/MathML",
                },
            )
            new_annotation = dd.new_tag(
                "annotation",
                attrs={"encoding": "application/x-tex"},
            )
            new_annotation.string = merged_alt
            new_math.append(new_annotation)
            new_mathml_span.append(new_math)
            new_span.append(new_mathml_span)
            # Replace first span; remove rest and surrounding whitespace.
            run[0].replace_with(new_span)
            for span in run[1:]:
                span.extract()
            # Clean up adjacent whitespace NS.
            prev = new_span.previous_sibling
            while isinstance(prev, NavigableString) and not prev.strip():
                to_remove = prev
                prev = to_remove.previous_sibling
                to_remove.extract()
            nxt = new_span.next_sibling
            while isinstance(nxt, NavigableString) and not nxt.strip():
                to_remove = nxt
                nxt = to_remove.next_sibling
                to_remove.extract()
            # Mark the merged span so _is_inline_math knows it was
            # assembled from multiple inline math spans.
            new_span["data-merged-inline"] = ""
            merged_any = True
            break  # restart scan from beginning
        if not merged_any:
            break


def _make_converter(
    wiki_dir: PathLike[str] | None = None,
    wiki_lang_dir: PathLike[str] | None = None,
    image_metadata: Mapping[str, str] | None = None,
    names_map: Mapping[str, str] | None = None,
    soup: BeautifulSoup | None = None,
    page_name: str | None = None,
) -> WikiHtmlConverter:
    """Create a WikiHtmlConverter with default path fallbacks."""
    return WikiHtmlConverter(
        converted_wiki_dir=wiki_dir or _cfg._CONVERTED_WIKI_DIRECTORY,
        converted_wiki_lang_dir=wiki_lang_dir
        or _cfg._CONVERTED_WIKI_LANGUAGE_DIRECTORY,
        image_metadata=image_metadata or {},
        names_map=names_map,
        soup=soup,
        page_name=page_name,
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
    ) as raw_session:
        session = RetryClient(
            client_session=raw_session,
            retry_options=_cfg._WikimediaRetry(
                attempts=3,
                start_timeout=1.0,
                max_timeout=30.0,
                statuses={429},
            ),
            raise_for_status=False,
        )
        try:
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
        finally:
            await session.close()


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
            if idx > 0:
                prev_sib = parent_children[idx - 1]
            elif len(parents) >= 2:
                # Math is the first/only child of its container (e.g. the sole
                # child of a link).  Fall back to the container's previous
                # sibling in the grandparent so spacing reflects the real
                # preceding text rather than the (empty) container interior.
                grandparent = parents[-2]
                gp_children = grandparent.get("children", [])
                gp_idx = next(
                    (i for i, t in enumerate(gp_children) if t is parent), None
                )
                prev_sib = gp_children[gp_idx - 1] if gp_idx and gp_idx > 0 else None
            else:
                prev_sib = None
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
                        if needs_before and gap and gap[-1] == "[" and dollar_pos >= 2:
                            if text[dollar_pos - 2].isspace():
                                # Link-wrapped block math already separated
                                # from the preceding text by a space outside
                                # the link — keep it as-is.
                                parts.append(gap)
                            else:
                                # Link-wrapped block math: the separator
                                # belongs outside the link, between the
                                # preceding text and the opening bracket, so
                                # the math still renders inside the link
                                # target.
                                parts.append(gap[:-1])
                                parts.append(separator)
                                parts.append("[")
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


def _merge_dl_after_thumb_into_list(soup: BeautifulSoup | Tag) -> None:
    """Merge <dl> paragraphs into preceding list when separated by a thumbnail.

    When a <dl> follows a <div class="thumb"> that follows a <ul>/<ol>,
    the <dd> children belong to the last <li> of that list (they are
    continuations of the list item content).  This restructuring moves
    the <dd> elements into the last <li> and removes the empty <dl>.

    Display-math-only <dl> elements are skipped — they have different
    semantics (equation references, not prose continuations).
    """
    if not isinstance(soup, (BeautifulSoup, Tag)):
        return

    def _content_sibling(ele: Tag, *, following: bool) -> Tag | None:
        """Return the first content sibling, skipping <link>/<style>."""
        if following:
            nxt = ele.find_next_sibling()
            while isinstance(nxt, Tag) and nxt.name in {"link", "style"}:
                nxt = nxt.find_next_sibling()
            return nxt if isinstance(nxt, Tag) else None
        prev = ele.find_previous_sibling()
        while isinstance(prev, Tag) and prev.name in {"link", "style"}:
            prev = prev.find_previous_sibling()
        return prev if isinstance(prev, Tag) else None

    for dl in list(soup.find_all("dl")):
        # Skip display-math-only <dl> — different semantics.
        if _is_display_math_only_dl(dl):
            continue

        # Check if previous sibling is a thumbnail.
        prev = _content_sibling(dl, following=False)
        if prev is None or prev.name != "div":
            continue
        if "thumb" not in frozenset(prev.get_attribute_list("class")):
            continue

        # Check if the thumbnail's previous sibling is a list.
        list_ele = _content_sibling(prev, following=False)
        if list_ele is None or list_ele.name not in {"ul", "ol"}:
            continue

        # Get the last <li> of the list.
        li_items = list_ele.find_all("li", recursive=False)
        if not li_items:
            continue
        last_li = li_items[-1]

        # Move <dd> children from <dl> into <p> elements inside the
        # last <li>.  Using <p> instead of <dl> avoids two issues:
        # (1) the <dl> joiner doesn't add a space before the first <dd>,
        # (2) the <dl> suffix always adds a trailing `` <p> ``.
        # Creating a new <dl> preserves the original <dl>'s
        # display-math-only semantics (which trigger the `` <p> \xa0\xa0\xa0\xa0``
        # prefix in the converter).
        dd_children = [c for c in dl.children if isinstance(c, Tag) and c.name == "dd"]
        if not dd_children:
            continue
        for dd in dd_children:
            p = soup.new_tag("p")
            for child in list(dd.children):
                p.append(child.extract())
            last_li.append(p)

        # Remove whitespace NavigableString between the preceding <dl>
        # and our new <p>.  This ensures the preceding <dl> gets the
        # `` <p> `` suffix (with trailing space) instead of `` <p>``
        # (without), which affects the space after the `` <p> `` separator.
        last_appended = list(last_li.children)[-1]
        prev_sibling = last_appended.previous_sibling
        if isinstance(prev_sibling, NavigableString) and not prev_sibling.strip():
            prev_sibling.extract()

        # Remove the empty <dl> from the tree.
        dl.decompose()


# Block-level tags that prevent a <div> from being "inline-only".
_BLOCK_TAGS = frozenset(
    {"p", "ul", "ol", "dl", "table", "blockquote", "pre", "hr"}
    | {f"h{i}" for i in range(1, 7)}
)


def _unwrap_navbox_inline_divs(soup: BeautifulSoup | Tag) -> None:
    """Unwrap inline-only <div> wrappers inside navbox-abovebelow cells.

    A ``<td class="navbox-abovebelow">`` that lacks the ``hlist`` class
    often wraps inline content (an image + a link) in a ``<div>``.  The
    ``<div>`` block-level handler adds a ``\n\n`` suffix which then
    becomes ``<br/> <br/>`` in table-cell postprocessing — an unwanted
    separator between the icon and the link text.

    This function unwraps such ``<div>`` elements (replacing them with
    their children) so the content stays on one line.
    """
    for td in soup.find_all("td", class_=lambda c: c and "navbox-abovebelow" in c):
        classes = frozenset(td.get_attribute_list("class"))
        if "hlist" in classes:
            continue
        for div in td.find_all("div", recursive=False):
            # Only unwrap if every child is inline/transparent (no block tags).
            if any(
                isinstance(child, Tag) and child.name in _BLOCK_TAGS
                for child in div.children
            ):
                continue
            div.unwrap()


def _preprocess_html(soup: BeautifulSoup | Tag) -> None:
    """Mutate the HTML tree before conversion.

    All tree mutations belong here: style/CS1 cleanup, numblk table
    merging, adjacent math merging, external math punctuation
    normalization, sfrac replacement, and annotated-image cleanup.

    The converter receives a clean tree and must not perform any
    mutations during its walk.
    """
    if not isinstance(soup, (BeautifulSoup, Tag)):
        return

    # 1. Strip <style> tags — CSS is never content.
    for style_tag in soup.find_all("style"):
        style_tag.decompose()

    # 2. Drop CS1-maintenance citation-comment spans.
    for cs1_maint in soup.find_all("span", class_="cs1-maint"):
        cs1_maint.decompose()

    # 3. Merge adjacent numblk tables into one multi-row table.
    _merge_adjacent_numblk_tables(soup)

    # 4. Merge consecutive inline math spans in <dd>/<dt> elements.
    for dd in soup.find_all(["dd", "dt"]):
        _merge_adjacent_math_dd(dd)

    # 5. Normalize external math punctuation: absorb trailing
    #    punctuation from sibling text into math alttext.
    _DISPLAY_MATH_CONTAINERS = frozenset({"dd", "dt"})
    for container in soup.find_all(list(_DISPLAY_MATH_CONTAINERS | {"p"})):
        WikiHtmlConverter._normalize_external_math_punctuation(container)

    # 6. Replace sfrac spans with <math> elements.
    for span in soup.find_all("span"):
        LatexConverter.replace_sfrac_with_math(span, soup)  # ty: ignore[invalid-argument-type] — Tag.new_tag works identically

    # 7. Clean up annotated-image divs: remove annotation divs
    #    and noviewer spans so the converter sees clean content.
    for div in soup.find_all("div", typeof=lambda v: v and "mw:Transclusion" in str(v)):
        if "annotated image" in str(div.get("data-mw", "")):
            for ann_div in div.find_all(
                "div", id=lambda v: v and v.startswith("annotation_")
            ):
                ann_div.decompose()
            for noviewer in div.find_all("span", class_="noviewer"):
                noviewer.decompose()

    # 8. Merge <dl> paragraphs into preceding list when separated by a
    #    thumbnail.  When a <dl> follows a <div class="thumb"> that
    #    follows a <ul>/<ol>, the <dd> children belong to the last <li>
    #    of that list (they are continuations of the list item content).
    _merge_dl_after_thumb_into_list(soup)

    # 9. Unwrap inline-only <div> wrappers inside navbox-abovebelow cells
    #    without hlist.  These <div> elements add a block-level suffix
    #    that becomes a spurious <br/> <br/> separator in the output.
    _unwrap_navbox_inline_divs(soup)


def _merge_adjacent_numblk_tables(ele: PageElement) -> None:
    """Merge chains of adjacent <table class="numblk"> siblings into one table.

    Adjacent numblk tables share the same parent and have only whitespace
    or non-content siblings (``<link>``, ``<style>``) between them.  This
    function moves ``<tr>`` elements from each subsequent numblk table
    into the first table's ``<tbody>``, then decomposes the subsequent
    table.  The inner while-loop handles chains of 3+ tables.
    """
    if not isinstance(ele, Tag):
        return
    for table in list(ele.find_all("table", class_="numblk")):
        while True:
            nxt = table.find_next_sibling()
            while isinstance(nxt, Tag) and nxt.name in {"link", "style"}:
                nxt = nxt.find_next_sibling()
            if not isinstance(nxt, Tag) or nxt.name != "table":
                break
            if "numblk" not in frozenset(nxt.get_attribute_list("class")):
                break
            # Both are numblk tables and adjacent — merge rows.
            # Tag each row with its originating table id so anchors
            # can be placed inside the correct equation-number cell.
            src_id = nxt.get("id")
            for tr in (nxt.find("tbody") or nxt).find_all("tr"):
                if src_id and not tr.get("data-origin-id"):
                    tr["data-origin-id"] = src_id
            dst_id = table.get("id")
            if dst_id:
                for tr in (table.find("tbody") or table).find_all("tr"):
                    if not tr.get("data-origin-id"):
                        tr["data-origin-id"] = dst_id
            src_tbody = nxt.find("tbody") or nxt
            dst_tbody = table.find("tbody") or table
            for tr in src_tbody.find_all("tr"):
                dst_tbody.append(tr.extract())
            nxt.decompose()


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
    # Preprocess: mutate HTML tree before conversion.
    if isinstance(ele, (BeautifulSoup, Tag)):
        _preprocess_html(ele)
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
    # Create redirect symlinks collected during conversion.
    for from_name, to_name in converter._pending_redirects:
        await _create_redirect_symlinks(
            converter._converted_wiki_dir,
            converter._converted_wiki_lang_dir,
            from_name,
            to_name,
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
    # Deduplicate doubled <p> separators from overlapping suffix/prefix
    # when a <dl> inside a <li> ends with `` <p>`` and a following <dl>
    # (after </ul>) starts with `` <p> ``.
    result = re.sub(r"(<p>?)\s*<p>", r"\1", result)
    result = result.strip()
    return result + "\n" if result else result


async def run_pipeline(
    html: BeautifulSoup,
    *,
    session: ClientType | None = None,
    redirect_map: MutableMapping[str, _RedirectInfo] | None = None,
    image_metadata: Mapping[str, str] | None = None,
    cache_path: PurePath | None = None,
    names_map: Mapping[str, str] | None = None,
    wiki_dir: PathLike[str] | None = None,
    wiki_lang_dir: PathLike[str] | None = None,
    refs: bool = True,
    page_name: str | None = None,
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
                wiki_dir,
                wiki_lang_dir,
                image_metadata,
                names_map,
                soup=html,
                page_name=page_name,
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
        converter=_make_converter(
            wiki_dir, wiki_lang_dir, image_metadata, names_map, page_name=page_name
        ),
    )
    return output, out_to_archive
