"""Data types used by the Wikipedia HTML-to-Markdown converter.

Contains ``_RedirectInfo``, ``_HandlerConfig``, ``_RedirectItem``,
``_ApiQueryBody``, and ``_ApiResponse``.
"""

from collections.abc import Callable
from dataclasses import dataclass
from typing import NotRequired, TypedDict

"""Exported names from this module."""
__all__ = ()


@dataclass(frozen=True)
class _RedirectInfo:
    """Resolved redirect information for a Wikipedia page title."""

    to: str
    tofragment: str = ""
    cached_at: str = ""


"""Type alias for a single redirect entry from the MediaWiki API response."""
_RedirectItem = TypedDict(
    "_RedirectItem",
    {
        "from": str,  # Original page title (required)
        "to": NotRequired[str],  # Redirect target title
        "tofragment": NotRequired[str],  # Section fragment
    },
)


class _ExtMetadataValue(TypedDict, total=False):
    """A single value in the ``extmetadata`` dict of an ``imageinfo`` entry."""

    value: str


class _ImageInfo(TypedDict, total=False):
    """A single ``imageinfo`` entry for a page in a MediaWiki API response."""

    extmetadata: dict[str, _ExtMetadataValue]


class _ApiPage(TypedDict, total=False):
    """A ``page`` entry in the ``query`` section of a MediaWiki API response."""

    title: str
    imageinfo: list[_ImageInfo]


class _ApiQueryBody(TypedDict, total=False):
    """The ``query`` section of a MediaWiki API response."""

    redirects: list[_RedirectItem]
    pages: list[_ApiPage]


class _ApiResponse(TypedDict, total=False):
    """A MediaWiki ``action=query`` API response with redirects and pages."""

    query: _ApiQueryBody


@dataclass
class _HandlerConfig:
    """Configuration for a tag handler in the WikiHtmlConverter.

    Attributes
    ----------
    prefix:
        String prepended to the inner text of a tag.
    suffix:
        String appended to the inner text of a tag.
    joiner:
        String used to join inner child results.
    process_strings:
        Callback for post-processing the concatenated inner text.
    full_result:
        Whether to return the processed result as-is, bypassing the
        ``prefix``/``suffix`` wrapping in ``WikiHtmlConverter.convert()``.
    list_stack:
        Override for the list nesting stack.
    """

    prefix: str = ""
    suffix: str = ""
    joiner: str = ""
    process_strings: Callable[[str], str] = staticmethod(lambda s: s)
    full_result: bool = False
    list_stack: tuple[int, ...] | None = None
