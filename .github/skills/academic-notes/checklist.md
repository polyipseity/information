# Academic notes author checklist (detailed)

Before committing a new or updated course note under `special/academia`, run through this checklist.

Required (must-have) ✅

1. YAML frontmatter exists and is delimited by `---` at top of file.
2. `aliases` include the canonical course code and a human-readable name (for `index.md`).
3. `tags` include `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` (required in course note files where flashcards are desired).
   - Note: flashcards are regenerated automatically; you never need (and an
     agent must never attempt) to run `init generate` manually when editing
     notes.
4. Do NOT create, modify, or edit files under `general/`. Course-note authors and agents must only edit files inside the course folder.
5. `# index` present for `index.md` files.
6. `## children` lists child pages in teaching order (or a `children:` YAML key).  Make sure folders appear first; file entries should follow only after all folder links, regardless of alphabetical order. (This mirrors most file explorers and aids human navigation.)
7. Each `week` entry has `datetime` and `topic` (recommended to include timezone offset).  Use ISO‑8601 format for all date, time, and datetime values to avoid parsing errors.  When a session has `status: unscheduled` (holiday, cancelled, overflow), remove the `topic:` field entirely; the validator warns if both appear.
8. **Ordering rules**: lecture/lab/tutorial entries must follow chronological order; exams must come after all other sessions (validator will warn on violations).  For courses with multiple sessions per week, restart numbering each week after filtering irrelevant streams.  If a timetable uses the same week number twice (e.g. around a holiday), shift subsequent weeks upward and insert an entry with `status: public holiday`.
9. Semester headings in institution-level indexes must be chronologically ordered (validator warns if not).

Recommended (helpful) ⚠️
8. Use `assignments/`, `questions/`, and `attachments/` subfolders for respective content.
9. Link to `general/` canonical pages instead of copying long definitions.
10. Filenames are friendly and human-readable; use spaces and percent-encode when needed for links.
10. Run `python .github/skills/academic-notes/validate_academic.py` to detect common errors; use `--content` for guidance on minimal content signals.  (The script now warns about unscheduled sessions with topics, duplicate week numbers, missing venues, and exam placement.)

Content checklist (content-first guidance):
12. **Details matter.**  Treat each slide bullet, spoken remark, formula, and
    example as content to capture.  If a slide presents three bullet points,
    make three separate notes.  Include explanations, numerical values,
    algorithmic steps, and any instructor warnings or ``gotchas``.  Aim to make
    the notes self‑contained so a reader could reconstruct the lecture flow
    without seeing the slides.  If uncertain how much to include, lean towards
    including more; excess material can be pruned in a follow-up review.
13. Each lecture/tutorial **may** include outcomes captured in prose or via flashcards.)  Capture instructor emphasis and worked examples when possible.
14. For lists intended for memorization (features, characteristics), collapse
    them into a single gloss line with hyphens and `<br/>` separators rather
    than multi-line sub-bullets.
    Where appropriate, link outline items to sections of an external
    topic-specific note using anchor references (e.g. `electronic%20component.md#atoms%20and%20charge`).
15. After the bullet outline for a session, add a prose paragraph (preceded by
    `---`) containing administrative comments such as schedule links, next‑week
    reminders, grading breakdowns, and other logistics.  The week‑1 lecture
    example in this file demonstrates how a single prose block can carry all of
    the course logistics without polluting the outline.  Use cloze markup within
    that paragraph if you wish to generate flashcards from the commentary.
    **Do not update earlier lecture paragraphs when adding new lectures; keep
    summaries focused on that session only.**
16. Ensure every outline item you add corresponds to a flashcard pair; convert generic headings into specific cloze entries or remove them if they are not pairs.
17. Keep all outline/list items on a single source line; use `<br/>` or `<p>` for internal line breaks or paragraphs.
    // mathematical equations should always use `$…$` or `$$…$$` delimiters;
    avoid TeX-style `\(\)`/`\[\]` which are not supported by some renderers.
18. When writing `::@::` clozes, use short left-hand labels (avoid long descriptive phrases) and always start the path with an explicit hierarchy (e.g. `<COURSE> / topic`).  For complex topics you may introduce multiple-folder levels (`<COURSE> / section / subsection / item`).  Repeat the full path text on every gloss even if it appears as a nested bullet; this ensures context is preserved when cards are generated.
17. Do NOT include instructor/TA/IA/TO names, office locations, phone numbers or email addresses in notes; refer to the official syllabus or LMS instead. Replace any existing personal names with generic role descriptions; do not annotate that they were removed.
18. Include at least one worked example or solution sketch for important techniques covered that week (recommended).
19. Link slides and recordings in `attachments/` or `attachments/index.md` when available (recommended).
20. Add `::@::` concise definitions for flashcard-worthy items and check `flashcards.md` rules (recommended).
21. Record your lab/tutorial **section identifiers** near the top of the note so automated tooling can filter irrelevant streams when importing schedules.
22. Ensure venue lines follow immediately after `datetime:`; apply the HKUST room interpretation rule if appropriate (numeric rooms → "Room ####, Academic Building").

Note on existing inline idioms:

- Many notes use `term ::@:: gloss` or `takeaway ::@:: ...` inline inside the session body. This is acceptable; prefer converting these into structured `- topic:` entries in a follow-up PR rather than making large automatic rewrites. When suggesting normalization, list affected files in the PR description so maintainers can review changes.

Commit-msg tip: include `academic-notes: add <INSTITUTION>/<COURSE> ...` for changes that modify course content or introduce new course notes.

Run the validator in content mode to get guidance on minimal content signals:

```bash
python .github/skills/academic-notes/validate_academic.py --content special/academia/<INSTITUTION>
```

See also: `issue_frequencies.md` for a recent frequency summary of validator findings and quick remediation notes (auto-generated from a validator run).
