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

    for _, rule in RULE_REGISTRY.items():
        try:
            results = rule(ctx)
        except Exception as exc:  # pragma: no cover - defensive
            errors.append(
                ValidationMessage(f"exception in rule {rule.__name__}: {exc}")
            )
            continue
        errors.extend(results)

    return errors


async def walk_and_check(roots: Sequence[Path]) -> ValidationResult:
    """Recursively validate all Markdown files under *roots*.

    Missing root paths produce a printed warning but do not abort the scan.
    The returned :class:`ValidationResult` holds both errors and warnings;
    callers can inspect them separately.
    """
    res = ValidationResult()
    for root in roots:
        if not await root.exists():
            _CONSOLE.print(f"[yellow]Warning:[/] path does not exist: {root}")
            continue
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
            _CONSOLE.print(msg, style="bold", markup=False, end="")
            _CONSOLE.print(f" — {len(entries)} file(s)", markup=False)
            for e in entries:
                loc = ""
                if e.line is not None:
                    loc = f" (line {e.line}"
                    if e.col is not None:
                        loc += f", col {e.col}"
                    loc += ")"
                _CONSOLE.print(f"    - {e.path}{loc}", markup=False)
                if e.excerpt:
                    prefix = "      preview: "
                    _CONSOLE.print(prefix + e.excerpt, markup=False)
                    if e.caret:
                        _CONSOLE.print(" " * len(prefix) + e.caret, markup=False)
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
            _CONSOLE.print(msg, style="bold", markup=False, end="")
            _CONSOLE.print(f" — {len(entries)} file(s)", markup=False)
            for e in entries:
                loc = ""
                if e.line is not None:
                    loc = f" (line {e.line}"
                    if e.col is not None:
                        loc += f", col {e.col}"
                    loc += ")"
                _CONSOLE.print(f"    - {e.path}{loc}", markup=False)
                if e.excerpt:
                    prefix = "      preview: "
                    _CONSOLE.print(prefix + e.excerpt, markup=False)
                    if e.caret:
                        _CONSOLE.print(" " * len(prefix) + e.caret, markup=False)
        _CONSOLE.print("\nWarnings do not block publishing but should be reviewed.")
        return 1

    _CONSOLE.print("[green]OK:[/] No issues detected (basic checks)")
    return 0
