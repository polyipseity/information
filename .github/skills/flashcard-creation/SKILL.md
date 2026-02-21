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

This skill codifies the pattern the user has been applying when
transforming ordinary notes into flashcard‑enabled material.  It is
intended for interactive use via chat: `/flashcard-creation` followed by a
path, a snippet, or a description of the content to process.

## When to invoke

- You need to convert prose in an existing `.md` file into active recall
  flashcards.
- The file already exists and is part of `general/`, `special/`, or any
  other directory; do *not* create new files.
- You want to follow the user's personal style, which emphasises logical
  chunks, names, dates, and conceptual definitions.
- You will be iteratively improved by user feedback: after suggesting
  clozes, the user may correct or refine them, and the skill should
  remember those refinements for future invocations.

## Core workflow

1. **Surface the source text.**  Accept either a file path or the raw
   paragraph(s) the user wants to flashcard.  If a path is given, read the
   relevant lines from the workspace.

2. **Scan for key information.**  Identify:
   - **Definitions** (`X is …`, `Y refers to …`, `called`, etc.)
   - **Dates & names** ("1976", "Prof. Stephan Ross", etc.)
   - **Equations and formulas** that express relationships
   - **Assumptions, limitations, advantages/disadvantages**
   - **Examples or anecdotes** that encapsulate a concept

3. **Convert to markup.**  For each atomic fact or concept, insert the
   appropriate pytextgen cloze syntax:
   - Use `{@{…}@}` around words or phrases to hide them in review.
   - Use `::@::` to split a question and answer when rewriting a single
     sentence into Q/A form (often for equations or when the answer is
     longer than a few words).
   - Use `:@:` only when the original text already contains a natural
     separation or when a short-answer question is preferable.
   - Preserve existing Markdown formatting, math (KaTeX), and links.
   - Avoid wrapping long sentences or splitting existing lines.

4. **Respect style patterns.**  Examples from the workspace show
   preferred behaviours:
   - Favor clozing the **term** itself first (e.g. `{__Arbitrage Pricing
     Theory__}`) then follow with supporting details.
   - In a list of assumptions/factors, cloze each item individually rather
     than the whole sentence.
   - When a sentence contains multiple facts, cloze them separately rather
     than combining them in one deletion.
   - For formulas, consider clozing the relationship rather than every
     symbol (e.g. `$\bar r_i- r_f = \beta_{i,M}(\bar r_M- r_f)$` may be
     left intact unless teaching the symbol names).
   - Use hard-coded `__bold__` or italic markup where the user would have
     emphasised a term in the original note.

5. **Output** the revised paragraph(s) with cloze markers inserted.  If a
   file path was provided, the skill may optionally patch the file but it
   always shows a diff-like preview for confirmation.

6. **Generate flashcards.**  Remind the user to run:

   ```bash
   uv run -m init generate <file>
   ```

   (add `-C` or `--init-flashcards` as needed) to update the pytextgen
   blocks.

## Continuous improvement

- After delivering suggestions, solicit explicit feedback such as
  "which deletions are wrong?" or "prefer Q/A instead of inline cloze"
  so the skill accumulates examples.
- Store a handful of representative before/after samples (privately in
  session memory) and refer to them when making subsequent suggestions.
- When the user corrects the style, incorporate that rule into the next
  iteration (e.g., "never cloze the year unless it's central to the
  concept").
- **Long‑term consolidation**: if session memory grows large (more than
  about 20 examples or after a prolonged editing session), summarise the
  learned rules and append them to this SKILL.md or a companion note in
  `/memories/repo/` so that future invocations start with an expanded
  rule set.  The agent can prompt the user once it detects many
  corrections: "I've collected many flashcard edits—shall I merge the
  distilled guidelines into the permanent skill doc?" Once the user
  agrees, a new entry is added here and the session memory trimmed.

This continual learning mechanism ensures the skill evolves without
losing earlier insights.

## Example inputs & outputs

- **Input**: first paragraph of `special/academia/HKUST/FINA 3103/...` (as
  given by the user prompt above).
- **Output**: the same paragraph with cloze markers inserted at each
  significant fact, matching the user's example.

- **Input**: a bullet list of CAPM assumptions; **Output**: a list where
  each item has a `{...}` around the assumption phrase.

## Related customizations

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
