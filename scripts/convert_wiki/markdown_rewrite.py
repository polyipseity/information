"""Pure markdown rewriting for reprocess mode."""

import re
from collections.abc import Mapping, Sequence
from typing import Any
from urllib.parse import unquote

from .ast_utils import (
    _MISTUNE_PARSER,
    _collect_md_link_urls,
    _find_link_destination_ranges,
    _walk_tokens,
)
from .utils import _fix_filename, _fix_name_maybe

"""Exported names from this module."""
__all__ = ()


_ATX_HEADING_RE = re.compile(r"^(#{1,6})\s+(?P<inner>\S.*?)(?:\s*#+\s*)?$")


def _encode_stem(stem: str) -> str:
    """Encode a filename stem for a markdown link target."""
    return _fix_filename(stem).replace(" ", "%20")


def _decode_link_stem(target: str) -> tuple[str, str]:
    """Split a link target into ``(stem, fragment)``."""
    page, _, fragment = target.partition("#")
    if not page.endswith(".md"):
        msg = f"not a markdown page link: {target!r}"
        raise ValueError(msg)
    stem = unquote(page.removesuffix(".md"))
    return stem, fragment


def _rewrite_link_target(
    target: str,
    migrations: Mapping[str, str],
) -> str:
    """Rewrite a single markdown link target using stem migrations."""
    stem, fragment = _decode_link_stem(target)
    new_stem = migrations.get(stem, stem)
    encoded = _encode_stem(new_stem)
    return f"{encoded}.md{f'#{fragment}' if fragment else ''}"


def _rewrite_markdown_links(
    text: str,
    migrations: Mapping[str, str],
) -> str:
    """Rewrite markdown ``.md`` link targets according to *migrations*."""
    if not migrations:
        return text

    parse_result, _state = _MISTUNE_PARSER.parse(text)
    del _state
    if isinstance(parse_result, str):
        return text

    md_urls = [url for url in _collect_md_link_urls(parse_result) if ".md" in url]
    if not md_urls:
        return text

    destination_ranges = _find_link_destination_ranges(text)
    if not destination_ranges:
        return text

    edits: list[tuple[int, int, str]] = []
    url_index = 0
    for dest_start, dest_end, destination in destination_ranges:
        if not destination.endswith(".md") and ".md#" not in destination:
            continue
        if url_index >= len(md_urls):
            break
        expected_url = md_urls[url_index]
        url_index += 1
        if destination != expected_url:
            continue
        new_url = _rewrite_link_target(expected_url, migrations)
        if new_url != expected_url:
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
) -> str:
    """Fix heading-text casing at all levels (``#``-``######``).

    Re-applies the ingestion heuristic ``_fix_name_maybe`` (with
    ``replace_underscores=False``) to the plain text of every top-level
    ATX heading, using *names_map*, then applies stem *migrations* on top
    so renamed or re-cased stems propagate to headings at every level.
    YAML frontmatter and fenced code blocks are excluded. Idempotent on
    already-canonical headings.
    """
    if not names_map:
        return text

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
        if not plain or plain not in inner:
            continue
        new_plain = _fix_name_maybe(
            plain,
            replace_underscores=False,
            names_map=names_map,
        )
        if migrations is not None:
            new_plain = migrations.get(new_plain, new_plain)
        if new_plain == plain:
            continue
        inner_start = line_start + match.start("inner")
        idx = inner.find(plain)
        edits.append((inner_start + idx, inner_start + idx + len(plain), new_plain))

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
