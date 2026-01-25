---
name: special
description: Conventions for all Markdown content and tools under special/
applyTo: "special/**/*.md, special/**/*.py"
---

# Special Content Instructions

The `special/` directory contains specialized knowledge including coursework, tutorials, language texts, business frameworks, and other curated learning materials.

## Content Organization

### special/academia/

Academic coursework organized hierarchically:

```
special/academia/
├── <Institution>/           # e.g., HKUST, Korea University, Pusan National University
│   ├── index.md            # Course listings by semester/year
│   ├── reviews.md          # Institution-specific reviews
│   └── <Course Code>/      # e.g., COMP 2012, ACCT 2010
│       ├── index.md        # Course overview and materials
│       └── *.md            # Lecture notes, assignments
```

**Institution structure**:
- Each institution has its own directory (HKUST, Korea University, Pusan National University, USFQ, Yonsei University)
- `reviews.md` contains institution-specific reviews and notes
- Courses organized by code (e.g., `COMP 2012`, `ACCT 2010`)

**Course metadata** (in YAML frontmatter and index.md):
- Semester and year tags (e.g., `2023-fall`, `2024-spring`)
- Credits (e.g., `3 credits`)
- Status: `taken`, `not-taken`, `transferred`, `auditing`
- Prerequisites and corequisites
- Instructors and teaching assistants

**Index maintenance**:
- Keep `index.md` updated with course listings organized by semester/year
- List courses chronologically (most recent first)
- Include course code, title, credits, and status
- Academic converters in `tools/special/` help maintain these indexes

### Other special/ subdirectories

- **Language texts**: Foreign language learning materials, grammar guides
- **Business frameworks**: MBA frameworks, strategy models, case studies
- **Tutorials**: Technical guides, how-tos, walkthroughs
- **Lecture series**: Organized lecture notes from online courses or seminars

**Convention**: Each directory recursively has `index.md` with:
- Directory overview and purpose
- Listing of subdirectories and files
- Cross-references to related content in `general/` or other `special/` folders

## Markdown Conventions

Apply the same conventions as `general/` notes:

- **Frontmatter**: YAML with `aliases`, `tags`, `language/in/English`
- **Cloze markup**: Preserve `{@{ ... }@}`, `::@::`, and `:@:` exactly as-is
- **pytextgen fences**: Do not modify `# pytextgen generate ...` comments or `return export_seq(...)` signatures
- **Links**: Relative paths with `%20` encoding for spaces
- **Math**: KaTeX `$inline$` and `$$display$$` formats
- **Media**: Reference files in `archives/` with relative paths

## Special Differences from general/

1. **Sources**: Content may come from coursework, personal notes, tutorials, not just Wikipedia
2. **Structure**: May have deeper hierarchies (institution → semester → course → topic)
3. **Metadata**: Additional fields for academic context (semester, credits, instructors)
4. **Updates**: Modified manually or via academic converters, not via `convert wiki.py`

## Tools in tools/special/

**Academic converters** (LMS export processors):
- `convert Canvas submission.py`: Canvas LMS exports → YAML frontmatter
- `convert HKUST Zinc submission.py`: HKUST Zinc submissions → YAML
- `get HKUST undergraduate courses.py`: Fetch HKUST course catalog → CSV

**Usage**: See the `tools-special` agent skill for detailed workflows.

**Stability requirements**:
- Preserve CLI interfaces (argument names, expected formats)
- Keep YAML output schemas stable (field names, structure)
- Maintain CSV column names for course list exports

## Editing Guidelines

- **Coursework**: Preserve academic integrity; cite sources appropriately
- **Index updates**: Keep `index.md` files current when adding/removing courses or materials
- **Cross-references**: Link between related courses, prerequisites, or `general/` encyclopedia entries
- **Consistency**: Follow institution-specific conventions (e.g., HKUST course codes vs. Korea University codes)
