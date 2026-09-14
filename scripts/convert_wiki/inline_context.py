"""Structural queries on the HTML tree for inline/display-math context.

These pure functions inspect the tree to determine whether an element is
in an inline context, contains display-math-only content, or is adjacent
to display-math nodes.  They are used by converter handlers to adjust
prefix/suffix spacing without duplicating the same tree walks.
"""

from __future__ import annotations

from bs4 import NavigableString, Tag

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


def _is_display_math_only_dl(ele: Tag) -> bool:
    """Return True if *ele* is a <dl> whose content is display math
    followed by trailing text (e.g. "for events satisfying ...").

    Matches a <dl> with a single <dd> child whose first rendered
    element is display math and whose last rendered element is a
    non-math span or text node (the trailing description).
    """
    if ele.name != "dl":
        return False
    children = [
        c
        for c in ele.children
        if not (isinstance(c, NavigableString) and not c.strip())
    ]
    if (
        len(children) != 1
        or not isinstance(children[0], Tag)
        or children[0].name != "dd"
    ):
        return False
    dd = children[0]
    dd_children = [
        c for c in dd.children if not (isinstance(c, NavigableString) and not c.strip())
    ]
    if not dd_children:
        return False
    # The first child must be a math element (block or inline)
    first = dd_children[0]
    if not isinstance(first, Tag):
        return False
    class_str = " ".join(first.get_attribute_list("class"))
    if "mwe-math-element" not in class_str:
        return False
    # A single merged multi-part math span qualifies — it was
    # assembled from adjacent inline math spans and should be
    # joined inline like the original multi-part form.
    if len(dd_children) == 1 and first.get("data-merged-inline") is not None:
        return True
    # Match as long as the first child is math and there are
    # ≥2 children (ensuring trailing content exists).  The last
    # child may be math (e.g. "$\\Delta x=0\\ $" at the end of
    # "for events satisfying …").
    if len(dd_children) < 2:
        return False
    return True


def _dl_follows_p(ele: Tag) -> bool:
    """Return True if *ele* is a <dl> whose previous sibling is a <p>."""
    prev = ele.find_previous_sibling()
    while isinstance(prev, Tag) and prev.name in {"link", "style"}:
        prev = prev.find_previous_sibling()
    return isinstance(prev, Tag) and prev.name == "p"
