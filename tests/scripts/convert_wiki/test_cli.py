"""Tests for ``scripts.convert_wiki.cli``.

Covers argument parsing, the ``main`` entry point in various modes, and
error handling.
"""

from __future__ import annotations

import argparse
from os import PathLike
from pathlib import Path
from sys import stderr
from unittest.mock import AsyncMock, patch

import pytest
from anyio import Path as AnyioPath

from scripts.convert_wiki.cli import main
from scripts.convert_wiki.reconcile import _ReconcileReport
from scripts.convert_wiki.types import _ReprocessReport

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def minimal_html() -> str:
    """Return a minimal Wikipedia-style HTML snippet."""
    return "<html><body><p>Hello world</p></body></html>"


@pytest.fixture
def expected_markdown() -> str:
    """Expected Markdown output from converting *minimal_html*."""
    return "Hello world"


@pytest.fixture
def parser() -> argparse.ArgumentParser:
    """Recreate the argument parser used by ``main``."""
    p = argparse.ArgumentParser(
        description="Convert Wikipedia HTML to Markdown. Reads from stdin by default."
    )  # noqa: E501
    p.add_argument("--no-refs", action="store_true", help="Omit reference citations.")
    p.add_argument(
        "--output-mode",
        "-m",
        choices=["clipboard", "stdout", "stderr", "append"],
        default="clipboard",
        help="Output mode (default: clipboard).",
    )
    p.add_argument(
        "--output-file", "-f", type=Path, help="File path for append output mode."
    )
    p.add_argument(
        "--input-file",
        "-i",
        type=Path,
        default="-",
        help="Read HTML from file instead of stdin (default: stdin).",
    )  # noqa: E501
    p.add_argument(
        "--clipboard",
        "-c",
        action="store_true",
        help="Read HTML from system clipboard (overrides --input-file).",
    )  # noqa: E501
    p.add_argument(
        "--update-redirects",
        action="store_true",
        help="Reconcile redirect symlinks against the live API instead of converting HTML.",
    )  # noqa: E501
    p.add_argument(
        "--reprocess",
        action="store_true",
        help="Reprocess articles and name_map entries without converting HTML.",
    )
    p.add_argument(
        "--mapping",
        nargs=2,
        action="append",
        metavar=("TITLE", "STEM"),
        help="Name map entry for --reprocess (repeatable TITLE STEM pair).",
    )
    p.add_argument(
        "--mapping-file",
        type=Path,
        help="JSONC name map for --reprocess (mutually exclusive with --mapping).",
    )
    p.add_argument(
        "--article",
        action="append",
        default=[],
        metavar="ARTICLE",
        help="Article stem or path to reprocess (repeatable).",
    )
    p.add_argument(
        "--update-links",
        action="store_true",
        help="With --reprocess, rewrite link targets corpus-wide.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="With --update-redirects or --reprocess, report actions without changing anything.",
    )  # noqa: E501
    return p


# ---------------------------------------------------------------------------
# Argument parsing tests
# ---------------------------------------------------------------------------


class TestArgumentParsing:
    """Verify argparse correctly parses CLI arguments."""

    def test_defaults(self, parser: argparse.ArgumentParser) -> None:
        """Default arguments should set output-mode to clipboard."""
        args = parser.parse_args([])
        assert args.output_mode == "clipboard"
        assert args.no_refs is False
        assert args.clipboard is False
        assert args.output_file is None
        assert args.input_file == Path("-")

    def test_no_refs(self, parser: argparse.ArgumentParser) -> None:
        """--no-refs flag should be parsed correctly."""
        args = parser.parse_args(["--no-refs"])
        assert args.no_refs is True

    def test_output_mode_stdout(self, parser: argparse.ArgumentParser) -> None:
        """-m stdout should be recognised."""
        args = parser.parse_args(["-m", "stdout"])
        assert args.output_mode == "stdout"

    def test_output_mode_stderr(self, parser: argparse.ArgumentParser) -> None:
        """--output-mode stderr should be recognised."""
        args = parser.parse_args(["--output-mode", "stderr"])
        assert args.output_mode == "stderr"

    def test_output_mode_append_with_file(
        self, parser: argparse.ArgumentParser
    ) -> None:
        """Append mode with a valid output file."""
        args = parser.parse_args(["-m", "append", "-f", "/tmp/out.md"])
        assert args.output_mode == "append"
        assert args.output_file == Path("/tmp/out.md")

    def test_invalid_output_mode(self, parser: argparse.ArgumentParser) -> None:
        """An invalid output mode should be rejected."""
        with pytest.raises(SystemExit):
            parser.parse_args(["-m", "invalid"])

    def test_input_file(self, parser: argparse.ArgumentParser) -> None:
        """--input-file should override the default stdin."""
        args = parser.parse_args(["-i", "/path/to/input.html"])
        assert args.input_file == Path("/path/to/input.html")

    def test_clipboard_flag(self, parser: argparse.ArgumentParser) -> None:
        """--clipboard flag should be parsed."""
        args = parser.parse_args(["-c"])
        assert args.clipboard is True

    def test_short_output_file(self, parser: argparse.ArgumentParser) -> None:
        """-f with short form should work."""
        args = parser.parse_args(["-f", "output.md"])
        assert args.output_file == Path("output.md")

    def test_update_redirects_flag(self, parser: argparse.ArgumentParser) -> None:
        """--update-redirects flag should be parsed."""
        args = parser.parse_args(["--update-redirects"])
        assert args.update_redirects is True

    def test_dry_run_flag(self, parser: argparse.ArgumentParser) -> None:
        """--dry-run flag should be parsed."""
        args = parser.parse_args(["--dry-run"])
        assert args.dry_run is True


# ---------------------------------------------------------------------------
# Main() entry point tests
# ---------------------------------------------------------------------------


class TestMainStdout:
    """Test ``main()`` with ``--output-mode stdout`` (no side effects)."""

    @pytest.mark.anyio
    @patch("scripts.convert_wiki.cli.stdin", autospec=True)
    async def test_stdout_output(
        self,
        mock_stdin: AsyncMock,
        minimal_html: str,
        expected_markdown: str,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should print converted Markdown to stdout."""
        mock_stdin.read.return_value = minimal_html
        monkeypatch.setattr(
            "sys.argv",
            ["convert_wiki", "-m", "stdout"],
        )

        with (
            patch("scripts.convert_wiki.cli.print") as mock_print,
            patch("scripts.convert_wiki.pipeline.run_pipeline") as mock_run,
        ):
            mock_run.return_value = (expected_markdown, set())
            await main()

        mock_print.assert_called_once_with(expected_markdown)

    @pytest.mark.anyio
    @patch("scripts.convert_wiki.cli.stdin", autospec=True)
    async def test_stdout_with_no_refs(
        self,
        mock_stdin: AsyncMock,
        minimal_html: str,
        expected_markdown: str,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """--no-refs should be passed through to the pipeline."""
        mock_stdin.read.return_value = minimal_html
        monkeypatch.setattr("sys.argv", ["convert_wiki", "-m", "stdout", "--no-refs"])

        with patch("scripts.convert_wiki.pipeline.run_pipeline") as mock_run:
            mock_run.return_value = (expected_markdown, set())
            await main()

        mock_run.assert_called_once()
        _args, kwargs = mock_run.call_args
        assert kwargs.get("refs") is False


class TestMainStderr:
    """Test ``main()`` with ``--output-mode stderr``."""

    @pytest.mark.anyio
    @patch("scripts.convert_wiki.cli.stdin", autospec=True)
    async def test_stderr_output(
        self,
        mock_stdin: AsyncMock,
        minimal_html: str,
        expected_markdown: str,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should print converted Markdown to stderr."""
        mock_stdin.read.return_value = minimal_html
        monkeypatch.setattr("sys.argv", ["convert_wiki", "-m", "stderr"])

        with (
            patch("scripts.convert_wiki.cli.print") as mock_print,
            patch("scripts.convert_wiki.pipeline.run_pipeline") as mock_run,
        ):
            mock_run.return_value = (expected_markdown, set())
            await main()

        mock_print.assert_called_once_with(expected_markdown, file=stderr)


class TestMainAppend:
    """Test ``main()`` with ``--output-mode append``."""

    @pytest.mark.anyio
    async def test_append_to_file(
        self,
        minimal_html: str,
        expected_markdown: str,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should append converted Markdown to the specified file."""
        out_file = AnyioPath(tmp_path) / "output.md"
        monkeypatch.setattr(
            "sys.argv",
            ["convert_wiki", "-m", "append", "-f", str(out_file)],
        )

        with (
            patch("scripts.convert_wiki.cli.stdin") as mock_stdin,
            patch("scripts.convert_wiki.pipeline.run_pipeline") as mock_run,
        ):
            mock_stdin.read.return_value = minimal_html
            mock_run.return_value = (expected_markdown, set())
            await main()

        content = await out_file.read_text()
        assert expected_markdown in content

    @pytest.mark.anyio
    async def test_append_without_file_raises_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Append mode without --output-file should raise SystemExit."""
        monkeypatch.setattr("sys.argv", ["convert_wiki", "-m", "append"])

        with pytest.raises(SystemExit):
            await main()


class TestMainInput:
    """Test ``main()`` with different input sources."""

    @pytest.mark.anyio
    async def test_input_file(
        self,
        expected_markdown: str,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should read HTML from a file specified via --input-file."""
        html_file = AnyioPath(tmp_path) / "input.html"
        await html_file.write_text("<html><body><p>File input</p></body></html>")
        monkeypatch.setattr(
            "sys.argv",
            ["convert_wiki", "-m", "stdout", "-i", str(html_file)],
        )

        with patch("scripts.convert_wiki.pipeline.run_pipeline") as mock_run:
            mock_run.return_value = (expected_markdown, set())
            await main()

        # Verify the pipeline received the converted HTML
        mock_run.assert_called_once()

    @pytest.mark.anyio
    async def test_clipboard_input(
        self,
        expected_markdown: str,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Should read HTML from clipboard when --clipboard is set."""
        monkeypatch.setattr("sys.argv", ["convert_wiki", "-m", "stdout", "-c"])

        with (
            patch("scripts.convert_wiki.cli.paste_html") as mock_paste,
            patch("scripts.convert_wiki.pipeline.run_pipeline") as mock_run,
        ):
            mock_paste.return_value = "<html><body><p>Clipboard</p></body></html>"
            mock_run.return_value = (expected_markdown, set())
            await main()

        mock_paste.assert_called_once()
        mock_run.assert_called_once()


class TestMainError:
    """Test error handling in ``main()``."""

    @pytest.mark.anyio
    async def test_clipboard_non_text_raises_type_error(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Non-text clipboard content should raise TypeError."""
        monkeypatch.setattr("sys.argv", ["convert_wiki", "-m", "stdout", "-c"])

        with patch("scripts.convert_wiki.cli.paste_html") as mock_paste:
            mock_paste.return_value = None  # Not a string

            with pytest.raises(TypeError, match="Clipboard does not contain HTML text"):
                await main()


class TestMainUpdateRedirects:
    """Test ``main()`` with ``--update-redirects`` (maintenance mode)."""

    @pytest.mark.anyio
    async def test_update_redirects_runs_reconcile_and_skips_html(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """--update-redirects should run reconciliation and skip HTML input."""
        report = _ReconcileReport(
            scanned=2, retargeted=1, removed=0, kept=1, changed=("A",)
        )
        monkeypatch.setattr(
            "sys.argv", ["convert_wiki", "--update-redirects", "-m", "stdout"]
        )

        with (
            patch("scripts.convert_wiki.cli.stdin") as mock_stdin,
            patch(
                "scripts.convert_wiki.cli.reconcile_redirect_symlinks"
            ) as mock_reconcile,
            patch("scripts.convert_wiki.pipeline.run_pipeline") as mock_run,
            patch("scripts.convert_wiki.cli.print") as mock_print,
        ):
            mock_reconcile.return_value = report
            await main()

        mock_reconcile.assert_called_once()
        _args, kwargs = mock_reconcile.call_args
        assert kwargs.get("dry_run") is False
        mock_stdin.read.assert_not_called()
        mock_run.assert_not_called()
        mock_print.assert_any_call(
            "Redirect reconciliation: scanned=2, retargeted=1, removed=0, kept=1"
        )
        mock_print.assert_any_call("Changed: A")

    @pytest.mark.anyio
    async def test_update_redirects_dry_run_passthrough(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """--dry-run should be forwarded to the reconciliation engine."""
        report = _ReconcileReport(
            scanned=0, retargeted=0, removed=0, kept=0, changed=()
        )
        monkeypatch.setattr(
            "sys.argv", ["convert_wiki", "--update-redirects", "--dry-run"]
        )

        with patch(
            "scripts.convert_wiki.cli.reconcile_redirect_symlinks"
        ) as mock_reconcile:
            mock_reconcile.return_value = report
            await main()

        mock_reconcile.assert_called_once()
        _args, kwargs = mock_reconcile.call_args
        assert kwargs.get("dry_run") is True

    @pytest.mark.anyio
    async def test_dry_run_alone_is_inert(
        self,
        minimal_html: str,
        expected_markdown: str,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """--dry-run without --update-redirects should convert normally."""
        monkeypatch.setattr("sys.argv", ["convert_wiki", "--dry-run", "-m", "stdout"])

        with (
            patch("scripts.convert_wiki.cli.stdin") as mock_stdin,
            patch(
                "scripts.convert_wiki.cli.reconcile_redirect_symlinks"
            ) as mock_reconcile,
            patch("scripts.convert_wiki.pipeline.run_pipeline") as mock_run,
        ):
            mock_stdin.read.return_value = minimal_html
            mock_run.return_value = (expected_markdown, set())
            await main()

        mock_reconcile.assert_not_called()
        mock_run.assert_called_once()


class TestMainReprocess:
    """Test ``main()`` with ``--reprocess`` (maintenance mode)."""

    @pytest.mark.anyio
    async def test_reprocess_runs_and_skips_html(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """--reprocess should run reprocess_articles and skip HTML input."""
        report = _ReprocessReport(
            mappings_added=1,
            symlinks_created=0,
            symlinks_removed=0,
            symlinks_retargeted=0,
            files_renamed=0,
            articles_rewritten=0,
            links_updated_corpus=0,
            dry_run=False,
            changed=("Modern physics",),
        )
        monkeypatch.setattr(
            "sys.argv",
            [
                "convert_wiki",
                "--reprocess",
                "--mapping",
                "Modern physics",
                "Modern physics",
            ],
        )

        with (
            patch("scripts.convert_wiki.cli.stdin") as mock_stdin,
            patch("scripts.convert_wiki.cli.reprocess_articles") as mock_reprocess,
            patch("scripts.convert_wiki.pipeline.run_pipeline") as mock_run,
            patch("scripts.convert_wiki.cli.print") as mock_print,
        ):
            mock_reprocess.return_value = report
            await main()

        mock_reprocess.assert_called_once()
        mock_stdin.read.assert_not_called()
        mock_run.assert_not_called()
        mock_print.assert_any_call(
            "Reprocess: mappings_added=1, symlinks_created=0, symlinks_removed=0, "
            "symlinks_retargeted=0, files_renamed=0, articles_rewritten=0, "
            "links_updated_corpus=0, dry_run=False"
        )
        mock_print.assert_any_call("Changed: Modern physics")

    @pytest.mark.anyio
    async def test_reprocess_dry_run_passthrough(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """--dry-run should be forwarded to the reprocess request."""
        report = _ReprocessReport(
            mappings_added=0,
            symlinks_created=0,
            symlinks_removed=0,
            symlinks_retargeted=0,
            files_renamed=0,
            articles_rewritten=0,
            links_updated_corpus=0,
            dry_run=True,
            changed=(),
        )
        monkeypatch.setattr(
            "sys.argv",
            [
                "convert_wiki",
                "--reprocess",
                "--mapping",
                "Modern physics",
                "Modern physics",
                "--dry-run",
            ],
        )

        with patch("scripts.convert_wiki.cli.reprocess_articles") as mock_reprocess:
            mock_reprocess.return_value = report
            await main()

        request = mock_reprocess.call_args.args[0]
        assert request.dry_run is True

    @pytest.mark.anyio
    async def test_reprocess_rejects_mapping_and_mapping_file(
        self,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """--mapping and --mapping-file cannot be used together."""
        monkeypatch.setattr(
            "sys.argv",
            [
                "convert_wiki",
                "--reprocess",
                "--mapping",
                "Modern physics",
                "Modern physics",
                "--mapping-file",
                "fixes.jsonc",
            ],
        )

        with pytest.raises(SystemExit):
            await main()
