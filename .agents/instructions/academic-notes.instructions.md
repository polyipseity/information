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

- **Header style validator is language-aware**: The validator now properly handles non-Latin scripts (CJK, Cyrillic, Arabic, Greek, etc.) which lack uppercase/lowercase distinction. Topic notes in any language no longer need header_style suppressions. Only Latin-script headers require the lowercase-except-proper-nouns convention.
- Prefer one durable home per concept: **duplicate → link**, **enhancement →
  deepen existing note**, **new → create new note only if no good home exists**.
- When you change a topic note, update its **prose**, **flashcards**, and every
  affected **`index.md` section link** in the same task.
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
- For Canvas-derived assignment-style leaf indexes (for example lab rounds,
  homework folders, or similar deliverables, but not quiz pages), keep the visible
  Canvas wording verbatim in `## description`, preserve color with `<span
  style>`, use Markdown for bold/italics/links/paragraphing/line breaks, put
  the Canvas title header first as `- title: <verbatim title>`, then order the
  sections as `## children`, `## description`, `## attachments`,
  `## submission`, and `## solution` with no extra `---` after the parent line.
  Omit generic `## logistics` / `## overview`, include a local attachments
  list, and leave `submission` / `solution` empty until real content exists.
  If the task explicitly keeps submission or solution artifacts private but
  still wants the public page to preserve the normal file routes, keep ordinary
  relative links in the public `## submission` / `## solution` sections as if
  the files were still colocated, and do not rewrite them to `private/` paths.
  When a solution artifact exists, list it in `## solution` with the same plain
  markdown bullet style used in `## attachments`. Reserve the more advanced
  nested `file:` plus metadata structure for `## submission` only.
  If a referenced file was not captured locally at all, preserve the visible
  Canvas wording but do not invent a fake file.
  Any Canvas-derived metadata value containing a date, datetime, or duration
  must be normalized to ISO 8601 with timezone where applicable: `Due` and
  `locked at` should be single ISO datetimes, availability windows should use
  an ISO datetime range plus an ISO duration when both endpoints are known, and
  pure durations should use ISO duration syntax. Canvas start timestamps use
  seconds `:00`; Canvas end timestamps use seconds `:59`. This applies only to
  metadata fields, not to the ordinary description prose: keep human-readable
  Canvas sentences such as `This assignment was...` verbatim even when they
  contain dates or times.
- When such a folder also has companion pages like `lab.md` or `prelab.md`, let
  `index.md` own the logistics and attachments. Use the companion pages for new
  knowledge points, worked cases, implementation pitfalls, and brief routing to
  durable topic notes instead of repeating theory that already has a canonical
  home. Keep those companion pages about pure knowledge only: avoid workflow
  checklists, student expectations, assessment framing, and other logistics-like
  prose there. When the source includes concrete programming work such as
  MATLAB, keep a few short code idioms and implementation details in the
  companion page as part of the knowledge. Make code-centered flashcards
  self-contained by naming the relevant snippet or variable roles instead of
  asking only generic function questions; when useful, include the local given
  model or workflow too, especially on the left-hand side of the card. Also avoid meta-summary sections whose
  main content is “this page covers X, Y, and Z”; start with ordinary
  subject-matter prose instead. Keep `prelab.md` limited to preparation-stage
  setup and preview knowledge; move solved assignment-specific values and final
  interpretation into `lab.md`.
- Questions pages are not topic notes. Official material should usually be in
  blockquotes; self-authored review prompts should usually be ordinary headings
  and lists.
- Canvas quiz conversions should normally be split into a public `questions/`
  review page and a private mirrored archival page. Keep shared metadata on
  both sides; keep verbatim official question text on the private side; keep
  hint/review prompts on the public side. Keep the public `## hints` in the
  same order as the archived/private question order even when the wording later
  becomes more conceptual. Do not keep a parallel
  `assignments/online quiz N/index.md` stub once the quiz has a home under
  `questions/`; quiz pages belong in the `questions/` family even when Canvas
  surfaced them through the assignments UI. If only quiz timing or schedule
  metadata is known, keep a minimal public placeholder in `questions/quiz N.md`
  until fuller content is archived. Private quiz pages do not need a
  stock explanatory paragraph before `## content`; start directly with the
  archived questions unless a page-specific caveat is genuinely needed. If the
  archive shows only a checked choice rather than explicit grading correctness,
  record it as an archived selection instead of asserting it as a solution,
  unless the user explicitly confirms that the checked choices are correct. In
  that confirmed-correctness case, keep the solution and explanation inside the
  same quoted question block, using quoted `Solution:` and `Explanation:` lines
  rather than out-of-quote bullets. Add meaningful cloze coverage of the
  method, condition, or conceptual reason rather than only re-clozing the final
  option, and do this even when the prompt or confirmed answer depends on an
  embedded image. If the `Solution:` line itself embeds an image, still put at
  least one cloze on that `Solution:` line so the chosen option, label, or
  structural descriptor is directly reviewable there rather than only in the
  later `Explanation:`. When the archived quiz question contains actual figures, extract the
  real image assets from the archived HTML into a local `attachments/` folder
  beside the archival quiz family and embed them in Markdown instead of leaving
  raw figure filenames such as `Q1_1.jpg` in the note body. Preserve the
  original Canvas-exported filenames when available for traceability. Fall back
  to a short textual identifier only when the archived source truly does not
  preserve an extractable image payload. Keep the public quiz page pedagogical:
  keep the hint one step away from the original question rather than many steps
  away: preserve the option family, named property, band edge, timing pattern,
  or transform form that helps the reader map the hint back to the quiz, but
  avoid copying the full official prompt verbatim. When the user asks for more
  context, add it mainly on the left-hand side prompt itself: use option-family
  cues, mutated-but-equivalent givens, or the decisive spectral, timing, or
  topology landmarks without reproducing the official choices verbatim. For
  spectrum/block-diagram quiz explanations, describe the stage-by-stage signal
  processing chain — such as carrier multiplication, band shifting, and which
  replica the LTI block preserves or rejects — rather than only naming the
  final cutoff or option. Use alternate-number toy equations only when they
  genuinely clarify the same solving method. Do not mirror the full official
  image-heavy prompt there unless the user asks for that. If the private
  archival page intentionally keeps only archive tags,
  use a local `metadata_flash_tag` suppression rather than inventing an active
  tag.
- Split oversized `questions.md` files into `questions/index.md` plus child
  pages.
- Keep distinct official question families distinct (tutorials, problem sets,
  practice exams, solutions).
- For detailed rules on quoted solutions, cloze coverage, MD028 handling, and
  subpart formatting, consult `../skills/academic-notes/SKILL.md`.
- For accounting courses, place each journal-entry example in the most specific
  topical note rather than in a monolithic collector file; the detailed
  table/cloze conventions live in `SKILL.md`.

## Suppressions and validation

- Prefer fixing content over suppressing rules.
- Allowed suppression forms are `ignore-line[...]`, `ignore-next-line[...]`,
  and `ignore-file[...]`, each with a clear rationale.
- File-level suppressions are mainly for genuine special cases such as
  assignment-style index pages.
- Do not add duplicate directives of the same type on one line.
- If a prose-oriented validator rule keeps flagging room codes, percent-encoded
  link destinations, inline code, or HTML comments, prefer fixing the rule
  instead of copy-pasting the same suppression through multiple notes.
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
5. Use QA cards for topic notes by default; allow cloze only inside embedded
  accounting journal-entry worked examples.
6. Route labs, tutorials, and large question collections through dedicated topic
   notes or child pages instead of bloating weekly entries.
7. Validate the smallest relevant path.
8. If the task exposed a reusable convention, fold it into the skill docs.
