---
name: academic-deprecated
description: >
  Documents deprecated academic material patterns that still exist in legacy
  content. DO NOT use these patterns for new content. This skill is
  documentation-only: active skills may cite it only to warn against a
  deprecated pattern or to point to the fix.
---

# Academic Deprecated Patterns

> __DO NOT use these patterns for new content.__ This skill documents legacy patterns that exist in the repository. When updating existing content that uses one, migrate to the active pattern when practical.

## Deprecated patterns

### 1. Flat assignment directories at course root

Assignment, homework, or lab directories placed directly at the course root instead of inside a parent `assignments/` or `labs/` directory.

Examples: CIVL 1100 (`assignment I.1/`, `assignment I.2/`, `assignment II.1/`), COMP 1942 (`homework 1/`, `homework 2/`, `project/`), COMP 2011 (`assignment 1/`, `lab 1/`, `lab 2/`).

Use `assignments/<name>/` for unbound work, `labs/<name>/` for labs, and `tutorials/<name>/` for tutorials.

### 2. Flat `questions.md` file

A single `questions.md` at the course root holding inline questions under `##` sections, instead of individual files in a `questions/` directory.

Examples: FINA 2303, ECON 2103, ACCT 2200, ACCT 2010, MATH 2023, PHYS 1314, ACCT 3020, ACCT 3010, FINA 3103, COMP 2211, ELEC 4110, FINA 3203, COMP 1942, PHYS 1002.

Use `questions/<name>.md` for individual question pages, or `questions/<name>/index.md` for multi-page sets.

Flat files grow unwieldy with many questions, prevent per-question metadata (tags, aliases), and make specific questions hard to link.

### 3. `transcripts/` directory

A `transcripts/` directory holding lecture transcripts (PDF-to-markdown conversions), such as CIVL 1100's `transcripts/I-4.1 History of civil engineering and Infrastructure.pdf.md`.

Use topic notes for authored content, or `transcludes/` for Wikipedia-derived content. Transcripts duplicate topic notes and add maintenance burden without a clear benefit.

## Migration guidance

1. Flat assignment dirs → move contents into `assignments/<name>/` or `labs/<name>/` and add an `index.md`.
2. Flat `questions.md` → split into individual `questions/<name>.md` files with frontmatter.
3. `transcripts/` → convert to topic notes or `transcludes/` entries.

Migrate only content that is being actively updated; do not migrate solely for cleanup.

## Rules

- Do not create new content with these patterns
- Reference this skill from active skills only to warn against a deprecated pattern or to point to the fix, never as an active convention
- Do not add new deprecated patterns without explicit user approval
- When migrating, preserve all existing content and flashcards

## References

- `academic-crud-course-index` for active course structure patterns
- `academic-crud-question` for active question patterns
- `academic-crud-submission` for active submission patterns
- `academic-crud-transcludes` for the active transcludes pattern
