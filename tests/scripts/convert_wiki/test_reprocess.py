"""Tests for scripts.convert_wiki.reprocess."""

import json
from os import PathLike

import json5
import pytest
from anyio import Path as AnyioPath

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


class TestPlanReprocess:
    """Pure planning tests."""

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

        saved = json5.loads(await map_path.read_text(encoding="UTF-8"))
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


class TestColonTitleReprocess:
    """A mapped title whose text contains ``:`` must reach every link.

    ``_encode_fragment`` drops ``:``, so an anchor never spells its key, and
    ``_fix_stem`` maps ``:`` to ``_``, so a stem never spells one either.
    Both are resolved through the effective name map instead of guessed at.
    """

    @staticmethod
    async def _make_wiki(tmp_path: PathLike[str]) -> tuple[AnyioPath, AnyioPath]:
        """Build a wiki with a colon section, a colon article, and one reader."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        await (lang_dir / "A_ b.md").write_text("# A: b\n", encoding="UTF-8")
        await (lang_dir / "evidence.md").write_text(
            "# Evidence\n"
            "\n"
            "## A: b\n"
            "\n"
            "See [self](#A%20b), [page](A%5F%20b.md), and\n"
            "[section](A%5F%20b.md#A%20b).\n",
            encoding="UTF-8",
        )
        await (wiki_dir / "map.jsonc").write_text("{}\n", encoding="UTF-8")
        return wiki_dir, lang_dir

    @pytest.mark.anyio
    async def test_mapping_rewrites_anchors_and_stems(
        self, tmp_path: PathLike[str]
    ) -> None:
        """A case-only colon mapping rewrites the anchor and the link stems."""
        wiki_dir, lang_dir = await self._make_wiki(tmp_path)

        plan = await plan_reprocess(
            _ReprocessRequest(
                mappings={"A: b": "a: b"},
                articles=("evidence",),
                update_links=False,
                dry_run=False,
                wiki_dir=wiki_dir,
                cache_path=wiki_dir / "cache.json",
                name_map_path=wiki_dir / "map.jsonc",
            ),
            base_map={},
        )

        assert plan.rename_actions == ()
        assert plan.base_map == {}
        report = await apply_reprocess_plan(plan, dry_run=False)
        assert report.articles_rewritten == 1
        assert await (lang_dir / "evidence.md").read_text(encoding="UTF-8") == (
            "# Evidence\n"
            "\n"
            "## a: b\n"
            "\n"
            "See [self](#a%20b), [page](a%5F%20b.md), and\n"
            "[section](a%5F%20b.md#a%20b).\n"
        )

    @pytest.mark.anyio
    async def test_article_already_at_its_final_name_is_rewritten(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Typing the raw title resolves to the sanitised note already on disk."""
        wiki_dir, lang_dir = await self._make_wiki(tmp_path)

        plan = await plan_reprocess(
            _ReprocessRequest(
                mappings={"A: b": "a: b"},
                articles=("A: b",),
                update_links=False,
                dry_run=False,
                wiki_dir=wiki_dir,
                cache_path=wiki_dir / "cache.json",
                name_map_path=wiki_dir / "map.jsonc",
            ),
            base_map={},
        )

        assert plan.rename_actions == ()
        assert list(plan.heading_updates.values()) == ["a: b"]
        await apply_reprocess_plan(plan, dry_run=False)
        assert await (lang_dir / "A_ b.md").read_text(encoding="UTF-8") == ("# a: b\n")


class TestCollidingNameMap:
    """A name map that two titles claim differently stops the run early."""

    @pytest.mark.anyio
    async def test_planning_refuses_a_collision(self, tmp_path: PathLike[str]) -> None:
        """A collision raises while planning, before any action is decided."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        await (wiki_dir / "map.jsonc").write_text("{}\n", encoding="UTF-8")

        with pytest.raises(ValueError, match="name map collision"):
            await plan_reprocess(
                _ReprocessRequest(
                    mappings={"A: b": "x", "A b": "y"},
                    articles=(),
                    update_links=False,
                    dry_run=True,
                    wiki_dir=wiki_dir,
                    cache_path=wiki_dir / "cache.json",
                    name_map_path=wiki_dir / "map.jsonc",
                ),
                base_map={},
            )
