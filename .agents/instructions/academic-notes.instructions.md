---
name: Academic notes conventions
description: Guidelines and automated checks for files under special/academia (institution-agnostic)
applyTo: "special/academia/**,private/special/academia/**"
---

# Academic notes instruction

This instruction file surfaces the essential, quick-reference guidance from the `academic-notes` skill for agents and maintainers working on course folders under `special/academia` (including the private mirror path `private/special/academia`). **Agents must read every file in `.agents/skills/academic-notes/` and every line of those files before acting; do not assume the concise guidance is exhaustive.** It is intentionally concise — consult the full skill docs for examples and tooling.

## Scope & purpose

- Applies to: `special/academia/**` and mirrored `private/special/academia/**` course folders.
- Purpose: give agents a compact checklist for authoring, validating, and triaging course notes using the `academic-notes` conventions and helpers.

## Quick guidance for agents

- Do NOT create or edit `general/` files automatically. Suggest canonical Wikipedia titles (use the helper) and leave `general/` edits to maintainers.
- Require a flashcard activation tag in course files: `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` (case-insensitive). The validator will flag missing tags. Notes may use any of the three markup types – cloze `{@{ }@}`, two-sided `::@::`, or one-sided `:@:` – but remember that the latter two must stay on a single line.  **Do not trim prompts for calculations**; the warning rules exist to catch missing numeric/symbolic data, not to enforce brevity.  You may write arbitrarily long equations or value lists before the separator; splitting a single logical example into multiple cards just to shorten the left-hand text is counter‑productive. When converting prose or examples into flashcard bullets, also copy any relevant diagrams or images from the paragraph above and include them in the question text – the validator will remind you if an image appears in the source but not in the card. A suppression directive is permitted only when the card truly tests a conceptual fact (e.g. `<!-- check: ignore-line[two_sided_calc_warning]: conceptual -->`).
- Prefer **single-focus flashcards** for conceptual material: if a card answers multiple distinct points, split it into multiple smaller cards. Keep calculation cards self-contained on the left-hand side (do not delete givens just to shorten prompts).
- When embedding LaTeX, always use `$...$` for inline math and `$$...$$` for display equations; do **not** employ `\(\)` or `\[\]` variants, as the validator and rendering pipelines expect dollar‑sign delimiters.
- When adding comments, avoid placing more than one directive of the **same type** on a single line; the validator now flags duplicates and authors should merge them into a single comment listing all applicable rule IDs (the syntax already supports commas).
- Use the validator conservatively: run `check.py --content` for advisory guidance; it will flag missing tags, exams before sessions, duplicate week numbers, unscheduled sessions carrying topics, out-of-order semester headings, and similar structural issues. Treat its output as suggestions unless maintainers request strict enforcement.
- Treat submodules (including `private/`, `tools/pytextgen/`, `tools/pyarchivist/`) as read-only unless the user explicitly grants permission.
- Prefer small, reviewable changes to skill docs and helper scripts; document rationale and link to the Continuous improvement section of SKILL.md (or log in `continuous_improvement.md`) when proposing edits.
- **Always run the `check.py` validator after using any edit tool.** The agent frequently emits malformed Markdown, so validating immediately helps catch and fix errors or warnings before they land in a PR.

## Tools & locations

- Skill docs, examples, and helper scripts: `.agents/skills/academic-notes/`
- Validator: `.agents/skills/academic-notes/check.py`
- Wikipedia helper: `.agents/skills/academic-notes/find_wikipedia.py`
- Continuous improvement workflow: **Continuous improvement** section of `.agents/skills/academic-notes/SKILL.md`; log incidents in `.agents/skills/academic-notes/continuous_improvement.md`

## Course index and logistics (conventions)

- **Separator**: After the course list (institution, `name:`, `credits:`), insert `---` before the course description.
- **Sections format**: Under `logistics` → `sections`, use one key for the chosen stream (e.g. `lecture: L1`). List all section identifiers and their details under that key (e.g. L1, L2, L3 with venue and times). Do not create separate `lecture: L2`, `lecture: L3` keys.
- **Session headings**: Use `## week N lecture` and `## week N lecture 2` (space in “lecture 2”). Do not put holiday or status text in the heading (e.g. `## week 3` not `## week 3 (Lunar New Year)`).
- **No-class days**: Omit `topic:` for sessions without classes. Use `status: public holiday: <name>` when the holiday is known (e.g. Lunar New Year, Labor Day); use `status: no class` for other non-teaching days (e.g. midterm break).
- **Index session flashcards**: Omit session-level flashcard bullets in the index when they only describe scope or coverage; keep substantive flashcards in topic notes and questions.
- **Emphasis**: Use underscore for italic and bold: `_italic_`, `__bold__`.

## Short author checklist

1. Add YAML frontmatter including `title`, `aliases`, `tags:` (must include the `special/academia/<INSTITUTION>` tag).
2. Add or confirm flashcard activation tag in `tags:` when flashcards are desired.
3. Ensure `index.md` pages contain `# index` and a `children:` or `## children` section where appropriate.
4. For weekly pages, include `datetime:` ranges and concise `topic:` / `learning_outcomes:` or `takeaway:` entries. When a session references a topic note, add a **section links index**: under the topic parent bullet, list one `[§ section name](file#anchor)` per top-level section (`##`), and under each section list one `[§ subsection name](file#anchor)` per subsection (`###`) and any deeper (`####`). Place these § links before any session-specific flashcard glosses. Use percent-encoded spaces in anchors, or hyphenated anchors (e.g. `#saturation-transistor-types-and-layout`) for headings with commas/special chars to avoid validator false positives. The course index may also include a dedicated "Topic (sections and subsections)" block with the full nested outline. When you merge or remove ### subsections in a topic note, update the § links and glosses in the index to match.
5. **Topic notes**: Use lowercase filenames (e.g. `voltage regulator.md`), or the full canonical term when it matches the general article (e.g. `brushed DC electric motor.md`). Aliases = general term and synonyms only (not instances like LM7805); **include both singular and plural forms** (e.g. brushed motor / brushed motors). When linking to `general/`, use **lowercase first word** in both link display text and path (e.g. `[brushed DC electric motor](.../general/brushed%20DC%20electric%20motor.md)`). Circuit examples must state topology, polarities, and loop direction; when introducing a component via an instance, define the general concept (e.g. IC, datasheet) with flashcards. Use ### subsections under ## where it improves hierarchy. Describe **course-specific circuit layouts** explicitly (e.g. H-bridge: top row both PNP, bottom row both NPN) rather than a generic topology.
   - When introducing circuit notation or jargon (e.g. $V_{CC}$, $V_{CE}$, “low-side switch”), add a brief definition near first use (and optionally a flashcard) so the note is readable without prior course context.
   - When embedding diagrams/schematics, put the image markup (e.g. `<p> ![...](attachments/... )`) on the same line as the preceding paragraph. Add diagram‑recall flashcards (image in the prompt) for key symbols/circuits so learners can recall what each represents. When adding or editing circuit diagram generators (e.g. schemdraw scripts in `attachments/`): draw the main rail first, use `.push()` at the branch node, finish the rail, then `.pop()` and draw the branch; use `.reverse()` on diodes when polarity requires it (see academic-notes skill “Images and circuit diagrams”).
   - IC power pins (e.g. 74HC14): VCC = any valid supply voltage (course may use 5 V); GND = ground. Do not state “must be 5 V” unless the course fixes that.
6. **Session prose**: After the session outline (`---`), add prose only when it adds value (next lecture, grading); do not duplicate index bullets and topic notes. Omit “lecture summary” index cards unless they cover major grading components.
7. **Questions pages** (e.g. `questions.md`): Not topic notes; sections do not need the "Flashcards for this section are as follows:" rubric. Add questions and solutions as content; flashcards are optional per section.
8. Run `uv run .agents/skills/academic-notes/check.py --content <path>` and resolve obvious authoring omissions before opening a PR.

## Continuous improvement

This instruction set and the skill are living artifacts. If you discover missing examples, ambiguous rules, or repeated validation warnings, follow the steps in the **Continuous improvement** section of `.agents/skills/academic-notes/SKILL.md`; record feedback in `continuous_improvement.md`, draft a minimal clarification, and present it for maintainer review.

## Developer tooling & tests (academic notes)

- When adding tooling or scripts that process academic notes (for example, LMS converters), include unit tests and integration tests that exercise representative course pages and edge cases (missing metadata, unexpected frontmatter). Place tests in the skill’s own `tests/` subfolder (`.agents/skills/academic-notes/tests/`); mirroring paths inside that directory (e.g., `tests/tools/test_convert_canvas.py`) keeps them close to the code they exercise and avoids cluttering the repository-level `tests/` tree.
- Validators updated for academic notes must come with tests that assert expected warnings and validation results. Run `bun run check` and `bun run test` locally before proposing CI changes; when working on a subset of files, supply explicit paths to these commands so they complete faster than scanning the whole repo.
