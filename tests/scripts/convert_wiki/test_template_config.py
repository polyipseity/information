"""Tests for template_config shared constants."""

from scripts.convert_wiki.template_config import (
    _ATOMIC_TAGS,
    _BLOCK_TAGS,
    _BLOCKQUOTE_CLASSES,
    _BLOCKQUOTE_PREFIX_RE,
    _BOXED_CLASSES,
    _DISPLAY_MATH_CONTAINERS,
    _DISPLAY_MATH_ENVIRONMENTS,
    _INFOBOX_CAPTION_RULES,
    _INLINE_LIST_CLASSES,
    _MEDIA_TAGS,
    _NAVBOX_SPEC,
    _OPAQUE_SPAN_CLASSES,
    _SEPARATOR_CELL_RE,
    _SIDEBAR_SPEC,
)

"""Public symbols exported by this module (none)."""
__all__ = ()


class TestDisplayMathContainers:
    """Tests for the _DISPLAY_MATH_CONTAINERS constant."""

    def test_contains_dd_dt(self) -> None:
        """Verify dd and dt are in the set."""
        assert "dd" in _DISPLAY_MATH_CONTAINERS
        assert "dt" in _DISPLAY_MATH_CONTAINERS

    def test_does_not_contain_p(self) -> None:
        """Verify p is not in the set."""
        assert "p" not in _DISPLAY_MATH_CONTAINERS


class TestSeparatorCellRe:
    """Tests for the _SEPARATOR_CELL_RE regex pattern."""

    def test_matches_standard(self) -> None:
        """Verify standard triple-dash separator matches."""
        assert bool(_SEPARATOR_CELL_RE.fullmatch("---"))

    def test_matches_colon_aligned(self) -> None:
        """Verify colon-aligned separators match."""
        assert bool(_SEPARATOR_CELL_RE.fullmatch(":--"))
        assert bool(_SEPARATOR_CELL_RE.fullmatch("--:"))
        assert bool(_SEPARATOR_CELL_RE.fullmatch(":-:"))

    def test_matches_short(self) -> None:
        """Verify short double-dash matches (len check is external)."""
        # The regex itself matches short strings; _is_separator_cell adds len >= 3
        assert bool(_SEPARATOR_CELL_RE.fullmatch("--"))


class TestBlockquotePrefixRe:
    """Tests for the _BLOCKQUOTE_PREFIX_RE regex pattern."""

    def test_matches_single(self) -> None:
        """Verify single blockquote prefix matches."""
        assert bool(_BLOCKQUOTE_PREFIX_RE.match("> "))

    def test_matches_nested(self) -> None:
        """Verify nested blockquote prefix matches."""
        assert bool(_BLOCKQUOTE_PREFIX_RE.match("> > "))

    def test_rejects_non_blockquote(self) -> None:
        """Verify non-blockquote text does not match."""
        assert not _BLOCKQUOTE_PREFIX_RE.match("hello")


class TestBoxedClasses:
    """Tests for the _BOXED_CLASSES frozenset."""

    def test_equation_box_present(self) -> None:
        """Verify equation-box is in the set."""
        assert "equation-box" in _BOXED_CLASSES

    def test_blockquote_classes_excludes_equation_box(self) -> None:
        """Verify _BLOCKQUOTE_CLASSES excludes equation-box but includes quotebox."""
        assert "equation-box" not in _BLOCKQUOTE_CLASSES
        assert "quotebox" in _BLOCKQUOTE_CLASSES


class TestOpaqueSpanClasses:
    """Tests for the _OPAQUE_SPAN_CLASSES frozenset."""

    def test_includes_boxed(self) -> None:
        """Verify _BOXED_CLASSES is a subset of _OPAQUE_SPAN_CLASSES."""
        assert _BOXED_CLASSES <= _OPAQUE_SPAN_CLASSES

    def test_includes_hatnote(self) -> None:
        """Verify hatnote is in the set."""
        assert "hatnote" in _OPAQUE_SPAN_CLASSES


class TestMediaTags:
    """Tests for the _MEDIA_TAGS frozenset."""

    def test_audio_video(self) -> None:
        """Verify audio and video tags are present."""
        assert "audio" in _MEDIA_TAGS
        assert "video" in _MEDIA_TAGS


class TestAtomicTags:
    """Tests for the _ATOMIC_TAGS frozenset."""

    def test_br_hr_img(self) -> None:
        """Verify br, hr, and img tags are present."""
        assert "br" in _ATOMIC_TAGS
        assert "hr" in _ATOMIC_TAGS
        assert "img" in _ATOMIC_TAGS


class TestBlockTags:
    """Tests for the _BLOCK_TAGS frozenset."""

    def test_common_block_elements(self) -> None:
        """Verify common block-level elements are present."""
        for tag in ("div", "p", "table", "ul", "ol", "dl", "pre"):
            assert tag in _BLOCK_TAGS


class TestDisplayMathEnvironments:
    """Tests for the _DISPLAY_MATH_ENVIRONMENTS tuple."""

    def test_contains_common_envs(self) -> None:
        """Verify common LaTeX environments are present."""
        for env in ("aligned", "align", "cases", "matrix"):
            assert env in _DISPLAY_MATH_ENVIRONMENTS

    def test_is_tuple(self) -> None:
        """Verify the constant is a tuple."""
        assert isinstance(_DISPLAY_MATH_ENVIRONMENTS, tuple)


class TestInlineListClasses:
    """Tests for the _INLINE_LIST_CLASSES frozenset."""

    def test_portalbox_present(self) -> None:
        """Verify portalbox is in the set."""
        assert "portalbox" in _INLINE_LIST_CLASSES


class TestNavboxSpec:
    """Tests for the _NAVBOX_SPEC dataclass."""

    def test_linear_indices(self) -> None:
        """Verify linear column indices."""
        assert _NAVBOX_SPEC.linear_indices == (0, 2, 3, 4)

    def test_angular_indices(self) -> None:
        """Verify angular column indices."""
        assert _NAVBOX_SPEC.angular_indices == (5, 6, 7, 8)

    def test_required_tr_count(self) -> None:
        """Verify required tr count is 2."""
        assert _NAVBOX_SPEC.required_tr_count == 2

    def test_min_inner_table_rows(self) -> None:
        """Verify minimum inner table rows is 3."""
        assert _NAVBOX_SPEC.min_inner_table_rows == 3

    def test_required_outer_classes(self) -> None:
        """Verify navbox-inner is a required outer class."""
        assert "navbox-inner" in _NAVBOX_SPEC.required_outer_classes


class TestSidebarSpec:
    """Tests for the _SIDEBAR_SPEC dataclass."""

    def test_trigger_classes(self) -> None:
        """Verify sidebar and cm-sidebar trigger classes."""
        assert "sidebar" in _SIDEBAR_SPEC.trigger_classes
        assert "cm-sidebar" in _SIDEBAR_SPEC.trigger_classes

    def test_wrap_rules_count(self) -> None:
        """Verify there are 3 wrap rules."""
        assert len(_SIDEBAR_SPEC.wrap_rules) == 3

    def test_caption(self) -> None:
        """Verify caption class and tag."""
        assert _SIDEBAR_SPEC.caption_class == "sidebar-caption"
        assert _SIDEBAR_SPEC.caption_tag == "i"


class TestInfoboxCaptionRules:
    """Tests for the _INFOBOX_CAPTION_RULES tuple."""

    def test_above_rule(self) -> None:
        """Verify infobox-above rule exists with correct properties."""
        rules = [r for r in _INFOBOX_CAPTION_RULES if r.cell_class == "infobox-above"]
        assert len(rules) == 1
        assert rules[0].cell_tag == "th"
        assert rules[0].wrap_tag == "b"

    def test_image_rule(self) -> None:
        """Verify infobox-image rule exists with correct properties."""
        rules = [r for r in _INFOBOX_CAPTION_RULES if r.cell_class == "infobox-image"]
        assert len(rules) == 1
        assert rules[0].cell_tag == "td"
        assert rules[0].wrap_tag is None
