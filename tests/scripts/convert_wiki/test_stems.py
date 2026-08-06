"""Tests for scripts.convert_wiki.stems."""

from scripts.convert_wiki import config as _cfg
from scripts.convert_wiki.stems import _stem_for_title

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestStemForTitle:
    """Tests for _stem_for_title."""

    def test_uses_name_map(self) -> None:
        """Mapped titles should resolve to the configured stem."""
        names_map = {"Modern physics": "Modern physics"}
        assert _stem_for_title("Modern physics", names_map) == "Modern physics"

    def test_matches_legacy_target_filename_behavior(self) -> None:
        """Should match the old reconcile _target_filename heuristic."""
        title = next(iter(_cfg._NAMES_MAP))
        assert _stem_for_title(title) == _stem_for_title(title, _cfg._NAMES_MAP)
