"""Utility functions for the Wikipedia HTML-to-Markdown converter.

Pure helper functions with no class dependencies.
"""

import re
from collections.abc import Mapping
from os import PathLike
from re import Pattern, compile
from urllib.parse import unquote

from anyio import Path
from bs4 import Tag
from yarl import URL

from . import config as _cfg
from .ast_utils import (
    _all_code_span_ranges,
    _all_math_ranges,
    _find_table_blocks,
    _is_in_span,
)

"""Exported names from this module."""
__all__ = ()


"""Regex for matching GFM table separator cells (e.g. ``---``, ``:--``, ``--:``,
``:-:``)."""
_SEPARATOR_CELL_RE: Pattern[str] = compile(r":?-+:?")


async def _find_child_exact(parent: Path, name: str) -> Path | None:
    """Return the child entry only when its basename equals *name* exactly."""
    async for entry in parent.iterdir():
        if entry.name == name:
            return entry
    return None


async def _unlink_case_colliding_symlinks(parent: Path, name: str) -> None:
    """Remove symlink children that differ from *name* only by letter case."""
    name_lower = name.lower()
    async for entry in parent.iterdir():
        if entry.name != name and entry.name.lower() == name_lower:
            if await entry.is_symlink():
                await entry.unlink()


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


async def _symlink_to_idempotent(
    path: Path,
    target: str,
    *,
    target_is_directory: bool = False,
) -> None:
    """Create *path* → *target* unless an equivalent symlink already exists.

      Concurrent converters may race to create the same redirect symlink; treat
    a matching existing symlink as success and re-raise only on conflict.
    """
    try:
        await path.symlink_to(target, target_is_directory=target_is_directory)
    except FileExistsError:
        if not (await path.is_symlink() and str(await path.readlink()) == target):
            raise


async def _create_redirect_symlinks(
    wiki_dir: PathLike[str],
    wiki_lang_dir: PathLike[str],
    from_filename: str,
    to_filename: str,
) -> None:
    """Create or retarget redirect symlinks for a renamed page.

    The language-directory symlink ``{from_filename}.md`` is retargeted when
    it already exists as a symlink pointing at a different file, left
    untouched when it already points at ``{to_filename}.md``, and never
    replaced when it is a real file.  The top-level mirror is created only
    if missing; an existing mirror (symlink or real file) is never touched.
    """
    wiki_dir_path = Path(wiki_dir)
    wiki_lang_dir_path = Path(wiki_lang_dir)
    redirect_name = f"{from_filename}.md"
    target = f"{to_filename}.md"
    redirect_file = await _find_child_exact(wiki_lang_dir_path, redirect_name)
    if redirect_file is not None:
        if await redirect_file.is_symlink():
            if str(await redirect_file.readlink()) != target:
                await redirect_file.unlink()
                await _unlink_case_colliding_symlinks(wiki_lang_dir_path, redirect_name)
                await _symlink_to_idempotent(
                    wiki_lang_dir_path / redirect_name,
                    target,
                )
    else:
        await _unlink_case_colliding_symlinks(wiki_lang_dir_path, redirect_name)
        await _symlink_to_idempotent(
            wiki_lang_dir_path / redirect_name,
            target,
        )
    mirror_name = redirect_name
    expected_mirror_target = str(
        wiki_lang_dir_path.relative_to(wiki_dir_path) / mirror_name
    )
    mirror_file = await _find_child_exact(wiki_dir_path, mirror_name)
    if mirror_file is not None:
        if await mirror_file.is_symlink():
            if str(await mirror_file.readlink()) != expected_mirror_target:
                await mirror_file.unlink()
                await _unlink_case_colliding_symlinks(wiki_dir_path, mirror_name)
                await _symlink_to_idempotent(
                    wiki_dir_path / mirror_name,
                    expected_mirror_target,
                )
    else:
        await _unlink_case_colliding_symlinks(wiki_dir_path, mirror_name)
        await _symlink_to_idempotent(
            wiki_dir_path / mirror_name,
            expected_mirror_target,
        )


async def _remove_redirect_symlinks(
    wiki_dir: PathLike[str],
    wiki_lang_dir: PathLike[str],
    from_filename: str,
) -> None:
    """Remove the redirect symlinks for a page that is no longer a redirect.

    Unlinks the language-directory symlink ``{from_filename}.md`` and its
    top-level mirror, but only when they are symlinks — a real file at
    either path is never touched (invariant).
    """
    wiki_dir_path = Path(wiki_dir)
    wiki_lang_dir_path = Path(wiki_lang_dir)
    redirect_name = f"{from_filename}.md"
    for parent in (wiki_lang_dir_path, wiki_dir_path):
        redirect_file = await _find_child_exact(parent, redirect_name)
        if redirect_file is not None and await redirect_file.is_symlink():
            await redirect_file.unlink()


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


def _smart_split_row(line: str) -> list[str] | None:
    """Split a pipe-table row into cells.

    Uses ``_all_math_ranges`` and ``_all_code_span_ranges`` to identify
    pipe characters inside math or code spans so they are not treated as
    cell boundaries.  Also respects backslash-escaped pipes (``\\|``).

    Returns ``None`` if the line is not a valid pipe-table row (must start
    and end with ``|``).
    """
    line = line.rstrip("\n")
    if not (line.startswith("|") and line.endswith("|")):
        return None
    inner = line[1:-1]

    # Precompute protected ranges (math and code spans).
    math_ranges = _all_math_ranges(inner)
    code_ranges = _all_code_span_ranges(inner)

    # Collect positions of pipe characters that are outside protected spans
    # and are not backslash-escaped.
    pipes: list[int] = []
    i = 0
    while i < len(inner):
        c = inner[i]
        if c == "\\" and i + 1 < len(inner) and inner[i + 1] == "|":
            # Escaped pipe: skip over it (not a cell boundary)
            i += 2
            continue
        if (
            c == "|"
            and not _is_in_span(i, math_ranges)
            and not _is_in_span(i, code_ranges)
        ):
            pipes.append(i)
        i += 1

    # Split by pipe positions.
    cells: list[str] = []
    start = 0
    for p in pipes:
        cells.append(_ZERO_WIDTH_CHARS_RE.sub("", inner[start:p].strip()))
        start = p + 1
    cells.append(_ZERO_WIDTH_CHARS_RE.sub("", inner[start:].strip()))
    return cells


def _reformat_table_block(block: list[str]) -> list[str]:
    """Reformat a single pipe-table block with columns padded to the widest
    cell per column.

    Uses ``_smart_split_row`` to parse each row, which correctly handles
    pipe characters inside math and code spans.  Expects at least 2 rows
    including one separator row.  Returns the block unchanged if it is not
    a valid pipe table.
    """
    if len(block) < 2:
        return block

    parsed: list[list[str]] = []
    sep_indices: list[int] = []
    for i, line in enumerate(block):
        cells = _smart_split_row(line)
        if cells is None:
            return block
        parsed.append(cells)
        if len(cells) > 0 and all(_is_separator_cell(c) for c in cells):
            sep_indices.append(i)

    if not sep_indices:
        return block

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


def _reformat_table(text: str) -> str:
    """Reformat all pipe-table blocks in *text* with columns padded to the
    widest cell per column.

    Uses ``_find_table_blocks`` (mistune AST) to locate table boundaries,
    then ``_reformat_table_block`` for formatting.
    """
    table_blocks = _find_table_blocks(text)
    if not table_blocks:
        return text

    parts: list[str] = []
    prev_end = 0
    for start, end in table_blocks:
        # Skip blocks that overlap or are before the previous end.
        # ``_find_table_blocks`` can return duplicate/overlapping ranges
        # when mistune's AST contains duplicate table tokens.
        if start < prev_end:
            continue

        # Non-table prefix.
        parts.append(text[prev_end:start])

        # Extract the table block and strip surrounding blank lines.
        block_text = text[start:end]
        lines = block_text.split("\n")

        # Find table content boundaries (lines starting with |).
        first = 0
        while first < len(lines) and not lines[first].startswith("|"):
            first += 1
        last = len(lines) - 1
        while last >= first and not lines[last].startswith("|"):
            last -= 1

        if first <= last:
            # Preserve leading blank lines as part of the prefix.
            if first > 0:
                parts.append("\n".join(lines[:first]) + "\n")

            # Group consecutive pipe lines into separate sub-blocks,
            # so that separate tables within the same AST range are
            # reformatted independently (matching the old heuristic).
            table_slice = lines[first : last + 1]
            reformatted: list[str] = []
            i = 0
            while i < len(table_slice):
                if table_slice[i].startswith("|"):
                    j = i
                    while j < len(table_slice) and table_slice[j].startswith("|"):
                        j += 1
                    sub_block = _reformat_table_block(table_slice[i:j])
                    reformatted.extend(sub_block)
                    i = j
                else:
                    reformatted.append(table_slice[i])
                    i += 1
            parts.append("\n".join(reformatted))

            # Trailing blank lines will be handled by the next prefix
            # (or the final suffix).
            trailing = lines[last + 1 :]
            if trailing:
                parts.append("\n" + "\n".join(trailing))
        else:
            parts.append(block_text)

        prev_end = end
    parts.append(text[prev_end:])
    return "".join(parts)
