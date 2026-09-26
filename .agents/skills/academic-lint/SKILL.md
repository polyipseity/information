---
name: academic-lint
description: 'Validate academic course notes after edits. Wraps main.py validator with two modes: whole-course or specific-files.'
---

# Academic Lint

Wraps the `main.py` validator and defines when and how to run it.

## When to run

Run it after every edit to academic notes under `special/academia/`. Do not skip validation before committing.

Validation is the __last__ step of an edit. The humanizer pass runs first (see "Humanizer pass" in `academic-ingest`): rewriting a card can strand a suppression with nothing to suppress, or create a warning that now needs one, and only the validator can show that.

## Invocation modes

### Specific files (preferred when known)

When you know which files were edited, lint those files only:

```bash
uv run python .agents/skills/academic-lint/main.py <file1> <file2> ...
```

### Whole-course (default)

When the whole course folder changed (scaffolding a new course, batch updates), lint the entire course:

```bash
uv run python .agents/skills/academic-lint/main.py "special/academia/<INSTITUTION>/<COURSE>/"
```

## Exit codes

- `0`: no issues
- `1`: warnings only, advisory, fix when practical
- `2`: errors found, must fix before commit

## Blind spots

A clean run is a shape check, not a content check, and a value that is internally consistent but wrong still passes. `session_datetime_order` compares the `datetime:` values as written, so it cannot tell a session carrying another section's weekday, time, or venue; no rule compares a session against the section recorded in `## logistics`, or an ordinal against the sessions around it in its week. A `status: no class` session holding a wrong slot is as invisible to the linter as a correct one. Verifying those is the author's job, against the source, per "Session ordering" and "Validation" in `academic-crud-course-index`.

In a whole-course run the warnings can come from files the task never touched. Re-run on the edited file to tell a pre-existing warning from an introduced one, and report the pre-existing ones instead of fixing them.

## Options

- `--json`: machine-readable output
- `--max-per-rule N`: limit per-rule output (default 5, 0 for unlimited)

## Sibling tools

These files live alongside `main.py` in the `academic-lint/` directory:

| Tool | Purpose |
| --- | --- |
| `main.py` | Entry point for the validator CLI |
| `main_mods/` | Validation rules, models, and registry |
| `tests_a7392be/` | Validator test suite |

## References

- All `academic-crud-*` skills run this after edits
