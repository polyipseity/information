# Feedback log — academic-notes skill

Append new incidents, patterns, and user feedback here with a **date** and a **one-sentence description**. The operational workflow (gather → document → teach validator → verify → PR) lives in the **Continuous improvement** section of `SKILL.md`; use this file to log raw feedback and to preserve provenance.

**When the log gets too long:** fold learnings into the appropriate skill files (`SKILL.md`, `course-template.md`, or `.agents/instructions` files that apply to `special/academia`). Add or clarify rules, examples, and checklist items where they belong, then **remove the incorporated entries from this log** so it stays a short, current list. Git history preserves provenance; no need to keep long historical blocks in this file.

---

- **2026-03-08** — Accounting course convention: topic note `journal entries.md` with one entry type per section; each example in a single blockquote (scenario, markdown table Dr/Cr right-aligned, optional explanation). Validator: `no_soft_wrap_paragraph` exempts only **table rows** (after stripping multi-level blockquote prefix `>`, `>>`, `> >`); blockquote prose remains subject to soft-wrap. Incorporated into SKILL.md (§ Journal entries note), academic-notes.instructions.md, rules.py (docstring + `after_quote` logic + test).

- **2026-03-08** — When adding new lecture content: prefer section links if content duplicates existing; enhance existing notes (prose + flashcards) and section-link if content extends existing material; create new notes only when there is no or little overlap. Documented in SKILL.md (§ Adding new lecture content) and academic-notes.instructions.md.
- **2026-03-08** — Journal entry examples: minimum—mask all debit and credit amounts with clozes; also mask scenario with one or more clozes but leave enough hint words; prefer slightly smaller clozes. Use `&nbsp;` instead of comma for three-digit thousands separator for readability. Incorporated into SKILL.md (§ Journal entries note) and academic-notes.instructions.md (§ Topic notes / accounting).
- **2026-03-08** — Topic notes (except journal entries): almost never use cloze ({@{ }@}); use two-sided (::@::) or extremely rarely one-sided (:@:) flashcards only. Incorporated into SKILL.md (§ Flashcards and markup, § Topic-specific notes, Pre-commit checklist), academic-notes.instructions.md (§ Topic notes), flashcard-creation SKILL.md.
- **2026-03-08** — Journal entry scenario clozes: cover almost the entire scenario but leave a few hint words at the beginning or end; for longer scenarios use two or three clozes. Updated SKILL.md, instructions, flashcard-creation skill; applied to ACCT 3020 journal entries.md.
- **2026-03-08** — Accounting courses: do not use LaTeX; use plain text, numbers, and symbols (×, −, ÷). Updated SKILL.md (Key principles, Journal entries note), academic-notes.instructions.md; removed LaTeX from ACCT 3020 current liability.md and journal entries.md.

(Append new entries below with date and short description.)
