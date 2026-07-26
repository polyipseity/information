"""Mistune AST utility functions for the convert_wiki pipeline.

Provides shared helpers for manipulating Markdown text via mistune's
AST representation, used by ``pipeline.py`` and any refactored modules
that replace fragile regex/string-based post-processing steps.

The core pattern shared by all functions:

1. Parse original Markdown *text* with ``_MISTUNE_PARSER`` to get an AST
   token list.
2. Walk/inspect the AST using helpers here to identify structural features
   (adjacent blockquotes, table dimensions, etc.).
3. Patch the *original text* directly — do not reconstruct from the AST
   (mistune's tokens carry no source-position metadata).

This is the same approach taken by ``pipeline._separate_block_math``.
"""

import re
from collections.abc import Generator, Iterable, Sequence
from typing import Any

import mistune
from mistune.plugins.math import math as _mistune_math
from mistune.plugins.math import math_in_list as _mistune_math_in_list
from mistune.plugins.math import math_in_quote as _mistune_math_in_quote
from mistune.plugins.table import table as _mistune_table

"""Exported names from this module."""
__all__ = (
    "_MISTUNE_PARSER",
    "_TEXT_BLOCK_TYPES",
    "_reconstruct_token_raw",
    "_find_token_range",
    "_walk_tokens",
    "_find_top_level_adjacent",
    "_inject_after_token",
    "_replace_pipes_outside_math",
)

# ---------------------------------------------------------------------------
# Shared parser
# ---------------------------------------------------------------------------

_MISTUNE_PARSER: mistune.Markdown = mistune.create_markdown(
    renderer="ast",
    plugins=[
        _mistune_math,
        _mistune_math_in_list,
        _mistune_math_in_quote,
        _mistune_table,
    ],
)
"""Mistune AST parser configured with math and table plugins.

Use via ``_MISTUNE_PARSER.parse(text: str) -> tuple[list[dict], Any]``.
The first return value is the top-level token list; the second is the
render state (kept for future extensibility but typically unused).
"""

# Token types whose children contain the actual text content (not raw).
_TEXT_BLOCK_TYPES: frozenset[str] = frozenset(
    {
        "block_quote",
        "paragraph",
        "table",
        "list",
        "list_item",
    }
)
"""Token types that use ``children`` rather than a ``raw`` field.

These need special handling in ``_reconstruct_token_raw``."""

# ---------------------------------------------------------------------------
# Token -> approximate source text
# ---------------------------------------------------------------------------


def _reconstruct_token_raw(token: dict[str, Any]) -> str | None:
    """Return an approximate source-text representation of *token*.

    For leaf tokens (``text``, ``block_math``, ``block_code``, ``image``,
    ``link``, ``thematic_break``, etc.) this returns the ``raw`` field.

    For structural tokens like ``block_quote``, ``paragraph``, or
    ``table``, this reconstructs a rough source form from their children.
    The result is a **best-effort** approximation that can be used to
    locate the token in the original text via ``str.find``.

    Returns ``None`` for tokens whose source text cannot be reliably
    approximated (e.g. ``blank_line`` — in the source this is ``\\n\\n``
    but that is ambiguous).  Callers should handle ``None`` by falling
    back to other strategies (e.g. looking at neighboring tokens).

    Parameters
    ----------
    token:
        A single mistune AST dict.

    Returns
    -------
    str or None
        Approximate source-text representation, or ``None``.
    """
    raw: str | None = token.get("raw")
    if raw is not None:
        return raw

    tok_type: str = token["type"]
    children: list[dict[str, Any]] | None = token.get("children")

    if tok_type == "thematic_break":
        return "***"  # or "---"; either works for finding
    if tok_type == "blank_line":
        # ``\n\n`` is too ambiguous to use as a search anchor.
        return None
    if tok_type == "block_code":
        # Block code has ``raw`` in normal cases — just in case.
        return token.get("raw")
    if tok_type == "block_quote":
        if children is None:
            return None
        parts: list[str] = []
        for child in children:
            child_raw = _reconstruct_token_raw(child)
            if child_raw is not None:
                # Prefix each non-empty line with ``> ``.
                for line in child_raw.split("\n"):
                    prefix = "> " if not line.startswith(">") else ""
                    parts.append(prefix + line)
            else:
                # A blank_line inside the blockquote.
                parts.append(">")
        return "\n".join(parts)
    if tok_type == "paragraph" and children is not None:
        all_raw: list[str] = []
        for child in children:
            cr = _reconstruct_token_raw(child)
            if cr is not None:
                all_raw.append(cr)
        return "".join(all_raw) if all_raw else None
    if tok_type == "strong" and children is not None:
        inner = "".join(_reconstruct_token_raw(c) or "" for c in children)
        return f"**{inner}**"
    if tok_type == "emphasis" and children is not None:
        inner = "".join(_reconstruct_token_raw(c) or "" for c in children)
        return f"*{inner}*"
    if tok_type in ("text", "inline_math", "codespan", "linebreak"):
        return token.get("raw")

    # Generic fallback for unknown container types: concatenate children.
    if children is not None:
        all_raw = [_reconstruct_token_raw(c) for c in children]
        non_none = [r for r in all_raw if r is not None]
        return "".join(non_none) if non_none else None

    return None


# ---------------------------------------------------------------------------
# Token position finding
# ---------------------------------------------------------------------------


def _find_token_range(
    text: str,
    tokens: Sequence[dict[str, Any]],
    index: int,
    *,
    _start_pos: int = 0,
) -> tuple[int, int] | None:
    """Find the byte range of the token at *index* in *text*.

    Scans sequentially through *tokens* (starting from ``_start_pos`` in
    the text for efficiency) matching each token's approximate source
    representation against the original *text*.

    Parameters
    ----------
    text:
        The original Markdown text that was parsed to produce *tokens*.
    tokens:
        The top-level token list (or any sequential list).
    index:
        The index of the target token in *tokens*.
    _start_pos:
        Internal: starting position in *text* for the scan.  Callers
        should omit this (it is used internally for recursive calls).

    Returns
    -------
    tuple[int, int] or None
        ``(start, end)`` byte positions, or ``None`` if the token
        cannot be located.
    """
    pos = _start_pos
    for i, tok in enumerate(tokens):
        if i > index:
            break
        raw = _reconstruct_token_raw(tok)
        if raw is not None:
            # ``str.find`` is used because ``raw`` is an approximation.
            found = text.find(raw, pos)
            if found < 0:
                # Approximation failed — try falling back.
                return None
            hit_end = found + len(raw)
            if i == index:
                return (found, hit_end)
            pos = hit_end
        elif i == index:
            # The target token has no raw representation.
            return None
        # Token before target without raw — skip by advancing past it.
        # Use the next token's raw to bound the skip.
        # If no next token, nothing to do.
        if i < len(tokens) - 1:
            _advance_to_next(text, tokens, i, pos)

    return None


def _advance_to_next(
    text: str,
    tokens: Sequence[dict[str, Any]],
    current_idx: int,
    pos: int,
) -> int:
    """Advance *pos* past the token at *current_idx* using the next token.

    When the current token has no raw representation, we try to locate
    the start of the *next* token in the text and use that as the
    new position.  This handles ``blank_line`` and other anchorless
    tokens.
    """
    for j in range(current_idx + 1, len(tokens)):
        next_raw = _reconstruct_token_raw(tokens[j])
        if next_raw is not None:
            nf = text.find(next_raw, pos)
            if nf >= 0:
                return nf
    return pos


# ---------------------------------------------------------------------------
# Token walking
# ---------------------------------------------------------------------------


def _walk_tokens(
    tokens: Iterable[dict[str, Any]],
    token_type: str | None = None,
    *,
    _depth: int = 0,
    _parents: tuple[dict[str, Any], ...] = (),
) -> Generator[tuple[dict[str, Any], int, tuple[dict[str, Any], ...]], None, None]:
    """Recursively yield ``(token, depth, parents)`` for each token.

    When *token_type* is given, only tokens whose ``type`` equals
    *token_type* are yielded.

    Parameters
    ----------
    tokens:
        An iterable of mistune AST dict tokens.
    token_type:
        Optional type filter (e.g. ``"block_quote"``, ``"table"``).
    _depth:
        Current recursion depth (internal, do not pass).
    _parents:
        Chain of ancestor tokens (internal, do not pass).

    Yields
    ------
    (token, depth, parents)
        *token* is the AST dict, *depth* is the nesting level (0 =
        top-level), and *parents* is the chain of ancestor tokens from
        outermost to innermost.
    """
    for token in tokens:
        if token_type is None or token["type"] == token_type:
            yield (token, _depth, _parents)
        children: list[dict[str, Any]] | None = token.get("children")
        if children is not None:
            yield from _walk_tokens(
                children,
                token_type,
                _depth=_depth + 1,
                _parents=_parents + (token,),
            )


# ---------------------------------------------------------------------------
# Adjacency detection
# ---------------------------------------------------------------------------


def _find_top_level_adjacent(
    tokens: Sequence[dict[str, Any]],
    token_type: str,
    *,
    ignore_types: frozenset[str] = frozenset({"blank_line"}),
) -> list[tuple[int, int]]:
    """Find indices of adjacent top-level *token_type* pairs.

    Two tokens of *token_type* are considered adjacent when there are no
    intervening tokens of any other type except those in *ignore_types*.

    Parameters
    ----------
    tokens:
        Top-level token list from mistune.
    token_type:
        Type to search for (e.g. ``"block_quote"``).
    ignore_types:
        Token types that may appear between adjacent pairs without
        breaking adjacency (default: only ``blank_line``).

    Returns
    -------
    list[tuple[int, int]]
        List of ``(first_index, second_index)`` pairs for consecutive
        adjacent groups.  For a group of N consecutive tokens, returns
        N-1 pairs covering all adjacent pairs in order.

    Examples
    --------
    >>> tokens = [
    ...     {"type": "block_quote"},
    ...     {"type": "blank_line"},
    ...     {"type": "block_quote"},
    ... ]
    >>> _find_top_level_adjacent(tokens, "block_quote")
    [(0, 2)]
    """
    # Collect indices of target tokens, then check there are only
    # ignore_types between them.
    target_indices: list[int] = []
    for i, tok in enumerate(tokens):
        if tok["type"] == token_type:
            target_indices.append(i)

    result: list[tuple[int, int]] = []
    for k in range(len(target_indices) - 1):
        first = target_indices[k]
        second = target_indices[k + 1]
        # Check everything between first+1 .. second-1 is ignore_types.
        _all_ignored = True
        for j in range(first + 1, second):
            if tokens[j]["type"] not in ignore_types:
                _all_ignored = False
                break
        if _all_ignored:
            result.append((first, second))

    return result


# ---------------------------------------------------------------------------
# Text patching
# ---------------------------------------------------------------------------


def _inject_after_token(
    text: str,
    tokens: Sequence[dict[str, Any]],
    index: int,
    content: str,
) -> str:
    """Insert *content* immediately after the token at *index* in *text*.

    Works by finding the token's approximate byte range in *text* using
    ``_find_token_range``, then inserting *content* after its end.

    *content* is inserted **inline** — if you need a newline before or
    after, include it in the *content* string yourself.

    Parameters
    ----------
    text:
        The original Markdown text that was parsed to produce *tokens*.
    tokens:
        The top-level token list (must match *text*).
    index:
        Index of the token to inject after.
    content:
        The text to insert.

    Returns
    -------
    str
        The new text with *content* inserted.  If the token cannot be
        located (e.g. no ``_reconstruct_token_raw``), returns *text*
        unchanged.
    """
    rng = _find_token_range(text, tokens, index)
    if rng is None:
        return text
    _start, end = rng
    return text[:end] + content + text[end:]


def _replace_pipes_outside_math(text: str) -> str:
    """Replace ``|`` with ``&#124;`` outside math and with ``\\vert`` inside math.

    Uses mistune AST to correctly identify math boundaries, unlike the
    previous regex approach which could misidentify math in edge cases.
    """
    parse_result, _state = _MISTUNE_PARSER.parse(text)
    del _state
    if isinstance(parse_result, str):
        return text  # Parse error, return unchanged.

    # Collect raw text of all math tokens (inline and block) in tree order.
    math_raws: list[str] = [
        token["raw"]
        for token, _depth, _parents in _walk_tokens(parse_result)
        if token.get("type") in ("inline_math", "block_math")
        and token.get("raw") is not None
    ]

    if not math_raws:
        return text.replace("|", "&#124;")

    # Find positions of each math raw in text, scanning forward
    # to handle duplicates correctly.
    math_ranges: list[tuple[int, int]] = []
    pos = 0
    for raw in math_raws:
        found = text.find(raw, pos)
        if found >= 0:
            math_ranges.append((found, found + len(raw)))
            pos = found + len(raw)

    # Build result by alternating non-math and math segments.
    parts: list[str] = []
    prev_end = 0
    for start, end in math_ranges:
        parts.append(text[prev_end:start].replace("|", "&#124;"))
        parts.append(re.sub(r"(?<!\\)\|", r"\\vert ", text[start:end]))
        prev_end = end
    parts.append(text[prev_end:].replace("|", "&#124;"))

    return "".join(parts)
