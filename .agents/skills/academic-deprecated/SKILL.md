---
name: academic-deprecated
description: >
  Documents deprecated academic material patterns that still exist in legacy
  content. DO NOT use these patterns for new content. This skill is
  documentation-only — active skills should not reference it.
---

# Academic Deprecated Patterns

> __⚠️ DO NOT use these patterns for new content.__ This skill documents legacy patterns that exist in the repository but should not be created for new courses. When updating existing content with these patterns, migrate to the active pattern when practical.

## Deprecated patterns

### 1. Flat assignment directories at course root

__Pattern:__ Assignment, homework, or lab directories placed directly at the course root instead of inside a parent `assignments/` or `labs/` directory.

__Examples:__

- CIVL 1100: `assignment I.1/`, `assignment I.2/`, `assignment II.1/`
- COMP 1942: `homework 1/`, `homework 2/`, `project/`
- COMP 2011: `assignment 1/`, `lab 1/`, `lab 2/`

__Use instead:__ `assignments/<name>/` for unbound work, `labs/<name>/` for labs, `tutorials/<name>/` for tutorials.

### 2. Flat `questions.md` file

__Pattern:__ A single `questions.md` file at the course root containing inline questions organized by `##` sections, instead of individual files in a `questions/` directory.

__Examples:__

- FINA 2303, ECON 2103, ACCT 2200, ACCT 2010, MATH 2023, PHYS 1314
- ACCT 3020, ACCT 3010, FINA 3103, COMP 2211, ELEC 4110, FINA 3203
- COMP 1942, PHYS 1002

__Use instead:__ `questions/<name>.md` for individual question pages, or `questions/<name>/index.md` for multi-page question sets.

__Why deprecated:__ Flat files grow unwieldy with many questions, prevent per-question metadata (tags, aliases), and make it harder to link to specific questions.

### 3. `transcripts/` directory

__Pattern:__ A `transcripts/` directory containing lecture transcript files (PDF-to-markdown conversions).

__Examples:__

- CIVL 1100: `transcripts/I-4.1 History of civil engineering and Infrastructure.pdf.md`

__Use instead:__ Topic notes for authored content, or `transcludes/` for Wikipedia-derived content.

__Why deprecated:__ Transcripts are source-derived content that duplicates topic notes. They add maintenance burden without clear benefit over well-structured topic notes.

## Migration guidance

When updating content with deprecated patterns:

1. __Flat assignment dirs__ → Move contents into `assignments/<name>/` or `labs/<name>/` and add an `index.md`.
2. __Flat `questions.md`__ → Split into individual `questions/<name>.md` files with frontmatter.
3. __`transcripts/`__ → Convert to topic notes or `transcludes/` entries.

Only migrate when the content is being actively updated. Do not migrate solely for cleanup.

## Rules

- Do NOT create new content using these patterns
- Do NOT reference this skill from active skills — it is documentation-only
- Do NOT add new deprecated patterns without explicit user approval
- When migrating, preserve all existing content and flashcards

## References

- `academic-crud-course-index` — active course structure patterns
- `academic-crud-question` — active question patterns
- `academic-crud-submission` — active submission patterns
- `academic-crud-transcludes` — active transcludes pattern
