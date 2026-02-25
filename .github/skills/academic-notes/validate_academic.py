#!/usr/bin/env python3
"""validate_academic.py

Strict validator for academic course notes under `special/academia/*`.

All structural and stylistic rules that were previously advisory are now
considered errors. The tool enforces complete metadata, proper flashcard use,
and a wide range of formatting conventions; any violation causes a nonzero
exit code and must be resolved before publishing course material. The
`--content` flag still exists for backward compatibility but is ignored –
all checks are always applied.

Usage:
    python validate_academic.py [--content] [paths...]

By default it checks `special/academia` and `private/special/academia`.
Exit codes:
  0 - no issues detected
  2 - errors found (including conditions that were previously warnings)
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
    """Collects validation messages found while scanning files.

    Attributes
    - errors: list of (Path, message) tuples for any violation. All issues,
      including those that were formerly warnings, are treated as errors.
    """

    def __init__(self) -> None:
        self.errors: list[tuple[Path, str]] = []

    def add_error(self, path: Path, msg: str) -> None:
        """Record a validation error for the given file path.

        The validator is strict: every message indicates a problem that should
        be corrected before the content is considered valid.
        """
        self.errors.append((path, msg))


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
    """Run checks on a single Markdown file and return (errors, extras).

    All validation rules are treated as errors. The returned second list is a
    legacy artifact and will always be empty. The `content_checks` flag is
    ignored but preserved for backward compatibility.
    """
    errors: list[str] = []
    extras: list[str] = []  # previously warnings
    # DEBUG: show whether content_checks flag is set (removed after debugging)
    # print(f"DEBUG check_markdown_file called with content_checks={content_checks}")
    text = path.read_text(encoding="utf-8")

    front = parse_frontmatter(text)
    if not front:
        errors.append("missing YAML frontmatter")
        return errors, extras

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
                errors.append(
                    "semester headings are not in chronological order ({} comes before {})".format(
                        semesters[i][2], semesters[i - 1][2]
                    )
                )
                break

    if True:  # content_checks ignored (strict mode)
        if (
            re.search(r"(?:^|\n)[ \t\-]*\b(?:lecture|lab|tutorial)\b", text)
            and "topic:" not in text
        ):
            errors.append(
                "appears to include session entries but no 'topic:' found — consider adding concise topic/takeaway"
            )
        # legacy rule removed: the header-level check below already ensures
        # that every Markdown section contains flashcards.  The earlier regex
        # was too broad and triggered false positives on ordinary prose
        # containing the words "lecture", "lab", or "tutorial".
        # (If new heuristics are needed in future they should be far
        # more specific, e.g. looking for explicit week/session headings.)
        # new broader rule: in topic-specific notes (non-index.md files),
        # every Markdown header (level 2 or deeper) must have at least one
        # flashcard marker somewhere in the text that follows it up to the next
        # header of the same or higher level.  This enforces the “every
        # Markdown section” requirement but is skipped for index pages, which
        # are governed by the session-entry rule above.
        if path.name.lower() != "index.md":
            header_iter = re.finditer(r"^(#{2,})\s+(.+)$", text, re.MULTILINE)
            for h in header_iter:
                lvl = len(h.group(1))
                start = h.end()
                # look ahead for next header of level <= current
                pattern = r"^(#{1,%d})\s+" % lvl
                m = re.search(pattern, text[start:], re.MULTILINE)
                end = start + (m.start() if m else len(text) - start)
                section = text[start:end]
                has_marker = bool(
                    re.search(r"::@::|:@:|Flashcards for this section", section)
                )
                if not has_marker:
                    hdr = h.group(0).strip()
                    errors.append(
                        f"header {hdr!r} has no flashcard markers in its section"
                    )
                else:
                    # ensure the first marker is preceded by a horizontal rule
                    m2 = re.search(r"(::@::|:@:|Flashcards for this section)", section)
                    if m2:
                        prefix = section[: m2.start()]
                        if "---" not in prefix:
                            hdr = h.group(0).strip()
                            errors.append(
                                f"flashcards under header {hdr!r} should be preceded by a '---' separator"
                            )
        # new rule: flag asterisk-based emphasis
        # (regex should avoid matching table pipes or escaped asterisks)
        if re.search(r"(?<!\\)(\*\*[^\*\n]+\*\*|\*[^\*\n]+\*)", text):
            errors.append(
                "found asterisk-based emphasis; use underscores (_italic_) or __bold__ instead"
            )
        # warn if common units appear outside math delimiters; this helps catch
        # oversights such as writing "5 V" or "0.125 W" without surrounding
        # dollar signs.  We split on dollar-delimited segments and examine only
        # the portions outside math mode.
        parts = re.split(r"(\$.*?\$)", text, flags=re.DOTALL)
        for segment in parts[::2]:
            if re.search(r"\b\d+(?:\.\d+)?\s*(?:V|A|Ω|W|mW|kΩ|C|Hz)\b", segment):
                errors.append(
                    "found a unit (e.g. V, A, Ω, W, mW, kΩ, C, Hz) outside math delimiters; enclose units in $...$"
                )
                break
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
                    errors.append(
                        "exam section appears before some lecture/lab/tutorial entries — exams should be placed after other sessions"
                    )
        # unscheduled sessions should not carry a topic field
        if "status: unscheduled" in lower and "topic:" in lower:
            errors.append(
                "session marked status: unscheduled but contains a 'topic:' field; remove topic from unscheduled sessions"
            )
        # forward-looking remarks about the next lecture/week are usually unnecessary
        if re.search(r"\bnext\s+(lecture|week|class)\b", lower):
            errors.append(
                "contains a 'next lecture/next week' remark; remove unless referring to a major grading component"
            )
        # duplicate week numbers indicate holiday or numbering bug
        week_nums = re.findall(r"##\s+week\s+(\d+)", lower)
        seen: set[str] = set()
        for num in week_nums:
            if num in seen:
                errors.append(
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
                errors.append(
                    "nested list item does not include full path (e.g. 'ELEC 1100 / ...')"
                )
                break
        # QA-style flashcard list check: look for a simple question::@::answer
        # bullet where the portion before the separator contains no slash.  The
        # previous implementation only checked the first character, causing
        # false positives when a course path (which includes slashes) appeared
        # later in the text.  This stricter regex prevents the flatten-single-
        # child case from being flagged.
        lines = text.splitlines()
        for i, line in enumerate(lines):
            # match a bullet whose left-hand text (up to the separator) has no '/'
            if re.match(r"^\s*-\s+([^/]*?)::@::", line) or re.match(
                r"^\s*-\s+([^/]*?):@:", line
            ):
                # look back for a nonblank previous line
                j = i - 1
                prev = None
                while j >= 0:
                    if lines[j].strip():
                        prev = lines[j].strip()
                        break
                    j -= 1
                if prev not in (
                    "Flashcards for this section are as follows:",
                    "---",
                ):
                    errors.append(
                        "QA-style flashcard list detected without preceding separator phrase"
                    )
                break
        # warn about lines that contain more than one flashcard separator
        for line in lines:
            if line.count("::@::") > 1 or line.count(":@:") > 1:
                errors.append(
                    "line contains multiple flashcard separators (::@:: or :@:); use only one per card"
                )
                break
        # warn when <br/> appears without a leading space (common in bibliographic lists)
        if re.search(r"[^ \t]>?<br/>", text):
            # ensure it's not part of an HTML tag like <br/> itself; we look for any
            # non-space character immediately before the break
            for line in lines:
                if re.search(r"[^ \t]<br/>", line):
                    errors.append(
                        "'<br/>' found without a preceding space; add a space before '<br/>'"
                    )
                    break

    return errors, extras


def walk_and_check(
    roots: Sequence[Path], content_checks: bool = False
) -> ValidationResult:
    """Walk `roots` recursively and validate all Markdown files.

    Returns a `ValidationResult` containing aggregated errors.  Previously the
    tool distinguished warnings; those are now elevated to errors and are
    merged before returning. Missing root paths produce a printed warning but
    do not abort the scan.
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
                for w in warns:  # extras from legacy behavior
                    res.add_error(p, w)
            except Exception as exc:
                res.add_error(p, f"exception while checking: {exc}")
    return res


def main(argv: Sequence[str] | None = None) -> int:
    """Command-line entry point for the validator.

    By default the tool checks `special/academia` and `private/special/academia`.
    The validator enforces all rules and treats every failure as an error. The
    `--content` flag is accepted for backwards compatibility but has no effect.
    `--json` will still emit a machine-readable summary; the warnings array is
    kept for compatibility but will always be empty.
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
        help="(ignored) legacy flag; all checks are always strict",
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

    if args.json:
        out = {
            "errors": [[msg, paths] for msg, paths in agg_errors.items()],
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

    # no warnings stage any more
    print("OK: No issues detected (basic checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
