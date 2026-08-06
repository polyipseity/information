"""Pure markdown rewriting for reprocess mode."""

import re
from collections.abc import Mapping
from re import Pattern
from urllib.parse import unquote

from .utils import _fix_filename

"""Exported names from this module."""
__all__ = ()

_LINK_TARGET_RE: Pattern[str] = re.compile(r"\]\(([^)]+\.md(?:#[^)]*)?)\)")


def _encode_stem(stem: str) -> str:
    """Encode a filename stem for a markdown link target."""
    return _fix_filename(stem).replace(" ", "%20")


def _decode_link_stem(target: str) -> tuple[str, str]:
    """Split a link target into ``(stem, fragment)``."""
    page, _, fragment = target.partition("#")
    if not page.endswith(".md"):
        msg = f"not a markdown page link: {target!r}"
        raise ValueError(msg)
    stem = unquote(page.removesuffix(".md"))
    return stem, fragment


def _rewrite_link_target(
    target: str,
    migrations: Mapping[str, str],
) -> str:
    """Rewrite a single markdown link target using stem migrations."""
    stem, fragment = _decode_link_stem(target)
    new_stem = migrations.get(stem, stem)
    encoded = _encode_stem(new_stem)
    return f"{encoded}.md{f'#{fragment}' if fragment else ''}"


def _rewrite_markdown_links(
    text: str,
    migrations: Mapping[str, str],
) -> str:
    """Rewrite markdown ``.md`` link targets according to *migrations*."""
    if not migrations:
        return text

    def replace(match: re.Match[str]) -> str:
        target = match.group(1)
        return f"]({_rewrite_link_target(target, migrations)})"

    return _LINK_TARGET_RE.sub(replace, text)


def _rewrite_article_heading(text: str, new_heading: str) -> str:
    """Replace the first ``#`` heading after optional YAML frontmatter."""
    lines = text.splitlines(keepends=True)
    in_frontmatter = False
    frontmatter_closed = False
    for index, line in enumerate(lines):
        stripped = line.strip()
        if index == 0 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
                frontmatter_closed = True
            continue
        if stripped.startswith("# "):
            lines[index] = f"# {new_heading}\n"
            break
        if frontmatter_closed or index > 0:
            if stripped.startswith("# "):
                lines[index] = f"# {new_heading}\n"
                break
    return "".join(lines)
