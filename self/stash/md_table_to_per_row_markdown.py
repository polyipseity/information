#!/usr/bin/env python3
"""parse_markdown_table.py — parse a Markdown table into row objects and a compact per-row
markdown format.

Usage examples:
  # Try clipboard (if pyperclip installed) else read stdin
  python parse_markdown_table.py --clipboard --copy

  # Read from a file and print output
  python parse_markdown_table.py -i table.md

  # Read from stdin and copy to clipboard if possible
  cat table.md | python parse_markdown_table.py --copy
"""

from __future__ import annotations

import argparse
import json
import re
import sys

import pyperclip

SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")


def process_markdown_table(md_table: str) -> tuple[list[dict[str, str]], list[str]]:
    """Parse a markdown table string into a list of row dicts and formatted markdown lines.

    Returns (rows, markdown_lines).
    """
    # `md_table` is statically typed as `str`; no runtime isinstance() check required.

    lines = [line.strip() for line in md_table.splitlines()]
    lines = [line for line in lines if line]
    if len(lines) < 2:
        return [], []

    def split_row(line: str) -> list[str]:
        trimmed = line
        if trimmed.startswith("|"):
            trimmed = trimmed[1:]
        if trimmed.endswith("|"):
            trimmed = trimmed[:-1]
        return [c.strip() for c in trimmed.split("|")]

    header_cells = split_row(lines[0])
    data_start_idx = 1
    if len(lines) >= 2:
        possible_sep = split_row(lines[1])
        is_separator = len(possible_sep) == len(header_cells) and all(
            SEPARATOR_CELL_RE.match(cell) for cell in possible_sep
        )
        if is_separator:
            data_start_idx = 2

    rows: list[dict[str, str]] = []
    for i in range(data_start_idx, len(lines)):
        cells = split_row(lines[i])
        normalized: list[str] = [
            ((cells[idx] if idx < len(cells) else "") or "").strip()
            for idx in range(len(header_cells))
        ]
        obj: dict[str, str] = {
            header_cells[idx].strip(): normalized[idx]
            for idx in range(len(header_cells))
        }
        rows.append(obj)

    headers = [h.strip() for h in header_cells]

    markdown_lines: list[str] = []
    for row in rows:
        if not headers:
            markdown_lines.append("")
            continue
        first_header = headers[0]
        first_value = (row.get(first_header, "") or "").strip()
        lines_for_row: list[str] = [f"- {first_value}"]
        for header in headers[1:]:
            value = (row.get(header, "") or "").strip()
            lines_for_row.append(f"  -  {first_value} / {header} ::@:: {value}")
        markdown_lines.append("\n".join(lines_for_row))

    return rows, markdown_lines


def read_clipboard_with_fallback() -> str:
    try:
        return pyperclip.paste() or ""
    except Exception:
        # Fallback: read from stdin if piped, else prompt user to paste and finish with EOF
        if not sys.stdin.isatty():
            return sys.stdin.read()
        print(
            "Paste your Markdown table, then end input with Ctrl-D (Ctrl-Z on Windows):"
        )
        return sys.stdin.read()


def write_clipboard_with_fallback(text: str) -> bool:
    try:
        pyperclip.copy(text)
        return True
    except Exception:
        # Fallback: print output and return False
        print("\n--- Output (copy manually) ---\n")
        print(text)
        print("\n--- End output ---\n")
        return False


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Parse Markdown tables and produce per-row formatted output."
    )
    p.add_argument(
        "-i",
        "--input-file",
        help="Read Markdown table from file instead of clipboard/stdin",
    )
    p.add_argument(
        "--clipboard",
        action="store_true",
        help="Prefer reading input from the clipboard (if available)",
    )
    p.add_argument(
        "--copy",
        action="store_true",
        help="Copy the formatted output back to the clipboard (if available)",
    )
    p.add_argument(
        "-j",
        "--json",
        action="store_true",
        help="Print parsed rows as JSON after formatted output",
    )
    p.add_argument("-o", "--output-file", help="Write the formatted output to a file")

    args = p.parse_args(argv)

    if args.input_file:
        try:
            with open(args.input_file, "r", encoding="utf-8") as fh:
                input_text = fh.read()
        except Exception as e:
            print("Error reading input file:", e, file=sys.stderr)
            return 2
    else:
        if args.clipboard:
            input_text = read_clipboard_with_fallback()
        else:
            # If stdin is piped and clipboard not explicitly requested, read stdin; otherwise use clipboard.
            if not sys.stdin.isatty():
                input_text = sys.stdin.read()
            else:
                input_text = read_clipboard_with_fallback()

    if not input_text or "|" not in input_text:
        print("No Markdown table-like content detected in input.", file=sys.stderr)
        return 3

    rows, markdown_lines = process_markdown_table(input_text)
    output = "\n\n".join(markdown_lines)

    if args.output_file:
        try:
            with open(args.output_file, "w", encoding="utf-8") as fh:
                fh.write(output)
        except Exception as e:
            print("Error writing output file:", e, file=sys.stderr)
            return 4

    if args.copy:
        copied = write_clipboard_with_fallback(output)
        if copied:
            print("✅ Output copied to clipboard.")
        else:
            print("⚠️ Could not write to clipboard; output printed to stdout.")

    # Print combined result to stdout (so the tool can be used in pipes)
    print(output)

    if args.json:
        print("\n# JSON rows:\n")
        print(json.dumps(rows, ensure_ascii=False, indent=2))

    # Also log parsed rows to stderr for debugging
    print("# Parsed row objects printed to stderr for debugging:", file=sys.stderr)
    print(json.dumps(rows, ensure_ascii=False), file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
