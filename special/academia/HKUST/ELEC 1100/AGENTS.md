---
aliases:
  - ELEC 1100 AGENTS
  - HKUST ELEC 1100 AGENTS
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/AGENTS
  - language/in/English
---

# ELEC 1100 agent instructions

- For each ELEC 1100 lab, use the Canvas lab handout and summary sheet (e.g. `LabN_2026s.pdf`, `LabN_SummarySheet_2026s.docx`) as the primary source.
- First, integrate any new concepts or workflows into the relevant topic notes (`lab equipment`, `electronic component`, `diode`, `voltage regulator`, `transistor`, `H-bridge`, etc.) and update the weekly session outline with `§` links and a few workflow/safety flashcards instead of duplicating full procedures in `index.md`.
- Second, create an assignment-style note under `labs/lab N/` that mirrors the Canvas assignment metadata (title, due/available window, points, submission type, file types) and lists official handouts (both the `LabN_2026s.pdf` manual and the summary-sheet `.docx`) under an attachments block and the canonical submission filename under a `submission` section.
- Assignment pages such as `labs/lab 1/index.md` may omit the standard `# index` / `## children` shell and instead use a file-level suppression (see academic-notes instructions for exact syntax) so only that file is exempt from index-heading rules.
- Attachments must be copied into `labs/lab N/attachments/` and the submission template into `labs/lab N/` with exact filenames referenced in the note so future agents can regenerate or extend lab notes consistently.
- Timetable normalization note: the source timetable contained a duplicated week-9 row. The first instance covers `30 Mar 2026 - 03 Apr 2026` (lab exam, tutorial, lecture, and public holiday on 3 Apr). A second copy of week 9 appears for `06 Apr 2026 - 10 Apr 2026` (three consecutive public holidays followed by final project lecture). Treat the latter as week 10 and renumber subsequent weeks accordingly.
- Holiday days should be represented as public-holiday sessions with status `public holiday` so they remain visible without inflating lecture count.
- Schedule note: `T3` and `T1` provide `T2` video recording during the week around `2026-04-20`.
- Maintenance note: additional sessions should be added in chronological order.
- Question-bank note: keep public practice material under `questions/` with family-split files such as circuit-analysis, devices-and-logic, embedded-control, written-exam, and lab-exam pages; use `questions/index.md` as the durable landing page for that family.
- Lab-archive note: when only PDF handouts and code templates are archived, list the source-derived due/available slot and mark missing Canvas submission metadata as pending instead of inventing assignment-export fields.
- Header note: preserve acronym-heavy section titles such as `PWM`, `LDR`, `IR`, `XOR`, and `XNOR`; when the validator flags the capitalization, use a local `header_style` suppression instead of lowercasing the acronym.
- Durable-note note: topical notes should state concepts directly and avoid source-trace wording such as "the lecture says" or "the lab shows"; keep session-specific logistics inside `index.md` or the `labs/` subtree.
- File-split note: keep MCU concepts in `microcontroller.md`, and keep Arduino board, pin-map, IDE, and programming details in `Arduino.md`.
