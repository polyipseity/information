---
name: create-flashcards
description: |
  Add spaced-repetition flashcards (cloze deletions or Q/A pairs) to existing Markdown notes: read the prose, identify key terms, dates, formulas, and logical assertions, and wrap them using flashcard markup (`{@{ }@}`, `::@::`, `:@:`).

  Three forms are supported: cloze (`{@{ }@}`), which hides arbitrary text inside paragraphs; two-sided QA (`::@::`) on a single line, yielding two cards; and one-sided QA (`:@:`) on a single line, yielding one card.

  QA cards must stay on one Markdown line; use `<br/>` or `<p>` instead of newline characters when visual separation is needed. Use existing flashcard files as style guides and adapt to user feedback.
---

# Flashcard Creation Skill

Convert Markdown prose into active-recall flashcards, editing the file in place. When a new pattern appears, capture it here as an example or heuristic. Do not run commands such as `init generate` while editing; operational advice belongs elsewhere.

__Academic content:__ when editing `special/academia` material, also consult `academic-ingest` for course-specific conventions. Topic notes use two-sided (`::@::`) or, rarely, one-sided (`:@:`) cards by default, never cloze.

## Card forms and formatting

- __Cloze__ (`{@{ }@}`) hides text inside a paragraph.
- __Two-sided QA__ (`::@::`) yields two cards from one line.
- __One-sided QA__ (`:@:`) yields one card from one line.

The closing cloze delimiter `}@}` comes before any trailing punctuation, which sits after the delimiter: `{@{text}@}.`, not `{@{text.}@}`.

## Diagrams in cards

A card may carry a diagram on the prompt side, the answer side, or both. A drawing a note defines has to be produced, not just recognised, so the cards carry it and the prose does not.

- __Recognition__: drawing on the prompt side, name or reading on the answer side: `- ground symbol: ![ground symbol: stacked horizontal strokes at a node](attachments/symbol_ground.svg) ::@:: The reference node whose potential is taken as $0\text{ V}$.`
- __Recall__: question on the prompt side, drawing on the answer side: `- draw the ground symbol: how is the node taken as $0\text{ V}$ marked on a circuit diagram? ::@:: Horizontal strokes stacked at the node. <p> ![ground symbol: stacked horizontal strokes at a node](attachments/symbol_ground.svg)`. Every drawing a note defines needs at least one recall card: the picture is what the reader has to produce.
- __Both__: each side carries a drawing when the card is a comparison or a transformation, the starting drawing on one side and the result on the other.

Paths are relative to the note (`attachments/<name>.svg`), and alt text is a plain-language description with no LaTeX. Several drawings that belong together (the forms one symbol can take, or the two directions of a convention) go side by side on the same line, each with its own alt text. Keep the card on one Markdown line and separate the image from the surrounding text with `<p>`. An answer that is a drawing is complete on its own; add a short description beside it when the card also has to read in the reverse direction. Look at the drawing in both directions before carding it, and write the alt text while looking (see `academic-vision`).

## Academic conventions

__Private quiz archives__ (the user has confirmed a checked option is correct): prefer a short `- explanation:` bullet with clozes over a bare answer-only card. Cloze the decisive method, condition, contrast, or reason; do not merely hide the same final option twice. When the question or answer depends on an embedded figure, still add the cloze-rich explanation rather than treating the image as review support. If the `Solution:` line contains the image, keep at least one cloze on that line too, so the chosen option or structural descriptor is directly quizzable.

__Public quiz hints__ written as `::@::`: keep the hints in the same order as the archived/private question order. To add context, put it on the left-hand prompt: option-family cues, mutated-but-equivalent givens, or the decisive spectral, timing, or topology landmarks, without copying the official choices verbatim.

__Topic notes:__ do not limit cards to isolated definitions. Prefer a balanced mix of comparison, intuition, example, counterexample, and worked-example cards when the material supports them. For a small clarification, enhance the existing card; for a substantial new cluster of distinctions or examples, add new cards instead of overloading an old one. For worked examples, place __all__ required givens, formulas, assumptions, and numeric input data on the left-hand side before `::@::`: the card has to be answerable in isolation.

__Mathematically technical notes:__ preserve the derivation or proof spine instead of testing only the final formula. A strong default is one card for the governing equation or setup, one for the decisive derivation step or inequality, and one for the final result or interpretation, when the material supports that structure.

__Chapter-number prompts:__ when a note is organized by topic pages and lecture weeks rather than stored chapter pages, avoid prompts such as `Chapter 2 / ...`; use self-contained concept wording or the actual topic-note context.

__Conceptual math-law cards:__ a descriptive prompt is often better than forcing the formula onto the left-hand side. When the card is genuinely conceptual rather than computational, prefer the descriptive prompt and, if needed, attach a targeted inline suppression comment on the same line instead of warping the card into a fake calculation.

## When to use

Invoke the skill when the user asks to "add flashcards", "cloze this", "quizify", or similar. The target file must already exist; never create new files, and never edit submodules or private content without permission. Process one paragraph or logical block at a time and display the original text for confirmation. Aim for at least 92% coverage of each paragraph and about 80-92% of every sentence. Numeric facts and simple assignments may be clozed as atomic units.

Inline comments such as `<!-- check: ignore-line[...]: equation on left -->` are rationales for validator suppressions, not editing instructions. Never split or reflow a card because a comment mentions "left" or "right": the left-hand portion always means the text before the `::@::` or `:@:` separator, and it may be long when calculations are involved.

## Workflow

1. __Consult examples.__ Scan the representative patterns below for one matching the current passage and cite its number in your reasoning (for example, "behaviour like example 3's QA rewrite").
2. __Select a paragraph or contiguous block.__ Work on one at a time, with a separate tool call per paragraph rather than batching, and pause after each block.
3. __Break text into meaning units.__ Look for definitions, names, dates, formulas, list items, pros and cons, conditional or contrast clauses, and semicolon-separated ideas, treating each as a potential card. If a sentence is mostly visible, add another cloze, and never hide an entire short sentence with no anchor word; leave a hint word or two visible.
   - Handle semicolon-separated clauses like a list, with separate clozes.
   - For conditional connectors (`if`, `when`, `once`, `unless`), hide the text after the connector unless the condition itself is being tested.
   - For contrastive conjunctions (`but`, `however`, `yet`), make separate clozes on either side.
4. __Insert clozes guided by examples__, wrapping material by meaning and recall effort rather than rigid word counts: dense or confusing ideas get smaller clozes, obvious concepts can be larger.
   - If text already has formatting (bold, italic, code, underline), enclose the whole formatted phrase inside the cloze, e.g. `{@{__foo__}@}`, not `__{@{foo}@}__`.
   - Cloze both a leading proposition and its supporting detail when both are worth testing, leaving one or two words outside the braces as a contextual hint.
   - When several closely related noun phrases appear, split them into smaller clozes instead of one huge one.
   - Place the cloze where it best prompts recall: the first word, last word, or middle, as the examples show.
   - __Never break a LaTeX equation.__ Hide the entire `$…$` or `$$…$$` block as a single atomic cloze.
   - Suggest inline clozes by default; rewrite to `::@::` or `:@:` only when the user requests QA style or an example clearly uses that format.
   - Preserve Markdown, KaTeX, links, and line ordering. Handle lists item by item unless an example shows a combined deletion.
5. __Apply the edits directly__ in the file and return the modified text. Provide alternate versions or explanations only when asked.
6. __Run the humanizer pass__ over the new cards and the prose they came from: cut prompts that repeat their answer, answers that repeat their prompt, filler, and trailing justification clauses; keep the hint words that make each cloze answerable. Preserve facts, cloze/QA markup, and LaTeX (see "Humanizer pass" in `academic-ingest`).

## Cloze creation methodology

Use this process for every clozing task: it yields fine-grained clozes that keep each blank to one recallable unit.

### 1. Assume everything needs clozing

Treat every clause, equation, and factual claim in the target sentence as a candidate blank. Aim for at least 80% of each solution sentence inside clozes (target around 90%); only linking words ("so", "hence", "therefore"), articles ("the", "a"), and 1-3 hint words should remain visible. In multi-step worked solutions, every intermediate equation and every conclusion must be individually clozed.

### 2. Split at natural boundaries

Break at commas, semicolons, conjunctions (`and`, `but`, `so`, `because`), relative clauses (`that`, `which`), and equation boundaries. Each fragment becomes a separate cloze candidate.

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

### 3. Shrink to leave hint words

Remove words from the cloze until one or two anchor words remain visible outside the braces; the visible words give recall context, the hidden words test the core concept.

```text
Before (one giant cloze): {@{The transistor is not in saturation because βIB < IC,max}@}
After (two focused clozes): The {@{transistor is not in saturation@}} because {@{βIB < IC,max@}}.
```

Never mix prose and equation in one cloze. For "The voltage is $V=...$", use `{@{The voltage}@} is {@{$V=...$}@}`, with the linking word visible. Do not apply this split to prose-to-prose sentences: "the Zener is effectively off" stays one cloze, `{@{the Zener is effectively off@}}`.

### 4. Audit coverage

Estimate the cloze-to-visible ratio for each solution line, with a hard minimum of 80% of each solution sentence inside clozes and a target around 90%. Reach the target with this hierarchy:

1. __Expand__ an existing cloze to absorb important visible content around it (preferred: fewest lines rewritten).
2. __Add__ a new cloze when uncovered content is far from any existing one.
3. __Merge__ two adjacent clozes separated by only one or two visible words when the merged version tests a single coherent concept. Use sparingly.

Common failures: clozing only equations while leaving prose explanations visible (both must be clozed), and splitting content into so many tiny clozes that one larger cloze would prompt recall better (`{@{reverse breakdown}@}` is weaker than `{@{reverse breakdown, the node is clamped near@}}`).

### Common mistakes

1. __Missing hint words.__ Every cloze needs at least one visible word outside it. A cloze starting a sentence with no lead-in is wrong; add a hint such as "The advantage is". Hints are typically 1-3 words but can be longer phrases ("The node voltage is", "Solution:"), with no upper limit. The validator catches cloze clauses with no visible hint words.
2. __Contrast merged into one cloze.__ Contrast items (A vs B) must be separate clozes, never `{@{X is good, whereas Y is bad}@}`.
3. __Over-splitting.__ Do not split at every comma; related items within one reasoning step stay in one cloze.
4. __Prose+equation merge.__ Never put both a prose description and an equation in one cloze (`{@{Ohm's law, $V=IR$}@}`); split into `{@{Ohm's law}@} is {@{$V=IR$}@}` so the concept name stays visible as a hint.
5. __Under-clozing solution steps.__ In multi-step solutions, cloze every intermediate equation and conclusion; each step gets its own cloze, with only linking words visible between them.
6. __Articles left outside the cloze.__ Articles (`the`, `a`, `an`) belong to the noun phrase inside the cloze, so `{@{the device}@}` recalls better than `the {@{device}@}`. The validator warns when an article immediately precedes a cloze opening.
7. __Trailing copula or auxiliary verb.__ Verbs such as `is`, `are`, `was`, `were`, `be`, `been`, `being`, `has`, `have`, `had` before a cloze opening usually belong inside it: `{@{is 5V}@}` beats `is {@{5V}@}`. The validator warns when a copula or auxiliary verb sits immediately before a cloze.
8. __Wrong cloze tokens.__ Cloze tokens must be exactly `{@{` and `}@}`. Common typos (`@{`, `@}`, `{@}`, reversed `}@`) are malformed, and the validator reports them.
9. __Insufficient coverage.__ A paragraph with cloze flashcards should have at least 80% of its visible characters inside cloze bodies; the validator warns below that.
10. __Excessive coverage.__ Above 98%, almost everything is hidden and too few hint words remain; leave context words visible so the reader knows what they are recalling. The validator warns above that.

## Representative examples

1. __Truth table + formula split__ (electronic circuits): the formula and the concept get separate clozes, each anchored by a hint word.

   ```text
   Input: The output is XNOR with Q = AB' + A'B.
   Output: The {@{output is XNOR@}} with {@{$Q = AB' + A'B$@}}.
   ```

2. __Splitting a single long cloze__ (embedded systems): one giant blank becomes three focused ones, each testing a distinct concept.

   ```text
   Input: millis() returns milliseconds and has no rollover risk for months, but delay() blocks the MCU and risks missing sensor inputs.
   Output: millis() returns {@{milliseconds@}} and has {@{no rollover risk for months@}}, but delay() {@{blocks the MCU and risks missing sensor inputs@}}.
   ```

3. __Resistor network__ (circuit analysis): split a single equation cloze into a concept cloze plus a separate equation cloze.

   ```text
   Input: In a parallel circuit, voltage is equal: V_1 = V_2 = V_3.
   Output: In a parallel circuit, {@{voltage is equal@}: $V_1 = V_2 = V_3$}.
   ```

4. __Additive clozing__ (circuit analysis): keep the existing clozes and add new ones around uncovered factual content.

   ```text
   Input: Below the combined threshold, the Zener is effectively off and the node behaves like an ordinary voltage divider. Once the current is large enough to drive the Zener into reverse breakdown, the node is clamped near 7.2 V and extra source variation mainly changes the current through the series path.

   After initial clozing (some factual content still visible):
   Below the combined threshold, the Zener is {@{effectively off@}} and the {@{node behaves like an ordinary voltage divider}@}. Once the current is large enough to drive the Zener into {@{reverse breakdown@}}, the {@{node is clamped near@} {@{$7.2\text{ V}$@}} and extra source variation mainly changes the current through the series path.

   After coverage audit (add new clozes for visible facts):
   Below the combined threshold, {@{the Zener is effectively off@}} and the {@{node behaves like an ordinary voltage divider}@}. Once the current is large enough to drive the Zener into {@{reverse breakdown@}}, the {@{node is clamped near@} {@{$7.2\text{ V}$@}} and {@{extra source variation mainly changes the current through the series path}@}.
   ```

5. __Cloze expansion__ (circuit analysis): merge two adjacent small clozes into one larger cloze when the expanded version tests a stronger, more coherent concept.

   ```text
   Before (two small clozes, visible text between them):
   The decision is made from stale data. Even if the physical sensor {@{changes@}}, the code keeps using the old value and the {@{motor behavior may continue incorrectly@}}.

   After (expand the first cloze to absorb nearby visible words):
   The decision is made from stale data. Even if the physical sensor {@{changes, the code keeps using the old value@}} and the {@{motor behavior may continue incorrectly@}}.
   ```

   Expansion is preferred when the two clozes are separated by only one or two visible words and the expanded version captures a single coherent cause-and-effect relationship.

## Heuristics

### General

- Preserve the source verbatim except for cloze markup; do not paraphrase or reflow.
- Never name the material in a card or its surrounding prose: no `the lecture`, `the slides`, `the deck`, or `the course`. State the content itself.
- Keep equations whole: wrap an entire `$...$` or `$$...$$` block in one cloze; never split math.
- Leave visible words around each deletion as a hint, and avoid blanking a sentence entirely unless the context is crystal clear.
- Mirror the user's style when they supply examples or corrections.
- Preserve HTML entities and escapes exactly, treating them as opaque literals.
- Never edit `private/`, `self/`, or other submodules without explicit authorization.

### Sentences and clauses

- Work paragraph by paragraph, adding clozes within one paragraph before moving on.
- Break long sentences with multiple ideas into separate cards rather than one huge deletion; give semicolon lists individual clozes per clause.
- Split around contrastive conjunctions (`but`, `however`) and keep conditional connectors (`if`, `when`) visible unless the condition itself is tested.
- Default to inline clozes; use `::@::` or `:@:` only when the user requests QA style or an example clearly shows it.
- When re-clozing a solution block, apply the methodology above for fine-grained clozes, one recallable unit per blank.
- For simple declarative sentences, consider hiding subject and object separately.
- Include articles, possessives, prepositions, and qualifiers inside the cloze when they are part of the tested concept.
- Hide the minimal meaningful semantic unit, adjusting only if the user later shifts words in or out.
- Cloze a year or date only when it is central to the idea; leave incidental dates visible.

### Lists and section-wide edits

- For a whole section of two-sided QA, prepend a horizontal rule and the exact phrase "Flashcards for this section are as follows:" on a blank line, then convert each bullet separately.
- Treat adjacent paragraphs as a unit when the user edits them together, and record such multi-paragraph patterns as new examples.

### Enumeration cards

A card's answer carries one slice of a list, never the whole list, and the boundary is the note's choice. Pick a property that makes each slice nameable and correct: an era or date range (`the five born before 1790`), a shared mathematical property (`the divergence equations`, `the curl equations`), or a common issuer, counterparty, or market. Name that boundary on the prompt side so each slice stands alone, and keep the dates and years on the card, because they are the boundary the prompt names.

The boundary need not be one the material draws; reorganizing a source list is expected, as long as every item lands in exactly one slice and no slice claims a membership the material contradicts. A list of six or more items always gets split, and a list of four gets split whenever its members group by such a property.

## Continuous improvement

- Keep durable flashcard lessons in this document (and, for course notes under `special/academia`, in `academic-crud-topic-note`) rather than a separate sidecar log that drifts.
- After suggesting clozes, ask "which deletions are wrong?" or "would you prefer Q/A instead of inline cloze?", and use the corrections to expand the examples or add rules. When the user says "this is my style", treat it as a high-priority rule and encode it here, noting which examples or heuristics changed.
- Analyse user edits with `git --no-pager diff --word-diff --no-color path/to/file.md`: word diffs reveal boundary shifts and merged or expanded clozes, which are the changes worth turning into examples.
- Watch for feedback about excessive fragmentation, and merge adjacent tiny deletions in future.
- When the user modifies or adds contiguous paragraphs, capture the whole block as one example so similar multi-paragraph patterns are recognisable later.
- Never suggest running an external command during editing; command advice is irrelevant to this skill.
- If session memory grows large (around 20 examples, or after a long session), summarise the learned rules into this document, prompting the user before consolidating.
