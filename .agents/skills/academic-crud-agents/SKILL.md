---
name: academic-crud-agents
description: Create, read, update, and delete course-level AGENTS.md files under special/academia/<INSTITUTION>/<COURSE>/.
---

# Academic CRUD: AGENTS.md

Course-level `AGENTS.md` files provide course-specific agent instructions and live at the course root.

## Target

`special/academia/<INSTITUTION>/<COURSE>/AGENTS.md`

## CRUD operations

### Create

1. Verify no `AGENTS.md` already exists in the course root; confirm with the user if one does.
2. Write the file with the required heading:

```markdown
# <COURSE CODE> agent instructions

<Course-specific rules and guidance>
```

The first heading must be exactly `# <COURSE CODE> agent instructions`. Keep the content concise and course-specific, and never add flashcard markup.

### Read

Show a course's current agent instructions.

### Update

1. Read the current file.
2. Apply the requested changes (add rules, update references, modify guidance).
3. Preserve the `# <COURSE CODE> agent instructions` heading.
4. Keep the file concise. Extract detailed rules into `.agents/instructions/` if they grow beyond ~30 lines.

### Delete

1. Confirm with the user.
2. Remove the file.
3. Remove the `[AGENTS](AGENTS.md)` link from the parent course `index.md` `## children` section (the validator requires this link when `AGENTS.md` exists).

## Rules

- First heading must be exactly `# <COURSE code> agent instructions`
- YAML frontmatter is allowed, commonly for `aliases` and `tags`
- No flashcard markup (`{@{ }@}`, `::@::`, `:@:`) in this file
- No PII, instructor names, or email addresses
- Keep concise, and reference other skills by name rather than embedding their rules
- If the file exceeds ~30 lines, split detailed rules into `.agents/instructions/` files
- Use `\[missing\]` for placeholder fields with absent values (see [special.instructions.md](../../instructions/special.instructions.md#missing-data))

## Validation

Run `academic-lint` after every edit. Pass the changed files when known; otherwise lint the whole course folder.

Give the rules you write the humanizer pass before validating: they are prose, and the AI patterns in the catalogue read as noise in a course's own instruction file (see "Humanizer pass" in `academic-ingest`).

## References

- `academic-crud-course-index` for course structure and index linkage
- `academic-lint` for validation
