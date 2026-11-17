"""Stem resolution for Wikipedia page titles.

Single source of truth for mapping a Wikipedia title to a local filename
stem (no ``.md`` extension).
"""

from collections.abc import Mapping

from .utils import _fix_name_maybe, _fix_stem

"""Exported names from this module."""
__all__ = ()

"""Stems that name no linkable file."""
_UNUSABLE_STEMS = frozenset({"", ".", ".."})


def _stem_for_title(
    title: str,
    names_map: Mapping[str, str] | None = None,
) -> str:
    """Map a Wikipedia page title to a local filename stem.

    A stem that sanitises to nothing, ``.``, or ``..`` names no linkable
    file, so the title is rejected instead of producing ``.md`` or a
    dot-file.
    """
    stem = _fix_stem(
        _fix_name_maybe(
            title,
            replace_underscores=True,
            names_map=names_map,
        )
    )
    if stem in _UNUSABLE_STEMS:
        msg = f"title {title!r} has no usable filename stem"
        raise ValueError(msg)
    return stem
