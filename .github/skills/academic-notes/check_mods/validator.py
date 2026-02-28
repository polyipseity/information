"""Core validation logic for academic-note Markdown files.

This module provides asynchronous functions that read files, construct a
:class:`ValidationContext`, execute all registered rules, and aggregate the
results.  The command-line entry point lives in ``check.py`` so the core
logic can be reused by tests and other callers.
"""

import json
import re
from argparse import ArgumentParser
from collections.abc import Sequence
from os import fspath

from anyio import Path
from pydantic_yaml import parse_yaml_raw_as
from rich.console import Console

from . import rules
from .models import (
    Frontmatter,
    Severity,
    ValidationContext,
    ValidationMessage,
    ValidationResult,
)
from .registry import RuleRegistry
from .utils import DEFAULT_PATHS, FRONT_RE, aggregate, parse_frontmatter

# build local registry and import the rules defined in rules.py
RULE_REGISTRY = RuleRegistry()
RULE_REGISTRY.include_registry(rules.RULE_REGISTRY)


__all__ = (
    "check_markdown_file",
    "walk_and_check",
    "main",
)

_CONSOLE = Console()


async def check_markdown_file(path: Path) -> list[ValidationMessage]:
    """Validate a single Markdown file and return any messages found.

    This is the core unit used by ``walk_and_check`` and by the test suite.
    The file’s frontmatter is parsed and a :class:`ValidationContext` built;
    each registered rule is invoked exactly once.  Rules are expected to
    return a ``Sequence[ValidationMessage]``; if a rule raises an exception a
    special message is appended so that the caller can observe the failure but
    continue processing other rules.
    """
    errors: list[ValidationMessage] = []
    text = await path.read_text(encoding="utf-8")

    # parse suppression comments of the form
    # <!-- check: ignore-line[rule1, rule2]: rationale -->
    # or ignore-next-line.  Build a map from target line number to list of
    # rule IDs to ignore.  Also emit a warning if the rationale is missing or
    # if no rules are listed.
    suppressions: dict[int, list[str]] = {}
    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in re.finditer(
            r"<!--\s*check:\s*(ignore-(?:line|next-line))\s*\[([^\]]*)\]\s*:\s*(.*?)\s*-->",
            line,
        ):
            kind = m.group(1)
            rules_list = m.group(2)
            rationale = m.group(3).strip()
            if not rationale:
                errors.append(
                    ValidationMessage(
                        "suppression comment missing rationale",
                        lineno,
                    )
                )
            rule_ids = [r.strip() for r in rules_list.split(",") if r.strip()]
            if not rule_ids:
                errors.append(
                    ValidationMessage(
                        "suppression comment contains no rule names",
                        lineno,
                    )
                )
            target = lineno + 1 if kind == "ignore-next-line" else lineno
            for rid in rule_ids:
                suppressions.setdefault(target, []).append(rid)

    front = parse_frontmatter(text)
    if not front:
        errors.append(ValidationMessage("missing YAML frontmatter"))
        return errors

    # parse YAML frontmatter into our model; pydantic does not support YAML
    # natively so we use PyYAML (imported at module level) to pre-process.  This
    # avoids silently dropping fields and ensures the validator sees whatever
    # tags/aliases the author provided.
    try:
        data = parse_yaml_raw_as(Frontmatter, front)
    except Exception:
        data = Frontmatter()

    body = text
    m = FRONT_RE.match(text)
    if m:
        body = text[m.end() :]

    session_headers: list[tuple[str, str, str, int]] = []
    for m in re.finditer(
        r"^##\s+week\s+(\d+)(?:\s+(\w+))?", text, re.IGNORECASE | re.MULTILINE
    ):
        week = m.group(1)
        typ = (m.group(2) or "").lower()
        session_headers.append((week, typ, m.group(0), m.start()))

    ctx = ValidationContext(
        path=path,
        text=text,
        front=front,
        data=data,
        body=body,
        session_headers=session_headers,
    )

    for rid, rule in RULE_REGISTRY.items():
        try:
            results = rule(ctx)
        except Exception as exc:  # pragma: no cover - defensive
            errors.append(
                ValidationMessage(f"exception in rule {rule.__name__}: {exc}")
            )
            continue
        # prefix each message with the rule ID for clearer headers
        for m in results:
            # avoid duplicate prefix if already present (e.g. tests may wrap)
            if not m.msg.startswith(f"[{rid}] "):
                m.msg = f"[{rid}] {m.msg}"
        errors.extend(results)

    # apply suppression map: drop any errors whose line number matches and
    # whose rule ID appears in the suppression list for that line.  Messages
    # without a line number or whose rule isn't listed are kept.  suppression
    # map keys come from comment parsing earlier.
    if suppressions:
        filtered: list[ValidationMessage] = []
        for m in errors:
            if m.line is not None:
                ignore_for_line = suppressions.get(m.line, [])
                suppressed = False
                for rid in ignore_for_line:
                    if m.msg.startswith(f"[{rid}]"):
                        suppressed = True
                        break
                if suppressed:
                    continue
            filtered.append(m)
        errors = filtered

    return errors


async def walk_and_check(roots: Sequence[Path]) -> ValidationResult:
    """Recursively validate all Markdown files under *roots*.

    Each entry in *roots* may be either a directory (in which case we
    recurse using ``rglob`` as before) or a path to a single file.  Only
    ``.md`` files are examined; non-markdown files are ignored with a
    warning.  A missing path is also reported but does not abort the scan.

    The returned :class:`ValidationResult` holds both errors and warnings;
    callers can inspect them separately.
    """
    res = ValidationResult()
    for root in roots:
        if not await root.exists():
            _CONSOLE.print(f"[yellow]Warning:[/] path does not exist: {root}")
            continue

        if await root.is_file():
            # single file provided as a root; only process if it's markdown
            if root.suffix.lower() == ".md":
                try:
                    msgs = await check_markdown_file(root)
                    for m in msgs:
                        res.add(root, m)
                except Exception as exc:
                    res.add(root, ValidationMessage(f"exception while checking: {exc}"))
            else:
                _CONSOLE.print(
                    f"[yellow]Warning:[/] skipping non-markdown file: {root}"
                )
            continue

        # otherwise treat it as a directory
        async for p in root.rglob("*.md"):
            try:
                msgs = await check_markdown_file(p)
                for m in msgs:
                    res.add(p, m)
            except Exception as exc:
                res.add(p, ValidationMessage(f"exception while checking: {exc}"))
    return res


async def main(argv: Sequence[str] | None = None) -> int:
    """Command-line entry point invoked by ``check.py``.

    By default the tool checks ``special/academia`` and
    ``private/special/academia``.  ``--json`` emits a machine-readable
    summary with ``errors`` and ``warnings`` arrays; warnings are normally
    empty under the current rule set.
    """
    parser = ArgumentParser(
        prog="check.py",
        description="Validate academic course notes (basic structural and content checks)",
    )
    parser.add_argument(
        "paths", nargs="*", help="Paths to check (defaults to special/academia roots)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output with `errors` and `warnings` arrays (machine-readable)",
    )
    args = parser.parse_args(argv)

    roots = [Path(p) for p in (args.paths or DEFAULT_PATHS)]
    res = await walk_and_check(roots)

    error_items = [(p, m) for p, m in res.messages if m.severity is Severity.ERROR]
    warning_items = [(p, m) for p, m in res.messages if m.severity is Severity.WARNING]

    if args.json:
        width = getattr(_CONSOLE.size, "width", 80)
        agg_errors = await aggregate(error_items, width)
        agg_warnings = await aggregate(warning_items, width)
        out = {
            "errors": [[msg, [e.to_dict() for e in paths]]]
            for msg, paths in agg_errors.items()
        }
        out["warnings"] = [
            [msg, [e.to_dict() for e in paths]] for msg, paths in agg_warnings.items()
        ]
        print(json.dumps(out, ensure_ascii=False, indent=2))
        if error_items:
            return 2
        if warning_items:
            return 1
        return 0

    if error_items:
        total = len(error_items)
        _CONSOLE.print(f"[bold red]Validation errors:[/] {total} problem(s) found.\n")
        width = getattr(_CONSOLE.size, "width", 80)
        agg_errors = await aggregate(error_items, width)
        for msg, entries in agg_errors.items():
            msg = msg.lstrip()
            if msg.startswith("[") and "]" in msg:
                id_part, rest = msg.split("]", 1)
                id_part += "]"
                _CONSOLE.print(
                    id_part, style="bold cyan", end="", markup=False, highlight=False
                )
                _CONSOLE.print(rest, style="bold", markup=False)
            else:
                _CONSOLE.print(msg, style="bold", markup=False)
            _CONSOLE.print(f"{len(entries)} occurrence(s)", markup=False)
            for e in entries:
                loc = fspath(e.path)
                if e.line is not None:
                    loc += f":{e.line}"
                    if e.col is not None:
                        loc += f":{e.col}"
                _CONSOLE.print(loc, markup=False, highlight=False)
                if e.excerpt:
                    _CONSOLE.print(e.excerpt, markup=False)
                    if e.caret:
                        _CONSOLE.print(e.caret, markup=False)
        _CONSOLE.print(
            "\nPlease fix errors before publishing or report to maintainers if unsure."
        )
        if warning_items:
            agg_warnings = await aggregate(warning_items, width)
            _CONSOLE.print(
                f"\n[bold yellow]Validation warnings also present:[/] {len(warning_items)} warning(s)"
            )
        return 2

    if warning_items:
        total = len(warning_items)
        _CONSOLE.print(
            f"[bold yellow]Validation warnings:[/] {total} problem(s) found.\n"
        )
        width = getattr(_CONSOLE.size, "width", 80)
        agg_warnings = await aggregate(warning_items, width)
        for msg, entries in agg_warnings.items():
            msg = msg.lstrip()
            if msg.startswith("[") and "]" in msg:
                id_part, rest = msg.split("]", 1)
                id_part += "]"
                _CONSOLE.print(
                    id_part, style="bold cyan", end="", markup=False, highlight=False
                )
                _CONSOLE.print(rest, style="bold", markup=False)
            else:
                _CONSOLE.print(msg, style="bold", markup=False)
            _CONSOLE.print(f"{len(entries)} occurrence(s)", markup=False)
            for e in entries:
                loc = fspath(e.path)
                if e.line is not None:
                    loc += f":{e.line}"
                    if e.col is not None:
                        loc += f":{e.col}"
                _CONSOLE.print(loc, markup=False, highlight=False)
                if e.excerpt:
                    _CONSOLE.print(e.excerpt, markup=False)
                    if e.caret:
                        _CONSOLE.print(e.caret, markup=False)
        _CONSOLE.print("\nWarnings do not block publishing but should be reviewed.")
        return 1

    _CONSOLE.print("[green]OK:[/] No issues detected (basic checks)")
    return 0
