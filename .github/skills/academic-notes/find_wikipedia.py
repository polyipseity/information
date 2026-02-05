#!/usr/bin/env python3
"""find_wikipedia.py

Search English Wikipedia for a query and suggest safe filenames and a path
suitable for linking under `general/` in the knowledgebase.

This helper is intentionally conservative: it suggests candidate article titles
and filename encodings so maintainers can choose the most suitable canonical
`general/` article. It prints JSON lines by default (one object per suggestion)
or a pretty JSON object with `--pretty`.

Usage:
    python .github/skills/academic-notes/find_wikipedia.py [--limit N] [--pretty] [--human] QUERY

Output (JSON): fields include:
- title: Wikipedia article title
- url: canonical Wikipedia URL
- filename: percent-encoded file name suitable for `general/`
- friendly_filename: percent-encoded name preserving human-friendly separators
- general_path: a suggested relative path to `general/`

Human view (`--human`): a concise, human-readable list with title, url and suggested `general/` path.
"""
from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request

API = "https://en.wikipedia.org/w/api.php"


def _make_request(url: str) -> dict:
    """Perform a simple GET request and parse JSON.

    Raises a propagated exception on network or JSON errors so the caller can
    format a user-friendly message.
    """
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "academic-notes-bot/1.0 (https://github.com)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.load(resp)


def search(term: str, limit: int = 3) -> list[dict[str, str]]:
    """Search Wikipedia for `term` and return up to `limit` search hits.

    Returns a list of dicts with `title` and `snippet` fields (snippet is an
    HTML snippet returned by the API). Network errors raise exceptions.
    """
    params = {
        "action": "query",
        "list": "search",
        "srsearch": term,
        "srlimit": str(limit),
        "format": "json",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    data = _make_request(url)
    results = data.get("query", {}).get("search", [])
    out: list[dict[str, str]] = []
    for item in results:
        out.append({"title": item.get("title", ""), "snippet": item.get("snippet", "")})
    return out


def make_filenames(title: str) -> dict[str, str]:
    """Return percent-encoded filenames for the given title.

    `filename` is a strict percent-encoded file name (no safe characters).
    `friendly_filename` preserves some common punctuation useful for reading in
    UIs while still being safe for file systems and URLs.
    """
    filename = urllib.parse.quote(title, safe="") + ".md"
    # Create a friendly filename that preserves readable characters but encodes
    # spaces as %20 and avoids filesystem-unsafe chars.
    friendly_filename = urllib.parse.quote(title, safe="-_–") + ".md"
    return {"filename": filename, "friendly_filename": friendly_filename}


def _get_extract(title: str) -> str:
    """Fetch the page extract (intro paragraph) for a Wikipedia `title`.

    Returns plain text extract or an empty string on failure.
    """
    params = {
        "action": "query",
        "prop": "extracts",
        "exintro": "",
        "explaintext": "",
        "titles": title,
        "format": "json",
    }
    url = API + "?" + urllib.parse.urlencode(params)
    try:
        data = _make_request(url)
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            return page.get("extract", "") or ""
    except Exception:
        return ""
    return ""


def format_result(title: str) -> dict[str, str]:
    """Format a search hit into the output shape used by the skill.

    The `general_path` is a suggested relative path into `general/` that
    maintainers can use if they decide to add or reference the article locally.
    The `extract` field is the intro paragraph (plain text) that helps
    maintainers quickly assess article relevance.
    """
    url = "https://en.wikipedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_"))
    names = make_filenames(title)
    extract = _get_extract(title)
    short_extract = (extract[:400] + "…") if extract and len(extract) > 400 else extract
    return {
        "title": title,
        "url": url,
        "filename": names["filename"],
        "friendly_filename": names["friendly_filename"],
        "general_path": "../../../../general/" + names["filename"],
        "extract": short_extract,
        "extract_full": extract,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="find_wikipedia.py",
        description="Search English Wikipedia and suggest general/ link targets",
    )
    parser.add_argument("query", nargs="+", help="Search terms")
    parser.add_argument("--limit", type=int, default=3, help="Number of search results to return")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output instead of one-line JSON per result",
    )
    parser.add_argument(
        "--human",
        action="store_true",
        help="Print a concise, human-readable summary for each suggested article",
    )
    args = parser.parse_args(argv)

    term = " ".join(args.query)
    try:
        results = search(term, limit=args.limit)
    except Exception as exc:
        print(json.dumps({"query": term, "error": str(exc)}, ensure_ascii=False))
        return 1

    if not results:
        if args.human:
            print(f"No Wikipedia results found for: {term}")
        else:
            print(json.dumps({"query": term, "results": []}, ensure_ascii=False))
        return 0

    out = [format_result(r["title"]) for r in results]

    if args.human:
        # Human-friendly summary lines with extracts
        for i, o in enumerate(out, start=1):
            print(f"{i}. {o['title']} — {o['url']}")
            if o.get('extract'):
                print(f"   {o['extract']}")
            print(f"   Suggested general/ path: {o['general_path']}")
            print()
    elif args.pretty:
        print(json.dumps({"query": term, "results": out}, ensure_ascii=False, indent=2))
    else:
        for o in out:
            print(json.dumps(o, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
