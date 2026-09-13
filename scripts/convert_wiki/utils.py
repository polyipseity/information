"""Utility functions for the Wikipedia HTML-to-Markdown converter.

Pure helper functions with no class dependencies.
"""

import re
from collections.abc import Mapping
from os import PathLike
from urllib.parse import unquote

from anyio import Path
from bs4 import Tag
from yarl import URL

from . import config as _cfg

"""Exported names from this module."""
__all__ = ()


async def _find_child_exact(parent: Path, name: str) -> Path | None:
    """Return the child entry only when its basename equals _name_ exactly."""
    async for entry in parent.iterdir():
        if entry.name == name:
            return entry
    return None


async def _unlink_case_colliding_symlinks(parent: Path, name: str) -> None:
    """Remove symlink children that differ from _name_ only by letter case."""
    name_lower = name.lower()
    async for entry in parent.iterdir():
        if entry.name != name and entry.name.lower() == name_lower:
            if await entry.is_symlink():
                await entry.unlink()


def _fix_name_maybe(
    name: str,
    *,
    normalize: bool = True,
    replace_underscores: bool = False,
    names_map: Mapping[str, str] | None = None,
) -> str:
    """Normalise a Wikipedia page title via the name map with fallback.

    Applies a single sequential heuristic:
    1. Normalise nbsp-to-space if *normalize* is True (default).
    2. Look up in *names_map* (defaults to ``_cfg._NAMES_MAP``).
       Return immediately if found.
    3. If *replace_underscores* is True, replace ``_`` with `` ``.
    4. Retry lookup with the (potentially underscore-replaced) name.
       If still not found, apply the lowercase-first-char fallback:
       ``name[1:].islower() or len(name) <= 1`` → lowercase first character.
    """
    names_map = names_map if names_map is not None else _cfg._NAMES_MAP
    if normalize:
        name = name.replace("\u00a0", " ")
    if name in names_map:
        return names_map[name]
    if replace_underscores:
        name = name.replace("_", " ")
        if name in names_map:
            return names_map[name]
    if len(name) > 1 and name[1:].islower():
        lowered = name[0].lower() + name[1:]
        if lowered in names_map:
            return names_map[lowered]
        return lowered
    return name


async def _symlink_to_idempotent(
    path: Path,
    target: str,
    *,
    target_is_directory: bool = False,
) -> None:
    """Create _path_ → _target_ unless an equivalent symlink already exists.

      Concurrent converters may race to create the same redirect symlink; treat
    a matching existing symlink as success and re-raise only on conflict.
    """
    try:
        await path.symlink_to(target, target_is_directory=target_is_directory)
    except FileExistsError:
        if not (await path.is_symlink() and str(await path.readlink()) == target):
            raise


async def _create_redirect_symlinks(
    wiki_dir: PathLike[str],
    wiki_lang_dir: PathLike[str],
    from_filename: str,
    to_filename: str,
) -> None:
    """Create or retarget redirect symlinks for a renamed page.

    The language-directory symlink ``{from_filename}.md`` is retargeted when
    it already exists as a symlink pointing at a different file, left
    untouched when it already points at ``{to_filename}.md``, and never
    replaced when it is a real file.  The top-level mirror is created only
    if missing; an existing mirror (symlink or real file) is never touched.
    """
    wiki_dir_path = Path(wiki_dir)
    wiki_lang_dir_path = Path(wiki_lang_dir)
    redirect_name = f"{from_filename}.md"
    target = f"{to_filename}.md"
    redirect_file = await _find_child_exact(wiki_lang_dir_path, redirect_name)
    if redirect_file is not None:
        if await redirect_file.is_symlink():
            if str(await redirect_file.readlink()) != target:
                await redirect_file.unlink()
                await _unlink_case_colliding_symlinks(wiki_lang_dir_path, redirect_name)
                await _symlink_to_idempotent(
                    wiki_lang_dir_path / redirect_name,
                    target,
                )
    else:
        await _unlink_case_colliding_symlinks(wiki_lang_dir_path, redirect_name)
        await _symlink_to_idempotent(
            wiki_lang_dir_path / redirect_name,
            target,
        )
    mirror_name = redirect_name
    expected_mirror_target = str(
        wiki_lang_dir_path.relative_to(wiki_dir_path) / mirror_name
    )
    mirror_file = await _find_child_exact(wiki_dir_path, mirror_name)
    if mirror_file is not None:
        if await mirror_file.is_symlink():
            if str(await mirror_file.readlink()) != expected_mirror_target:
                await mirror_file.unlink()
                await _unlink_case_colliding_symlinks(wiki_dir_path, mirror_name)
                await _symlink_to_idempotent(
                    wiki_dir_path / mirror_name,
                    expected_mirror_target,
                )
    else:
        await _unlink_case_colliding_symlinks(wiki_dir_path, mirror_name)
        await _symlink_to_idempotent(
            wiki_dir_path / mirror_name,
            expected_mirror_target,
        )


async def _remove_redirect_symlinks(
    wiki_dir: PathLike[str],
    wiki_lang_dir: PathLike[str],
    from_filename: str,
) -> None:
    """Remove the redirect symlinks for a page that is no longer a redirect.

    Unlinks the language-directory symlink ``{from_filename}.md`` and its
    top-level mirror, but only when they are symlinks — a real file at
    either path is never touched (invariant).
    """
    wiki_dir_path = Path(wiki_dir)
    wiki_lang_dir_path = Path(wiki_lang_dir)
    redirect_name = f"{from_filename}.md"
    for parent in (wiki_lang_dir_path, wiki_dir_path):
        redirect_file = await _find_child_exact(parent, redirect_name)
        if redirect_file is not None and await redirect_file.is_symlink():
            await redirect_file.unlink()


def _fix_filename(name: str) -> str:
    """Replace filesystem-unsafe characters with underscores."""
    return _cfg._BAD_CHARACTERS.sub("_", name)


def _strip_url_query(url: URL) -> URL:
    """Return _url_ with its query string and fragment removed."""
    return url.with_query(None).with_fragment(None)


def _filename_from_url(url: str) -> str | None:
    """Extract the original uploaded filename from a media URL.

    Applies ``_ARCHIVE_REGEXES`` + ``unquote`` + underscores→spaces. Works for
    image upload URLs, video ``resource`` (/wiki/File:…), and audio ``href``
    (//en.wikipedia.org/wiki/File:…) identically. Returns the filename without
    the ``File:`` prefix, or ``None`` if it cannot be determined.
    """
    src_url = _strip_url_query(_cfg._WIKI_HOST_URL.join(URL(str(url))))
    src_url_str = src_url.human_repr()
    for regex in _cfg._ARCHIVE_REGEXES:
        if match := regex.search(src_url_str):
            return unquote(match[1]).replace("_", " ")
    return None


def _get_image_filename(ele: Tag) -> str | None:
    """Extract the original uploaded filename from a media element.

    Returns the filename without ``File:`` prefix (e.g. ``Modernphysicsfields.svg``)
    or ``None`` if it cannot be determined from either ``resource`` or ``src``.
    """
    if resource := ele.get("resource"):
        if filename := _filename_from_url(str(resource)):
            return filename
    if src := ele.get("src"):
        return _filename_from_url(str(src))
    if href := ele.get("href"):
        return _filename_from_url(str(href))
    if mwtitle := ele.get("data-mwtitle"):
        return str(mwtitle).replace("_", " ")
    return None


def _encode_fragment(fragment: str) -> str:
    """Encode a plain-text fragment for a link target (no ``#`` prefix)."""
    return fragment.replace(":", "").replace(" ", "%20").replace("/", "%2F")


def _markdown_fragment(fragment: str) -> str:
    """Return a URL fragment string suitable for a Markdown link anchor."""
    return fragment and f"#{_encode_fragment(fragment)}"


def _markdown_link_target(page: str, fragment: str = "") -> str:
    """Build a relative Markdown link target for a given page name and fragment."""
    return f"{_fix_filename(page).replace(' ', '%20')}.md{_markdown_fragment(fragment)}"


def _tag_affixes(name: str) -> tuple[str, str]:
    """Return the opening and closing HTML tag strings for the given tag name."""
    return f"<{name}>", f"</{name}>"


def _balance_brackets(text: str) -> str:
    """Escape unbalanced ``[`` and ``]`` in _text_.

    Uses a two-pass stack algorithm:
    - Pass 1: scan left-to-right, track unmatched ``[`` positions on a stack.
              A ``]`` pops the stack if non-empty (matched pair) or is marked
              unbalanced if empty. Remaining stack positions at EOF are
              unclosed ``[``.
    - Pass 2: backslash-escape all unbalanced brackets.

    Balanced ``[...]`` pairs pass through unchanged per CommonMark \u00a76.3.
    Escaped ``\\[``/``\\]`` are inert per CommonMark \u00a72.4.
    """
    _stack: list[int] = []
    _unbalanced: set[int] = set()
    for _i, _c in enumerate(text):
        if _c == "[":
            _stack.append(_i)
        elif _c == "]":
            if _stack:
                _stack.pop()
            else:
                _unbalanced.add(_i)
    _unbalanced.update(_stack)
    if _unbalanced:
        _chars = list(text)
        for _i in sorted(_unbalanced):
            _chars[_i] = "\\" + _chars[_i]
        return "".join(_chars)
    return text


"""Characters that are zero-width in terminal display but count as width 1 in
Python ``len()``.  MD060 (table-column-style) fires when these skew column
widths.  Strip them from table cell content before computing widths."""
_ZERO_WIDTH_CHARS_RE = re.compile("[\u200b\u200c\u200d\u2060\ufeff]")
