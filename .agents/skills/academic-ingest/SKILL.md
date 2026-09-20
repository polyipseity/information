---
name: academic-ingest
description: Single entry point for all academic material ingestion. Accepts files, clipboard text, or pasted content; classifies the target destination in the repository and dispatches to the appropriate academic-crud-* skill.
---

# Academic Ingest

Accepts files (PDF, HTML, Markdown, images), clipboard text, or pasted content, then classifies the destination, resolves the course, and dispatches to the matching `academic-crud-*` skill. Classify __each material independently__: one invocation may produce several materials, each dispatched on its own.

## Scope guardrails

__Hard rule: create only what the source warrants.__ The decision tree fixes the target __type__; the source content fixes __how much__ to create. A generic course homepage is course-level metadata, so it produces only the course `index.md`, never lab directories, homework folders, session entries, or other scaffolding.

| Source type | Creates | Does NOT create |
| --- | --- | --- |
| Course homepage (generic HTML) | Course `index.md` only | Subdirectories, sessions, assignments |
| Canvas assignment page | Submission leaf (`index.md` + YAML) | Course-level sessions, other submissions |
| PRS/iClicker quiz HTML | In-class content file (`<type>.md`) | Course-level metadata, submission YAML |
| Canvas announcement | Blockquote in matching session | New sessions, new files |

__Lectures, labs, and tutorials are separate types__, each with its own section keys:

- `lecture`: `L1`, `L2`, `L3` (2-3 per week typical)
- `labs`: `LA1`, `LA2`, `LA3` (1 per week typical)
- `tutorials`: `T1`, `T2`, `T3` (1 per week typical)

Never conflate them into one type, create joint session entries, or mix types within a week heading. `## logistics` lists the enrolled sections, venues, and times; each session that meets gets its own `## week N <type>` heading, so a course with 2 lectures + 1 lab + 1 tutorial per week has 4 session headings, not 4 logistics entries. See "Session ordering" in `academic-crud-course-index`.

__A recurrent course groups its sessions by semester.__ It carries `- status: recurrent`, runs every term, and puts each session one level deeper under a `## <YYYY term>` header: `### 2026 fall week 3 tutorial`. Repeat the semester in the heading — without it the same week/type pair recurs every semester and `markdownlint` MD024 rejects the duplicate. Every session of a recurrent course is optional and is not assumed to be attended, so each carries `- status: optional` while keeping its `datetime:`, `venue:`, and `topic:`. A seminar series or training stream is recorded under whichever of `lecture`/`lab`/`tutorial` it matches, never as a new type. See "Recurring courses" in `academic-crud-course-index`.

__When in doubt, create less.__ Add scaffolding for future content only when the source enumerates items ("Lab 1, Lab 2, Lab 3") or the user asks for it. A homepage that mentions labs as a grading component does not warrant a `labs/` directory.

__Never write current status or provenance.__ What has been ingested, what remains, and how a derived value was established all go stale on the next ingest.

__Structure comes from the content, not the source.__ A source's layout never decides which notes or sections exist. Extracted text is raw material: its concepts set the file and section boundaries, and its headings are renamed to the sub-concepts they carry. A lecture deck must not produce a note about a lecture, and inside a section the paragraph order, list grouping, and card slicing follow the note's own logic. See the merge and split tests in `academic-crud-topic-note`.

__Write the content, not the material.__ A note states knowledge; it never narrates where the knowledge came from. Do not make the deck, slides, lecture, handout, or course the subject of a sentence, and do not report what a source does:

| Instead of | Write |
| --- | --- |
| The deck summarises the types of financial asset: bonds, stocks, ... | The types of financial asset are bonds, stocks, ... |
| The slide asks which exchange is more liquid. | Which exchange is more liquid? |
| The lecture's minibus example shows that ... | A minibus-arrival example shows that ... |
| The slides stress three characteristics. | Three characteristics matter. |
| The deck's chart counts 13 exchanges. | An earlier venue breakdown counts 13 exchanges. |

Write an open question as the question itself and a worked example as the example itself. Citations of real-world sources (an author, a paper, a data vendor) stay as they are; the teaching material they arrived in is not a source. Provenance belongs in the course `index.md` session entries, the one place the course may be named, because describing it is the index's subject.

## Source file preservation

__Hard rule: ingestion never deletes, moves, renames, or truncates a source file.__ The rule covers the file, wherever it lives: an ad-hoc ingest directory, a downloads folder, an attachments directory, a path on the command line, or a location outside the repository.

- Leave every source byte-identical at its original path.
- Do not delete a source because its content was "not stored in the repository". "Not stored" means not copied into the tracked content tree (`special/academia/...`); it never authorises deleting the original.
- Do not move, rename, or truncate a source to tidy up, deduplicate, or mark it processed.
- `.extracted/` outputs are additions beside a source, never replacements. Never remove a source to "clean up" after extraction.
- Disposing of sources is the user's decision. If cleanup looks desirable, ask.

## Convention authority

Every ingestion convention lives in these skills and instructions. Do not infer a convention by inspecting another course's content; a sibling course may be wrong, stale, or atypical, and copying it propagates the error.

When a convention is missing or ambiguous, report it as a skill defect rather than imitating other content or inventing a format.

## Document extraction (mandatory)

__Hard rule: run this before classifying anything.__ A document is not "read" until it has been extracted with the repository extractor:

```bash
uv run -m scripts.special.convert_document <input> <output_dir>
```

`<output_dir>` is the `.extracted/` folder described below. Extraction happens __in place, next to the source__, whether or not the source lives inside the repository.

__Never substitute an ad-hoc extractor.__ `pdftotext`, a direct `pymupdf` call, `pdfplumber`, and similar tools return text only: no page images, no manifest, nothing to cache-check. Using one is a skill violation even when the text looks correct.

__Post-conditions__: do not proceed to classification until all hold.

- `text.md` exists and is nonempty
- `pages/` holds one image per page/slide
- `manifest.json` records the source SHA-256, format, page count, and timestamp
- The recorded page count matches the source document

__Full coverage__: account for every page. Page text goes into the note; a figure the prose depends on is transcribed into it, and attached only when the picture itself is the material. A note that drops pages is an incomplete extraction, not a summary. If a source has no extractable text (scanned images only), say so and work from its images.

Document-like formats (PDF, DOCX, PPTX) produce extraction outputs that are persisted near the source:

- __Single file input__: `<stem>.extracted/` sibling folder (e.g., `lecture.pdf` → `lecture.extracted/`)
- __Directory input__: `.extracted/` subfolder inside the directory (e.g., `materials/` → `materials/.extracted/`)

Each `.extracted/` folder contains:

- `text.md`: extracted markdown text
- `pages/`: page/slide PNG renders at 150 DPI, for reading layout and slide text
- `images/`: the document's own embedded images at their true resolution, named for the page or slide holding them
- `manifest.json`: source file hash, format, page count, embedded image count, timestamp

__Cache check__: before running `convert_document.py`, check if `.extracted/` exists with a valid `manifest.json` matching the source file's SHA-256 hash. If valid, reuse the cached extraction; use `--force` to re-extract.

`.extracted/` is a derived artifact: not tracked in `index.md` `## children`, not linked from content files, safe to delete and re-extract. This applies to `.extracted/` alone, never to the source document (see "Source file preservation").

### Page image handling

`.extracted/` holds two image sets, used for different things:

- `pages/page_NNN.png`: a 150 DPI render of the whole page or slide, for locating content and reading slide text and layout.
- `images/`: the document's embedded images at true resolution, named for their page or slide. Read a figure here; the render is downscaled, so small labels and lettering that are unreadable in `pages/` are often clear.

__Look at every page and figure the material carries.__ When the model accepts images, open the page renders and the embedded images before classifying the material and before writing any prose about them; the `academic-vision` skill fixes the method, the legibility rules, and the checklist an image must pass. A figure described without having been looked at is a fabrication, not a summary.

__Read the embedded image, not the render, when the figure matters.__ A page whose extracted text is thin or empty usually still holds content. Open its embedded image, and crop and upscale if detail is unclear:

```bash
magick images/page_035_img_1.png -crop 200x70+320+235 +repage -resize 500% /tmp/zoom.png
```

Classify what the image holds, because each kind is handled differently:

- __Definitional drawing__ (a symbol, a schematic convention, a reference direction, a construction the material states by showing how it is drawn): the drawing is the definition, so attach it — see "Definitional drawings" below. No prose transcription replaces it.
- __Text-bearing figure__ (plot, table, document screenshot, annotated diagram that defines nothing): transcribe its labels, values, and steps into the note as prose or a Markdown table. The transcription is the record.
- __Purely pictorial image__ (photograph, engraving, illustration): describe it for the point it makes, per the rule below.

__Describe for learning, not for its own sake.__ Work out what the image does in its slide or section (a before/after pair showing a change in market structure, a diagram of a mechanism's steps, a chart supporting a claim) and write the description that carries that point. Include the detail that serves it and leave the rest out; do not inventory the picture. A photograph illustrating "trading floors then and now" needs the crowd, the medium, and the contrast, not every object in frame.

__Never assert what the image does not show.__ An image is evidence of what it depicts, not of context or intent:

- Do not name a venue, institution, person, or document that neither the slide nor the image names.
- Do not claim that two images show the same place, or that an image shows a particular company or exchange, because that reading is plausible.
- Do not read a signboard, heading, or caption that is illegible at the available resolution. Record that it is illegible.
- Do not read a chart's shape as a quantity it never states. The mode of a distribution is not its mean, and a line's movement is not a price change the slide never claims.
- Keep observation apart from the deck's commentary. "Men with arms raised and papers in hand" is observed; "bidding by open outcry" is the deck's framing of a trading floor, and one sentence must not present the second as if the image showed it.

__Attach a graphic only when the picture itself is the material.__ Page renders are never attachments, and an embedded image normally stays in `.extracted/` because text can carry what it shows. Copy one into `attachments/` under a descriptive name only when the reader must see the picture itself (geometry that carries the meaning, a chart whose shape is the point, a cheatsheet); expect that to be rare. A definitional drawing is the standing exception, and it is redrawn rather than copied — see below.

#### Definitional drawings

A drawing is part of a definition when the note cannot state the thing without showing it: a circuit symbol, a reference direction drawn on an element, a measurement setup, a construction. Such a drawing belongs beside the prose that defines it, and the prose alone never replaces it.

- Redraw it as an SVG in the owning directory's `attachments/`, produced by a generator script kept beside the drawings (`generate_circuit_diagrams.py`), so the set stays reproducible and editable; see `academic-crud-attachments`.
- Name it for what it draws (`symbol_<thing>.svg`, `<thing>_<convention>.svg`), never for the slide or page it came from. A form that differs is its own file, and the Markdown places the set side by side.
- Hand placement to the library: chain the elements, attach labels to the element they belong to, hang leads on named anchors, and pass no coordinate or nudge. See `academic-crud-attachments` for the full rule, and `academic-vision` for the render-and-compare check the drawing must pass.
- Embed it inline where the prose defines the thing, joined to the sentence by `<p>`: `text. <p> ![plain-language alt text](attachments/<name>.svg)`. Write the alt text in plain words, with no LaTeX.
- Card it in both directions: recognition with the drawing on the prompt side, recall with the drawing on the answer side, and both sides for a transformation — see `create-flashcards`.
- A picture specific to one question or worked example is not a definition: keep it as a crop of the extracted image in `attachments/`.

## Input handling

Accept any combination of:

- File paths (PDF, HTML, Markdown, images)
- Clipboard content (`--clipboard` or pasted text)
- Inline text from the user
- Multiple files in one invocation

Preprocess each input:

1. Read file content:
   - HTML: parse and extract readable text (see "Source identification")
   - Markdown: passthrough
   - Images: pass to the vision model if the model accepts images
   - Documents (PDF, DOCX, PPTX): extract per "Document extraction (mandatory)", then classify the role per "Document format handling"
2. Extract metadata (Canvas URLs, dates, course codes)
3. Normalize (strip HTML styling, extract plain text from PDFs)

### Source identification

Identify the HTML source type before extraction:

- __Canvas HTML__: URL contains `canvas.ust.hk`; has assignment metadata (title, due date, points, grade). Extract via `convert_canvas_submission`.
- __Canvas announcement__: URL contains `canvas.ust.hk` and the page type is "Topic". Has a title and body but no grade or submission metadata. Extract the title and body verbatim, dropping the platform chrome ("This topic is closed for comments") and redacting an instructor or TA name the body itself contains as `\[redacted\]`; see "Announcement preservation" in `academic-crud-course-index`.
- __PRS/iClicker HTML__: URL contains `prsmob.ust.hk/ars/`; has question text and numbered answer choices. Extract the quiz content directly; do not run `convert_canvas_submission`.
- __Generic HTML__: neither pattern. Extract readable text.

### Document format handling (PDF, DOCX, PPTX)

Document-like formats are not opaque: extraction is mandatory and runs before classification (see "Document extraction (mandatory)" for the command, cache check, and post-conditions). After extraction, classify the document:

1. __Vision-awareness check__: determine whether the current model accepts image inputs by checking the `PI_MODEL` and `PI_PROVIDER` environment variables. A vision-aware agent reads the page renders and embedded images alongside the text during classification and content extraction; otherwise it relies on the extracted text alone. Both image sets persist in `.extracted/` for later review either way.

2. __Role classification__ (after extraction, before dispatch):
   - __Content document__: the document IS the course material (lecture slides, topic notes, exam paper). Extracted text becomes the `.md` file; figures are transcribed into it, with an embedded image attached only when the picture itself is the material (see "Page image handling"); the original is left in place at its original path and the `.md` is canonical.
   - __Attachment document__: the document accompanies course material (prompt PDF, reference data, supplementary reading). The original is copied to `attachments/`; its extracted text is used during processing but not persisted as a separate `.md`; images stay in `.extracted/` unless the note has to show one.
   - __When ambiguous__: ask the user whether the document is the course content or a file that accompanies it.

3. __Ensure `.gitignore`__: when creating an `.extracted/` folder, create a `.gitignore` inside it containing `*`, so cached contents are never committed.

## Directory ingestion

When the input is a directory (or a glob resolving to directories), follow `.agents/prompts/academic-ingest-batch.prompt.md` instead of processing files one at a time. That prompt is the single source of truth for the batch steps and for the detection report; do not restate them here.

## Course resolution

1. __Extract from input:__ Canvas URL (the course ID in the path resolves the course; never record platform links in the target notes), file path (under `special/academia/<INST>/<CRS>/`), frontmatter tags.
2. __Parse the directory name__ for structural hints:
    - Pattern: `<COURSE> - <type> <N> (<binding> <M>)`
    - Example: `ELEC 1100 - quiz 1 (tutorial 2)` → course=ELEC 1100, type=quiz, number=1, binding=tutorial, target=2
    - The binding field selects the directory: tutorial → `tutorials/<name>/`, lab → `labs/<name>/`, and so on.
    - The course field resolves the institution and course directory.
    - This parsing is a hint, not a certainty; confirm with the user when the pattern is ambiguous.
3. __If ambiguous:__ list matching courses (name, institution, note count, last modified) and prompt the user to pick one.
4. __If no match:__ ask the user for the institution and course code, or confirm creation of a new course.
5. __If the course is recurrent__ (`- status: recurrent` in its `index.md`), read "Recurring courses" in `academic-crud-course-index` before writing any session entry: sessions are grouped by semester, each session heading repeats the semester and sits one level deeper, and every lecture, lab, and tutorial is optional.

## Splitting mixed-type materials

When one input contains several content types (a PDF with lecture notes followed by a problem set), split it into separate materials before classification.

__Split__ when the sections would route to different CRUD skills (a concept explanation → `topic-note`, exercises → `question`). __Do not split__ when they route to the same skill (a question set with diagrams stays one material), and treat a document that is primarily one type with minor supporting material as a single material.

To split:

1. Identify content boundaries (section headings, visual breaks, thematic shifts).
2. Create one material per distinct type, each carrying the same source file path and course context but its own `rawContent` slice and `targetHint`.
3. Classify each material independently through the decision tree below.
4. Dispatch each to its skill sequentially.
5. Coordinate shared indexes (create `assignments/index.md` before adding to it).

After splitting, report what was detected:

```text
Detected mixed content in <filename>. Splitting into 2 materials:
  1. Lecture notes → <topic>.md
  2. Problem set → questions/<name>.md
```

The user can intervene if the split is wrong ("Actually, treat the exercises as part of the lecture notes" → reclassify as one material).

## Classification decision tree

Classify by __target destination__ in the repository, not by input type. Apply the tree to each material independently, after any splitting.

```text
Material
│
├─ User specifies target type?
│  ├─ Yes → use it directly
│  └─ No → auto-classify ↓
│
├─ Course-level metadata?
│  (syllabus, schedule, grading policy, course logistics,
│   exam scores, grade distributions, exam statistics/reports)
│  ├─ Yes → academic-crud-course-index (top-level index.md)
│
├─ Canvas announcement? (discussion/topic page with title and body,
│  no grade/submission metadata)
│  ├─ Yes → academic-crud-course-index: place verbatim in the
│  │  matching session entry's free text area as a blockquote
│  │  (see "Announcement preservation" in academic-crud-course-index)
│
├─ Concept, theorem, or lecture topic? (standalone knowledge, not submission-bound)
│  ├─ Yes → academic-crud-topic-note (<topic>.md)
│
├─ Submission? (has attachments, due date, submission requirement)
│  ├─ Yes → which submission-bound directory?
│  │  ├─ Lab → academic-crud-submission (labs/<name>/)
│  │  ├─ Tutorial → academic-crud-submission (tutorials/<name>/)
│  │  ├─ Lecture-bound → academic-crud-submission (lectures/<name>/)
│  │  │    (Lecture slides submitted as an assignment are uncommon;
│  │  │     this branch typically handles lecture recordings,
│  │  │     worksheets, or graded lecture activities.)
│  │  ├─ Unbound (PS, HW, project) → academic-crud-submission (assignments/<name>/)
│  │  └─ Ambiguous → prompt user to pick directory
│  │
│  │  In-class component: If the Canvas page is for live session work
│  │  (in-class lab, tutorial, or lecture) for an existing submission,
│  │  route to academic-crud-submission and treat as an in-class addition
│  │  (creating lab.yml/tutorial.yml/lecture.yml and lab.md/tutorial.md/lecture.md).
│  │  Also apply when the source is PRS/iClicker HTML (quiz questions only,
│  │  no Canvas assignment page) — treat as in-class content for the matching
│  │  tutorial. PRS HTML contains quiz questions, not Canvas metadata — extract
│  │  question text and answer choices, do not run convert_canvas_submission.
│
├─ Question set? (problems, exercises, iPRs, no submission)
│  ├─ Yes → academic-crud-question (questions/<name>.md)
│
├─ Course-level agent guidance?
│  ├─ Yes → academic-crud-agents (AGENTS.md)
│
├─ Sub-directory index? (listing page for assignments/, questions/, etc.)
│  ├─ Yes → academic-crud-index (<dir>/index.md)
│
├─ Wikipedia articles for reference? (transcludes/ directory)
│  ├─ Yes → academic-crud-transcludes (transcludes/<article>.md)
│
└─ Unclear → two-phase ambiguity resolution (see below)
```

### Ambiguity resolution

When the classifier cannot determine the target with confidence, narrow it in two phases.

__Phase 1: category.__ Group the candidates into knowledge material (lecture notes, course logistics), assessment material (problem set, lab, assignment), and support material (reference article, attachment). If one category dominates (score ≥ 2× the next), go straight to Phase 2 within it; otherwise present the categories:

```text
I'm not sure how to classify this material. It looks like it could be:
1. Knowledge material (lecture notes, course logistics)
2. Assessment material (problem set, lab, assignment)
3. Support material (reference article, attachment)

Which category? [1/2/3]
```

__Phase 2: target.__ Present the target types within the chosen category:

```text
Within knowledge material, this could be:
1. Topic note — standalone concept or theorem explanation
2. Course index — syllabus, schedule, or grading info

Which destination? [1/2]
```

Show at most __3 candidates__ per phase, each with a one-line reason. If the user says "none of these", fall back to free-text input for the target type.

## Post-classification steps

Apply these steps to each material after its target type is known, before dispatch.

### Topic note naming (mandatory when the target is a topic note)

Fix the name before creating or renaming any `<topic>.md`. This is required, not stylistic; see "Topic note naming" in `academic-crud-topic-note` for the full rules.

```bash
uv run python .agents/skills/academic-crud-topic-note/find_wikipedia.py "<concept>"
```

The filename stem and the H1 title are the same sentence-case string (`operating system`, never `Operating System`). No lint rule inspects the H1 title or the filename, so a title-case name passes validation silently.

### Missing data

__Hard rule: always use `\[missing\]`.__ When a field is present but its value is unknown or unavailable, write `\[missing\]`. This is the only acceptable placeholder. Never use bare `none`, `N/A`, `TBD`, `?`, or an empty string; never use `\(none\)` outside exam statistics; never invent a value such as "TBA" or "upcoming".

The escape keeps `\[missing\]` from creating a wiki link in Obsidian. The brackets mean "field exists, value absent", as distinct from omitting the field entirely ("field not applicable").

See [special.instructions.md](../../instructions/special.instructions.md#missing-data) for the full convention.

### 1. Existing-match check

Fuzzy-match the input against existing notes of the __same target type__ within the resolved course:

- Course-index metadata → existing `index.md` sections
- Topic notes → existing `<topic>.md` files
- Submissions → existing submissions in the matched directory
- Questions → existing question pages

If a match is found, show the existing note and ask whether to __update__ it, __create new__ anyway, or __cancel__. All types support partial information, so a note can start minimal and be filled in later. An existing match never overrides type classification: a problem set that shares words with a topic note is still a question set.

### Multi-source merging

When several input files classify to the same target directory, merge them instead of creating duplicate entries.

1. Identify the shared target by matching directory name patterns (e.g., "quiz 1 (tutorial 2)" and "Quiz 01 (in Tutorial 02)" both target `tutorials/tutorial 2/`).
2. Determine which source provides what:
    - PRS/iClicker HTML → quiz content (questions, choices)
    - Canvas HTML → metadata (grade, assignment ID, submission record)
    - PDF/image attachments → supplementary files in `attachments/`
3. Create the target directory once, then apply each source's contribution:
    - Content from PRS HTML → `<type>.md` (quiz questions)
    - Metadata from Canvas HTML → `<type>.yml` (via `convert_canvas_submission`)
4. Report the merge:

```text
Merged 2 sources into tutorials/tutorial 2/:
  - PRS HTML → <type>.md (2 quiz questions)
  - Canvas HTML → <type>.yml (grade: 2/2)
```

### Schedule cross-referencing

For a submission (lab, tutorial, lecture), look up the matching session in the course `index.md` for reference. Do not copy schedule metadata into `<type>.yml` or `<type>.md` unless the source explicitly provides it; schedule info belongs in the course `index.md`.

### Source file disposition

After extraction, the material lands as follows. Nothing here authorises deleting or moving the source (see "Source file preservation").

- Quiz questions → `tutorial.md` / `lab.md` / `lecture.md`
- Grade metadata → `tutorial.yml` / `lab.yml` / `lecture.yml`
- Canvas submission metadata → `submission.yml`
- Canvas announcement body → course `index.md` session entry (blockquote)
- Prompt PDFs, data files, images → `attachments/` (only actual media/data)
- Original HTML files → left at their original path; not copied into the repository
- Original document files (PDF, DOCX, PPTX): content documents are left in place with the `.md` as the canonical copy; attachment documents are copied into `attachments/` and the source is left in place
- Figures → transcribed into the note; a definitional drawing is attached as a redrawn SVG (see "Definitional drawings"), and an embedded image is copied to `attachments/` under a descriptive name only when the picture itself is the material
- Extracted text → the `.md` file for content documents; ephemeral reference for attachment documents (the original is canonical)
- `.extracted/` folders → derived cache artifacts, not tracked in `index.md`

Do not copy extracted-content HTML into `attachments/`. `attachments/` holds raw referenced files (PDFs, images, data, scripts), not source documents whose content has been transcribed into markdown.

### Embedded image extraction (HTML sources)

PRS/iClicker HTML can embed base64 images (circuit diagrams, pinouts, sensor illustrations) that quiz questions reference. Extract them:

1. Scan for `data:image/...;base64,...` URIs.
2. Skip tiny images (< 1 KB); they are UI icons.
3. Use the original filename when available; otherwise generate a descriptive one (`req_circuit.jpg`, `l293_pinout.jpg`).
4. Preserve the original alt text from the `<img>` tag. If it is missing or empty, look at the image and write a concise plain-language description of what it shows ("Resistor network with 6, 12, 3, and 2 ohm resistors"); never use LaTeX in alt text, and never describe an image you have not opened — see `academic-vision`.
5. Reference the image in the quiz markdown as `![<alt text>](attachments/<name>.jpg)` inside the blockquote question.
6. List it in the `## attachments` section of both `<type>.md` and `index.md` (an in-class-only `index.md` omits `## attachments`).

### Canvas announcement extraction

Extract the title and body verbatim, strip the timestamp and platform chrome, redact an instructor or TA name the body contains as `\[redacted\]`, then place them as a bolded blockquote in the matching session entry (see "Announcement preservation" in `academic-crud-course-index`). Match assignment-related announcements to the lecture entry that links the assignment, and activity-related ones to the lab or tutorial entry. Announcement pages carry no grade or submission metadata, so never run `convert_canvas_submission` on them.

### In-class component detection

When the input is Canvas HTML for a lab, tutorial, or lecture that already has a `submission.yml`, ask the user whether the page is the out-of-class or in-class one. The in-class page produces `lab.yml`/`tutorial.yml`/`lecture.yml` (not `submission.yml`) and a `lab.md`/`tutorial.md`/`lecture.md` content file as a child of `index.md`. That file is Canvas-sourced, so it mirrors the Canvas header block of the submission `index.md`: frontmatter, `# <type>` heading, identity bullets, the Canvas metadata bullets drawn from the component YAML, and the verbatim Canvas description. See `academic-crud-submission` for the exact format.

### 2. Attachment handling

If the material includes raw files (PDFs, images, data files, scripts) supplementary to the classified content type, use `academic-crud-attachments` to set up the attachments directory. The material is still classified by its content type; attachments are storage metadata, not a content type.

Attachment directory placement follows the target:

- Topic note → `attachments/` inside the topic's directory
- Submission → `attachments/` inside the submission directory
- Question → `attachments/` inside the question's directory
- Course-level → `attachments/` at the course root

Skip this step when no raw files accompany the material.

A definitional drawing is an attachment even without a source file: redraw it as an SVG beside a generator script in the target's `attachments/` and embed it in the note that defines the thing (see "Definitional drawings" and `academic-crud-attachments`).

## Non-Canvas content templates

When in-class content is not Canvas-sourced, use these templates instead of the Canvas header block format.

### PRS/iClicker quiz (`<type>.md`)

Use the blockquote question format, matching existing question files. Applies to labs, tutorials, and lectures with in-class PRS/iClicker quizzes.

```markdown
---
aliases:
  - <INSTITUTION> <COURSE> <type> <N> <type>
  - <INSTITUTION> <COURSE> <type> <N> quiz content
tags:
  - flashcard/active/special/academia/<INST>/<CRS>/<type>s/<type>_<N>/<type>
  - language/in/English
---

# <type>

- <INSTITUTION> <COURSE> <type> <N>
- parent: [<type> <N>](index.md)

---

- title: <Canvas assignment title from Canvas HTML>
- points: <N> from Canvas HTML
- grade: <entered>/<possible> from Canvas grade record
- submitting: <submission type> from Canvas HTML

---

<Canvas description from Canvas HTML>

## attachments

- [`<filename>.ext`](attachments/<filename>.ext)

## quiz

> <question text>
>
> ![<alt text>](attachments/<diagram>.jpg)
>
> 1. <choice>
> 2. <choice>
> 3. <choice>
> 4. <choice>
>
> - solution: <correct answer>
> - explanation: <why this is correct>

<!-- markdownlint MD028 -->

> <next question>
```

Use `![](attachments/<name>.jpg)` inside the blockquote when the question references a diagram, and list the image in `## attachments` in both the content file and `index.md`.

One line per MC option. `solution` is required; `explanation` is optional, so remove the `- explanation:` line entirely when omitted.

### Cloze flashcards in question blocks

Every question quote block needs cloze flashcards (`{@{ }@}`) on its `- solution:` and `- explanation:` lines. Do not cloze the question text or the answer choices.

__Solution lines:__ one cloze per solution, on the core result, formula, or decisive step. Very long solutions (multi-step derivations, lengthy prose) may carry several clozes, one per logical step.

__Explanation lines:__ prefer several clozes, breaking the explanation into individual claims, conditions, and reasoning steps.

__Cloze syntax:__

- Closing delimiter is `}@}` (3 chars: `}` `@` `}`)
- LaTeX: `{@{content $LaTeX math$}@}`, where the trailing `$` closes the math before `}@}` closes the cloze
- Plain text: `{@{content plain text}@}`, closing with `}@}`
- For multiple questions, delegate cloze creation to a subagent using the `create-flashcards` skill

Separate consecutive blockquote questions with `<!-- markdownlint MD028 -->`. Strip PRS UI chrome (navigation, error messages, "Pull down to refresh", "Your response is submitted") and keep only the question text and answer choices. Preserve LaTeX math notation.

## Topic-note reconciliation (mandatory)

Every ingestion is compared against the course's existing topic notes, whatever the material is: a lecture deck, a lab manual, a tutorial handout, a problem set, a Canvas page, or a single figure. Session files (`lab.md`, `tutorial.md`, `lecture.md`, quiz pages, `questions/`) hold the material as it arrived; the course's durable concepts belong to the topic notes. Material whose concepts reach only a session file is an unfinished ingestion. The drawings count as concepts: when the material defines a symbol or a convention by drawing it, the owning note carries the drawing itself (see "Definitional drawings").

Run this after the dispatched CRUD skill has written its files and before the humanizer pass:

1. __List the concepts.__ Take every concept the material carries, including ones that look already covered.
2. __Find the owning note and section.__ Match by canonical title and by section meaning, never by wording; a course note may cover the concept under a different name.
3. __Apply exactly one outcome per concept, and record it:__
    - __extend__: the material adds a fact, distinction, example, drawing, or card the note lacks — write it into the owning section in the note's own words;
    - __prune__: the material contradicts, supersedes, or duplicates what the note says — remove or correct the stale part within the note's scope;
    - __create__: no note owns the concept and it is durable knowledge independent of the session — create a topic note per `academic-crud-topic-note` and link it from the course `index.md`;
    - __leave__: the note already covers the concept — name the section that covers it.
4. __Report the outcomes__, one line per note, the `leave` decisions included.

The session file and the topic note do different jobs: the session file keeps the material's own questions and framing, while the topic note states the concept. Reconciliation is never finished by copying the material's wording into a note, and never skipped because the material is only a lab, a tutorial, or a single handout.

## Dispatch

Route to the correct `academic-crud-*` skill with preprocessed context:

```json
{
  rawContent: <extracted text>,
  metadata: <Canvas metadata, dates, course codes>,
  sourceType: <pdf|html|markdown|text|image|document>,
  filePath: <original file path>,
  targetHint: <classification result>,
  documentRole: <content|attachment>,
  pageImages: <list of page-render paths, if available>,
  embeddedImages: <list of embedded image paths, if available>,
  extractionDir: <path to .extracted/ folder>
}
```

## Post-dispatch

After the dispatched skill completes:

1. __Reconcile the topic notes.__ Run "Topic-note reconciliation (mandatory)" above for every material in this ingestion, whatever its source.
2. __Section levelling pass.__ Re-review every note this ingestion wrote or touched, section by section, and re-level it: promote a sub-concept that earned its own heading, fold a section that restates the note's H1 or a lone `###` that is its parent's whole content, move material to the note that owns its concept, and re-link every session entry whose anchor a renamed, moved, or removed heading invalidated. Run it before the humanizer pass, which treats heading text as frozen; see "Section levelling pass" in `academic-crud-topic-note`.
3. __Humanizer pass.__ Load the `humanizer` skill and apply it to the new and changed prose and flashcards, the reconciled topic notes included, before validating. Every later edit gets the same pass, whether or not an ingestion is running; see "Humanizer pass" below.
4. Run validation on the created or modified files.
5. Add a link to the assignment in the last lecture entry on or before its due date in the course `index.md`.
6. Report what was created or updated, with file paths, and give the reconciliation outcome for each topic note.
7. Suggest next steps (add flashcards, update the index).

> __Legacy patterns:__ For deprecated content structures (flat `questions.md`, flat assignment directories, `transcripts/`), consult the `academic-deprecated` skill for migration guidance. Deprecated pattern detection is not part of ingestion classification; it is a separate maintenance concern.

### Humanizer pass

__Every edit to academic prose or flashcards triggers the pass, not only an ingestion.__ A note created from a deck, a reconciliation, a card rewritten on request, a heading renamed, a one-line correction: whatever changed the prose or the cards gets the pass over the text that changed, run after the edit and before `academic-lint`. Run it as you edit, or batch it at the end of the run when several edits accumulate — the timing is a choice, skipping it is not. Work that reaches the user with unpassed prose or cards is unfinished.

Every note this skill dispatches to gets the pass over __both the prose and the flashcards__. Prose and cards fail differently, so sweep them separately.

__Verbatim text is out of scope.__ Anything reproduced exactly as it arrived — a question statement from an official paper, the body of a Wikipedia transclude, an instructor's own phrasing — stays as it is, and so does heading text that session entries link to. The pass covers the prose and the cards you write.

__"Humanize", "humanizer pass", and "reduce verbosity" all mean one thing: load the `humanizer` skill and apply it.__ The skill is the authority on what changes; cutting verbosity is only the usual __focus__ of a pass, never a substitute for it. Do not run a pass from memory of these rules.

__Agents and subagents must load the skill.__ Read the `humanizer` skill's `SKILL.md` (user scope: `~/.agents/skills/humanizer/SKILL.md`) before editing. When the pass is delegated, the brief must name the `humanizer` skill, give that `SKILL.md` path, require the child to read it before editing, and require it to report the patterns it applied; pass `humanizer` in the subagent's skills as well. A rewrite reported without those patterns did not run the pass.

#### Flashcard focus

- __Prompts that give away the answer__ or that a reader cannot answer at all. Rewrite the pair rather than trimming either half.
- __Answers that restate their prompt__ or end in a justification clause ("…, which holds because the copies are independent").
- __Missing symbols.__ If cutting the prompt drops the givens or notation the answer uses, the card is broken, not shorter. Calculation cards must name every quantity they combine.
- __Labels longer than the concept.__ A prompt is a question, not a sentence.
- __Two ideas in one card.__ Split it rather than trimming both halves.
- __Enumeration answers.__ A card whose answer lists many items names its slice on the prompt side (`the five born before 1790`, `before 1850`, `the curl equations`) and leaves the rest to sibling cards (see "Enumeration cards" in `create-flashcards`).

Keep the givens the answer needs. A card should read as a short prompt carrying its symbols plus an answer of one or two clauses.

#### Prose focus

- __Openers that announce the structure__ instead of starting the content ("Three objects have to be kept apart", "There are two ways to obtain it").
- __Clauses explaining why the previous clause is useful__ ("which is why…", "so that…", "which makes… possible").
- __Facts already carried__ by the section's cards or by an earlier paragraph.
- __Hedging, and appositives that restate their subject__ ("$X$, whose distribution is not fully specified" when the sentence already said so).
- __Subordinate chains__ that a full stop would divide.

Leave the source's own emphasis alone: an instructor's "rare, difficult or even impossible" is content, not padding. Aim for one idea per sentence and no sentence announcing what comes next.

#### Repo patterns to watch

Academic notes attract these patterns from the `humanizer` catalogue: rule-of-three lists padded to three items, "not only… but also", copula avoidance ("serves as" or "represents" where "is" works), em dashes, bolded `**Term:** description` bullets, and over-bolded inline labels.

The target is a triad __padded__ to three items, not an enumeration of three real things: a list of three device types is content and stays.

Three catalogue patterns never apply here: headings are already sentence case, notes carry no emoji, and __heading text is frozen__ — session entries link to `#section%20anchors`, so a heading is never a humanizer target. Renaming, moving, or folding a heading belongs to the __section levelling pass__, which runs first and re-links the session entries it invalidates (see "Section levelling pass" in `academic-crud-topic-note`). Accuracy beats style in every conflict: a card that loses a given to read more naturally is broken.

#### After the pass

1. __Recheck suppressions.__ Cutting a prompt can strand a `two_sided_calc_warning` suppression with nothing to suppress (`academic-lint` errors on it), and restoring a symbol can create a warning that now needs one.
2. __Report the card count.__ Merging duplicate cards is encouraged, but the count feeds the `Flashcards-now` commit trailer.
3. __Re-read the file once.__ Heading text (session entries link to `#section%20anchors`), flashcard markup (`{@{ }@}`, `::@::`, `:@:`), LaTeX, links, pytextgen fences, and anything quoted verbatim from the source must be untouched.

## Skills dispatched to

| Target | Skill |
| --- | --- |
| Top-level `index.md`, exams, logistics, grade stats | `academic-crud-course-index` |
| Sub-directory `index.md` | `academic-crud-index` |
| `<topic>.md` standalone notes | `academic-crud-topic-note` |
| Submission pages (labs, tutorials, lectures, assignments) | `academic-crud-submission` |
| Question pages (no submission) | `academic-crud-question` |
| `AGENTS.md` | `academic-crud-agents` |
| Wikipedia transcludes | `academic-crud-transcludes` |

Attachment setup uses `academic-crud-attachments` as a post-classification helper for any target that includes raw files.

Reading, judging, and verifying images uses `academic-vision` as a helper wherever the material carries pictures: page renders, embedded figures, attached crops, and the drawings the notes generate.

## References

- All `academic-crud-*` skills for dispatch targets
- `academic-crud-attachments` for attachment directory setup
- `academic-vision` for looking at, classifying, and verifying images, including the generated drawings
- `academic-deprecated` for legacy pattern migration
- `create-flashcards` for flashcard markup guidance
- `humanizer` for the AI-writing patterns the humanizer pass removes
- `academic-lint` for validation
