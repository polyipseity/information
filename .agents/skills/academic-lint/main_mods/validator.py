"""Core validation logic for academic-note Markdown files.

This module provides asynchronous functions that read files, construct a
:class:`ValidationContext`, execute all registered rules, and aggregate the
results.  The command-line entry point lives in ``main.py`` so the core
logic can be reused by tests and other callers.
"""

import json
import re
from argparse import ArgumentParser
from collections.abc import Awaitable, Sequence
from os import fspath
from typing import cast

from anyio import Path
from pydantic_yaml import parse_yaml_raw_as
from rich.console import Console
from rich.text import Text

from . import rules
from .models import (
    AstNode,
    Frontmatter,
    Severity,
    ValidationContext,
    ValidationMessage,
    ValidationResult,
)
from .registry import RuleRegistry, RuleResult
from .utils import (
    _MD,
    DEFAULT_PATHS,
    FRONT_RE,
    aggregate,
    parse_frontmatter,
    parse_session_headers,
)

# build local registry and import the rules defined in rules.py
"""Merged registry of all validation rules; used by main() to run checks."""
RULE_REGISTRY = RuleRegistry()
RULE_REGISTRY.include_registry(rules.RULE_REGISTRY)


"""Public symbols exported by this module."""
__all__ = (
    "check_markdown_file",
    "walk_and_check",
    "main",
)

"""Rich console used for human-readable validation output (non-JSON)."""
_CONSOLE = Console(markup=False, emoji=False, highlight=False)

# Regex matching Markdown heading lines (``# title``, ``## section``, etc.)
"""Regex matching a Markdown heading line (``^\\s*#{1,6}\\s+``)."""
HEADING_LINE_RE = re.compile(r"^\s*#{1,6}\s+")

"""The two directives that span a run of lines rather than one."""
_REGION_KINDS = frozenset({"ignore-begin", "ignore-end"})


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

    # Suppression comments come in five kinds:
    #
    #   <!-- check: ignore-line[rule]: rationale -->       this line
    #   <!-- check: ignore-next-line[rule]: rationale -->   the line below
    #   <!-- check: ignore-file[rule]: rationale -->       the whole file
    #   <!-- check: ignore-begin[rule]: rationale -->      opens a region
    #   <!-- check: ignore-end[rule]: rationale -->        closes that region
    #
    # `suppressions` maps a line number to the rules silenced there, and
    # `file_suppressions` holds the file-wide ones. The first three kinds go
    # straight in. A region covers lines the author cannot edit, such as an
    # indented code block, so it is expanded into every line it spans once the
    # closer has been read.
    suppressions: dict[int, dict[str, set[str]]] = {}
    file_suppressions: list[tuple[str, int]] = []
    # A directive inside a fence targets code that is never checked, so it
    # suppresses nothing. The fence walk is the rules module's rather than a
    # second one here, since two copies of the same scan drift apart.
    front_head = FRONT_RE.match(text)
    body_start = front_head.end() if front_head else 0
    fenced_lines = dict(rules.iter_fence_state(text, body_start))
    # Line of the open region and the rules it named, or None when none is
    # open. Regions do not nest, so this is a pair rather than a stack.
    region_line: int | None = None
    region_rules: frozenset[str] = frozenset()
    # Closed regions as (first line, last line, rule). Kept so a region can be
    # judged for redundancy as a whole rather than line by line.
    region_spans: list[tuple[int, int, str]] = []
    offset = 0
    for lineno, line in enumerate(text.splitlines(), start=1):
        fenced = fenced_lines.get(offset, False)
        offset += len(line) + 1
        # gather all suppression directives on this line so we can detect
        # duplicates of the same kind (ignore-line vs ignore-next-line vs
        # ignore-file). Authors should merge them since the syntax already
        # allows listing multiple rule names in a single comment.
        matches = list(
            re.finditer(
                r"<!--\s*check:\s*(ignore-(?:line|next-line|file|begin|end))\s*\[([^\]]*)\]\s*:\s*(.*?)\s*-->",
                line,
            )
        )
        if len(matches) > 1:
            kinds = [m.group(1) for m in matches]
            # look for any kind appearing more than once
            for kind in set(kinds):
                if kinds.count(kind) > 1:
                    errors.append(
                        ValidationMessage(
                            "suppression-multiple-commands",
                            (
                                f"multiple suppression directives of type {kind!r} on the "
                                "same line; merge into one comment and list all rule IDs "
                                "(the syntax supports suppressing multiple rules at once)"
                            ),
                            line=lineno,
                        )
                    )
        # now process each directive normally
        for m in matches:
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

            if fenced:
                errors.append(
                    ValidationMessage(
                        "suppression-in-code-block",
                        (
                            f"{kind} sits inside a fenced code block, so it "
                            "suppresses nothing; move it outside and wrap the "
                            "block in ignore-begin and ignore-end"
                        ),
                        severity=Severity.WARNING,
                        line=lineno,
                    )
                )
                continue

            if kind == "ignore-begin":
                if region_line is not None:
                    errors.append(
                        ValidationMessage(
                            "suppression-region-nested",
                            (
                                f"this ignore-begin lands inside the region "
                                f"opened on line {region_line}; regions cannot "
                                "nest, so close that one first or widen its "
                                "rule list"
                            ),
                            line=lineno,
                        )
                    )
                    # Leave the outer region open on purpose. Registering this
                    # one would either hide the collision or hand the opener an
                    # "unclosed" complaint it did nothing to earn.
                    continue
                region_line = lineno
                region_rules = frozenset(rule_ids)
            elif kind == "ignore-end":
                if region_line is None:
                    errors.append(
                        ValidationMessage(
                            "suppression-pair-mismatch",
                            "ignore-end has no ignore-begin above it to close",
                            line=lineno,
                        )
                    )
                    continue
                if frozenset(rule_ids) != region_rules:
                    errors.append(
                        ValidationMessage(
                            "suppression-pair-mismatch",
                            (
                                f"this ignore-end names {sorted(rule_ids)} while "
                                f"the ignore-begin on line {region_line} named "
                                f"{sorted(region_rules)}; both ends of a region "
                                "have to name the same rules"
                            ),
                            line=lineno,
                        )
                    )
                    # The author clearly meant to close here, so close it. Left
                    # open, the opener would also collect an "unclosed"
                    # complaint, and the author would be chasing two lines for
                    # one mistake. Nothing is suppressed: the two ends disagree,
                    # so there is no agreement to apply.
                    region_line = None
                    region_rules = frozenset()
                    continue
                for target in range(region_line, lineno + 1):
                    for rid in rule_ids:
                        rid_map = suppressions.setdefault(target, {})
                        rid_map.setdefault(rid, set()).add("ignore-begin")
                for rid in rule_ids:
                    region_spans.append((region_line, lineno, rid))
                region_line = None
                region_rules = frozenset()
            elif kind == "ignore-file":
                for rid in rule_ids:
                    file_suppressions.append((rid, lineno))
            else:
                target = lineno + 1 if kind == "ignore-next-line" else lineno
                for rid in rule_ids:
                    rid_map = suppressions.setdefault(target, {})
                    rid_map.setdefault(rid, set()).add(kind)

        # warn when suppression directives are placed on a heading line. A
        # region opener is the exception: covering a heading with the lines
        # around it is the whole point of the pair.
        covering_line = [m for m in matches if m.group(1) not in _REGION_KINDS]
        if covering_line and HEADING_LINE_RE.search(line):
            errors.append(
                ValidationMessage(
                    "suppression-on-heading",
                    "suppression on a heading line; move it to the line above"
                    " and use ignore-next-line",
                    severity=Severity.WARNING,
                    line=lineno,
                )
            )

    if region_line is not None:
        errors.append(
            ValidationMessage(
                "suppression-pair-mismatch",
                (
                    f"the ignore-begin on line {region_line} is never closed; "
                    "add an ignore-end naming the same rules"
                ),
                line=region_line,
            )
        )

    front = parse_frontmatter(text)
    if not front:
        data = Frontmatter()
        body = text
        front = ""  # avoid NoneType errors in rules that inspect ctx.front
    else:
        # parse YAML frontmatter into our model; pydantic does not support YAML
        # natively so we use PyYAML (imported at module level) to pre-process.
        # This avoids silently dropping fields and ensures the validator sees
        # whatever tags/aliases the author provided.
        try:
            data = parse_yaml_raw_as(Frontmatter, front)
        except Exception:
            data = Frontmatter()

        # front_head was matched once already, while walking for fences
        body = text[front_head.end() :] if front_head else text

    # Parse the Markdown text (without YAML frontmatter) into an AST once,
    # so all rules can share the structured representation instead of each
    # rule re-parsing with regex.  Stripping frontmatter prevents mistune
    # (which has no frontmatter plugin) from misparsing YAML list items and
    # key-value pairs as Markdown lists/paragraphs, which would otherwise
    # produce spurious AST nodes.
    try:
        # Mistune returns untyped node dicts; its runtime shape is the
        # AstNode structure every rule consumes, so assert it once here
        # instead of re-narrowing at each rule.
        ast = cast("list[AstNode]", _MD(body))
    except Exception:
        ast = []

    # Extract session headings, cross-validated against AST positions
    session_headers = parse_session_headers(text, ast)

    ctx = ValidationContext(
        path=path,
        text=text,
        ast=ast,
        front=front,
        data=data,
        body=body,
        session_headers=session_headers,
    )

    for rid, rule in RULE_REGISTRY.items():
        try:
            errors.extend(await _collect_messages(rule(ctx)))
        except Exception as exc:  # pragma: no cover - defensive
            errors.append(
                ValidationMessage(
                    "validator-exception", f"exception in rule {rule.__name__}: {exc}"
                )
            )
            continue

    # before we actually apply the suppression filter, validate any rule IDs
    # in suppression directives.  If a rule ID is not registered then emit a
    # dedicated non-existent-rule message so users can fix typos.
    known_rule_ids = {rid for rid, _ in RULE_REGISTRY.items()}
    for target, rule_map in suppressions.items():
        for rid in rule_map:
            if rid not in known_rule_ids:
                errors.append(
                    ValidationMessage(
                        "suppression-non-existent-rule",
                        f"suppression references unknown rule {rid!r}",
                        line=target,
                    )
                )
    for rid, lineno in file_suppressions:
        if rid not in known_rule_ids:
            errors.append(
                ValidationMessage(
                    "suppression-non-existent-rule",
                    f"file-level suppression references unknown rule {rid!r}",
                    line=lineno,
                )
            )

    # check for redundant target coverage where the same rule is suppressed
    # by both ignore-line and ignore-next-line on the same target line.
    for target, rule_map in suppressions.items():
        for rid, kinds in rule_map.items():
            if "ignore-line" in kinds and "ignore-next-line" in kinds:
                errors.append(
                    ValidationMessage(
                        "suppression-conflict-line-next-line",
                        (
                            f"rule {rid!r} is suppressed by both ignore-line and "
                            f"ignore-next-line for line {target}; remove ignore-line "
                            "and keep ignore-next-line"
                        ),
                        line=target,
                    )
                )

    # before we actually apply the suppression filter, look for any
    # redundant directives.  A suppression is redundant when the target line
    # (for line/next-line suppressions) or the entire file (for file-level
    # suppressions) never produced an error with the given rule ID.  Emit an
    # error in that case so authors can clean up stale or misspelled comments.
    if suppressions or file_suppressions:
        active_pairs = {(m.line, m.rule_id) for m in errors if m.line is not None}
        active_rules = {m.rule_id for m in errors}
        # The exact lines a region covers, keyed by rule. Skipping whole rule
        # IDs instead would also spare every single-line suppression of the
        # same rule anywhere in the file, which is the next thing down.
        region_lines = {
            (line, rid)
            for start, end, rid in region_spans
            for line in range(start, end + 1)
        }
        # line- and next-line-specific suppressions
        for target, rule_map in suppressions.items():
            for rid in rule_map:
                # A rule covering a region is judged once per region below,
                # not once per line, or a working region would report
                # itself redundant on every line it silences.
                if rid not in known_rule_ids or (target, rid) in region_lines:
                    continue
                if (target, rid) not in active_pairs:
                    errors.append(
                        ValidationMessage(
                            "suppression-redundant",
                            f"suppression for rule {rid!r} on line {target} has no matching error",
                            line=target,
                        )
                    )
        # region suppressions, judged across the whole span
        for start, end, rid in region_spans:
            if rid not in known_rule_ids:
                continue
            silenced = any(
                m.line is not None and start <= m.line <= end and m.rule_id == rid
                for m in errors
            )
            if not silenced:
                errors.append(
                    ValidationMessage(
                        "suppression-redundant",
                        (
                            f"the region suppressing rule {rid!r} on lines "
                            f"{start}-{end} silenced nothing"
                        ),
                        line=start,
                    )
                )
        # file-level suppressions
        for rid, lineno in file_suppressions:
            if rid not in known_rule_ids:
                continue
            if rid not in active_rules:
                errors.append(
                    ValidationMessage(
                        "suppression-redundant",
                        (
                            f"file-level suppression for rule {rid!r} on line {lineno} "
                            "has no matching error in this file"
                        ),
                        line=lineno,
                    )
                )

    # apply suppression map: drop any errors whose line number matches and
    # whose rule ID appears in the suppression list for that line, or whose
    # rule ID appears in the file-level suppression list.  Messages without a
    # line number or whose rule isn't listed are kept.  Suppression map keys
    # come from comment parsing earlier.
    if suppressions or file_suppressions:
        file_level_ids = {rid for rid, _ in file_suppressions}
        filtered: list[ValidationMessage] = []
        for m in errors:
            # drop any message whose rule is suppressed for the entire file
            if m.rule_id in file_level_ids:
                continue
            if m.line is not None:
                ignore_for_line = suppressions.get(m.line, {})
                if m.rule_id in ignore_for_line:
                    continue
            filtered.append(m)
        errors = filtered

    return errors


async def _collect_messages(result: RuleResult) -> Sequence[ValidationMessage]:
    """Return the messages carried by *result*, awaiting async rules.

    *result* is the union of the sync and async rule return types.  Type
    narrowing cannot select the awaitable member of that union, so each
    branch asserts the member it consumes.
    """
    if isinstance(result, Awaitable):
        return await cast("Awaitable[Sequence[ValidationMessage]]", result)
    return cast("Sequence[ValidationMessage]", result)


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


async def main(argv: Sequence[str] | None = None) -> None:
    """Command-line entry point invoked by ``main.py``.

    By default the tool checks ``special/academia`` and
    ``private/special/academia``.  ``--json`` emits a machine-readable
    summary with ``errors`` and ``warnings`` arrays; warnings are normally
    empty under the current rule set.
    """
    parser = ArgumentParser(
        prog="main.py",
        description="Validate academic course notes (structural and content checks)",
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

    # sanity check: every registered rule id should match its function name.
    for rid, func in RULE_REGISTRY.items():
        if rid != func.__name__:
            _CONSOLE.print(
                f"[bold red]Internal error:[/] rule id {rid!r} does not match "
                f"function name {func.__name__!r}",
                markup=True,
            )
            return exit(3)

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
            return exit(2)
        if warning_items:
            return exit(1)
        return exit(0)

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
        return exit(2) if errcount else exit(1)

    _CONSOLE.print("[green]OK:[/] No issues detected", markup=True)
    return exit(0)
