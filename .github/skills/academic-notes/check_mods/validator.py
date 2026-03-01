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
from rich.text import Text

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

_CONSOLE = Console(markup=False, emoji=False, highlight=False)


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
                        "suppression-missing-rationale",
                        "suppression comment missing rationale",
                        line=lineno,
                    )
                )
            rule_ids = [r.strip() for r in rules_list.split(",") if r.strip()]
            if not rule_ids:
                errors.append(
                    ValidationMessage(
                        "suppression-missing-rules",
                        "suppression comment contains no rule names",
                        line=lineno,
                    )
                )
            target = lineno + 1 if kind == "ignore-next-line" else lineno
            for rid in rule_ids:
                suppressions.setdefault(target, []).append(rid)

    front = parse_frontmatter(text)
    if not front:
        errors.append(
            ValidationMessage("missing-yaml-frontmatter", "missing YAML frontmatter")
        )
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
                ValidationMessage(
                    "validator-exception", f"exception in rule {rule.__name__}: {exc}"
                )
            )
            continue
        errors.extend(results)

    # before we actually apply the suppression filter, look for any
    # redundant directives.  A suppression is redundant when the target line
    # never produced an error with the given rule ID.  Emit an error in that
    # case so authors can clean up stale or misspelled comments.
    if suppressions:
        active = {(m.line, m.rule_id) for m in errors if m.line is not None}
        for target, rule_ids in suppressions.items():
            for rid in rule_ids:
                if (target, rid) not in active:
                    errors.append(
                        ValidationMessage(
                            "suppression-redundant",
                            f"suppression for rule {rid!r} on line {target} has no matching error",
                            line=target,
                        )
                    )

    # apply suppression map: drop any errors whose line number matches and
    # whose rule ID appears in the suppression list for that line.  Messages
    # without a line number or whose rule isn't listed are kept.  suppression
    # map keys come from comment parsing earlier.
    if suppressions:
        filtered: list[ValidationMessage] = []
        for m in errors:
            if m.line is not None:
                ignore_for_line = suppressions.get(m.line, [])
                if m.rule_id in ignore_for_line:
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
            _CONSOLE.print(
                f"[yellow]Warning:[/] path does not exist: {root}", markup=True
            )
            continue

        if await root.is_file():
            # single file provided as a root; only process if it's markdown
            if root.suffix.lower() == ".md":
                try:
                    msgs = await check_markdown_file(root)
                    for m in msgs:
                        res.add(root, m)
                except Exception as exc:
                    res.add(
                        root,
                        ValidationMessage(
                            "validator-exception", f"exception while checking: {exc}"
                        ),
                    )
            else:
                _CONSOLE.print(
                    f"[yellow]Warning:[/] skipping non-markdown file: {root}",
                    markup=True,
                )
            continue

        # otherwise treat it as a directory
        async for p in root.rglob("*.md"):
            try:
                msgs = await check_markdown_file(p)
                for m in msgs:
                    res.add(p, m)
            except Exception as exc:
                res.add(
                    p,
                    ValidationMessage(
                        "validator-exception", f"exception while checking: {exc}"
                    ),
                )
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
    parser.add_argument(
        "--max-per-rule",
        type=int,
        default=5,
        help=(
            "Maximum number of occurrences to display per rule ID in the console. "
            "Set to 0 for no limit. (JSON output is unaffected.)"
        ),
    )
    args = parser.parse_args(argv)

    roots = [Path(p) for p in (args.paths or DEFAULT_PATHS)]
    res = await walk_and_check(roots)

    error_items = [(p, m) for p, m in res.messages if m.severity is Severity.ERROR]
    warning_items = [(p, m) for p, m in res.messages if m.severity is Severity.WARNING]
    all_items = [(p, m) for p, m in res.messages]

    if args.json:
        # produce a flat list of all issues with their locations
        width = getattr(_CONSOLE.size, "width", 80)
        agg_all = await aggregate(all_items, width)
        # ``aggregate`` returns ``dict[str, list[PreviewEntry]]``.  When
        # emitting JSON we want a mapping of rule IDs to lists of serialized
        # entries, which is easier for consumers to index.
        out: dict[str, dict[str, list[object]]] = {"issues": {}}

        for key_id, entries in agg_all.items():
            # ``entries`` is ``list[PreviewEntry]``; convert them to dicts.
            out["issues"][key_id] = [e.to_dict() for e in entries]
        print(json.dumps(out, ensure_ascii=False, indent=2))
        # exit codes unchanged (errors still take precedence)
        if error_items:
            return 2
        if warning_items:
            return 1
        return 0

    if all_items:
        errcount = len(error_items)
        warncount = len(warning_items)
        total = len(all_items)
        _CONSOLE.print(
            f"[bold red]Validation issues:[/] {total} problem(s) found "
            f"({errcount} errors, {warncount} warnings)\n",
            markup=True,
        )
        width = getattr(_CONSOLE.size, "width", 80)
        agg_all = await aggregate(all_items, width)

        # when printing to console, optionally cap the number of entries shown
        orig_counts: dict[str, int] = {k: len(v) for k, v in agg_all.items()}
        limit = args.max_per_rule
        if limit and limit > 0:
            for k, entries in list(agg_all.items()):
                if len(entries) > limit:
                    agg_all[k] = entries[:limit]

        for key_id, entries in agg_all.items():
            first = entries[0]
            msg = first.msg
            severity = first.severity
            prefix = f"[{severity}/{key_id}]"
            display = f"{prefix} {msg}" if severity else f"{key_id} {msg}"
            txt = Text(display)
            txt.stylize(severity.color, 0, len(prefix))
            if len(display) > len(prefix):
                txt.stylize("bold", len(prefix), len(display))
            _CONSOLE.print(txt, end=" - ")
            shown = len(entries)
            # total occurrences for this rule (may be higher than shown)
            total_for_rule = orig_counts.get(key_id, shown)
            # print number displayed; if we truncated, show actual total too
            if limit and limit > 0 and total_for_rule > shown:
                _CONSOLE.print(
                    f"{shown}/{total_for_rule} occurrence(s)", highlight=True
                )
            else:
                _CONSOLE.print(f"{shown} occurrence(s)", highlight=True)
            for e in entries:
                loc = fspath(e.path)
                if e.line is not None:
                    loc += f":{e.line}"
                    if e.col is not None:
                        loc += f":{e.col}"
                _CONSOLE.print(loc, style="grey53")
                if e.excerpt:
                    _CONSOLE.print(e.excerpt, highlight=True)
                    if e.caret:
                        _CONSOLE.print(e.caret)
            # indicate if we truncated results for this rule
            if limit and limit > 0 and total_for_rule > shown:
                omitted = total_for_rule - shown
                _CONSOLE.print(
                    f"[grey53]... {omitted} more occurrence(s) not shown[/]",
                    markup=True,
                    highlight=True,
                )
            _CONSOLE.print()
        _CONSOLE.print(
            "Please fix errors and review warnings before publishing or report to maintainers if unsure."
        )
        return 2 if errcount else 1

    _CONSOLE.print("[green]OK:[/] No issues detected (basic checks)", markup=True)
    return 0
