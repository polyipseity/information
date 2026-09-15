"""Shared constants and template configuration for convert_wiki.

Single source of truth for constants previously duplicated across
converter.py, pipeline.py, and table.py. Template class sets are
loaded from JSONC on first access.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path as PathlibPath
from re import Pattern
from typing import Any

import json5

"""Exported names from this module."""
__all__ = ()

"""Path to the JSONC template configuration file."""
_TEMPLATE_CONFIG_PATH = (
    PathlibPath(__file__).resolve(strict=True).parent.parent
    / "assets"
    / "convert_wiki.templates.jsonc"
)


def _load_template_config(
    path: PathlibPath | None = None,
) -> dict[str, Any]:
    """Load and return the template configuration from JSONC."""
    resolved = path or _TEMPLATE_CONFIG_PATH
    with open(resolved, "rt", encoding="UTF-8") as f:
        return json5.load(f)


"""Parsed template configuration loaded from JSONC."""
_config: dict[str, Any] = _load_template_config()

# --- Display math containers (previously in converter.py and pipeline.py) ---

"""HTML tags whose children may contain display math."""
_DISPLAY_MATH_CONTAINERS: frozenset[str] = frozenset(_config["display_math_containers"])

# --- Table formatting regexes (previously duplicated in table.py) ---

"""Regex matching Markdown table separator cells."""
_SEPARATOR_CELL_RE: Pattern[str] = re.compile(r":?-+:?")
"""Matches a leading blockquote prefix (one or more ``>`` markers, each followed by whitespace)."""
_BLOCKQUOTE_PREFIX_RE: Pattern[str] = re.compile(r"^(>\s+)+")
"""Collapse consecutive newlines into at most two."""
_CONSECUTIVE_NEWLINES_REGEX: Pattern[str] = re.compile(r"\n\n+")
"""Replace leading whitespace with non-breaking spaces."""
_CONSECUTIVE_LEADING_WHITESPACES_REGEX: Pattern[str] = re.compile(
    r"(?:^|\n)([ \t]+)", re.MULTILINE
)

# --- Template class sets (previously in converter.py) ---

"""CSS classes that render as boxed/bordered blocks."""
_BOXED_CLASSES: frozenset[str] = frozenset(_config["boxed_classes"])
"""Box-like classes whose content renders as a blockquote (excludes equation-box)."""
_BLOCKQUOTE_CLASSES: frozenset[str] = frozenset(
    c for c in _config["boxed_classes"] if c != "equation-box"
)
"""CSS classes whose content should not be reformatted."""
_OPAQUE_SPAN_CLASSES: frozenset[str] = _BOXED_CLASSES | frozenset(
    _config["opaque_span_classes_extra"]
)
"""HTML tags for embedded media (audio, video)."""
_MEDIA_TAGS: frozenset[str] = frozenset(_config["media_tags"])
"""Self-closing HTML tags that have no children."""
_ATOMIC_TAGS: frozenset[str] = frozenset(_config["atomic_tags"])
"""Block-level HTML tags that prevent inline-only classification."""
_BLOCK_TAGS: frozenset[str] = frozenset(_config["block_tags"])

# --- Display math environments (previously in converter.py) ---

"""LaTeX environment names that render as display math."""
_DISPLAY_MATH_ENVIRONMENTS: tuple[str, ...] = tuple(
    _config["display_math_environments"]
)

# --- Inline list classes (previously hardcoded "portalbox") ---

"""CSS classes that produce inline list rendering."""
_INLINE_LIST_CLASSES: frozenset[str] = frozenset(
    _config.get("inline_list_classes", ["portalbox"])
)


# --- Navbox spec (previously hardcoded in table.py) ---


@dataclass(frozen=True)
class NavboxSpec:
    """Dataclass defining navbox table column layout and constraints."""

    linear_indices: tuple[int, ...]
    angular_indices: tuple[int, ...]
    title_style_pattern: str
    min_inner_table_rows: int
    required_outer_classes: frozenset[str]
    required_tr_count: int


def _load_navbox_spec(config: dict[str, Any]) -> NavboxSpec:
    """Parse navbox configuration and return a NavboxSpec."""
    nb: dict[str, Any] = config.get("navbox", {})
    layout: dict[str, Any] = nb.get("column_layout", {})
    return NavboxSpec(
        linear_indices=tuple(layout.get("linear_indices", [0, 2, 3, 4])),
        angular_indices=tuple(layout.get("angular_indices", [5, 6, 7, 8])),
        title_style_pattern=nb.get("title_style_pattern", "font-size:114%"),
        min_inner_table_rows=nb.get("min_inner_table_rows", 3),
        required_outer_classes=frozenset(
            nb.get("required_outer_classes", ["navbox-inner"])
        ),
        required_tr_count=nb.get("required_tr_count", 2),
    )


"""Specification for Wikimedia navbox table layout."""
_NAVBOX_SPEC: NavboxSpec = _load_navbox_spec(_config)


# --- Sidebar spec (previously hardcoded in table.py) ---


@dataclass(frozen=True)
class SidebarWrapRule:
    """Rule for wrapping sidebar list items in a specific tag."""

    css_class: str
    wrap_tag: str
    scope: str  # "li" or "children"


@dataclass(frozen=True)
class SidebarSpec:
    """Specification for sidebar table trigger classes and wrap rules."""

    trigger_classes: frozenset[str]
    wrap_rules: tuple[SidebarWrapRule, ...]
    caption_class: str
    caption_tag: str


def _load_sidebar_spec(config: dict[str, Any]) -> SidebarSpec:
    """Parse sidebar configuration and return a SidebarSpec."""
    sb: dict[str, Any] = config.get("sidebar", {})
    return SidebarSpec(
        trigger_classes=frozenset(sb.get("trigger_classes", ["sidebar", "cm-sidebar"])),
        wrap_rules=tuple(
            SidebarWrapRule(
                css_class=r["class"],
                wrap_tag=r["tag"],
                scope=r["scope"],
            )
            for r in sb.get("wrap_rules", [])
        ),
        caption_class=sb.get("caption_class", "sidebar-caption"),
        caption_tag=sb.get("caption_tag", "i"),
    )


"""Specification for Wikipedia sidebar table layout."""
_SIDEBAR_SPEC: SidebarSpec = _load_sidebar_spec(_config)


# --- Infobox caption rules (previously hardcoded in table.py) ---


@dataclass(frozen=True)
class InfoboxCaptionRule:
    """Rule for transforming a single infobox caption cell."""

    cell_tag: str
    cell_class: str
    wrap_tag: str | None


def _load_infobox_captions(
    config: dict[str, Any],
) -> tuple[InfoboxCaptionRule, ...]:
    """Parse infobox caption rules from configuration."""
    return tuple(
        InfoboxCaptionRule(
            cell_tag=r["cell_tag"],
            cell_class=r["cell_class"],
            wrap_tag=r.get("wrap_tag"),
        )
        for r in config.get("infobox_captions", [])
    )


"""Rules for transforming infobox caption rows."""
_INFOBOX_CAPTION_RULES: tuple[InfoboxCaptionRule, ...] = _load_infobox_captions(_config)
