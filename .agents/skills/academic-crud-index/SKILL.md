---
name: academic-crud-index
description: Create, read, update, and delete sub-directory index.md pages (assignments/index.md, questions/index.md, labs/index.md, etc.). Shared utility used by other academic-crud-* skills.
---

# Academic CRUD: Index pages

Create, read, update, and delete sub-directory `index.md` files. This is a shared utility. Other `academic-crud-*` skills call it when they need to create or update a sub-directory index.

## Target

`<subdirectory>/index.md` (e.g., `assignments/index.md`, `questions/index.md`, `labs/index.md`, `tutorials/index.md`, `lectures/index.md`)

## Index format

All sub-directory indexes follow the same structure:

```markdown
---
aliases:
  - <INSTITUTION> <COURSE> <type>
  - <INSTITUTION> <COURSE> <type plural>
tags:
  - flashcard/active/special/academia/<INSTITUTION>/<COURSE>/<type>
  - function/index
  - language/in/English
---

# index

- <INSTITUTION> <COURSE>

## children

- [<name>](<name>/index.md)
```

### Frontmatter rules

- `aliases`: cover institution + course + type combinations (both short and long forms)
- `tags`: include `flashcard/active/...` path (underscore-normalized), `function/index`, and `language/in/<lang>`
- Keep aliases exhaustive. Cover `HKUST COMP 3031 assignment`, `HKUST COMP3031 assignments`, `COMP 3031 assignment`, etc.

### Children format

- One bullet per child, linking to the child's `index.md` (for submission pages) or directly to the file (for question pages)
- Submission leaf indexes may also link to in-class content files (`lab.md`, `tutorial.md`, `lecture.md`) as children when the in-class component exists
- Use `%20` encoding for spaces in links
- Order: chronological for sessions/assignments, alphabetical for topics

## CRUD operations

## Missing data

Use `(none)` for metadata fields with absent values in index pages. See [special.instructions.md](../../instructions/special.instructions.md#missing-data).

### Create

Scaffold a new sub-directory index.

1. Verify no `index.md` already exists in the target directory.
2. Write the file using the format above.
3. The parent course `index.md` should already link to this subdirectory (added by `academic-crud-course-index`).

### Read

List children of a subdirectory by reading its `index.md`.

### Update

Add, remove, or reorder child links.

1. Read the current `index.md`.
2. Apply changes:
   - __Add:__ insert a new bullet in the correct position (chronological or alphabetical).
   - __Remove:__ delete the bullet and verify the child file still exists (or remove it too).
   - __Reorder:__ reorder bullets to match the desired order.
3. Preserve frontmatter exactly. Only modify the `## children` section.

### Delete

Remove the index and optionally the entire subdirectory.

1. Confirm with user whether to delete the entire subdirectory or just the index.
2. If just the index: remove `index.md`, leave child files intact.
3. If entire subdirectory: remove recursively, and remove the subdirectory link from the course root `index.md`.

## When other skills call this

Other `academic-crud-*` skills create or update index pages as part of their workflows:

- `academic-crud-course-index` creates subdirectory indexes when setting up a new course
- `academic-crud-submission` adds child links when creating submission pages, including in-class content file links (`lab.md`, `tutorial.md`, `lecture.md`)
- `academic-crud-question` adds child links when creating question pages

The calling skill provides: target path, child name, child link path. This skill provides the format and structure.

## Validation

Run `academic-lint` after every edit. If you know which files changed, pass those files specifically. Otherwise lint the whole course folder.

## References

- `academic-crud-course-index/course-template.md` scaffold template for new course `index.md` files
- `academic-crud-course-index` creates subdirectories and their indexes
- `academic-crud-submission` adds submission pages to indexes
- `academic-crud-question` adds question pages to indexes
- `academic-lint` validation
