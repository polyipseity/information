"""Tests for scripts/convert_wiki/types.py.

These tests cover the _RedirectInfo dataclass and other type definitions.
"""

import dataclasses

from scripts.convert_wiki import types as _mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestRedirectInfo:
    """Tests for _RedirectInfo dataclass."""

    def test_default_tofragment(self) -> None:
        """tofragment should default to empty string."""
        info = _mod._RedirectInfo(to="Target Page")  # noqa: SLF001
        assert info.to == "Target Page"
        assert info.tofragment == ""

    def test_explicit_fragment(self) -> None:
        """tofragment should be settable."""
        info = _mod._RedirectInfo(to="Page", tofragment="section")  # noqa: SLF001
        assert info.tofragment == "section"

    def test_frozen(self) -> None:
        """_RedirectInfo should be frozen (immutable)."""

        assert dataclasses.is_dataclass(_mod._RedirectInfo)  # noqa: SLF001
        assert _mod._RedirectInfo.__dataclass_params__.frozen  # noqa: SLF001
