"""Utility functions for the Wikipedia HTML-to-Markdown converter.

Pure helper functions with no class dependencies.
"""

import re
from collections.abc import Mapping
from re import Pattern, compile
from urllib.parse import unquote

from bs4 import BeautifulSoup, Tag
from bs4.element import NavigableString
from yarl import URL

from . import config as _cfg

"""Exported names from this module."""
__all__ = ()


"Regex for matching GFM table separator cells (e.g. ``---``, ``:--``, ``--:``, ``:-:``)."
_SEPARATOR_CELL_RE: Pattern[str] = compile(r":?-+:?")


def _fix_name_maybe(
    name: str,
    *,
    normalize: bool = True,
    replace_underscores: bool = False,
    names_map: Mapping[str, str] | None = None,
) -> str:
    """Normalise a Wikipedia page title via the name map with fallback.

    Applies a single sequential heuristic:
    1. Normalise nbsp-to-space if *normalize* is True (default).
    2. Look up in *names_map* (defaults to ``_cfg._NAMES_MAP``).
       Return immediately if found.
    3. If *replace_underscores* is True, replace ``_`` with `` ``.
    4. Retry lookup with the (potentially underscore-replaced) name.
       If still not found, apply the lowercase-first-char fallback:
       ``name[1:].islower() or len(name) <= 1`` → lowercase first character.
    """
    names_map = names_map if names_map is not None else _cfg._NAMES_MAP
    if normalize:
        name = name.replace("\u00a0", " ")
    if name in names_map:
        return names_map[name]
    if replace_underscores:
        name = name.replace("_", " ")
        if name in names_map:
            return names_map[name]
    if len(name) > 1 and name[1:].islower():
        return name[0].lower() + name[1:]
    return name


def _fix_filename(name: str) -> str:
    """Replace filesystem-unsafe characters with underscores."""
    return _cfg._BAD_CHARACTERS.sub("_", name)


def _get_image_filename(ele: Tag) -> str | None:
    """Extract the original uploaded filename from an ``<img>`` element.

    Returns the filename without ``File:`` prefix (e.g. ``Modernphysicsfields.svg``)
    or ``None`` if it cannot be determined from either ``resource`` or ``src``.
    """
    if resource := ele.get("resource"):
        src_url = _cfg._WIKI_HOST_URL.join(URL(str(resource)))
        src_url_str = src_url.human_repr()
        for regex in _cfg._ARCHIVE_REGEXES:
            if match := regex.search(src_url_str):
                return unquote(match[1]).replace("_", " ")
    if src := ele.get("src"):
        src_url = _cfg._WIKI_HOST_URL.join(URL(str(src)))
        src_url_str = src_url.human_repr()
        for regex in _cfg._ARCHIVE_REGEXES:
            if match := regex.search(src_url_str):
                return unquote(match[1]).replace("_", " ")
    return None


def _markdown_fragment(fragment: str) -> str:
    """Return a URL fragment string suitable for a Markdown link anchor."""
    return (
        fragment
        and f"#{fragment.replace(':', '').replace(' ', '%20').replace('/', '%2F')}"
    )


def _markdown_link_target(page: str, fragment: str = "") -> str:
    """Build a relative Markdown link target for a given page name and fragment."""
    return f"{_fix_filename(page).replace(' ', '%20')}.md{_markdown_fragment(fragment)}"


def _tag_affixes(name: str) -> tuple[str, str]:
    """Return the opening and closing HTML tag strings for the given tag name."""
    return f"<{name}>", f"</{name}>"


def _bs4_new_element(html: str) -> Tag | NavigableString:
    """Parse a minimal HTML fragment into a single BeautifulSoup element."""
    soup = BeautifulSoup(html, "html.parser")
    element = next(iter(soup), None)
    if element is None or isinstance(element, NavigableString):
        msg = f"Could not parse HTML: {html!r}"
        raise ValueError(msg)
    if not isinstance(element, Tag):
        msg = f"Expected a Tag element, got {type(element).__name__}: {html!r}"
        raise ValueError(msg)
    return element


def _balance_brackets(text: str) -> str:
    """Escape unbalanced ``[`` and ``]`` in *text*.

    Uses a two-pass stack algorithm:
    - Pass 1: scan left-to-right, track unmatched ``[`` positions on a stack.
              A ``]`` pops the stack if non-empty (matched pair) or is marked
              unbalanced if empty. Remaining stack positions at EOF are
              unclosed ``[``.
    - Pass 2: backslash-escape all unbalanced brackets.

    Balanced ``[...]`` pairs pass through unchanged per CommonMark \u00a76.3.
    Escaped ``\\[``/``\\]`` are inert per CommonMark \u00a72.4.
    """
    _stack: list[int] = []
    _unbalanced: set[int] = set()
    for _i, _c in enumerate(text):
        if _c == "[":
            _stack.append(_i)
        elif _c == "]":
            if _stack:
                _stack.pop()
            else:
                _unbalanced.add(_i)
    _unbalanced.update(_stack)
    if _unbalanced:
        _chars = list(text)
        for _i in sorted(_unbalanced):
            _chars[_i] = "\\" + _chars[_i]
        return "".join(_chars)
    return text


def _is_separator_cell(cell: str) -> bool:
    """Check if a table cell is a GFM separator (e.g. ---, :--, --:, :-:)."""
    return bool(_SEPARATOR_CELL_RE.fullmatch(cell)) and len(cell) >= 3


def _get_separator_alignment(cell: str) -> str:
    """Extract the GFM alignment marker from a separator cell."""
    if cell.startswith(":") and cell.endswith(":"):
        return ":-:"
    if cell.endswith(":"):
        return "--:"
    if cell.startswith(":"):
        return ":--"
    return "---"


def _format_separator_cell(width: int, alignment: str) -> str:
    """Build a separator cell padded to the given column width."""
    width = max(width, 3)
    if alignment == "---":
        return "-" * width
    if alignment == ":--":
        return ":" + "-" * (width - 1)
    if alignment == "--:":
        return "-" * (width - 1) + ":"
    # :-:
    return ":" + "-" * (width - 2) + ":"


"""Characters that are zero-width in terminal display but count as width 1 in
Python ``len()``.  MD060 (table-column-style) fires when these skew column
widths.  Strip them from table cell content before computing widths."""
_ZERO_WIDTH_CHARS_RE = re.compile("[\u200b\u200c\u200d\u2060\ufeff]")


def _parse_table_row(line: str) -> list[str] | None:
    """Parse a pipe-table row into cell contents.  Returns None if the line
    is not a valid table row."""
    line = line.rstrip("\n")
    if not (line.startswith("|") and line.endswith("|")):
        return None
    inner = line[1:-1]  # strip outer pipes
    return [_ZERO_WIDTH_CHARS_RE.sub("", p.strip()) for p in inner.split(" | ")]


def _pad_table_block(lines: list[str]) -> list[str]:
    """Reformat a pipe-table block with columns padded to the widest cell per
    column.  Expects at least 2 rows including one separator row."""
    if len(lines) < 2:
        return lines

    parsed: list[list[str]] = []
    sep_indices: list[int] = []
    for i, line in enumerate(lines):
        cells = _parse_table_row(line)
        if cells is None:
            return lines  # not a valid table — pass through unchanged
        parsed.append(cells)
        if len(cells) > 0 and all(_is_separator_cell(c) for c in cells):
            sep_indices.append(i)

    if not sep_indices:
        return lines

    ncols = max(len(cells) for cells in parsed)

    # Get alignment per column from the first separator row.
    alignments: list[str] = []
    for j in range(ncols):
        sep_row_idx = sep_indices[0]
        sep_cell = parsed[sep_row_idx][j] if j < len(parsed[sep_row_idx]) else ""
        alignments.append(_get_separator_alignment(sep_cell))

    # Column width = max content width across all content rows (not separators).
    col_widths = [0] * ncols
    for i, cells in enumerate(parsed):
        if i in sep_indices:
            continue
        for j in range(len(cells)):
            col_widths[j] = max(col_widths[j], len(cells[j]))

    # Ensure every column is at least 3 characters wide (GFM minimum).
    col_widths = [max(w, 3) for w in col_widths]

    result: list[str] = []
    for i, cells in enumerate(parsed):
        padded = list(cells)
        while len(padded) < ncols:
            padded.append("")

        if i in sep_indices:
            sep_cells = [
                _format_separator_cell(col_widths[j], alignments[j])
                for j in range(ncols)
            ]
            result.append("| " + " | ".join(sep_cells) + " |")
        else:
            data_cells = [
                _cfg._JUSTIFY_MAP[alignments[j]](padded[j], col_widths[j])
                for j in range(ncols)
            ]
            result.append("| " + " | ".join(data_cells) + " |")

    return result


def _pad_table_blocks(text: str) -> str:
    """Find all pipe-table blocks in *text* and pad columns to the widest
    content per column."""
    lines = text.split("\n")
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("|") and line.endswith("|"):
            block: list[str] = [line]
            i += 1
            while (
                i < len(lines) and lines[i].startswith("|") and lines[i].endswith("|")
            ):
                block.append(lines[i])
                i += 1
            result.extend(_pad_table_block(block))
        else:
            result.append(line)
            i += 1
    return "\n".join(result)
