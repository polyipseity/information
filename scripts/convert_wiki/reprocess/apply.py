"""Apply a reprocess plan to the filesystem."""

from os import fspath, rename

from anyio import Path

from ..markdown_rewrite import _rewrite_article_heading, _rewrite_markdown_links
from ..name_map_io import _reload_names_map, _save_names_map
from ..types import (
    _ReprocessPlan,
    _ReprocessReport,
    _ReprocessRequest,
    _SymlinkActionKind,
)
from ..utils import _create_redirect_symlinks, _remove_redirect_symlinks
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
    old_note = lang_dir / f"{old_stem}.md"
    new_note = lang_dir / f"{new_stem}.md"
    old_mirror = wiki_dir / f"{old_stem}.md"
    new_mirror = wiki_dir / f"{new_stem}.md"
    tmp_note = old_note.with_suffix(".md.tmp")
    await old_note.rename(tmp_note)
    rename(fspath(tmp_note), fspath(new_note))
    if await old_mirror.is_symlink():
        await old_mirror.unlink()
    if not await new_mirror.exists():
        await new_mirror.symlink_to(
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
    old_path = lang_dir / f"{old_stem}.md"
    if not await old_path.is_symlink():
        return
    target = str(await old_path.readlink())
    if target.endswith(".md"):
        target_stem = target.removesuffix(".md")
        new_target = f"{migrations.get(target_stem, target_stem)}.md"
    else:
        new_target = target
    await old_path.unlink()
    new_path = lang_dir / f"{new_stem}.md"
    await new_path.symlink_to(new_target, target_is_directory=False)
    old_mirror = wiki_dir / f"{old_stem}.md"
    new_mirror = wiki_dir / f"{new_stem}.md"
    if await old_mirror.is_symlink():
        await old_mirror.unlink()
    if not await new_mirror.exists():
        await new_mirror.symlink_to(
            f"{lang_dir_name}/{new_stem}.md",
            target_is_directory=False,
        )


async def apply_reprocess_plan(
    plan: _ReprocessPlan,
    *,
    dry_run: bool,
) -> _ReprocessReport:
    """Execute *plan* and return a summary report."""
    wiki_dir = Path(plan.wiki_dir)
    migrations = _stem_migration_map(plan.stem_migrations)
    changed: list[str] = []
    mappings_added = len(plan.new_mapping_keys)
    symlinks_created = 0
    symlinks_removed = 0
    symlinks_retargeted = 0
    files_renamed = 0
    articles_rewritten = 0
    links_updated_corpus = 0
    listed_paths = set(plan.heading_updates)

    if dry_run:
        changed.extend(plan.new_mapping_keys)
        changed.extend(action.from_stem for action in plan.symlink_actions)
        changed.extend(rename_action.old_stem for rename_action in plan.rename_actions)
        return _ReprocessReport(
            mappings_added=mappings_added,
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
            articles_rewritten=len(plan.rewrite_targets),
            links_updated_corpus=len(plan.rewrite_targets),
            dry_run=True,
            changed=tuple(dict.fromkeys(changed)),
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
        files_renamed += 1
        changed.append(rename_action.old_stem)

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
        changed.append(action.from_stem)

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
                changed.append(action.from_stem)
            case _SymlinkActionKind.RETARGET:
                await _create_redirect_symlinks(
                    wiki_dir,
                    lang_dir,
                    action.from_stem,
                    action.to_stem,
                )
                symlinks_retargeted += 1
                changed.append(action.from_stem)
            case _SymlinkActionKind.REMOVE:
                await _remove_redirect_symlinks(
                    wiki_dir,
                    lang_dir,
                    action.from_stem,
                )
                symlinks_removed += 1
                changed.append(action.from_stem)
            case _SymlinkActionKind.RENAME:
                pass

    for target in plan.rewrite_targets:
        target_path = Path(target)
        if not await target_path.exists() or await target_path.is_symlink():
            continue
        original = await target_path.read_text(encoding="UTF-8")
        rewritten = _rewrite_markdown_links(original, migrations)
        heading = plan.heading_updates.get(fspath(target_path))
        if heading is not None:
            rewritten = _rewrite_article_heading(rewritten, heading)
        if rewritten != original:
            tmp = target_path.with_suffix(".md.tmp")
            await tmp.write_text(rewritten, encoding="UTF-8")
            await tmp.replace(target_path)
            articles_rewritten += 1
            if fspath(target_path) not in listed_paths:
                links_updated_corpus += 1
            changed.append(target_path.name.removesuffix(".md"))

    return _ReprocessReport(
        mappings_added=mappings_added,
        symlinks_created=symlinks_created,
        symlinks_removed=symlinks_removed,
        symlinks_retargeted=symlinks_retargeted,
        files_renamed=files_renamed,
        articles_rewritten=articles_rewritten,
        links_updated_corpus=links_updated_corpus,
        dry_run=False,
        changed=tuple(dict.fromkeys(changed)),
    )


async def reprocess_articles(request: _ReprocessRequest) -> _ReprocessReport:
    """Plan and apply a reprocess run for *request*."""
    plan = await plan_reprocess(request)
    return await apply_reprocess_plan(plan, dry_run=request.dry_run)
