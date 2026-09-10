---
name: academic-crud-transcludes
description: Manage transcludes/ directories containing Wikipedia articles included by reference with cloze markup.
---

# Academic CRUD: Transcludes

Manage `transcludes/` directories containing Wikipedia articles included by reference. These are full Wikipedia articles stored as Markdown files with cloze markup, used as reference material for courses.

## Target

`special/academia/<INSTITUTION>/<COURSE>/transcludes/<article>.md`

## When to use

Use `transcludes/` when a course references Wikipedia articles that should be available as study material with flashcards. The articles are Wikipedia content, not authored topic notes.

## Key rules

- Articles are Wikipedia content, not original topic notes
- Stored as `.md` files with full frontmatter and cloze markup
- Use `find_wikipedia.py` from `academic-crud-topic-note` for canonical title discovery
- Flashcard tag path includes `transcludes/` segment (e.g., `flashcard/active/special/academia/HKUST/ELEC 4110/transcludes/Fourier transform`)
- Linked from course `## children` as topic notes
- Use `\[missing\]` for absent fields. See [special.instructions.md](../../instructions/special.instructions.md#missing-data)

## Creating a transclude

1. Use `find_wikipedia.py` to discover the canonical Wikipedia title:

   ```bash
   uv run .agents/skills/academic-crud-topic-note/find_wikipedia.py --limit 5
   ```

2. Ingest the Wikipedia article using the `ingest-wikipedia` skill.
3. Place the resulting `.md` file in the `transcludes/` directory.
4. Add cloze markup (`{@{ }@}`) for key concepts.
5. Add a child link in the course `index.md` `## children` section.

## Updating a transclude

1. Edit the `.md` file directly.
2. Preserve the Wikipedia source structure and cloze markup.
3. Run `academic-lint` after editing.

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

Run `academic-lint` after every edit. If you know which files changed, pass those files specifically. Otherwise lint the whole course folder.

## References

- `academic-crud-topic-note` — `find_wikipedia.py` for canonical title discovery
- `ingest-wikipedia` — Wikipedia article ingestion workflow
- `academic-crud-course-index` — course structure and `## children` linkage
- `academic-lint` — validation
