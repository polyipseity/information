"""Data types used by the Wikipedia HTML-to-Markdown converter.

Contains ``_RedirectInfo``, ``_RedirectStatus``, ``_HandlerConfig``,
``_RedirectItem``, ``_NormalizedItem``, ``_ApiQueryBody``, and
``_ApiResponse``.
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


@dataclass(frozen=True)
class _RedirectStatus:
    """Live redirect status of a Wikipedia page title.

    Unlike ``_RedirectInfo`` (a cache entry), this is a probe result that
    always reflects the current state of the wiki.

    Attributes
    ----------
    to:
        Redirect target title, or the title itself when the page is not a
        redirect.
    tofragment:
        Section fragment of the redirect target.
    missing:
        Whether the page is missing or invalid (both are treated
        conservatively as absent).
    final_to:
        Terminal target of the redirect chain; ``""`` means the same as
        ``to`` (no chain).  Only meaningful for redirects.
    """

    to: str
    tofragment: str = ""
    missing: bool = False
    final_to: str = ""


"""Type alias for a single redirect entry from the MediaWiki API response."""
_RedirectItem = TypedDict(
    "_RedirectItem",
    {
        "from": str,  # Original page title (required)
        "to": NotRequired[str],  # Redirect target title
        "tofragment": NotRequired[str],  # Section fragment
    },
)

"""Type alias for a single title-normalization entry from the MediaWiki API response."""
_NormalizedItem = TypedDict(
    "_NormalizedItem",
    {
        "from": str,  # Original (sent) page title (required)
        "to": str,  # Canonical page title (required)
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

    pageid: int
    title: str
    missing: bool
    invalid: bool
    invalidreason: str
    imageinfo: list[_ImageInfo]


class _ApiQueryBody(TypedDict, total=False):
    """The ``query`` section of a MediaWiki API response."""

    normalized: list[_NormalizedItem]
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
