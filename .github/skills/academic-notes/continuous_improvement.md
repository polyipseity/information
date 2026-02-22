# Continuous improvement — academic-notes skill

- **2026‑02‑22 consolidation:** migrated continuous‑learning
  documentation so every skill folder now has its own note; this file was
  updated accordingly.

This document describes the feedback loop for continuously improving the `academic-notes` skill and its validator/examples.

Workflow

- Gather examples from course folders under `special/academia/<INSTITUTION>`.
- Update `patterns.md` and `examples.md` with newly observed idioms and normalization guidance.
- Run `validate_academic.py --content` to discover common missing metadata and produce reports.
- Create small, reviewable PRs containing suggested normalizations and example patches.
- After merge, re-run validator and update `issue_frequencies.md`.

Best practices

- Prefer human-reviewed PRs for normalization; do not mass-apply automated fixes without maintainer consent.
- Record any new inline idioms (e.g., `::@::` variants, taxonomy chains) in `patterns.md` with examples in `examples.md`.
- Keep the validator conservative — use `--content` mode for advisory warnings and only enforce rules when maintainers request stricter behavior.

Example: improving the skill instructions (no PR performed)

- Step 1 — collect feedback: a user reports that the flashcard activation tag examples are confusing. Record the feedback in a short note file (e.g., `./reports/feedback_log.md`) with date, reporter, and brief description.
- Step 2 — draft a minimal instruction edit locally: update `SKILL.md` or `patterns.md` with a one-paragraph clarification and an explicit example. Keep the change atomic and well-commented.
- Step 3 — validate locally: run `python validate_academic.py --content special/academia/<INSTITUTION>` and confirm no regressions in examples.
- Step 4 — present the draft to the maintainer as a patch or PR for review. Since you asked for "no PR" in this workflow example, instead save the draft change as a patch file (`git format-patch` or a unified diff) and attach it to the feedback note so a maintainer can apply it.
- Step 5 — after review, incorporate reviewer comments into the instruction and update `issue_frequencies.md` if the change reduces common warnings.

Notes:

- Keep edits minimal and reversible. Prefer adding examples and clarifications rather than sweeping automated normalizations.
- Always link feedback to a short test or validation run to show the effect of the change.

- **2026‑02‑22 lesson:** while creating a new course note I mis‑ordered semesters and accidentally duplicated the `groups` block in the HKUST index. Corrective actions included reordering the term sections, removing the duplicate list, and inserting an HTML comment marker (`<!-- future term sections ... -->`) to simplify future edits. This prompted additions to the validator (semester chronology warning, exam‑ordering warning) and corresponding documentation updates. A record of the incident should be kept in `reports/feedback_log.md` for traceability.
- **2026‑02‑22 follow‑up lesson:** When generating weekly sessions from a timetable, I assumed generic lab/tutorial numbering and populated every week. The course actually used LA3 and T2 only; I should have asked for the specific section identifiers first. Added guidance to `patterns.md` about querying the user and respecting numbered lab/tutorial sessions. This shows the value of clarifying ambiguous schedule data before bulk entry.

- **2026‑02‑22 additional refinement:** After filtering to the relevant LA3 and T2 sessions, I further simplified the notes by renaming them to `lab 1`/`tutorial 1` for each week. The rule is: once irrelevant sections are removed, reset numbering per week unless multiple sessions occur in that week. This reduces clutter and aligns with common course-note patterns. Update the validator-style guidance to mention this renumbering heuristic and add it to `patterns.md` as well.

- **2026‑02‑22 final tweak:** Following feedback about two lectures per week, I revisited the schedule and inserted the second lecture for each week with exact start/end times taken from the provided table. I also corrected a mis‑assigned tutorial (Lab 5 vs Lab 6) when the timetable clarified which week it belonged to, and added an HTML comment noting that T3 and T1 would provide a T2 video recording in late April. All tutorials, labs and exams now use full ISO interval datetimes (e.g. `2026-02-02T10:30:00+08:00/2026-02-02T13:20:00+08:00, PT2H50M`). This exercise underscores the importance of capturing complete interval information for all session types up front, which makes auditing and automation far simpler.

- **2026‑02‑22 ongoing note:** remember to handle multiple lectures per week when parsing timetables and to embed the full interval for every session. Explicit datetime intervals make it easier to detect holidays, clashes, and exam windows automatically.

- **2026‑02‑22 unscheduled sessions:** when a session is marked `status: unscheduled`, it should not include a `topic:` field. This keeps holiday/overflow entries clean and avoids misleading content. Update import/generation logic accordingly.

- **2026‑02‑22 problem‑finding lesson:** periodically run a problems/MD lint check on the course file. The MD024 rule flagged a duplicate `### week 6 lecture 1` heading after reorganising sessions; removing the stray block resolved it. Regular linting catches these copy‑paste errors quickly. Also take care to reorder sessions by datetime when reviewing the file, as the earlier fix taught.

- **2026‑02‑22 session‑selection rule:** capture the student’s lab/tutorial section (e.g. LA3, T2) near the top of the note and consult it when importing schedules. If the section is unknown, the agent must ask the user before adding any sessions. This ensures irrelevant streams are filtered out early and reduces clutter in weekly listings.

- **2026‑02‑22 section metadata style:** use a nested `sections:` list with `lecture`, `tutorial`, and `lab` sub‑items instead of separate top‑level list entries. Lecture entries now use a numeric placeholder (`L<number>`) rather than a question mark, matching the format of the tutorial and lab fields. Agents should prompt for each field and populate them accordingly. Remove any duplicate explanatory comments from the template to avoid confusion.

- **2026‑02‑22 session_times pattern:** the template now includes a `session_times:` block containing the standard weekday/time intervals for lectures, tutorials, and labs (e.g. Monday 16:00‑16:50 and Friday 11:30‑12:20 for lectures). Agents should consult this when generating weekly schedule entries, inferring the proper datetime intervals automatically. Add this block to existing course indexes as well (ELEC 1100 has been updated).

- **2026‑02‑22 inline datetime section syntax:** the `sections:` list now attaches ISO datetime interval(s) directly after the stream code using a semicolon (`L1; 2026-XX-XXT16:00...`). This replaces the previous separate `session_times` block and allows the note to be self‑contained. The agent prompt has been rewritten to treat lectures, tutorials, and labs identically when asking for this information.

- **2026‑02‑22 weekday/time format:** we further simplified the syntax by storing only the day-of-week (using full names such as `Monday` instead of abbreviations) and times (e.g. `MondayT16:00:00/MondayT16:50:00`), since schedules are built week‑by‑week based on the day of week. Agents should prompt for these patterns accordingly and avoid including full dates.

- **2026‑02‑22 venue metadata:** section entries now include a venue field placed between the stream identifier and the weekly time pattern, separated by semicolons (e.g. `L1; CYT‑LTL; MondayT…`). The template and existing notes such as ELEC 1100 have been updated accordingly. When parsing schedules, extract the venue from the timetable and store it here.

- **2026‑02‑22 venue placement:** when writing weekly entries the `- venue:` line should appear immediately after the `- datetime:` line.  This positioning makes automated parsing and manual scanning more reliable and avoids confusion when sessions are unscheduled or cancelled.

- **2026‑02‑22 grading details:** the grading section now lists components directly under `- grading` (no intermediate `scheme` level).  Each line is a `<component name>: <percent>%` pair; append `; <description>` only if you have extra qualifiers.  Use placeholders like `<component name>` and `<percent>%` in templates rather than concrete examples.  Write the component name first, then the percentage (no space before `%`), and add a semicolon only when a description follows; never put a space before the semicolon.  The optional description should clarify the component (e.g. number of labs) and you may drop the word “total.”  Policy notes and other text belong in the course description block rather than under grading; description blocks should not include instructor or staff names/emails.  This flattened, generic format simplifies both manual editing and automated import.

- **2026‑02‑22 venue interpretation:** for HKUST timetables a bare numeric (or numeric range like `2133&2134`) denotes a room in the Academic Building.  When recording such venues, prepend the word **Room** and append ", Academic Building" so the entry reads Room 2133 & 2134, Academic Building.  This rule aids consistency across course indexes.

- **2026‑02‑22 week‑numbering bug:** some timetables repeat a week label (week 9) during a holiday break. When this occurs, shift subsequent week numbers upward (duplicate → week 10, week 10→week 11, etc.) and insert explicit holiday entries with `status: public holiday`. Always keep a section record for holidays rather than skipping them. Template and validator updates were made to document this behaviour.

- **2026‑02‑22 template refinement:** avoid a separate “## sections” heading; instead add the lab/tutorial section metadata as list items under the existing `## logistics` block. This keeps the template compact and consistent with course notes.

- **2026‑02‑22 file sanity check reminder:** periodically scan the generated course index for duplicated headings (e.g. `## groups` or stray week blocks) before regenerating or committing. In this run a duplicate `## groups` header was spotted and removed earlier; routine checks catch such copy‑and‑paste artifacts early.  When working in the IDE, make frequent use of the Problems panel (or equivalent) to surface syntactic and structural issues; it can often highlight duplicate headings, missing frontmatter, or other formatting problems without writing a custom script.
