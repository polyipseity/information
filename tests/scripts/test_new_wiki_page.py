"""Tests for scripts/new_wiki_page.py."""

from collections.abc import Callable
from os import PathLike
from pathlib import Path as PathlibPath

import pytest
from anyio import Path

from scripts import new_wiki_page as _mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestResolveLang:
    """Tests for the _resolve_lang function."""

    def test_english_alpha2(self) -> None:
        """Should resolve 'en' to English."""
        dir_code, name, _ = _mod._resolve_lang("en")  # noqa: SLF001
        assert dir_code == "eng"
        assert name == "English"

    def test_english_alpha3(self) -> None:
        """Should resolve 'eng' to English."""
        dir_code, name, _ = _mod._resolve_lang("eng")  # noqa: SLF001
        assert dir_code == "eng"
        assert name == "English"

    def test_chinese_alpha2(self) -> None:
        """Should resolve 'zh' to Chinese."""
        dir_code, name, _ = _mod._resolve_lang("zh")  # noqa: SLF001
        assert dir_code == "zho"
        assert name == "Chinese"

    def test_chinese_alpha3(self) -> None:
        """Should resolve 'zho' to Chinese."""
        dir_code, name, _ = _mod._resolve_lang("zho")  # noqa: SLF001
        assert dir_code == "zho"
        assert name == "Chinese"

    def test_case_and_whitespace_insensitive(self) -> None:
        """Should be case and whitespace insensitive."""
        dir_code, name, _ = _mod._resolve_lang("  EN  ")  # noqa: SLF001
        assert dir_code == "eng"
        assert name == "English"

    def test_unknown_code_raises(self) -> None:
        """Should raise LookupError for unknown codes."""
        with pytest.raises(LookupError, match="unknown language code"):
            _mod._resolve_lang("xyz")  # noqa: SLF001


class TestMain:
    """Tests for the main() function."""

    def _fake_input(self, answers: list[str]) -> Callable[[str], str]:
        """Return a fake input() that yields pre-defined answers."""
        answers_iter = iter(answers)

        def fake(prompt: str = "") -> str:
            """Return next answer from pre-defined list."""
            return next(answers_iter)

        return fake

    @pytest.mark.anyio
    async def test_normal_creation(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: PathLike[str]
    ) -> None:
        """Should create a note file and symlink for a valid language/article."""
        # Point REPO_ROOT to tmp_path
        tmp = Path(tmp_path)
        general_dir = tmp / "general"
        eng_dir = general_dir / "eng"
        await eng_dir.mkdir(parents=True)

        monkeypatch.setattr("scripts.new_wiki_page._REPO_ROOT", tmp_path)
        monkeypatch.setattr("builtins.input", self._fake_input(["", "Fourier transform"]))

        await _mod.main()

        # Check the note file was created
        note_path = eng_dir / "Fourier transform.md"
        assert await note_path.is_file()
        content = await note_path.read_text(encoding="utf-8")
        assert "Fourier transform" in content
        assert "eng" in content
        assert "English" in content

        # Check the symlink was created
        link_path = general_dir / "Fourier transform.md"
        assert await link_path.is_symlink()

    @pytest.mark.anyio
    async def test_note_already_exists(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: PathLike[str]
    ) -> None:
        """Should raise FileExistsError when note already exists."""
        tmp = Path(tmp_path)
        general_dir = tmp / "general"
        eng_dir = general_dir / "eng"
        await eng_dir.mkdir(parents=True)
        await (eng_dir / "Fourier transform.md").touch()

        monkeypatch.setattr("scripts.new_wiki_page._REPO_ROOT", tmp_path)
        monkeypatch.setattr("builtins.input", self._fake_input(["", "Fourier transform"]))

        with pytest.raises(FileExistsError, match="note already exists"):
            await _mod.main()

    @pytest.mark.anyio
    async def test_symlink_already_exists(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: PathLike[str]
    ) -> None:
        """Should raise FileExistsError when symlink target already exists."""
        tmp = Path(tmp_path)
        general_dir = tmp / "general"
        eng_dir = general_dir / "eng"
        await eng_dir.mkdir(parents=True)
        await (general_dir / "Fourier transform.md").touch()

        monkeypatch.setattr("scripts.new_wiki_page._REPO_ROOT", tmp_path)
        monkeypatch.setattr("builtins.input", self._fake_input(["", "Fourier transform"]))

        with pytest.raises(FileExistsError, match="symlink target already exists"):
            await _mod.main()

    @pytest.mark.anyio
    async def test_missing_language_directory(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: PathLike[str]
    ) -> None:
        """Should raise FileNotFoundError when language directory does not exist."""
        tmp = Path(tmp_path)
        general_dir = tmp / "general"
        await general_dir.mkdir()
        # No eng/ directory
        monkeypatch.setattr("scripts.new_wiki_page._REPO_ROOT", tmp_path)
        monkeypatch.setattr("builtins.input", self._fake_input(["", "Fourier transform"]))

        with pytest.raises(FileNotFoundError, match="language directory does not exist"):
            await _mod.main()

    @pytest.mark.anyio
    async def test_empty_name_raises(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: PathLike[str]
    ) -> None:
        """Should raise ValueError when name is empty."""
        tmp = Path(tmp_path)
        general_dir = tmp / "general"
        eng_dir = general_dir / "eng"
        await eng_dir.mkdir(parents=True)

        monkeypatch.setattr("scripts.new_wiki_page._REPO_ROOT", tmp_path)
        monkeypatch.setattr("builtins.input", self._fake_input(["", ""]))

        with pytest.raises(ValueError, match="name cannot be empty"):
            await _mod.main()

    @pytest.mark.anyio
    async def test_cleanup_on_failure(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: PathLike[str]
    ) -> None:
        """Should clean up temporary files on failure."""
        tmp = Path(tmp_path)
        general_dir = tmp / "general"
        eng_dir = general_dir / "eng"
        await eng_dir.mkdir(parents=True)

        monkeypatch.setattr("scripts.new_wiki_page._REPO_ROOT", tmp_path)
        monkeypatch.setattr("builtins.input", self._fake_input(["", "Fourier transform"]))

        # Simulate an OSError during temp file write
        original_write_text = PathlibPath.write_text

        def broken_write_text(
            self, data: str, encoding: str | None = None, errors: str | None = None, newline: str | None = None
        ) -> int:
            """Simulate write failure for .md.tmp files."""
            if str(self).endswith(".md.tmp"):
                raise OSError("Simulated write failure")
            return original_write_text(self, data, encoding=encoding, errors=errors, newline=newline)

        monkeypatch.setattr(PathlibPath, "write_text", broken_write_text)

        with pytest.raises(OSError, match="Simulated write failure"):
            await _mod.main()

        # Verify no temp files or partial output remains
        assert not await (eng_dir / "Fourier transform.md").exists()
        assert not await (eng_dir / "Fourier transform.md.tmp").exists()
        assert not await (general_dir / "Fourier transform.md.link.tmp").exists()

    @pytest.mark.anyio
    async def test_uppercases_title_correctly(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: PathLike[str]
    ) -> None:
        """Should handle titles with special characters."""
        tmp = Path(tmp_path)
        general_dir = tmp / "general"
        eng_dir = general_dir / "eng"
        await eng_dir.mkdir(parents=True)

        monkeypatch.setattr("scripts.new_wiki_page._REPO_ROOT", tmp_path)
        monkeypatch.setattr(
            "builtins.input",
            self._fake_input(["", "Fourier transform (disambiguation)"]),
        )

        await _mod.main()

        note_path = eng_dir / "Fourier transform (disambiguation).md"
        content = await note_path.read_text(encoding="utf-8")
        # Title should have disambiguation stripped
        assert "aliases:\n  - Fourier transform" in content
        # Wikipedia URL should have underscores
        assert "Fourier_transform_(disambiguation)" in content

    @pytest.mark.anyio
    async def test_symlink_target_is_correct(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: PathLike[str]
    ) -> None:
        """Should create symlink pointing to the correct relative target."""
        tmp = Path(tmp_path)
        general_dir = tmp / "general"
        eng_dir = general_dir / "eng"
        await eng_dir.mkdir(parents=True)

        monkeypatch.setattr("scripts.new_wiki_page._REPO_ROOT", tmp_path)
        monkeypatch.setattr("builtins.input", self._fake_input(["", "Fourier transform"]))

        await _mod.main()

        link_path = general_dir / "Fourier transform.md"
        assert await link_path.is_symlink()
        assert await link_path.readlink() == Path("eng/Fourier transform.md")
