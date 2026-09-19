---
name: academic-crud-attachments
description: Manage attachments directories at any level (course root, questions/, submission-level). Attachments hold raw files (PDFs, images, data, scripts) referenced by Markdown notes.
---

# Academic CRUD: Attachments

`attachments/` directories hold raw files referenced by Markdown notes: PDFs, images, SVGs, CSVs, Python scripts, Java files, and other non-Markdown content. They can appear at any level of the course hierarchy: course root (cheatsheets, exam data, analysis scripts, diagrams, present in 18+ courses), submission level (prompt PDFs, data files, template code), questions level (question images, problem-set data), or any other directory that needs raw files beside its notes.

## Key rules

- `attachments/` has no `index.md` (validator rule `index_children_missing_index`)
- Link from the parent `## children` as `[attachments/](attachments/)` or as individual file links
- Contents are raw files, not Markdown notes
- Images are attachments only when the picture itself is the material; page renders from `.extracted/pages/` never are (see "Page image handling" in `academic-ingest`)
- Encode spaces as `%20` in links
- `\[missing\]` rarely applies here: files exist or they don't (see [special.instructions.md](../../instructions/special.instructions.md#missing-data))

## Document-like formats (PDF, DOCX, PPTX)

Documents are not opaque blobs: extraction of text, page renders, and embedded images always runs on ingest, with outputs persisted in `.extracted/` beside the source. Disposition depends on the document's role (see "Document format handling" in `academic-ingest`):

- __Content document__ (the document IS the course material): the `.md` file is canonical, and the original is not stored in `attachments/` unless the user explicitly requests provenance. Extracted text becomes the `.md`; images stay in `.extracted/images/`, except an embedded image copied into `attachments/` under a descriptive name when the picture itself is the material; page renders are never attachments.
- __Attachment document__ (the document accompanies course material): the original is canonical and is stored in `attachments/` for provenance and re-extraction. Its extracted text is read during classification but not persisted; images stay in `.extracted/images/` and are copied into `attachments/` only when the note must show one.

When documents are ingested into `attachments/`, extraction outputs persist in a sibling `.extracted/` folder:

```text
attachments/
├── lecture.pdf                    # original file (attachment-role)
├── lecture.extracted/             # extraction cache
│   ├── text.md
│   ├── pages/
│   │   ├── page_001.png
│   │   └── ...
│   ├── images/
│   │   ├── page_007_img_1.png
│   │   └── ...
│   └── manifest.json
├── data.csv
└── ...
```

`.extracted/` is a derived artifact: not tracked in `index.md` `## children`, not linked from content files. The agent checks `manifest.json` (source hash) before re-extracting, and a `.gitignore` inside `.extracted/` containing `*` keeps cached contents out of commits. Create that `.gitignore` whenever you create `.extracted/`.

## Linking

- Directory link: `- [attachments/](attachments/)`
- Individual file: `- [\`filename.pdf\`](attachments/filename.pdf)`
- Images: individual links to the graphics actually kept, e.g. `- [\`lob_depth_diagram.png\`](attachments/lob_depth_diagram.png)`

## Creating or updating attachments

### Add files to an existing `attachments/` directory

1. Place the file in the directory.
2. Add a child link in the parent `index.md` if not already present.

### Create a new `attachments/` directory

1. Create the directory and place the files inside it.
2. Add a child link in the parent `index.md` `## children` section.

When the directory becomes empty (every file removed, or replaced by text transcribed into the notes), delete it and its child link. An `attachments/` directory that only duplicates prose is worse than none.

## Examples

Course-root attachments (ELEC 4110):

```markdown
## children

- [\`final examination cheatsheet.pdf\`](attachments/final%20examination%20cheatsheet.pdf)
- [transcludes/](transcludes/)
```

Questions-level attachments (COMP 2711H):

```markdown
## children

- [attachments/](attachments/)
- [midterm 1 practice problem set.md](midterm%201%20practice%20problem%20set.md)
```

## Validation

Run `academic-lint` after every edit. Pass the changed files when known; otherwise lint the whole course folder.

## References

- `academic-crud-course-index` for course-root attachments in `## children`
- `academic-crud-submission` for submission-level attachments
- `academic-crud-question` for questions-level attachments
- `academic-lint` for validation (rule `index_children_missing_index` forbids `index.md` in `attachments/`)
