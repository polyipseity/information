"""Utility functions for the Wikipedia HTML-to-Markdown converter.

Pure helper functions with no class dependencies.
"""

import re
from collections.abc import Collection, Mapping
from os import PathLike, fspath, replace
from os.path import dirname, isabs, join, realpath, split
from unicodedata import normalize as _normalize_unicode
from urllib.parse import unquote

import pathvalidate
from anyio import Path, to_thread
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


async def _find_child_case_insensitive(parent: Path, name: str) -> Path | None:
    """Return the child entry whose basename equals _name_ ignoring letter case."""
    name_lower = name.lower()
    async for entry in parent.iterdir():
        if entry.name != name and entry.name.lower() == name_lower:
            return entry
    return None


def _fold_text(text: str) -> str:
    """Return a comparison key for _text_ that ignores letter case."""
    return _normalize_unicode("NFC", text).casefold()


def _fold_path_key(path: str) -> str:
    """Return a comparison key for a path that ignores letter case.

    ``os.path.normcase`` cannot be used: it is the identity function on
    POSIX, while the filesystems this must guard are case-insensitive there
    too.  Only the directory components are resolved, so two spellings that
    reach the same directory through a symlink fold together while the final
    link stays the final link the walk is about.
    """
    parent, name = split(path)
    return _fold_text(join(realpath(parent), name))


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
    lowercase_fallback: bool = True,
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

    Set *lowercase_fallback* to False where the text is prose rather than a
    page title, as for a heading: a name in the map is worth adopting, but
    guessing a heading's case from the map lowercases every proper noun it
    does not happen to contain.
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
    if lowercase_fallback and len(name) > 1 and name[1:].islower():
        lowered = name[0].lower() + name[1:]
        if lowered in names_map:
            return names_map[lowered]
        return lowered
    return name


async def _replace_symlink(path: Path, target: str) -> None:
    """Point _path_ at _target_, replacing the link that was there.

    The new link is built beside the old one and moved into place, so an
    interruption leaves the old redirect intact instead of deleting it and
    dying before the replacement exists.
    """
    temporary = path.with_name(f".{path.name}.link")
    if await temporary.is_symlink():
        await temporary.unlink()
    await temporary.symlink_to(target, target_is_directory=False)
    await to_thread.run_sync(replace, fspath(temporary), fspath(path))


"""Upper bound on link hops followed while checking for a cycle."""
_MAX_SYMLINK_HOPS = 40


async def _symlink_would_loop(parent: Path, name: str, target: str) -> bool:
    """Return whether ``parent/name`` -> ``target`` would close a cycle.

    The walk follows the chain that already exists from the proposed target,
    so an indirect cycle through other links is caught as well as a direct
    self-loop.  Paths are compared case-insensitively after resolution,
    because the link and its target name one file on a case-insensitive
    filesystem.  A chain that revisits a path, or that outlives the hop
    budget, is already broken, so the new link is refused rather than made
    unreachable.
    """
    parent_path = fspath(parent)
    link_key = _fold_path_key(join(parent_path, name))
    current = join(parent_path, target)
    visited = {link_key}
    for _hop in range(_MAX_SYMLINK_HOPS):
        key = _fold_path_key(current)
        if key in visited:
            return True
        visited.add(key)
        current_path = Path(current)
        if not await current_path.is_symlink():
            return False
        next_target = fspath(await current_path.readlink())
        current = (
            next_target if isabs(next_target) else join(dirname(current), next_target)
        )
    return True


async def _point_symlink(parent: Path, name: str, target: str) -> bool:
    """Create or retarget ``parent/name`` -> ``target``, never onto a cycle.

    Returns whether the path now names the intended link.  A real file that
    occupies the name, exactly or differing only by letter case, is never
    replaced; an existing symlink that names another target is retargeted.
    A link that would resolve to itself, directly or through other links, is
    refused and logged instead of written.
    """
    path = parent / name
    if await _symlink_would_loop(parent, name, target):
        _cfg._logger.warning("refusing circular symlink: %s -> %s", path, target)
        return False
    occupant = await _find_child_exact(parent, name)
    if occupant is None:
        occupant = await _find_child_case_insensitive(parent, name)
    if occupant is not None:
        if not await occupant.is_symlink():
            _cfg._logger.warning("leaving real file in place: %s", occupant)
            return False
        if str(await occupant.readlink()) == target:
            return True
    await _unlink_case_colliding_symlinks(parent, name)
    await _replace_symlink(path, target)
    return True


async def _create_redirect_symlinks(
    wiki_dir: PathLike[str],
    wiki_lang_dir: PathLike[str],
    from_filename: str,
    to_filename: str,
) -> bool:
    """Create or retarget redirect symlinks for a renamed page.

    The language-directory symlink ``{from_filename}.md`` is retargeted when
    it already exists as a symlink pointing at a different file, left
    untouched when it already points at ``{to_filename}.md``, and never
    replaced when it is a real file.  The top-level mirror is created only
    if missing; an existing mirror (symlink or real file) is never touched.
    When a real file differing only in letter case occupies the
    language-directory path, no symlink is created there and the mirror is
    left alone, since there is nothing left to mirror.  Neither link is
    written when it would resolve to itself; the return value says whether
    both were pointed at their target.
    """
    wiki_dir_path = Path(wiki_dir)
    wiki_lang_dir_path = Path(wiki_lang_dir)
    redirect_name = f"{from_filename}.md"
    exact = await _find_child_exact(wiki_lang_dir_path, redirect_name)
    real_file_occupies_name = exact is not None and not await exact.is_symlink()
    lang_ok = await _point_symlink(
        wiki_lang_dir_path, redirect_name, f"{to_filename}.md"
    )
    if not lang_ok and not real_file_occupies_name:
        # Nothing is left at the name to mirror: a real file differing only
        # by case still owns the path, or the link was refused as circular.
        return False
    mirror_name = redirect_name
    expected_mirror_target = str(
        wiki_lang_dir_path.relative_to(wiki_dir_path) / mirror_name
    )
    return (
        await _point_symlink(wiki_dir_path, mirror_name, expected_mirror_target)
        and lang_ok
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


"""Longest filename a Windows path component may carry."""
_MAX_FILENAME_LENGTH = 255
"""Extension every note carries; the stem is sanitised with it appended."""
_STEM_SUFFIX = ".md"


def _fix_stem(stem: str) -> str:
    """Replace filesystem-unsafe characters in a filename stem.

    The sanitiser polices a whole filename, so the suffix is appended before
    the call and removed afterwards: a trailing dot or space is legal once
    ``.md`` follows it (``i.i.d..md`` ends in ``d``), while a character
    Windows forbids anywhere (``: * ? " < > |``) is still replaced.

    ``pathvalidate`` truncates at 255 characters, so the stem is capped
    first and the extension is guaranteed to survive.  A device name such as
    ``con`` grows by one character, so the retry shortens once more.
    """
    limit = _MAX_FILENAME_LENGTH - len(_STEM_SUFFIX)
    for cap in (limit, limit - 1):
        full = pathvalidate.sanitize_filename(
            f"{stem[:cap]}{_STEM_SUFFIX}",
            platform="windows",
            replacement_text="_",
        )
        if full.endswith(_STEM_SUFFIX):
            return full.removesuffix(_STEM_SUFFIX)
    msg = f"stem {stem!r} cannot keep its extension under the name limit"
    raise ValueError(msg)


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


"""Bytes that ``Sanitizer::escapeIdInternal``'s ``legacy`` mode never escapes.

MediaWiki encodes legacy fragments with
``strtr(urlencode(str_replace(' ', '_', $id)), ['%3A' => ':', '%' => '.'])``,
so ``urlencode`` leaves ``A-Za-z0-9-_.`` alone and ``strtr`` restores ``:``.
A ``.HH`` run whose bytes fall in that set therefore cannot be an escape.
"""
_LEGACY_LITERAL_BYTES = frozenset(
    b"-._:0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
)
"""Characters a decoded legacy escape may produce.

``urlencode`` leaves spaces alone too, but the encoder replaces every space
with ``_`` before encoding, so a space byte inside a legacy run can only come
from a literal dot followed by two hex digits (``al.1994``, ``Section.2004``).
The same holds for control characters, which no anchor contains.
"""
_LEGACY_DECODABLE_CHARACTERS = frozenset(
    chr(value) for value in range(0x21, 0x7F)
) | frozenset(chr(value) for value in range(0xA0, 0x10000))

"""Matches one run of MediaWiki legacy (``.HH``) or percent (``%HH``) escapes."""
_FRAGMENT_ESCAPE_RUN_REGEX = re.compile(r"(?:\.[0-9A-Fa-f]{2})+|(?:%[0-9A-Fa-f]{2})+")


def _decode_legacy_escape_run(run: str) -> str:
    """Decode one ``.HH`` run, or return it verbatim when it is literal text.

    A run is ambiguous with a literal dot followed by two hex digits, since
    MediaWiki's legacy encoder leaves a literal ``.`` alone.  Three readings
    cannot have been produced by that encoder, so all three stay verbatim
    rather than turning into replacement characters or stray spaces: a run
    whose bytes include a literal byte of the legacy encoding, a run that is
    not valid UTF-8, and a run that decodes to a space or a control character.
    """
    values = bytes(
        int(run[index + 1 : index + 3], 16) for index in range(0, len(run), 3)
    )
    if any(value in _LEGACY_LITERAL_BYTES for value in values):
        return run
    try:
        decoded = values.decode("UTF-8")
    except UnicodeDecodeError:
        return run
    if all(character in _LEGACY_DECODABLE_CHARACTERS for character in decoded):
        return decoded
    return run


def _decode_legacy_fragment(fragment: str) -> str:
    """Decode MediaWiki legacy (``.HH``) and percent (``%HH``) escapes once.

    Every escape run in the *source* fragment is decoded exactly once and
    emitted output is never re-scanned, so a decoded percent sign (``.25``)
    cannot become a percent escape and an escaped percent sign (``%25``) cannot
    become a legacy escape.
    """
    parts: list[str] = []
    position = 0
    for match in _FRAGMENT_ESCAPE_RUN_REGEX.finditer(fragment):
        parts.append(fragment[position : match.start()])
        run = match.group()
        parts.append(
            _decode_legacy_escape_run(run) if run.startswith(".") else unquote(run)
        )
        position = match.end()
    parts.append(fragment[position:])
    return "".join(parts)


def _plain_fragment(
    fragment: str, *, known_fragments: Collection[str] = frozenset()
) -> str:
    """Decode a URL fragment from an HTML ``href`` into plain text.

    Fragments reach the converter percent-encoded and, because Wikipedia's
    stored HTML uses the legacy fragment mode, with section anchors dot-escaped
    (``.E2.80.93`` for ``–``), but the name map, the ``_fix_name_maybe`` casing
    heuristic, and ``_encode_fragment`` all operate on plain text.  Decoding once
    at the ``href`` boundary keeps ingestion in step with
    ``_rewrite_link_target``, which decodes the fragment it reads back from the
    written Markdown; without it a fragment such as
    ``Schr%C3%B6dinger_equation`` keeps its encoding (and its uppercase hex
    digits suppress the lowercase-first-char fallback).

    A legacy run is ambiguous with a literal dot followed by two hex digits,
    because MediaWiki's encoder leaves a literal ``.`` alone.  Two readings
    settle it.  ``_decode_legacy_escape_run`` rejects a run that decodes to a
    space or a control character, which that encoder cannot produce, so
    ``al.1994`` keeps its dot and ``einstein.27s_theory`` decodes without the
    target note having to exist.  When *known_fragments* is supplied, an
    in-document self-link adds the stronger evidence: the literal reading wins
    when only it names an anchor of this document (``id="Section.28"``).
    """
    literal = unquote(fragment)
    decoded = _decode_legacy_fragment(fragment)
    if decoded == literal:
        return literal
    if (
        known_fragments
        and any(variant in known_fragments for variant in _fragment_variants(literal))
        and not any(
            variant in known_fragments for variant in _fragment_variants(decoded)
        )
    ):
        return literal
    return decoded


def _fragment_variants(fragment: str) -> tuple[str, ...]:
    """Spellings a fragment may take: underscores collide with spaces."""
    return (fragment, fragment.replace("_", " ")) if "_" in fragment else (fragment,)


def _encode_fragment(fragment: str) -> str:
    """Encode a plain-text fragment for a link target (no ``#`` prefix)."""
    return fragment.replace(":", "").replace(" ", "%20").replace("/", "%2F")


def _markdown_fragment(fragment: str) -> str:
    """Return a URL fragment string suitable for a Markdown link anchor."""
    return fragment and f"#{_encode_fragment(fragment)}"


def _markdown_link_target(page: str, fragment: str = "") -> str:
    """Build a relative Markdown link target for a given page name and fragment."""
    return f"{_fix_stem(page).replace(' ', '%20').replace('_', '%5F')}.md{_markdown_fragment(fragment)}"


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
