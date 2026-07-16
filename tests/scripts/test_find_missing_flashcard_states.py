"""Tests for scripts/find_missing_flashcard_states.py."""

from os import PathLike, fspath

import pytest
from anyio import Path

from scripts import find_missing_flashcard_states as _mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

"""Regex pattern matching flashcard state date annotations (prefix ``!`` followed by ``YYYY-MM-DD``)."""
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
        self, capsys: pytest.CaptureFixture[str], tmp_path: PathLike[str]
    ) -> None:
        """Should not print anything for a directory."""
        tmp = Path(tmp_path)
        dir_path = tmp / "somedir"
        await dir_path.mkdir()
        await _mod._check_file(dir_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_skip_symlink(
        self, capsys: pytest.CaptureFixture[str], tmp_path: PathLike[str]
    ) -> None:
        """Should not print anything for a symlink."""
        tmp = Path(tmp_path)
        target = tmp / "target"
        await target.write_text("content", encoding="utf-8")
        link = tmp / "link"
        await link.symlink_to(target)
        await _mod._check_file(link)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_no_markers_no_states(
        self, capsys: pytest.CaptureFixture[str], tmp_path: PathLike[str]
    ) -> None:
        """Should not print if there are no flashcard markers at all."""
        tmp = Path(tmp_path)
        file_path = tmp / "test.md"
        await file_path.write_text("plain text without markers", encoding="utf-8")
        await _mod._check_file(file_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_equal_markers_and_states(
        self, capsys: pytest.CaptureFixture[str], tmp_path: PathLike[str]
    ) -> None:
        """Should not print if flashcard markers equal flashcard states."""
        tmp = Path(tmp_path)
        file_path = tmp / "test.md"
        await file_path.write_text(
            "{@{cloze}@} <!--SR:!2024-01-15,100,5-->", encoding="utf-8"
        )
        await _mod._check_file(file_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_more_states_than_markers(
        self, capsys: pytest.CaptureFixture[str], tmp_path: PathLike[str]
    ) -> None:
        """Should not print if there are more states than markers (unexpected but handled)."""
        tmp = Path(tmp_path)
        file_path = tmp / "test.md"
        await file_path.write_text(
            "{@{cloze}@} <!--SR:!2024-01-15,100,5!2024-01-16,200,6-->",
            encoding="utf-8",
        )
        await _mod._check_file(file_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""

    @pytest.mark.anyio
    async def test_missing_states_printed(
        self, capsys: pytest.CaptureFixture[str], tmp_path: PathLike[str]
    ) -> None:
        """Should print file path when there are fewer states than markers."""
        tmp = Path(tmp_path)
        file_path = tmp / "test.md"
        await file_path.write_text(
            "{@{cloze_a}@} {@{cloze_b}@} <!--SR:!2024-01-15,100,5-->",
            encoding="utf-8",
        )
        await _mod._check_file(file_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert fspath(file_path) in captured.out

    @pytest.mark.anyio
    async def test_counts_qa_markers(
        self, capsys: pytest.CaptureFixture[str], tmp_path: PathLike[str]
    ) -> None:
        """Should count ::@:: and :@: markers in addition to {@{."""
        tmp = Path(tmp_path)
        file_path = tmp / "test.md"
        await file_path.write_text("question ::@:: answer :@:", encoding="utf-8")
        await _mod._check_file(file_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert fspath(file_path) in captured.out

    @pytest.mark.anyio
    async def test_mixed_markers_missing_states(
        self, capsys: pytest.CaptureFixture[str], tmp_path: PathLike[str]
    ) -> None:
        """Should detect missing states with mixed cloze and QA markers."""
        tmp = Path(tmp_path)
        file_path = tmp / "test.md"
        await file_path.write_text(
            "{@{cloze}@} ::@:: <!--SR:!2024-01-15,100,5-->",
            encoding="utf-8",
        )
        await _mod._check_file(file_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert fspath(file_path) in captured.out

    @pytest.mark.anyio
    async def test_zero_markers_any_states(
        self, capsys: pytest.CaptureFixture[str], tmp_path: PathLike[str]
    ) -> None:
        """Should not print when there are zero markers regardless of states."""
        tmp = Path(tmp_path)
        file_path = tmp / "test.md"
        await file_path.write_text(
            "<!--SR:!2024-01-15,100,5-->", encoding="utf-8"
        )
        await _mod._check_file(file_path)  # noqa: SLF001
        captured = capsys.readouterr()
        assert captured.out == ""


class TestMain:
    """Tests for the main() function."""

    @pytest.mark.anyio
    async def test_path_prompt(
        self,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
        tmp_path: PathLike[str],
    ) -> None:
        """Should prompt for path and check files there."""
        tmp = Path(tmp_path)
        await (tmp / "ok.md").write_text(
            "{@{cloze}@} <!--SR:!2024-01-15,100,5-->",
            encoding="utf-8",
        )
        await (tmp / "missing.md").write_text(
            "{@{cloze_a}@} {@{cloze_b}@} <!--SR:!2024-01-15,100,5-->",
            encoding="utf-8",
        )
        monkeypatch.setattr("builtins.input", lambda _: fspath(tmp))
        await _mod.main()
        captured = capsys.readouterr()
        assert fspath(tmp / "missing.md") in captured.out
        assert fspath(tmp / "ok.md") not in captured.out

    @pytest.mark.anyio
    async def test_skip_directory_entries(
        self,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
        tmp_path: PathLike[str],
    ) -> None:
        """Should skip subdirectories during iteration."""
        tmp = Path(tmp_path)
        sub_dir = tmp / "sub"
        await sub_dir.mkdir()
        await (sub_dir / "nested.md").write_text(
            "{@{cloze}@}",
            encoding="utf-8",
        )
        monkeypatch.setattr("builtins.input", lambda _: fspath(tmp))
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
        tmp_path: PathLike[str],
    ) -> None:
        """Should not print anything when all files are fine."""
        tmp = Path(tmp_path)
        await (tmp / "a.md").write_text(
            "{@{cloze}@} <!--SR:!2024-01-15,100,5-->",
            encoding="utf-8",
        )
        await (tmp / "b.md").write_text(
            "no markers at all",
            encoding="utf-8",
        )
        monkeypatch.setattr("builtins.input", lambda _: fspath(tmp))
        await _mod.main()
        captured = capsys.readouterr()
        assert captured.out == ""
