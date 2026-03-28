---
name: academic-notes
description: Content conventions, examples, and tooling for course notes under special/academia.
---

# Academic notes — consolidated skill

This skill is the authoritative guide for creating and maintaining course notes under `special/academia/<INSTITUTION>`. Read it before editing academic notes. Flashcards are generated automatically by the build system; do **not** run `init generate` manually.

## Skill folder map

- `SKILL.md` — authoritative workflow and policy reference.
- `course-template.md` — scaffold for new course `index.md` pages.
- `check.py` + `check_mods/*` — validator entry point and rules.
- `find_wikipedia.py` — title-discovery helper for canonical `general/` article names.
- `tests_a7392be/*` — tests for validator and helper behavior.

## Key principles

1. **Content first.** Capture the lecture's actual ideas, definitions, formulas, examples, and instructor remarks as complete prose or structured bullets.
2. **Keep prose and flashcards synchronized.** Whenever you add, remove, split, merge, or rename content, update the corresponding flashcards in the same edit.
3. **Treat flashcards as standalone artifacts.** Restate the local hypotheses, notation, and conditions needed for correctness.
4. **Respect metadata and chronology.** Use YAML frontmatter, ISO‑8601 datetimes, valid `children:` lists, and chronological session ordering; keep exams after regular sessions.
5. **Use skill files, not memory, as the source of truth.** Durable lessons belong in `SKILL.md`, `course-template.md`, related instructions, and tests.
6. **Keep math clean.** Use `$...$` or `$$...$$`, keep math on one source line, and do not put math in code fences. In accounting notes, avoid LaTeX and use plain text instead.
7. **Keep headers and emphasis consistent.** Topic-note headers should normally be lowercase except for proper nouns; use `_italic_` and `__bold__` rather than asterisks.
8. **Validate immediately and narrowly.** Run `uv run .agents/skills/academic-notes/check.py` after edits, targeting only the relevant course directory or file.
9. **Prefer one durable home per concept.** Enhance existing notes and add section links before creating overlapping new notes.
10. **For honors or proof-heavy courses, raise the rigor.** State hypotheses explicitly, include proof sketches or derivation skeletons, keep concrete examples and counterexamples, and prefer the quartet _formula + derivation + intuition + worked example_ for technical notes.

## Authoring workflow

Use this workflow whenever you add or revise course content.

1. Start from `course-template.md` when creating a new course `index.md`.
2. Fill frontmatter carefully: aliases, tags, course name, credits, and description.
3. Add `logistics` with grading and chosen-section metadata.
4. Maintain `children:` in teaching order and keep links current.
5. Write explanatory prose first; add flashcards after the prose is accurate.
6. Update related `index.md` anchors and section links in the same pass.
7. Run the validator and fix both errors and warnings before moving on.
8. Before finishing, check the note once as a reader and once as a flashcard consumer.

### Adding new lecture content

Before creating a new topic note, classify the incoming material:

- **Duplicate** → do not create a new note; add a section link to the existing material.
- **Enhancement** → extend the existing note and update its flashcards and session links.
- **New** → create a new note only when the concept has no suitable home yet.

Also follow these rules:

- Absorb theory from appendices or auxiliary PDFs into topic notes; do not leave required content stranded in attachments.
- Verify theorem hypotheses and prefer the standard theorem statement unless a stronger version is clearly intended and explained.
- For analysis or calculus background, include intuition as well as formulas: geometry, slicing, box approximations, or event-region interpretations where relevant.
- Keep worked examples computationally visible: show the main setup, order of computation, and the key step, not just the final answer.
- Prefer one rich, answerable card to several brittle micro-cards when the reasoning is naturally short.
- For mathematically structured machine-learning notes, include at least one worked example and one derivation or proof sketch when the lecture supports them.

### Machine-learning note refinement checklist

- Use **formula + derivation + intuition + caveat** rather than formula-only summaries.
- Make assumptions explicit: IID status, priors, thresholds, intercept conventions, row/column roles, and whether a quantity is a loss, metric, or decision rule.
- Distinguish estimation from decision, especially in probabilistic classification notes.
- Distinguish true distribution $P$ from model/scoring distribution $Q$ in entropy, cross-entropy, and Kullback-Leibler discussions.
- Include the shared output-layer memory rule `prediction minus target` where it applies.
- For softmax, include the cross-entropy form, index meanings, and numerical-stability guidance such as logsumexp or max-shift.
- For deep networks, pair the forward repeated-composition view with the backward local-error or transposed-Jacobian view.
- Compare activation families on both theoretical and empirical axes.
- Explain graph-based intuition explicitly: axes, curve shapes, spread across runs, and what the graph means.
- Distinguish per-sample SGD, minibatch SGD, and full-batch gradient descent explicitly when optimization updates are discussed.

### Pre-commit checklist

- YAML frontmatter is present and valid.
- `aliases` are sorted and `tags` include the correct flashcard activation tag.
- `index.md` has `# index` and a valid `children` section when appropriate.
- Sessions are chronological; exams come last.
- Topic-note sections each have their own flashcard block and separator.
- `questions/`, `assignments/`, and `attachments/` are used consistently.
- No instructor or TA names or email addresses appear in notes.
- Any changed topic-note headings have matching updated section links in `index.md`.
- Validator, formatting, checks, and tests have been run on explicit paths.

### Session and index rules

- After the course list (`institution`, `name`, `credits`), insert `---` before the description.
- Under `sections:`, use one key per stream type for the **chosen** section only, then list all section IDs under that key.
- Session headings must be exactly `## week N lecture`, `## week N lecture 2`, `## week N lab`, or `## week N tutorial` (same rule for numbering). Put holidays or cancellations in metadata, not in headings.
- Use `status: public holiday: <name>` or `status: no class` for no-class days; omit `topic:` on those days. `status: unscheduled` also requires omitting `topic:`.
- Weekly session metadata must match the chosen lecture/tutorial/lab stream.
- Session-level flashcards in the index are optional; use them only for genuinely testable content, not scope summaries.
- For topic notes referenced by a session, link the note as a parent bullet and the covered sections as indented `§` links beneath it.
- On review/question pages, use ordinary headings and lists for self-authored material and markdown blockquotes for official course material.
- Split large `questions.md` files into `questions/index.md` plus child pages when needed, and keep official question families (tutorials, problem sets, exams, solutions) distinct.
- In official quoted questions, avoid manual numbering in the question line, use `Solution:`, keep subparts as quoted lists, and maintain useful cloze coverage on both method and result.

## Flashcards and markup

The repository supports only three flashcard patterns:

- **Cloze**: `{@{hidden text}@}`
- **Two-sided QA**: `term ::@:: definition`
- **One-sided QA**: `term :@: answer`

Core rules:

- Cloze syntax is strict: opening token `{@{`, closing token `}@}`; no nesting; no multiline clozes.
- Do **not** place clozes inside existing math delimiters. If you want to hide an equation, cloze the entire equation from outside.
- In topic notes other than `journal entries.md`, prefer QA cards and avoid cloze in prose.
- Flashcards must be self-contained. Repeat givens, hypotheses, notation, and any relevant diagrams if the card would otherwise be ambiguous.
- For mathematical or derivation-heavy prompts, LaTeX on the left-hand side is acceptable when it is the natural way to state the prompt.
- For derivation or proof clusters, use a descriptive left-hand label and keep the important formulas on the right.
- Use one or two focused ideas per card unless the method is naturally short and unified.
- Nested flashcard bullets must indent by exactly two spaces per level and include the full in-file parent path.
- Calculation cards must keep all givens on the left; do not shorten them by removing data.
- Circuit or electronics calculation cards must state topology, polarity, direction, and node naming if a diagram is not included.
- Keep the right-hand side single-line in source; use `<br/>` for internal structure instead of lists.
- Every section in a topic note must have its own `---` and flashcard block. Index files and question pages are exempt.
- Keep units inside math delimiters, for example `$5\text{ V}$`.

Minimal examples:

```markdown
## week 3 lecture

- datetime: 2025-09-16T12:00:00+08:00/2025-09-16T13:20:00+08:00, PT1H20M
- topic: polymorphism; type bound; variance
- COMP 3031
  - COMP 3031 / polymorphism ::@:: Parametric polymorphism and subtyping polymorphism.
```

```markdown
---

Flashcards for this section are as follows:

- example power calculation: Given a $200\,\Omega$ resistor with $5\text{ V}$ across it, what power is dissipated? ::@:: Use $P=V^{2}/R$ to get $0.125\text{ W}$.
```

## Topic-specific notes

Create a topic note when a concept deserves a durable, reusable home. Topic notes should read like compact encyclopedia articles: explanatory prose first, flashcards immediately after each section.

- Use QA cards, not cloze, except in `journal entries.md`.
- Prefer concise, concept-based headings rather than copying slide titles mechanically.
- Use subsections only when they improve structure; if a subsection is tiny, consider merging it.
- Keep notes and the course index synchronized: when headings change, update the corresponding `§` links.
- In optimization notes, distinguish **L2 regularization** from **weight decay** explicitly. L2 regularization is an objective-level penalty such as $L(\theta)+\frac{\lambda}{2}\lVert\theta\rVert_2^2$ (or $L(\theta)+\lambda\lVert\theta\rVert_2^2$ under a different coefficient convention), whereas weight decay is an update-level multiplicative shrinkage such as $\theta_{t+1}=(1-\eta\lambda)\theta_t-\eta\nabla L(\theta_t)$. State clearly when they are equivalent under plain gradient descent / stochastic gradient descent, note the factor-of-$2$ convention when the loss omits $\frac{1}{2}$, and also state clearly when they are **not** equivalent — especially in adaptive optimizers such as Adam, where the L2 penalty gradient is scaled by the adaptive denominator and therefore can regularize large-history coordinates less than decoupled weight decay. When relevant, mention AdamW as the standard decoupled fix and include a short coordinatewise numeric example.
- In dropout sections, be explicit that the **unit activations are masked, not the weights**. Show the actual masked-activation formula (for example $\tilde a_j=m_j a_j$ or $\tilde a_j=\frac{m_j}{1-p}a_j$), give the training steps in order, and include a brief chain-rule explanation of why masked units receive zero gradient (for example $\partial L/\partial w_{jk}=\delta_k m_j a_j$). Also state both technical compensation conventions clearly: (1) non-inverted dropout, where after training one multiplies by the keep probability $1-p$ the **next layer's weights fed by the dropout-applied layer** (that is, the connections leaving the masked activations; do this after training, not during training), and (2) inverted dropout, where one divides the kept activations by $1-p$ **during training** and does **not** modify weights after training, so inference is unchanged. When helpful, explain the intuition that without compensation a unit is connected to about $1/(1-p)$ times as many active inputs at test time as during training.

### Filenames, titles, and links

- Prefer lowercase filenames except for genuine proper nouns.
- Prefer the singular canonical concept name unless the concept is inherently plural.
- Keep topic-note aliases to the canonical term plus genuine singular/plural synonyms; do not treat specific instances as aliases of the general term.
- Use `%20` in links, but do not percent-escape actual filenames.
- When linking to `general/`, use the canonical article title but do **not** create or edit the `general/` file as part of course-note work.

### Images and circuit diagrams

- Put image markup on the same line as the end of the preceding paragraph.
- Store course-specific assets under the course folder (typically `attachments/`).
- If a course keeps diagram-generation scripts, keep the docstrings descriptive enough for future maintainers to reconstruct topology and drawing style.
- For common circuit scripts, prefer building the main rail first, saving branch points explicitly, and documenting special topologies such as H-bridges clearly.

### Course index and outline updates

- Add every new topic note to the course `children:` list.
- In session entries, link the note as a parent bullet and the relevant sections as indented `§` links.
- Every named section or subsection that matters for navigation should be reachable from the course index or session outline.
- Keep link text exactly aligned with the actual heading text.

### Journal entries note (accounting courses)

For accounting courses, maintain a dedicated `journal entries.md` topic note.

- One journal-entry type per `##` section.
- Each worked example lives in a single blockquote: scenario, journal-entry table, then optional explanation/calculation.
- Use markdown tables with right-aligned Dr/Cr columns.
- Wrap the first-column header description and each account name in clozes.
- Mask all debit and credit amounts with clozes and use `&nbsp;` as the thousands separator.
- Keep punctuation outside the closing cloze token: `{@{text}@}.`
- Link each new journal-entry section back into the course index and the relevant week.

## Validator and tooling

Use the validator as the structural authority for this skill.

```shell
# POSIX shell
uv run .agents/skills/academic-notes/check.py special/academia/<institution>/ELEC\ 1100

# Windows PowerShell or cmd
uv run .agents/skills/academic-notes/check.py "special/academia/<institution>/ELEC 1100"
```

Rules of thumb:

- Validate the **smallest relevant scope only**.
- Common failures include missing tags, missing `datetime`, invalid headings, broken section-card structure, duplicate week numbers, and exams placed too early.
- The validator also checks `index_children_order`, `index_children_missing`, and `index_children_missing_index` for `index.md` files.
- After structural fixes, run repository formatting, checks, and tests on explicit paths.

## Continuous improvement

Keep the skill concise and authoritative.

- If a durable lesson appears, update `SKILL.md`, `course-template.md`, the relevant instruction file, and tests in the same task.
- Do not use persistent memory as a second documentation system for academic-notes conventions.
- Prefer editing the validator when the issue is structural and recurring.
- Keep changes focused and reviewable; avoid broad mechanical rewrites unless clearly justified.

### Workflow for agents

1. Identify whether the lesson belongs in prose, the template, or the validator.
2. Update the authoritative file immediately rather than leaving a “remember later” note.
3. If the issue is structural, teach the validator and add a test.
4. Re-run validation or tests on the affected scope.

### Extending the validator

When prose guidance is not enough, extend the validator instead of relying on repeated suppressions.

1. Add a new pure rule in `check_mods/rules.py` and register it with `@RULE_REGISTRY.register()`.
2. Add matching tests in `tests_a7392be/check_mods/test_rules.py`.
3. Run the validator or tests against representative notes.
4. Document the new rule briefly here or in the related instruction/template if authors need guidance when it fires.
