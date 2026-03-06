---
name: flashcard-creation
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

All style decisions are driven by the representative examples and heuristics embedded in this document.  When you encounter a new pattern, capture it here as an example or add a heuristic rule.  An optional prompt file (`flashcard-creation.prompt.md`) can solicit path/line information.  Do **not** run any commands such as `init generate` in the course of editing; operational advice belongs elsewhere.

**Academic content:** if editing `special/academia` material also consult the `academic-notes` skill for course‑specific conventions such as full hierarchical gloss paths and QA list separators; it links back here for general guidance.  Conversely, the `academic-notes` documentation refers you here for the general cloze/QA patterns and example transformations.

## When to use

Be careful when users add inline comments or annotations such as
`<!-- check: ignore-line[...]: equation on left -->`. Such comments are
rationales for validator suppressions and **not** editing instructions.
Never split or reflow the card simply because a comment mentions “left” or
“right”; the left-hand portion always means *the text that appears before the
`::@::` or `:@:` separator*, and it may be long when calculations are involved.

Invoke the skill when the user asks to “add flashcards”, “cloze this”, “quizify”, or similar.  The target file must already exist; never create new files or edit submodules/private content without permission.  Process one paragraph or logical block at a time and display the original text for confirmation.  Aim for at least 92 % coverage of each paragraph and about 80–92 % of every sentence.  Numeric facts or simple assignments may be clozed as atomic units.

## Workflow

1. **Consult examples.**  Scan the index of representative patterns earlier in this file for descriptions matching the current passage.  Refer to the matching example numbers in your reasoning (e.g., “behaviour like example 3’s QA rewrite”).
2. **Select a paragraph or contiguous block.**  Work on one at a time.  Use a separate tool call per paragraph rather than batching.  Pause after each block to retrieve the next.
3. **Break text into meaning units.**  Look for definitions, names, dates, formulas, list items, pros/cons, conditional or contrast clauses, and semicolon‑separated ideas.  Treat each as a potential card.  If a sentence is mostly visible, add another cloze.  Do not hide an entire short sentence with no anchor word; leave a hint word or two visible.
   - Handle semicolon‑separated clauses like a list with separate clozes.
   - For conditional connectors (`if`, `when`, `once`, `unless`), hide the text after the connector unless the condition itself is being tested.
   - For contrastive conjunctions (`but`, `however`, `yet`, etc.) make separate clozes on either side.
4. **Insert clozes guided by examples.**  Use the matched examples as
   templates:
   - Wrap material based on meaning and recall effort rather than rigid word counts.  Dense or confusing ideas get smaller clozes; obvious concepts can be larger.
   - If text already has formatting (bold, italic, code, underline, etc.), enclose the entire formatted phrase inside the cloze rather than inserting braces within it.  For example use `{@{__foo__}@}` instead of `__{@{foo}@}__`.
   - Cloze both a leading proposition and its supporting detail if both are worth testing.  Leave one or two words outside the braces for a contextual hint.
   - When several closely related noun phrases appear, split them into multiple smaller clozes instead of a single huge one.
   - Place the cloze where it best prompts recall—the first word, last word, or middle as the example shows.
   - **Never break a LaTeX equation.**  Hide the entire `$…$` or `$$…$$` block as a single atomic cloze.
   - By default suggest inline clozes; only rewrite to `::@::` or `:@:` if the user explicitly requests QA style or if an example clearly uses that format.
   - Preserve Markdown, KaTeX, links, and line ordering.  Lists are handled item‑by‑item unless an example demonstrates a combined deletion.
5. **Apply the edits directly** in the file and return the modified text.
   Provide alternate versions or explanations only if the user asks.

## Continuous improvement

- (See the companion file `continuous_improvement.md` for a standalone summary and quick reference; keep it sync'd when the main section evolves.)
- After suggesting clozes, ask “which deletions are wrong?” or “would you prefer Q/A instead of inline cloze?”  Use corrections to expand the examples or add rules.  When the user states “this is my style”, treat it as a high‑priority rule and immediately encode it in this document, noting which examples or heuristics were updated.
- Analyse user edits using `git --no-pager diff --word-diff --no-color path/to/file.md`.  Word diffs reveal boundary shifts and merged or expanded clozes; use them as training data and add corresponding examples.
- Watch for feedback about excessive fragmentation.  Merge adjacent tiny deletions in future and update the rules accordingly.
- When the user modifies or adds contiguous paragraphs, capture the whole block as a single example tagged appropriately so the agent can recognise similar multi‑paragraph patterns later.
- Never suggest running any external command during editing.  Command advice is irrelevant to this skill.
- If session memory grows large (≈20 examples or after a long session), summarise learned rules and cement them in this document. Prompt the user before consolidating.

## Representative examples

Several patterns recur frequently; the first five entries below illustrate the kinds of transformations you should perform.  When editing a new passage, recall which example best matches and mimic its cloze placement and style.

1. **Dense math paragraph** – multiple expressions and annotations require many inline clozes so each formula or qualifier can be tested separately.
2. **Long technical paragraph** – break a single sentence containing several logical ideas into separate deletions rather than one giant blank.
3. **Circuit cancellation description** – sequential procedural text with paired concepts gets split at each step; retain anchors such as “easiest way” or “however”.
4. **Transform hierarchy statement** – simple declarative sentence with nested subjects encourages small, discrete clozes for each noun phrase.
5. **Concentration/spread of Fourier transform** – comparative statement best handled by clozing each contrasted clause individually.

Below are the full before/after examples for reference (copy them into the agent’s reasoning when needed):

```text
Input: If _f_ is (annotation: of exponential growth; then) also causal, and analytical, then: ${\widehat {f} }(i\tau )=F(-2\pi \tau )$. Thus, extending the Fourier transform to the complex domain means it includes the Laplace transform as a special case in the case of causal functions—but with the change of variable _s_ = _i_<-- markdown separator -->2π<-- markdown separator -->_ξ_. (annotation: That is, make any expression containing _ξ_ in the form of that on the right hand side, then simply replace it with _s_. Now the Fourier transform with _ξ_ as input becomes the Laplace transform with _s_ as input.)
Output: If _f_ is {@{(annotation: of exponential growth; then) also causal, and analytical}@}, then: {@{${\widehat {f} }(i\tau )=F(-2\pi \tau )$}@}. Thus, extending {@{the Fourier transform to the complex domain}@} means it includes {@{the Laplace transform as a special case}@} in the case of {@{causal functions}@}—but with {@{the change of variable _s_ = _i_<-- markdown separator -->2π<-- markdown separator -->_ξ_}@}. (annotation: That is, make {@{any expression containing _ξ_}@} in the form of that on {@{the right hand side}@}, then simply {@{replace it with _s_}@}. Now {@{the Fourier transform with _ξ_ as input}@} becomes {@{the Laplace transform with _s_ as input}@}.)
```

```text
Input: From another, perhaps more classical viewpoint, the Laplace transform by its form involves an additional exponential regulating term which lets it converge outside of the imaginary line where the Fourier transform is defined. As such it can converge for at most exponentially divergent series and integrals, whereas the original Fourier decomposition cannot, enabling analysis of systems with divergent or critical elements. Two particular examples from linear signal processing are the construction of allpass filter networks from critical comb and mitigating filters via exact pole-zero cancellation on the unit circle. Such designs are common in audio processing, where highly nonlinear phase response is sought for, as in reverb.
Output: From another, perhaps {@{more classical viewpoint}@}, {@{the Laplace transform by its form}@} involves {@{an additional exponential regulating term}@} which lets it converge {@{outside of the imaginary line}@} where {@{the Fourier transform is defined}@}. As such it can {@{converge for at most exponentially divergent series and integrals}@}, whereas {@{the original Fourier decomposition cannot}@}, enabling {@{analysis of systems with divergent or critical elements}@}. Two particular examples from {@{linear signal processing}@} are the construction of {@{allpass filter networks from critical comb}@} and {@{mitigating filters}@} via {@{exact pole-zero cancellation on the unit circle}@}. Such designs are {@{common in audio processing}@}, where {@{highly nonlinear phase response}@} is {@{sought for, as in reverb}@}.
```

*The remaining examples follow the same pattern; open the files for more entries if needed.*

## Heuristics and rules

The form of the examples above is complemented by a set of practical heuristics, which are now incorporated below under the appropriate sections (learned rules no longer require a separate file).

### General editing principles

- Preserve the source verbatim except for cloze markup; do not paraphrase or reflow text.
- Equations stay whole: wrap an entire `$...$` or `$$...$$` block in a single cloze; never split math.
- **Prompt length is irrelevant for calculations.**  When constructing two‑sided or one‑sided cards involving numeric problems, copy every number, parameter, and even full equations to the left of the separator; the prompt may be arbitrarily long.  The warning rules in the validator are designed to catch cases where the answer cannot possibly be deduced from the prompt, not to force brevity.  Resist any urge to split a single calculation across multiple cards purely to shorten the left-hand text – that reduces clarity and defeats the purpose of spaced repetition.
- Anchor context: leave visible words around each deletion to give a hint; avoid blanking a sentence entirely unless context is crystal clear.
- Mirror the user’s style when they supply examples or corrections.
- Preserving HTML entities and escapes exactly; treat them as opaque literals.
- Submodule safety: never edit `private/`, `self/`, or other submodules without explicit authorization.

### Sentence and clause handling

- Work paragraph by paragraph; add clozes only within a single paragraph before moving on.
- Break long sentences with multiple ideas into separate cards rather than one huge deletion.  Semicolon lists get individual clozes per clause.
- Split around contrastive conjunctions (`but`, `however`, etc.) and keep conditional connectors (`if`, `when`, etc.) visible unless the condition itself is tested.
- Default to inline clozes; use `::@::` or `:@:` only if the user requests QA style or an example clearly shows it.
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
