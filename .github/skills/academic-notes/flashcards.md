# Flashcard conventions (academic notes)

- Use the `::@::` marker after a linked term to add a concise definition or gloss that will be converted into flashcards by the pipeline. Example:

`- programming paradigm ::@:: It is a relatively high-level way to conceptualize and structure the implementation of a computer program.`

- Flashcard activation tag pattern: `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` where `<INSTITUTION>` is the canonical short name for the university (e.g., `HKUST`, `MIT`) and `<PAGE>` is the page identifier using underscores for spaces (e.g., `COMP_3031`).

- Prefer to attach cloze-style hints or one-line glosses only when the item is concise (single sentence or phrase). Long derivations or full proofs should not be auto-flashcarded.

- When adding generated flashcards, keep the `::@::` content short (1–2 sentences); long paragraphs will create poor flashcards.

- Preserve existing course-scoped `flashcard/active/...` tags when normalizing. If a course file is missing the tag, propose adding one in a small PR rather than mass-editing.
