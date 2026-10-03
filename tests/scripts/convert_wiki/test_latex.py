"""Tests for ``LatexConverter``."""

from __future__ import annotations

import pytest
from bs4 import BeautifulSoup, Tag

from scripts.convert_wiki.latex import LatexConverter

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


def _soup(html: str) -> Tag:
    """Parse *html* and return its single root element."""
    root = BeautifulSoup(html, "html.parser").find(True)
    assert isinstance(root, Tag)
    return root


class TestSfrac:
    """Tests for both ``sfrac`` layouts."""

    def test_class_based_fraction(self) -> None:
        """``span.num`` and ``span.den`` become numerator and denominator."""
        ele = _soup(
            '<span class="sfrac"><span class="tion">'
            '<span class="num"><i>dq</i></span>'
            '<span class="den"><i>dt</i></span></span></span>'
        )
        assert LatexConverter.texhtml_to_latex_sfrac(ele) == r"\frac{dq}{dt}"

    def test_class_based_fraction_nested_in_tion_wrapper(self) -> None:
        """The class-based layout survives its ``tion`` wrapper."""
        ele = _soup(
            '<span class="sfrac"><span class="num"><i>h</i></span>'
            '<span class="sr-only">per</span>'
            '<span class="den"><i>c</i></span></span>'
        )
        assert LatexConverter.texhtml_to_latex_sfrac(ele) == r"\frac{h}{c}"

    def test_style_based_dot_accent(self) -> None:
        """A shrunk accent block over a base block is a dot accent."""
        ele = _soup(
            '<span class="sfrac nowrap"><span style="display: inline-block">'
            '<span style="display: block; line-height: 0.3; font-size: 70%">\u22c5</span>'
            '<span style="display: block; line-height: 0.3"><i>q</i></span>'
            "</span></span>"
        )
        assert LatexConverter.texhtml_to_latex_sfrac(ele) == r"\dot{q}"

    def test_style_based_fraction(self) -> None:
        """``0.3`` over ``0.7`` line-heights is a fraction."""
        ele = _soup(
            '<span class="sfrac nowrap"><span style="display: inline-block">'
            '<span style="display: block; line-height: 0.3"><i>dq</i></span>'
            '<span style="display: block; line-height: 0.7"><i>dt</i></span>'
            "</span></span>"
        )
        assert LatexConverter.texhtml_to_latex_sfrac(ele) == r"\frac{dq}{dt}"

    def test_unreadable_layout_raises(self) -> None:
        """An sfrac neither reading covers is a defect, not an empty fraction."""
        ele = _soup('<span class="sfrac"><i>q</i></span>')
        with pytest.raises(ValueError, match="unreadable sfrac layout"):
            LatexConverter.texhtml_to_latex_sfrac(ele)

    def test_sup_script_follows_accent(self) -> None:
        """A trailing superscript joins the accent in one LaTeX string."""
        ele = _soup(
            '<span class="texhtml"><span class="sfrac nowrap">'
            '<span style="display: inline-block">'
            '<span style="display: block; line-height: 0.3; font-size: 70%">\u22c5</span>'
            '<span style="display: block; line-height: 0.3"><i>q</i></span>'
            "</span></span><sup><i>i</i></sup></span>"
        )
        assert LatexConverter.texhtml_to_latex(ele) == r"\dot{q}^{i}"


class TestRadicals:
    """Tests for radical markup."""

    def test_radical_with_vinculum(self) -> None:
        """A ``border-top`` span after the root sign is the radicand."""
        ele = _soup(
            '<span class="texhtml"><span class="nowrap">'
            '<span typeof="mw:Entity">\u221a</span>'
            '<span style="border-top: 1px solid; padding: 0px 0.1em"><i>t</i></span>'
            "</span></span>"
        )
        assert LatexConverter.texhtml_to_latex(ele) == r"\sqrt{t}"

    def test_radicand_with_greek_and_slash(self) -> None:
        """A radicand keeps its whole group and maps unicode math letters."""
        ele = _soup(
            '<span class="texhtml"><span class="nowrap">'
            '<span typeof="mw:Entity">\u221a</span>'
            '<span style="border-top: 1px solid"><i>\u0127</i>/(<i>m\u03c9</i>)</span>'
            "</span></span>"
        )
        assert LatexConverter.texhtml_to_latex(ele) == r"\sqrt{\hbar/(m{\omega})}"


class TestMathLetterCommands:
    """Tests for unicode math letters without an ASCII spelling."""

    @pytest.mark.parametrize(
        ("text", "expected"),
        [("\u0127", r"\hbar"), ("\u210f", r"\hbar")],
    )
    def test_letters_map_to_commands(self, text: str, expected: str) -> None:
        """Both h-with-stroke spellings become ``\\hbar``."""
        assert LatexConverter._escape_latex_text(text) == expected
