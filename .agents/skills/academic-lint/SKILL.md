---
name: academic-lint
description: Validate academic course notes after edits. Wraps main.py validator with two modes: whole-course or specific-files.
---

# Academic Lint

Validate academic course notes after every edit. This skill wraps the `main.py` validator and defines when and how to run it.

## When to run

Run this skill after every edit to academic notes under `special/academia/`. Do not skip validation before committing.

## Invocation modes

### Specific files (preferred when known)

When you know which files were edited, lint those files only:

```bash
uv run .agents/skills/academic-lint/main.py <file1> <file2> ...
```

### Whole-course (default)

When the full course folder was modified (e.g., scaffolding a new course, batch updates), lint the entire course:

```bash
uv run .agents/skills/academic-lint/main.py "special/academia/<INSTITUTION>/<COURSE>/"
```

## Exit codes

- `0` — no issues
- `1` — warnings only (advisory; fix when practical)
- `2` — errors found (must fix before commit)

## Behavior

- Report errors clearly with file paths and line numbers
- Do not proceed to commit until errors are resolved
- Warnings are advisory; fix when practical but do not block
- Use `--json` for machine-readable output when needed
- Use `--max-per-rule N` to limit per-rule output (default 5, 0 for unlimited)

## Sibling tools

These files live alongside `main.py` in the `academic-lint/` directory:

| Tool | Purpose |
| --- | --- |
| `main.py` | Entry point for the validator CLI |
| `main_mods/` | Validation rules, models, and registry |
| `course-template.md` | Scaffold template for new course `index.md` files |
| `find_wikipedia.py` | Wikipedia search for canonical `general/` note titles |
| `tests_a7392be/` | Validator test suite |

## References

- `academic-crud-course-index` uses `course-template.md` for scaffolding
- `academic-crud-topic-note` uses `find_wikipedia.py` for canonical titles
- All `academic-crud-*` skills run this after edits
