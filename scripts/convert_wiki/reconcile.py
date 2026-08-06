"""Redirect symlink reconciliation for the Wikipedia HTML-to-Markdown converter.

The ingestion path creates redirect symlinks from cached redirect data.
When Wikipedia redirects change (or pages become redirects/full articles),
those symlinks go stale.  This module reconciles the on-disk symlinks
against the live API state, without ever touching real files.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from os import PathLike

from aiohttp import ClientSession
from anyio import Path

from . import config as _cfg
from .api import _fetch_redirect_status, _load_redirect_cache, _save_redirect_cache
from .symlinks import _resolve_status_target_filename, _scan_redirect_symlinks
from .types import _RedirectInfo
from .utils import _create_redirect_symlinks, _remove_redirect_symlinks

"""Exported names from this module."""
__all__ = ()


@dataclass(frozen=True)
class _ReconcileReport:
    """Summary of a redirect reconciliation run."""

    scanned: int
    retargeted: int
    removed: int
    kept: int
    changed: tuple[str, ...]


async def reconcile_redirect_symlinks(
    session: ClientSession,
    *,
    wiki_dir: PathLike[str] | None = None,
    cache_path: PathLike[str] | None = None,
    dry_run: bool = False,
) -> _ReconcileReport:
    """Reconcile redirect symlinks in a converted wiki against the live API.

    Scans every language subdirectory of *wiki_dir* for ``*.md`` symlinks,
    probes the current status of each title (bypassing the cache), then:

    - missing pages are kept (conservative),
    - titles that became full articles have their symlinks removed,
    - stale redirects are retargeted to their current target, preferring
      the final target of a redirect chain when the first hop is not
      ingested locally.

    The redirect cache is refreshed for every scanned title so that
    subsequent ingestion stays consistent with the reconciled symlinks.
    With *dry_run*, nothing is written (no symlink changes, no cache
    write) and the report describes what would happen.

    Parameters
    ----------
    session:
        aiohttp session for API requests.
    wiki_dir:
        Converted wiki root (defaults to ``_CONVERTED_WIKI_DIRECTORY``).
    cache_path:
        Redirect cache file (defaults to ``_REDIRECT_CACHE_PATH``).
    dry_run:
        If true, report only; do not modify symlinks or the cache.
    """
    wiki_dir_path = Path(
        wiki_dir if wiki_dir is not None else _cfg._CONVERTED_WIKI_DIRECTORY
    )
    resolved_cache_path = (
        cache_path if cache_path is not None else _cfg._REDIRECT_CACHE_PATH
    )
    found = await _scan_redirect_symlinks(wiki_dir_path)
    statuses = await _fetch_redirect_status(session, [t for t, _, _ in found])
    cache = _load_redirect_cache(resolved_cache_path)
    now_iso = datetime.now(timezone.utc).isoformat()
    scanned = 0
    retargeted = 0
    removed = 0
    kept = 0
    changed: list[str] = []
    for title, lang_dir, symlink in found:
        scanned += 1
        status = statuses.get(title)
        if status is None or status.missing:
            # Missing or unclassifiable — keep (page may return).
            kept += 1
            cache[title] = _RedirectInfo(to=title, cached_at=now_iso)
            continue
        if status.to == title:
            # Now a full article — remove the redirect symlinks.
            removed += 1
            changed.append(title)
            if not dry_run:
                await _remove_redirect_symlinks(wiki_dir_path, lang_dir, title)
            cache[title] = _RedirectInfo(to=title, cached_at=now_iso)
            continue
        target = await _resolve_status_target_filename(
            lang_dir=lang_dir,
            status=status,
            names_map=_cfg._NAMES_MAP,
        )
        if str(await symlink.readlink()) == target:
            kept += 1
            cache[title] = _RedirectInfo(
                to=status.to, tofragment=status.tofragment, cached_at=now_iso
            )
            continue
        retargeted += 1
        changed.append(title)
        if not dry_run:
            await _create_redirect_symlinks(
                wiki_dir_path,
                lang_dir,
                title,
                target.removesuffix(".md"),
            )
        cache[title] = _RedirectInfo(
            to=status.to, tofragment=status.tofragment, cached_at=now_iso
        )
    if not dry_run:
        await _save_redirect_cache(cache, cache_path=resolved_cache_path)
    return _ReconcileReport(
        scanned=scanned,
        retargeted=retargeted,
        removed=removed,
        kept=kept,
        changed=tuple(changed),
    )
