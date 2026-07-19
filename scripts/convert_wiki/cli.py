"""Command-line interface for the Wikipedia HTML-to-Markdown converter.

Provides ``main`` (argparse-driven entry) and ``__main__`` (wrapped with
asyncer.runnify for async dispatch).
"""

import argparse
from logging import INFO, basicConfig
from os import fspath
from sys import stderr, stdin

import anyio
from anyio import Path
from asyncer import runnify
from bs4 import BeautifulSoup
from jaraco.clipboard import paste_html
from pyarchivist import ArchiveResult, Args
from pyarchivist.Wikimedia_Commons import archive as pyarchivist_archive
from pyperclip import copy as clip_copy

from . import config as _cfg
from .pipeline import run_pipeline

"""Exported names from this module."""
__all__ = ()


async def main() -> None:
    """Parse CLI arguments and orchestrate the HTML-to-Markdown conversion pipeline."""
    parser = argparse.ArgumentParser(
        description="Convert Wikipedia HTML to Markdown. Reads from stdin by default."
    )
    parser.add_argument(
        "--no-refs",
        action="store_true",
        help="Omit reference citations.",
    )
    parser.add_argument(
        "--output-mode",
        "-m",
        choices=["clipboard", "stdout", "stderr", "append"],
        default="clipboard",
        help="Output mode (default: clipboard).",
    )
    parser.add_argument(
        "--output-file",
        "-f",
        type=Path,
        help="File path for append output mode.",
    )
    parser.add_argument(
        "--input-file",
        "-i",
        type=Path,
        default="-",
        help="Read HTML from file instead of stdin (default: stdin).",
    )
    parser.add_argument(
        "--clipboard",
        "-c",
        action="store_true",
        help="Read HTML from system clipboard (overrides --input-file).",
    )
    args = parser.parse_args()
    refs = not args.no_refs

    if args.output_mode == "append" and args.output_file is None:
        parser.error("--output-file is required when --output-mode is append.")

    basicConfig(level=INFO)
    _cfg._logger.info("Starting Wikipedia HTML to Markdown conversion")

    if args.clipboard:
        html_text = paste_html()
        if not isinstance(html_text, str):
            msg = (
                f"Clipboard does not contain HTML text (got {type(html_text).__name__})"
            )
            raise TypeError(msg)
    else:
        source = stdin if fspath(args.input_file) == "-" else open(args.input_file)
        with source:
            html_text = source.read()

    html = BeautifulSoup(html_text, "html.parser")

    output, out_to_archive = await run_pipeline(html, refs=refs)

    if out_to_archive:
        _cfg._logger.info("Archiving %d media files", len(out_to_archive))
        downloaded_so_far = 0

        def _on_progress(current: int, total: int) -> None:
            """Report conversion progress for status output."""
            nonlocal downloaded_so_far
            if current - downloaded_so_far >= 5:
                _cfg._logger.info("Archiving progress: %d/%d", current, total)
                downloaded_so_far = current

        result: ArchiveResult = await pyarchivist_archive(
            Args(
                inputs=tuple(out_to_archive),
                dest=anyio.Path("../archives/Wikimedia Commons/"),
                index=anyio.Path("../archives/Wikimedia Commons/index.md"),
                ignore_individual_errors=True,
                skip_existing=True,
                request_timeout=30.0,
                progress_callback=_on_progress,
            )
        )
        if result.errors:
            for err in result.errors:
                _cfg._logger.warning(
                    "Archive error [%s] %s: %s",
                    err.phase,
                    err.title,
                    err.message,
                )
        _cfg._logger.info(
            "Archiving done: %d downloaded, %d skipped",
            result.downloaded,
            result.skipped,
        )

    match args.output_mode:
        case "clipboard":
            print(output)
            clip_copy(output)
            print(":)")
        case "stdout":
            print(output)
        case "stderr":
            print(output, file=stderr)
        case "append":
            with open(args.output_file, "a") as f:
                f.write(output)
                f.write("\n")


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()
