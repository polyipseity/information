---
name: flashcard-creation
description: |
  Help the user add spaced-repetition flashcards (cloze deletions or Q/A
  pairs) to existing Markdown notes across the repository.  The skill
  encapsulates the multi‑step process the user follows in their finance
  lecture notes (e.g. FINA 3103) and elsewhere: read the prose, identify
  key terms, dates, formulas and logical assertions, and wrap them using
  pytextgen cloze markup (`{@{ }@}`, `::@::`, `:@:`).  Use existing files
  with flashcards as style guides and adapt the output based on user
  feedback.  The skill also suggests regeneration commands once flashcards
  are inserted.
---

# Flashcard Creation Skill

> **MUST read this skill document _and the companion `examples.md` file every time you use the skill.**
> There is no exception: the examples are the authoritative guide.  They
> include a semantic index and actual before/after pairs; you must open
> and consult them at the start of every invocation to ensure behaviour
> consistency and to absorb any new formatting rules.
>
> **Note when editing `examples.md`:** it is a shared, line‑sensitive file.
> Insert new examples only at the appropriate location, update the index
> table, and double‑check that you have not modified surrounding entries.
> Avoid bulk search‑and‑replace operations; a misplaced edit will confuse
> future invocations of the skill.

This skill codifies the pattern the user has been applying when
transforming ordinary notes into flashcard‑enabled material.  It is
intended for interactive use via chat: `/flashcard-creation` followed by a
path, a snippet, or a description of the content to process.  Permanent
input/output examples are kept in `examples.md` in this folder; consult
that file when in doubt.

## When to invoke

- The conversation indicates the user wants to add flashcards, cloze
  deletions, quizzes, or active‑recall questions to existing Markdown
  notes.  Phrases like “make flashcards”, “add clozes”, “quizify this”
  or “convert to Q/A” should trigger you to suggest using this skill.- You need to convert prose in an existing `.md` file into active recall
  flashcards.
- The file already exists and is part of `general/`, `special/`, or any
  other directory; do *not* create new files.
- You want to follow the user's personal style, which emphasises logical
  chunks, names, dates, and conceptual definitions.
- You will be iteratively improved by user feedback: after suggesting
  clozes, the user may correct or refine them, and the skill should
  remember those refinements for future invocations.

## Core workflow

> **Verbatim preservation.** Every edit must keep the original text
> exactly as written; only add the cloze delimiters `{@{` and `}@}`.  Do
> not rephrase, reorder, or reflow the prose when inserting cards.  In
> particular, treat HTML entities like `&nbsp;` and escaped characters
> such as `\$` as opaque literals; do not convert them into spaces or
> remove the backslash.

The examples in `examples.md` are the *style guide*, not optional
reading.  Every invocation should begin by opening that file, scanning the
semantic index for relevant tags, and mentally aligning the source text
with one or more before/after pairs.  Match the existing examples' structure
and phrasing as closely as possible – if the input looks like example 7,
apply the same transformations that example 7 used.

1. **Gather the material.**  Accept either a file path (plus line range or
   heading context) or literal paragraphs from the user.  Show the exact
   original text back so the user can confirm you are editing the right
   passage.

   **Work paragraph by paragraph.**  Only read and modify one paragraph at a
   time: pause after completing a paragraph, then fetch the next.  Use a
   separate tool call for each paragraph rather than batching edits across
   multiple paragraphs.  This discipline forces you to target each chunk of
   prose individually, avoids missed sentences, and makes it easier to hit
   high coverage targets.

   **Aim for very high coverage.**  Strive for at least 92 % of the text in a
   paragraph to be hidden by clozes, and try to cover 80–92 % of the words in
   each sentence (leaving just a contextual hint).  If a sentence is still
   mostly visible after the first pass, add another cloze until the target
   is reached.  Do not hide an entire brief declarative sentence as a single
   cloze; instead split it so at least one nearby word remains visible.  The
   exception is numeric facts or variable assignments, which may be clozed as
   atomic units since they convey a single piece of information (e.g.
   `{@{the risk‑free rate is 4%}@}`).

2. **Read the index first.**  Open `examples.md` and scan the index table
   at the top, looking for tags or descriptions that resemble the current
   passage.  This immediate orientation helps you select relevant
   examples before touching the text.

3. **Locate analogous examples.**  Once you have candidates from the index,
   read the corresponding examples in full.  Identify one or more entries
   whose tags and prose structure match the source.  Note which example
   number(s) informed your thinking when you describe your changes (e.g.
   “behaviour like example 3’s QA rewrite”).  You should refer back to these
   examples repeatedly while constructing clozes, ensuring consistency
   throughout the process.

4. **Break the text into cards.**  Think in terms of *meaning units* rather
   than fixed word counts.  Complex or counter‑intuitive ideas usually
   deserve smaller, more focused deletions; simple, natural concepts can
   be wrapped together even if they span a full clause.  Identify
   definitions, names/dates, formulas, list items, advantages/limitations,
   and natural question/answer pairs.  Handle semicolon‑separated clauses as
   if they were a short list, giving each clause its own cloze, and treat
   clauses joined by contrastive conjunctions (but, however, yet, etc.) as
   separate cards on either side of the conjunction.  When sentences begin
   with conditional words such as *if*, *when*, *once* or *unless*, hide
   the text following the connector rather than the connector itself unless
   the condition is being tested.  If the source contains multiple distinct
   ideas, make separate cards for each – see example 13’s anti‑conglomerate
   rule.  Aim for roughly 92 % coverage across the passage, avoiding long
   runs of text with no cards at all; if coverage is low, revisit the
   paragraph immediately and add more deletions.

5. **Apply cloze syntax by example.**  Using the matched example(s) as a
   template:
   - Wrap material based on the **meaning and expected recall effort** rather
     than rigid boundaries.  When a concept is intuitive or easy to infer,
     you can hide more of it; conversely, err on the side of smaller
     deletions when the idea is dense or prone to confusion.  The goal is
     to make the card a challenge with a clear, discoverable answer.
   - If a piece of text is already surrounded by Markdown formatting
     (bold, italic, code, underline, etc.), the cloze should encompass the
     entire formatted phrase rather than inserting the braces inside the
     markup.  This preserves the original styling and avoids awkward
     constructions like ``__{@{foo}@}__``; instead use ``{@{__foo__}@}``.
   - When a sentence consists of a leading propositional phrase followed
     by one or more details, **apply clozes to both parts separately**.  For
     example, in "Biases arise along two dimensions: how information is
     processed and how decisions are subsequently made and acted upon",
     hide both the opening proposition and the trailing list of dimensions.
     The goal is to test recall of the relationship *and* the specifics,
     unless the supporting details are trivial and the user indicates a
     preference for a single, larger deletion.  If you discover a new
     pattern while editing, add an illustrative example to `examples.md`.
   - Always leave at least one or two leading/trailing words outside the
     cloze so the learner has a contextual hint; avoid hiding an entire
     sentence or clause with no anchors.
   - When a sentence contains multiple closely related noun phrases or
     descriptive segments, don’t bundle them into a single large cloze.  A
     better option is to split the sentence into several smaller clozes,
     each covering a single conceptual chunk (see new example 22 and example 23).
   - Place the deletion strategically within the semantic unit: sometimes
     leaving the first or last word visible helps prompt the response,
     other times the middle is better – follow whatever the example does.
   - **Do not break LaTeX equations.**  If the flashcard involves a formula
     or any `$...$`/`$$...$$` block, hide the whole expression as a single
     cloze rather than clozing part of it; this prevents rendering problems
     and matches user preference.  Equations count as atomic units.
   - By default, generate **cloze deletions only**.  Convert to a
     `question ::@:: answer` or `:@:` style card only if the user specifically
     requests a Q/A format or if an example clearly demonstrates that style.
     Q/A rewrites are not the norm and should not be assumed.
   - Preserve Markdown, KaTeX, and links intact; examples never reflow or
     split lines.
   - Lists are handled item‑by‑item unless an example demonstrates a
     combined deletion.
   - Keep formulas whole unless an example clozes part of the
     relationship (see example 5’s treatment of a scaling property).

6. **Apply the edits directly.**  Once you’ve chosen clozes based on the
   examples and meaning units, modify the file in place without showing a
   separate preview.  Ask the user only if they want a variant or need a
   justification; otherwise assume the change is final.

By anchoring every step in concrete examples, the workflow automatically
reflects the user’s existing flashcard style and makes iterative feedback
straightforward.

## Continuous improvement

- After delivering suggestions, solicit explicit feedback such as
  "which deletions are wrong?" or "prefer Q/A instead of inline cloze"
  so the skill accumulates examples.
- When a user declares “this is my style” or otherwise characterises their
  personal flashcard preferences, treat that remark as a high‑priority rule
  and immediately incorporate it into the examples and guidelines.  The
  agent should mention which existing examples or rules were updated to
  reflect the new style.

- When the user edits your clozes, inspect the **git diff** output
  with word‑level highlighting and without a pager, for example:

  **Academic note paths:** when working specifically on `special/academia`
  course notes, remember that every cloze gloss should include the full
  hierarchical path (e.g. `ELEC 1100 / topic / subtopic`) before `::@::`.
  The generator relies on literal text; do not assume nested bullet indentation
  will supply context.  This requirement is addressed in the academic-notes
  skill, but reinforcing it here helps keep flashcard creation consistent
  across formats.

  ```sh
  git --no-pager diff --word-diff --no-color path/to/file.md
  ```

  The `--no-pager` flag ensures the entire diff is printed in one shot so
  you can see multiple word changes in context; otherwise a truncated view
  might hide how an adjustment interacts with earlier words.  Word diff
  marks deletions as `[-deleted text-]` and additions as `{+added text+}`.
  Read adjacent markers together: if two `[- -]` groups are separated by a
  single space, the user probably merged two clozes, and `[-foo-] {+foo bar+}`
  means they expanded a hidden region.  Observing several markers in the
  same sentence helps you infer boundary shifts that would be missed by a
  simple line diff.

  Treat the annotated output as a mini‑training dataset: note whether the
  user moved a cloze to include a formatting delimiter, hid a leading
  proposition instead of details, merged adjacent small clozes, or made
  any other systematic adjustment.  Update `examples.md` (and, if
  necessary, `rules.md` or this document) with a new entry capturing the
  pattern.  Over time, the cumulative diffs should be the primary driver of
  your continuous learning.

- Pay attention when the user criticises fragmentation or "too many
  small clozes".  If they request merging adjacent deletions into a
  larger cloze, update the rule set and examples accordingly so the
  model learns to avoid excessive micro‑clozing in future.

- Store a handful of representative before/after samples (privately in
  session memory) and refer to them when making subsequent suggestions.

- When the user corrects the style, incorporate that rule into the next
  iteration (e.g., "never cloze the year unless it's central to the
  concept").  In particular, if the user edits your cloze output you
  should compare the two versions, identify the discrepancy, and update
  the permanent guidance (either in `SKILL.md` or `examples.md`) so the
  rule is remembered.

- **Deep review of edits.**  Take extra time when the user revises your
  changes: read through every modification in the file, note patterns
  such as clozed full sentences or numeric facts, and explicitly add a
  corresponding example or rule.  This thoughtful analysis is essential
  for aligning the model with the user's personal flashcard style.

- **New:** when the user modifies or adds contiguous paragraphs (as in
  the CAPM/SIM example), treat the entire block as a single learning
  unit and add a corresponding entry in `examples.md`.  The index table
  should be updated with a brief description and relevant tags so the
  agent can match similar multi‑paragraph structures in the future.
  This helps the model generalise to multi‑sentence transformations.

- **Equation rule:** never insert a cloze inside a LaTeX equation; if the
  flashcard involves a mathematical expression, the entire equation block
  must be hidden as a single deletion.  This avoids partial hides that
  break rendering and aligns with the user's preferred style.

- **Minimal-cloze awareness:** strive to hide the smallest meaningful
  unit that still challenges recall.  If a user edits your suggestion to
  remove a leading article, conjunction or pronoun from a cloze, adjust
  future cards accordingly and consider adding an example illustrating the
  corrected boundary.  Minimal clozes make cards crisper and reduce
  unnecessary reveal of context.

  *However*, avoid creating a string of tiny adjacent deletions that each
  cover only one or two words.  When you find consecutive small clozes
  separated by only a word or two, consider merging them into a single
  deletion that spans the intervening text.  This reduces fragmentation,
  keeps cards focused on coherent ideas, and prevents the flashcards from
  feeling like a list of trivia bits.

- **Command‑avoidance rule:** the skill should not suggest running any
  commands (e.g. `init generate`) when editing text; such operational
  advice belongs elsewhere and is never relevant during interactive
  flashcard creation.

- **Long‑term consolidation**: if session memory grows large (more than
  about 20 examples or after a prolonged editing session), summarise the
  learned rules and append them to this skill folder.  The preferred
  destination for paired examples is `examples.md`; rules and distilled
  guidelines may live in `rules.md` or in the same file if convenient.  An
  index at the top of `examples.md` should list all entries so they can be
  rapidly consulted.  The agent can prompt the user once it detects many
  corrections: "I've collected many flashcard edits—shall I merge the
  distilled guidelines into the permanent skill doc or create a new
  note in the skill directory?" Once the user agrees, a new entry is
  added in the appropriate skill folder file and the session memory
  trimmed.
  **Personal style updates:** When the user explicitly states a stylistic
  preference (e.g. “this is my style”), the agent should automatically copy
  that preference into session memory and consider adding a corresponding
  example or rule immediately, even if session memory has not yet grown
  large.  This ensures fast adaptation to the user’s habits.
This continual learning mechanism ensures the skill evolves without
losing earlier insights.  See `rules.md` for a summary of the most
important, stable rules that have emerged from past sessions.

## Example inputs & outputs

Rather than crowd this document with long transcripts, example input/output
pairs are stored separately in the `examples.md` file located in this skill
folder (`.github/skills/flashcard-creation/examples.md`).  Each entry is
accompanied by semantic **tags and descriptions** (e.g. `math-heavy`,
`list items`, `partial clozes`, `Q/A style`) which form an index of the flashcard
placement semantics, styles, and notable decisions.  The agent should always
consult that file when generating or refining flashcards.  When new examples
are collected during a session, the agent can append them to the file and
update the index table with appropriate tags.

## Related customizations

- A companion `rules.md` file may be used to collect distilled
  heuristics and stylistic bullet points that do not naturally fit into
  an example pair.  The agent should consult `rules.md` alongside
  `examples.md` when generating clozes.  See the newly created
  `rules.md` for current guidance.

- Consider a companion prompt (`flashcard-creation.prompt.md`) that asks
  the user for the file path and lines to process.
- A custom agent could iterate over an entire directory, creating
  flashcards file-by-file and asking for confirmation on each change.

## Implementation notes

- The implementation may be purely heuristic; it does not need to run
  pytextgen or parse Markdown deeply.  Simplicity is fine as long as
  results are usually reasonable and the user can refine them.
- Do *not* modify files under `private/` or submodules without explicit
  permission.  The skill should operate only on visible Markdown notes.

---

Using this skill should make flashcard creation more efficient while
preserving the user's established style.  Keep the dialogue interactive
and remember past corrections to improve future suggestions.

> **Reminder (end of document):** before you perform any editing or
> suggestion, make sure you have opened and read `examples.md`.  The
> examples are the ultimate reference and must be consulted each time.
