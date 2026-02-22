# Continuous improvement — wiki-ingestion skill

This document describes the feedback loop for continuously improving the
`wiki-ingestion` skill.  Whenever the workflow or its documentation
receives feedback from the user, summarise the lesson here and update
examples or the SKILL.md accordingly.

## Feedback process

1. **Collect feedback.**  When the user reports a problem (broken link
   encoding, missing media, poor flashcard generation, etc.), note the
date and description in a persistent log (`reports/feedback_log.md` or
similar).
2. **Draft an edit.**  Add a concise bullet or paragraph below that
   documents the lesson, and if necessary modify the workflow steps or
   examples to prevent recurrence.
3. **Validate locally.**  Run the same commands the user would run and
   confirm the issue is resolved (e.g. ingest a sample page, inspect
   archive paths, run `uv run -m init generate`).  Check markdown with
   `pnpm run check:md` to ensure formatting remains valid.
4. **Present changes.**  Either create a PR or save a patch and attach it
   to the feedback note.  When the user approves, merge the update and
   close the feedback item.

## Lessons learned (2026‑02‑22 and earlier)

- When normalising links, always convert spaces to `%20`.  `%3A` or other
  encodings break relative‑path resolution.
- Ensure media downloads land in `archives/Wikimedia Commons/` with the
  expected filename; incorrect renames often stem from clipboard
garbled HTML.
- After ingestion, remember to run `uv run -m init generate <file>` so
  that any cloze markup added later produces flashcards; remind the user
  about this step in the workflow.
- Validate the final markdown with `markdownlint-cli2` to catch duplicate
  headings and other structural problems that can occur when pasting big
  blocks of HTML.
- **General formatting rules** from other skills also apply here: use
  full weekday names when the note contains a timetable, and omit `topic:`
  from any `status: unscheduled` row.  Consolidate these cross‑skill
  rules rather than repeating them in every workflow description.
- **2026‑02‑22 consolidation:** this document was added as part of a
  repo‑wide effort to place continuous‑learning notes in every skill
  directory.

---

Add new lessons below as the skill evolves.
