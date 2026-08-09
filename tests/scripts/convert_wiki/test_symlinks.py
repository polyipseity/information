"""Tests for scripts.convert_wiki.symlinks."""

from os import PathLike

import pytest
from anyio import Path as AnyioPath

from scripts.convert_wiki.symlinks import _resolve_local_target_filename

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestResolveLocalTargetFilename:
    """Tests for redirect target filename resolution."""

    @pytest.mark.anyio
    async def test_requires_exact_casing(self, tmp_path: PathLike[str]) -> None:
        """Wrong-cased on-disk targets must not satisfy canonical names."""
        lang_dir = AnyioPath(tmp_path)
        await (lang_dir / "Final page.md").write_text("x", encoding="UTF-8")

        resolved = await _resolve_local_target_filename(
            lang_dir=lang_dir,
            to_title="Intermediate",
            final_to_title="Final page",
            names_map={"Intermediate": "intermediate", "Final page": "final page"},
        )

        assert resolved == "intermediate.md"

    @pytest.mark.anyio
    async def test_prefers_exact_final_target(self, tmp_path: PathLike[str]) -> None:
        """Chain resolution should use final target when present with exact casing."""
        lang_dir = AnyioPath(tmp_path)
        await (lang_dir / "final page.md").write_text("x", encoding="UTF-8")

        resolved = await _resolve_local_target_filename(
            lang_dir=lang_dir,
            to_title="Intermediate",
            final_to_title="Final page",
            names_map={"Intermediate": "intermediate", "Final page": "final page"},
        )

        assert resolved == "final page.md"
