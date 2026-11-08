"""Tests for scripts/audit_math_macros.py."""

from os import PathLike, fspath
from pathlib import Path

import pytest

from scripts import audit_math_macros as _mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestMathSegments:
    """Tests for the _math_segments function."""

    def test_ignores_frontmatter(self) -> None:
        """Should not treat metadata dollars as math."""
        text = "---\ntitle: $x$\n---\n$y$"
        assert _mod._math_segments(text) == ["y"]  # noqa: SLF001

    def test_ignores_fenced_code(self) -> None:
        """Should skip code blocks opened by backticks or by tildes."""
        backtick_fenced = "```\n$x$\n```\n$y$"
        tilde_fenced = "~~~python\n$x$\n~~~\n$y$"
        assert _mod._math_segments(backtick_fenced) == ["y"]  # noqa: SLF001
        assert _mod._math_segments(tilde_fenced) == ["y"]  # noqa: SLF001

    def test_ignores_blockquoted_fenced_code(self) -> None:
        """Should skip a code block that is quoted as part of an excerpt."""
        text = "> ```\n> $x$\n> ```\n$y$"
        assert _mod._math_segments(text) == ["y"]  # noqa: SLF001

    def test_ignores_inline_code(self) -> None:
        """Should skip inline code spans, including double-backtick spans."""
        assert _mod._math_segments("`$x$` and $y$") == ["y"]  # noqa: SLF001
        assert _mod._math_segments("``a ` $x$`` and $y$") == ["y"]  # noqa: SLF001

    def test_extracts_inline_and_display_math(self) -> None:
        """Should collect $...$ on one line and $$...$$ across lines."""
        assert _mod._math_segments("$x$ and $$y$$") == ["x", "y"]  # noqa: SLF001
        assert _mod._math_segments("$$\na+b\n$$") == ["\na+b\n"]  # noqa: SLF001

    def test_extracts_parenthesized_and_bracketed_math(self) -> None:
        """Should collect \\(...\\) and \\[...\\], the latter across lines."""
        assert _mod._math_segments(r"\(x\)") == ["x"]  # noqa: SLF001
        assert _mod._math_segments("\\[\nx\n\\]") == ["\nx\n"]  # noqa: SLF001

    def test_ignores_escaped_dollar(self) -> None:
        """Should not open math on an escaped dollar."""
        assert _mod._math_segments(r"costs \$5 and no math") == []  # noqa: SLF001
        assert _mod._math_segments(r"costs \$5 but $x$") == ["x"]  # noqa: SLF001

    def test_ignores_unclosed_math(self) -> None:
        """Should not collect a delimiter that never closes."""
        assert _mod._math_segments("$x and more") == []  # noqa: SLF001


class TestMacroNames:
    """Tests for the _macro_names function."""

    def test_finds_polyfill_macro(self) -> None:
        """Should collect the name of a polyfilled macro."""
        assert _mod._macro_names(r"\Eta(T | a)") == {"Eta"}  # noqa: SLF001

    def test_finds_typo_macro(self) -> None:
        """Should collect the name of a misspelled macro."""
        assert _mod._macro_names(r"{\sqdeert {n} }") == {"sqdeert"}  # noqa: SLF001

    def test_line_break_does_not_create_macro(self) -> None:
        """Should skip both backslashes of a line break instead of reading the next letter."""
        names = _mod._macro_names(r"\begin{matrix} A \\A B \end{matrix}")  # noqa: SLF001
        assert names == {"begin", "end"}

    def test_ignores_non_ascii_letters(self) -> None:
        """Should not read a non-ASCII letter as the start of a macro name."""
        assert _mod._macro_names("\\é") == set()  # noqa: SLF001


class TestCollectFiles:
    """Tests for the _collect_files function."""

    def test_drops_dangling_links_and_duplicates(self, tmp_path: PathLike[str]) -> None:
        """Should audit a linked note once and ignore a link whose target does not exist."""
        root = Path(tmp_path)
        note = root / "note.md"
        note.write_text("$x$", encoding="utf-8")
        (root / "zz alias.md").symlink_to(note)
        (root / "dangling.md").symlink_to(root / "missing.md")
        assert _mod._collect_files([root]) == [note]  # noqa: SLF001


class TestAudit:
    """Tests for the _audit function."""

    def test_counts_distinct_files_and_macros(self, tmp_path: PathLike[str]) -> None:
        """Should map each macro to exactly the files that use it."""
        root = Path(tmp_path)
        first = root / "first.md"
        second = root / "second.md"
        first.write_text(r"$\Eta$ and $\Z$", encoding="utf-8")
        second.write_text(r"$\Z$", encoding="utf-8")
        assert _mod._audit([first, second]) == {  # noqa: SLF001
            "Eta": {first},
            "Z": {first, second},
        }


class TestMain:
    """Tests for the main function."""

    def test_prints_polyfill_and_typo_sections(
        self, tmp_path: PathLike[str], capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should report the polyfill and the typo used by a temporary tree."""
        root = Path(tmp_path)
        (root / "note.md").write_text(r"$\Eta$ and $\sqdeert$", encoding="utf-8")

        _mod.main([fspath(root)])

        output = capsys.readouterr().out
        assert "Audited 1 file(s); found 2 distinct math macros." in output
        assert "Polyfills" in output
        assert r"\Eta: defined as \mathrm{H}; 1 file(s)" in output
        assert "Typo fixes" in output
        assert r"\sqdeert: should be sqrt; 1 file(s)" in output
        assert fspath(root / "note.md") in output

    def test_all_lists_every_macro(
        self, tmp_path: PathLike[str], capsys: pytest.CaptureFixture[str]
    ) -> None:
        """Should list every macro with its file count when --all is given."""
        root = Path(tmp_path)
        (root / "note.md").write_text(r"$\alpha$", encoding="utf-8")

        _mod.main([fspath(root), "--all"])

        output = capsys.readouterr().out
        assert "All macros used in math:" in output
        assert r"\alpha: 1 file(s)" in output
