---
name: special
description: Conventions for all Markdown content and tools under special/
applyTo: "special/**/*.md, special/**/*.py"
---

# Special Content Instructions

The `special/` directory holds coursework, tutorials, language texts, business frameworks, technical documentation, command libraries, and other curated learning materials. Content comes from academic coursework, online courses, personal notes, reference documentation, and practical guides — not Wikipedia ingestion.

## Directory structure

```text
special/
├── academia/                       # Academic coursework by institution
│   ├── HKUST/                      # Hong Kong University of Science and Technology
│   ├── Korea University/           # Korea University courses
│   ├── Pusan National University/  # Pusan National University courses
│   ├── USFQ/                       # Universidad San Francisco de Quito
│   └── Yonsei University/          # Yonsei University courses
├── audio signal processing/        # Audio signal processing course materials
├── C/                              # C programming language reference
├── C++/                            # C++ language features
├── MySQL/                          # MySQL database reference
├── NumPy/                          # NumPy library documentation
├── language acquisition/           # Language learning (English, Chinese)
├── questions/                      # Timestamped Q&A entries
├── examples/                       # Worked examples and case studies
├── attachments/                    # Supporting files (images, PDFs, etc.)
├── nutritional information/        # Nutritional data and supplements
├── [Business frameworks].md        # MBA/strategy frameworks (individual files)
├── [Technical guides].md           # Usage guides for tools and software
├── [Command/regex libraries].md    # Reusable command and regex patterns
└── [Classical Chinese texts].md    # Traditional Chinese literary works
```

Content types include: academic coursework (`academia/`), online course materials, programming language references (`C/`, `C++/`, `MySQL/`, `NumPy/`), language acquisition materials, business/strategy frameworks, technical usage guides, command/regex libraries, classical Chinese texts, questions collections (`questions/`), worked examples (`examples/`), mathematical content, and miscellaneous specialized content.

When encountering a new content type, apply the conventions in this document (frontmatter structure, cloze markup, pytextgen patterns, links, formatting) and follow the most similar existing content type for domain-specific guidance.

## Markdown conventions

- __Frontmatter__: YAML with `aliases`, `tags`, `language/in/<lang>` (or `language/for/<lang>` for language texts)
- __Cloze & flashcard markup__: See [editing-conventions.instructions.md](../editing-conventions.instructions.md) for complete syntax rules
- __pytextgen fences__: Preserve `# pytextgen generate ...` comments and `return export_seq(...)` signatures; do not run `uv run -m init generate` yourself
- __Links__: Relative paths with `%20` encoding for spaces
- __Math__: KaTeX `$inline$` and `$$display$$` formats
- __Media__: Reference files in `archives/` with relative paths
- __Code blocks__: Use fenced code blocks with language tags

## Editing guidelines

Follow the conventions in [editing-conventions.instructions.md](../editing-conventions.instructions.md) and the [academic-ingest](../skills/academic-ingest/SKILL.md) skill. Preserve institution-specific formatting, semester notation, and status markers. Include source references in frontmatter where applicable. Keep `index.md` files current when adding or removing content.

### Academia-specific

- Preserve institution-specific course code formatting (e.g., HKUST uses `COMP 2012` in titles, both `COMP 2012` and `COMP2012` in aliases)
- Use consistent semester notation: `2023 fall`, `2024 spring`, `2023 winter`
- Keep course status markers up-to-date in institution `index.md` (`taken`, `not-taken`, `transferred`)
- Do not include personal student IDs, grades, or identifying information

### Classical Chinese texts

- Preserve original classical Chinese text exactly
- Use `notes.embed()` for inline annotations
- Include `by/<author>` tag in frontmatter
- Use both `language/for/中文` and `language/in/中文` tags

## Developer tooling & tests

- New tools that transform `special/` content require tests under `tests/` using `tmp_path: os.PathLike[str]` (annotate the fixture as `PathLike[str]`). Use `os.fspath(path_like)` when converting paths to strings.
- Async helpers must follow repo-wide AnyIO/Asyncer conventions (not `asyncio`)
- Content changes affecting pytextgen fences need round-trip tests that do not invoke `uv run -m init generate`
- Run `bun run check`, `bun run format`, and `bun run test` before submitting; include explicit file arguments (e.g., `bun run check:md --no-globs special/academia/...`)

## Tools in scripts/special/

Academic converters (LMS export processors): `convert_canvas_submission.py`, `convert_hkust_zinc_submission.py`, `get_hkust_undergraduate_courses.py`. See the `tools` skill for workflows and interfaces. Preserve CLI interfaces, YAML output schemas, and CSV column structures across updates.
