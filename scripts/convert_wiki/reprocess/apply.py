"""Apply a reprocess plan to the filesystem."""

from collections.abc import Mapping
from os import fspath, rename

from anyio import Path

from ..markdown_rewrite import (
    _rewrite_article_heading,
    _rewrite_markdown_headings,
    _rewrite_markdown_links,
)
from ..name_map_io import _reload_names_map, _save_names_map
from ..types import (
    _ReprocessPlan,
    _ReprocessReport,
    _ReprocessRequest,
    _SymlinkActionKind,
)
from ..utils import (
    _create_redirect_symlinks,
    _find_child_exact,
    _remove_redirect_symlinks,
    _unlink_case_colliding_symlinks,
)
from .plan import _stem_migration_map, plan_reprocess

"""Exported names from this module."""
__all__ = ()


async def _apply_rename(
    wiki_dir: Path,
    *,
    lang_dir_name: str,
    old_stem: str,
    new_stem: str,
) -> None:
    """Atomically rename an article and its top-level mirror symlink."""
    lang_dir = wiki_dir / lang_dir_name
    old_name = f"{old_stem}.md"
    new_name = f"{new_stem}.md"
    old_note = await _find_child_exact(lang_dir, old_name)
    if old_note is None:
        msg = f"article not found for rename: {lang_dir / old_name}"
        raise FileNotFoundError(msg)
    new_note = lang_dir / new_name
    tmp_note = lang_dir / f"{old_stem}.md.tmp"
    await old_note.rename(tmp_note)
    rename(fspath(tmp_note), fspath(new_note))
    old_mirror = await _find_child_exact(wiki_dir, old_name)
    if old_mirror is not None and await old_mirror.is_symlink():
        await old_mirror.unlink()
    if await _find_child_exact(wiki_dir, new_name) is None:
        await (wiki_dir / new_name).symlink_to(
            f"{lang_dir_name}/{new_stem}.md",
            target_is_directory=False,
        )


async def _apply_symlink_rename(
    wiki_dir: Path,
    *,
    lang_dir_name: str,
    old_stem: str,
    new_stem: str,
    migrations: dict[str, str],
) -> None:
    """Rename a redirect symlink and migrate its target stem when needed."""
    lang_dir = wiki_dir / lang_dir_name
    old_name = f"{old_stem}.md"
    new_name = f"{new_stem}.md"
    old_path = await _find_child_exact(lang_dir, old_name)
    if old_path is None or not await old_path.is_symlink():
        return
    target = str(await old_path.readlink())
    if target.endswith(".md"):
        target_stem = target.removesuffix(".md")
        new_target = f"{migrations.get(target_stem, target_stem)}.md"
    else:
        new_target = target
    await old_path.unlink()
    await _unlink_case_colliding_symlinks(lang_dir, new_name)
    new_path = lang_dir / new_name
    await new_path.symlink_to(new_target, target_is_directory=False)
    old_mirror = await _find_child_exact(wiki_dir, old_name)
    if old_mirror is not None and await old_mirror.is_symlink():
        await old_mirror.unlink()
    if await _find_child_exact(wiki_dir, new_name) is None:
        await (wiki_dir / new_name).symlink_to(
            f"{lang_dir_name}/{new_stem}.md",
            target_is_directory=False,
        )


async def _read_rewrite_sources(
    plan: _ReprocessPlan,
    wiki_dir: Path,
) -> dict[str, str]:
    """Read the pre-rename text of every rewrite target as ``{path: text}``.

    Renames move files without altering bytes, so a rename destination is
    read from its rename source; targets renamed away do not exist after
    the apply run and are skipped. Missing and symlink targets are skipped
    just like the apply path.
    """
    rename_sources: dict[str, Path] = {}
    rename_source_paths: set[str] = set()
    for rename_action in plan.rename_actions:
        lang_dir = wiki_dir / rename_action.lang_dir_name
        source_path = lang_dir / f"{rename_action.old_stem}.md"
        rename_sources[fspath(lang_dir / f"{rename_action.new_stem}.md")] = source_path
        rename_source_paths.add(fspath(source_path))
    sources: dict[str, str] = {}
    for target in plan.rewrite_targets:
        target_path = Path(target)
        target_key = fspath(target_path)
        if target_key in rename_source_paths:
            continue
        source_path = rename_sources.get(target_key, target_path)
        if not await source_path.exists() or await source_path.is_symlink():
            continue
        sources[target_key] = await source_path.read_text(encoding="UTF-8")
    return sources


def _compute_rewrites(
    sources: Mapping[str, str],
    plan: _ReprocessPlan,
    migrations: Mapping[str, str],
) -> dict[str, str]:
    """Compute rewritten text for targets whose content actually changes."""
    rewrites: dict[str, str] = {}
    for target, original in sources.items():
        rewritten = _rewrite_markdown_links(
            original, migrations, names_map=plan.effective_map
        )
        heading = plan.heading_updates.get(target)
        if heading is not None:
            rewritten = _rewrite_article_heading(rewritten, heading)
        rewritten = _rewrite_markdown_headings(
            rewritten, plan.effective_map, migrations
        )
        if rewritten != original:
            rewrites[target] = rewritten
    return rewrites


async def apply_reprocess_plan(
    plan: _ReprocessPlan,
    *,
    dry_run: bool,
) -> _ReprocessReport:
    """Execute *plan* and return a summary report.

    Dry runs and real runs share the same report computation, so their
    reports match except for the ``dry_run`` flag.
    """
    wiki_dir = Path(plan.wiki_dir)
    migrations = _stem_migration_map(plan.stem_migrations)
    sources = await _read_rewrite_sources(plan, wiki_dir)
    rewrites = _compute_rewrites(sources, plan, migrations)
    listed_paths = set(plan.heading_updates)
    changed = tuple(
        dict.fromkeys(
            [
                *plan.new_mapping_keys,
                *(rename_action.old_stem for rename_action in plan.rename_actions),
                *(action.from_stem for action in plan.symlink_actions),
                *(Path(target).name.removesuffix(".md") for target in rewrites),
            ]
        )
    )

    if dry_run:
        return _ReprocessReport(
            mappings_added=len(plan.new_mapping_keys),
            symlinks_created=sum(
                1
                for action in plan.symlink_actions
                if action.kind == _SymlinkActionKind.CREATE
            ),
            symlinks_removed=sum(
                1
                for action in plan.symlink_actions
                if action.kind == _SymlinkActionKind.REMOVE
            ),
            symlinks_retargeted=sum(
                1
                for action in plan.symlink_actions
                if action.kind == _SymlinkActionKind.RETARGET
            ),
            files_renamed=len(plan.rename_actions),
            articles_rewritten=len(rewrites),
            links_updated_corpus=sum(
                1 for target in rewrites if target not in listed_paths
            ),
            dry_run=True,
            changed=changed,
        )

    await _save_names_map(plan.effective_map, path=plan.name_map_path)
    _reload_names_map()

    for rename_action in plan.rename_actions:
        await _apply_rename(
            wiki_dir,
            lang_dir_name=rename_action.lang_dir_name,
            old_stem=rename_action.old_stem,
            new_stem=rename_action.new_stem,
        )

    for action in plan.symlink_actions:
        if action.kind != _SymlinkActionKind.RENAME:
            continue
        await _apply_symlink_rename(
            wiki_dir,
            lang_dir_name=action.lang_dir_name,
            old_stem=action.from_stem,
            new_stem=action.to_stem,
            migrations=migrations,
        )

    symlinks_created = 0
    symlinks_removed = 0
    symlinks_retargeted = 0
    for action in plan.symlink_actions:
        lang_dir = wiki_dir / action.lang_dir_name
        match action.kind:
            case _SymlinkActionKind.CREATE:
                await _create_redirect_symlinks(
                    wiki_dir,
                    lang_dir,
                    action.from_stem,
                    action.to_stem,
                )
                symlinks_created += 1
            case _SymlinkActionKind.RETARGET:
                await _create_redirect_symlinks(
                    wiki_dir,
                    lang_dir,
                    action.from_stem,
                    action.to_stem,
                )
                symlinks_retargeted += 1
            case _SymlinkActionKind.REMOVE:
                await _remove_redirect_symlinks(
                    wiki_dir,
                    lang_dir,
                    action.from_stem,
                )
                symlinks_removed += 1
            case _SymlinkActionKind.RENAME:
                pass

    for target, rewritten in rewrites.items():
        target_path = Path(target)
        tmp = target_path.with_suffix(".md.tmp")
        await tmp.write_text(rewritten, encoding="UTF-8")
        await tmp.replace(target_path)

    return _ReprocessReport(
        mappings_added=len(plan.new_mapping_keys),
        symlinks_created=symlinks_created,
        symlinks_removed=symlinks_removed,
        symlinks_retargeted=symlinks_retargeted,
        files_renamed=len(plan.rename_actions),
        articles_rewritten=len(rewrites),
        links_updated_corpus=sum(
            1 for target in rewrites if target not in listed_paths
        ),
        dry_run=False,
        changed=changed,
    )


async def reprocess_articles(request: _ReprocessRequest) -> _ReprocessReport:
    """Plan and apply a reprocess run for *request*."""
    plan = await plan_reprocess(request)
    return await apply_reprocess_plan(plan, dry_run=request.dry_run)
