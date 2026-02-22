# Continuous improvement — pyarchivist skill

This document describes the feedback loop for continuously improving the
`pyarchivist` skill, which handles archiving online content and
maintaining `index.md` files in `archives/`.

## Feedback procedure

1. Log user reports or issues in a central feedback file.
2. Add a lesson bullet below and, if necessary, adjust the pyarchivist
   documentation or index generation scripts.
3. Test by archiving representative content and verifying the resulting
   `index.md` entry (correct timestamp, URL, and filename).

## Lessons learned (2026‑02‑22 and earlier)

- Always verify that archived filenames are correct; mis‑named files can
  break relative links from notes.  If the default hash‑based name is
  unreadable, provide a descriptive alias explicitly.
- Ensure `index.md` is updated after every archive operation; manual
  edits must not conflict with the automatic metadata appended by the
  tool.
- Relative link encoding (`%20` for spaces) is important when referencing
  archived media from notes; the same rule applies across all skills.
- **Scheduling rules** from other skills (full weekday names, no topic on
  unscheduled) apply when pyarchivist is used to archive timetable data or
  schedules scraped from web pages.
- Run `pnpm run check:md` on affected index files after archiving to
  catch inadvertent markdown errors such as duplicate headings or
  misplaced YAML frontmatter.
- **2026‑02‑22 consolidation:** this document was added as part of a
  repo‑wide effort to place continuous‑learning notes in every skill
  directory.

---

Add more lessons here as new patterns or bugs are discovered.
