---
name: flashcard-creation
description: |
  Help the user add spaced-repetition flashcards (cloze deletions or Q/A pairs) to existing Markdown notes across the repository.  The skill encapsulates the multi‑step process the user follows in their finance lecture notes (e.g. FINA 3103) and elsewhere: read the prose, identify key terms, dates, formulas and logical assertions, and wrap them using flashcard markup (`{@{ }@}`, `::@::`, `:@:`).

  There are three supported forms:

  - **Cloze** (`{@{ }@}`) hides arbitrary text inside paragraphs.
  - **Two-sided QA** (`::@::`) on a single line, yielding two cards.
  - **One-sided QA** (`:@:`) on a single line, yielding a single card.

  For the QA formats remember the line-only rule; if visual separation is needed insert `<br/>`/`<p>` instead of newline characters.  The examples in `examples.md` illustrate all three types.  Use existing flashcard files as style guides and adapt the output based on user feedback.  The skill also suggests regeneration commands once flashcards are inserted.
---

# Flashcard Creation Skill

This skill automates the user’s process for converting Markdown prose into active‑recall flashcards.  It works interactively: you provide a file path or text snippet, the agent edits it in place with cloze markup, and the user refines.  The skill supports three forms of flashcards—inline cloze (`{@{ }@}`), two‑sided QA (`::@::`), and one‑sided QA (`:@:`).  QA cards must fit on one Markdown line; use `<br/>` or `<p>` for visual breaks.

All style decisions are driven by `examples.md`, which contains before/after pairs indexed by semantic tags.  Open that file on every invocation and refer to the relevant example numbers in your reasoning.  When you encounter a new pattern plant a new entry there and update its index table.  A companion `rules.md` may hold distilled heuristics that do not fit as examples.  An optional prompt file (`flashcard-creation.prompt.md`) can solicit path/line information.  Do **not** run any commands such as `init generate` in the course of editing; operational advice belongs elsewhere.

**Academic content:** if editing `special/academia` material also consult the `academic-notes` skill for course‑specific conventions such as full hierarchical gloss paths and QA list separators; it links back here for general guidance.

## When to use

Invoke the skill when the user asks to “add flashcards”, “cloze this”, “quizify”, or similar.  The target file must already exist; never create new files or edit submodules/private content without permission.  Process one paragraph or logical block at a time and display the original text for confirmation.  Aim for at least 92 % coverage of each paragraph and about 80–92 % of every sentence.  Numeric facts or simple assignments may be clozed as atomic units.

## Workflow

1. **Consult examples.**  Scan the index in `examples.md` for tags or descriptions matching the current passage.  Read the full examples and keep them visible while you edit.  When reporting back, state which example(s) influenced your choices (e.g. “behaviour like example 3’s QA rewrite”).
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

- After suggesting clozes, ask “which deletions are wrong?” or “would you
  prefer Q/A instead of inline cloze?”  Use corrections to expand the examples or add rules.  When the user states “this is my style”, treat it as a high‑priority rule and immediately encode it in `examples.md` and/or `rules.md`, noting which entries were updated.
- Analyse user edits using `git --no-pager diff --word-diff --no-color path/to/file.md`.  Word diffs reveal boundary shifts and merged or expanded clozes; use them as training data and add corresponding examples.
- Watch for feedback about excessive fragmentation.  Merge adjacent tiny deletions in future and update the rules accordingly.
- When the user modifies or adds contiguous paragraphs, capture the whole block as a single example tagged appropriately so the agent can recognise similar multi‑paragraph patterns later.
- Never suggest running any external command during editing.  Command advice is irrelevant to this skill.
- If session memory grows large (≈20 examples or after a long session), summarise learned rules and append them to `examples.md` or `rules.md`. Prompt the user before consolidating.

## Examples & related files

All input/output pairs live in `examples.md` with semantic tags such as `math-heavy`, `list items`, `partial clozes`, or `Q/A style`.  Use the index table to find relevant examples.  Append new entries when you learn a new pattern and update the index.  `rules.md` may hold high-level heuristics that don’t fit well as examples.  An optional prompt file can gather path/line parameters.

## Implementation notes

- The skill may be purely heuristic; there is no need to parse Markdown deeply or run pytextgen.  Simple text manipulation is sufficient if the results are usually reasonable and users can refine them.
- Only edit visible Markdown notes; do not modify `private/` or any submodule content without explicit permission.
- Dialogue should remain interactive and improvement-driven; remember past corrections to improve future performance.

Using this skill makes flashcard creation faster while faithfully following the user’s style.  Always start by reading `examples.md`—the examples are the ultimate reference.
