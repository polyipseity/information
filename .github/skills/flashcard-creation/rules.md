# Flashcard‑creation Rules

This file lists concise, actionable heuristics the agent follows when
generating or editing flashcards.  It is read alongside the examples file
and is intended to be fast to scan.

- **Preserve the source verbatim.** Except for inserting or moving the cloze delimiters `{@{` and `}@}`, leave every word, punctuation mark, and spacing unchanged.  Do not paraphrase, reflow, or reformat the text; the only edits allowed are the cloze markers themselves.
- **Equations stay whole.** Wrap entire `$...$` or `$$...$$` blocks in a single cloze if they must be hidden.  Never split or partially delete math expressions; doing so breaks rendering.
- **Anchor context.** Always leave one or more visible words around each cloze so the learner has a hint.  Avoid hiding a sentence in its entirety unless adjacent context makes the meaning crystal clear.
- **Work paragraph by paragraph.** Read a paragraph, add clozes only to that paragraph, then move on.  This ensures no large section is skipped accidentally.
- **Break long sentences.** If a sentence contains multiple logical fragments or ideas, split it into two or more cards rather than forcing a single giant deletion.  Refer to the examples index for our standard patterns.
- **Default to inline clozes.** Use `{@{ }@}` unless the user explicitly asks for `::@::` or `:@:` format.  Q/A style rewrites are only used when an existing example shows the format.
- **Two‑sided QA lists.** When the user indicates an entire section should become a list of question/answer pairs, preserve the source text and create a markdown list of `Q ::@:: A` or `Q :@: A` items.  Start the list with a horizontal rule and the exact phrase “Flashcards for this section are as follows:” on a blank line so the intention is unmistakable.  Handle each bullet separately and never merge multiple list items unless an example says to do so.
- **Treat adjacent paragraphs as a unit if edited together.** Add a new example entry when two or more consecutive paragraphs are meant to be learned as one concept; this teaches the model to reproduce multi‑para edits.
- **Mirror the user’s style.** When incorporating user‑provided examples, copy their preferred cloze placement, punctuation, hyphenation, and ordering.  Annotate the example table where useful so future matches behave similarly.
- **Split subject/object in declarative sentences.** For simple statements with a named subject followed by its description, consider hiding the subject and the object separately rather than one long cloze.  This yields smaller, more focused cards.
- **Use the examples index actively.** Before editing, search the index for similar cases and keep those examples open while you work.  The index lookup and cross‑referencing should be part of the editing workflow.
- **Year handling.** Only cloze a year if it is central to the idea.  If the date is incidental, leave it visible.
- **Feedback loop.** If the user alters your output, compare before and after, then update `rules.md` or add a new example so future prompts follow the corrected behaviour.
- **Short sentences and simple assertions.** Do not hide an entire brief declarative sentence in one cloze.  Split the sentence into subject and predicate deletions (e.g. `{@{Mispricing}@} leads to {@{arbitrage}@}`). Numeric values or variable assignments can be hidden whole if needed.
- **Semicolon lists.** When semicolons separate related clauses, wrap each clause in its own cloze so the learner can recall them individually.
- **Article/qualifier placement.** Include leading articles (`the`, `a`, etc.), possessives, prepositions, or qualifiers inside the cloze. The visible context should follow the deletion.  For example, `{@{the market exposure}@}` is preferred over `the {@{market exposure}@}`.
- **Contrastive conjunctions.** Split around *but*, *however*, *yet*, *although* etc. rather than creating a single multi‑idea cloze.
- **Conditional connectors.** When a sentence begins with *if*, *when*, *once*, *unless* or similar, keep the connector visible unless the entire condition is being tested.  Place the cloze after the word.
- **Minimal semantic cloze.** Hide the smallest meaningful unit that still tests the concept.  Adjust patterns when the user moves a word into or out of the cloze.
- **No command suggestions.** This skill edits text only; do not suggest running `init generate` or any other command as part of flashcard creation.
- **Preserve HTML entities and escapes.** Treat sequences like `&nbsp;`, `\$`, `\$&nbsp;123` as opaque literals.  Do not convert entities to spaces, alter backslashes, or break them across clozes.
- **Submodule safety.** Never edit files under `private/`, `self/`, or any git submodule unless the user explicitly authorizes it.

Continue adding to this file as new heuristics arise during sessions.
