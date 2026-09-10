---
name: academic-crud-attachments
description: Manage attachments directories at any level (course root, questions/, submission-level). Attachments hold raw files (PDFs, images, data, scripts) referenced by Markdown notes.
---

# Academic CRUD: Attachments

Manage `attachments/` directories at any level of the course hierarchy. Attachments hold raw files — PDFs, images, SVGs, CSVs, Python scripts, Java files, and other non-Markdown content — that are referenced by Markdown notes.

## Scope

Attachments can appear at multiple levels:

- __Course-root `attachments/`__: Cheatsheets, exam data, analysis scripts, diagrams (18+ courses)
- __Submission-level `attachments/`__: Prompt PDFs, data files, template code (labs, assignments)
- __Questions-level `attachments/`__: Images for questions, data files for problem sets
- __Any other directory level__ where raw files need to be stored alongside Markdown

## Key rules

- `attachments/` should NOT have `index.md` (per validator rule `index_children_missing_index`)
- Link from parent `## children` as `[attachments/](attachments/)` or as individual file links
- Contents are raw files (PDF, PNG, SVG, CSV, Python, Java, etc.), not Markdown notes
- Use `%20` encoding for spaces in filenames when linking
- Missing-data indicator `(none)` rarely applies here — files either exist or don't. See [special.instructions.md](../../instructions/special.instructions.md#missing-data)

## Creating or updating attachments

### Add files to an existing `attachments/` directory

1. Place the file in the `attachments/` directory.
2. Add a child link in the parent `index.md` if not already present:
   - Directory link: `- [attachments/](attachments/)`
   - Individual file link: `- [\`filename.pdf\`](attachments/filename.pdf)`

### Create a new `attachments/` directory

1. Create the `attachments/` directory.
2. Place files inside it.
3. Add a child link in the parent `index.md` `## children` section.

## Linking to attachments

Use relative paths with `%20` encoding for spaces:

```markdown
- [\`cheatsheet.pdf\`](attachments/cheatsheet.pdf)
- [attachments/](attachments/)
```

For course-root attachments linked from `index.md`:

```markdown
## children

- [assignments/](assignments/)
- [attachments/](attachments/)
```

## Examples

### Course-root attachments (ELEC 4110)

```markdown
## children

- [\`final examination cheatsheet.pdf\`](attachments/final%20examination%20cheatsheet.pdf)
- [transcludes/](transcludes/)
```

### Questions-level attachments (COMP 2711H)

```markdown
## children

- [attachments/](attachments/)
- [midterm 1 practice problem set.md](midterm%201%20practice%20problem%20set.md)
```

## Validation

Run `academic-lint` after every edit. If you know which files changed, pass those files specifically. Otherwise lint the whole course folder.

## References

- `academic-crud-course-index` — course-root attachments in `## children`
- `academic-crud-submission` — submission-level attachments
- `academic-crud-question` — questions-level attachments
- `academic-lint` — validation (rule `index_children_missing_index` forbids `index.md` in `attachments/`)
