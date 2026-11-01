"""Pure markdown rewriting for reprocess mode."""

import difflib
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any
from unicodedata import normalize as _normalize_unicode
from urllib.parse import unquote

from .ast_utils import (
    _MISTUNE_PARSER,
    _collect_md_link_urls,
    _find_link_destination_ranges,
    _walk_tokens,
)
from .stems import _stem_for_title
from .utils import _encode_fragment, _fix_filename, _plain_fragment

"""Exported names from this module."""
__all__ = ()

"""Regex matching ATX heading lines (``#`` through ``######``)."""
_ATX_HEADING_RE = re.compile(r"^(#{1,6})\s+(?P<inner>\S.*?)(?:\s*#+\s*)?$")


def _encode_stem(stem: str) -> str:
    """Encode a filename stem for a markdown link target."""
    return _fix_filename(stem).replace(" ", "%20").replace("_", "%5F")


def _decode_link_stem(target: str) -> tuple[str, str]:
    """Split a link target into ``(stem, fragment)``.

    An older converter wrote a same-page target as ``Page#anchor.md``.  The
    ``.md`` belongs to the page in every other target shape, so it moves back
    to the end of the page and the anchor is read as the fragment.
    """
    page, _, fragment = target.partition("#")
    if not page.endswith(".md") and fragment.endswith(".md"):
        page = f"{page}.md"
        fragment = fragment.removesuffix(".md")
    if not page.endswith(".md"):
        msg = f"not a markdown page link: {target!r}"
        raise ValueError(msg)
    stem = unquote(page.removesuffix(".md"))
    return stem, fragment


@dataclass(frozen=True)
class _LinkIndex:
    """Map-spelled lookups for link stems, link fragments, and headings.

    The name map is keyed by Wikipedia titles and valued by the local title
    text, which doubles as the filename stem before sanitisation. A link
    written under an older map, and an anchor that lost a character the
    encoding drops, both fail to spell a key, so every layer here projects
    the map into the space the markdown actually stores:

    - ``plain_*`` hold keys and values themselves, for headings;
    - ``anchor_*`` hold them in ``_encode_fragment`` form, so a fragment
      that lost its ``:`` still matches the key that produced it;
    - ``stem_*`` map the sanitised stem the *base* map produced to the one
      the *effective* map produces, so a case-only or punctuation-only
      mapping still reaches its links;
    - each ``*_fold`` layer answers when no exact spelling matches, which
      recovers a fragment the ingestion fallback already lowercased.
    """

    plain_exact: Mapping[str, str]
    plain_fold: Mapping[str, str]
    anchor_exact: Mapping[str, str]
    anchor_fold: Mapping[str, str]
    stem_old: Mapping[str, str]
    stem_old_fold: Mapping[str, str]
    ambiguous: tuple[str, ...]


def _fold(text: str) -> str:
    """Fold _text_ for the forgiving lookup layers."""
    return _normalize_unicode("NFC", text).casefold()


def _index_add(
    index: dict[str, str],
    ambiguous: set[str],
    key: str,
    value: str,
) -> None:
    """Add ``key -> value`` unless another entry claims the key differently."""
    if key in ambiguous:
        return
    if key not in index:
        index[key] = value
        return
    if index[key] != value:
        del index[key]
        ambiguous.add(key)


def _build_link_index(
    base_map: Mapping[str, str],
    effective_map: Mapping[str, str],
) -> _LinkIndex:
    """Build the lookup layers for _effective_map_, migrating from _base_map_."""
    plain_exact: dict[str, str] = {}
    plain_fold: dict[str, str] = {}
    anchor_exact: dict[str, str] = {}
    anchor_fold: dict[str, str] = {}
    stem_old: dict[str, str] = {}
    stem_old_fold: dict[str, str] = {}
    ambiguous: set[str] = set()
    for title, text in effective_map.items():
        _index_add(plain_exact, ambiguous, title, text)
        _index_add(plain_fold, ambiguous, _fold(title), text)
        anchor = _encode_fragment(title)
        _index_add(anchor_exact, ambiguous, anchor, text)
        _index_add(anchor_fold, ambiguous, _fold(anchor), text)
        old_stem = _stem_for_title(title, base_map)
        new_stem = _fix_filename(text)
        _index_add(stem_old, ambiguous, old_stem, new_stem)
        _index_add(stem_old_fold, ambiguous, _fold(old_stem), new_stem)
    return _LinkIndex(
        plain_exact=plain_exact,
        plain_fold=plain_fold,
        anchor_exact=anchor_exact,
        anchor_fold=anchor_fold,
        stem_old=stem_old,
        stem_old_fold=stem_old_fold,
        ambiguous=tuple(sorted(ambiguous)),
    )


def _resolve_plain(
    plain: str,
    *,
    index: _LinkIndex,
    replace_underscores: bool,
) -> str:
    """Resolve plain text to the title text the map spells for it.

    The layers run from most to least specific: the text itself, its anchor
    form, then the same two folded. A link fragment is looked up with
    ``replace_underscores=True`` because a Wikipedia URL encodes spaces as
    underscores; a heading is looked up as written, since an underscore in
    a heading is a literal underscore.
    """
    variants = (plain,)
    if replace_underscores and "_" in plain:
        variants = (plain, plain.replace("_", " "))
    for variant in variants:
        if variant in index.plain_exact:
            return index.plain_exact[variant]
    for variant in variants:
        if (hit := index.anchor_exact.get(_encode_fragment(variant))) is not None:
            return hit
    for variant in variants:
        if (hit := index.plain_fold.get(_fold(variant))) is not None:
            return hit
    for variant in variants:
        anchor = _fold(_encode_fragment(variant))
        if (hit := index.anchor_fold.get(anchor)) is not None:
            return hit
    return plain


def _resolve_stem(
    stem: str,
    index: _LinkIndex,
    migrations: Mapping[str, str],
) -> str:
    """Resolve a link stem to the stem the effective map spells for it."""
    if (migrated := migrations.get(stem)) is not None:
        return migrated
    if (exact := index.stem_old.get(stem)) is not None:
        return exact
    return index.stem_old_fold.get(_fold(stem), stem)


def _align_plain_to_raw(raw: str, plain: str) -> list[int] | None:
    """Greedily map each plain char to a raw index (subsequence alignment)."""
    mapping: list[int] = []
    search_from = 0
    for char in plain:
        idx = raw.find(char, search_from)
        if idx < 0:
            return None
        mapping.append(idx)
        search_from = idx + 1
    return mapping


def _rewrite_plain_span(raw: str, plain: str, new_plain: str) -> str:
    """Rewrite _raw_ so its plain-text projection becomes _new_plain_.

    Preserves inline markup (emphasis delimiters, backslash escapes) by
    applying the diff between *plain* and *new_plain* at the aligned raw
    positions. Returns *raw* unchanged when alignment fails.
    """
    if new_plain == plain:
        return raw
    if plain == raw:
        return new_plain
    mapping = _align_plain_to_raw(raw, plain)
    if mapping is None:
        return raw
    rewritten = raw
    for tag, i1, i2, j1, j2 in reversed(
        difflib.SequenceMatcher(None, plain, new_plain, autojunk=False).get_opcodes()
    ):
        if tag == "equal":
            continue
        start = mapping[i1] if i1 < len(mapping) else len(raw)
        end = mapping[i2 - 1] + 1 if i2 > 0 else start
        rewritten = rewritten[:start] + new_plain[j1:j2] + rewritten[end:]
    return rewritten


def _rewrite_link_target(
    target: str,
    migrations: Mapping[str, str],
    *,
    names_map: Mapping[str, str] | None = None,
    index: _LinkIndex | None = None,
) -> str:
    """Rewrite a single markdown link target through the name map.

    Handles page links (``Page.md#frag``) and same-article fragment links
    (``#frag``) alike: the stem resolves through the stem layer, and the
    fragment through the plain and anchor layers, so anchors stay in step
    with heading rewriting.  A fragment the map does not know is left as
    it stands; a footnote anchor such as ``#^ref-13`` survives by the same
    rule.  Resolving a stem covers a mapping that only re-cases the title
    or only changes a character the filename transform sanitises, which
    produces no stem migration at all.
    """
    if index is None:
        index = _build_link_index({}, names_map or {})
    page = target.partition("#")[0]
    if not page:
        fragment = target.removeprefix("#")
        # A bare "#" carries no fragment; leave it as written.
        if not fragment:
            return target
        base = ""
    else:
        stem, fragment = _decode_link_stem(target)
        base = f"{_encode_stem(_resolve_stem(stem, index, migrations))}.md"
    if fragment:
        plain_fragment = _plain_fragment(fragment)
        new_fragment = _resolve_plain(
            plain_fragment,
            index=index,
            replace_underscores=True,
        )
        if new_fragment != plain_fragment:
            fragment = _encode_fragment(new_fragment)
    if not fragment:
        return base
    return f"{base}#{fragment}" if base else f"#{fragment}"


def _is_rewritable_target(url: str) -> bool:
    """Return whether a link destination is one this module rewrites.

    Rewritable destinations name a markdown page (``Page.md`` or
    ``Page.md#frag``, including the legacy ``Page#anchor.md`` shape) or
    are same-article fragment links (``#frag``).  A name that merely
    contains ".md" (``notes.md.txt``) names no page and is left alone.
    """
    return url.startswith("#") or url.endswith(".md") or ".md#" in url


def _rewrite_markdown_links(
    text: str,
    migrations: Mapping[str, str],
    *,
    names_map: Mapping[str, str] | None = None,
    index: _LinkIndex | None = None,
) -> str:
    """Rewrite markdown ``.md`` link targets according to _migrations_.

    Link stems are resolved through *index*'s stem layer as well, and link
    fragments (section anchors) through its plain and anchor layers, so a
    mapping reaches every link that names it.  Build *index* once per run
    and pass it in; a run over a single file may omit it.
    """
    if index is None and not migrations and not names_map:
        return text
    if index is None:
        index = _build_link_index({}, names_map or {})

    parse_result, _state = _MISTUNE_PARSER.parse(text)
    del _state
    if isinstance(parse_result, str):
        return text

    md_urls = [
        url for url in _collect_md_link_urls(parse_result) if _is_rewritable_target(url)
    ]
    if not md_urls:
        return text

    destination_ranges = _find_link_destination_ranges(text)
    if not destination_ranges:
        return text

    # Build a dict from AST-detected URLs for content-based matching.
    # This avoids fragile 1:1 sequential matching which desyncs when
    # _find_link_destination_ranges finds extra ]( patterns.
    ast_urls_by_unquoted: dict[str, str] = {}
    for url in md_urls:
        ast_urls_by_unquoted[unquote(url)] = url

    edits: list[tuple[int, int, str]] = []
    for dest_start, dest_end, destination in destination_ranges:
        if not _is_rewritable_target(destination):
            continue
        # Match by unquoted content against AST-detected URLs.
        expected_url = ast_urls_by_unquoted.get(unquote(destination))
        if expected_url is None:
            continue
        new_url = _rewrite_link_target(
            expected_url,
            migrations,
            names_map=names_map,
            index=index,
        )
        if unquote(new_url) != unquote(destination):
            edits.append((dest_start, dest_end, new_url))

    if not edits:
        return text

    rewritten = text
    for dest_start, dest_end, new_url in reversed(edits):
        rewritten = rewritten[:dest_start] + new_url + rewritten[dest_end:]
    return rewritten


def _heading_plain_text(children: Sequence[Mapping[str, Any]]) -> str:
    """Concatenate plain text of heading children, stripping inline markup."""
    parts: list[str] = []
    for child in children:
        raw = child.get("raw")
        if isinstance(raw, str):
            parts.append(raw)
            continue
        nested = child.get("children")
        if isinstance(nested, list):
            parts.append(_heading_plain_text(nested))
    return "".join(parts)


def _rewrite_markdown_headings(
    text: str,
    names_map: Mapping[str, str],
    migrations: Mapping[str, str] | None = None,
    *,
    index: _LinkIndex | None = None,
) -> str:
    """Fix heading-text casing at all levels (``#``-``######``).

    Resolves the plain text of every top-level ATX heading through *index*
    (built from *names_map* when omitted) and applies stem *migrations* on
    top, so renamed or re-cased titles propagate to headings at every
    level. A heading is prose, so a name the map does not hold is left
    alone rather than guessed at: the lowercase-first-char fallback would
    lowercase ``Hubble's law`` and ``Python implementation``.
    YAML frontmatter and fenced code blocks are excluded. Idempotent on
    already-canonical headings.
    """
    if not names_map and index is None:
        return text
    if index is None:
        index = _build_link_index({}, names_map)

    parse_result, _state = _MISTUNE_PARSER.parse(text)
    del _state
    if isinstance(parse_result, str):
        return text

    # Byte ranges of fenced code blocks (raw is the exact source slice).
    code_ranges: list[tuple[int, int]] = []
    pos = 0
    for token, _depth, _parents in _walk_tokens(parse_result):
        raw = token.get("raw")
        if token.get("type") != "block_code" or not isinstance(raw, str):
            continue
        found = text.find(raw, pos)
        if found >= 0:
            code_ranges.append((found, found + len(raw)))
            pos = found + len(raw)

    # Top-level ATX headings, paired 1:1 with heading source lines in
    # document order. Nested headings (blockquote/list) never match the
    # line regex, and block_code tokens cover fenced code lines.
    heading_tokens = [
        token
        for token, depth, _parents in _walk_tokens(parse_result)
        if depth == 0 and token.get("type") == "heading" and token.get("style") == "atx"
    ]
    if not heading_tokens:
        return text

    edits: list[tuple[int, int, str]] = []
    token_index = 0
    in_frontmatter = False
    line_offset = 0
    for line in text.splitlines(keepends=True):
        line_start = line_offset
        line_offset += len(line)
        stripped = line.strip()
        if line_start == 0 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter and stripped == "---":
            in_frontmatter = False
            continue
        match = _ATX_HEADING_RE.match(line)
        if match is None:
            continue
        if any(start < line_offset and line_start < end for start, end in code_ranges):
            # ATX-like line inside fenced code: the parser creates no
            # heading token for it, so do not consume one.
            continue
        if token_index >= len(heading_tokens):
            break
        token = heading_tokens[token_index]
        token_index += 1
        if in_frontmatter:
            # Phantom heading tokens the parser creates inside YAML
            # frontmatter (e.g. ``# comment``): consumed, never edited.
            continue
        inner = match["inner"]
        children = token.get("children")
        plain = _heading_plain_text(children) if isinstance(children, list) else ""
        if not plain:
            continue
        new_plain = _resolve_plain(
            plain,
            index=index,
            replace_underscores=False,
        )
        if migrations is not None:
            new_plain = migrations.get(new_plain, new_plain)
        if new_plain == plain:
            continue
        inner_start = line_start + match.start("inner")
        inner_end = line_start + match.end("inner")
        rewritten_inner = _rewrite_plain_span(inner, plain, new_plain)
        edits.append((inner_start, inner_end, rewritten_inner))

    if not edits:
        return text

    rewritten = text
    for start, end, replacement in reversed(edits):
        rewritten = rewritten[:start] + replacement + rewritten[end:]
    return rewritten


def _rewrite_article_heading(text: str, new_heading: str) -> str:
    """Replace the first ``#`` heading after optional YAML frontmatter."""
    lines = text.splitlines(keepends=True)
    in_frontmatter = False
    for index, line in enumerate(lines):
        stripped = line.strip()
        if index == 0 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("# "):
            line_ending = line[len(line.rstrip("\r\n")) :]
            lines[index] = f"# {new_heading}{line_ending}"
            break
    return "".join(lines)
