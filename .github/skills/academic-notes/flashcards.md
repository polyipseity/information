# Flashcard conventions (academic notes)

- Use the `::@::` marker after a linked term to add a concise definition or gloss that will be converted into flashcards by the pipeline. Example:

`- programming paradigm ::@:: It is a relatively high-level way to conceptualize and structure the implementation of a computer program.`

- **Two-sided lists:** Some sections may instead use explicit question/answer pairs (a two-sided flashcard format) rather than cloze deletions. When doing so, precede the list with a horizontal rule (`---`) and the exact sentence:

  ```text
  Flashcards for this section are as follows:
  ```

  The separator helps readers and tooling distinguish the QA list; place a
  blank line between the `---` rule and the phrase for readability.  Each
  item after the phrase should use `question ::@:: answer` or `question :@:`
  syntax as usual.
- Flashcard activation tag pattern: `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` where `<INSTITUTION>` is the canonical short name for the university (e.g., `HKUST`, `MIT`) and `<PAGE>` is the page identifier using underscores for spaces (e.g., `COMP_3031`).

- Prefer to attach cloze-style hints or one-line glosses only when the item is concise (single sentence or phrase). Long derivations or full proofs should not be auto-flashcarded.

- When adding generated flashcards, keep the `::@::` content short (1–2 sentences); long paragraphs will create poor flashcards.
- Folder bullets: if you create a parent bullet purely to group related cards, label it with the full path (e.g. `ELEC 1100 / class expectations`); this makes the hierarchy explicit even when the folder itself has no direct flashcards.  Nesting may be multiple levels deep; feel free to group a subgroup under a second or third level, for example:

  ```text
  - ELEC 1100 / robotics introduction / features
    - ELEC 1100 / robotics introduction / features / artificial ::@:: …
    - …
  ```

  If a folder contains only a single gloss and the parent has no `::@::` of its own,
  collapse it by putting the full path on the gloss line instead of adding an
  extra layer.  (This keeps the structure compact and avoids redundant
  indirection.)

- Preserve existing course-scoped `flashcard/active/...` tags when normalizing. If a course file is missing the tag, propose adding one in a small PR rather than mass-editing.
- **Full path requirement:** every gloss must begin with the complete hierarchical path (e.g. `ELEC 1100 / teaching methodology / traditional limitations`); do not rely on indentation or section headers to convey context. Indentation may be used purely for readability, but the text itself is what the flashcard generator sees.
- **Session headers:** do not introduce artificial parent folders such as “Week 1 lecture 1”. The surrounding `###` header already provides context for the session and should not be repeated in the gloss path.
