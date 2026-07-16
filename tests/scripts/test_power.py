"""Tests for ``scripts.power``.

This module tests the standalone script ``scripts/power.py``, which provides
an interactive helper for modular exponentiation experiments.  We test the
internal helper ``_pow`` as well as the interactive entry points by mocking
``builtins.input``.
"""

import builtins

from _pytest.capture import CaptureFixture
from pytest import MonkeyPatch

from scripts import power as _mod

"""No public symbols exported from this test module."""
__all__ = ()


class TestPowInternal:
    """Tests for ``_pow(a, b, c, d=0)`` — the pure helper function."""

    def test_pow_basic(self) -> None:
        """``_pow(2, 3, 100)`` → ``pow(2, 3, 100) + 0`` = 8."""
        assert _mod._pow(2, 3, 100) == 8

    def test_pow_with_addend(self) -> None:
        """``_pow(2, 3, 100, 5)`` → ``pow(2, 3, 100) + 5`` = 13."""
        assert _mod._pow(2, 3, 100, 5) == 13

    def test_pow_large_mod(self) -> None:
        """``_pow(2, 10, 100000000)`` → 1024 (since 2¹⁰ = 1024 < mod)."""
        assert _mod._pow(2, 10, 100000000) == 1024

    def test_pow_zero_exponent(self) -> None:
        """``_pow(5, 0, 7)`` → ``pow(5, 0, 7)`` = 1."""
        assert _mod._pow(5, 0, 7) == 1

    def test_pow_zero_base(self) -> None:
        """``_pow(0, 5, 10)`` → 0."""
        assert _mod._pow(0, 5, 10) == 0

    def test_pow_negative_base(self) -> None:
        """``_pow(-2, 3, 100)`` → ``pow(-2, 3, 100)`` = 92 (always non-negative)."""
        assert _mod._pow(-2, 3, 100) == 92

    def test_pow_mod_1(self) -> None:
        """``_pow(2, 5, 1)`` → 0 (any ``pow(a, b, 1)`` = 0)."""
        assert _mod._pow(2, 5, 1) == 0


class TestPowerInteractive:
    """Tests for the interactive entry points ``a()``, ``b()``, ``default()`` and ``main()``."""

    # ── Mode a ──────────────────────────────────────────────────────────────

    def test_mode_a_mocked(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """``a()`` with a=2, b=3 → ``pow(2, 3, 100000000)`` = 8."""
        inputs = iter(["2", "3"])

        def mock_input(_prompt: str = "") -> str:
            return next(inputs)

        monkeypatch.setattr(builtins, "input", mock_input)
        _mod.a()
        out = capsys.readouterr().out.strip()
        assert out == "8", f"Expected '8', got {out!r}"

    # ── Mode b ──────────────────────────────────────────────────────────────

    def test_mode_b_mocked(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """``b()`` with a=5, b=3 → ``pow(5, 3, 9999999) + 20000000`` = 20000125."""
        inputs = iter(["5", "3"])

        def mock_input(_prompt: str = "") -> str:
            return next(inputs)

        monkeypatch.setattr(builtins, "input", mock_input)
        _mod.b()
        out = capsys.readouterr().out.strip()
        expected = str(pow(5, 3, 9999999) + 20000000)
        assert out == expected, f"Expected {expected!r}, got {out!r}"

    # ── Dispatch via main ───────────────────────────────────────────────────

    def test_main_mode_a(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """``main()`` with m="a", a=2, b=3 → dispatches to ``a()`` → 8."""
        inputs = iter(["a", "2", "3"])

        def mock_input(_prompt: str = "") -> str:
            return next(inputs)

        monkeypatch.setattr(builtins, "input", mock_input)
        _mod.main()
        out = capsys.readouterr().out.strip().splitlines()
        # Should contain result line and ":)"

        # The first line must be the numeric result (8)
        assert out[0] == "8", f"Expected first line '8', got {out[0]!r}"
        assert ":)" in out, f"Expected ':)' in output lines {out!r}"

    def test_main_mode_b(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """``main()`` with m="b", a=5, b=3 → dispatches to ``b()``."""
        inputs = iter(["b", "5", "3"])

        def mock_input(_prompt: str = "") -> str:
            return next(inputs)

        monkeypatch.setattr(builtins, "input", mock_input)
        _mod.main()
        out = capsys.readouterr().out.strip().splitlines()
        expected_result = str(pow(5, 3, 9999999) + 20000000)
        assert out[0] == expected_result, (
            f"Expected first line {expected_result!r}, got {out[0]!r}"
        )
        assert ":)" in out, f"Expected ':)' in output lines {out!r}"

    def test_main_mode_default(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """``main()`` with unknown mode "x" → dispatches to ``default()``.

        ``default()`` prompts for a, b, c, d and computes ``pow(a,b,c)+d``.
        """
        inputs = iter(["x", "2", "3", "100", "5"])

        def mock_input(_prompt: str = "") -> str:
            return next(inputs)

        monkeypatch.setattr(builtins, "input", mock_input)
        _mod.main()
        out = capsys.readouterr().out.strip().splitlines()
        # pow(2, 3, 100) + 5 = 8 + 5 = 13
        assert out[0] == "13", f"Expected first line '13', got {out[0]!r}"
        assert ":)" in out, f"Expected ':)' in output lines {out!r}"

    # ── default() directly ──────────────────────────────────────────────────

    def test_default_mode_mocked(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """``default()`` with a=7, b=2, c=13, d=(empty→0) → ``pow(7,2,13)+0`` = 10."""
        inputs = iter(["7", "2", "13", ""])

        def mock_input(_prompt: str = "") -> str:
            return next(inputs)

        monkeypatch.setattr(builtins, "input", mock_input)
        _mod.default()
        out = capsys.readouterr().out.strip()
        expected = str(pow(7, 2, 13))
        assert out == expected, f"Expected {expected!r}, got {out!r}"
