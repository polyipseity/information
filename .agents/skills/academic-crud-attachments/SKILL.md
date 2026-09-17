---
name: academic-crud-attachments
description: Manage attachments directories at any level (course root, questions/, submission-level). Attachments hold raw files (PDFs, images, data, scripts) referenced by Markdown notes.
---

# Academic CRUD: Attachments

Manage `attachments/` directories at any level of the course hierarchy. Attachments hold raw files — PDFs, images, SVGs, CSVs, Python scripts, Java files, and other non-Markdown content — that are referenced by Markdown notes.

## Scope

Attachments can appear at multiple levels:

- __Course-root `attachments/`__: Cheatsheets, exam data, analysis scripts, diagrams (18+ courses)
- __Submission-level `attachments/`__: Prompt PDFs, data files, template code (labs, assignments)
- __Questions-level `attachments/`__: Images for questions, data files for problem sets
- __Any other directory level__ where raw files need to be stored alongside Markdown

## Key rules

- `attachments/` should NOT have `index.md` (per validator rule `index_children_missing_index`)
- Link from parent `## children` as `[attachments/](attachments/)` or as individual file links
- Contents are raw files (PDF, PNG, SVG, CSV, Python, Java, etc.), not Markdown notes
- Use `%20` encoding for spaces in filenames when linking
- Missing-data indicator `\[missing\]` rarely applies here — files either exist or don't. See [special.instructions.md](../../instructions/special.instructions.md#missing-data)

### Document-like formats (PDF, DOCX, PPTX)

Documents are NOT opaque blobs. Dual extraction (text + page images) always runs when a document is ingested, with outputs persisted in `.extracted/` near the source. Disposition depends on the document's role:

#### Content documents (the document IS the course material)

The `.md` file + page images are the canonical form. The original document is NOT stored in `attachments/` unless the user explicitly requests provenance.

- Extracted text → the `.md` content file itself
- Page images → `attachments/pages/` (referenced from the `.md` for visual content)
- `.extracted/` → persists as cache near the source; if source is not stored, `.extracted/` may also be omitted

#### Attachment documents (the document ACCOMPANIES course material)

The original file is the canonical form, stored in `attachments/`.

- Original file → `attachments/` (for provenance and re-extraction)
- Extracted text → ephemeral reference: agent reads it during classification, but the `.md` content comes from elsewhere
- Page images → `attachments/pages/` only when visual content needs inline reference; otherwise just cached in `.extracted/`
- `.extracted/` → persists as cache near the original in `attachments/`

#### `.extracted/` folder convention

When documents are ingested into `attachments/`, extraction outputs persist in a sibling `.extracted/` folder:

```text
attachments/
├── lecture.pdf                    # original file (attachment-role)
├── lecture.extracted/             # extraction cache
│   ├── text.md
│   ├── pages/
│   │   ├── page_001.png
│   │   └── ...
│   └── manifest.json
├── data.csv
└── ...
```

`.extracted/` is a derived artifact — not tracked in `index.md` `## children`, not linked from content files. The agent checks `manifest.json` (source hash) before re-extracting. A `.gitignore` inside `.extracted/` containing `*` prevents cached contents from being committed.

When creating `.extracted/`, create `.extracted/.gitignore` with content `*` to ignore all cached outputs.

#### Linking

Link from parent `index.md` as usual:

- Directory link: `- [attachments/](attachments/)`
- Individual file: `- [\`filename.pdf\`](attachments/filename.pdf)`
- Page images: `- [attachments/pages/](attachments/pages/)` or per-image links

## Creating or updating attachments

### Add files to an existing `attachments/` directory

1. Place the file in the `attachments/` directory.
2. Add a child link in the parent `index.md` if not already present:
   - Directory link: `- [attachments/](attachments/)`
   - Individual file link: `- [\`filename.pdf\`](attachments/filename.pdf)`

### Create a new `attachments/` directory

1. Create the `attachments/` directory.
2. Place files inside it.
3. Add a child link in the parent `index.md` `## children` section.

## Linking to attachments

Use relative paths with `%20` encoding for spaces:

```markdown
- [\`cheatsheet.pdf\`](attachments/cheatsheet.pdf)
- [attachments/](attachments/)
```

For course-root attachments linked from `index.md`:

```markdown
## children

- [assignments/](assignments/)
- [attachments/](attachments/)
```

## Examples

### Course-root attachments (ELEC 4110)

```markdown
## children

- [\`final examination cheatsheet.pdf\`](attachments/final%20examination%20cheatsheet.pdf)
- [transcludes/](transcludes/)
```

### Questions-level attachments (COMP 2711H)

```markdown
## children

- [attachments/](attachments/)
- [midterm 1 practice problem set.md](midterm%201%20practice%20problem%20set.md)
```

## Validation

Run `academic-lint` after every edit. If you know which files changed, pass those files specifically. Otherwise lint the whole course folder.

## References

- `academic-crud-course-index` — course-root attachments in `## children`
- `academic-crud-submission` — submission-level attachments
- `academic-crud-question` — questions-level attachments
- `academic-lint` — validation (rule `index_children_missing_index` forbids `index.md` in `attachments/`)
