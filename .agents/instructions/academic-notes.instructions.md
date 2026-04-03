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

- Prefer one durable home per concept: **duplicate → link**, **enhancement →
  deepen existing note**, **new → create new note only if no good home exists**.
- When you change a topic note, update its **prose**, **flashcards**, and every
  affected **`index.md` section link** in the same task.
- Keep technical notes at the lecture's real depth: preserve formulas,
  distinctions, derivation skeletons, and representative examples or
  counterexamples.
- Do not use chapter numbers as stand-ins for links when the repository has no
  chapter page to link to.
- Keep companion continuous-time and discrete-time notes at comparable rigor
  when the mathematics genuinely mirrors.
- Do not automatically prune motivating historical or technology context if the
  lecture uses it to teach the core idea.
- In topic notes other than `journal entries.md`, prefer QA cards rather than
  cloze in prose.
- Make flashcards standalone: restate givens, assumptions, notation, and any
  needed diagram context.
- Keep math on one source line and use `$...$` / `$$...$$`; do not use `\(\)`
  or `\[\]`.
- Use underscore-normalized flashcard tags, for example
  `flashcard/active/special/academia/HKUST/COMP_3031` or
  `flashcard/active/special/academia/Pusan_National_University/IT3000504`.
- Do **not** create or edit `general/` files automatically; use the Wikipedia
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
- Questions pages are not topic notes. Official material should usually be in
  blockquotes; self-authored review prompts should usually be ordinary headings
  and lists.
- Split oversized `questions.md` files into `questions/index.md` plus child
  pages.
- Keep distinct official question families distinct (tutorials, problem sets,
  practice exams, solutions).
- For detailed rules on quoted solutions, cloze coverage, MD028 handling, and
  subpart formatting, consult `../skills/academic-notes/SKILL.md`.
- For accounting courses, keep journal-entry examples in `journal entries.md`;
  the detailed table/cloze conventions live in `SKILL.md`.

## Suppressions and validation

- Prefer fixing content over suppressing rules.
- Allowed suppression forms are `ignore-line[...]`, `ignore-next-line[...]`,
  and `ignore-file[...]`, each with a clear rationale.
- File-level suppressions are mainly for genuine special cases such as
  assignment-style index pages.
- Do not add duplicate directives of the same type on one line.
- After editing academic notes, validate the **smallest relevant scope only**.

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
5. Use QA cards for topic notes except `journal entries.md`.
6. Route labs, tutorials, and large question collections through dedicated topic
   notes or child pages instead of bloating weekly entries.
7. Validate the smallest relevant path.
8. If the task exposed a reusable convention, fold it into the skill docs.
