"""Structural queries on the HTML tree for inline/display-math context.

These pure functions inspect the tree to determine whether an element is
in an inline context, contains display-math-only content, or is adjacent
to display-math nodes.  They are used by converter handlers to adjust
prefix/suffix spacing without duplicating the same tree walks.
"""

from __future__ import annotations

from bs4 import NavigableString, PageElement, Tag

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


def _is_display_math_only_dl(ele: Tag) -> bool:
    """Return True if *ele* is a <dl> whose content is display math.

    Matches a <dl> whose children are all <dd> rows and whose first row
    starts with display math (block or inline).  Multi-row <dl>s are
    equation blocks whose rows are joined on one line.  A single-row
    <dl> must additionally carry trailing text (e.g. "for events
    satisfying ...") or be a merged multi-part math span.
    """
    return _is_display_formula_dl(ele)


def _dl_follows_p(ele: Tag) -> bool:
    """Return True if *ele* is a <dl> whose previous sibling is a <p>."""
    prev = ele.find_previous_sibling()
    while isinstance(prev, Tag) and prev.name in {"link", "style"}:
        prev = prev.find_previous_sibling()
    return isinstance(prev, Tag) and prev.name == "p"
