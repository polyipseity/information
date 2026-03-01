#!/usr/bin/env python3
"""find_wikipedia.py

Search English Wikipedia for a query and suggest safe filenames and a path
suitable for linking under `general/` in the knowledgebase.

The original script was intentionally conservative; this refactor adds
strong typing with :mod:`pydantic` and improves terminal output using
:mod:`rich`.  The overall behaviour is unchanged but the models make it
easier to reason about the data and provide built-in validation.

The CLI now supports a few additional options:

* ``--full`` prints the full extract text when using ``--human``.
* ``--json`` is an alias for the original (default) JSON output mode.

Usage::

    python .github/skills/academic-notes/find_wikipedia.py [--limit N]
        [--pretty] [--human] [--full] QUERY

The JSON structure remains the same: ``title``, ``url``, ``filename``,
``friendly_filename``, ``general_path``, ``extract`` and ``extract_full``.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from typing import TypeVar

from pydantic import BaseModel, Field, HttpUrl, ValidationError
from rich.console import Console
from rich.json import JSON as RichJSON
from rich.table import Table
from rich.traceback import install as install_rich_traceback

__all__ = (
    "search",
    "make_filenames",
    "format_result",
    "main",
)

# enable rich traceback for nicer error output when running interactively
install_rich_traceback()

_API = "https://en.wikipedia.org/w/api.php"

_CONSOLE = Console(markup=False, highlight=False, emoji=False)


class SearchHit(BaseModel):
    """Represents a single hit returned by the Wikipedia search API."""

    title: str
    snippet: str = ""


class FormattedResult(BaseModel):
    """Normalized output format produced by :func:`format_result`.

    ``extract`` is truncated to 400 characters; ``extract_full`` holds the
    complete introductory paragraph when available.
    """

    title: str
    url: HttpUrl
    filename: str
    friendly_filename: str
    general_path: str
    extract: str = ""
    extract_full: str = Field(default="", alias="extract_full")


class WikipediaAPIError(Exception):
    """Raised when an API call to Wikipedia fails or returns invalid data.

    This wraps network errors and validation issues so callers can handle
    them uniformly without importing lower-level exceptions.
    """


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------


ModelType = TypeVar("ModelType", bound=BaseModel)


def _make_request(url: str, model: type[ModelType]) -> ModelType:
    """Fetch JSON from *url* and parse it into an instance of *model*.

    This is the preferred entrypoint for network calls; callers supply a
    pydantic model describing the expected JSON schema and receive a
    validated object back.  Errors are wrapped in
    :class:`WikipediaAPIError` so the CLI can display them cleanly.
    """
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "academic-notes-bot/1.0 (https://github.com)",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            # read response as text so we can pass raw JSON directly to the
            # pydantic helper that avoids an intermediate Python structure
            raw_text = resp.read().decode("utf-8")
    except Exception as exc:  # pragma: no cover - network failures are hard to test
        raise WikipediaAPIError(str(exc))

    try:
        return model.model_validate_json(raw_text)
    except ValidationError as exc:
        raise WikipediaAPIError(f"unexpected response format: {exc}")


# ---------------------------------------------------------------------------
# Core functionality
# ---------------------------------------------------------------------------


# response models used by search()/extract helpers


class SearchQuery(BaseModel):
    """Pydantic model for the ``query`` field returned by the search API.

    The ``search`` attribute holds a list of :class:`SearchHit` objects.
    """

    search: list[SearchHit] = []


class SearchResponse(BaseModel):
    """Top‑level response model for the Wikipedia search API.

    The JSON returned by ``action=query&list=search`` nests the results under
    a ``query`` key which is represented by :class:`SearchQuery`.
    """

    query: SearchQuery


def search(term: str, limit: int = 3) -> list[SearchHit]:
    """Return up to *limit* search hits for *term* from Wikipedia.

    The API returns HTML snippets which we leave untouched; callers may
    render them with an HTML-aware tool if desired.  Parsing is handled by
    :class:`SearchResponse`, so this function simply forwards the resulting
    list.
    """
    params = {
        "action": "query",
        "list": "search",
        "srsearch": term,
        "srlimit": str(limit),
        "format": "json",
    }
    url = _API + "?" + urllib.parse.urlencode(params)
    resp = _make_request(url, SearchResponse)
    return resp.query.search


def make_filenames(title: str) -> dict[str, str]:
    """Return percent-encoded filenames derived from *title*.

    ``filename`` is fully percent-encoded, whereas ``friendly_filename``
    preserves ``-``/``_``/``–`` to improve readability in UIs.
    """
    filename = urllib.parse.quote(title, safe="") + ".md"
    friendly_filename = urllib.parse.quote(title, safe="-_–") + ".md"
    return {"filename": filename, "friendly_filename": friendly_filename}


# models for the extract API


class PageExtract(BaseModel):
    """Model used when requesting plaintext extracts for a specific page.

    The ``extract`` field contains the introductory paragraph of the page.
    """

    extract: str = ""


class ExtractQuery(BaseModel):
    """Wrapper for the ``pages`` dictionary returned by the extracts API.

    Each key is a page ID and the value is a :class:`PageExtract` instance.
    """

    pages: dict[str, PageExtract] = {}


class ExtractResponse(BaseModel):
    """Top-level response model for the Wikipedia extracts API.

    The API nests the page data under a ``query`` key containing an
    :class:`ExtractQuery` object.
    """

    query: ExtractQuery


def _get_extract(title: str) -> str:
    """Retrieve the plaintext intro paragraph for *title*.

    Returns an empty string on failure; callers may ignore this.
    """
    params = {
        "action": "query",
        "prop": "extracts",
        "exintro": "",
        "explaintext": "",
        "titles": title,
        "format": "json",
    }
    url = _API + "?" + urllib.parse.urlencode(params)
    try:
        resp = _make_request(url, ExtractResponse)
        # pages is a dict keyed by pageid; grab first extract available
        for page in resp.query.pages.values():
            return page.extract or ""
    except WikipediaAPIError:
        return ""
    return ""


def format_result(title: str) -> FormattedResult:
    """Return a validated :class:`FormattedResult` for *title*.

    The URL is canonicalised by replacing spaces with underscores.
    """
    string_url = "https://en.wikipedia.org/wiki/" + urllib.parse.quote(
        title.replace(" ", "_")
    )
    # convert to HttpUrl for static type checkers
    wiki_url: HttpUrl = HttpUrl(string_url)
    names = make_filenames(title)
    extract_full = _get_extract(title)
    extract = (
        (extract_full[:400] + "…")
        if extract_full and len(extract_full) > 400
        else extract_full
    )
    general_path = "../../../../general/" + names["filename"]
    # directly construct the model; HttpUrl instance satisfies type
    return FormattedResult(
        title=title,
        url=wiki_url,
        filename=names["filename"],
        friendly_filename=names["friendly_filename"],
        general_path=general_path,
        extract=extract,
        extract_full=extract_full,
    )


# ---------------------------------------------------------------------------
# CLI / output
# ---------------------------------------------------------------------------


def _print_human(results: list[FormattedResult], show_full: bool) -> None:
    """Display *results* in a human-readable fashion using ``rich``.

    *show_full* controls whether the full extract text is printed.
    """
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=3)
    table.add_column("Title")
    table.add_column("URL")
    table.add_column("Extract", overflow="fold")
    table.add_column("General path")

    for idx, res in enumerate(results, start=1):
        extract_text = res.extract_full if show_full else res.extract
        # rich requires renderable objects; convert HttpUrl to str
        table.add_row(
            str(idx),
            res.title,
            str(res.url),
            extract_text or "—",
            res.general_path,
        )
    _CONSOLE.print(table)


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint for the script.

    Parses command-line arguments, performs a Wikipedia search, and
    prints results either as JSON or in a human-readable table.  Returns an
    integer exit code (0 for success, nonzero on error).

    The *argv* parameter facilitates testing by allowing callers to
    supply a custom argument list; it behaves like :func:`sys.argv[1:]`
    when ``None`` is passed.
    """
    parser = argparse.ArgumentParser(
        prog="find_wikipedia.py",
        description="Search English Wikipedia and suggest general/ link targets",
    )
    parser.add_argument("query", nargs="+", help="Search terms")
    parser.add_argument(
        "--limit", type=int, default=3, help="Number of search results to return"
    )
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output (implies --json)",
    )
    output_group.add_argument(
        "--human", action="store_true", help="Print human-readable table"
    )
    parser.add_argument(
        "--full",
        action="store_true",
        help="Show full extract text when used with --human",
    )
    parser.add_argument(
        "--json", action="store_true", help="Force JSON output (default)"
    )

    args = parser.parse_args(argv)
    term = " ".join(args.query)

    try:
        hits = search(term, limit=args.limit)
    except WikipediaAPIError as exc:
        _CONSOLE.print(f"[red]error:[/] {exc}", markup=True)
        return 1

    if not hits:
        if args.human:
            _CONSOLE.print(
                f"No Wikipedia results found for: [bold]{term}[/]", markup=True
            )
        else:
            _CONSOLE.print(
                json.dumps({"query": term, "results": []}, ensure_ascii=False),
                highlight=True,
            )
        return 0

    formatted = [format_result(h.title) for h in hits]

    if args.human:
        _print_human(formatted, show_full=args.full)
    else:
        # serialize results; make sure HttpUrl fields become strings
        results_list = [r.model_dump(by_alias=True) for r in formatted]
        for item in results_list:
            if "url" in item:
                item["url"] = str(item["url"])
        payload = {"query": term, "results": results_list}
        if args.pretty:
            _CONSOLE.print(RichJSON.from_data(payload), highlight=True)
        else:
            # plain JSON lines (use regular print to avoid automatic wrapping)
            for r in payload["results"]:
                print(json.dumps(r, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
