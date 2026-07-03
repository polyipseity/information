---
name: Academic notes conventions
description: Guidelines and automated checks for files under special/academia (institution-agnostic)
applyTo: "special/academia/**,private/special/academia/**"
---

# Academic notes instruction

This instruction file is the quick-reference checklist for work under
`special/academia/**` and the mirrored `private/special/academia/**` path.

The authoritative long-form policy lives in
`../skills/academic-notes/SKILL.md`. Use that file for detailed guidance on
machine-learning notes, honors and proof-heavy courses, Fourier and generalized-
function notes, questions-page authoring, validation suppressions, and validator
extension work.

## Scope and source of truth

- Read `../skills/academic-notes/SKILL.md` before acting.
- Use `../skills/academic-notes/course-template.md` as the scaffold for new
  course indexes.
- The validator path is fixed at `.agents/skills/academic-notes/check.py`; do
  not recurse through the repository or the skill folder to find it.
- Durable conventions belong in the skill files and tests, not in memory.

## Quick rules for agents

- __Header style validator is language-aware__: The validator now properly handles non-Latin scripts (CJK, Cyrillic, Arabic, Greek, etc.) which lack uppercase/lowercase distinction. Topic notes in any language no longer need header_style suppressions. Only Latin-script headers require the lowercase-except-proper-nouns convention.
- Prefer one durable home per concept: __duplicate → link__, __enhancement →
  deepen existing note__, __new → create new note only if no good home exists__.
- When you change a topic note, update its __prose__, __flashcards__, and every
  affected __`index.md` section link__ in the same task.
- Keep technical notes at the lecture's real depth: preserve formulas,
  distinctions, derivation skeletons, and representative examples or
  counterexamples.
- Do not use chapter numbers as durable references in prose, flashcards,
  routes, or agent guidance. `.tmp` materials and source decks are not a
  stable navigation layer; use topic names and in-repo section links instead.
- When a tutorial, exam, or review question reveals a tricky case, exam trap,
  or "what if" variant, fold it into the canonical topic note under a clear
  subheading and update the relevant `index.md` route.
- Keep companion continuous-time and discrete-time notes at comparable rigor
  when the mathematics genuinely mirrors.
- Do not automatically prune motivating historical or technology context if the
  lecture uses it to teach the core idea.
- In topic notes, prefer QA cards rather than cloze in prose, except that
  accounting journal-entry worked examples may use cloze inside quoted
  scenarios, tables, calculations, and short explanations.
- In accounting topic notes, keep every journal-entry scenario and Dr/Cr table
  above the local `Flashcards for this section are as follows:` block; once
  that rubric begins, only flashcards should remain until the next header.
- Make flashcards standalone: restate givens, assumptions, notation, and any
  needed diagram context.
- Keep math on one source line and use `$...$` / `$$...$$`; do not use `\(\)`
  or `\[\]`.
- __LaTeX conventions for probability notes__: Use `\operatorname` for named
  distributions (`\operatorname{Bin}`, `\operatorname{Cau}`); `\mathbf 1` for
  indicators; `\binom{n}{k}`; `\lim_{y\uparrow m}` for left limits;
  `\begin{cases}` with `[2pt]` spacing for piecewise definitions.
- Use underscore-normalized flashcard tags, for example
  `flashcard/active/special/academia/HKUST/COMP_3031` or
  `flashcard/active/special/academia/Pusan_National_University/IT3000504`.
- Do __not__ create or edit `general/` files automatically; use the Wikipedia
  helper only to discover canonical titles for links.
- Do not put instructor or TA names or email addresses in course notes.
- Course-local `AGENTS.md` files must use the exact heading
  `# <course code> agent instructions` and must not contain flashcard markup.

## Course-root and topic-note checklist

- In a course-root `index.md`, order major top-level sections as `## children`,
  then `## logistics`, then `## overview`.
- After the course list (`institution`, `name`, `credits`), insert `---` before
  the course description.
- Keep weekly sessions in chronological order and use exact headings such as
  `## week N lecture`, `## week N lecture 2`, `## week N tutorial`, and
  `## week N lab`.
- If the official schedule exposes a recurring lecture, tutorial, or lab
  stream, keep that stream's week headings continuous even across no-class
  weeks; use `status:` metadata instead of dropping the week entirely.
- For no-class sessions, omit `topic:` and use `status: public holiday: <name>`
  or `status: no class`.
- Keep `index.md` pages lean; route readers to topic notes instead of duplicating
  long explanations in weekly entries.
- When a section introduces reusable recognition patterns, centralize the real
  explanation in the topic note and keep only a short route card or link in the
  index.
- For topic-note filenames and titles, prefer lowercase singular canonical
  concept names unless a proper noun or standard plural makes that unnatural.
- In course topic-note flashcards, use local prompts such as `definition` or
  `Bayes theorem finite`; do not repeat the note title unless nested context
  requires it.

## Questions, labs, and special note families

- Treat lab-prep decks and lab manuals as normal lecture ingestion: centralize
  theory and worked examples in topic notes, then route lab pages there with
  `§` links.
- For assignment-style leaf indexes (lab rounds, homework folders, or similar
  Canvas deliverables) use the
  [assignment-creation](../skills/assignment-creation/SKILL.md) skill instead.
  That skill covers Canvas metadata, section ordering, companion pages, code
  idioms, and submission/solution conventions.
- When an assignment-style leaf folder has companion pages such as `lab.md` or
  `prelab.md`, the [assignment-creation](../skills/assignment-creation/SKILL.md)
  skill covers companion page conventions in detail (knowledge-only content,
  code idioms, flashcards, and prelab/lab separation).
- Questions pages are not topic notes. Official material should usually be in
  blockquotes; self-authored review prompts should usually be ordinary headings
  and lists.
- Canvas quiz conversions: See the "Canvas quiz conversions" section in [../skills/academic-notes/SKILL.md](../skills/academic-notes/SKILL.md) for the complete public/private layout, solution conventions, attachment handling, and cloze coverage rules.
- Split oversized `questions.md` files into `questions/index.md` plus child
  pages.
- Keep distinct official question families distinct (tutorials, problem sets,
  practice exams, solutions).
- At the top of a questions page, include a `- topics:` line listing the major
  concepts covered (for example `- topics: medians, sigma-algebras, CDFs`).
- Questions-page __solutions__ use cloze `{@{ }@}` (not QA cards like topic
  notes). For detailed rules on cloze strategy, inference-word attribution, and
  question-page authoring conventions, see the "Questions and problem-set pages"
  section in `../skills/academic-notes/SKILL.md`.
- For detailed rules on quoted solutions, cloze coverage, MD028 handling,
  blockquote continuation, and subpart formatting, consult
  `../skills/academic-notes/SKILL.md`.
- For accounting courses, place each journal-entry example in the most specific
  topical note rather than in a monolithic collector file; the detailed
  table/cloze conventions live in `SKILL.md`.

## Suppressions and validation

- Prefer fixing content over suppressing rules.
- Allowed suppression forms are `ignore-line[...]`, `ignore-next-line[...]`,
  and `ignore-file[...]`, each with a clear rationale.
- File-level suppressions are mainly for genuine special cases such as
  assignment-style index pages (see the
  [assignment-creation](../skills/assignment-creation/SKILL.md) skill).
- Do not add duplicate directives of the same type on one line.
- If a prose-oriented validator rule keeps flagging room codes, percent-encoded
  link destinations, inline code, or HTML comments, prefer fixing the rule
  instead of copy-pasting the same suppression through multiple notes.
- After editing academic notes, validate the __smallest relevant scope only__.

## Tools and locations

- Skill folder: `.agents/skills/academic-notes/`
- Template: `.agents/skills/academic-notes/course-template.md`
- Validator: `.agents/skills/academic-notes/check.py`
- Wikipedia helper: `.agents/skills/academic-notes/find_wikipedia.py`
- Skill-folder tests: `.agents/skills/academic-notes/tests_a7392be/`

Validator commands:

- PowerShell or cmd:
  `uv run .agents/skills/academic-notes/check.py "special/academia/<INSTITUTION>/<COURSE>"`
- POSIX shell:
  `uv run .agents/skills/academic-notes/check.py special/academia/<INSTITUTION>/<COURSE>`
- Narrow single-file check:
  `uv run .agents/skills/academic-notes/check.py "special/academia/<INSTITUTION>/<COURSE>/index.md"`

## Continuous improvement

If a task reveals a durable academic-notes lesson, update the authoritative
files directly:

- `../skills/academic-notes/SKILL.md`
- `../skills/academic-notes/course-template.md`
- this instruction file
- related validator tests when appropriate

Persistent memory is not the long-term documentation system for academic-notes
work.

## Short author checklist

1. Confirm valid frontmatter and underscore-normalized flashcard tags.
2. Keep `index.md` order, chronology, and chosen-section metadata consistent.
3. Deepen existing topic notes before creating overlapping new ones.
4. Keep topic-note prose, flashcards, and index links synchronized.
5. Use QA cards for topic notes by default; allow cloze only inside embedded
   accounting journal-entry worked examples.
6. Route labs, tutorials, and large question collections through dedicated topic
   notes or child pages instead of bloating weekly entries.
7. Validate the smallest relevant path.
8. If the task exposed a reusable convention, fold it into the skill docs.
