---
name: academic-crud-index
description: Create, read, update, and delete sub-directory index.md pages (assignments/index.md, questions/index.md, labs/index.md, etc.). Shared utility used by other academic-crud-* skills.
---

# Academic CRUD: Index pages

Create, read, update, and delete sub-directory `index.md` files. Other `academic-crud-*` skills call this one when they need a sub-directory index.

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

- `aliases`: cover institution + course + type combinations, both short and long forms (for HKUST COMP 3031: `HKUST COMP 3031 assignment`, `HKUST COMP3031 assignments`, `COMP 3031 assignment`, and so on). Keep them exhaustive, and accept that generic aliases repeat across notes: notes link by relative path, never by `[[wikilink]]`, so a duplicate elsewhere is not a defect.
- `tags`: include the `flashcard/active/...` path (underscore-normalized), `function/index`, and `language/in/<lang>`.

### Children format

- One bullet per child, linking to the child's `index.md` for submission pages or directly to the file for question pages
- Submission leaf indexes may also list in-class content files (`lab.md`, `tutorial.md`, `lecture.md`) as children
- __Order__: folders first, then files, each group sorted by Python string order of the destination path, never chronologically or by teaching order. The `index_children_order` rule enforces this; `AGENTS.md` sorts before `Arduino.md` because uppercase sorts first.
- __Folder entries__: write the link and its display text with a trailing slash (`- [assignments/](assignments/index.md)`, `- [attachments/](attachments/)`).
- __Encoding__: encode spaces as `%20` and keep every other character literal, parentheses included, so `cache (computing).md` is linked as `- [cache (computing)](cache%20(computing).md)`.

```markdown
## children

- [assignments/](assignments/index.md)
- [questions/](questions/index.md)
- [AGENTS](AGENTS.md)
- [cache (computing)](cache%20(computing).md)
- [cloud computing](cloud%20computing.md)
```

> __Note:__ This skill defines the directory listing index (e.g., `tutorials/index.md`). Individual submission pages (e.g., `tutorials/tutorial 1/index.md`) follow the format in `academic-crud-submission`.

## Missing data

Use `\[missing\]` for fields with absent values (see [special.instructions.md](../../instructions/special.instructions.md#missing-data)).

## CRUD operations

### Create

1. Verify no `index.md` already exists in the target directory.
2. Write the file using the format above.
3. The parent course `index.md` should already link to this subdirectory (added by `academic-crud-course-index`).

### Read

List the subdirectory's children by reading its `index.md`.

### Update

1. Read the current `index.md`.
2. Apply changes:
   - __Add__: insert the bullet in its correct position (folders first, then files, Python string order within each group).
   - __Remove__: delete the bullet and verify the child file no longer exists, or remove it too.
   - __Reorder__: reorder bullets to match that order.
3. Preserve frontmatter exactly and modify only `## children`.

### Delete

1. Confirm whether to delete the entire subdirectory or just the index.
2. Index only: remove `index.md` and leave child files intact.
3. Entire subdirectory: remove it recursively and remove its link from the course root `index.md`.

## Callers

Other `academic-crud-*` skills create or update index pages as part of their workflows:

- `academic-crud-course-index` creates subdirectory indexes when setting up a new course
- `academic-crud-submission` adds child links when creating submission pages, including in-class content file links (`lab.md`, `tutorial.md`, `lecture.md`)
- `academic-crud-question` adds child links when creating question pages

The calling skill supplies the target path, child name, and child link path; this skill supplies the format and structure.

## Validation

Run the humanizer pass over new or changed prose and flashcards, focusing on the description paragraph and prose above `## children` (see "Humanizer pass" in `academic-ingest`). Then run `academic-lint`, passing changed files when known.

## References

- `academic-crud-course-index/course-template.md` for the new-course `index.md` scaffold
- `academic-crud-course-index` for subdirectory and index creation
- `academic-crud-submission` for adding submission pages to indexes
- `academic-crud-question` for adding question pages to indexes
- `humanizer` for the AI-writing patterns it removes (see "Humanizer pass" in `academic-ingest`)
- `academic-lint` for validation
