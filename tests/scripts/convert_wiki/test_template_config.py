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
    def test_contains_dd_dt(self) -> None:
        assert "dd" in _DISPLAY_MATH_CONTAINERS
        assert "dt" in _DISPLAY_MATH_CONTAINERS

    def test_does_not_contain_p(self) -> None:
        assert "p" not in _DISPLAY_MATH_CONTAINERS


class TestSeparatorCellRe:
    def test_matches_standard(self) -> None:
        assert bool(_SEPARATOR_CELL_RE.fullmatch("---"))

    def test_matches_colon_aligned(self) -> None:
        assert bool(_SEPARATOR_CELL_RE.fullmatch(":--"))
        assert bool(_SEPARATOR_CELL_RE.fullmatch("--:"))
        assert bool(_SEPARATOR_CELL_RE.fullmatch(":-:"))

    def test_matches_short(self) -> None:
        # The regex itself matches short strings; _is_separator_cell adds len >= 3
        assert bool(_SEPARATOR_CELL_RE.fullmatch("--"))


class TestBlockquotePrefixRe:
    def test_matches_single(self) -> None:
        assert bool(_BLOCKQUOTE_PREFIX_RE.match("> "))

    def test_matches_nested(self) -> None:
        assert bool(_BLOCKQUOTE_PREFIX_RE.match("> > "))

    def test_rejects_non_blockquote(self) -> None:
        assert not _BLOCKQUOTE_PREFIX_RE.match("hello")


class TestBoxedClasses:
    def test_equation_box_present(self) -> None:
        assert "equation-box" in _BOXED_CLASSES

    def test_blockquote_classes_excludes_equation_box(self) -> None:
        assert "equation-box" not in _BLOCKQUOTE_CLASSES
        assert "quotebox" in _BLOCKQUOTE_CLASSES


class TestOpaqueSpanClasses:
    def test_includes_boxed(self) -> None:
        assert _BOXED_CLASSES <= _OPAQUE_SPAN_CLASSES

    def test_includes_hatnote(self) -> None:
        assert "hatnote" in _OPAQUE_SPAN_CLASSES


class TestMediaTags:
    def test_audio_video(self) -> None:
        assert "audio" in _MEDIA_TAGS
        assert "video" in _MEDIA_TAGS


class TestAtomicTags:
    def test_br_hr_img(self) -> None:
        assert "br" in _ATOMIC_TAGS
        assert "hr" in _ATOMIC_TAGS
        assert "img" in _ATOMIC_TAGS


class TestBlockTags:
    def test_common_block_elements(self) -> None:
        for tag in ("div", "p", "table", "ul", "ol", "dl", "pre"):
            assert tag in _BLOCK_TAGS


class TestDisplayMathEnvironments:
    def test_contains_common_envs(self) -> None:
        for env in ("aligned", "align", "cases", "matrix"):
            assert env in _DISPLAY_MATH_ENVIRONMENTS

    def test_is_tuple(self) -> None:
        assert isinstance(_DISPLAY_MATH_ENVIRONMENTS, tuple)


class TestInlineListClasses:
    def test_portalbox_present(self) -> None:
        assert "portalbox" in _INLINE_LIST_CLASSES


class TestNavboxSpec:
    def test_linear_indices(self) -> None:
        assert _NAVBOX_SPEC.linear_indices == (0, 2, 3, 4)

    def test_angular_indices(self) -> None:
        assert _NAVBOX_SPEC.angular_indices == (5, 6, 7, 8)

    def test_required_tr_count(self) -> None:
        assert _NAVBOX_SPEC.required_tr_count == 2

    def test_min_inner_table_rows(self) -> None:
        assert _NAVBOX_SPEC.min_inner_table_rows == 3

    def test_required_outer_classes(self) -> None:
        assert "navbox-inner" in _NAVBOX_SPEC.required_outer_classes


class TestSidebarSpec:
    def test_trigger_classes(self) -> None:
        assert "sidebar" in _SIDEBAR_SPEC.trigger_classes
        assert "cm-sidebar" in _SIDEBAR_SPEC.trigger_classes

    def test_wrap_rules_count(self) -> None:
        assert len(_SIDEBAR_SPEC.wrap_rules) == 3

    def test_caption(self) -> None:
        assert _SIDEBAR_SPEC.caption_class == "sidebar-caption"
        assert _SIDEBAR_SPEC.caption_tag == "i"


class TestInfoboxCaptionRules:
    def test_above_rule(self) -> None:
        rules = [r for r in _INFOBOX_CAPTION_RULES if r.cell_class == "infobox-above"]
        assert len(rules) == 1
        assert rules[0].cell_tag == "th"
        assert rules[0].wrap_tag == "b"

    def test_image_rule(self) -> None:
        rules = [r for r in _INFOBOX_CAPTION_RULES if r.cell_class == "infobox-image"]
        assert len(rules) == 1
        assert rules[0].cell_tag == "td"
        assert rules[0].wrap_tag is None
