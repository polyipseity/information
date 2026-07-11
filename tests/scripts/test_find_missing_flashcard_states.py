"""Tests for scripts/find_missing_flashcard_states.py."""

from pathlib import Path

import pytest

from scripts import find_missing_flashcard_states as _mod

FLASHCARD_STATE_REGEX_PATTERN = r"!\d{4}-\d{2}-\d{2}"


class TestFLASHCARD_STATE_REGEX:
    """Tests for the FLASHCARD_STATE_REGEX constant."""

    def test_regex_matches_date_annotations(self) -> None:
        """Should match standard flashcard state date annotations."""
        text = "!2024-01-15!2024-12-31"
        matches = _mod.FLASHCARD_STATE_REGEX.findall(text)
        assert matches == ["!2024-01-15", "!2024-12-31"]

    def test_regex_no_match_without_exclamation(self) -> None:
        """Should not match bare dates without leading '!'."""
        text = "2024-01-15"
        matches = _mod.FLASHCARD_STATE_REGEX.findall(text)
        assert matches == []

    def test_regex_invalid_date_format(self) -> None:
        """Should not match improperly formatted dates."""
        text = "!24-1-5 !2024/01/15 !2024-01"
        matches = _mod.FLASHCARD_STATE_REGEX.findall(text)
        assert matches == []

    def test_regex_embedded_in_sr_comment(self) -> None:
        """Should match dates inside <!--SR:...--> comments."""
        text = "<!--SR:!2024-01-15,100,5-->"
        matches = _mod.FLASHCARD_STATE_REGEX.findall(text)
        assert matches == ["!2024-01-15"]


class TestCheckFile:
    """Tests for the _check_file function."""

    @pytest.mark.anyio
    async def test_skip_directory(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should not print anything for a directory."""
        fake_path = _fake_path(monkeypatch, is_dir=True, text="")
        await _mod._check_file(fake_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_skip_symlink(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should not print anything for a symlink."""
        fake_path = _fake_path(monkeypatch, is_symlink=True, text="")
        await _mod._check_file(fake_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_no_markers_no_states(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should not print if there are no flashcard markers at all."""
        fake_path = _fake_path(monkeypatch, text="plain text without markers")
        await _mod._check_file(fake_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_equal_markers_and_states(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should not print if flashcard markers equal flashcard states."""
        text = "{@{cloze}@} <!--SR:!2024-01-15,100,5-->"
        fake_path = _fake_path(monkeypatch, text=text)
        await _mod._check_file(fake_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_more_states_than_markers(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should not print if there are more states than markers (unexpected but handled)."""
        text = "{@{cloze}@} <!--SR:!2024-01-15,100,5!2024-01-16,200,6-->"
        fake_path = _fake_path(monkeypatch, text=text)
        await _mod._check_file(fake_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_missing_states_printed(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should print file path when there are fewer states than markers."""
        text = "{@{cloze_a}@} {@{cloze_b}@} <!--SR:!2024-01-15,100,5-->"
        fake_path = _fake_path(monkeypatch, text=text)
        await _mod._check_file(fake_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert str(fake_path) in captured.out

    @pytest.mark.anyio
    async def test_counts_qa_markers(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should count ::@:: and :@: markers in addition to {@{."""
        text = "question ::@:: answer :@:"
        fake_path = _fake_path(monkeypatch, text=text)
        await _mod._check_file(fake_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert str(fake_path) in captured.out

    @pytest.mark.anyio
    async def test_mixed_markers_missing_states(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should detect missing states with mixed cloze and QA markers."""
        text = "{@{cloze}@} ::@:: <!--SR:!2024-01-15,100,5-->"
        fake_path = _fake_path(monkeypatch, text=text)
        await _mod._check_file(fake_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert str(fake_path) in captured.out

    @pytest.mark.anyio
    async def test_zero_markers_any_states(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should not print when there are zero markers regardless of states."""
        fake_path = _fake_path(monkeypatch, text="<!--SR:!2024-01-15,100,5-->")
        await _mod._check_file(fake_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""


class TestMain:
    """Tests for the main() function."""

    @pytest.mark.anyio
    async def test_path_prompt(
        self,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
        tmp_path: Path,
    ) -> None:
        """Should prompt for path and check files there."""
        (tmp_path / "ok.md").write_text(
            "{@{cloze}@} <!--SR:!2024-01-15,100,5-->",
            encoding="utf-8",
        )
        (tmp_path / "missing.md").write_text(
            "{@{cloze_a}@} {@{cloze_b}@} <!--SR:!2024-01-15,100,5-->",
            encoding="utf-8",
        )
        monkeypatch.setattr("builtins.input", lambda _: str(tmp_path))
        await _mod.main()
        captured = capsys.readouterr()
        assert str(tmp_path / "missing.md") in captured.out
        assert str(tmp_path / "ok.md") not in captured.out

    @pytest.mark.anyio
    async def test_skip_directory_entries(
        self,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
        tmp_path: Path,
    ) -> None:
        """Should skip subdirectories during iteration."""
        sub_dir = tmp_path / "sub"
        sub_dir.mkdir()
        (sub_dir / "nested.md").write_text(
            "{@{cloze}@}",
            encoding="utf-8",
        )
        monkeypatch.setattr("builtins.input", lambda _: str(tmp_path))
        await _mod.main()
        captured = capsys.readouterr()
        # sub directory itself is not a file, but its content shouldn't be checked
        # since we're iterating tmp_path, not recursing
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_all_ok(
        self,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
        tmp_path: Path,
    ) -> None:
        """Should not print anything when all files are fine."""
        (tmp_path / "a.md").write_text(
            "{@{cloze}@} <!--SR:!2024-01-15,100,5-->",
            encoding="utf-8",
        )
        (tmp_path / "b.md").write_text(
            "no markers at all",
            encoding="utf-8",
        )
        monkeypatch.setattr("builtins.input", lambda _: str(tmp_path))
        await _mod.main()
        captured = capsys.readouterr()
        assert captured.out == ""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fake_path(
    monkeypatch: pytest.MonkeyPatch,
    *,
    is_dir: bool = False,
    is_symlink: bool = False,
    text: str = "",
) -> object:
    """Return a stub Path-like object for _check_file testing."""

    class _FakePath:
        def __init__(self) -> None:
            self._is_dir = is_dir
            self._is_symlink = is_symlink
            self._text = text

        async def is_dir(self) -> bool:
            return self._is_dir

        async def is_symlink(self) -> bool:
            return self._is_symlink

        async def read_text(self) -> str:
            return self._text

        def __str__(self) -> str:
            return "/fake/path.md"

    return _FakePath()
