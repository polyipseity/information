---
name: Academic notes conventions
description: Guidelines and automated checks for files under special/academia (institution-agnostic)
applyTo: "special/academia/**,private/special/academia/**"
---

# Academic notes instruction

For all academic material ingestion, start with the `academic-ingest` dispatcher skill. It classifies input and routes to the correct CRUD skill.

- Read `../skills/academic-ingest/SKILL.md` as the entry point for all ingestion.
- Read `../skills/academic-crud-course-index/course-template.md` as the scaffold for new course indexes.
- The validator is at `.agents/skills/academic-lint/main.py`; run `academic-lint` to validate after editing.

## Skills

| Skill | Purpose |
| --- | --- |
| `academic-ingest` | Dispatcher — classify input, resolve course, route to CRUD skill |
| `academic-lint` | Validate academic notes after edits (wraps main.py) |
| `academic-crud-course-index` | Top-level `index.md`, exams, logistics, course scaffolding |
| `academic-crud-index` | Sub-directory `index.md` (shared utility) |
| `academic-crud-submission` | Labs, tutorials, lectures, assignments (shared hierarchy) |
| `academic-crud-topic-note` | Standalone concept and lecture notes |
| `academic-crud-question` | Problem sets, iPRs, quizzes (no submission) |
| `academic-crud-agents` | Course-level `AGENTS.md` files |
| `academic-crud-attachments` | Attachments directories at any level |
| `academic-crud-transcludes` | Wikipedia articles included by reference |
| `academic-deprecated` | Deprecated patterns (documentation-only) |
| `create-flashcards` | Flashcard markup (referenced by other skills) |

## Cross-cutting rules

- Use underscore-normalized flashcard tags: `flashcard/active/special/academia/HKUST/COMP_3031`.
  Spaces → underscores; keep consistent with institution/course code formatting.
- Do not put instructor or TA names or email addresses in course notes.
- Course-local `AGENTS.md` files must use heading `# <course code> agent instructions` and must not contain flashcard markup.
- Do not use chapter numbers as durable references in prose, flashcards, routes, or agent guidance. Use topic names and in-repo section links instead.
- Prefer QA cards for topic notes; cloze only inside embedded accounting journal-entry worked examples.
- Questions-page solutions use cloze `{@{ }@}`, not QA cards.
- When changing a topic note, update its prose, flashcards, and every affected `index.md` section link in the same task.

## Reference

- [special.instructions.md](special.instructions.md) — general special/ conventions
