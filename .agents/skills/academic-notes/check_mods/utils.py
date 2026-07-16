"""Utility routines shared by the academic-notes validator.

This module contains text-processing helpers, frontmatter parsing, preview
excerpt generation, AST utilities, session header parsing, and other small
functions shared between the validator and tests.
"""

import re
from collections.abc import Iterator

import mistune
from anyio import Path
from mistune.plugins.formatting import strikethrough as _mistune_strikethrough
from mistune.plugins.math import (
    math as _mistune_math,
)
from mistune.plugins.math import (
    math_in_list as _mistune_math_in_list,
)
from mistune.plugins.math import (
    math_in_quote as _mistune_math_in_quote,
)
from mistune.plugins.table import table as _mistune_table

from .models import PreviewEntry, ValidationMessage

"""Public symbols exported by this module."""
__all__ = (
    "parse_frontmatter",
    "has_flash_tag",
    "locate",
    "locate_range",
    "get_excerpt",
    "aggregate",
    "DEFAULT_PATHS",
    "FRONT_RE",
    # AST helpers
    "iter_ast",
    "filter_ast",
    "ast_collect_text",
    "ast_headings",
    "ast_sections",
    # session/AST shared helpers
    "_MD",
    "SESSION_HEADING_RE",
    "extract_ast_heading_positions",
    "parse_session_headers",
    # string helpers
    "html_cpt",
)

# shared mistune parser (AST output) used by validator and tests
"""A mistune Markdown parser configured for AST output."""
_MD = mistune.create_markdown(
    renderer="ast",
    plugins=[
        _mistune_strikethrough,
        _mistune_table,
        _mistune_math,
        _mistune_math_in_quote,
        _mistune_math_in_list,
    ],
)

"""Default root directories scanned when no paths are supplied on the command line."""
DEFAULT_PATHS = ["special/academia", "private/special/academia"]

# LF/CRLF line endings.
"""Regex matching YAML frontmatter block (--- ... ---) with optional CRLF."""
FRONT_RE = re.compile(r"\A\s*---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)", re.DOTALL)

# flashcard tag matcher used by metadata rules
"""Regex matching the flashcard activation tag prefix in frontmatter tags."""
FLASH_TAG_RE = re.compile(r"flashcard/active/special/academia/", re.IGNORECASE)

# Regex for ## week N lecture|lab|tutorial [number] headings, used by session rules.
"""Regex matching session headings: ``## week N type [number]``."""
SESSION_HEADING_RE = re.compile(
    r"^##\s+week\s+(\d+)\s+((?:lecture|lab|tutorial)(?:\s+\d+)?)\s*$",
    re.IGNORECASE | re.MULTILINE,
)


# location helpers -----------------------------------------------------------


def locate(text: str, idx: int) -> tuple[int, int]:
    """Return 1-based (line, col) corresponding to byte offset *idx*."""
    line = text.count("\n", 0, idx) + 1
    last_n = text.rfind("\n", 0, idx)
    col = idx - last_n
    return line, col


def locate_range(text: str, start: int, length: int) -> tuple[int, int, int]:
    """Return (line, col, col_end) for a span at *start* of *length* bytes.

    *col_end* is the 1-based column index of the last character in the span.
    When the span is entirely on one line this is simply ``col + length - 1``.
    If the span crosses a newline we intentionally truncate *col_end* to the
    end of the first line of the span.  Many of our rules only report the
    starting line, and the caret generation logic in :func:`get_excerpt`
    assumes *col_end* refers to that same line.  Previously we calculated
    ``col_end`` using the full length even when newlines were present, which
    produced wildly oversized carets (the issue reported in
    ``latex_single_line`` caret output).  This helper now handles the
    newline case correctly.
    """
    line, col = locate(text, start)
    # look for a newline within the span; if found, limit the column end to the
    # character just before that newline so caret markers stay on the first
    # line.  Otherwise fall back to the naive calculation.
    span = text[start : start + length]
    nl_index = span.find("\n")
    if nl_index != -1:
        # nl_index is zero-based offset within span; subtract one to point at
        # the preceding character (if nl_index==0 the span starts with a
        # newline, which is unusual but we treat col_end==col).
        col_end = col + max(0, nl_index - 1)
    else:
        col_end = col + max(0, length - 1)
    return line, col, col_end


# frontmatter helpers --------------------------------------------------------


def parse_frontmatter(text: str) -> str | None:
    """Extract YAML frontmatter from *text*.

    Returns the raw YAML body (without the ``---`` fences) or ``None`` if
    frontmatter is absent.
    """
    m = FRONT_RE.match(text)
    return m.group(1) if m else None


def has_flash_tag(front: str) -> bool:
    """Return ``True`` if a flashcard activation tag appears in *front*.

    The check is case-insensitive and only looks for the generic
    ``special/academia`` prefix; more specific path-derived checks live in the
    ``rules`` module.
    """
    return bool(FLASH_TAG_RE.search(front))


# excerpt/preview logic ------------------------------------------------------


async def get_excerpt(
    path: Path,
    msg: str,
    line: int | None = None,
    col: int | None = None,
    col_end: int | None = None,
    chars: int = 200,
) -> tuple[str, str | None]:
    """Generate a short preview snippet for *msg* in *path*.

    Returns ``(excerpt, caret)``; ``caret`` may be ``None`` when the
    snippet does not need a pointer line.
    """
    try:
        text = await path.read_text(encoding="utf-8")
    except Exception:  # pragma: no cover - best effort
        return "(no preview available)", None

    if line is not None:
        lines = text.splitlines()
        if 1 <= line <= len(lines):
            full = lines[line - 1].rstrip("\n")
            # Skip lone LaTeX delimiters to show the next real content line
            if full.strip() in ("$", "$$") and line < len(lines):
                nxt = lines[line]
                if nxt.strip():
                    full = nxt.rstrip("\n")
                    if col is not None:
                        col = 1
                        col_end = len(full) if full else 1
            if col is not None:
                start_idx = max(0, min(col - 1, len(full)))
                width = (col_end - col + 1) if (col_end and col_end >= col) else 1
                if len(full) > chars:
                    half = chars // 2
                    win_start = max(0, start_idx - half)
                    # Build windowed display with ellipses
                    seg_len = chars
                    end = min(len(full), win_start + seg_len)
                    pref = "..." if win_start > 0 else ""
                    suf = "..." if end < len(full) else ""
                    avail = chars - len(pref) - len(suf)
                    segment = full[
                        win_start : min(len(full), win_start + max(0, avail))
                    ]
                    display = pref + segment + suf
                    # Adjust window if caret falls outside
                    if start_idx < win_start:
                        win_start2 = start_idx
                        pref2 = "..." if win_start2 > 0 else ""
                        end2 = min(len(full), win_start2 + chars - len(pref2))
                        suf2 = "..." if end2 < len(full) else ""
                        avail2 = chars - len(pref2) - len(suf2)
                        segment2 = full[
                            win_start2 : min(len(full), win_start2 + avail2)
                        ]
                        display = pref2 + segment2 + suf2
                    elif start_idx >= end:
                        seg_len_no_ellipsis = len(segment)
                        if pref:
                            seg_len_no_ellipsis = len(segment)
                        if suf:
                            pass
                        win_start2 = max(0, start_idx - seg_len_no_ellipsis // 2)
                        pref2 = "..." if win_start2 > 0 else ""
                        end2 = min(len(full), win_start2 + chars - len(pref2))
                        suf2 = "..." if end2 < len(full) else ""
                        avail2 = chars - len(pref2) - len(suf2)
                        segment2 = full[
                            win_start2 : min(len(full), win_start2 + avail2)
                        ]
                        display = pref2 + segment2 + suf2
                    caret_start = (
                        start_idx - win_start + (3 if display.startswith("...") else 0)
                    )
                else:
                    display = full
                    caret_start = start_idx
                max_width = len(display) - caret_start
                actual_width = min(width, max(1, max_width))
                return display.strip(), " " * caret_start + "^" * actual_width
            return full.strip(), None
    fm: str | None = parse_frontmatter(text)
    if "frontmatter" in msg.lower() or "tags:" in msg.lower():
        if fm:
            lines = fm.strip().splitlines()[:6]
            if lines:
                return "\n".join(lines), None
        return text[:chars], None
    # fallback: skip frontmatter and markup lines, return first content line
    body = text
    if fm:
        m2 = FRONT_RE.match(text)
        if m2:
            body = text[m2.end() :]
    for ln in body.splitlines():
        stripped = ln.strip()
        if not stripped or stripped[0] in ("#", "-", "*"):
            continue
        return (stripped[: chars - 3].rstrip() + "...") if len(
            stripped
        ) > chars else stripped, None
    return text[:chars].strip().replace("\n", " "), None


# JSON helper used by CLI when ``--json`` is requested
async def aggregate(
    items: list[tuple[Path, ValidationMessage]], width: int
) -> dict[str, list[PreviewEntry]]:
    """Aggregate messages into a structure suitable for JSON output.

    The returned dictionary is keyed by *rule ID* (``key_id``) rather than the
    entire message string.  Each value is itself a dict containing the
    original message text (without the ``[severity/id]`` prefix), the
    severity level, and a list of :class:`PreviewEntry` objects under the
    ``entries`` key.  This makes downstream consumers (both console and
    JSON) easier to work with.

    ``width`` is used to compute a sensible excerpt length based on terminal
    size; the caller already knows this so we avoid coupling to the rich
    module here.
    """
    agg: dict[str, list[PreviewEntry]] = {}
    chars = max(20, width - 1)
    for p, err in items:
        excerpt, caret = await get_excerpt(
            p, err.msg, err.line, err.col, err.col_end, chars=chars
        )
        entry = PreviewEntry(
            path=p, excerpt=excerpt, msg=err.msg, severity=err.severity
        )
        if caret:
            entry.caret = caret
        if err.line is not None:
            entry.line = err.line
        if err.col is not None:
            entry.col = err.col
        agg.setdefault(err.rule_id, []).append(entry)
    return agg


# AST/session helpers (mistune) --------------------------------------------


def extract_ast_heading_positions(ast: list[dict] | None, text: str) -> set[int]:
    """Return set of byte positions where the AST finds real headings.

    Skips headings inside code blocks or comments that regex might match
    but the Markdown parser does not recognise as real headings.
    """
    positions: set[int] = set()
    if not ast:
        return positions
    for node in iter_ast(ast):
        if node.get("type") == "heading":
            raw_text = ast_collect_text(node)
            needle = f"{'#' * node.get('attrs', {}).get('level', 2)} {raw_text}"
            idx = text.find(needle)
            # Consume previously-found positions so duplicates aren't lost.
            while idx in positions and idx != -1:
                idx = text.find(needle, idx + len(needle))
            if idx != -1:
                positions.add(idx)
    return positions


def parse_session_headers(
    text: str, ast: list[dict] | None = None
) -> list[tuple[str, str, str, int]]:
    """Extract session heading metadata from *text*.

    Looks for ``## week N lecture|lab|tutorial [number]`` headings.  When
    *ast* is provided, results are filtered to only include positions that
    correspond to real AST headings (excluding false positives from code
    blocks or comments).

    Returns a list of ``(week, type, raw_heading, byte_pos)`` tuples.
    """
    ast_positions = (
        extract_ast_heading_positions(ast, text) if ast is not None else None
    )
    headers: list[tuple[str, str, str, int]] = []
    for m in SESSION_HEADING_RE.finditer(text):
        # Skip matches that don't correspond to real AST headings.
        # Only filter when we actually found AST positions: an empty
        # set means no headings in AST, so keep all regex matches.
        if ast_positions and m.start() not in ast_positions:
            continue
        headers.append(
            (m.group(1), m.group(2).strip().lower(), m.group(0).strip(), m.start())
        )
    return headers


# AST helpers (mistune) ------------------------------------------------------


def iter_ast(nodes: list[dict]) -> Iterator[dict]:
    """Recursively yield all AST nodes depth-first pre-order from *nodes*."""
    for node in nodes:
        yield node
        children = node.get("children")
        if children:
            yield from iter_ast(children)


def filter_ast(nodes: list[dict], node_type: str) -> Iterator[dict]:
    """Yield only AST nodes whose ``type`` equals *node_type*."""
    return (n for n in iter_ast(nodes) if n.get("type") == node_type)


def ast_collect_text(node: dict) -> str:
    """Collect all ``raw`` text from *node* and its children recursively."""

    def _walk(n: dict, parts: list[str]) -> None:
        """Recursively collect raw text from an AST node into parts list."""
        if "raw" in n:
            parts.append(n["raw"])
        for c in n.get("children", []):
            _walk(c, parts)

    parts: list[str] = []
    _walk(node, parts)
    return "".join(parts)


def ast_headings(ast_nodes: list[dict]) -> list[dict]:
    """Return summary dicts for every heading in *ast_nodes*.

    Each result has keys ``type``, ``level``, ``text``, ``node``.
    """
    result: list[dict] = []
    for node in filter_ast(ast_nodes, "heading"):
        result.append(
            {
                "type": "heading",
                "level": node.get("attrs", {}).get("level", 1),
                "text": ast_collect_text(node),
                "node": node,
            }
        )
    return result


def ast_sections(ast_nodes: list[dict]) -> list[dict]:
    """Split the top-level AST into heading-delimited sections.

    Returns a list of dicts with keys ``heading`` (the heading node, or
    ``None`` for the preamble) and ``children`` (non-heading nodes in that
    section).  ``blank_line`` nodes are silently dropped.
    """
    sections: list[dict] = []
    current_children: list[dict] = []
    current_heading: dict | None = None

    for node in ast_nodes:
        if node.get("type") == "heading":
            if current_heading is not None or current_children:
                sections.append(
                    {"heading": current_heading, "children": current_children}
                )
            current_heading = node
            current_children = []
        elif node.get("type") != "blank_line":
            current_children.append(node)

    if current_heading is not None or current_children:
        sections.append({"heading": current_heading, "children": current_children})

    return sections


# string helpers --------------------------------------------------------------


def html_cpt(text: str) -> str:
    """Return an HTML comment containing *text*.

    This helper exists because the agent's file-editing tools treat
    the HTML comment open delimiter as an HTML comment and mangle
    literal occurrences in Python source strings.  Using this
    function avoids that tool artifact.
    """
    return "<!-- " + text + " -->"
