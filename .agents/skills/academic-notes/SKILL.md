---
name: academic-notes
description: Content conventions, examples, and tooling for course notes under special/academia.
---

# Academic notes — consolidated skill

This skill is the authoritative long-form guide for creating and maintaining
course notes under `special/academia/<INSTITUTION>`. The matching instruction
file is a quick-reference checklist for agents; this file owns the detailed
policy. The course template owns only scaffold-facing reminders.

Flashcards are generated automatically by the build system; do **not** run
`init generate` manually.

## Skill folder map

- `SKILL.md` — authoritative workflow and policy reference.
- `course-template.md` — scaffold for new course `index.md` pages.
- `check.py` — validator entry point. The validator is always at
  `.agents/skills/academic-notes/check.py`; do **not** recurse through the
  repository to find it.
- `check_mods/*` — validator rules and implementation modules.
- `find_wikipedia.py` — helper for discovering canonical `general/` article
  titles when a course note wants to link outward.
- `tests_a7392be/*` — validator and helper tests for this skill folder.

> **⚠️ Do not run tests from inside this folder.** This folder has its own
> `pyproject.toml` (for `ty` type-checker config only), so running `uv run pytest`
> here will create `.venv/` and `uv.lock` inside the skill folder. Always run
> tests from the workspace root: `uv run pytest .agents/skills/academic-notes/tests_a7392be/`.

## Source-of-truth split

- `SKILL.md` owns detailed writing, restructuring, validator, and note-family
  policy.
- `.agents/instructions/academic-notes.instructions.md` is the short,
  agent-facing checklist for quick triage.
- `course-template.md` owns the minimal scaffold and fill-in reminders for new
  course indexes.
- Durable lessons belong in these files and, when needed, in validator tests —
  not in persistent memory.

## Key principles

1. **Content first.** Capture the lecture's actual ideas, formulas,
   distinctions, examples, and instructor caveats before polishing structure.
2. **One durable home per concept.** Prefer enhancing an existing topic note and
   updating links before creating overlapping pages.
3. **Prose, flashcards, and navigation move together.** When you add, split,
   merge, or rename content in a topic note, update the note's flashcards and
   every affected `index.md` section link in the same task.
4. **Flashcards are standalone artifacts.** Restate local hypotheses, notation,
   givens, and conditions needed to answer the card correctly.
5. **Keep the lecture's mathematical spine.** For technical notes, the default
   bundle is _formula + derivation or proof sketch + intuition + worked
   example_.
6. **Preserve teaching detail, not just headlines.** Named classifications,
   operational distinctions, and memorable examples should survive ingestion.
7. **Respect metadata and chronology.** Keep YAML frontmatter valid, keep
   sessions in chronological order, and place exams after regular sessions.
8. **Keep math validator-friendly.** Use `$...$` or `$$...$$`, keep math on one
   source line, and avoid putting LaTeX inside emphasis. Use `$$...$$` on the
   same line as surrounding text (not on its own line). Accounting notes should
   avoid LaTeX entirely.
9. **Keep headers and emphasis consistent.** Topic-note headers in Latin scripts (English, etc.) should be **lowercase except for proper nouns** (every word lowercase unless it is a proper noun — NOT sentence case). Non-Latin scripts (CJK, Cyrillic, Arabic, etc.) are exempt since they lack uppercase/lowercase distinction. Prefer `_italic_` and `__bold__`.
10. **Validate narrowly and immediately.** Run the fixed validator path on the
    smallest relevant course or file after edits; never aim it at the whole
    repo or the entire skill folder.
11. **Skill files are the durable memory.** If a lesson recurs, update this
    skill, the template, the instruction file, and tests when appropriate.
12. **Course-local agent guidance lives in `AGENTS.md`.** Keep it concise,
    course-specific, titled exactly `# <course code> agent instructions`, and
    free of flashcard markup.
13. **Do not migrate validation metadata into `AGENTS.md`.** Suppression
    comments belong in the content file that needs them.
14. **Do not create or edit `general/` files automatically.** Use the Wikipedia
    helper only to discover canonical titles for links; course content still
    lives under `special/academia/<INSTITUTION>/<COURSE>/`.
15. **Do not put instructor or TA names or email addresses in course notes.**
    Refer readers to the official syllabus or LMS for contact information.

## Authoring workflow

Use this workflow whenever you add or revise course content.

1. Start from `course-template.md` when creating a new course `index.md`.
2. If agent-specific guidance is needed, add or update `<course folder>/AGENTS.md`
   with the exact title `# <course code> agent instructions`.
3. Fill frontmatter carefully: aliases, tags, course name, credits, and
   description.
4. Normalize flashcard activation tags with underscore-separated path fragments,
   for example `flashcard/active/special/academia/HKUST/COMP_3031` or
   `flashcard/active/special/academia/Pusan_National_University/IT3000504`.
5. Add `logistics` with grading and chosen-section metadata.
6. Maintain `children:` in teaching order and include `[AGENTS](AGENTS.md)` only
   when the file actually exists.
7. For course-root `index.md` pages, order major top-level sections as
   `## children`, then `## logistics`, then `## overview`; keep later sections
   in functional or chronological order after that.
8. Prefer one merged `## overview` section in the course root for official scope
   bullets, topic-to-file mapping, and other high-value orientation material.
9. Write explanatory prose first; add or revise flashcards after the prose is
   accurate.
10. Update related `index.md` anchors and session links in the same pass.
11. Run the validator and fix both warnings and errors before moving on.
12. Before finishing, review the note once as a reader and once as a flashcard
    consumer.

When building scaffolds, keep `index.md` pages lean. Avoid duplicating long
calendars or schedule prose across course roots, folder indexes, and leaf pages
when a child page can own the details more cleanly. Use a flat leaf file such as
`tutorial 1.md` when no subpages or local attachments are expected; use a folder
with `index.md` only when the item is likely to accumulate children of its own.

## Course metadata and index structure

### Frontmatter and tags

- Keep YAML frontmatter valid and stable.
- Require a flashcard activation tag on academic-note files when flashcards are
  desired. Tag segments should be underscore-normalized rather than space-based,
  for example `Korea_University/ISC213/questions/quiz_1`.
- Course indexes typically also carry `function/index` and
  `language/in/<language>`.
- For topic notes, prefer aliases that are genuine synonyms of the concept, not
  specific instances of the concept.

### Course-root layout

- After the course list (`institution`, `name`, `credits`), insert `---` before
  the course description.
- Put `## children` first, then `## logistics`, then `## overview`.
- Under `sections:`, use one key for the chosen stream, then list all stream IDs
  and their logistics under that key.
- Weekly session metadata must match the chosen lecture/tutorial/lab stream.
- Use session headings exactly like `## week N lecture`, `## week N lecture 2`,
  `## week N tutorial`, and `## week N lab`.
- If the official schedule exposes a recurring lecture, tutorial, or lab
  stream, keep that stream's week headings continuous across the teaching term
  even when a given week has no meeting. Mark the gap with `status:` metadata
  rather than silently skipping the week.
- If a session has no class, omit `topic:`. Use `status: public holiday: <name>`
  when known, otherwise `status: no class`.
- Keep session-level flashcards in the index only when they test a reusable
  pattern or concept. Do not use them merely to summarize scope.

### Examination sessions

When a regular lecture, tutorial, or lab slot is used for an examination
(midterm, final, quiz, or other formal assessment), keep the session's week
heading continuous rather than dropping it. This preserves the chronological
skeleton and reminds readers that the slot was occupied. Use this pattern:

- Keep the normal session heading (`## week N lecture`, `## week N tutorial`,
  etc.) as-is.
- Preserve `datetime:` and `venue:` — the exam occupies the regular time and
  room.
- Use `status: unscheduled; <exam name>` to mark the slot (e.g.,
  `status: unscheduled; midterm examination`). This mirrors the existing
  `status: no class` / `status: public holiday: <name>` convention for other
  non-lecture sessions.
- Omit `topic:` since no new subject matter is taught.
- Add a `[§ <exam section>](#<anchor>)` link pointing to the dedicated exam
  section elsewhere in the index (typically a separate `## <exam name>`
  heading later in the file). The section symbol `§` makes the link visually
  distinct from topic references.
- Optionally include exam-scope flashcards under the session entry when they
  clarify the exam's emphasis or highlight recurring proof patterns likely to
  appear. Keep these cards sparse and high-value — the exam section itself is
  the primary reference.

### Examination section format

Each exam gets its own top-level section elsewhere in the course `index.md`,
typically near the end after all regular sessions. Use a lowercase heading:
`## midterm examination` or `## final examination`. The section documents the
exam's logistics, the student's performance, and a reflective error report.

**Metadata fields** (order within the section is flexible; list them grouped by
function). Links to course materials (e.g., `[questions / ...](...)`) must
appear **after** the `report:` field, not before it.

- `datetime:` — ISO 8601 with duration, same format as session blocks.
- `venue:` — Room or hall name.
- `scope:` — Optional simple inline list of topics covered (
  e.g., `scope: topic 1, topic 2, topic 3`). Omit if the exam is
  cumulative and the course overview already lists all topics.
- `format:` — Document the exam conditions as a YAML list of single-key
  mappings (bullet items), not as a flat map. Common keys:
  - `calculator:` — `yes` / `no`
  - `cheatsheet:` — `yes` / `no` / `yes (unlimited)` / `yes (one A4 page)`
  - `referencing:` — e.g., `closed book, closed notes`
  - `provided:` — Materials handed out with the exam, or `(none)`
  - `questions:` — e.g., `long questions ×8` or `question ×5 (with subquestions)`
- `note:` — Optional free-form note about unexpected exam conditions (e.g.,
  an error found mid-exam that added extra time). Always present this field
  even if empty; use `\(none\)` for no content.
- `grade:` — Personal score (e.g., `89/100`). When bonus marks are
  included, use the form `base+bonus/max+max bonus`
  (e.g., `80+5/100+10`). Nested fields:
  - `letter grade:` — Letter grade (e.g., `A+`), or `\(none\)` if unknown.
  - `statistics:` — Class statistics. Group values under a session key
    that identifies the lecture section the exam belongs to (the course
    section identifier such as `L1`, not the week number). Include all of
    the following keys, using `\(none\)` for any
    value that is unavailable: `timestamp`, `count`, `mean`,
    `standard deviation`, `low`, `lower quartile`, `median`,
    `upper quartile`, `high`, `distribution`, and `data`.

    `timestamp:` — Set to the Canvas announcement posting datetime
    (ISO 8601 with timezone), not the exam start/end time. Extract from
    the announcement page's "Posted" metadata. When no announcement is
    available, use the data-extraction date.

    `data:` — Use `\(none\)`. Do **not** link to Canvas or any external
    LMS. Source data belongs in a course-local source folder (e.g.,
    `.math2431sources/`).

    **Canvas single-student view** provides: mean, median, high, low,
    upper quartile, lower quartile (displayed as "Upper Quartile",
    "Lower Quartile"). It does **not** provide: standard deviation,
    count, distribution — use `\(none\)` for those fields.

  - `breakdown:` — Optional per-question scores. One bullet per question
    using `score/max` format (e.g., `Q11: 8/10`). When the per-question
    max is unknown, omit the `/max` part entirely (e.g., `Q11: 5`). If a
    question includes bonus marks, use `base+bonus/max+max bonus`
    (e.g., `Q13: 8+0.5/8+2`).

- `report:` — Optional retrospective analysis using flashcards (`::@::`). Each
  bullet covers a mistake, surprise, or lesson learned. Use nested bullets for
  sub-topics. This section is the most valuable part for future review; write
  substantive cards that explain _why_ the mistake happened and what to do
  differently. Include the point deduction in parentheses (e.g., `(–1)` or
  `(+1.5)`) after the topic name. Always present this field even if empty;
  use `\(none\)` as the sole bullet for no content (not `(to be filled)` or other placeholders).
- `check:` — Optional paper-checking session. Sub-fields:
  - `datetime:` and `venue:` as usual.
  - `report:` — Optional nested section documenting what was
    contested and whether the score changed. Use the same `(–N)` / `(+N)`
    notation as in the main report.

#### total

A course-grade summary placed in an `## aftermath` section after the final
exam. Uses a subset of the exam metadata fields:

- `grade:` — Overall course grade as score out of total (e.g., `89.15/100`).
  Do **not** write the marking scheme formula or percentage.
  - `letter grade:` — Always present; the letter grade (e.g., `A+`), or
    `\(none\)` if unknown.
- `statistics:` — Class statistics. Group values under the course's lecture
  section key (e.g., `- L1:`), using the same format as exam statistics.

**Announcement preservation**: Official exam announcements (typically from
Canvas or other LMS) contain authoritative logistics and can shift in time or
venue. Preserve them as quoted blocks (`>`) after the exam section, and
preserve the original formatting (bold, italic, underline, color, etc.). Use
`---` to separate the structured metadata from the announcement prose. For
Canvas-specific extraction patterns, see [§ Extracting exam
data](#extracting-exam-data).

**Linking**: Each exam section is the target of `[§ <exam name>](#<anchor>)`
links from the week sessions in the same `index.md`. Ensure the section
heading's auto-generated anchor matches the link target.

#### Extracting exam data

When gathering scores and logistics from Canvas or other LMS sources, these
practical patterns apply across courses.

**Statistics from Canvas grades page**: Open a single assessment column in
the Canvas gradebook's single-student view. The page HTML embeds
per-assessment statistics as plain text. In Python, extract with:

```python
import re

pattern = (
    r"Score\s+out\s+of\s+(\d+\.?\d*)\s+([^Z]+?)"
    r"(?:Your\s+Score[^Z]+?)?"
    r"Mean\s+([\d.]+)\s+Upper\s+Quartile\s+([\d.]+)\s+"
    r"Lower\s+Quartile\s+([\d.]+)\s+Median\s+([\d.]+)\s+"
    r"High\s+([\d.]+)\s+Low\s+([\d.]+)"
)
for m in re.finditer(pattern, html_text, re.DOTALL):
    print(m.groups())
```

Alternatively, filter the page's stripped text for `"out of"` lines followed
by `"Median"` to locate stat blocks. Each extracted block maps to one
assessment (problem set, midterm, final, etc.).

**Exam announcements from Canvas**: Canvas announcement HTML is
densely styled. Strip `<style>`, `<script>`, and all HTML tags to recover
readable plain text, then preserve the result as a quoted block (`>`) under
the exam section. Include the announcement author and timestamp if visible in
the source to maintain provenance.

**Per-question breakdown from PDF**: When the instructor releases a scanned
PDF with per-question scores, extract using PyMuPDF (`import fitz`) if
`pdftotext` is unavailable:

```python
import fitz
doc = fitz.open(path)
for page in doc:
    text = page.get_text("text")
```

Map each extracted score to its question label following the exam's question
numbering (e.g., Q1–Q5 multiple choice, Q6–Q10 true/false, Q11–Q14 long
questions), which is typically indicated by the PDF layout.

**Grades notation**: Canvas displays "Your Score: X out of N" without
explicit bonus mark breakdown. Use the simple `X/N` form unless the course
separately documents bonus marks, in which case use the
`base+bonus/max+max bonus` form instead.

#### `aftermath` section

A `## aftermath` section appears after all exam sections to record the
final course outcome. Sub-sections:

- Supplementary non-examinable material (covered after the final exam) is
  documented as separate topic notes; the aftermath section links to them
  via an outline before the grade summary.
- `### total` — Final course grade with `grades:` and `statistics:` fields
  in the same format as exam sections (see above). Use `\(none\)` when no
  data is available.

The `aftermath` section typically does not have `report:` or `check:`
since those belong to individual exam sections; flashcard-worthy course-level
retrospectives, if any, go in the final session entry instead.

### Style conventions for topic notes

Topic notes (standalone `.md` files for a concept, theorem, or chapter section)
follow a consistent prose-and-flashcard pattern extracted from existing notes in
the repository. This pattern keeps the exposition readable and the flashcards
self-contained.

**Section structure.** Each major section in a topic note should follow this
template:

1. A section heading (lowercase except for proper nouns; mark proper-noun
   headings with `<!-- check: ignore-next-line[header_style]: proper noun -->`).
2. Explanatory prose — one or more paragraphs that define the concept, motivate
   why it matters, state the theorem or formula, and explain key steps
   (derivations, proofs, worked examples woven into the paragraph flow rather
   than isolated theorem blocks).
3. A `---` separator.
4. `Flashcards for this section are as follows:`
5. A bullet list of `::@::` flashcards.

**Critical rules for flashcard placement and grouping:**

- **Every section in a topic note must have its own flashcard block.** Do not
  skip sections based on perceived importance. Every section must include its
  own `---` ⇒ `Flashcards for this section are as follows:` ⇒ bullet‑list
  block. Treat all sections the same — the rule is identical for every section.
- **Group related flashcards within a section using inline bold text.**
  When a section covers several distinct topics, prefix each group of cards
  with a bold label (e.g., `**superposition.**`) inside the same flashcard
  bullet list rather than creating new headings. This avoids heading‑duplication
  errors (MD024) while keeping cards organized.

**Flashcard content conventions.**

- Each flashcard uses the `::@::` format (two-sided: left and right each
  generate a card). The left side should be a short, descriptive question (not
  just a label), and the right side should be a self-contained answer.
- Each card must be on a single Markdown line. Do not split `::@::` cards across
  lines.
- The first card of a section typically summarizes the main definition or
  theorem (e.g., `concept / definition ::@:: The definition in one sentence.`).
- Include enough context in the answer so the card works without referencing the
  surrounding prose. For example, restate the hypothesis in the answer side.
- Use KaTeX math (`$...$`, `$$...$$`) inside flashcards as needed, keeping it
  on the same line.
- **Split packed flashcards.** When a concept has multiple distinct criteria,
  formulations, or implications, split them into separate flashcards rather
  than packing them into a single card. For example, "recurrent vs transient"
  (return-probability definition) should be separated from the series criterion
  and the closed-class criterion, because each is a self-contained result with
  its own proof rationale. A card that lists "equivalently, A ↔ B and also
  C and D" should become at least two cards: one for A ↔ B and one for A ↔ C.
- **Include proof sketches for non-obvious statements.** For statements whose
  truth is not immediately clear from the definition, include a brief proof
  sketch in both the prose and the corresponding flashcard. The flashcard
  should state the key step or insight (e.g., the geometric-series argument
  linking the expected number of returns to $f_{xx}$). A flashcard that merely
  restates a non-obvious claim ("$\sum\Pi^n(x,x)<\infty$ iff $x$ is transient")
  without the reasoning is harder to internalize and less useful for review.
- **Cover finer distinctions explicitly.** When a classification has natural
  sub-categories (e.g., positive vs null recurrence), cover them in both the
  prose and dedicated flashcards. Do not let important finer distinctions
  remain implied — if a concept branches, the note should mirror that
  branching.
- **Proof and derivation flashcards.** When a section contains a proof or
  derivation (e.g., $N=(I-Q)^{-1}$, absorption probability formula), create
  a dedicated flashcard that walks through the key steps. This helps the
  reader reconstruct the logic during review. Keep the proof sketch compact
  enough to fit on one line; use `<p>` if paragraph separation is needed.
- **Equation-system flashcards.** When a concept involves solving a system of
  linear equations (e.g., hitting probabilities, expected hitting times,
  absorption probabilities, stationary distribution via global balance), create
  dedicated flashcards that walk through the equation setup, the boundary
  conditions, and the solution structure. This helps the reader internalise the
  "first-step decomposition" pattern (or similar linear-solver pattern) that
  recurs across many sections.
- **Algorithmic content in flashcards.** When the prose describes an algorithm
  or computational procedure for identifying a structural property (e.g.,
  finding communicating classes via strongly connected components, checking
  closed-class status by examining outgoing transitions, identifying cyclic
  classes for periodic chains, computing hitting probabilities by solving a
  linear system), add a flashcard that captures the computational check. This
  bridges abstract characterisations with practical computation and helps the
  reader apply the concept to new chains.
- **Example card pair pattern.** For well-known illustrative examples (e.g.,
  gambler's ruin — both hitting probabilities and expected duration; two-state
  periodic chain — both raw convergence failure and Cesàro convergence), create
  at least two cards: one that states the classical result (the formula or
  conclusion) and one that explains the solution method (how the equations or
  decomposition are set up and solved). The "method" card generalises beyond
  the specific example and trains the reader to apply similar reasoning to new
  problems.
- **Strengthen example method cards with explicit algebraic steps.** When a
  canonical example involves solving a difference or linear equation (e.g.,
  gambler's ruin — characteristic equation, general solution, boundary
  conditions, solving for constants), the "method" flashcard should walk
  through these intermediate steps explicitly. Include the characteristic
  equation, the form of the general solution, the boundary conditions, and
  how the constants are determined. This bridges the gap between a prose
  description ("solve the recurrence") and a fully worked answer.
- **"Why it works" cards for characterisation proofs.** When a section
  characterises a quantity as the unique/minimal solution to a system of
  equations (e.g., hitting probability as minimal non-negative solution,
  stationary distribution as unique solution to global balance), add a
  dedicated flashcard that explains why this characterisation holds. The key
  insight is typically a difference argument: assume two candidates, subtract,
  and show the difference must be zero (via induction, contraction, or maximum
  principle). This trains the reader to recognise when a candidate solution
  can be verified without computing the full path sum.
- **Named analogies to classical mathematics.** When a Markov-chain concept
  maps to a classical PDE or analysis structure (e.g., discrete Dirichlet
  problem, discrete Poisson equation, maximum principle), add a dedicated
  flashcard that:
  1. Names the classical structure explicitly.
  2. States the discrete analogue equation ($Lh=0$ on $A^c$ with $h|_A=1$
     for Dirichlet; $Lg=\mathbf 1_{A^c}$ with $g|_A=0$ for Poisson).
  3. Explains what the analogy implies (uniqueness, superposition, solution
     structure, comparison arguments).
     This connects probability theory to the reader's existing PDE/analysis
     knowledge and deepens intuition for why these equations behave as they do.
- **Definition with equivalent formulations.** When a concept has multiple
  equivalent definitions (e.g., total variation distance: $\\frac12 L^1$ and
  max-over-events; recurrence: return-probability, expected-number-of-returns,
  and series criterion), start with a definition card for the primary
  formulation, then add a separate card for each equivalent form with a brief
  equivalence proof sketch or translation guide. This prepares the reader to
  recognise and use whichever formulation is most convenient in a given
  context.

**Lint comments.** Every flashcard that contains math uses the `two_sided_calc_warning`
lint suppression:

```html
<!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
```

Place this comment between the `::@::` answer content and the end of the line.

These comments appear in a trailing position on the flashcard line.

**LaTeX ordinal convention.** Ordinals involving math variables **must** use a
hyphen between the variable and the ordinal suffix. Write `$k$-th`,
`$(k-1)$-th`, `$n$-th`, `$i$-th`, `$(i+1)$-th` — never `$k$th`, `$(k-1)$th`,
`$n$th`, `$i$th`, `$(i+1)$th`. Without the hyphen, LaTeX renders the character
sequence literally (e.g., `$k$th` produces "kth" in roman) because there is
no `\th` command, breaking both display and readability. This applies to all
ordinal suffixes (`-th`, `-st`, `-nd`, `-rd`) and all math-mode expressions.

**`<p>` paragraphing convention for flashcards.** When a `::@::` flashcard
contains multiple logical paragraphs, insert `<p>` between them for
readability in the source. Always include a space before and after `<p>`:

```markdown
- topic / label ::@:: First paragraph text. <p> Second paragraph text. <p> Third paragraph text.
```

The spaces around `<p>` keep the source readable without affecting HTML
rendering. Use `<p>` only when the flashcard genuinely has multiple distinct
paragraphs — do not split single-sentence cards.

**No `<b>` / `</b>` HTML tags in flashcards.** Do not use `<b>` or `</b>` for
bold text in flashcards — use `__` (Markdown bold) instead. Unlike `<p>`, which
is the standard way to create paragraph breaks in single-line source, `<b>` has
a straightforward Markdown equivalent (`__`) and mixing HTML bold into
flashcard lines creates a maintenance burden. This rule is stricter than the
general Markdown convention (where `<b>` is technically valid) because
flashcard lines must be easy to read and edit at a glance. The linter will
flag any remaining `<b>` / `</b>` as errors.

**Opening prose for topic notes.** The file-level opening section (before any `##`
headings) should start with one to three paragraphs of motivating prose that
explains why the concept matters and how it fits into the broader narrative of the
course. This is followed by a `---` separator and 2–3 overview flashcards that
capture the high-level motivation, key applications, and structural themes of the
topic.

### AGENTS.md in course folders

- Keep course-local agent instructions in `AGENTS.md`, not in hidden comments in
  `index.md`.
- The first content heading must be exactly
  `# <course code> agent instructions`.
- Do not put flashcard markup in `AGENTS.md`.

## Adding new lecture content

Before creating a new topic note, classify the incoming material:

- **Duplicate** → do not create a new note; add section links to the existing
  content.
- **Enhancement** → deepen the existing note and update its flashcards and
  session links.
- **New** → create a new durable topic note only when no good home exists yet.

Also follow these rules:

- If tutorial sheets, examples, or auxiliary handouts mainly deepen an existing
  concept, merge that material into the relevant topic note before inventing a
  detached catch-all section.
- Do not flatten dense lecture material into a few broad summaries. Preserve the
  explicit distinctions, classifications, formulas, examples, counterexamples,
  and teaching caveats that make the lecture memorable.
- Do not use external source numbering or indexing — theorem numbers,
  definition numbers, proposition numbers, lemma numbers, example numbers,
  chapter/section numbers, or any other numbering scheme from source
  lectures, textbooks, or handouts — in prose, headings, or flashcards.
  Durable notes must refer only to topic names, canonical note files, and
  in-repo section links. For the same reason, prose should not narrate its
  original context with wording such as _"in this lecture"_, _"the tutorial
  sheet shows"_, _"the lab manual asks"_, or other references to temporary
  delivery artifacts unless the artifact itself is the note's subject.
  Flashcards must use descriptive labels (e.g., _"smooth test function
  lemma"_, _"vanishing product"_) not source numbers.
- When tutorials, exams, or office-hours questions reveal a tricky question,
  edge case, or "what if" variant, absorb it into the canonical topic note
  under a descriptive subheading instead of leaving it in a detached collector
  or as a chapter-based memory cue.
- Keep companion notes at similar rigor when the mathematics genuinely mirrors,
  especially for continuous-time versus discrete-time analogues.
- If a general topic note starts accumulating a coherent subcluster — for
  example discrete-time representation methods, canonical sequence families, and
  periodicity rules — give that cluster one canonical home rather than leaving
  overlapping fragments in several files.
- Refresh matching `topic:` lines and short lecture-summary prose in
  `index.md` whenever a topic note grows materially deeper, even if its section
  anchors stay unchanged.
- If required theory lives only in an appendix or auxiliary PDF, absorb the
  content into topic notes and let the index point there. Attachments may remain
  as optional archival references, not the sole durable home.
- Lab-preparation decks and lab manuals should be treated as normal lecture
  ingestion: centralize definitions, circuit behavior, and worked examples in
  topic notes, then route lab or tutorial pages to those sections with `§`
  links and a small number of workflow or safety flashcards.

### Technical and mathematical notes

For mathematically substantive notes, the prose and flashcards should usually
include the governing formula, the derivation or proof sketch, the intuition for
the key step, and a worked example.

Key expectations:

- Explicitly compare related concepts students often confuse, such as message
  versus signal, discrete-time versus digital, energy versus power, or vertical
  versus horizontal transformations.
- When a note introduces an additive decomposition (DC/AC, even/odd,
  real/imaginary, and similar splits), include the decomposition formula, the
  derivation showing why the cross term vanishes, the orthogonality or zero-
  covariance interpretation, and at least one worked example.
- For finite windows or rectangular sequences, state endpoint conventions
  explicitly rather than leaving the reader to infer them from a step-function
  expression.
- In discrete-time oscillation notes, state the rational-versus-irrational
  periodicity test explicitly and include at least one example where the written
  digital angular frequency is not the sequence's fundamental digital frequency
  because digital frequency is defined modulo $2\pi$.
- When continuous-time and discrete-time examples are taught as counterparts,
  make the parallel explicit: what the impulse does initially, why the later
  dynamics become homogeneous, and how geometric versus exponential evolution
  line up.
- In ODE-based response notes, map the competing labels directly: homogeneous,
  particular, zero-input, zero-state, natural, forced, transient, and steady-
  state. Also state the caveat that zero-state response may require a homogeneous
  correction in addition to a particular solution.
- For transform and Fourier notes, keep the exact applied rule visible when a
  factor or sign matters. Do not write only “by duality” or “apply the
  convolution theorem” if the normalization could be forgotten.
- Preserve the practical Fourier-problem workflow the lecture uses: try
  linearity, differentiation or integration properties, and partial fractions
  before resorting to direct integration.
- In Fourier-series notes, treat the DC term explicitly rather than as “just
  another coefficient.” Explain why zero frequency has no positive/negative
  partner.
- When converting between cosine-sine and amplitude-phase form, include both the
  amplitude and phase formulas and a short geometric interpretation.
- Compare real trigonometric and complex exponential orthogonal-function sets
  explicitly when both appear in the lecture. If the lecture reaches that level,
  include a short Hilbert-space or Riesz-style interpretation with clear
  explanation rather than name-dropping.
- For real signals, note when a one-sided spectrum is valid and why the nonzero
  lines double while the DC line does not.
- In Parseval discussions, say explicitly that the exponential form is the most
  natural two-sided power sum, and explain the $1/2$ factor in real folded
  forms.
- For singular or generalized functions, describe how the graph is drawn, which
  parts are symbolic, and how ordinary pulse families approach the generalized
  object in the limit.
- For singular-signal notes, include formulas in common equivalent forms and
  state relations among nearby signal families such as step, ramp, gate, signum,
  impulse, and doublet.
- For doublet and impulse-derivative sampling rules, explain the sign intuition
  and contrast direct sampling with convolution.
- When a lecture uses differentiation or integration properties of convolution,
  include the higher-order operator view and at least one example where a
  differentiated kernel collapses into shifted impulses.
- For time-delay identities, give the formula, the graphical sliding-overlap
  intuition, the physical interpretation of delay, and the operator view
  $f(t-t_0)=f*\delta(t-t_0)$.
- For discrete-time convolution, connect the sum to continuous-time convolution
  of impulse trains and spell out the remaining differences: Kronecker versus
  Dirac delta, sum versus integral, stem plots versus impulse arrows, and any
  sample-period caveat.
- When presenting delta-sequence families, show the normalization or unit-area
  check explicitly.
- Explain test functions as smooth localized probes and say why smoothness and
  compact support are useful.
- Verify theorem hypotheses instead of copying a slide or appendix statement
  blindly. Prefer the standard theorem statement unless a stronger form is
  clearly intended and explained.
- For analysis-style appendix material, add geometric or probabilistic
  interpretation as well as formulas: box approximations, slicing intuition,
  indicator-function viewpoints, or event-region interpretations.
- When a computation appears in the prose, do not jump from setup to final
  answer; show the main intermediate step or strategy in both prose and
  flashcards.

### Honors and proof-heavy courses

Honors courses deserve more rigor, not merely more words.

- State hypotheses explicitly.
- Prefer short derivation or proof sketches to bare theorem statements.
- Break long arguments into a few logically separate paragraphs instead of one
  dense wall of text.
- Keep concrete examples and counterexamples in both prose and flashcards.
- When a theorem has a tempting but false overstatement, repair it in the note
  rather than copying the broken version from the source.
- When a concept has several equivalent formulations, list them explicitly and
  explain what each one means rather than leaving them as opaque labels.
- For measure-theoretic or probability-heavy notes, keep notation reader-facing:
  define the value space, sigma-algebra membership, pushforward notation,
  preimage notation, and any hybrid distribution notation before using it in a
  proof.
- When a proof naturally has a concrete layer and an abstract layer, teach both:
  for example, a direct event-based argument first and then the abstract
  pushforward or generator-based argument.
- For random-variable, distribution-function, and measure-equality notes,
  explain the criterion being used and why it is enough, rather than citing a
  theorem name without the proof idea.
- For auxiliary set systems such as pi-systems and Dynkin systems, compare them
  explicitly with sigma-algebras and make the disjointification trick readable.
- When the lecture uses a theorem operationally, also add “how to use it”
  guidance in prose and flashcards.

### Machine-learning notes

Machine-learning notes should preserve derivations, notation discipline, and the
distinction between modeling, optimization, and decision.

Use these defaults:

- Prefer _formula + derivation + intuition + caveat + worked example_ over a
  formula-only summary.
- Make assumptions explicit: IID status, priors, thresholds, intercept
  conventions, row/column roles, and whether a quantity is a loss, metric, or
  decision rule.
- Separate estimation from decision. For example, distinguish cross-entropy or
  likelihood fitting from Bayes-threshold classification.
- Keep true/source distribution $P$ and model/scoring distribution $Q$ distinct
  in entropy, cross-entropy, and Kullback-Leibler notes. Write the full formula
  triad when relevant.
- When conditional cross entropy or hybrid-joint notation appears, define the
  notation before invoking decomposition identities.
- Explain why empirical training loss carries a $1/N$ factor: it is an empirical
  expectation, not a decorative constant.
- In logistic-regression notes, explain odds, logit, coefficient interpretation
  on the odds scale, and any course-specific threshold convention together with
  common tie variants.
- In softmax-regression notes, prefer the general target-distribution form before
  the one-hot special case; include the categorical cross-entropy derivation,
  the binary $C=2$ reduction, the shared gradient memory rule `prediction minus
target`, and numerical-stability advice such as logsumexp or max-shift.
- If a course has both `classification.md` and `logistic regression.md`, prefer
  putting performance metrics in `classification.md`, including binary and
  multiclass macro, micro, and weighted formulas.
- When a lecture compares surrogate loss with classification error, include a
  concrete example where the two move differently.
- For convexity, bias-variance, or generalization notes, keep the target of each
  formula explicit and distinguish sample-specific from expected quantities.
- For optimization notes, include a practical by-hand update workflow and at
  least one tiny numerical example when appropriate.
- Distinguish per-sample SGD, minibatch SGD, and full-batch gradient descent
  explicitly.
- For deep networks, pair the repeated forward layer equation with a composition
  interpretation, and pair that with a backward local-error or transposed-
  Jacobian view.
- Define “signal” in initialization discussions in terms of activation or
  gradient scale, and explain fan-in/fan-out and variance flow.
- When discussing vanishing gradients, include at least a short chain-rule or
  norm-product derivation instead of leaving it as a slogan.
- Activation-function sections should compare nearby activations on both
  theoretical and empirical axes: boundedness, smoothness, saturation,
  monotonicity, zero-centering, dead units, optimization behavior, and compute
  cost.
- For backpropagation, define the local error explicitly and show how the same
  quantity yields both the incoming weight gradient and the propagated upstream
  error.
- For dropout, state clearly that activations are masked, not weights. Explain
  both non-inverted and inverted dropout conventions carefully and say which
  objects get rescaled and when.
- Distinguish **L2 regularization** from **weight decay** explicitly. L2 is an
  objective-level penalty; weight decay is an update-level shrinkage. State when
  they are equivalent under plain SGD and when they are not, especially for
  adaptive optimizers such as Adam. Mention AdamW when relevant.

### Physics, electronics, and lab notes

- When introducing notation or jargon such as $V_{CC}$, $V_{CE}$, or “low-side
  switch,” add a brief definition near first use so the note is readable without
  hidden course context.
- Circuit and electronics calculation cards should state topology, polarity,
  loop direction, and node naming if a diagram is not shown.
- Put image markup on the same source line as the end of the preceding
  paragraph.
- Add diagram-recall flashcards for key symbols or circuits when the diagram is
  itself a learning target.
- For signal-processing block-diagram questions, write the explanation as a
  stage-by-stage chain: identify the operation (for example carrier
  multiplication or filtering), name the resulting shifted or removed bands
  using the actual frequency landmarks from the figure when available, then
  state which component the LTI block preserves or rejects.
- If the course keeps diagram-generation scripts, keep docstrings descriptive
  enough for future maintainers to reconstruct topology and style.
- For common schemdraw-style circuit scripts, build the main rail first, save
  branch points explicitly, and use `.reverse()` on diode-like components when
  polarity requires it.
- IC power pins such as VCC and GND should be described generically unless the
  course fixes a specific supply value.

### Questions and problem-set pages

Questions pages (problem sets, practice exams, tutorial questions) use different
conventions from topic notes.

**Solution structure.** A well-structured solution follows a predictable skeleton:
decompose the target expression → apply the relevant bound, inequality, or theorem
→ evaluate the limit → state the conclusion. Organize each proof around this flow.

**Cloze granularity.** Each `{@{...}@}` should wrap one complete reasoning step
(claim + justification), not individual symbols or entire paragraphs. This keeps
each card reviewable without overwhelming the reader.

**Multi-cloze paragraph sequencing.** A single paragraph can contain many clozes
in sequence, each covering one short step:

```markdown
By {@{Chebyshev's inequality}@}, {@{$$P(\dots)\le\frac1{n^2\varepsilon^2}\sum\frac{m}{\log m}$$}@}.
Split {@{the sum at $\lfloor\sqrt n\rfloor$}@}: …
```

This creates a linear fill-in-the-blank review flow. Reserve separate paragraphs
with explicit markers (First, Second, Third) for longer independent sub-arguments.

**Blockquote formatting.** Place each official problem inside a blockquote (`>`).
Within a single blockquote, use `<p>` tags to create paragraph breaks. Between
adjacent blockquotes (separate problems), insert a blank line containing
`<!-- markdownlint MD028 -->` to suppress the adjacent-blockquote linter rule.

**Blockquote continuation discipline.** Every line inside a blockquote must
begin with `>` — including blank lines between display math and prose, blank
lines between paragraphs, and lines containing only display math delimiters.
A single blank line without `>` terminates the blockquote. This is the most
common Markdown formatting pitfall when writing multi-line solutions inside
blockquotes. The fix is simple: every empty line between `>` lines also needs
`>`:

```markdown
> $$f_X(x) = \lambda e^{-\lambda x}$$
>
> The CDF is obtained by integrating.
```

Not:

```markdown
> $$f_X(x) = \lambda e^{-\lambda x}$$

The CDF is obtained by integrating.
```

**Cloze-in-LaTeX rule.** `{@{ }@}` must never appear inside `$…$` or `$$…$$`
delimiters — pytextgen cannot parse them there. Instead, wrap the entire math
expression from outside: `{@{$\dots$}@}` or `{@{$$…$$}@}`.

**Technique-level clozes.** Cloze the name of the heuristic or method
(`{@{Swap sum order}@}`, `{@{the triangle inequality}@}`), not just the
algebraic outcome. This tests recognition of _which_ technique applies.

**Solution elaboration.** Show intermediate steps: include the antiderivative
and its evaluation, the geometric-series closed form, the factorial-ratio
simplification, etc. Do not jump from setup to final answer.

**Cross-referencing.** When a formula or technique derived in one problem is
reused in another, cite the earlier problem explicitly
(e.g., `(from Problem 2(b))`).

**Multi-paragraph blockquote math fix.** When a blockquote paragraph contains
display math (`$$…$$`) followed by more prose, the academic-notes validator may
flag `no_soft_wrap_paragraph`. Insert a blank blockquote line (`>`) between the
display math and the following prose to separate them into distinct paragraphs.

**Inline solution layout.** Within a single problem blockquote, place the
question text first, then a blank line, then `> Solution:` on its own line.
This keeps each prompt and its solution visually self-contained without
splitting into separate blocks.

**Topic orientation list.** Include a brief comma-separated topic list near the
top of the page (before the first problem) for quick scanning. This serves as a
compact table of contents.

**Source attribution for supplementary questions.** When the page includes
extra or externally sourced problem sets, separate them with `---` and add
`<!-- Source: <description> -->` on the next line.

**Multi-part labeling.** Label sub-answers as `(a)`, `(b)`, `(c)` inline within
the solution prose. Use a list format (`> - (a)`) inside the blockquote when
the parts are long.

**Key equivalence proofs.** When a solution relies on a non-trivial equivalence
(e.g., `F^{-1}(u)≤x ⇔ u≤F(x)`), include a brief two-direction proof using
`($\Rightarrow$) ... ($\Leftarrow$)` or `(⇐)` / `(⇒)` right after stating the
equivalence. Typically one direction uses a sup definition and right-continuity
argument, the other uses monotonicity.

**Case breakdown.** When the formula differs by parity, sign, or other
condition, use explicit headings like "For odd $n$, … For even $n$, …" with
separate formulas in each branch.

**Clozing bullet-list case splits.** When case splits are presented as a bullet
list, wrap each bullet's content in `{@{ }@}` while keeping the `-` prefix
outside. When a bullet states both a condition and its consequence, cloze them
as separate units: `- {@{condition}@}, giving {@{result}@}` (or `{@{so ...}@}`,
`{@{hence ...}@}`). This tests cause-effect reasoning within each case.

**Intuition-first for non-obvious proofs.** When a proof technique is not the
first thing a reader would think of, precede the algebraic derivation with a
brief "The intuition is that…" paragraph explaining the strategic insight. This
teaches _why_ one would choose the approach before showing _how_ it works,
building transferable problem-solving skills. For example, before the Hölder
manipulation in a Minkowski proof: "The intuition is that Minkowski's inequality
resembles the triangle inequality for norms; to prove it using Hölder, we need
to turn $\|f+g\|_p$ into a product so that Hölder applies."

**Prefer direct notation over unnecessary indirection.** Use quantities directly
(e.g., $E[Y\mid X]$) rather than introducing intermediate variables
(e.g., $\theta(X)=E[Y\mid X]$) unless the intermediate is reused multiple times
or significantly improves readability. Unnecessary indirection adds cognitive
overhead without clarifying the argument.

## Topic-specific notes

Create a topic note when a concept deserves a durable, reusable home. Topic
notes should read like compact encyclopedia entries: explanatory prose first,
then flashcards immediately after each section.

### Structure and naming

- Topic notes **must** use QA cards (`::@::` or `:@:`), not cloze `{@{ }@}`.
  Exception: accounting journal-entry worked examples embedded in topical notes
  may use cloze inside quoted scenarios, tables, calculations, and short
  explanations.
- Prefer concise, concept-based headings rather than mechanically copying slide
  titles.
- Use subsections only when they improve structure; if a subsection is tiny,
  consider merging it.
- Prefer lowercase filenames except for genuine proper nouns.
- Prefer the singular canonical concept name unless the concept is inherently
  plural by standard usage.
- Keep topic-note aliases to the canonical term and real synonyms; do not treat
  specific instances as aliases of the general concept.
- When linking to `general/`, use the canonical article title but do not create
  or edit the `general/` file as part of course-note work.
- In course topic notes, omit redundant filename, title, or delivery-context
  text from both prose and flashcard prompts. Do not use source files, slide
  decks, tutorial sheets, lab handouts, or temporary course artifacts as prose
  scaffolding unless the artifact itself is the subject. Use local prompts such
  as `definition` or `Bayes theorem finite`, not `probability measure /
definition` unless nested context requires it.

### Section-local flashcards

- Every section **and subsection** in a topic note must have its own `---` and
  flashcard block. Subsection flashcards must live under their own subsection
  heading, not under the parent section's flashcard block.
- The suppression reason "cards in parent section flashcard block" and other similar reasons for
  `header_flashcard_presence` are **not allowed**. If a subsection lacks its own
  flashcard block, add one.
- If a topic note has an overview section followed by representative example
  subsections, keep the detailed flashcards with the matching subsection rather
  than concentrating most of the cards at the end.
- When the prose only needs a small clarification or comparison, enhance the
  existing flashcards instead of spawning near-duplicates.
- When the prose gains a substantial cluster of distinctions, examples, or
  counterexamples, add new flashcards instead of overstuffing one old card.
- Do not insert explanatory prose between a section's horizontal rule (`---`)
  and `Flashcards for this section are as follows:`. Place any new prose above
  the `---` separator, or convert the clarification into flashcards, so the
  flashcard heading always remains directly under the separator.

- **Flashcard question phrasing.** Each `::@::` left-hand side must be a
  descriptive phrase that uniquely identifies the concept. Use a
  `category / specific-description` format, all on one line. Avoid terse labels
  like `Poisson process: definition` — the left side should be independently
  understandable. Examples from existing notes:
  - `Kolmogorov axiom (P1) / normalization ::@:: $P[\Omega] = 1$`
  - `algebraic properties / complement rule ::@:: $P[A^c] = 1 - P[A]$`
  - `continuity / continuity from below ::@:: If $A_1\subseteq A_2\subseteq\cdots$ then $P[\bigcup_j A_j] = \lim_{n\to\infty} P[A_n]$.`

- **Overview flashcard.** The first section's flashcard block must begin with an
  `overview ::@:: <single-sentence definition>` card. For other sections,
  consider an overview card at the start of that section's flashcard block as
  well.

- **Lint suppression comments.** Every `::@::` flashcard line MUST end with a
  trailing lint suppression comment, except when the card legitimately triggers
  a calculation warning that should not be suppressed. Standard patterns:
  - `<!-- check: ignore-line[two_sided_calc_warning]: conceptual -->` for
    conceptual cards (definitions, overviews, interpretations, examples without
    heavy algebra).
  - If a card contains explicit derivation steps, it may omit the
    `two_sided_calc_warning` suppression since the warning is legitimate there.
  - For headings that must capitalize a proper noun, suppress the header-style
    check on the line above:
    `<!-- check: ignore-next-line[header_style]: proper noun -->`.

- **Elaborated answers.** The right-hand side of a `::@::` card should include
  contextual framing beyond the bare formula. For proof-based cards, embed the
  key steps with "Derivation:" or "Proof:" inline. Examples:
  - `algebraic properties / inclusion-exclusion for two sets ::@:: $P[A\cup B] = P[A] + P[B] - P[A\cap B]$, proved by disjoint union $B = (A\cap B)\cup(B\setminus A)$ and additivity.`
  - `algebraic properties / why $P[\emptyset]=0$ ::@:: $P[\emptyset]=0$ from $\sigma$-additivity: $P[\emptyset] = P[\emptyset\cup\emptyset\cup\cdots] = \sum P[\emptyset]$.

- For "iff" theorems, embed both direction sketches in the same card so the
  reader can review the complete logical equivalence. Use "Proof sketch
  (forward direction):" and "Proof sketch (reverse direction):" markers
  within the right-hand side, separated by `<br/>`.`

- **Keep the same conceptual level.** Group cards by conceptual level; do not
  mix high-level conceptual cards with hyper-specific formula cards under the
  same heading.

### Journal entry examples in accounting topic notes

Accounting courses should place each journal-entry example in the most specific
topical note rather than defaulting to a course-wide `journal entries.md`
collector.

- Keep the explanatory concept prose and the worked journal-entry examples in
  the same topical section whenever practical.
- A worked example should usually live in a single blockquote: scenario,
  journal-entry table, then optional explanation or calculation.
- If one concept naturally needs several related entries (for example warranty
  provision plus settlement, or bond issue between coupon dates plus first
  coupon-date adjustment), keep that cluster together in the same topical
  section.
- Keep every journal-entry scenario, Dr/Cr table, and short calculation
  explanation above that section's local flashcard block. Once `Flashcards for
this section are as follows:` begins, the remainder of the section should be
  flashcards only until the next header.
- Use markdown tables with right-aligned Dr/Cr columns.
- Wrap the first-column header description and each account name in clozes.
- Mask all debit and credit amounts in the worked example with clozes and use
  `&nbsp;` as the thousands separator.
- Keep punctuation outside the closing cloze token: `{@{text}@}.`
- Warranty examples should allow settlement credits such as Cash, Inventory, or
  Accrued Payroll when appropriate.
- Service-type warranty examples should reflect revenue recognized over the
  service period rather than at the assurance-warranty stage.
- When distributing entries into topic notes, also update the relevant
  `index.md` links so readers are routed directly to the topical home.

## Questions pages

Question pages are not topic notes. They usually do not need the “Flashcards for
this section are as follows:” rubric.

Use these rules:

- For repository-authored review prompts, prefer ordinary headings and lists.
- For official course materials, use markdown blockquotes.
- If a page mixes official material with self-authored review prompts, keep the
  official content quoted and the self-authored content unquoted.
- If the file becomes too large, split it into `questions/index.md` plus smaller
  child pages such as tutorial weeks, problem sets, review sets, or exam blocks.
- **Topics line**: At the top of a questions page, include a `- topics:` line
  listing the major concepts covered (for example `- topics: medians of
distributions, sigma-algebras, CDFs`). This helps readers quickly identify
  the material tested.
- **Page description**: After the topics line, consider adding a paragraph
  describing the page's structure and pedagogical aim — for example, explaining
  which source materials were combined, what skill progression the questions
  build towards, or why certain topics are grouped together. This gives readers
  orienting context that a bare topic list cannot convey.
- **Original summary questions**: When a recurring technique or theme appears
  across multiple problems without a dedicated source question, consider
  creating an original summary question that synthesizes the pattern. Label it
  clearly as self-authored (ordinary prose rather than a blockquote) and place
  it alongside the official problems. This turns implicit heuristics into
  explicit, reviewable material.
- **Mastery-flow ordering**: Order problems by pedagogical progression rather
  than by source order: start with the foundational inequality or definition,
  then apply it to simple concrete cases, then build skill through multi-step
  examples, and finally tackle deeper or more abstract extensions. This creates
  a coherent narrative where each problem prepares the reader for the next.
- Keep naturally distinct official families distinct: tutorials, problem sets,
  practice exams, solution sheets, and so on.
- In official quoted questions, do not add manual numbering to the question
  line. If a question has subparts, use a quoted list inside the same blockquote.
- Use `Solution:` instead of `Solution sketch:` and include concise but complete
  solution logic.
- When the question has subparts, mirror that structure in the quoted solution.
- Keep cloze coverage meaningful in official quoted solutions: cover method,
  condition, and final result, not only equations.
- Do not hide only a variable name or re-hide a formula already visible in the
  prompt when a more explanatory cloze is available.
- When cleaning up low-value clozes, re-audit each quoted solution block so it
  still contains meaningful coverage.
- Prefer clozing a reasoning step together with its equation when they form a
  single proof step.
- **Cloze as logical implication**: When clozing solution steps, structure the
  visible text as the logical premise or framing (the method, condition, or
  known fact), and hide the conclusion, formula, or consequence that follows
  from it. This tests inference rather than isolated recall.
- **Attribution and inference words**: Connect each step with explicit reasoning
  language: "By [definition/theorem name]", "since [known condition]", "hence
  [consequence]", "substituting [expression] yields [result]".
- **Inline sub-answer labels**: When a question has subparts, label answers
  inline as `(a)`, `(b)`, etc. within the solution prose rather than using
  separate headings.
- **Explicit step decomposition**: For multi-step proofs, decompose with
  explicit markers: "First, show ...", "Second, show ...", "Third, ...". Label
  each logical chunk so the reader can follow the argument structure.
- Keep each quoted `Solution:` as one source paragraph line; avoid manual soft
  wrapping for that style.
- **Maximum-coverage cloze density for solution review.** On question/solution
  pages, clozes can be applied much more densely than on topic notes — wrap
  every substantive claim, formula, theorem reference, condition, and key term
  in its own `{@{ }@}`. This turns the prose solution into a complete
  fill-in-the-blank review tool. Each cloze still wraps a complete unit
  (one formula, one claim, one method), but the coverage is near-exhaustive
  across the entire solution.
- **Cloze separation of formula from prose interpretation.** When a LaTeX
  formula and its prose gloss appear together, wrap each in a separate cloze:
  `{@{$E[X]=\int_\Omega X\,dP$}@}` is `{@{the Lebesgue integral...}@}`.
  This tests both symbolic recognition and verbal understanding as distinct
  review items.
- **True/false answer structure.** For "Decide whether true or false"
  questions, use this pattern: false statements get **False.** followed by a
  concrete counterexample with explicit distributions, computation of both
  sides, demonstration that they differ, and a conceptual takeaway. True
  statements get **True.** followed by a reference to a prior result or known
  theorem and brief justification.
- **Cloze of multi-name results.** When a result has two equally common names
  (e.g., "tail-sum formula" / "layer-cake representation"), cloze both names
  together so the reader learns the connection: `{@{the layer-cake
representation (or tail-sum formula)}@}`.
- **Visual breaks in single-line source**: Use `<p>` for paragraph breaks and
  `<br/>` for line breaks inside single-line source paragraphs. This keeps
  the markdown source continuous (no hard line breaks) while producing visual
  separation in the rendered output.
- For consecutive quote blocks, prefer local MD028 control comments instead of a
  global suppression.
- **Progressive elaboration**: Start each solution step with the core idea or
  method, then expand the algebra only where a typical reader would need to
  write down an intermediate rearrangement. Show the expression after a
  substitution, integration, or algebraic manipulation before stating the
  result, but do not pad with trivial steps.
- **Cross-reference between problems**: When the same formula, trick, or
  theorem powers two solutions, cite the earlier problem by number (for
  example `(from Problem 2(b))`). This builds a proof dependency graph
  that rewards cumulative study.
- **Result-cloze heuristic**: Prefer clozing the _result_ or _takeaway_ of a
  derivation rather than the algebraic steps that produced it. The visible
  premise carries the method or condition; the hidden part holds the
  conclusion or formula that follows.
- **Technique-level clozes**: Cloze not only the answer but also the name of
  the heuristic or technique that was used to get there (for example
  `{@{Swap sum order}@}` or `{@{completing the square}@}`). This tests
  whether the reader can recognize _which_ method applies — a key
  problem-solving skill — rather than just recalling the mechanical result.
- **Cloze density**: Aim for roughly 2–4 clozes per subquestion — enough to
  test recall of the headline formulas without making the card unanswerable.
- **Progressive cloze density across multi-problem pages**: On pages with
  several problems, consider using dense step-by-step clozes on the first
  problem (testing each mathematical move independently) and progressively
  sparser clozes on later problems (testing only the final closed-form or key
  insight). This builds foundational fluency on the first pass and then tests
  independent application on subsequent passes. For example, in a 5-problem
  tutorial, the first problem might cloze every reasoning step while the last
  problem may only cloze the bottom-line result.
- **Source anchoring**: When official problem-set PDFs or source extracts
  exist, verify solution content against the original. Restore dropped context
  paragraphs, limit definitions, and precise subquestion wording that a
  paraphrase may have lost.
- **Group separator with source annotation**: When a page draws from multiple
  source documents, group problems from the same source together and separate
  groups with `---` followed by `<!-- Source: <description> -->`. This keeps
  provenance clear without cluttering individual problem blocks.
- **Alternative-solution labeling**: When a question admits multiple solution
  methods (for example Jacobian vs. CDF approach for a transformation),
  present each as a labeled alternative inside the solution block. Use a bold
  header such as `**Alternative (method name):**` or
  `**Alternative (approach, per hint):**` to separate them. This shows
  readers the equivalence between techniques and reinforces when each method
  is natural to apply.
- **Recall anchors for prerequisites**: At the start of a solution that
  depends on a prerequisite distribution, identity, or function (for example
  the gamma function, the Beta function, or the MGF of a named distribution),
  include a compact reminder in parentheses: `(Recall the gamma function
$\Gamma(\alpha)=\int_0^\infty u^{\alpha-1}e^{-u}\,du$ ...)`. This keeps the
  solution self-contained and reduces friction during spaced-repetition
  review.
- **Self-contained inequality statements in problem prompts**: When a problem
  asks to prove or apply a named inequality, theorem, or definition, state the
  full mathematical statement in the question body — not just the name. For
  example, instead of "Prove the finite weighted Jensen inequality," write
  "Prove the finite weighted Jensen inequality: for convex $\varphi$ and
  weights $\lambda_i>0$ with $\sum_i\lambda_i=1$,
  $\varphi(\sum_i\lambda_i x_i)\le\sum_i\lambda_i\varphi(x_i)$." This
  makes the prompt self-contained for spaced-repetition review and doubles as a
  flashcard cue.
- **Display math merged onto same blockquote line**: When a solution step
  uses display math inside a blockquote, merge concluding text and the display
  math onto the same blockquote source line (e.g.
  `> The quadratic form simplifies to $$...$$`). This avoids triggering the
  `no_soft_wrap_paragraph` validator rule while keeping the math visually
  clear. The text before the math serves as a logical premise or label for the
  expression that follows.
- **Cloze layering**: Within a single solution step, chain multiple clozes at
  different conceptual levels to test the full reasoning chain: first clozed
  the theorem or method name (`{@{by the spectral theorem}@}`), then the key
  formula (`{@{$\Sigma=Q\Lambda Q^\top$}@}`), then the conclusion that follows
  (`{@{the density integrates to 1}@}`). This tests recall of the method, its
  mathematical expression, and the logical consequence — a deeper form of
  active recall than testing any one layer alone. Combine with `<p>` and
  display math so the reasoning chain is both testable and readable.
- **Casewise answer packaging via indicator functions**: When a solution
  yields different values on different subsets of the sample space, package
  the answer concisely using indicator functions rather than listing cases with
  prose labels or footnotes. For example,
  `$E[X\mid Y]=\frac{r}{p}\mathbf 1_{\{Y=1\}}+\frac{p-r}{1-p}\mathbf 1_{\{Y=0\}}$`.
  This keeps the result compact, self-contained, and directly testable via
  cloze — the reader must match each indicator condition to its expression.
- **Progressive difficulty: simple case first, then extend**: When a question
  has multiple cases of increasing complexity (e.g., square matrix $A$, then
  non-square $A$), solve the simpler case completely first, then open the
  harder case with wording like "For [harder case], extend/apply [the simpler
  result]...". This rewards cumulative understanding and lets readers verify
  their grasp before moving on to the generalization.

### Canvas quiz conversions

When a Canvas quiz is converted into notes, use a paired public/private layout
rather than trying to make one page serve both goals.

- Put the public pedagogical page at
  `special/academia/<INSTITUTION>/<COURSE>/questions/quiz N.md` with an active
  flashcard tag and a `## hints` section.
- Put the private archival page at the mirrored private path with an archive
  flashcard tag and a `## content` section.
- Do not keep a parallel `assignments/online quiz N/index.md` stub once the
  quiz has a home in `questions/`. Even if the LMS exposes the quiz through an
  assignments-style route, the repository should keep quiz families together
  under `questions/`. For the structure of actual assignment-style pages (as
  opposed to quiz pages), see the
  [assignment-creation](../assignment-creation/SKILL.md) skill.
- Preserve the common quiz metadata in both pages when it is visible in the
  source: due datetime, points, number of questions, availability window, time
  limit, and allowed attempts.
- Public quiz pages should transform the official quiz into review material:
  recognition rules, conceptual hints, compact worked reminders, and active
  recall prompts. Keep the public `## hints` in the same order as the
  archived/private question order even if individual hints are later rewritten
  to be more conceptual. Do **not** copy the full official question set
  verbatim into the public page when a private archival page exists.
- If only quiz timing or schedule metadata is known and the question content has
  not been archived yet, keep a minimal placeholder page in `questions/quiz
N.md` rather than opening a separate assignments stub (for which the
  [assignment-creation](../assignment-creation/SKILL.md) skill is the
  appropriate reference). Make the placeholder explicit about the missing
  archived content.
- Private quiz pages should preserve the official prompt text as faithfully as
  practical, usually in blockquotes, together with the archived answer state.
  Do not add a stock boilerplate paragraph at the start of `## content`; begin
  directly with the questions unless the page needs a genuinely specific caveat
  about missing source context.
- If the archived source explicitly shows correctness, grading feedback, or an
  official solution, label the answer line as `- solution:`.
- If the archived source only shows a checked option or stored attempt state,
  do **not** overclaim correctness. Use labels such as `- archived selection:`
  or `- selected answer:` instead of asserting a solution.
- If the user later confirms that the archived checked options are indeed
  correct, you may promote those answer lines to `- solution:` even if the raw
  screenshot itself only showed a checked state.
- When a private quiz page records confirmed solutions, add a short explanation
  bullet for each question. That explanation should carry meaningful cloze
  coverage of the governing method, condition, distinction, or inference step;
  do not stop at a bare clozed final option if the reasoning can be stated
  concisely.
- Once a private quiz page promotes an archived answer to a confirmed solution,
  keep the prompt, `Solution:`, and `Explanation:` inside one continuous quoted
  question block rather than placing `- solution:` or `- explanation:` bullets
  outside the quote. This keeps the archival unit visually intact and matches
  the normal quoted-solution style used elsewhere in official question pages.
- Keep the explanatory cloze coverage even for image-based quiz questions.
  Embedding the actual figure does not replace the flashcard duty of the text:
  the quoted `Explanation:` should still cloze the governing method, landmark,
  contrast, or decision rule that makes the pictured answer correct.
- If the quoted `Solution:` line itself contains an embedded image, keep at
  least one cloze on that same `Solution:` line as well. Cloze the chosen
  option number, the correct branch or topology label, or a short structural
  descriptor of the pictured answer so the solution is directly reviewable even
  before the reader reaches the explanation.
- For image-based quiz questions, prefer extracting the actual figure payloads
  from archived HTML snapshots into a local quiz `attachments/` folder and
  embedding them with Markdown image syntax inside the private archival page.
  Preserve the original Canvas-exported filenames such as `Q2_1.jpg` when they
  are available so the note remains traceable back to the source archive.
  Replace placeholder lines like `prompt figure: Q2_1.jpg` with the real image
  embed once extraction succeeds.
- If multiple archived snapshots exist, prefer the one that still contains the
  real question-body image payloads rather than a later protected-results shell.
  Only fall back to textual figure identifiers when the archive truly lacks an
  extractable image payload.
- Keep the public quiz page pedagogical even when the private page embeds the
  real figures: preserve conceptual hints and active-recall prompts on the
  public side instead of copying the full official image-heavy prompt verbatim.
  Keep those hints close enough to the original quiz that a reader can still
  recognize the target question: preserve the option family, named theorem,
  transform form, timing pattern, or essential band-edge geometry when that
  anchor helps. When the user asks for more context, add it mainly on the left-
  hand prompt itself: use option-family cues, mutated-but-equivalent givens, or
  decisive spectral, timing, or topology landmarks without reproducing the
  official choices verbatim. Prefer general reasoning cues first, and use
  alternate-number toy equations only when they clarify the same method better
  than a direct but still non-verbatim hint would.
- If the validator still expects an activation flashcard tag on a private
  archive-only quiz mirror, prefer a local
  `ignore-file[metadata_flash_tag]: private archival quiz mirror` suppression
  over adding a fake active tag.
- If a quiz question is image-based and extraction is impossible, preserve the
  available figure identifiers or a short description of the figure dependence
  so the archival page still records what was shown.
- Keep public and private basenames aligned, for example `quiz 1.md` on both
  sides.
- When a course accumulates multiple converted quizzes, add a public
  `questions/index.md` collection page that lists the quiz review pages. The
  private mirror usually stays as a flat quiz-file collection unless the user
  asks for a private index explicitly.

<!-- assignment-style leaf pages moved to `.agents/skills/assignment-creation/SKILL.md` -->

## Flashcards and markup

The repository supports only three flashcard patterns:

- **Cloze**: `{@{hidden text}@}`
- **Two-sided QA**: `term ::@:: definition`
- **One-sided QA**: `term :@: answer`

Core rules:

- Cloze syntax is strict: `{@{` opens and `}@}` closes. No nesting, no
  multiline clozes, and no `}}` pseudo-closing token.
- Do **not** place clozes inside existing math delimiters. If you want to hide
  an equation, cloze the entire equation from outside.
- Topic notes **must** use QA cards (`::@::` or `:@:`) over cloze (`{@{ }@}`)
  in prose. Cloze flashcards `{@{ }@}` are **not allowed** in topic notes. The
  only exception is embedded accounting journal-entry worked examples, which
  may use cloze in their quoted scenarios, tables, calculations, and short
  explanations.
- Flashcards must be self-contained. Repeat givens, hypotheses, notation, and
  any relevant diagrams if the card would otherwise be ambiguous.
- For mathematical prompts, LaTeX on the left-hand side is acceptable when it is
  the natural statement of the prompt.
- For derivation or approximation clusters, descriptive left-hand prompts are
  often better than dumping the whole derivation on the left.
- Use one or two focused ideas per card unless the method is naturally short and
  unified.
- Nested flashcard bullets must indent by exactly two spaces per level and
  include the full in-file parent path.
- Calculation cards must keep all givens on the left; do not shorten them by
  removing data.
- Keep the right-hand side single-line in source and use `<br/>` for internal
  structure.
- In accounting QA cards, use `<br/>` to separate distinct journal entries,
  dates, or accounting steps — not every individual Dr/Cr line inside one
  journal entry. Keep one entry grouped together with commas or semicolons
  unless line-by-line separation is itself the learning target.
- Units should stay inside math delimiters, for example `$5\text{ V}$`.

## LaTeX conventions for mathematical notes

Use these conventions for consistent notation in mathematical notes:

- **Distribution names**: Use `\operatorname{Bin}`, `\operatorname{Cau}`,
  `\operatorname{Exp}`, `\operatorname{Poi}`, etc. for named distributions.
- **Indicator functions**: `\mathbf 1_A(x)` or `\mathbb 1_A(x)`.
- **Left and right limits**: `\lim_{y\uparrow m}` and `\lim_{y\downarrow m}`.
- **"Distributed as"**: `\sim` (e.g., `$X\sim N(0,1)$`).
- **Binomial coefficients**: `\binom{n}{k}`.
- **Piecewise definitions**: `\begin{cases}` with `[2pt]` vertical spacing
  between cases.
- **Multi-letter operators**: Use `\operatorname` rather than plain text for
  multi-letter operators like `CDF`, `PDF`, `Var`, `Cov`, `E`, `MSE`.
  In probability notes, use `\operatorname{E}[X]` for expectation and
  `\operatorname{Var}(X)` for variance (rather than bare `E[X]` or `\mathbb E`).

## Validation suppressions

Prefer fixing the content over suppressing the validator. When suppression is
truly necessary, use one of these forms with a short rationale:

- `ignore-line[rule_id]`
- `ignore-next-line[rule_id]`
- `ignore-file[rule1, rule2]`

Additional rules:

- Line and next-line suppressions apply only to their local target.
- File-level suppressions are for genuine special cases, such as assignment-style
  index pages (see the [assignment-creation](../assignment-creation/SKILL.md)
  skill) that intentionally omit the normal `# index` / `children` shell.
- Do not add a file-level suppression for a rule that never fires in the file;
  that is redundant.
- Do not place more than one directive of the same type on the same line; merge
  rule IDs into one directive when needed.
- If a rule such as `numeric_text_not_latex` keeps firing on room identifiers,
  percent-encoded link destinations, inline code, or HTML comments, treat that
  as a validator bug: mask the non-prose span or refine the rule instead of
  scattering repeated suppressions through course notes.
- The suppression reason "cards in parent section flashcard block" and other similar reasons are **not valid** for `header_flashcard_presence`. Every subsection must have its own flashcard block.
- Conceptual law cards may justify a local suppression when a descriptive prompt
  is pedagogically stronger than a formula-heavy calculation prompt.

## Filenames, titles, links, and external lookups

- Prefer lowercase filenames unless a proper noun requires capitalization.
- Use `%20` in markdown links but do not percent-escape actual filenames.
- Topic-note filenames should normally follow the singular canonical concept.
- When linking to `general/`, prefer the canonical article title and the correct
  relative path, but do not create or edit the `general/` file automatically.
- Use the Wikipedia helper only to discover canonical titles.

## Validator and tooling

Use the validator as the structural authority for this skill.

The validator location is fixed: `.agents/skills/academic-notes/check.py`.
Do **not** recurse through `.agents/skills/academic-notes/`, list the whole
folder, or search the entire workspace just to locate it. Run the fixed path
directly and pass the smallest relevant course-note path.

```shell
# POSIX shell
uv run .agents/skills/academic-notes/check.py special/academia/<institution>/ELEC\ 1100

# Windows PowerShell or cmd
uv run .agents/skills/academic-notes/check.py "special/academia/<institution>/ELEC 1100"

# Validate a single file instead of a whole course when possible
uv run .agents/skills/academic-notes/check.py "special/academia/<institution>/ELEC 1100/index.md"
```

Rules of thumb:

- Validate the **smallest relevant scope only**.
- Do **not** run the validator on the repository root, the whole workspace, or
  the entire skill folder.
- Common failures include missing tags, missing `datetime`, invalid headings,
  broken section-card structure, duplicate week numbers, exams placed too early,
  and malformed cloze syntax.
- Common index-related rules include `index_children_order`,
  `index_children_missing`, and `index_children_missing_index`.
- Common cloze-related rules include `cloze_open_close_matching`,
  `cloze_wrong_closing_token`, `cloze_single_line`, and `cloze_no_nested`.
- Common math-layout rules include `latex_block_no_newline`,
  `latex_not_standalone`, and `no_soft_wrap_paragraph`.

### Developer tooling and tests

- Validator and helper tests for this skill live in
  `.agents/skills/academic-notes/tests_a7392be/`.
- If you extend validator behavior or helper scripts in this skill folder, add
  or update tests there.
- When you change repository-level tooling that processes course notes more
  broadly, repository-level tests may still belong under `tests/`; choose the
  smallest scope that matches the code being changed.
- After structural fixes, run repository formatting, checks, and tests on
  explicit paths when practical.

### Extending the validator

When prose guidance is not enough, extend the validator instead of relying on
repeated suppressions.

1. Add a new pure rule in `check_mods/rules.py` and register it with
   `@RULE_REGISTRY.register()`.
2. Add matching tests in `tests_a7392be/check_mods/test_rules.py` or the most
   relevant test module in `tests_a7392be/`.
3. Run the validator or tests against representative notes.
4. Document the new rule briefly here or in the instruction/template if authors
   need guidance when it fires.

## Related skills

- [assignment-creation](../assignment-creation/SKILL.md) — Creating and
  maintaining assignment pages (problem sets, homework, project milestones)
  under `assignments/`, including directory structure, Canvas metadata, and
  solution conventions.

## Continuous improvement

Keep the skill concise, authoritative, and aligned with the validator.

- If a durable lesson appears, update `SKILL.md`, `course-template.md`, the
  instruction file, and tests in the same task when appropriate.
- Do not use persistent memory as a second documentation system for academic-
  notes conventions.
- Prefer editing the validator when the issue is structural and recurring.
- Keep changes focused and reviewable; avoid broad mechanical rewrites unless
  they clearly improve the guidance structure.

### Workflow for agents

1. Identify whether the lesson belongs in prose, the template, or the validator.
2. Update the authoritative file immediately rather than leaving a side note.
3. If the issue is structural, teach the validator and add a test.
4. Re-run the relevant validation or tests on the affected scope.
