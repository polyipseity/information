"""Tests for the --repair-illegal-names reprocess pass."""

from os import PathLike

import pytest
from anyio import Path as AnyioPath

from scripts.convert_wiki.reprocess.apply import apply_reprocess_plan
from scripts.convert_wiki.reprocess.plan import plan_reprocess
from scripts.convert_wiki.types import _ReprocessRequest

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestRepairIllegalNames:
    """Only a name no filesystem can hold is rewritten."""

    @pytest.mark.anyio
    async def test_a_flagged_run_repairs_an_impossible_link(
        self, tmp_path: PathLike[str]
    ) -> None:
        """An impossible stem becomes the sanitised name, a legal one stays."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        await (wiki_dir / "map.jsonc").write_text("{}\n", encoding="UTF-8")
        await (lang_dir / "note.md").write_text(
            "see [a](C*-algebra.md) and [b](i.i.d..md)\n", encoding="UTF-8"
        )
        request = _ReprocessRequest(
            mappings={},
            articles=(),
            update_links=True,
            repair_illegal_names=True,
            dry_run=False,
            wiki_dir=wiki_dir,
            cache_path=wiki_dir / "cache.json",
            name_map_path=wiki_dir / "map.jsonc",
        )
        plan = await plan_reprocess(request, base_map={})
        report = await apply_reprocess_plan(plan, dry_run=False)

        assert report.names_repaired == 1
        assert await (lang_dir / "note.md").read_text(encoding="UTF-8") == (
            "see [a](C%5F-algebra.md) and [b](i.i.d..md)\n"
        )

    @pytest.mark.anyio
    async def test_an_unflagged_run_leaves_the_link_alone(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Without the flag, the corpus pass rewrites no impossible name."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        await (wiki_dir / "map.jsonc").write_text("{}\n", encoding="UTF-8")
        await (lang_dir / "note.md").write_text(
            "see [a](C*-algebra.md)\n", encoding="UTF-8"
        )
        request = _ReprocessRequest(
            mappings={},
            articles=(),
            update_links=True,
            dry_run=False,
            wiki_dir=wiki_dir,
            cache_path=wiki_dir / "cache.json",
            name_map_path=wiki_dir / "map.jsonc",
        )
        plan = await plan_reprocess(request, base_map={})
        report = await apply_reprocess_plan(plan, dry_run=False)

        assert report.names_repaired == 0
        assert await (lang_dir / "note.md").read_text(encoding="UTF-8") == (
            "see [a](C*-algebra.md)\n"
        )
