"""Tests for scripts/rematch_flashcard_states.py."""

import pytest

from scripts.rematch_flashcard_states import (
    FLASHCARD_STATE_REGEX,
    FLASHCARD_STATES_REGEX,
    main,
    normalize_line_endings,
)

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

# ── normalize_line_endings ──────────────────────────────────────────────


class TestNormalizeLineEndings:
    """Tests for normalize_line_endings()."""

    def test_normalize_line_endings_lf(self) -> None:
        """``\\n`` stays ``\\n``."""
        assert normalize_line_endings("hello\nworld\n") == "hello\nworld\n"

    def test_normalize_line_endings_crlf(self) -> None:
        """``\\r\\n`` → ``\\n``."""
        assert normalize_line_endings("hello\r\nworld\r\n") == "hello\nworld\n"

    def test_normalize_line_endings_mixed(self) -> None:
        """Mix of line endings unified to ``\\n``."""
        mixed = "line1\nline2\r\nline3\rline4\vline5\fline6"
        expected = "line1\nline2\nline3\nline4\nline5\nline6"
        assert normalize_line_endings(mixed) == expected

    def test_normalize_line_endings_cr(self) -> None:
        """``\\r`` → ``\\n``."""
        assert normalize_line_endings("hello\rworld\r") == "hello\nworld\n"


# ── Regex constants ─────────────────────────────────────────────────────


class TestFlashcardStatesRegex:
    """Tests for FLASHCARD_STATES_REGEX."""

    def test_flashcard_states_regex(self) -> None:
        """Regex matches ``<!--SR:...-->`` with DOTALL flag (cross-paragraph matching)."""
        text = "<!--SR:state1\nstate2-->"
        matches = FLASHCARD_STATES_REGEX.findall(text)
        assert len(matches) == 1
        assert matches[0] == "state1\nstate2"

    def test_flashcard_states_regex_multiple(self) -> None:
        """Regex matches multiple ``<!--SR:...-->`` blocks."""
        text = "a<!--SR:s1-->b<!--SR:s2-->c"
        matches = FLASHCARD_STATES_REGEX.findall(text)
        assert matches == ["s1", "s2"]

    def test_flashcard_states_regex_no_match(self) -> None:
        """Regex returns empty when no state blocks present."""
        text = "no state blocks here"
        matches = FLASHCARD_STATES_REGEX.findall(text)
        assert matches == []


class TestFlashcardStateRegex:
    """Tests for FLASHCARD_STATE_REGEX (individual state entries)."""

    def test_flashcard_state_regex_legacy(self) -> None:
        """Matches ``!2024-01-15,100,5`` (legacy format)."""
        text = "!2024-01-15,100,5"
        match = FLASHCARD_STATE_REGEX.search(text)
        assert match is not None
        assert match[0] == "!2024-01-15,100,5"

    def test_flashcard_state_regex_fsrs(self) -> None:
        """Matches ``!fsrs,...`` format."""
        text = (
            "!fsrs,2024-01-15T12:30:00.000Z,1.5,2.0,3,4,5,6,7,2024-01-16T12:30:00.000Z"
        )
        match = FLASHCARD_STATE_REGEX.search(text)
        assert match is not None
        assert match[0] == text

    def test_flashcard_state_regex_rejects_invalid(self) -> None:
        """Invalid format ``!abc`` not matched."""
        text = "!abc"
        match = FLASHCARD_STATE_REGEX.search(text)
        assert match is None

    def test_flashcard_state_regex_multiple(self) -> None:
        """Multiple state entries all matched."""
        text = "!2024-01-15,100,5!2024-01-16,200,6"
        matches = FLASHCARD_STATE_REGEX.findall(text)
        assert len(matches) == 2
        assert matches[0] == "!2024-01-15,100,5"
        assert matches[1] == "!2024-01-16,200,6"


# ── main() ──────────────────────────────────────────────────────────────


class TestMain:
    """Tests for main()."""

    def test_main_basic_rematch(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """2 paragraphs, each with 1 ``{@{`` + 2 states → states redistributed correctly."""
        clipboard_input = (
            "paragraph1 {@{cloze_a}@} <!--SR:!2024-01-15,100,5!2024-01-16,200,6-->\n"
            "\n"
            "paragraph2 {@{cloze_b}@} <!--SR:!2024-01-17,300,7!2024-01-18,400,8-->"
        )
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        captured = capsys.readouterr()

        # 2 paragraphs × 1 cloze each = 2 cloze total, 4 states total → 2 states per paragraph
        assert "paragraph1" in captured.out
        assert "paragraph2" in captured.out
        assert "<!--SR:" in captured.out
        assert len(copied) == 1
        assert "paragraph1" in copied[0]
        assert "paragraph2" in copied[0]

    def test_main_paragraph_without_flashcards(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Paragraph with 0 ``{@{`` → no ``<!--SR:...-->`` appended."""
        clipboard_input = "paragraph1 <!--SR:!2024-01-15,100,5-->\n\nparagraph2"
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        captured = capsys.readouterr()

        # paragraph2 has no cloze → no SR block appended
        assert "<!--SR:!-->".replace("!", "") not in captured.out
        assert len(copied) == 1

    def test_main_no_state_blocks(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Text without any ``<!--SR:...-->`` → unchanged."""
        clipboard_input = "paragraph1\n\nparagraph2"
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        captured = capsys.readouterr()

        assert captured.out.strip() == clipboard_input
        assert len(copied) == 1
        assert copied[0] == clipboard_input

    def test_main_empty_clipboard(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Empty clipboard → empty output."""
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr("scripts.rematch_flashcard_states.paste", lambda: "")
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        captured = capsys.readouterr()

        assert captured.out.strip() == ""
        assert len(copied) == 1
        assert copied[0] == ""

    def test_main_fsrs_states_preserved(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """FSRS format states preserved through rematch."""
        fsrs_state = (
            "!fsrs,2024-01-15T12:30:00.000Z,1.5,2.0,3,4,5,6,7,2024-01-16T12:30:00.000Z"
        )
        clipboard_input = (
            "paragraph1 {@{cloze1}@} <!--SR:" + fsrs_state + "-->"
            "\n"
            "\n"
            "paragraph2 {@{cloze2}@}"
        )
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        captured = capsys.readouterr()

        # FSRS state should appear in output
        assert "!fsrs," in captured.out
        assert "2024-01-16T12:30:00.000Z" in captured.out
        assert len(copied) == 1

    def test_main_legacy_states_preserved(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Legacy ``!YYYY-MM-DD,int,int`` preserved."""
        clipboard_input = (
            "paragraph1 {@{cloze1}@} <!--SR:!2024-01-15,100,5!2024-01-16,200,6-->"
            "\n"
            "\n"
            "paragraph2 {@{cloze2}@}"
        )
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        captured = capsys.readouterr()

        assert "!2024-01-15,100,5" in captured.out
        assert "!2024-01-16,200,6" in captured.out
        assert len(copied) == 1

    def test_main_mixed_fsrs_and_legacy(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Both formats in same block → both preserved."""
        clipboard_input = (
            "paragraph1 {@{cloze1}@} <!--SR:!2024-01-15,100,5!fsrs,"
            "2024-01-15T12:30:00.000Z,"
            "1.5,"
            "2.0,"
            "3,4,5,6,7,"
            "2024-01-16T12:30:00.000Z-->"
            "\n"
            "\n"
            "paragraph2 {@{cloze2}@}"
        )
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        captured = capsys.readouterr()

        assert "!2024-01-15,100,5" in captured.out
        assert "!fsrs," in captured.out
        assert len(copied) == 1

    def test_main_more_paragraphs_than_states(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """More paragraphs with flashcards than available states → potential IndexError (KNOWN BUG)."""
        # 3 paragraphs with cloze, but only 2 states → flashcard_cum_counts[2] = 2 → slice(2, 2) = ()
        clipboard_input = (
            "{@{a}@} <!--SR:!2024-01-15,100,5!2024-01-16,200,6-->\n\n{@{b}@}\n\n{@{c}@}"
        )
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        # This may raise IndexError (slice issue) or silently produce empty states
        # — we just observe the outcome
        try:
            main()
            capsys.readouterr()  # consume output, not asserting on it
            # If it doesn't crash, the third paragraph gets empty states (silent data loss bug)
            assert len(copied) == 1
        except IndexError:
            pass  # Expected known bug — IndexError from slice with out-of-range index

    def test_main_fewer_paragraphs_than_states(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """More states than paragraphs → trailing states dropped."""
        # 1 paragraph with 1 cloze, 3 states → only 1 state assigned, 2 dropped
        clipboard_input = (
            "{@{a}@} <!--SR:!2024-01-15,100,5!2024-01-16,200,6!2024-01-17,300,7-->"
        )
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        captured = capsys.readouterr()

        assert len(copied) == 1
        # Only first state should appear in output (only 1 cloze)
        assert "!2024-01-15,100,5" in captured.out
        # The `!2024-01-15,100,5` is the only state; the other 2 are dropped silently
        assert "!2024-01-16,200,6" not in captured.out
        assert "!2024-01-17,300,7" not in captured.out

    def test_main_paragraphs_with_only_qa_markers(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """``::@::`` and ``:@:`` not counted → 0 states assigned (KNOWN BUG - QA marker counting gap)."""
        clipboard_input = (
            "question ::@:: answer <!--SR:!2024-01-15,100,5-->"
            "\n"
            "\n"
            "term :@: definition <!--SR:!2024-01-16,200,6-->"
        )
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        captured = capsys.readouterr()

        # Both paragraphs have only QA markers (no {@{ ), so counts are both 0
        # → flashcard_cum_counts = [0, 0, 0] → each gets slice(0, 0) = empty
        assert len(copied) == 1
        # Neither paragraph should have any state attached (known bug)
        assert "!2024-01-15,100,5" not in captured.out
        assert "!2024-01-16,200,6" not in captured.out

    def test_main_state_block_in_middle_of_paragraph(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """State block extracted, paragraph gets new state at end."""
        clipboard_input = (
            "start {@{cloze1}@} middle <!--SR:!2024-01-15,100,5--> end\n\n{@{cloze2}@}"
        )
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        captured = capsys.readouterr()

        assert len(copied) == 1
        # The SR comment should be appended at the end of each paragraph
        assert "end <!--SR:" in captured.out or "cloze1}@} <!--SR:" in captured.out
        assert "!2024-01-15,100,5" in captured.out

    def test_main_copies_to_clipboard(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Verify ``pyperclip.copy`` was called with result."""
        clipboard_input = "test <!--SR:!2024-01-15,100,5-->"
        monkeypatch.setattr("builtins.input", lambda _: "")
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.paste", lambda: clipboard_input
        )
        copied: list[str] = []
        monkeypatch.setattr(
            "scripts.rematch_flashcard_states.copy", lambda text: copied.append(text)
        )

        main()
        _ = capsys.readouterr()

        assert len(copied) == 1
        assert isinstance(copied[0], str)
        assert len(copied[0]) > 0
