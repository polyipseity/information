# Flashcard‑creation Rules

This auxiliary file collects stable heuristics and stylistic points for
use during flashcard generation.  It is consulted in addition to
`examples.md` whenever the agent needs a quick reminder of behaviour.

- **Preserve equations.** Never hide part of a LaTeX expression; if a
  card needs mathematical content, wrap the entire `$...$` or `$$...$$`
  block in one cloze.  Partial deletions inside equations break rendering
  and are forbidden.

- **Contextual anchors.** Leave at least one or two words outside each
  cloze to provide a hint.  Avoid clozing an entire sentence with no
  visible anchors unless the surrounding text makes the meaning
  obvious.

- **Process one paragraph at a time.**  Work through the source text
  paragraph by paragraph: read a single paragraph, add clozes to that
  paragraph only, then move on.  This guarantees high coverage and avoids
  accidentally leaving large swaths of prose untagged.

- **Split long sentences.** When a sentence contains multiple logical
  chunks, break it into two or more cards.  Don’t attempt to cram a
  paragraph into a single deletion; refer to examples 22 and 23 for the
  usual pattern.

- **Default to inline clozes.** Generate `{@{ }@}` deletions unless the
  user explicitly requests a `::@::` or `:@:` question‑answer format.
  Q/A rewrites occur only when an example demonstrates that style.

- **Lists by item.** Handle list elements individually; do not combine
  separate bullets unless an example shows otherwise.

- **Two‑paragraph units.** If the user edits consecutive paragraphs as a
  single conceptual block (e.g. continuous prose under a heading), treat
  them as one learning unit and add a new example entry.  This helps the
  model recognise and reproduce multi‑paragraph transformations.

- **Mirror user style.** When incorporating a new example from the user,
  pay attention to their preferred cloze ordering, punctuation, and
  hyphenation.  Update the index table and, where practical, add a note in
  the example description so future matches automatically mimic that
  style.

- **Split subject and object when appropriate.** If a declarative sentence
  names an item followed by its description (e.g. “two macro variables drive
  the returns of a regulated utility and an airline”), consider hiding the
  subject and the object as separate clozes rather than a single long
  deletion.  This mirrors the user’s preference for smaller, focused cards.

- **Use examples as a living guide.** Before making any edits, read the
  `examples.md` index to find similar cases, then keep those examples open
  and consult them as you insert clozes.  The index lookup and continual
  referencing should be treated as an essential part of the workflow rather
  than an optional step.

- **Year handling.** Years are clozed only when central to the idea; if
  they are incidental (e.g. historical date in passing) leave them
  visible.

- **Feedback loop.** When the user modifies your output, compare the
  before/after, derive a rule, and update either `rules.md` or
  `examples.md` so future suggestions respect the correction.  In most
  cases you will perform both edits simultaneously: add an example that
  demonstrates the change and a rule that explains why it was needed.

- **Short declarative sentences.** Do *not* hide an entire brief
  declarative sentence as a single cloze.  Instead, split it into
  separate deletions for the subject and predicate (e.g. use
  `{@{Mispricing}@} leads to {@{arbitrage}@}` rather than hiding the
  whole phrase).  Numeric quantities and variable assignments remain
  fair game to hide (for example, `{@{the risk-free rate is 4%}@}`),
  but simple English statements should be divided so that the learner
  sees at least one contextual word outside each cloze.

- **Semicolon lists.** When a sentence uses semicolons to enumerate
  related clauses (e.g. the three realistic assumptions of APT), treat
  each clause as an independent card.  Each item should be wrapped in
  its own cloze so the learner can recall them individually.

- **Article placement.** If a noun phrase begins with an article or
  possessive (`the`, `a`, `an`, `its`, `their`, etc.), include that
  leading word inside the cloze.  The visible context should follow the
  cloze, not precede it.  For example, prefer `{@{the market exposure}@}`
  rather than `the {@{market exposure}@}` when the phrase is being
  hidden.  This matches the user’s style throughout the file.

- **Contrastive clauses.** Conjunctions like *but*, *however*, *yet* or
  *although* generally mark shifts in meaning; generate separate
  deletions on both sides of the conjunction rather than one large
  composite cloze.  This mirrors the user’s preference to test each
  contrasted idea separately.

- **Conditional connectors.** When a sentence begins with a conditional
  word such as *if*, *when*, *once*, *unless*, etc., do not hide the
  connector itself unless the entire condition is being tested.  Place
  the cloze after the conjunction so the visible hint remains intact.
  For example, prefer `If {@{such an opportunity existed}@}` instead of
  `{@{If such an opportunity existed}@}`.

- **Minimal semantic cloze.** Aim to hide the smallest meaningful unit
  that still challenges recall.  Avoid wrapping entire clauses or
  sentences when a shorter noun phrase or verb phrase suffices.  If you
  accidentally hide a leading article or pronoun, move the boundary so
  the visible context stays outside the cloze.  This rule is the
  reverse of the “Article placement” guideline and helps keep cards
  crisp and focused.

- **Avoid command suggestions.** The skill is purely about text edits;
  do not suggest running `init generate` or similar commands as part of
  flashcard creation.

- **No submodule editing.** Never operate on files under `private/`,
  `self/`, or any git submodule unless explicitly authorised by the
  user.

This file should grow gradually as new heuristics are distilled during
sessions.  After each editing spree, consider merging freshly learned
rules here and pruning session memory accordingly.
