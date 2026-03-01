"""Utility routines shared by the academic-notes validator.

Constants
---------

DEFAULT_PATHS -- roots scanned when no paths are supplied on the command line


This module contains text-processing helpers, frontmatter parsing, preview
excerpt generation, and other small functions that are not rules themselves.
"""

import re

from anyio import Path

from .models import PreviewEntry, ValidationMessage

__all__ = (
    "parse_frontmatter",
    "has_flash_tag",
    "locate",
    "locate_range",
    "get_excerpt",
    "aggregate",
    "DEFAULT_PATHS",
    "FRONT_RE",
)

# regex used by parse_frontmatter; accepts optional whitespace and both

DEFAULT_PATHS = ["special/academia", "private/special/academia"]

# LF/CRLF line endings.
FRONT_RE = re.compile(r"\A\s*---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)", re.DOTALL)

# flashcard tag matcher used by metadata rules
FLASH_TAG_RE = re.compile(r"flashcard/active/special/academia/", re.IGNORECASE)


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

    The returned tuple is ``(excerpt, caret)``; ``caret`` may be ``None`` if
    the snippet does not require a pointer line.  The heuristics are tuned to
    produce useful excerpts for backend JSON output and console display.
    """
    try:
        text = await path.read_text(encoding="utf-8")
    except Exception:  # pragma: no cover - best effort
        return "(no preview available)", None

    if line is not None:
        lines = text.splitlines()
        if 1 <= line <= len(lines):
            full = lines[line - 1].rstrip("\n")
            # If the trimmed line is merely a LaTeX delimiter we prefer to show
            # the next line of real math content (if any).  This makes error
            # previews more helpful when the dollar sign sits alone on its own
            # line, as often happens when authors split inline math across
            # multiple lines for readability.  When we switch, adjust both
            # *col* and *col_end* so that the caret spans the *entire* replacement
            # line rather than just the first column; this gives a visual sense of
            # the full LaTeX expression that triggered the rule.
            if full.strip() in ("$", "$$") and line < len(lines):
                nxt = lines[line]
                if nxt.strip():
                    full = nxt.rstrip("\n")
                    if col is not None:
                        col = 1
                        # highlight the whole line
                        col_end = len(full) if full else 1
            if col is not None:
                start_idx = max(0, min(col - 1, len(full)))
                if col_end and col_end >= col:
                    width = col_end - col + 1
                else:
                    width = 1
                # determine display window
                if len(full) > chars:
                    half = chars // 2
                    win_start = max(0, start_idx - half)

                    def make_display(ws: int) -> tuple[str, int]:
                        """Return a windowed display string of length *chars* starting at *ws*.

                        The function builds a snippet with ellipses if the window does not
                        include the start/end of the full line.  It also returns the
                        absolute end index within *full* of the returned segment, which
                        is used by the caller to adjust the caret position.
                        """
                        seg_len = chars
                        end = min(len(full), ws + seg_len)
                        pref = "..." if ws > 0 else ""
                        suf = "..." if end < len(full) else ""
                        avail = chars - len(pref) - len(suf)
                        if avail < 0:
                            avail = 0
                        end = min(len(full), ws + avail)
                        segment = full[ws:end]
                        disp = pref + segment + suf
                        return disp, end

                    disp, win_end = make_display(win_start)
                    if start_idx < win_start:
                        win_start = start_idx
                        disp, win_end = make_display(win_start)
                    elif start_idx >= win_end:
                        seg_len = len(disp)
                        if disp.startswith("..."):
                            seg_len -= 3
                        if disp.endswith("..."):
                            seg_len -= 3
                        win_start = max(0, start_idx - seg_len // 2)
                        disp, win_end = make_display(win_start)
                    display = disp
                    caret_start = (
                        start_idx - win_start + (3 if display.startswith("...") else 0)
                    )
                else:
                    display = full
                    caret_start = start_idx
                # ensure caret width does not overflow the displayed snippet
                max_width = len(display) - caret_start
                if max_width < 1:
                    max_width = 1
                actual_width = min(width, max_width)
                caret_line = " " * caret_start + "^" * actual_width
                return display.strip(), caret_line
            return full.strip(), None
    fm: str | None = parse_frontmatter(text)
    if "frontmatter" in msg.lower() or "tags:" in msg.lower():
        if fm:
            lines = fm.strip().splitlines()[:6]
            if lines:
                return "\n".join(lines), None
        return text[:chars], None
    # fallback heuristics
    body = text
    if fm:
        m2 = FRONT_RE.match(text)
        if m2:
            body = text[m2.end() :]
    for ln in body.splitlines():
        stripped = ln.strip()
        if not stripped:
            continue
        if (
            stripped.startswith("#")
            or stripped.startswith("-")
            or stripped.startswith("*")
        ):
            continue
        snippet = stripped
        if len(snippet) > chars:
            avail = max(0, chars - 3)
            snippet = snippet[:avail].rstrip() + "..."
        return snippet, None
    for keyword in ["datetime:", "topic:", "lecture", "lab", "tutorial", "week"]:
        idx = text.lower().find(keyword)
        if idx != -1:
            start = max(0, idx - 60)
            return text[start : start + chars].strip().replace("\n", " "), None
    body = text
    if fm:
        body = text[len(fm) + 4 :]
    for ln in body.splitlines():
        if ln.strip():
            snippet = ln.strip()
            if len(snippet) > chars:
                avail = max(0, chars - 3)
                snippet = snippet[:avail].rstrip() + "..."
            return snippet, None
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
