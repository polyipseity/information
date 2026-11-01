"""Tests for scripts.convert_wiki.stems."""

import pytest

from scripts.convert_wiki.stems import _stem_for_title

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestUnrepresentableStem:
    """A title whose stem names nothing stops the run."""

    @pytest.mark.parametrize("title", ["", " ", "\u00a0", ".", ".."])
    def test_a_title_with_no_usable_stem_raises(self, title: str) -> None:
        """A title that cannot name anything is refused."""
        with pytest.raises(ValueError, match="no usable filename stem"):
            _stem_for_title(title, {})

    def test_a_dotted_title_keeps_its_dot(self) -> None:
        """A dotted title keeps its dot."""
        assert _stem_for_title("Q.E.D.", {}) == "Q.E.D."
        assert _stem_for_title("I.i.d.", {"I.i.d.": "i.i.d."}) == "i.i.d."
