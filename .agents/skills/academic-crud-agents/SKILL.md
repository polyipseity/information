---
name: academic-crud-agents
description: Create, read, update, and delete course-level AGENTS.md files under special/academia/<INSTITUTION>/<COURSE>/.
---

# Academic CRUD: AGENTS.md

A course-level `AGENTS.md` holds what an agent needs to know about one course, and nothing that another course already says. It lives at the course root, beside `index.md`.

## Target

`special/academia/<INSTITUTION>/<COURSE>/AGENTS.md`

## Rules

- The first heading is exactly `# <COURSE CODE> agent instructions`, and it survives every later edit.
- YAML frontmatter is allowed (`aliases` and `tags` are the usual keys).
- No flashcard markup (`{@{ }@}`, `::@::`, `:@:`).
- No PII, no instructor or TA names, no email addresses.
- Course-specific and short. Reference another skill by name rather than copying its rules, and once the file passes ~30 lines, move the detail into `.agents/instructions/`.
- `\[missing\]` for a field that exists with no value (see [special.instructions.md](../../instructions/special.instructions.md#missing-data)).

## CRUD operations

### Create

1. Verify no `AGENTS.md` already exists in the course root; confirm with the user if one does.
2. Write a file that satisfies the rules above:

```markdown
# <COURSE CODE> agent instructions

<Course-specific rules and guidance>
```

### Read

Show a course's current agent instructions.

### Update

1. Read the current file.
2. Apply the requested changes (add rules, update references, modify guidance).
3. Check the result against the rules above, then validate.

### Delete

1. Confirm with the user.
2. Remove the file.
3. Remove the `[AGENTS](AGENTS.md)` link from the parent course `index.md` `## children` section (the validator requires this link when `AGENTS.md` exists).

## Validation

Run `academic-lint` after every edit, passing changed files when known.

Give the rules you write the humanizer pass first. The catalogue's patterns read as noise in a course's own instruction file, where every sentence has to earn its place (see "Humanizer pass" in `academic-ingest`).

## References

- `academic-crud-course-index` for course structure and index linkage
- `academic-lint` for validation
