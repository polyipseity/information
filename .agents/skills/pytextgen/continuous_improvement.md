# Continuous improvement — pytextgen skill

This document describes the feedback loop for continuously improving the
`pytextgen` skill, which deals with programmatically-generated Markdown
content and the `init.py` wrapper.

## Feedback process

- Record feedback or bug reports in a log (`reports/feedback_log.md`).
- Update this document with descriptive lessons and modify the relevant
  tool or instructions accordingly.
- Validate by running the corresponding pytextgen commands (`init
  generate`, `init clear`) and by regenerating sample files.

## Lessons learned (2026‑02‑22 and earlier)

- Preserve all fence syntax exactly; even small deviations in
  `# pytextgen generate ...` comments break regeneration.
- Use `--no-code-cache` when debugging mysterious failures—stale
  compiled modules in `__pycache__/` are a common trap.
- When adding schedule-related generators (course indexes, lecture
  tables), standardise on full weekday names and embedded ISO datetime
  intervals so other skills can parse them reliably.
- Session entries flagged `status: unscheduled` should not include a
  `topic:` field; generators that produce filler rows must omit the
  topic to avoid clutter.
- Always run `bun run check:md` on files before committing; duplicate
  headings and other markdown errors often originate from generated
  output.
- Include explicit public‑holiday rows rather than skipping them; the
  `init.py` wrapper and other tools rely on their presence for accurate
  week numbering.
- **2026‑02‑22 consolidation:** this document was added as part of a
  repo‑wide effort to place continuous‑learning notes in every skill
  directory.

---

New improvements can be added below as the skill evolves.
