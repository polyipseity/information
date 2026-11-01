"""Pure planning for reprocess mode."""

from collections.abc import Mapping, Sequence
from os import fspath

from anyio import Path

from .. import config as _cfg
from ..api import _load_redirect_cache
from ..markdown_rewrite import _build_link_index
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
from ..utils import (
    _find_child_case_insensitive,
    _find_child_exact,
    _fold_text,
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
    # A key two titles claim differently cannot be applied, so the lookup
    # index is built here first: planning fails before anything is decided,
    # and a dry run reports the defect instead of a plan.
    _build_link_index(base, effective_map)

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
    migration_map = _stem_migration_map(stem_migrations)
    title_for_stem: dict[str, str] = {}
    for title in sorted(effective_map):
        title_for_stem.setdefault(_stem_for_title(title, base), effective_map[title])

    scanned = await _scan_redirect_symlinks(wiki_dir)
    expected_targets: dict[tuple[str, str], str] = {}
    default_lang = Path(_cfg._CONVERTED_WIKI_LANGUAGE_DIRECTORY).name
    lang_dirs = {lang_dir.name for _, lang_dir, _ in scanned} or {default_lang}
    for title, info in redirect_cache.items():
        if title in _cfg._CITATION_UI_TITLES:
            continue
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

    def _planned_stem(stem: str) -> str:
        """Return the stem a redirect stored as *stem* will carry.

        The on-disk name can differ from the base map's spelling in letter
        case, so both the rename and the lookup go through the canonical
        form first; only then does a stem migration apply.
        """
        canonical = _stem_for_title(stem, base)
        return migration_map.get(canonical, canonical)

    symlink_actions: list[_SymlinkAction] = []
    for from_stem, lang_dir, _symlink in scanned:
        new_from_stem = _planned_stem(from_stem)
        if new_from_stem != from_stem:
            symlink_actions.append(
                _SymlinkAction(
                    kind=_SymlinkActionKind.RENAME,
                    from_stem=from_stem,
                    to_stem=new_from_stem,
                    lang_dir_name=lang_dir.name,
                )
            )

    scanned_lookup = {
        (_planned_stem(from_stem), lang_dir.name): (from_stem, lang_dir, symlink)
        for from_stem, lang_dir, symlink in scanned
    }
    for title, info in redirect_cache.items():
        if title in _cfg._CITATION_UI_TITLES:
            continue
        from_stem = _stem_for_title(title, effective_map)
        for lang_dir_name in lang_dirs:
            expected = expected_targets[(title, lang_dir_name)]
            expected_stem = migration_map.get(
                expected.removesuffix(".md"),
                expected.removesuffix(".md"),
            )
            expected = f"{expected_stem}.md"
            key = (from_stem, lang_dir_name)
            # A redirect that would name its own target carries nothing; it is
            # removed rather than written as a link to itself, which the link
            # and its target are on a case-insensitive filesystem.
            if info.to == title or _fold_text(from_stem) == _fold_text(expected_stem):
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
        new_stem = migration_map.get(stem, _stem_for_title(stem, effective_map))
        title_text = title_for_stem.get(_stem_for_title(stem, base), new_stem)
        rewrite_path = current_path
        if new_stem != stem:
            target_path = lang_dir / f"{new_stem}.md"
            exact_target = await _find_child_exact(lang_dir, target_path.name)
            exact_current = await _find_child_exact(lang_dir, current_path.name)
            if exact_current is None:
                # No file carries the old stem, so there is nothing to rename:
                # the note already sits at its final name under some spelling
                # of it, and only its text moves.
                existing = exact_target or await _find_child_case_insensitive(
                    lang_dir, target_path.name
                )
                if existing is not None:
                    rewrite_path = existing
                    heading_updates[fspath(existing)] = title_text
            else:
                if (
                    exact_target is not None
                    and exact_target != exact_current
                    and not await exact_target.is_symlink()
                ):
                    msg = f"rename target already exists: {target_path}"
                    raise FileExistsError(msg)
                rename_actions.append(
                    _RenameAction(
                        lang_dir_name=lang_dir_name,
                        old_stem=stem,
                        new_stem=new_stem,
                    )
                )
                # The heading carries the mapped title, not the sanitised
                # stem: a title with ``:`` sanitises to ``_`` in the filename.
                heading_updates[fspath(target_path)] = title_text
                rewrite_path = target_path
        elif stem in {migration.old_stem for migration in stem_migrations}:
            heading_updates[fspath(current_path)] = migration_map.get(stem, stem)
        listed_paths.append(rewrite_path)

    rewrite_targets = await _collect_rewrite_targets(
        wiki_dir,
        listed_paths=listed_paths,
        update_links=request.update_links,
    )

    return _ReprocessPlan(
        base_map=base,
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
