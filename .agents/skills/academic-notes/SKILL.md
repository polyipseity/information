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
   source line, and avoid putting LaTeX inside emphasis. Accounting notes should
   avoid LaTeX entirely.
9. **Keep headers and emphasis consistent.** Topic-note headers should normally
   be lowercase except for proper nouns; prefer `_italic_` and `__bold__`.
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
- Place `assignments/` immediately after `children` and before session entries
  when the course has an assignments section.
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
- Administrative exam information may be ordinary prose; do not force it into
  flashcards or bullets unless the user wants that style.

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
- Do not use unresolved chapter numbers as substitutes for links when no
  chapter-page artifact exists in the repository.
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
- If the course keeps diagram-generation scripts, keep docstrings descriptive
  enough for future maintainers to reconstruct topology and style.
- For common schemdraw-style circuit scripts, build the main rail first, save
  branch points explicitly, and use `.reverse()` on diode-like components when
  polarity requires it.
- IC power pins such as VCC and GND should be described generically unless the
  course fixes a specific supply value.

## Topic-specific notes

Create a topic note when a concept deserves a durable, reusable home. Topic
notes should read like compact encyclopedia entries: explanatory prose first,
then flashcards immediately after each section.

### Structure and naming

- Use QA cards, not cloze, in topic notes other than `journal entries.md`.
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
- In course topic notes, omit redundant filename or title text from flashcard
  prompts. Use local prompts such as `definition` or `Bayes theorem finite`, not
  `probability measure / definition` unless nested context requires it.

### Section-local flashcards

- Every section in a topic note should have its own `---` and flashcard block.
- If a topic note has an overview section followed by representative example
  subsections, keep the detailed flashcards with the matching subsection rather
  than concentrating most of the cards at the end.
- When the prose only needs a small clarification or comparison, enhance the
  existing flashcards instead of spawning near-duplicates.
- When the prose gains a substantial cluster of distinctions, examples, or
  counterexamples, add new flashcards instead of overstuffing one old card.

### Journal entries note for accounting courses

Accounting courses should maintain a dedicated `journal entries.md` topic note.

- One journal-entry type per `##` section.
- Each worked example lives in a single blockquote: scenario, journal-entry
  table, then optional explanation or calculation.
- Use markdown tables with right-aligned Dr/Cr columns.
- Wrap the first-column header description and each account name in clozes.
- Mask all debit and credit amounts with clozes and use `&nbsp;` as the
  thousands separator.
- Keep punctuation outside the closing cloze token: `{@{text}@}.`
- Warranty examples should allow settlement credits such as Cash, Inventory, or
  Accrued Payroll when appropriate.
- Service-type warranty examples should reflect revenue recognized over the
  service period rather than at the assurance-warranty stage.

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
- Keep each quoted `Solution:` as one source paragraph line; avoid manual soft
  wrapping for that style.
- For consecutive quote blocks, prefer local MD028 control comments instead of a
  global suppression.

## Assignment-style leaf index pages

Some leaf folders represent a single Canvas or LMS assignment-like artifact,
such as a lab round, homework, quiz handout, project milestone, or similar
deliverable page with local attachments.

Use these rules when the source is a Canvas assignment HTML page:

- Keep the visible Canvas wording verbatim in the description body.
- Preserve color with `<span style>` and use Markdown for bold, italics,
  links, paragraphing, and line breaks.
- Treat the Canvas title header as metadata inside `## description`, not as a
  Markdown heading. The first property in that section should be exactly
  `- title: <Canvas title header verbatim>`.
- For these assignment-style leaf indexes, use this section order:
  index metadata (with no extra `---` after the parent line), `## children`,
  `## description`, `## attachments`, `## submission`, and `## solution`.
- Omit generic `## logistics` and `## overview` sections on these pages.
- Include an explicit attachments list pointing to the local `attachments/`
  files.
- Leave `## submission` and `## solution` empty until actual repository
  content is provided.

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
- Topic notes other than `journal entries.md` should prefer QA cards over cloze
  in prose.
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
- Units should stay inside math delimiters, for example `$5\text{ V}$`.

## Validation suppressions

Prefer fixing the content over suppressing the validator. When suppression is
truly necessary, use one of these forms with a short rationale:

- `ignore-line[rule_id]`
- `ignore-next-line[rule_id]`
- `ignore-file[rule1, rule2]`

Additional rules:

- Line and next-line suppressions apply only to their local target.
- File-level suppressions are for genuine special cases, such as assignment-style
  index pages that intentionally omit the normal `# index` / `children` shell.
- Do not add a file-level suppression for a rule that never fires in the file;
  that is redundant.
- Do not place more than one directive of the same type on the same line; merge
  rule IDs into one directive when needed.
- If a rule such as `numeric_text_not_latex` keeps firing on room identifiers,
  percent-encoded link destinations, inline code, or HTML comments, treat that
  as a validator bug: mask the non-prose span or refine the rule instead of
  scattering repeated suppressions through course notes.
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
