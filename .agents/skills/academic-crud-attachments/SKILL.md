---
name: academic-crud-attachments
description: Manage attachments directories at any level (course root, questions/, submission-level). Attachments hold raw files (PDFs, images, data, scripts) referenced by Markdown notes.
---

# Academic CRUD: Attachments

A course root, a submission, or a questions directory may each need raw files beside its notes, and the level they sit at decides the route. Most of them live at the course root: cheatsheets, exam data, analysis scripts, and diagrams, present in 18+ courses.

## Key rules

- `attachments/` has no `index.md` by default, and gains one when pyarchivist maintains it: the validator rule `index_children_missing_index` fires only on a `## children` link that points _at_ an `index.md` in a folder lacking one, so an `index.md` that exists is never itself an error
- Link from the parent `## children` as `[attachments/](attachments/)` or as individual file links
- Contents are raw files, not Markdown notes
- Images are attachments only when the picture itself is the material; page renders from `.extracted/pages/` never are (see "Page image handling" in `academic-ingest`)
- A definitional drawing is an attachment even when no source file carries it: redraw it as an SVG and embed it in the note (see "Definitional drawings" below)
- Encode spaces as `%20` in links
- `\[missing\]` rarely applies here: files exist or they don't (see [special.instructions.md](../../instructions/special.instructions.md#missing-data))

## Document-like formats (PDF, DOCX, PPTX)

Documents are not opaque blobs: extraction of text, page renders, and embedded images always runs on ingest, with outputs persisted in `.extracted/` beside the source. Disposition depends on the document's role (see "Document format handling" in `academic-ingest`):

- __Content document__ (the document IS the course material): the `.md` file is canonical, and the original is not stored in `attachments/` unless the user explicitly requests provenance. Extracted text becomes the `.md`; images stay in `.extracted/images/`, except an embedded image copied into `attachments/` under a descriptive name when the picture itself is the material. Page renders are never attachments.
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

### Definitional drawings

A drawing that defines a symbol, a convention, or a measurement setup is part of the definition, so the note has to show it. `academic-ingest` decides whether the material defines anything by drawing; this section is how one gets made.

#### Source the figure before making one

Search Wikimedia Commons first, and download with pyarchivist when a suitable freely-licensed image exists. A figure the world already has is better than one invented for the note: it carries a real author, a real licence, and a provenance record, none of which a generated drawing can.

```bash
uv run -m pyarchivist Wikimedia_Commons -d <attachments dir> -i <attachments dir>/index.md <inputs...>
```

pyarchivist writes the file, records the source URL, the timestamp, and the hash, and maintains the `index.md` entries. Keep those entries: they are what makes the download auditable. CC BY and CC BY-SA require attribution, so check whether the generated index records the author, and where it does not, carry the author and licence in the note's `## references`.

Use `-i` pointing at the course's own `attachments/index.md` when the figures belong to one course, and `-d` the same directory, so the course stays self-contained. The archives default of `archives/Wikimedia Commons/` applies to media a whole vault shares, not to a figure one course's note depends on.

Generating a figure is the fallback, not the default. Redraw only when the search comes up empty, and record the search that came up empty in the generator's module docstring so the next person does not repeat it. Never bend the note's prose to fit a substitute image: if the available figure omits something the note's card depends on, keep generating. A card that points at a detail the image does not show is worse than no image.

#### Generating the rest

The generated set comes from a single script kept in the same `attachments/` directory, named `generate_figures.py`. One file, not one per topic: the point is that the script is the only thing edited when a drawing changes. It writes its output beside itself, the SVGs and the script are both committed, and running it must be deterministic. Name each file for what it draws (`symbol_<thing>.svg`, `<thing>_<convention>.svg`), never for the slide, page, or lecture it came from, and keep one form per file (`symbol_source_battery.svg`, `symbol_source_circle.svg`) so the Markdown can place the set side by side: a drawing library cannot put a second figure into one image without coordinates.

Let the library place everything. Chain the elements in drawing order, attach each label to the element it belongs to, and hang leads on named anchors so its defaults decide every position. Pass no coordinate and no nudge, because one that exists to make the picture look right breaks as soon as anything moves. State only what carries meaning: direction, size, colour, order.

Then wire the figure into the note, and check it:

- Embed it inline in the note that defines the thing, joined to the sentence by `<p>`: `text. <p> ![plain-language alt text](attachments/<name>.svg)`. Write alt text in plain words with no LaTeX, and write it from the image in front of you, not from a description of it.
- Card it in both directions: recognition with the drawing on the prompt side, recall with the drawing on the answer side, and both sides for a transformation or comparison (see `create-flashcards`).
- Verify it before wiring it in, with the checklist in `academic-vision`: open the image itself — rasterise a generated SVG, and open a downloaded one as it landed — on every figure the change touches. Geometry that lands in the wrong place, a label that overflows its box, and two parts drawn on top of each other are invisible in the source and in the generator's own output. A downloaded file can also be an error page rather than an image, which no amount of reading the source reveals.
- Redraw the material's drawing. A page render is never an attachment, and a screenshot of a slide is not a drawing.

Two boundaries close this out. A picture that belongs to one question or worked example is not a definition, so it stays a crop of the extracted image under a descriptive name (`req_circuit.jpg`, `l293_pinout.jpg`). And each course's `attachments/` is self-contained: a symbol already drawn for another course is redrawn, never linked across courses.

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

Run `academic-lint` after every edit, passing changed files when known.

Alt text and any description of an attachment are prose: give them the humanizer pass before validating (see "Humanizer pass" in `academic-ingest`).

## References

- `academic-crud-course-index` for course-root attachments in `## children`
- `academic-crud-submission` for submission-level attachments
- `academic-crud-question` for questions-level attachments
- `academic-lint` for validation
- `academic-vision` for the visual checklist an image must pass
