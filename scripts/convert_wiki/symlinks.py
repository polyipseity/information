"""Redirect symlink scanning and local target resolution."""

from collections.abc import Mapping
from os import PathLike

from anyio import Path

from .api import _resolve_chain_terminal
from .stems import _stem_for_title
from .types import _RedirectInfo, _RedirectStatus

"""Exported names from this module."""
__all__ = ()


async def _scan_redirect_symlinks(
    wiki_dir: PathLike[str],
) -> tuple[tuple[str, Path, Path], ...]:
    """Return ``(title, lang_dir, symlink_path)`` for every redirect symlink."""
    wiki_dir_path = Path(wiki_dir)
    found: list[tuple[str, Path, Path]] = []
    async for lang_dir in wiki_dir_path.iterdir():
        if not await lang_dir.is_dir():
            continue
        async for entry in lang_dir.iterdir():
            if await entry.is_symlink() and entry.name.endswith(".md"):
                found.append((entry.name.removesuffix(".md"), lang_dir, entry))
    return tuple(found)


async def _resolve_local_target_filename(
    *,
    lang_dir: Path,
    to_title: str,
    final_to_title: str,
    names_map: Mapping[str, str],
) -> str:
    """Resolve the on-disk redirect target filename with chain preference."""
    target = f"{_stem_for_title(to_title, names_map)}.md"
    if to_title != final_to_title:
        final_target = f"{_stem_for_title(final_to_title, names_map)}.md"
        if (
            not await (lang_dir / target).exists()
            and await (lang_dir / final_target).exists()
        ):
            target = final_target
    return target


async def _resolve_cache_target_filename(
    *,
    lang_dir: Path,
    info: _RedirectInfo,
    redirect_cache: Mapping[str, _RedirectInfo],
    names_map: Mapping[str, str],
) -> str:
    """Resolve redirect target filename from a cache entry and chain data."""
    redirect_from_to = {key: value.to for key, value in redirect_cache.items()}
    final_to = _resolve_chain_terminal(info.to, redirect_from_to)
    return await _resolve_local_target_filename(
        lang_dir=lang_dir,
        to_title=info.to,
        final_to_title=final_to,
        names_map=names_map,
    )


async def _resolve_status_target_filename(
    *,
    lang_dir: Path,
    status: _RedirectStatus,
    names_map: Mapping[str, str],
) -> str:
    """Resolve redirect target filename from a live API status probe."""
    final_to = status.final_to or status.to
    return await _resolve_local_target_filename(
        lang_dir=lang_dir,
        to_title=status.to,
        final_to_title=final_to,
        names_map=names_map,
    )
