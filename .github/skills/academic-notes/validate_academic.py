#!/usr/bin/env python3
"""validate_academic.py

Lightweight validator for academic course notes under `special/academia/*`.

The validator performs basic structure checks (frontmatter, children lists,
flashcard tags) and, when run in content mode, emits advisory warnings for
common patterns such as missing topics, exams placed before lectures,
duplicate week numbers, unscheduled sessions carrying a topic field, and
out-of-order semester headings.

Usage:
    python validate_academic.py [--content] [paths...]

By default it checks `special/academia` and `private/special/academia`.
Exit codes:
  0 - no issues (and no warnings when --content used)
  2 - fatal issues found
"""

import argparse
import json
import re
from collections.abc import Sequence
from pathlib import Path

DEFAULT_PATHS = ["special/academia", "private/special/academia"]

# Accept varied line endings and optional whitespace around YAML '---' markers
FRONT_RE = re.compile(r"\A\s*---\s*\r?\n(.*?)\r?\n---\s*(\r?\n|$)", re.S)
# Generic flash tag prefix for any institution under special/academia
FLASH_TAG_RE = re.compile(r"flashcard/active/special/academia/", re.I)


class ValidationResult:
    """Collects validation errors and warnings found while scanning files.

    Attributes
    - errors: list of (Path, message) tuples for issues that should be fixed.
    - warnings: list of (Path, message) tuples for advisory content guidance.
    """

    def __init__(self) -> None:
        self.errors: list[tuple[Path, str]] = []
        self.warnings: list[tuple[Path, str]] = []

    def add_error(self, path: Path, msg: str) -> None:
        """Record a validation error for the given file path.

        Errors indicate missing or malformed required metadata and should be
        corrected before publishing (or brought to the maintainers' attention).
        """
        self.errors.append((path, msg))

    def add_warning(self, path: Path, msg: str) -> None:
        """Record a non-fatal advisory message about content quality.

        Warnings are intended for `--content` guidance and are not treated as
        fatal by default.
        """
        self.warnings.append((path, msg))


def parse_frontmatter(text: str) -> str | None:
    """Extract YAML frontmatter from the given Markdown text.

    Returns the raw YAML body as a string, or None if frontmatter is missing.
    The regex is tolerant of CRLF vs LF line endings.
    """
    m = FRONT_RE.match(text)
    return m.group(1) if m else None


def has_flash_tag(front: str) -> bool:
    """Return True if the frontmatter contains a flashcard activation tag.

    The check is case-insensitive and looks for the `flashcard/active/...`
    prefix under `special/academia`.
    """
    return bool(FLASH_TAG_RE.search(front))


def check_markdown_file(
    path: Path, content_checks: bool = False
) -> tuple[list[str], list[str]]:
    """Run checks on a single Markdown file and return (errors, warnings).

    Errors are missing or malformed required fields (frontmatter, tags,
    index structure). Warnings are content-style suggestions emitted only when
    `content_checks` is True (i.e., the `--content` mode).
    """
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")

    front = parse_frontmatter(text)
    if not front:
        errors.append("missing YAML frontmatter")
        return errors, warnings

    if "tags:" not in front:
        errors.append("no 'tags:' in frontmatter")
    elif not has_flash_tag(front):
        errors.append("missing flashcard activation tag in 'tags:'")

    name = path.name.lower()
    if name == "index.md":
        if "# index" not in text:
            errors.append("index.md missing '# index' heading")
        if "## children" not in text and "children:" not in text:
            errors.append("index missing 'children' section")
        # check semester heading chronological order if this is an institution index
        # look for lines like "### YYYY term" and ensure they increase
        semesters: list[tuple[int, int, str]] = []  # list of (year, term_order, text)
        term_map = {"winter": 1, "spring": 2, "summer": 3, "fall": 4}
        for line in text.splitlines():
            m = re.match(r"###\s+(\d{4})\s+([A-Za-z]+)", line)
            if m:
                year = int(m.group(1))
                term = m.group(2).lower()
                order = term_map.get(term)
                if order:
                    semesters.append((year, order, line))
        for i in range(1, len(semesters)):
            if semesters[i][:2] < semesters[i - 1][:2]:
                warnings.append(
                    "semester headings are not in chronological order ({} comes before {})".format(
                        semesters[i][2], semesters[i - 1][2]
                    )
                )
                break

    # check for session entries (lecture/lab/tutorial) using word boundaries
    # to avoid matching fragments such as 'lab' inside 'available'.
    if re.search(r"\b(lecture|lab|tutorial)\b", text) and "datetime:" not in text:
        errors.append("appears to include session entries but no 'datetime:' found")

    if content_checks:
        if re.search(r"\b(lecture|lab|tutorial)\b", text) and "topic:" not in text:
            warnings.append(
                "appears to include session entries but no 'topic:' found — consider adding concise topic/takeaway"
            )
        # previous versions warned when no learning_outcomes or takeaway was
        # present.  Feedback showed that explicit outcome sections are often
        # redundant—authors typically capture objectives in prose or via
        # flashcards—so the warning has been removed (continuous learning).
        # If future consensus shifts, reintroduce a lighter advisory here.
        # exam ordering: exams should come after other session types
        lower = text.lower()
        if "midterm" in lower or "final" in lower:
            # find position of first exam header
            exam_idx = min(
                (
                    lower.find(h)
                    for h in ["## midterm", "## final"]
                    if lower.find(h) != -1
                ),
                default=-1,
            )
            if exam_idx != -1:
                # look for any week/lecture/lab/tutorial after that index
                tail = lower[exam_idx:]
                if any(k in tail for k in ["## week", "lecture", "lab", "tutorial"]):
                    warnings.append(
                        "exam section appears before some lecture/lab/tutorial entries — exams should be placed after other sessions"
                    )
        # unscheduled sessions should not carry a topic field
        if "status: unscheduled" in lower and "topic:" in lower:
            warnings.append(
                "session marked status: unscheduled but contains a 'topic:' field; remove topic from unscheduled sessions"
            )
        # duplicate week numbers indicate holiday or numbering bug
        week_nums = re.findall(r"##\s+week\s+(\d+)", lower)
        seen: set[str] = set()
        for num in week_nums:
            if num in seen:
                warnings.append(
                    f"duplicate week number {num} found; check for holiday or numbering bug"
                )
                break
            seen.add(num)
        # flashcard path completeness: after the top-level course bullet, any
        # nested bullet should include a slash in its text.  Ignore frontmatter
        # and items that occur before the course name appears (e.g. logistics
        # section).  This prevents alerts on unrelated lists.
        body = text
        m = FRONT_RE.match(text)
        if m:
            body = text[m.end() :]
        # determine course identifier from first top-level bullet in the body
        course = None
        for line in body.splitlines():
            m = re.match(r"^\s*-\s+(.+?)\s*$", line)
            if m:
                # use entire text after dash as course name
                course = m.group(1)
                break
        seen_course = False
        for line in body.splitlines():
            if not seen_course and course and line.strip().startswith(f"- {course}"):
                seen_course = True
                continue
            if not seen_course:
                continue
            # if we reach a new top-level heading, stop checking further
            if line.lstrip().startswith("## "):
                break
            # match any bullet with at least two spaces of indentation
            if re.match(r"^ {2,}- ", line) and "/" not in line:
                warnings.append(
                    "nested list item does not include full path (e.g. 'ELEC 1100 / ...')"
                )
                break

    return errors, warnings


def walk_and_check(
    roots: Sequence[Path], content_checks: bool = False
) -> ValidationResult:
    """Walk `roots` recursively and check all Markdown files.

    Returns a `ValidationResult` containing aggregated errors and warnings.
    Missing root paths are warned about but do not stop the scan.
    """
    res = ValidationResult()
    for root in roots:
        if not root.exists():
            print(f"Warning: path does not exist: {root}")
            continue
        for p in root.rglob("*.md"):
            try:
                errs, warns = check_markdown_file(p, content_checks=content_checks)
                for e in errs:
                    res.add_error(p, e)
                for w in warns:
                    res.add_warning(p, w)
            except Exception as exc:
                res.add_error(p, f"exception while checking: {exc}")
    return res


def main(argv: Sequence[str] | None = None) -> int:
    """Command-line entry point for the validator.

    By default the tool checks `special/academia` and `private/special/academia`.
    Use `--content` to enable advisory content warnings. Use `--json` to emit a
    machine-readable summary of errors and warnings.
    """
    parser = argparse.ArgumentParser(
        prog="validate_academic.py",
        description="Validate academic course notes (basic structural and content checks)",
    )
    parser.add_argument(
        "paths", nargs="*", help="Paths to check (defaults to special/academia roots)"
    )
    parser.add_argument(
        "--content",
        action="store_true",
        help="Enable non-strict content guidance warnings (advisory)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output with `errors` and `warnings` arrays (machine-readable)",
    )
    args = parser.parse_args(argv)

    roots = [Path(p) for p in (args.paths or DEFAULT_PATHS)]
    res = walk_and_check(roots, content_checks=args.content)

    # Helper: extract a short context snippet for a file and message
    def get_excerpt(path: str, msg: str, chars: int = 200) -> str:
        try:
            text = Path(path).read_text(encoding="utf-8")
        except Exception:
            return "(no preview available)"
        # Frontmatter preview
        fm = parse_frontmatter(text)
        if "frontmatter" in msg.lower() or "tags:" in msg.lower():
            if fm:
                lines = fm.strip().splitlines()[:6]
                if lines:
                    return "\n".join(lines)
            return text[:chars]
        # datetime/topic related: try to find a nearby line
        for keyword in ["datetime:", "topic:", "lecture", "lab", "tutorial", "week"]:
            idx = text.lower().find(keyword)
            if idx != -1:
                start = max(0, idx - 60)
                return text[start : start + chars].strip().replace("\n", " ")
        # default: return file head
        return text[:chars].strip().replace("\n", " ")

    # Aggregate messages to improve human readability and include excerpts
    def aggregate(items: list[tuple[Path, str]]) -> dict[str, list[dict[str, str]]]:
        agg: dict[str, list[dict[str, str]]] = {}
        for p, msg in items:
            excerpt = get_excerpt(str(p), msg)
            agg.setdefault(msg, []).append({"path": str(p), "excerpt": excerpt})
        return agg

    agg_errors = aggregate(res.errors)
    agg_warnings = aggregate(res.warnings)

    if args.json:
        out = {
            "errors": [[msg, paths] for msg, paths in agg_errors.items()],
            "warnings": [[msg, paths] for msg, paths in agg_warnings.items()],
        }
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return 2 if res.errors else 0

    # Human-friendly summary
    if res.errors:
        total = len(res.errors)
        print(f"Validation errors: {total} problem(s) found.\n")
        for msg, entries in agg_errors.items():
            print(f"* {msg} — {len(entries)} file(s)")
            for e in entries[:5]:
                print(f"    - {e['path']}")
                if e.get("excerpt"):
                    print(f"      preview: {e['excerpt']}")
            if len(entries) > 5:
                print(f"    ... and {len(entries) - 5} more\n")
        print(
            "\nPlease fix errors before publishing or report to maintainers if unsure."
        )
        return 2

    if res.warnings:
        total = len(res.warnings)
        print(f"Validation warnings: {total} advisory message(s) found.\n")
        for msg, entries in agg_warnings.items():
            print(f"* {msg} — {len(entries)} file(s)")
            for e in entries[:5]:
                print(f"    - {e['path']}")
                if e.get("excerpt"):
                    print(f"      preview: {e['excerpt']}")
            if len(entries) > 5:
                print(f"    ... and {len(entries) - 5} more\n")
        print(
            "\nThese are advisory suggestions; consider addressing the most common issues first or running with `--content` to get more guidance."
        )
        return 0

    print("OK: No issues detected (basic checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
