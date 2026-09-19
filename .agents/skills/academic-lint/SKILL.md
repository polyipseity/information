---
name: academic-lint
description: 'Validate academic course notes after edits. Wraps main.py validator with two modes: whole-course or specific-files.'
---

# Academic Lint

Wraps the `main.py` validator and defines when and how to run it.

## When to run

Run it after every edit to academic notes under `special/academia/`. Do not skip validation before committing.

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
