"""Command-line interface for the Wikipedia HTML-to-Markdown converter.

Provides ``main`` (argparse-driven entry) and ``__main__`` (wrapped with
asyncer.runnify for async dispatch).
"""

import argparse
from logging import INFO, basicConfig
from os import fspath
from sys import stderr, stdin

import anyio
import json5
from aiohttp import ClientSession, TCPConnector
from anyio import Path
from asyncer import runnify
from bs4 import BeautifulSoup
from jaraco.clipboard import paste_html
from pyarchivist import ArchiveResult, Args
from pyarchivist.Wikimedia_Commons import archive as pyarchivist_archive
from pyperclip import copy as clip_copy

from . import config as _cfg
from .name_map_io import _pairs_to_map
from .pipeline import run_pipeline
from .reconcile import reconcile_redirect_symlinks
from .reprocess import reprocess_articles
from .types import _ReprocessRequest


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
    parser.add_argument(
        "--update-redirects",
        action="store_true",
        help="Reconcile redirect symlinks against the live API instead of converting HTML.",
    )
    parser.add_argument(
        "--reprocess",
        action="store_true",
        help="Reprocess articles and name_map entries without converting HTML.",
    )
    parser.add_argument(
        "--mapping",
        nargs=2,
        action="append",
        metavar=("TITLE", "STEM"),
        help="Name map entry for --reprocess (repeatable TITLE STEM pair).",
    )
    parser.add_argument(
        "--mapping-file",
        type=Path,
        help="JSONC name map for --reprocess (mutually exclusive with --mapping).",
    )
    parser.add_argument(
        "--article",
        action="append",
        default=[],
        metavar="ARTICLE",
        help="Article stem or path to reprocess (repeatable).",
    )
    parser.add_argument(
        "--update-links",
        action="store_true",
        help="With --reprocess, rewrite link targets corpus-wide.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="With --update-redirects or --reprocess, report actions without changing anything.",
    )
    args = parser.parse_args()
    refs = not args.no_refs

    if args.reprocess and args.update_redirects:
        parser.error("--reprocess cannot be combined with --update-redirects.")

    if args.reprocess:
        if args.mapping and args.mapping_file is not None:
            parser.error("--mapping and --mapping-file are mutually exclusive.")
        await _run_reprocess_maintenance(
            mapping_pairs=tuple(tuple(pair) for pair in args.mapping or ()),
            mapping_file=args.mapping_file,
            articles=tuple(args.article),
            update_links=args.update_links,
            dry_run=args.dry_run,
        )
        return

    if args.update_redirects:
        await _run_redirect_maintenance(dry_run=args.dry_run)
        return

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
                dest=anyio.Path(_cfg._ARCHIVES_COMMONS_DIRECTORY),
                index=anyio.Path(_cfg._ARCHIVES_COMMONS_INDEX),
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


"""Exported names from this module."""
__all__ = ()


def _load_mapping_file(path: Path) -> dict[str, str]:
    """Load a JSONC mapping file from *path*."""
    with open(path, "rt", encoding="UTF-8") as handle:
        loaded = json5.load(handle)
    if not isinstance(loaded, dict):
        msg = f"--mapping-file must contain a JSON object: {path}"
        raise TypeError(msg)
    return {str(key): str(value) for key, value in loaded.items()}


async def _run_reprocess_maintenance(
    *,
    mapping_pairs: tuple[tuple[str, str], ...],
    mapping_file: Path | None,
    articles: tuple[str, ...],
    update_links: bool,
    dry_run: bool,
) -> None:
    """Run name_map reprocess maintenance without converting HTML."""
    if mapping_pairs and mapping_file is not None:
        msg = "--mapping and --mapping-file are mutually exclusive"
        raise ValueError(msg)
    if mapping_file is not None:
        mappings = _load_mapping_file(mapping_file)
    elif mapping_pairs:
        mappings = _pairs_to_map(mapping_pairs)
    else:
        mappings = {}
    if not mappings and not articles:
        msg = "at least one of --mapping, --mapping-file, or --article is required"
        raise ValueError(msg)
    report = await reprocess_articles(
        _ReprocessRequest(
            mappings=mappings,
            articles=articles,
            update_links=update_links,
            dry_run=dry_run,
        )
    )
    print(
        "Reprocess: "
        f"mappings_added={report.mappings_added}, "
        f"symlinks_created={report.symlinks_created}, "
        f"symlinks_removed={report.symlinks_removed}, "
        f"symlinks_retargeted={report.symlinks_retargeted}, "
        f"files_renamed={report.files_renamed}, "
        f"articles_rewritten={report.articles_rewritten}, "
        f"links_updated_corpus={report.links_updated_corpus}, "
        f"dry_run={report.dry_run}"
    )
    if report.changed:
        print(f"Changed: {', '.join(report.changed)}")


async def _run_redirect_maintenance(*, dry_run: bool) -> None:
    """Reconcile redirect symlinks without reading HTML input or writing output."""
    async with ClientSession(
        connector=TCPConnector(limit_per_host=_cfg._MAX_CONCURRENT_REQUESTS_PER_HOST),
        headers={
            "Accept-Encoding": "gzip",
            "User-Agent": _cfg.USER_AGENT,
        },
    ) as session:
        report = await reconcile_redirect_symlinks(session, dry_run=dry_run)
    print(
        f"Redirect reconciliation: scanned={report.scanned}, "
        f"retargeted={report.retargeted}, removed={report.removed}, "
        f"kept={report.kept}"
    )
    if report.changed:
        print(f"Changed: {', '.join(report.changed)}")


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()
