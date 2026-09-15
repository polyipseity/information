"""Tests for scripts.convert_wiki.reprocess."""

from dataclasses import replace
from os import PathLike

import pytest
from anyio import Path as AnyioPath

from scripts.convert_wiki.reprocess.apply import apply_reprocess_plan
from scripts.convert_wiki.reprocess.plan import (
    plan_reprocess,
)
from scripts.convert_wiki.types import (
    _ReprocessRequest,
)

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

"""Directory of snapshot input and expected files."""


class TestReprocessSymlinkRename:
    """Capitalization migrations should rename existing redirect symlinks."""

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

    @pytest.mark.anyio
    async def test_apply_rewrites_headings_at_all_levels(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Reprocess should re-case section headers at every level and rename."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        article = lang_dir / "modern physics.md"
        await article.write_text(
            "# modern physics\n\n## modern physics\n\n### modern physics\n\n"
            "See [physics](modern%20physics.md).\n\n"
            "{@{Link [inside](modern%20physics.md)}@}\n",
            encoding="UTF-8",
        )
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
        rewritten = await renamed.read_text(encoding="UTF-8")
        assert rewritten == (
            "# Modern physics\n\n## Modern physics\n\n### Modern physics\n\n"
            "See [physics](Modern%20physics.md).\n\n"
            "{@{Link [inside](Modern%20physics.md)}@}\n"
        )

    @pytest.mark.anyio
    async def test_dry_run_report_matches_apply_report(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Dry-run and apply reports should match except for the dry_run flag."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        article = lang_dir / "modern physics.md"
        await article.write_text(
            "# modern physics\n\nSee [d'Alembert](Jean%20le%20Rond%20d'Alembert.md).\n",
            encoding="UTF-8",
        )
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")
        base_map = {
            "Modern physics": "modern physics",
            "Jean le Rond d'Alembert": "Jean le Rond d'Alembert",
        }
        mappings = {
            "Modern physics": "Modern physics",
            "Jean le Rond d'Alembert": "Jean Le Rond d'Alembert",
        }

        request = _ReprocessRequest(
            mappings=mappings,
            articles=("modern physics",),
            update_links=False,
            dry_run=True,
            wiki_dir=wiki_dir,
            cache_path=wiki_dir / "cache.json",
            name_map_path=map_path,
        )
        dry_plan = await plan_reprocess(request, base_map=base_map)
        dry_report = await apply_reprocess_plan(dry_plan, dry_run=True)

        apply_plan = await plan_reprocess(
            replace(request, dry_run=False), base_map=base_map
        )
        apply_report = await apply_reprocess_plan(apply_plan, dry_run=False)

        assert dry_report.dry_run is True
        assert apply_report.dry_run is False
        assert dry_report == replace(apply_report, dry_run=True)

    @pytest.mark.anyio
    async def test_dry_run_no_writes_and_reports_actual_changes(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Dry-run should not mutate files and should count only articles whose text changes."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        article = lang_dir / "modern physics.md"
        await article.write_text(
            "# Modern physics\n\nNo links to migrate here.\n",
            encoding="UTF-8",
        )
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")

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
        assert report.files_renamed == 1
        assert report.articles_rewritten == 0
        assert report.links_updated_corpus == 0
        # Verify no files were mutated
        assert await article.read_text(encoding="UTF-8") == (
            "# Modern physics\n\nNo links to migrate here.\n"
        )

    @pytest.mark.anyio
    async def test_apply_rewrites_apostrophe_link(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Reprocess should rewrite apostrophe .md link targets in articles."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        article = lang_dir / "modern physics.md"
        await article.write_text(
            "See [d'Alembert](Jean%20le%20Rond%20d'Alembert.md).\n",
            encoding="UTF-8",
        )
        map_path = wiki_dir / "map.jsonc"
        await map_path.write_text("{}\n", encoding="UTF-8")

        request = _ReprocessRequest(
            mappings={"Jean le Rond d'Alembert": "Jean Le Rond d'Alembert"},
            articles=("modern physics",),
            update_links=False,
            dry_run=False,
            wiki_dir=wiki_dir,
            cache_path=wiki_dir / "cache.json",
            name_map_path=map_path,
        )
        plan = await plan_reprocess(
            request,
            base_map={"Jean le Rond d'Alembert": "Jean le Rond d'Alembert"},
        )
        await apply_reprocess_plan(plan, dry_run=False)

        rewritten = await article.read_text(encoding="UTF-8")
        assert "Jean%20Le%20Rond%20d'Alembert.md" in rewritten
        assert "Jean%20le%20Rond%20d'Alembert.md" not in rewritten
