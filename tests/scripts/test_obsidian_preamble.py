"""Tests that the Obsidian MathJax preamble stays safe for MathJax 4.

The preamble feeds every math span in the notes, so a macro it redefines can
shadow the native MathJax 4 definition and break rendering. These tests pin the
polyfills that must remain and the macros that must be left to MathJax.
"""

from pathlib import Path
from re import compile as re_compile

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

"""Path of the Obsidian MathJax preamble, relative to the repository root."""
_PREAMBLE_PATH = Path(".obsidian/plugins/obsidian-latex/preamble.sty")

"""Macros MathJax 4 does not supply, which the preamble must define."""
_REQUIRED_DEFINITIONS = ("Eta", "argmax", "argmin", "Z", "degree", "texteuro")

"""Macros MathJax 4 supplies natively, which the preamble must not redefine."""
_NATIVE_MACROS = ("nobreak", "oiint", "oiiint", "AA")

r"""Regex matching a macro definition written with ``\def`` or ``\newcommand``."""
_DEFINITION_REGEX = re_compile(r"\\(?:def|newcommand)\*?\s*\{?\\(?P<name>[A-Za-z]+)")

r"""Regex matching the spaced ``\newcommand \Name`` form, which MathJax 4 rejects."""
_SPACED_NEWCOMMAND_REGEX = re_compile(r"\\newcommand\s+\\")


def _preamble_text() -> str:
    """Return the preamble decoded as UTF-8, read relative to the repository root."""
    return (Path(__file__).parents[2] / _PREAMBLE_PATH).read_text(encoding="utf-8")


class TestPreamblePolyfills:
    """Tests for the polyfills the preamble defines."""

    def test_defines_required_polyfills(self) -> None:
        r"""Should define every required polyfill with ``\def``."""
        text = _preamble_text()
        for name in _REQUIRED_DEFINITIONS:
            assert f"\\def\\{name}" in text


class TestPreambleSafety:
    """Tests for the definitions the preamble must not carry."""

    def test_omits_mathllap(self) -> None:
        r"""Should not need ``\mathllap``, which comes from mathtools."""
        assert "\\mathllap" not in _preamble_text()

    def test_uses_no_spaced_newcommand(self) -> None:
        r"""Should not use the ``\newcommand \Name`` space form."""
        offenders = [
            line
            for line in _preamble_text().splitlines()
            if _SPACED_NEWCOMMAND_REGEX.search(line)
        ]
        assert offenders == []

    def test_leaves_native_macros_to_mathjax(self) -> None:
        """Should not define the macros MathJax 4 supplies natively."""
        defined = set(_DEFINITION_REGEX.findall(_preamble_text()))
        # Guard against a regex that matches nothing, which would pass vacuously.
        assert set(_REQUIRED_DEFINITIONS) <= defined
        assert defined.isdisjoint(_NATIVE_MACROS)
