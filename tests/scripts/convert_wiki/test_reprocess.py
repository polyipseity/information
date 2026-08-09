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
    async def test_plan_article_rename_no_false_conflict_on_case_only(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Case-only renames should not raise when only wrong casing exists on disk."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        await (lang_dir / "modern physics.md").write_text(
            "# modern physics\n", encoding="UTF-8"
        )
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")

        plan = await plan_reprocess(
            _ReprocessRequest(
                mappings={"Modern physics": "Modern physics"},
                articles=("modern physics",),
                update_links=False,
                dry_run=True,
                wiki_dir=wiki_dir,
                cache_path=wiki_dir / "cache.json",
                name_map_path=map_path,
            ),
            base_map={"Modern physics": "modern physics"},
        )

        assert len(plan.rename_actions) == 1
        assert plan.rename_actions[0].new_stem == "Modern physics"

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

        assert lang_dir / "Modern physics.md" in plan.rewrite_targets
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


class TestReprocessJumpUpGuard:
    """Citation UI titles must not drive redirect symlink planning."""

    @pytest.mark.anyio
    async def test_reprocess_does_not_create_jump_up_symlink(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Jump up cache pollution must not create redirect symlinks."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        cache_path = wiki_dir / "cache.json"
        await cache_path.write_text(
            json.dumps(
                {
                    "Jump up": {
                        "to": "Jump Up",
                        "tofragment": "",
                        "cached_at": "2099-01-01T00:00:00+00:00",
                    }
                }
            ),
            encoding="UTF-8",
        )
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")

        plan = await plan_reprocess(
            _ReprocessRequest(
                mappings={},
                articles=(),
                update_links=False,
                dry_run=True,
                wiki_dir=wiki_dir,
                cache_path=cache_path,
                name_map_path=map_path,
            ),
            base_map={},
        )
        assert not any(action.from_stem == "jump up" for action in plan.symlink_actions)


class TestReprocessSymlinkRename:
    """Capitalization migrations should rename existing redirect symlinks."""

    @pytest.mark.anyio
    async def test_plan_symlink_rename_on_capitalization(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Existing capitalized redirect symlinks should plan RENAME actions."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        symlink = lang_dir / "Exponential map (Lie group).md"
        await symlink.symlink_to(
            "Exponential map (Lie theory).md", target_is_directory=False
        )
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")

        plan = await plan_reprocess(
            _ReprocessRequest(
                mappings={
                    "Exponential map (Lie group)": "exponential map (Lie group)",
                    "Exponential map (Lie theory)": "exponential map (Lie theory)",
                },
                articles=(),
                update_links=False,
                dry_run=True,
                wiki_dir=wiki_dir,
                cache_path=wiki_dir / "cache.json",
                name_map_path=map_path,
            ),
            base_map={},
        )
        rename_actions = [
            action
            for action in plan.symlink_actions
            if action.from_stem == "Exponential map (Lie group)"
            and action.to_stem == "exponential map (Lie group)"
        ]
        assert rename_actions

    @pytest.mark.anyio
    async def test_apply_symlink_rename_and_retarget(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Renamed symlinks should use lowercase stems and migrated targets."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        symlink = lang_dir / "Exponential map (Lie group).md"
        await symlink.symlink_to(
            "Exponential map (Lie theory).md", target_is_directory=False
        )
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")

        request = _ReprocessRequest(
            mappings={
                "Exponential map (Lie group)": "exponential map (Lie group)",
                "Exponential map (Lie theory)": "exponential map (Lie theory)",
            },
            articles=(),
            update_links=False,
            dry_run=False,
            wiki_dir=wiki_dir,
            cache_path=wiki_dir / "cache.json",
            name_map_path=map_path,
        )
        plan = await plan_reprocess(request, base_map={})
        await apply_reprocess_plan(plan, dry_run=False)

        assert not await (lang_dir / "Exponential map (Lie group).md").exists()
        renamed = lang_dir / "exponential map (Lie group).md"
        assert await renamed.is_symlink()
        assert str(await renamed.readlink()) == "exponential map (Lie theory).md"

    @pytest.mark.anyio
    async def test_apply_top_level_mirror_renamed(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Top-level mirrors should follow lowercase redirect symlink renames."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        await (lang_dir / "Exponential map (Lie group).md").symlink_to(
            "Exponential map (Lie theory).md", target_is_directory=False
        )
        await (wiki_dir / "Exponential map (Lie group).md").symlink_to(
            "eng/Exponential map (Lie group).md", target_is_directory=False
        )
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")

        request = _ReprocessRequest(
            mappings={
                "Exponential map (Lie group)": "exponential map (Lie group)",
                "Exponential map (Lie theory)": "exponential map (Lie theory)",
            },
            articles=(),
            update_links=False,
            dry_run=False,
            wiki_dir=wiki_dir,
            cache_path=wiki_dir / "cache.json",
            name_map_path=map_path,
        )
        plan = await plan_reprocess(request, base_map={})
        await apply_reprocess_plan(plan, dry_run=False)

        mirror = wiki_dir / "exponential map (Lie group).md"
        assert await mirror.is_symlink()
        assert str(await mirror.readlink()) == "eng/exponential map (Lie group).md"
        assert not await (wiki_dir / "Exponential map (Lie group).md").exists()

    @pytest.mark.anyio
    async def test_apply_article_rename_from_stem_migration(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Listed articles should rename via stem migrations, not only map keys."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        article = lang_dir / "modern physics.md"
        await article.write_text("# modern physics\n", encoding="UTF-8")
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")

        request = _ReprocessRequest(
            mappings={"Modern physics": "Modern physics"},
            articles=("modern physics",),
            update_links=False,
            dry_run=False,
            wiki_dir=wiki_dir,
            cache_path=wiki_dir / "cache.json",
            name_map_path=map_path,
        )
        plan = await plan_reprocess(
            request,
            base_map={"Modern physics": "modern physics"},
        )
        await apply_reprocess_plan(plan, dry_run=False)

        renamed = lang_dir / "Modern physics.md"
        assert await renamed.is_file()
        assert not await renamed.is_symlink()

    @pytest.mark.anyio
    async def test_apply_rewrites_parenthetical_link_in_article(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Reprocess should rewrite parenthetical .md link targets in articles."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        article = lang_dir / "tetrad formalism.md"
        await article.write_text(
            "See [exp](Exponential%20map%20(Lie%20group).md).\n",
            encoding="UTF-8",
        )
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")

        request = _ReprocessRequest(
            mappings={
                "Exponential map (Lie group)": "exponential map (Lie group)",
            },
            articles=("tetrad formalism",),
            update_links=False,
            dry_run=False,
            wiki_dir=wiki_dir,
            cache_path=wiki_dir / "cache.json",
            name_map_path=map_path,
        )
        plan = await plan_reprocess(request, base_map={})
        await apply_reprocess_plan(plan, dry_run=False)

        rewritten = await article.read_text(encoding="UTF-8")
        assert "exponential%20map%20(Lie%20group).md" in rewritten
        assert "Exponential%20map%20(Lie%20group).md" not in rewritten


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

    def test_name_map_parenthetical_capitalization_snapshot(self) -> None:
        """Snapshot rewrite should handle parenthetical .md link targets."""
        input_text = (
            _SNAPSHOT_DIR / "name_map_parenthetical_capitalization.input.md"
        ).read_text(encoding="UTF-8")
        expected = (
            _SNAPSHOT_DIR / "name_map_parenthetical_capitalization.expected.md"
        ).read_text(encoding="UTF-8")
        mappings = json.loads(
            (
                _SNAPSHOT_DIR / "name_map_parenthetical_capitalization.mappings.json"
            ).read_text(encoding="UTF-8")
        )
        base = {
            "Exponential map (Lie group)": "Exponential map (Lie group)",
            "Modern physics": "modern physics",
        }
        effective = _merge_names_maps(base, mappings)
        migration_map = {
            migration.old_stem: migration.new_stem
            for migration in _compute_stem_migrations(
                list(effective),
                base_map=base,
                effective_map=effective,
            )
        }
        rewritten = _rewrite_markdown_links(input_text, migration_map)
        assert rewritten == expected
