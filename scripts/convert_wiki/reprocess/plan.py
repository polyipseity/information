"""Pure planning for reprocess mode."""

from collections.abc import Mapping, Sequence
from os import fspath

from anyio import Path

from .. import config as _cfg
from ..api import _load_redirect_cache
from ..name_map_io import _merge_names_maps, _new_mapping_keys
from ..stems import _stem_for_title
from ..symlinks import _resolve_cache_target_filename, _scan_redirect_symlinks
from ..types import (
    _RenameAction,
    _ReprocessPlan,
    _ReprocessRequest,
    _StemMigration,
    _SymlinkAction,
    _SymlinkActionKind,
)

"""Exported names from this module."""
__all__ = ()


def _compute_stem_migrations(
    titles: Sequence[str],
    *,
    base_map: Mapping[str, str],
    effective_map: Mapping[str, str],
) -> tuple[_StemMigration, ...]:
    """Compute unique stem migrations for the given Wikipedia titles."""
    migrations: dict[str, str] = {}
    for title in titles:
        old_stem = _stem_for_title(title, base_map)
        new_stem = _stem_for_title(title, effective_map)
        if old_stem != new_stem:
            migrations[old_stem] = new_stem
    return tuple(
        _StemMigration(old_stem=old, new_stem=new)
        for old, new in sorted(migrations.items())
    )


def _stem_migration_map(
    migrations: Sequence[_StemMigration],
) -> dict[str, str]:
    """Convert stem migrations to a lookup dict."""
    return {migration.old_stem: migration.new_stem for migration in migrations}


def _resolve_article_spec(
    spec: str,
    wiki_dir: Path,
) -> tuple[str, str]:
    """Resolve an article spec to ``(lang_dir_name, stem)``."""
    normalized = spec.strip().removeprefix("general/").removesuffix(".md")
    parts = Path(normalized).parts
    if len(parts) >= 2:
        return parts[0], "/".join(parts[1:])
    return "eng", normalized


async def _collect_rewrite_targets(
    wiki_dir: Path,
    *,
    listed_paths: Sequence[Path],
    update_links: bool,
) -> tuple[Path, ...]:
    """Collect markdown files whose link targets should be rewritten."""
    targets: list[Path] = list(listed_paths)
    if not update_links:
        return tuple(dict.fromkeys(targets))
    async for entry in wiki_dir.rglob("*.md"):
        if await entry.is_symlink():
            continue
        if not await entry.is_file():
            continue
        if entry not in targets:
            targets.append(entry)
    return tuple(targets)


async def plan_reprocess(
    request: _ReprocessRequest,
    *,
    base_map: Mapping[str, str] | None = None,
) -> _ReprocessPlan:
    """Build an immutable reprocess plan without mutating the filesystem."""
    wiki_dir = Path(
        request.wiki_dir
        if request.wiki_dir is not None
        else _cfg._CONVERTED_WIKI_DIRECTORY
    )
    cache_path = (
        request.cache_path
        if request.cache_path is not None
        else _cfg._REDIRECT_CACHE_PATH
    )
    name_map_path = (
        request.name_map_path
        if request.name_map_path is not None
        else _cfg._DATA_DIRECTORY / f"{_cfg._NAMES_MAP_NAME}.name_map.jsonc"
    )
    base = base_map if base_map is not None else _cfg._NAMES_MAP
    effective_map = _merge_names_maps(base, request.mappings)
    new_keys = _new_mapping_keys(base, effective_map)

    resolved_articles = [
        _resolve_article_spec(spec, wiki_dir) for spec in request.articles
    ]
    article_titles = [stem for _, stem in resolved_articles]
    redirect_cache = _load_redirect_cache(cache_path)
    titles = sorted(set(redirect_cache) | set(effective_map) | set(article_titles))
    stem_migrations = _compute_stem_migrations(
        titles,
        base_map=base,
        effective_map=effective_map,
    )

    scanned = await _scan_redirect_symlinks(wiki_dir)
    expected_targets: dict[tuple[str, str], str] = {}
    default_lang = Path(_cfg._CONVERTED_WIKI_LANGUAGE_DIRECTORY).name
    lang_dirs = {lang_dir.name for _, lang_dir, _ in scanned} or {default_lang}
    for title, info in redirect_cache.items():
        for lang_dir_name in lang_dirs:
            lang_dir = wiki_dir / lang_dir_name
            expected_targets[
                (title, lang_dir_name)
            ] = await _resolve_cache_target_filename(
                lang_dir=lang_dir,
                info=info,
                redirect_cache=redirect_cache,
                names_map=effective_map,
            )

    symlink_actions: list[_SymlinkAction] = []
    scanned_lookup = {
        (from_stem, lang_dir.name): (from_stem, lang_dir, symlink)
        for from_stem, lang_dir, symlink in scanned
    }
    for title, info in redirect_cache.items():
        from_stem = _stem_for_title(title, effective_map)
        for lang_dir_name in lang_dirs:
            expected = expected_targets[(title, lang_dir_name)]
            expected_stem = expected.removesuffix(".md")
            key = (from_stem, lang_dir_name)
            if info.to == title or from_stem == expected_stem:
                if key in scanned_lookup:
                    symlink_actions.append(
                        _SymlinkAction(
                            kind=_SymlinkActionKind.REMOVE,
                            from_stem=from_stem,
                            to_stem=expected_stem,
                            lang_dir_name=lang_dir_name,
                        )
                    )
                continue
            if key not in scanned_lookup:
                symlink_actions.append(
                    _SymlinkAction(
                        kind=_SymlinkActionKind.CREATE,
                        from_stem=from_stem,
                        to_stem=expected_stem,
                        lang_dir_name=lang_dir_name,
                    )
                )
            else:
                _, _, symlink = scanned_lookup[key]
                if fspath(await symlink.readlink()) != expected:
                    symlink_actions.append(
                        _SymlinkAction(
                            kind=_SymlinkActionKind.RETARGET,
                            from_stem=from_stem,
                            to_stem=expected_stem,
                            lang_dir_name=lang_dir_name,
                        )
                    )

    rename_actions: list[_RenameAction] = []
    listed_paths: list[Path] = []
    heading_updates: dict[str, str] = {}
    for lang_dir_name, stem in resolved_articles:
        lang_dir = wiki_dir / lang_dir_name
        current_path = lang_dir / f"{stem}.md"
        listed_paths.append(current_path)
        new_stem = _stem_for_title(stem, effective_map)
        if new_stem != stem:
            target_path = lang_dir / f"{new_stem}.md"
            if await target_path.exists() and not await target_path.is_symlink():
                msg = f"rename target already exists: {target_path}"
                raise FileExistsError(msg)
            rename_actions.append(
                _RenameAction(
                    lang_dir_name=lang_dir_name,
                    old_stem=stem,
                    new_stem=new_stem,
                )
            )
            heading_updates[fspath(target_path)] = new_stem
        elif stem in {migration.old_stem for migration in stem_migrations}:
            heading_updates[fspath(current_path)] = _stem_migration_map(
                stem_migrations
            ).get(stem, stem)

    rewrite_targets = await _collect_rewrite_targets(
        wiki_dir,
        listed_paths=listed_paths,
        update_links=request.update_links,
    )

    return _ReprocessPlan(
        effective_map=effective_map,
        new_mapping_keys=new_keys,
        stem_migrations=stem_migrations,
        symlink_actions=tuple(symlink_actions),
        rename_actions=tuple(rename_actions),
        rewrite_targets=rewrite_targets,
        heading_updates=heading_updates,
        wiki_dir=wiki_dir,
        cache_path=cache_path,
        name_map_path=name_map_path,
    )
