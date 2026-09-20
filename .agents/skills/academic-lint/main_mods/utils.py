"""Utility routines shared by the academic-notes validator.

This module contains text-processing helpers, frontmatter parsing, preview
excerpt generation, AST utilities, session header parsing, and other small
functions shared between the validator and tests.
"""

import re
from collections.abc import Iterator
from dataclasses import dataclass
from typing import TypedDict

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

from .models import AstNode, PreviewEntry, SessionHeader, ValidationMessage

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
    "ast_heading_level",
    "AstHeading",
    "AstSection",
    # session/AST shared helpers
    "_MD",
    "SEMESTER_HEADER_RE",
    "SEMESTER_RE",
    "SESSION_HEADING_RE",
    "extract_ast_heading_positions",
    "is_recurrent_index",
    "parse_session_headers",
    # string helpers
    "html_cpt",
    # markdown link helpers
    "InlineLink",
    "iter_inline_links",
    "MalformedLink",
    "iter_malformed_links",
    "parse_list_link",
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
"""Regex matching the ``YYYY term`` prefix of a recurrent course's session headings."""
SEMESTER_RE = r"\d{4}\s+(?:spring|summer|fall|winter)"

"""Regex matching session headings: ``## week N type [number]``, or ``### YYYY term week N type [number]`` in a recurrent course."""
SESSION_HEADING_RE = re.compile(
    r"^(?P<level>#{2,3})\s+"
    r"(?:(?P<semester>" + SEMESTER_RE + r")\s+)?"
    r"week\s+(?P<week>\d+)\s+(?P<type>(?:lecture|lab|tutorial)(?:\s+\d+)?)\s*$",
    re.IGNORECASE | re.MULTILINE,
)

"""Regex matching a level-2 semester header, ``## YYYY term``, used by recurrent-course rules."""
SEMESTER_HEADER_RE = re.compile(
    r"^##\s+(\d{4})\s+(spring|summer|fall|winter)\s*$",
    re.IGNORECASE | re.MULTILINE,
)

"""Regex matching the ``- status: recurrent`` line that marks a course index recurrent."""
_RECURRENT_STATUS_RE = re.compile(
    r"^[ \t]*- status:\s*recurrent\b", re.IGNORECASE | re.MULTILINE
)


def is_recurrent_index(text: str) -> bool:
    """Report whether *text* declares ``- status: recurrent`` in its identity block.

    The identity block runs from the ``# index`` heading to the first level-2
    heading, so a ``status:`` line belonging to a session entry never counts.
    """
    match = FRONT_RE.match(text)
    body = text[match.end() :] if match else text
    first_section = re.search(r"^##\s", body, re.MULTILINE)
    header = body[: first_section.start()] if first_section else body
    return bool(_RECURRENT_STATUS_RE.search(header))


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


# markdown link helpers ------------------------------------------------------


@dataclass(frozen=True)
class InlineLink:
    """A parsed inline Markdown link ``[text](destination)``.

    All offsets are byte positions into the text that was scanned.  ``start``
    is the opening ``[`` and ``end`` is one past the closing ``)``.
    """

    start: int
    end: int
    text: str
    text_start: int
    destination: str
    destination_start: int


def _walk_destination(text: str, index: int) -> int | None:
    """Return the index of the ``)`` closing the link destination at *index*.

    *index* points just past the destination's opening ``(``.  The destination
    is read with a parenthesis-depth counter, so paths that contain balanced
    parentheses (``cache%20(computing).md``) survive intact.  Returns ``None``
    when the destination is unterminated: a raw line break or the end of the
    text arrives before the parentheses balance, which is the case for a
    truncated link such as ``[x](path.md_``.  Stopping at the line break keeps
    such a link from swallowing the rest of the file.
    """
    depth = 1
    while index < len(text):
        char = text[index]
        if char == "\n":
            return None
        if char == "\\":
            index += 2
            continue
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return None


def _scan_inline_link(text: str, start: int) -> InlineLink | None:
    """Parse the inline link beginning at ``text[start] == '['``.

    Returns ``None`` when *start* does not begin a well-formed inline link.
    """
    if start >= len(text) or text[start] != "[":
        return None
    close = text.find("]", start + 1)
    if close < 0 or close + 1 >= len(text) or text[close + 1] != "(":
        return None
    end = _walk_destination(text, close + 2)
    if end is None:
        return None
    return InlineLink(
        start=start,
        end=end + 1,
        text=text[start + 1 : close],
        text_start=start + 1,
        destination=text[close + 2 : end],
        destination_start=close + 2,
    )


def iter_inline_links(text: str) -> Iterator[InlineLink]:
    """Yield every inline Markdown link in *text*.

    The naive ``[^)]+`` destination pattern stops at the first ``)``, so a
    link to a path containing parentheses is either rejected outright or
    silently skipped by rules that match on it.  This scanner tracks
    parenthesis depth and backslash escapes instead.  A destination that
    reaches a line break is not a link and is skipped.
    """
    index = 0
    while True:
        start = text.find("[", index)
        if start < 0:
            return
        link = _scan_inline_link(text, start)
        if link is None:
            index = start + 1
            continue
        yield link
        index = link.end


@dataclass(frozen=True)
class MalformedLink:
    """An inline link whose destination is never closed by ``)``.

    All offsets are byte positions into the text that was scanned.  ``start``
    is the opening ``[`` and ``end`` is where the scan stopped: the raw line
    break or end of text that interrupted the destination.
    """

    start: int
    end: int


def iter_malformed_links(text: str) -> Iterator[MalformedLink]:
    """Yield every inline link whose destination is never closed by ``)``.

    :func:`iter_inline_links` silently skips a destination that reaches a raw
    line break, so a truncated link such as ``[x](path.md_`` resolves to
    nothing and no rule can see it.  This scanner reports those links so they
    can be flagged instead of ignored.  Scanning resumes after the truncation
    point, so a single broken link yields one result.
    """
    index = 0
    while True:
        start = text.find("[", index)
        if start < 0:
            return
        index = start + 1
        close = text.find("]", start + 1)
        if close < 0 or close + 1 >= len(text) or text[close + 1] != "(":
            continue
        if _walk_destination(text, close + 2) is not None:
            continue
        newline = text.find("\n", close + 2)
        end = len(text) if newline < 0 else newline
        yield MalformedLink(start=start, end=end)
        index = end + 1


def parse_list_link(line: str) -> InlineLink | None:
    """Return the link when *line* is exactly ``- [text](destination)``.

    The bullet may be ``-`` or ``*``, leading whitespace is ignored, and
    nothing may follow the closing parenthesis.  A line with any other shape
    returns ``None``.  Offsets in the result refer to *line* as passed in.
    """
    stripped = line.strip()
    if not stripped or stripped[0] not in "-*":
        return None
    rest = stripped[1:].lstrip()
    if not rest.startswith("["):
        return None
    link = _scan_inline_link(stripped, len(stripped) - len(rest))
    if link is None or not link.text.strip():
        return None
    if stripped[link.end :].strip():
        return None
    return link


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


def extract_ast_heading_positions(ast: list[AstNode] | None, text: str) -> set[int]:
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
            needle = f"{'#' * ast_heading_level(node, 2)} {raw_text}"
            idx = text.find(needle)
            # Consume previously-found positions so duplicates aren't lost.
            while idx in positions and idx != -1:
                idx = text.find(needle, idx + len(needle))
            if idx != -1:
                positions.add(idx)
    return positions


def parse_session_headers(
    text: str, ast: list[AstNode] | None = None
) -> list[SessionHeader]:
    """Extract session heading metadata from *text*.

    Matches ``## week N lecture|lab|tutorial [number]`` and, for a recurrent
    course, ``### YYYY term week N lecture|lab|tutorial [number]``.  When
    *ast* is provided, results are filtered to positions that correspond to
    real AST headings (excluding false positives from code blocks or
    comments).

    Returns one :class:`SessionHeader` per heading found.
    """
    ast_positions = (
        extract_ast_heading_positions(ast, text) if ast is not None else None
    )
    headers: list[SessionHeader] = []
    for m in SESSION_HEADING_RE.finditer(text):
        # Skip matches that don't correspond to real AST headings.
        # Only filter when we actually found AST positions: an empty
        # set means no headings in AST, so keep all regex matches.
        if ast_positions and m.start() not in ast_positions:
            continue
        headers.append(
            SessionHeader(
                semester=" ".join((m.group("semester") or "").split()).lower(),
                week=m.group("week"),
                type=" ".join(m.group("type").split()).lower(),
                heading=m.group(0).strip(),
                pos=m.start(),
            )
        )
    return headers


# AST helpers (mistune) ------------------------------------------------------


class AstHeading(TypedDict):
    """Summary of one heading produced by :func:`ast_headings`."""

    type: str
    level: int
    text: str
    node: AstNode


class AstSection(TypedDict):
    """One heading-delimited section produced by :func:`ast_sections`."""

    heading: AstNode | None
    children: list[AstNode]


def ast_heading_level(node: AstNode, default: int) -> int:
    """Return the heading level recorded in *node*'s ``attrs``.

    Mistune stores the ATX/Setext level as an integer under ``attrs``.
    *default* is returned when the parser omits the attribute or records a
    non-integer value, preserving the callers' fallback semantics.
    """
    level = node.get("attrs", {}).get("level", default)
    return level if isinstance(level, int) else default


def iter_ast(nodes: list[AstNode]) -> Iterator[AstNode]:
    """Recursively yield all AST nodes depth-first pre-order from *nodes*."""
    for node in nodes:
        yield node
        children = node.get("children")
        if children:
            yield from iter_ast(children)


def filter_ast(nodes: list[AstNode], node_type: str) -> Iterator[AstNode]:
    """Yield only AST nodes whose ``type`` equals *node_type*."""
    return (n for n in iter_ast(nodes) if n.get("type") == node_type)


def ast_collect_text(node: AstNode) -> str:
    """Collect all ``raw`` text from *node* and its children recursively."""

    def _walk(n: AstNode, parts: list[str]) -> None:
        """Recursively collect raw text from an AST node into parts list."""
        if "raw" in n:
            parts.append(n["raw"])
        for c in n.get("children", []):
            _walk(c, parts)

    parts: list[str] = []
    _walk(node, parts)
    return "".join(parts)


def ast_headings(ast_nodes: list[AstNode]) -> list[AstHeading]:
    """Return summary dicts for every heading in *ast_nodes*.

    Each result has keys ``type``, ``level``, ``text``, ``node``.
    """
    result: list[AstHeading] = []
    for node in filter_ast(ast_nodes, "heading"):
        result.append(
            {
                "type": "heading",
                "level": ast_heading_level(node, 1),
                "text": ast_collect_text(node),
                "node": node,
            }
        )
    return result


def ast_sections(ast_nodes: list[AstNode]) -> list[AstSection]:
    """Split the top-level AST into heading-delimited sections.

    Returns a list of dicts with keys ``heading`` (the heading node, or
    ``None`` for the preamble) and ``children`` (non-heading nodes in that
    section).  ``blank_line`` nodes are silently dropped.
    """
    sections: list[AstSection] = []
    current_children: list[AstNode] = []
    current_heading: AstNode | None = None

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


def _segment_paragraphs(text: str) -> list[tuple[str, int, int]]:
    """Segment *text* into paragraphs with blockquote stripping.

    Returns a list of ``(stripped_text, start_offset, end_offset)`` tuples
    where ``start_offset`` and ``end_offset`` are byte offsets into the
    original ``text``.  A paragraph is a maximal run of consecutive
    non-blank lines (blank lines = ``\n\n`` boundaries).  Leading
    ``> `` / ``> > `` / etc. blockquote prefixes are stripped from each
    line when building ``stripped_text``.

    Empty paragraphs (consecutive blank lines) produce no entries.
    """
    result: list[tuple[str, int, int]] = []
    if not text:
        return result

    # Split on blank lines (\n\n boundaries).
    # We need to track byte offsets, so work with the raw string.
    paragraphs: list[tuple[int, int]] = []  # (start, end) byte offsets
    start = 0
    i = 0
    n = len(text)
    last_added_end = -1  # track end of last added paragraph
    while i < n:
        # Find next blank line (\n\n)
        nl = text.find("\n", i)
        if nl == -1:
            # Rest of text is one paragraph
            paragraphs.append((start, n))
            last_added_end = n
            break
        # Check if next line is also blank
        if nl + 1 < n and text[nl + 1] == "\n":
            # Found blank line; paragraph ends before the blank
            if start < nl:  # non-empty paragraph
                paragraphs.append((start, nl))
                last_added_end = nl
            # Skip blank lines
            i = nl + 2
            while i < n and text[i] == "\n":
                i += 1
            start = i
        else:
            i = nl + 1

    # Handle last paragraph if text doesn't end with blank line
    # and we haven't already added it
    if start < n and last_added_end != n:
        paragraphs.append((start, n))

    # Process each paragraph: strip blockquote prefixes
    blockquote_re = re.compile(r"^(?:\s*>\s*)+")
    for para_start, para_end in paragraphs:
        raw_para = text[para_start:para_end]
        lines = raw_para.splitlines(keepends=True)
        stripped_lines: list[str] = []
        for line in lines:
            # Remove trailing newline for processing
            content = line.rstrip("\n")
            m = blockquote_re.match(content)
            if m:
                # Strip the blockquote prefix
                stripped = content[m.end() :]
            else:
                stripped = content
            stripped_lines.append(stripped)
        stripped_text = "\n".join(stripped_lines)
        result.append((stripped_text, para_start, para_end))

    return result
