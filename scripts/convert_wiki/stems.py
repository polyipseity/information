"""Stem resolution for Wikipedia page titles.

Single source of truth for mapping a Wikipedia title to a local filename
stem (no ``.md`` extension).
"""

from collections.abc import Mapping

from .utils import _fix_filename, _fix_name_maybe

"""Exported names from this module."""
__all__ = ()


def _stem_for_title(
    title: str,
    names_map: Mapping[str, str] | None = None,
) -> str:
    """Map a Wikipedia page title to a local filename stem."""
    return _fix_filename(
        _fix_name_maybe(
            title,
            replace_underscores=True,
            names_map=names_map,
        )
    )
