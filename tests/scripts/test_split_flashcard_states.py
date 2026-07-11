"""Tests for ``scripts.split_flashcard_states``.

This module tests the standalone script ``scripts/split_flashcard_states.py``,
which reads a combined flashcard state annotation string from stdin and
splits it into individual per-card annotations.  The script is not importable
as a library (``__all__ = ()``), so we test via ``from scripts import split_flashcard_states as _mod``.
"""

import builtins

from _pytest.capture import CaptureFixture
from pytest import MonkeyPatch

from scripts import split_flashcard_states as _mod

__all__ = ()


def _test_main(
    monkeypatch: "MonkeyPatch",
    capsys: "CaptureFixture[str]",
    input_str: str,
    *,
    expected_lines: list[str],
) -> None:
    """Helper: stub ``builtins.input``, call ``_mod.main()``, then verify output."""
    monkeypatch.setattr(builtins, "input", lambda _prompt: input_str)
    _mod.main()
    captured = capsys.readouterr()
    out = captured.out.splitlines()
    for line in expected_lines:
        assert line in out, f"Expected line {line!r} not found in output {out!r}"


class TestSplitFlashcardStates:
    """Test suite for ``split_flashcard_states.main()``."""

    # ── Basic splitting behaviour ────────────────────────────────────────────

    def test_main_two_states(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """Two states separated by ``!`` with full prefix/suffix."""
        _test_main(
            monkeypatch,
            capsys,
            "<!--SR:!a!b-->",
            expected_lines=["<!--SR:!a-->", "<!--SR:!b-->", ":)"],
        )

    def test_main_single_state(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """A single-state input produces exactly one annotation line."""
        _test_main(
            monkeypatch,
            capsys,
            "<!--SR:!a-->",
            expected_lines=["<!--SR:!a-->", ":)"],
        )

    def test_main_no_prefix_suffix(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """Input without ``<!--SR:!`` / ``-->`` still splits correctly.

        ``str.removeprefix`` / ``str.removesuffix`` are no-ops when the
        prefix/suffix is absent, so the raw content is split by ``!``.
        """
        _test_main(
            monkeypatch,
            capsys,
            "!a!b",
            expected_lines=["<!--SR:!a-->", "<!--SR:!b-->", ":)"],
        )

    def test_main_empty_input(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """Empty input produces only the ``:)`` trailer."""
        _test_main(
            monkeypatch,
            capsys,
            "",
            expected_lines=[":)"],
        )

    def test_main_whitespace_input(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """Whitespace-only input is stripped to empty, yielding only ``:)``."""
        _test_main(
            monkeypatch,
            capsys,
            "   \t  ",
            expected_lines=[":)"],
        )

    def test_main_trailing_separator(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """Trailing and repeated ``!`` separators are filtered out.

        ``filter(None, ...)`` removes empty strings produced by empty segments
        between consecutive or trailing ``!`` characters.
        """
        _test_main(
            monkeypatch,
            capsys,
            "<!--SR:!a!!b!-->",
            expected_lines=["<!--SR:!a-->", "<!--SR:!b-->", ":)"],
        )

    # ── Exact output format ──────────────────────────────────────────────────

    def test_main_happy_path_output_format(
        self, monkeypatch: "MonkeyPatch", capsys: "CaptureFixture[str]"
    ) -> None:
        """Verify the exact multiline output for ``<!--SR:!x!y-->``."""
        monkeypatch.setattr(builtins, "input", lambda _prompt: "<!--SR:!x!y-->")
        _mod.main()
        out = capsys.readouterr().out
        expected = "<!--SR:!x-->\n<!--SR:!y-->\n:)\n"
        assert out == expected, f"Output mismatch:\n{out!r} != {expected!r}"
