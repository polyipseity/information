---
name: create-flashcards
description: |
  Help the user add spaced-repetition flashcards (cloze deletions or Q/A pairs) to existing Markdown notes across the repository.  The skill encapsulates the multi‑step process the user follows in their finance lecture notes (e.g. FINA 3103) and elsewhere: read the prose, identify key terms, dates, formulas and logical assertions, and wrap them using flashcard markup (`{@{ }@}`, `::@::`, `:@:`).

  There are three supported forms:

  - **Cloze** (`{@{ }@}`) hides arbitrary text inside paragraphs.
  - **Two-sided QA** (`::@::`) on a single line, yielding two cards.
  - **One-sided QA** (`:@:`) on a single line, yielding a single card.

  For the QA formats remember the line-only rule; if visual separation is needed insert `<br/>`/`<p>` instead of newline characters.  Representative examples later in this document illustrate all three types.  Use existing flashcard files as style guides and adapt the output based on user feedback.  The skill also suggests regeneration commands once flashcards are inserted.
---

# Flashcard Creation Skill

This skill automates the user’s process for converting Markdown prose into active‑recall flashcards.  It works interactively: you provide a file path or text snippet, the agent edits it in place with cloze markup, and the user refines.  The skill supports three forms of flashcards—inline cloze (`{@{ }@}`), two‑sided QA (`::@::`), and one‑sided QA (`:@:`).  QA cards must fit on one Markdown line; use `<br/>` or `<p>` for visual breaks.

All style decisions are driven by the representative examples and heuristics embedded in this document.  When you encounter a new pattern, capture it here as an example or add a heuristic rule.  An optional prompt file (`create-flashcards.prompt.md`) can solicit path/line information.  Do __not__ run any commands such as `init generate` in the course of editing; operational advice belongs elsewhere.

__Academic content:__ if editing `special/academia` material also consult the `academic-ingest` skill for course‑specific conventions such as full hierarchical gloss paths and QA list separators; it links back here for general guidance.  Conversely, the `academic-notes` documentation refers you here for the general cloze/QA patterns and example transformations. __Topic notes:__ by default do __not__ add cloze cards; use only two-sided (::@::) or very rarely one-sided (:@:) cards and add more of those as needed. __Cloze delimiter:__ the closing `}@}` must come __before__ any trailing punctuation; place punctuation after the delimiter (e.g. `{@{text}@}.` not `{@{text.}@}`).

For private academic quiz archives where the user has explicitly confirmed that a checked option is correct, prefer a short `- explanation:` bullet with clozes over a bare answer-only card. Cloze the decisive method, condition, contrast, or reason that makes the selected answer correct; do not merely hide the same final option twice. If the question or answer depends on an embedded figure, still add the cloze-rich explanation instead of treating the image itself as sufficient review support. If the `Solution:` line contains the embedded image, keep at least one cloze on that `Solution:` line too so the chosen option or structural descriptor is directly quizzable there.

For public academic quiz hints written as `::@::` cards, keep the hints in the same order as the archived/private question order. If the user wants slightly more context, add it mainly on the left-hand side prompt itself: use option-family cues, mutated-but-equivalent givens, or the decisive spectral, timing, or topology landmarks without copying the official choices verbatim.

For academic topic notes, do not limit cards to isolated definitions. Prefer a balanced mix of comparison cards, intuition cards, example cards, counterexample cards, and worked-example cards when the material supports them. If a section needs only a small clarification, enhance the existing flashcards; if it needs a substantial new cluster of distinctions or examples, add new flashcards instead of overloading one old card. For worked examples, place __all__ required givens, formulas, assumptions, and numeric input data on the left-hand side before `::@::` so the card is fully answerable in isolation.

For mathematically technical academic notes, preserve the derivation or proof spine in the flashcards instead of testing only the final formula. A strong default is to add at least one card for the governing equation or setup, one card for the decisive derivation step or inequality, and one card for the final result or interpretation when the source material supports that structure.

When a course note is organized by topic pages and lecture weeks rather than stored chapter pages, avoid chapter-number-only prompts such as `Chapter 2 / ...`. Use self-contained concept wording or the actual topic-note context instead.

For conceptual math-law cards in academic notes, a descriptive prompt is often better than forcing the formula itself onto the left-hand side. When such a card is genuinely conceptual rather than computational, prefer the descriptive prompt and, if needed, attach a targeted inline suppression comment on the same line instead of warping the card into a fake calculation prompt.

## When to use

Be careful when users add inline comments or annotations such as `<!-- check: ignore-line[...]: equation on left -->`. Such comments are rationales for validator suppressions and __not__ editing instructions.
Never split or reflow the card simply because a comment mentions “left” or
“right”; the left-hand portion always means _the text that appears before the
`::@::` or `:@:` separator_, and it may be long when calculations are involved.

Invoke the skill when the user asks to “add flashcards”, “cloze this”, “quizify”, or similar.  The target file must already exist; never create new files or edit submodules/private content without permission.  Process one paragraph or logical block at a time and display the original text for confirmation.  Aim for at least 92 % coverage of each paragraph and about 80–92 % of every sentence.  Numeric facts or simple assignments may be clozed as atomic units.

## Workflow

1. __Consult examples.__  Scan the index of representative patterns earlier in this file for descriptions matching the current passage.  Refer to the matching example numbers in your reasoning (e.g., “behaviour like example 3’s QA rewrite”).
2. __Select a paragraph or contiguous block.__  Work on one at a time.  Use a separate tool call per paragraph rather than batching.  Pause after each block to retrieve the next.
3. __Break text into meaning units.__  Look for definitions, names, dates, formulas, list items, pros/cons, conditional or contrast clauses, and semicolon‑separated ideas.  Treat each as a potential card.  If a sentence is mostly visible, add another cloze.  Do not hide an entire short sentence with no anchor word; leave a hint word or two visible.
   - Handle semicolon‑separated clauses like a list with separate clozes.
   - For conditional connectors (`if`, `when`, `once`, `unless`), hide the text after the connector unless the condition itself is being tested.
   - For contrastive conjunctions (`but`, `however`, `yet`, etc.) make separate clozes on either side.
4. __Insert clozes guided by examples.__  Use the matched examples as
   templates:
   - Wrap material based on meaning and recall effort rather than rigid word counts.  Dense or confusing ideas get smaller clozes; obvious concepts can be larger.
   - If text already has formatting (bold, italic, code, underline, etc.), enclose the entire formatted phrase inside the cloze rather than inserting braces within it.  For example use `{@{__foo__}@}` instead of `__{@{foo}@}__`.
   - Cloze both a leading proposition and its supporting detail if both are worth testing.  Leave one or two words outside the braces for a contextual hint.
   - When several closely related noun phrases appear, split them into multiple smaller clozes instead of a single huge one.
   - Place the cloze where it best prompts recall—the first word, last word, or middle as the example shows.
   - __Never break a LaTeX equation.__  Hide the entire `$…$` or `$$…$$` block as a single atomic cloze.
   - By default suggest inline clozes; only rewrite to `::@::` or `:@:` if the user explicitly requests QA style or if an example clearly uses that format.
   - Preserve Markdown, KaTeX, links, and line ordering.  Lists are handled item‑by‑item unless an example demonstrates a combined deletion.
5. __Apply the edits directly__ in the file and return the modified text.
   Provide alternate versions or explanations only if the user asks.

## Continuous improvement

- Keep durable flashcard lessons in this document (and, for course notes under `special/academia`, in the `academic-crud-topic-note` skill) rather than maintaining a separate sidecar learning log that drifts out of sync.
- After suggesting clozes, ask “which deletions are wrong?” or “would you prefer Q/A instead of inline cloze?”  Use corrections to expand the examples or add rules.  When the user states “this is my style”, treat it as a high‑priority rule and immediately encode it in this document, noting which examples or heuristics were updated.
- Analyse user edits using `git --no-pager diff --word-diff --no-color path/to/file.md`.  Word diffs reveal boundary shifts and merged or expanded clozes; use them as training data and add corresponding examples.
- Watch for feedback about excessive fragmentation.  Merge adjacent tiny deletions in future and update the rules accordingly.
- When the user modifies or adds contiguous paragraphs, capture the whole block as a single example tagged appropriately so the agent can recognise similar multi‑paragraph patterns later.
- Never suggest running any external command during editing.  Command advice is irrelevant to this skill.
- If session memory grows large (≈20 examples or after a long session), summarise learned rules and cement them in this document. Prompt the user before consolidating.

## Cloze creation methodology

Use this three-step process for every clozing task.  It produces fine-grained clozes that maximise recall context while keeping each blank to one recallable unit.

### Step 1: Assume everything needs clozing

Read the target sentence and treat every clause, equation, and factual claim as a candidate blank.  This counteracts the natural tendency to under-cloze.  Aim for ≥80% of each solution sentence inside clozes — only linking words ("so", "hence", "therefore"), articles ("the", "a"), and 1–3 hint words should remain visible.  In multi-step worked solutions, every intermediate equation and every conclusion must be individually clozed — not left visible between clozes.

### Step 2: Split at natural boundaries

Break at commas, semicolons, conjunctions (`and`, `but`, `so`, `because`), relative clauses (`that`, `which`), and equation boundaries.  Each resulting fragment becomes a separate cloze candidate.

| Boundary type | Example split |
| --- | --- |
| Comma | "voltage is equal, so current differs" → two clozes |
| Semicolon | "R increases; X decreases" → two clozes |
| Conjunction | "blocks the MCU and risks missing inputs" → two clozes |
| Equation boundary | "IB is 0.09 mA, so βIB is 8.2 mA" → two clozes |
| Prose + equation | "current is $I=...$" → two clozes (prose visible, equation hidden) |
| Solution step | "IB is 0.09 mA, so βIB is 8.2 mA" → each equation gets its own cloze |
| Contrast (A vs B) | "X is good, whereas Y is bad" → two clozes |
| Do NOT split | "$01\to1$, $10\to1$" (same type of item) → one cloze |

> __Important:__ the prose+equation split applies only when one side is a math expression (`$...$`). For all-prose sentences, keep related clauses together in one cloze.

### Common mistakes

1. __Missing hint words.__ Every cloze must have at least one visible word outside it. A cloze that starts at the beginning of a sentence without a lead-in phrase is wrong — add a hint like "The advantage is" before it. Hint words are at least 1 word, typically 1–3 words, but can be longer phrases (e.g., "The node voltage is", "Solution:"). There is no upper limit on hint length. The validator now catches cloze clauses with no visible hint words.
2. __Contrast merged into one cloze.__ Contrast items (A vs B) must be separate clozes — never `{@{X is good, whereas Y is bad}@}`.
3. __Over-splitting.__ Do not split at every comma. Related items within one reasoning step stay in one cloze.
4. __Prose+equation merge.__ Never put both prose description and equation in one cloze (e.g., `{@{Ohm's law, $V=IR$}@}`). Split into `{@{Ohm's law}@} is {@{$V=IR$}@}` so the concept name stays visible as a recall hint.
5. __Under-clozing solution steps.__ In multi-step solutions, every intermediate equation and every conclusion must be clozed. Leaving an equation or conclusion visible between clozes means the solver sees the answer instead of recalling it. Each step gets its own cloze; only linking words (`so`, `hence`, `therefore`) stay visible between clozes.
6. __Articles left outside cloze.__ Articles (`the`, `a`, `an`) are determiners that belong to the noun phrase inside the cloze. `the {@{device}@}` means the article is a hint but the user likely intended to test recall of "the device" as a unit. Move the article inside: `{@{the device}@}` with surrounding hint text produces better recall. The validator warns when an article immediately precedes a cloze opening.
7. __Trailing copula/auxiliary verb.__ Verbs like `is`, `are`, `was`, `were`, `be`, `been`, `being`, `has`, `have`, `had` before a cloze opening usually signal that the verb itself should be inside the cloze for better recall. `is {@{5V}@}` is less useful than `{@{is 5V}@}`. The validator warns when a copula/auxiliary verb sits immediately before a cloze.
8. __Wrong cloze token variants.__ Cloze tokens must be exactly `{@{` and `}@}`. Common typos include `@{` (missing opening brace), `@}` (missing closing brace), `{@}` (wrong structure), and reversed `}@`. The validator detects these malformed tokens and reports them.
9. __Insufficient coverage.__ Each paragraph with cloze flashcards should have at least 80% of visible characters inside cloze bodies. Coverage below 80% means too much content is left visible for effective recall. The validator warns when coverage falls below this threshold.
10. __Excessive coverage.__ When coverage exceeds 98%, almost everything is hidden and there are too few hint words visible. Leave at least some context words outside clozes so the reader knows what they're recalling. The validator warns when coverage exceeds this threshold.

### Step 3: Shrink to leave hint words

Remove words from the cloze until one or two anchor words remain visible outside the braces.  The visible words provide recall context; the hidden words test the core concept.

```text
Before (one giant cloze): {@{The transistor is not in saturation because βIB < IC,max}@}
After (two focused clozes): The {@{transistor is not in saturation@}} because {@{βIB < IC,max@}}.
```

__Never mix prose and equation in one cloze.__  When a sentence has prose plus an equation (e.g., "The voltage is $V=...$"), put the prose in one cloze and the equation in a separate cloze, with the linking word (`is`, `gives`) visible between them: `{@{The voltage}@} is {@{$V=...$}@}`.  __Do not apply this split to prose-to-prose sentences.__  A sentence like "the Zener is effectively off" is all prose — keep it as one cloze: `{@{the Zener is effectively off@}}`.

### Step 4: Audit coverage

After applying clozes, estimate the cloze-to-visible ratio for each solution line.  The hard minimum is 80% of each solution sentence inside clozes; the target is ~90%.  Use the expand→add→merge hierarchy below to reach the target:

1. __Expand__: if an existing cloze has important content visible around it, expand the cloze to absorb that content (preferred first step — rewrites the fewest lines).
2. __Add__: if uncovered content is far from any existing cloze, add a new cloze around it.
3. __Merge__: if two adjacent clozes are separated by only one or two visible words and merging yields a stronger recall prompt, combine them into one cloze.  Use sparingly — only when the merged cloze tests a single coherent concept.

A common failure mode is clozing only equations while leaving entire prose explanations visible — both prose and equations must be inside clozes.  Another failure mode is splitting content into too many tiny clozes when one larger cloze would be a stronger recall prompt (e.g., `{@{reverse breakdown}@}` is weaker than `{@{reverse breakdown, the node is clamped near@}}`).

### Splitting guide for common patterns

- __Equation + prose__: when a sentence contains prose plus an equation (`$...$`), put the prose in one cloze and the equation in a separate cloze; the linking word (`is`, `gives`) stays visible between them.  __Do not use this pattern for all-prose sentences__ — "the Zener is effectively off" stays as one cloze: `{@{the Zener is effectively off@}}`.
- __Conditional chain__: keep `if`/`when` visible, cloze the condition body separately from the consequence.
- __Comparison__: cloze each side of the contrast separately; keep the contrastive conjunction (`but`, `however`) visible.
- __Step-by-step procedure__: one cloze per step; keep step connectors (`then`, `next`, `finally`) visible.

## Representative examples

The three worked examples below illustrate the three-step cloze methodology in action.  Each shows the before/after transformation.

1. __Truth table + formula split__ (electronic circuits) – formula and concept get separate clozes; a hint word anchors each.

   ```text
   Input: The output is XNOR with Q = AB' + A'B.
   Output: The {@{output is XNOR@}} with {@{$Q = AB' + A'B$@}}.
   ```

2. __Splitting a single long cloze__ (embedded systems) – one giant blank becomes three focused ones, each testing a distinct concept.

   ```text
   Input: millis() returns milliseconds and has no rollover risk for months, but delay() blocks the MCU and risks missing sensor inputs.
   Output: millis() returns {@{milliseconds@}} and has {@{no rollover risk for months@}}, but delay() {@{blocks the MCU and risks missing sensor inputs@}}.
   ```

3. __Resistor network__ (circuit analysis) – split a single equation cloze into a concept cloze plus a separate equation cloze.

   ```text
   Input: In a parallel circuit, voltage is equal: V_1 = V_2 = V_3.
   Output: In a parallel circuit, {@{voltage is equal@}: $V_1 = V_2 = V_3$}.
   ```

4. __Additive clozing__ (circuit analysis) – keep existing clozes, add new ones around uncovered factual content.

   ```text
   Input: Below the combined threshold, the Zener is effectively off and the node behaves like an ordinary voltage divider. Once the current is large enough to drive the Zener into reverse breakdown, the node is clamped near 7.2 V and extra source variation mainly changes the current through the series path.

   After initial clozing (some factual content still visible):
   Below the combined threshold, the Zener is {@{effectively off@}} and the {@{node behaves like an ordinary voltage divider}@}. Once the current is large enough to drive the Zener into {@{reverse breakdown@}}, the {@{node is clamped near@} {@{$7.2\text{ V}$@}} and extra source variation mainly changes the current through the series path.

   After coverage audit (add new clozes for visible facts):
   Below the combined threshold, {@{the Zener is effectively off@}} and the {@{node behaves like an ordinary voltage divider}@}. Once the current is large enough to drive the Zener into {@{reverse breakdown@}}, the {@{node is clamped near@} {@{$7.2\text{ V}$@}} and {@{extra source variation mainly changes the current through the series path}@}.
   ```

5. __Cloze expansion__ (circuit analysis) – merge two adjacent small clozes into one larger cloze when the expanded version tests a stronger, more coherent concept.

   ```text
   Before (two small clozes, visible text between them):
   The decision is made from stale data. Even if the physical sensor {@{changes@}}, the code keeps using the old value and the {@{motor behavior may continue incorrectly@}}.

   After (expand first cloze to absorb nearby visible words):
   The decision is made from stale data. Even if the physical sensor {@{changes, the code keeps using the old value@}} and the {@{motor behavior may continue incorrectly@}}.
   ```

   Expansion is preferred when the two clozes are separated by only one or two visible words and the expanded version captures a single coherent cause-and-effect relationship.

_These examples demonstrate the three-step methodology: assume everything → split at natural boundaries → shrink to leave hint words.  Apply this pattern when clozing Q&A solutions, worked examples, and explanatory prose._

## Heuristics and rules

The form of the examples above is complemented by a set of practical heuristics, which are now incorporated below under the appropriate sections (learned rules no longer require a separate file).

### General editing principles

- Preserve the source verbatim except for cloze markup; do not paraphrase or reflow text.
- Equations stay whole: wrap an entire `$...$` or `$$...$$` block in a single cloze; never split math.
- Anchor context: leave visible words around each deletion to give a hint; avoid blanking a sentence entirely unless context is crystal clear.
- Mirror the user’s style when they supply examples or corrections.
- Preserving HTML entities and escapes exactly; treat them as opaque literals.
- Submodule safety: never edit `private/`, `self/`, or other submodules without explicit authorization.

### Sentence and clause handling

- Work paragraph by paragraph; add clozes only within a single paragraph before moving on.
- Break long sentences with multiple ideas into separate cards rather than one huge deletion.  Semicolon lists get individual clozes per clause.
- Split around contrastive conjunctions (`but`, `however`, etc.) and keep conditional connectors (`if`, `when`, etc.) visible unless the condition itself is tested.
- Default to inline clozes; use `::@::` or `:@:` only if the user requests QA style or an example clearly shows it.
- When re-clozing a solution block, apply the three-step methodology (assume everything → split at natural boundaries → shrink to leave hint words). This yields fine-grained clozes where each blank tests one recallable unit.
- For simple declarative sentences, consider hiding subject and object separately to yield focused cards.
- Articles, possessives, prepositions, and qualifiers should be included inside the cloze when they are part of the tested concept.
- Hide the minimal meaningful semantic unit—adjust if the user later shifts words in or out of the cloze.
- Only cloze a year or date if it is central to the idea; incidental dates remain visible.

### Lists and section‑wide edits

- Two‑sided QA lists: when the entire section should become a list of question/answer pairs, prepend a horizontal rule and the exact phrase “Flashcards for this section are as follows:” on a blank line, then convert each bullet separately.
- Treat adjacent paragraphs as a unit if the user edits them together; record such multi‑paragraph patterns as new examples.

### Improvement process

- After editing, solicit feedback (“which deletions are wrong?”, “prefer QA instead?”) and use corrections to update examples and rules immediately.
- Analyse user edits with `git --no-pager diff --word-diff --no-color` and add training examples for boundary shifts or merged clozes.
- Summarise learned rules periodically into this document; avoid letting session memory grow unbounded.

## Implementation notes

- The skill may be purely heuristic; there is no need to parse Markdown deeply or run pytextgen.  Simple text manipulation is sufficient if the results are usually reasonable and users can refine them.
- Only edit visible Markdown notes; do not modify `private/` or any submodule content without explicit permission.
- Dialogue should remain interactive and improvement-driven; remember past corrections to improve future performance.

Using this skill makes flashcard creation faster while faithfully following the user’s style.  Always start by reading the example section—those patterns are the ultimate reference.
