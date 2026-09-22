---
name: academic-crud-transcludes
description: Manage transcludes/ directories containing Wikipedia articles included by reference with cloze markup.
---

# Academic CRUD: Transcludes

`transcludes/` directories hold full Wikipedia articles as Markdown files with cloze markup, for use as course reference material. Use one when a course references Wikipedia articles that should be available as study material with flashcards; the articles are Wikipedia content, not authored topic notes.

## Target

`special/academia/<INSTITUTION>/<COURSE>/transcludes/<article>.md`

## Key rules

- Store articles as `.md` files with full frontmatter and cloze markup
- Use `find_wikipedia.py` from `academic-crud-topic-note` for canonical title discovery
- The flashcard tag path includes a `transcludes/` segment (e.g., `flashcard/active/special/academia/HKUST/ELEC 4110/transcludes/Fourier transform`)
- Link from the course `## children` as topic notes
- Use `\[missing\]` for absent fields (see [special.instructions.md](../../instructions/special.instructions.md#missing-data))

## Creating a transclude

1. Discover the canonical Wikipedia title:

   ```bash
   uv run python .agents/skills/academic-crud-topic-note/find_wikipedia.py --limit 5
   ```

2. Ingest the article using the `ingest-wikipedia` skill.
3. Place the resulting `.md` file in `transcludes/`.
4. Add cloze markup (`{@{ }@}`) for key concepts.
5. Add a child link in the course `index.md` `## children` section.

## Updating a transclude

1. Edit the `.md` file directly.
2. Preserve the Wikipedia source structure and cloze markup.

## Deleting a transclude

1. Confirm with the user.
2. Remove the `.md` file.
3. Remove the child link from the course `index.md` `## children` section.

## Examples

### ELEC 4110 transcludes

```markdown
## children

- [assignments/](assignments/)
- [attachments/](attachments/)
- [transcludes/Fourier transform.md](transcludes/Fourier%20transform.md)
- [transcludes/Laplace transform.md](transcludes/Laplace%20transform.md)
```

### PHYS 1314 transcludes

```markdown
## children

- [lab 1/](lab%201/)
- [transcludes/Fresnel equations.md](transcludes/Fresnel%20equations.md)
- [transcludes/Photon.md](transcludes/Photon.md)
```

## Validation

Run `academic-lint` after every edit, passing changed files when known.

The article body is verbatim, so the humanizer pass leaves it untouched; anything you write around it, such as a description in the course `index.md`, is yours to humanize (see "Humanizer pass" in `academic-ingest`).

## References

- `academic-crud-topic-note` for `find_wikipedia.py` canonical title discovery
- `ingest-wikipedia` for the Wikipedia article ingestion workflow
- `academic-crud-course-index` for course structure and `## children` linkage
- `academic-lint` for validation
