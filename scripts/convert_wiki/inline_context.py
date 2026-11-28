"""Structural queries on the HTML tree for inline/display-math and box context.

These pure functions inspect the tree to determine whether an element is
in an inline context, contains display-math-only content, or is adjacent
to display-math nodes.  They are used by converter handlers to adjust
prefix/suffix spacing without duplicating the same tree walks.
"""

from __future__ import annotations

import re

from bs4 import NavigableString, PageElement, Tag

from .template_config import _BOXED_CLASSES

"""Matches a suppressed left border in an inline ``style`` attribute."""
_BORDERLESS_STYLE_RE = re.compile(r"\bborder-left-style\s*:\s*none\b", re.IGNORECASE)
"""Ancestors whose layout a box indent would break."""
_BOX_HOST_TAGS = ("li", "td", "th")

"""Exported names from this module."""
__all__ = ()


def _in_inline_context(ele: Tag) -> bool:
    """Check if element is inside a handler that provides block spacing.

    Returns True when the image/audio appears inside an element whose
    handler already injects its own block-level spacing (``\\n`` or
    ``\\n\\n``), so the image/audio should NOT add its own ``\\n\\n``.

    Excludes ``<p>`` because the ``<p>`` handler's ``\\n\\n`` suffix
    goes *after* the entire element, not between its children.
    Excludes ``<div>`` and ``<figure>`` for similar block-level
    separation reasons.
    """
    for p in ele.parents:
        if not isinstance(p, Tag):
            continue
        if p.name in {"li", "td", "th", "div", "figure"}:
            return p.name != "div" and p.name != "figure"
    return False


def _is_display_math_only(ele: Tag) -> bool:
    """Return True if *ele* is a <p> whose sole child is display math."""
    if ele.name != "p":
        return False
    children = [
        c
        for c in ele.children
        if not (isinstance(c, NavigableString) and not c.strip())
    ]
    if len(children) != 1:
        return False
    child = children[0]
    if not isinstance(child, Tag):
        return False
    class_str = " ".join(child.get_attribute_list("class"))
    return "mwe-math-element" in class_str and "mwe-math-element-block" in class_str


def _significant_children(tag: Tag) -> list[PageElement]:
    """Return *tag*'s children excluding whitespace-only text nodes."""
    return [
        c
        for c in tag.children
        if not (isinstance(c, NavigableString) and not c.strip())
    ]


def _is_texhtml_formula_element(ele: PageElement) -> bool:
    """Return True if *ele* is a ``span.texhtml`` formula element."""
    return (
        isinstance(ele, Tag)
        and ele.name == "span"
        and "texhtml" in frozenset(ele.get_attribute_list("class"))
    )


def _is_mwe_math_element(ele: PageElement) -> bool:
    """Return True if *ele* is an ``mwe-math-element`` wrapper."""
    return isinstance(ele, Tag) and "mwe-math-element" in " ".join(
        ele.get_attribute_list("class")
    )


def _dd_first_formula_element(dd: Tag) -> Tag | None:
    """Return the first formula element of *dd*, if any."""
    children = _significant_children(dd)
    if not children or not isinstance(children[0], Tag):
        return None
    first = children[0]
    if _is_mwe_math_element(first) or _is_texhtml_formula_element(first):
        return first
    return None


def _dd_display_formula_element(dd: Tag) -> Tag | None:
    """Return the sole/primary formula element of a display-formula ``<dd>``.

    Matches a ``<dd>`` whose substantive content is one formula element
    (``mwe-math-element`` or ``span.texhtml``) optionally followed by
    trailing sentence punctuation.  Used to qualify and promote
    display-formula ``<dl>`` rows.
    """
    children = _significant_children(dd)
    if not children or not isinstance(children[0], Tag):
        return None
    first = children[0]
    if not (_is_mwe_math_element(first) or _is_texhtml_formula_element(first)):
        return None
    if len(children) == 1:
        return first
    if len(children) == 2 and isinstance(children[1], NavigableString):
        if children[1].strip() in {".", ","}:
            return first
    return None


def _is_display_formula_dl(ele: Tag) -> bool:
    """Return True if *ele* is a display-formula ``<dl>``.

    Generalizes display-math-only ``<dl>`` detection to include texhtml
    formula rows (and sole display-math elements), so join/indent logic
    and block-math rendering apply consistently.
    """
    if ele.name != "dl":
        return False
    children = _significant_children(ele)
    if not children:
        return False
    if not all(isinstance(c, Tag) and c.name == "dd" for c in children):
        return False
    first_row = children[0]
    if not isinstance(first_row, Tag):
        return False
    first_formula = _dd_first_formula_element(first_row)
    if first_formula is None:
        return False
    # Multi-row display-formula blocks: preserve existing display-math-only
    # behavior (a math-leading first row makes the whole all-<dd> block one
    # equation block).
    if len(children) > 1:
        return True
    # Single-row: accept sole/primary display formulas, merged inline math,
    # and rows that carry trailing content (formula + punctuation/prose).
    dd_children = _significant_children(first_row)
    if _is_texhtml_formula_element(first_formula):
        return _dd_display_formula_element(first_row) is not None
    if _is_mwe_math_element(first_formula):
        class_str = " ".join(first_formula.get_attribute_list("class"))
        if "mwe-math-element-block" in class_str:
            return True
        if first_formula.get("data-merged-inline") is not None:
            return True
    if ele.get("data-dl-display-math-join") is not None:
        return True
    return len(dd_children) >= 2


def _is_sole_formula_dd_row(row: Tag) -> bool:
    """Return True if *row* has no meaningful non-math text content.

    Sole-formula rows inside non-display ``<dl>``s are left to the
    block-math path and must not be indented as prose definition rows.
    """
    for string in row.find_all(string=True):
        text = str(string).strip()
        if not text:
            continue
        parent = string.parent
        if isinstance(parent, Tag):
            if parent.find_parent("math"):
                continue
            if parent.find_parent(
                class_=lambda classes: (
                    bool(classes)
                    and any(
                        token in " ".join(classes).lower()
                        for token in (
                            "mwe-math",
                            "texhtml",
                            "mjx",
                            "katex",
                            "mathjax",
                        )
                    )
                )
            ):
                continue
            if parent.name in {"annotation", "script", "style"}:
                continue
        if text.strip(" \t\n\r\f\v.,;:"):
            return False
    return True


def _is_indented_dd_row(row: Tag) -> bool:
    """Return True if *row* is a prose ``<dd>`` that should be indented.

    True when all hold: ``row.name == "dd"``; parent is a ``<dl>``; parent
    is not a display-formula ``<dl>``; the row has text; the row has
    meaningful non-math text content (sole-formula rows inside
    non-display ``<dl>``s are left to the block-math path); the row
    contains no ``ul``, ``ol``, or ``table`` descendant.

    Known quirks (T10): (1) A prose ``<dd>`` wrapping a nested prose
    ``<dl>`` gets two indents inline (``&nbsp;... outer&nbsp;... inner``).
    Base output already glues the rows; no fixture has the shape.
    (2) A ``<dt>`` in a prose ``<dl>`` stays unindented -- correct, since
    Wikipedia renders the term flush and the description indented.
    """
    if row.name != "dd":
        return False
    parent = row.parent
    if not isinstance(parent, Tag) or parent.name != "dl":
        return False
    if _is_display_formula_dl(parent):
        return False
    if row.find_parent(["td", "th"]) is not None:
        return False
    if row.find_parent("li") is not None:
        return False
    # Post-list continuation: <dl> directly after <li>/<ul>/<ol> uses the
    # " <p> " joiner and must not be indented as a prose definition row.
    prev = parent.previous_sibling
    while prev is not None:
        if isinstance(prev, NavigableString):
            if prev.strip():
                break
        elif isinstance(prev, Tag):
            if prev.name not in {"link", "style"}:
                if prev.name in {"li", "ul", "ol"}:
                    return False
                break
        prev = prev.previous_sibling
    if not row.get_text(strip=True):
        return False
    if _is_sole_formula_dd_row(row):
        return False
    if row.find(["ul", "ol", "table"]) is not None:
        return False
    return True


def _is_indented_box_blockquote(ele: Tag) -> bool:
    """Return True if *ele* is a borderless ``<blockquote>`` box to indent.

    Wikipedia draws a theorem or linear-programme box as a ``<blockquote>``
    whose inline style suppresses the quote border
    (``border-left-style: none``).  The box is set off by indentation in the
    source article, so it is indented here as one block level.

    True when all hold: ``ele.name == "blockquote"``; no class is in
    ``_BOXED_CLASSES`` (those render with a ``>`` prefix, which already
    indents); the inline style suppresses the left border; no ``li``,
    ``td``, or ``th`` ancestor; the element has text; and the element
    contains no ``ul``, ``ol``, or ``table`` descendant, since a nested list
    or table carries its own layout and must not be prefixed.
    """
    if ele.name != "blockquote":
        return False
    if _BOXED_CLASSES & frozenset(ele.get_attribute_list("class")):
        return False
    if not _BORDERLESS_STYLE_RE.search(str(ele.get("style", ""))):
        return False
    if ele.find_parent(_BOX_HOST_TAGS) is not None:
        return False
    if not ele.get_text(strip=True):
        return False
    return ele.find(["ul", "ol", "table"]) is None


def _dl_follows_p(ele: Tag) -> bool:
    """Return True if *ele* is a <dl> whose previous sibling is a <p>."""
    prev = ele.find_previous_sibling()
    while isinstance(prev, Tag) and prev.name in {"link", "style"}:
        prev = prev.find_previous_sibling()
    return isinstance(prev, Tag) and prev.name == "p"
