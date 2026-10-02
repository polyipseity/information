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
| `academic-vision` | Images a material carries: classify a figure, read what only the picture shows, verify a drawing or crop before it reaches a note |
| `academic-video` | Videos a material links: read the content from the subtitles, defer the ones without usable subtitles, and ask the user to have those watched before the run ends |
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

- A line opens and closes with its content. `line_leading_whitespace` and `line_trailing_whitespace` report either, and a block tag counts as part of the edge, so a space just inside `<br/>` is the same defect as one just inside the line. An edge tag is legal only as one `<br/>` breaking to a line that continues the same block; `<p>` on an edge is padding.
- Use underscore-normalized flashcard tags: `flashcard/active/special/academia/HKUST/COMP_3031`.
  Spaces → underscores; keep consistent with institution/course code formatting.
- Do not put instructor or TA names or email addresses in course notes. Content quoted verbatim is the one case that keeps a visible mark: an instructor or TA name inside it is redacted as `\[redacted\]`, while anywhere else the name is omitted (see `../skills/academic-crud-course-index/SKILL.md`).
- Course-local `AGENTS.md` files must use heading `# <course code> agent instructions` and must not contain flashcard markup.
- Do not use chapter numbers as durable references in prose, flashcards, routes, or agent guidance. Use topic names and in-repo section links instead.
- Never narrate the source in a note: no `the deck`, `the slides`, `the lecture`, or `the course` as the subject of a sentence, and no reporting what a source shows or asks. State the fact, example, or question itself; provenance belongs to the course `index.md` session entries.
- Every edit to academic prose or flashcards — a note created, a late correction, one card rewritten — gets a writing pass before you report back: load `../skills/academic-writing/SKILL.md` for the order, then the `humanizer` skill for the surface patterns, and sweep the text that changed. Batching the pass to the end of a run is fine; returning to the user without it is not. Verbatim text and linked heading text are out of scope — see `../skills/academic-ingest/SKILL.md`.
- Prefer QA cards for topic notes; cloze only inside embedded accounting journal-entry worked examples.
- Questions-page solutions use cloze `{@{ }@}`, not QA cards.
- Within `lab.md`, `tutorial.md`, and `lecture.md`, one section carries one flashcard style: prose with `::@::`/`:@:` cards, or question blocks whose `- solution:`/`- explanation:` lines carry clozes. A prompt that is not a question is prose — see `../skills/academic-ingest/SKILL.md`.
- A section's cards belong to that section, whatever level its heading sits at: `---`, then `Flashcards for this section are as follows:`, then its own cards; cards under a child heading never answer for its parent. A `::@::`/`:@:` prompt names the specific thing recalled; a bare label such as `overview` is an error (`qa_prompt_generic`).
- When changing a topic note, update its prose, flashcards, and every affected `index.md` section link in the same task.
- Every ingestion reconciles the course's existing topic notes with the material, whatever its source (lecture, lab, tutorial, question set): extend, prune, create, or record each concept as already covered before validating. Work from the concepts the material develops, not the ones it names, since a durable concept needs a topic note and a passing mention does not. A topic the course barely reached gets the note the material supports, not the length the subject could support — see `../skills/academic-ingest/SKILL.md`.
- A drawing that defines a symbol, a convention, or a measurement setup is part of the definition: keep it in `attachments/`, embed it in the owning note, and card it both ways (shown for recognition, asked for as recall). Source it from Wikimedia Commons via pyarchivist when a suitable freely-licensed image exists, and only generate an SVG from a script when the search comes up empty; the generated set lives in one `attachments/generate_figures.py`. Look at every drawing and figure the material carries, and at whatever the notes take from them, before it is written about — see `../skills/academic-vision/SKILL.md`, `../skills/create-flashcards/SKILL.md`, and `../skills/academic-crud-attachments/SKILL.md`. A page render is never an attachment.
- A video link the material carries is part of the material, not a decoration: read the video's content from its subtitles, and when it has no usable English subtitles, defer it — write nothing about it, and ask the user once, at the very end of the run, to have it watched through Gemini (YouTube) or another tool that takes the file, so the content can be incorporated on the next pass — see `../skills/academic-video/SKILL.md`.
- A recurrent course (`- status: recurrent`, running every term) groups sessions by semester: a `## <YYYY term>` header, `### <YYYY term> week N <type> <number>` session headings, and `- status: optional` on every session, since none is assumed to be attended. See `../skills/academic-crud-course-index/SKILL.md`.
- Group notes and their sections by concept, never by the ingested material's layout: no note named after a lecture, chapter, or part, and no section named after a slide title. Nest to the depth the sub-concepts reach, since a deeper heading beats splitting one concept across files: `###` for a sub-concept the note's own concept raises, one that carries a card and a sentence of its own, flat for one the parent's prose absorbs or that only the source listed, and `####` when a `###` carries sub-concepts of its own, justified inline with a `check: ignore-line[header_deep_nesting]` comment — see `../skills/academic-crud-topic-note/SKILL.md` for that rule and for the levelling pass that re-reviews a written note before the humanizer pass, re-linking every session entry anchor a renamed, moved, or folded heading invalidates.

## Reference

- [special.instructions.md](special.instructions.md) — general special/ conventions
