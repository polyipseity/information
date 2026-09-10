---
name: academic-crud-agents
description: Create, read, update, and delete course-level AGENTS.md files under special/academia/<INSTITUTION>/<COURSE>/.
---

# Academic CRUD: AGENTS.md

Create, read, update, and delete course-level `AGENTS.md` files. These files provide course-specific agent instructions and live at the course root.

## Target

`special/academia/<INSTITUTION>/<COURSE>/AGENTS.md`

## CRUD operations

### Create

Scaffold a new `AGENTS.md` with the required heading and minimal structure.

1. Verify no `AGENTS.md` already exists in the course root (confirm with user if it does).
2. Write the file:

```markdown
# <COURSE CODE> agent instructions

<Course-specific rules and guidance>
```

1. The first heading must be exactly `# <COURSE CODE> agent instructions`.
2. Keep content concise and course-specific.
3. Do not add flashcard markup to this file.

### Read

Show the current agent instructions for a course. Read the file and present its contents.

### Update

Modify the guidance in an existing `AGENTS.md`.

1. Read the current file.
2. Apply requested changes (add rules, update references, modify guidance).
3. Preserve the `# <COURSE CODE> agent instructions` heading.
4. Keep the file concise. Extract detailed rules into `.agents/instructions/` if they grow beyond ~30 lines.

### Delete

Remove the `AGENTS.md` file.

1. Confirm with the user before deleting.
2. Remove the file.
3. Remove the `[AGENTS](AGENTS.md)` link from the parent course `index.md` `## children` section (the validator requires this link when `AGENTS.md` exists).

## Rules

- First heading must be exactly `# <COURSE code> agent instructions`
- YAML frontmatter is allowed and commonly used for `aliases` and `tags`
- No flashcard markup (`{@{ }@}`, `::@::`, `:@:`) in this file
- No PII, instructor names, or email addresses
- Keep concise. Reference other skills by name, not by embedding their rules
- If the file exceeds ~30 lines, split detailed rules into `.agents/instructions/` files

## Validation

Run `academic-lint` after every edit. If you know which files changed, pass those files specifically. Otherwise lint the whole course folder.

## References

- `academic-crud-course-index` — for course structure and index linkage
- `academic-lint` — validation
