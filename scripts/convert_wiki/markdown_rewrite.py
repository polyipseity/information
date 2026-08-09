"""Pure markdown rewriting for reprocess mode."""

from collections.abc import Mapping
from urllib.parse import unquote

from .ast_utils import (
    _MISTUNE_PARSER,
    _collect_md_link_urls,
    _find_link_destination_ranges,
)
from .utils import _fix_filename

"""Exported names from this module."""
__all__ = ()


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

    parse_result, _state = _MISTUNE_PARSER.parse(text)
    del _state
    if isinstance(parse_result, str):
        return text

    md_urls = [url for url in _collect_md_link_urls(parse_result) if ".md" in url]
    if not md_urls:
        return text

    destination_ranges = _find_link_destination_ranges(text)
    if not destination_ranges:
        return text

    edits: list[tuple[int, int, str]] = []
    url_index = 0
    for dest_start, dest_end, destination in destination_ranges:
        if not destination.endswith(".md") and ".md#" not in destination:
            continue
        if url_index >= len(md_urls):
            break
        expected_url = md_urls[url_index]
        url_index += 1
        if destination != expected_url:
            continue
        new_url = _rewrite_link_target(expected_url, migrations)
        if new_url != expected_url:
            edits.append((dest_start, dest_end, new_url))

    if not edits:
        return text

    rewritten = text
    for dest_start, dest_end, new_url in reversed(edits):
        rewritten = rewritten[:dest_start] + new_url + rewritten[dest_end:]
    return rewritten


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
