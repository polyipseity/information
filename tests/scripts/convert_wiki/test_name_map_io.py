"""Tests for scripts.convert_wiki.name_map_io."""

from os import PathLike

import pytest
from anyio import Path as AnyioPath

from scripts.convert_wiki import config as cfg
from scripts.convert_wiki.name_map_io import (
    _merge_names_maps,
    _new_mapping_keys,
    _reload_names_map,
    _save_names_map,
)

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestMergeNamesMaps:
    """Tests for _merge_names_maps."""

    def test_later_maps_override(self) -> None:
        """Later maps should override earlier keys."""
        merged = _merge_names_maps({"A": "a"}, {"A": "b"})
        assert merged == {"A": "b"}

    def test_new_mapping_keys(self) -> None:
        """Changed and new keys should be reported."""
        keys = _new_mapping_keys(
            {"Modern physics": "modern physics"},
            {"Modern physics": "Modern physics", "Foo": "foo"},
        )
        assert keys == ("Modern physics", "Foo")


class TestSaveNamesMap:
    """Tests for _save_names_map."""

    @pytest.mark.anyio
    async def test_round_trip(self, tmp_path: PathLike[str]) -> None:
        """Saved maps should be readable from disk."""
        path = AnyioPath(tmp_path) / "map.name_map.jsonc"
        await _save_names_map({"A": "a"}, path=path)
        text = await path.read_text(encoding="UTF-8")
        assert '"A": "a"' in text

    @pytest.mark.anyio
    async def test_reload_updates_module_map(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Reload should refresh the module-level map."""
        path = AnyioPath(tmp_path) / "map.name_map.jsonc"
        await _save_names_map({"Reload": "reload"}, path=path)
        monkeypatch.setattr(cfg, "_NAMES_MAP", {"Old": "old"})
        monkeypatch.setattr(
            cfg,
            "_load_names_map",
            lambda name_map_path=None: {"Reload": "reload"},
        )
        _reload_names_map()
        assert cfg._NAMES_MAP == {"Reload": "reload"}
