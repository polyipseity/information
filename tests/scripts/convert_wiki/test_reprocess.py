"""Tests for scripts.convert_wiki.reprocess."""

import json
from os import PathLike
from pathlib import Path

import pytest
from anyio import Path as AnyioPath

from scripts.convert_wiki.markdown_rewrite import (
    _rewrite_article_heading,
    _rewrite_markdown_links,
)
from scripts.convert_wiki.name_map_io import _merge_names_maps
from scripts.convert_wiki.reprocess.apply import apply_reprocess_plan
from scripts.convert_wiki.reprocess.plan import (
    _compute_stem_migrations,
    plan_reprocess,
)
from scripts.convert_wiki.types import (
    _ReprocessRequest,
    _SymlinkActionKind,
)

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

"""Directory of snapshot input and expected files."""
_SNAPSHOT_DIR = Path(__file__).resolve(strict=True).parent / "snapshots"


class TestPlanReprocess:
    """Pure planning tests."""

    def test_merge_mappings_cli_overrides_base(self) -> None:
        """CLI mappings should override the base map during planning."""
        base = {"Modern physics": "modern physics"}
        effective = _merge_names_maps(base, {"Modern physics": "Modern physics"})
        assert effective["Modern physics"] == "Modern physics"

    def test_stem_migration_from_mapping_change(self) -> None:
        """Mapping changes should produce stem migrations."""
        migrations = _compute_stem_migrations(
            ["Modern physics"],
            base_map={"Modern physics": "modern physics"},
            effective_map={"Modern physics": "Modern physics"},
        )
        assert len(migrations) == 1
        assert migrations[0].old_stem == "modern physics"
        assert migrations[0].new_stem == "Modern physics"

    @pytest.mark.anyio
    async def test_plan_rewrite_targets_scoped(
        self,
        tmp_path: PathLike[str],
    ) -> None:
        """Listed articles should be rewrite targets without --update-links."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        article = lang_dir / "modern physics.md"
        await article.write_text("# modern physics\n", encoding="UTF-8")
        other = lang_dir / "other.md"
        await other.write_text("[x](modern%20physics.md)\n", encoding="UTF-8")

        plan = await plan_reprocess(
            _ReprocessRequest(
                mappings={"Modern physics": "Modern physics"},
                articles=("modern physics",),
                update_links=False,
                dry_run=True,
                wiki_dir=wiki_dir,
                cache_path=wiki_dir / "cache.json",
                name_map_path=wiki_dir / "map.jsonc",
            ),
            base_map={"Modern physics": "modern physics"},
        )

        assert article in plan.rewrite_targets
        assert other not in plan.rewrite_targets


class TestApplyReprocess:
    """Filesystem apply tests."""

    @pytest.mark.anyio
    async def test_dry_run_no_writes(self, tmp_path: PathLike[str]) -> None:
        """Dry runs should not mutate files."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        article = lang_dir / "modern physics.md"
        await article.write_text("# modern physics\n", encoding="UTF-8")
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text(
            '{"Modern physics": "modern physics"}\n', encoding="UTF-8"
        )

        request = _ReprocessRequest(
            mappings={"Modern physics": "Modern physics"},
            articles=("modern physics",),
            update_links=False,
            dry_run=True,
            wiki_dir=wiki_dir,
            cache_path=wiki_dir / "cache.json",
            name_map_path=map_path,
        )
        plan = await plan_reprocess(
            request,
            base_map={"Modern physics": "modern physics"},
        )
        report = await apply_reprocess_plan(plan, dry_run=True)

        assert report.dry_run is True
        assert await map_path.read_text(encoding="UTF-8") == (
            '{"Modern physics": "modern physics"}\n'
        )

    @pytest.mark.anyio
    async def test_name_map_persisted(self, tmp_path: PathLike[str]) -> None:
        """Apply should persist the effective name map."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        article = lang_dir / "modern physics.md"
        await article.write_text("# modern physics\n", encoding="UTF-8")
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")

        request = _ReprocessRequest(
            mappings={"Modern physics": "Modern physics"},
            articles=(),
            update_links=False,
            dry_run=False,
            wiki_dir=wiki_dir,
            cache_path=wiki_dir / "cache.json",
            name_map_path=map_path,
        )
        plan = await plan_reprocess(request, base_map={})
        await apply_reprocess_plan(plan, dry_run=False)

        saved = json.loads(await map_path.read_text(encoding="UTF-8"))
        assert saved["Modern physics"] == "Modern physics"

    @pytest.mark.anyio
    async def test_apply_symlink_created(self, tmp_path: PathLike[str]) -> None:
        """Redirect cache entries should create symlinks when stems differ."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        target = lang_dir / "new title.md"
        await target.write_text("# new title\n", encoding="UTF-8")
        cache_path = wiki_dir / "cache.json"
        await cache_path.write_text(
            json.dumps(
                {
                    "old title": {
                        "to": "New title",
                        "tofragment": "",
                        "cached_at": "2099-01-01T00:00:00+00:00",
                    }
                }
            ),
            encoding="UTF-8",
        )
        map_path = wiki_dir / "map.jsonc"
        names_map = {"Old title": "old title", "New title": "new title"}
        await map_path.write_text(json.dumps(names_map), encoding="UTF-8")

        request = _ReprocessRequest(
            mappings={},
            articles=(),
            update_links=False,
            dry_run=False,
            wiki_dir=wiki_dir,
            cache_path=cache_path,
            name_map_path=map_path,
        )
        plan = await plan_reprocess(request, base_map=names_map)
        create_actions = [
            action
            for action in plan.symlink_actions
            if action.kind == _SymlinkActionKind.CREATE
        ]
        assert create_actions
        await apply_reprocess_plan(plan, dry_run=False)
        symlink = lang_dir / "old title.md"
        assert await symlink.is_symlink()
        assert str(await symlink.readlink()) == "new title.md"


class TestMarkdownRewriteSnapshot:
    """Regression snapshot for markdown rewrite."""

    def test_name_map_capitalization_snapshot(self) -> None:
        """Snapshot rewrite should match the expected fixture."""
        input_text = (_SNAPSHOT_DIR / "name_map_capitalization.input.md").read_text(
            encoding="UTF-8"
        )
        expected = (_SNAPSHOT_DIR / "name_map_capitalization.expected.md").read_text(
            encoding="UTF-8"
        )
        mappings = json.loads(
            (_SNAPSHOT_DIR / "name_map_capitalization.mappings.json").read_text(
                encoding="UTF-8"
            )
        )
        base = {"Modern physics": "modern physics", "modern physics": "modern physics"}
        effective = _merge_names_maps(base, mappings)
        migrations = _compute_stem_migrations(
            list(effective),
            base_map=base,
            effective_map=effective,
        )
        migration_map = {
            migration.old_stem: migration.new_stem for migration in migrations
        }
        rewritten = _rewrite_markdown_links(input_text, migration_map)
        rewritten = _rewrite_article_heading(rewritten, "Modern physics")
        assert rewritten == expected
