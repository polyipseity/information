---
name: academic-crud-submission
description: Create, read, update, and delete submission-bound pages (labs, tutorials, lectures, assignments) with attachments, submissions, and solutions under special/academia/<INSTITUTION>/<COURSE>/. Handles partial information gracefully.
---

# Academic CRUD: Submission pages

`labs/`, `tutorials/`, `lectures/`, and `assignments/` share one folder hierarchy and one page format, so a single skill covers all four.

## Target

`<subdirectory>/<name>/index.md` + `attachments/` + `submission/` + `solution/`

`<name>` is the deliverable's own name, `lab 1` or `homework 2`, and it takes no week: a submission is not a session. A deliverable spanning several sessions keeps one directory, and every session entry that meets it links that same directory. Session content that is not a submission is named after its session heading, `week N <type> K` (see "Session types: lecture, lab, tutorial" in `academic-crud-course-index`).

The `##` sections inside `lab.md`/`tutorial.md`/`lecture.md` group the session's content by sub-concept, not by the source's headings; the file names themselves stay session-bound (see "Grouping: concepts, not source layout" in `academic-crud-topic-note`).

## Public and private split

A submission's artifacts write to the private tree whether its component is in-class or out-of-class, so an in-class lab's uploaded answer sheet is private exactly as an out-of-class one is. The pages and metadata that describe the work stay public. The lab's own handouts are not submission artifacts and travel with the lab in the public tree: a blank answer-sheet template, a manual, a data sheet, and the figures the notes generate. For a leaf at `special/academia/<INST>/<CRS>/assignments/<name>/`:

| File or directory | Tree |
| --- | --- |
| `attachments/`, `submission/`, `solution/` | `private/special/academia/<INST>/<CRS>/assignments/<name>/...` |
| `assignment.md` | private |
| `index.md`, `submission.yml`, `submission.pdf.yml` | public, in place |

A lab or tutorial splits the same way however many components it has: every artifact a component uploaded goes private, while `index.md`, the component YAML, and the `lab.md`/`tutorial.md`/`lecture.md` content stay public.

An assignment's authored content never goes into `index.md`. The index keeps the Canvas metadata block and the verbatim Canvas description; the assignment itself — the problems, the specification, the requirements — is written to `assignment.md` beside it and routes private. The index links it from `## children` as `- [assignment](assignment.md)`.

Every link keeps the ordinary colocated form — `[ass1.zip](attachments/ass1.zip)`, never a path through `private/` (see "Public and private trees" in `academic-ingest`). Delete removes the artifacts from the private tree along with the public leaf.

## Dual-component model

Labs, tutorials, and lectures can have two Canvas submission components:

- __Out-of-class__ (pre-lab, post-lab, take-home): work completed outside the session and submitted on Canvas, before, after, or both. Metadata: `submission.yml`.
- __In-class__ (lab, tutorial, lecture): work done live during the session and submitted on Canvas. Metadata: `lab.yml`/`tutorial.yml`/`lecture.yml`.

Assignments have a single component: `submission.yml`.

When the in-class component exists, the `index.md` links to `lab.md`/`tutorial.md`/`lecture.md` as children. The Canvas HTML for the in-class component is converted to the component-specific YAML via `convert_canvas_submission.py`.

| Submission type | Out-of-class YAML | In-class YAML | In-class content |
| --------------- | ----------------- | ------------- | ---------------- |
| Lab | `submission.yml` | `lab.yml` | `lab.md` |
| Tutorial | `submission.yml` | `tutorial.yml` | `tutorial.md` |
| Lecture | `submission.yml` | `lecture.yml` | `lecture.md` |
| Assignment | `submission.yml` | N/A | N/A |

### Component YAML format

`lab.yml`, `tutorial.yml`, and `lecture.yml` are produced by `convert_canvas_submission.py`, and their format is entirely defined by that script; do not invent custom schemas. Run the script to generate the YAML:

```bash
echo "/path/to/Canvas HTML.html" | uv run -m scripts.special.convert_canvas_submission 2> tutorial.yml
```

Redirect stderr to `tutorial.yml`/`lab.yml`/`lecture.yml` for in-class components and to `submission.yml` for out-of-class ones. When no Canvas page exists, such as an ungraded Personal Response System (PRS)-only session, do not create a component YAML file.

### In-class-only submissions

When a tutorial/lab/lecture has only an in-class component (no pre-lab, no take-home, no Canvas assignment outside the session):

- Create `tutorial.yml`/`lab.yml`/`lecture.yml` only; do not create `submission.yml`.
- `index.md` carries the Canvas metadata block and the verbatim Canvas description, then `## submission` and `## children`, with no `## attachments`.
- `## submission` lists the uploaded file first — `- file:` with the component YAML, then the artifacts it was produced from: a `source:` child for one, a `sources:` list for several — then `- in-class submission` with the same component YAML. The uploaded artifacts and their sources both sit in `submission/` of the private tree, so these links are the record of what was handed in.
- `tutorial.md`/`lab.md`/`lecture.md` carries no Canvas assignment metadata: identity bullets and parent, then the content.

```markdown
# index.md (in-class only)

---
aliases:
  - ...
tags:
  - ...
---

# index

- <INSTITUTION> <COURSE>

---

- title: <Canvas assignment title>
- due: <ISO 8601 with timezone>
- points: <N>
- grade: <entered>/<possible>
- submitting: <submission type>

---

<verbatim Canvas description>

## submission

- file: [`<uploaded>.<ext>`](submission/<uploaded>.<ext>)
    - metadata: [`<type>.yml`](<type>.yml)
    - sources:
        - [`<artifact>.<ext>`](submission/<artifact>.<ext>)
- in-class submission
    - metadata: [`<type>.yml`](<type>.yml)

## children

- [<type>](<type>.md)
```

```markdown
# <type>.md (in-class only)

---
aliases:
  - ...
tags:
  - ...
---

# <type>

- <INSTITUTION> <COURSE> <type> <N>
- parent: [<type> <N>](index.md)

## <authored content>
```

### Cloze flashcards in question blocks

Every question quote block needs cloze flashcards on its `- solution:` and `- explanation:` lines, never on the question text or the answer choices, and the solution line stays inside the blockquote holding its question. Those two lines are authored text, so every acronym, abbreviation, or personal name on them carries its full form on the same line (see "Full forms on every card" in `create-flashcards`); the quoted question itself is verbatim and exempt. The per-line split, the `}@}` delimiter, the LaTeX and plain-text forms, and the `<!-- markdownlint MD028 -->` separator between consecutive questions are in "Cloze flashcards in question blocks" in `academic-ingest`; the methodology is in `create-flashcards`.

### Flashcard style per section

Each section of a content file answers to two separate requirements. Question blocks whose `- solution:`/`- explanation:` lines carry clozes stand on their own: a section made up of nothing but those blocks needs no flashcard block. Anything else in the section, prose or a list or a table or an image, still needs its own `Flashcards for this section are as follows:` block. A prompt that is not a question is prose, so it takes cards rather than a `- solution:` line. The two styles and the `academic-lint` rules that enforce them are in "Flashcard style per section" in `academic-ingest`.

### No-submission case (no Canvas at all)

When a tutorial/lab/lecture has neither in-class nor out-of-class Canvas components (an ungraded practice session):

- Do not create `tutorial.yml`/`lab.yml`/`lecture.yml`.
- `index.md` contains only `## children`, with no `## submission`.
- `tutorial.md`/`lab.md`/`lecture.md` contains only the content, with no Canvas metadata block and no attachments section unless raw files are referenced.

Detect this when the source is PRS/iClicker HTML with only ungraded test questions, or the user confirms there are no Canvas pages for the session.

## Partial-info workflow

Submissions arrive in stages. Each stage fills in what is available without requiring everything upfront.

### Stage 1: Canvas HTML + attachments

Input: a Canvas assignment HTML page plus prompt files.

1. Create `<subdir>/<name>/` with `attachments/`, `submission/`, and `solution/`.
2. Extract Canvas metadata from the HTML: title, due date (ISO 8601 with timezone), points, submission type, description text (verbatim, keeping `<span style>` for color), update announcements (verbatim), and the assignment ID from the URL comment.
3. Create `index.md` with the metadata and description.
4. Copy prompt PDFs, DOCX, PPTX, and data files to `attachments/`. For an out-of-class component the directory is its private mirror (see "Public and private split").
5. For a PDF/DOCX/PPTX, check for an existing extraction under `.pi/ingest/` at the source's path minus `special/academia/<INSTITUTION>/`, with `.extracted` appended to the leaf stem, and when no valid cache exists, run:

   ```bash
   uv run -m scripts.special.convert_document attachments/<stem>.pdf \
     ".pi/ingest/<COURSE>/<component path>/attachments/<stem>.extracted/"
   ```

   Use the extracted text to understand the prompt during classification. The original in `attachments/` is canonical. Leave the images in that `.extracted/pages/` and `.extracted/images/`; reference an embedded image from a content file only when the picture itself is the material (see "Page image handling" in `academic-ingest`).
6. Apply the display-vs-link convention for versioned PDFs.

### What goes in `attachments/`

- Prompt PDFs and assignment sheets
- Data files (CSV, JSON, datasets)
- Code files (.ino, .py, .java) referenced by the submission
- Images (circuit diagrams, screenshots, pinout diagrams)
- Quiz images extracted from PRS/iClicker HTML
- Documents (PDF, DOCX, PPTX) that are prompt files, assignment sheets, or reference documents (attachment role)
- `<stem>.extracted/` caches for those documents live under `.pi/ingest/`, never in the tree (`text.md`, `pages/`, `images/`, `manifest.json`)
- For an out-of-class component the directory itself sits in the private tree; what goes in it does not change

When adding images:

- Preserve the original filename when available; for a bare base64 data URI, generate a descriptive name.
- Preserve the original alt text from the HTML `<img>` tag; when it is missing or empty, write a concise plain-language description. Never use LaTeX in alt text.

Do not put in `attachments/`:

- HTML source files (Canvas pages, PRS pages): these are extraction sources, not referenced raw files. Extract the content into `.md`/`.yml` and discard the HTML.
- Transcripted text: content that can be represented as markdown belongs in a `.md` file.
- Downloaded videos and subtitle files: a linked video is a source, read through `academic-video`; only the content derived from it reaches a note.

### Stage 2: Submission file(s)

Input: the artifact uploaded to Canvas (a document, rendered PDF, archive, source code, or link) plus, when it was generated from a local file, that local file.

1. Add files to `submission/`. For an out-of-class component the directory is its private mirror.
2. Update the `index.md` submission section: the uploaded artifact is the entry itself, and the local artifacts it was generated from become a `source:` child when there is one or a `sources:` list when there are several (see "Submission entry model").
3. For Apple Notes markdown:
   - Detect UUID attachment paths: `(Attachments|../attachments)/<UUID>.<ext>`
   - Rewrite paths to `../attachments/`
   - Add file-level suppression comments at the top
   - Copy referenced UUID-named images to `attachments/`
4. For regular markdown, copy as-is.

### Stage 3: submission.yml

Input: Canvas HTML for metadata extraction.

__Out-of-class component__ (default):

```bash
uv run -m scripts.special.convert_canvas_submission <<< "/path/to/Canvas HTML.html" 2> submission.yml
```

__In-class component__ (labs, tutorials, lectures):

```bash
uv run -m scripts.special.convert_canvas_submission <<< "/path/to/Canvas HTML.html" 2> lab.yml
```

Use `lab.yml` for labs, `tutorial.yml` for tutorials, and `lecture.yml` for lectures, overwriting the existing file when present. Assignments use `submission.yml`.

Redact author names in the resulting YAML:

```bash
sed -i '' "s/author: .*/author: '[redacted]'/" submission.yml
```

### Grade extraction

When the Canvas HTML is a submission detail page (containing "Grade:" and "pts possible"), extract the grade into the component YAML:

```yaml
grade:
  entered: 2    # from "Grade: 2"
  possible: 2   # from "(2 pts possible)"
```

Also extract `canvas_assignment_id` from the URL comment or page content for cross-referencing, and add both fields to `tutorial.yml`/`lab.yml`/`lecture.yml`.

### Stage 4: Solution

Input: solution file(s).

1. Add them to `solution/`. For an out-of-class component the directory is its private mirror.
2. Update the `index.md` solution section.

### Stage 5: Topic-note reconciliation

Every submission carries concepts the course's topic notes may already own. After the stages above, run "Topic-note reconciliation (mandatory)" in `academic-ingest`. A concept the submission names without developing stays in the session file, so start from the concepts it develops: extend the owning note where it adds something needed to state a concept the note already holds, prune what the material supersedes, create a topic note when none owns a developed concept, or record that the concept is already covered. A drawing the submission teaches is one of those concepts. The note that defines it carries the drawing as an SVG in `attachments/` (see "Definitional drawings" in `academic-ingest`); a picture belonging to one question stays a crop in that submission's own `attachments/`.

`lab.md`, `tutorial.md`, and `lecture.md` are the session's pages, not the home of its concepts. The session file keeps the material's own wording, while the topic note states the concept.

Reconcile before the humanizer pass, so the changed notes get humanized and validated together with the submission.

## CRUD operations

### Create

Follow the partial-info workflow above, starting from whatever stage the input provides.

### Read

List submissions in a directory; show details (due date, points, completion stage).

### Update

Fill in the next available stage. Check completion:

- Stage 1: `index.md` + `attachments/`
- Stage 2: files in `submission/`
- Stage 3: `submission.yml` (out-of-class) and, if applicable, `lab.yml`/`tutorial.yml`/`lecture.yml` (in-class)
- Stage 4: files in `solution/`
- Stage 5: the course's topic notes reconciled, each concept extended, pruned, created, or recorded as already covered

Add what is missing without disturbing existing content.

### Delete

Remove the submission directory and files, then remove it from the parent `index.md`. Remove the leaf's artifacts from the private mirror as well.

## Index page format

### Out-of-class only (assignments, or labs/tutorials/lectures without an in-class component)

```markdown
---
aliases:
  - <INSTITUTION> <COURSE> <type> <name>
  - <INSTITUTION> <COURSE> <type> <name> <variant>
tags:
  - date/<YYYY>/<MM>/<DD>
  - flashcard/active/special/academia/<INSTITUTION>/<COURSE>/<type>/<name>
  - language/in/English
---

# <name>

- <INSTITUTION> <COURSE>

---

- title: <Canvas title>
- due: <ISO 8601 with timezone>
- points: <N>
- submitting: <Canvas submission type>

---

<verbatim Canvas description>

[<filename>](attachments/<filename>)

## attachments

- [`<display-name>`](attachments/<file>)

## submission

- file: [`<uploaded>.<ext>`](submission/<uploaded>.<ext>)
    - metadata: [`submission.yml`](submission.yml)

## solution

- [`<filename>`](solution/<filename>)
```

When `assignment.md` exists, `index.md` gains `## children` as its last section with `- [assignment](assignment.md)`.

### Submission entry model

The submission entry names the artifact uploaded to Canvas. Choose the label that matches its form:

| Label | Use when |
| ----- | -------- |
| `- file:` | a single uploaded file (document, PDF, archive) |
| `- folder:` | an uploaded directory tree |
| `- URL:` | a link was submitted instead of a file |
| `- submission` | the submission type is not yet known (no link) |

These child keys nest under the entry:

- `metadata:`: the component YAML (`submission.yml`, `lab.yml`, `tutorial.yml`, `lecture.yml`) or rendering config such as `submission.pdf.yml`
- `filename:`: the uploaded filename, when it differs from the canonical on-disk name
- `source:`: the single local artifact the uploaded file was generated from
- `sources:`: the same relation when the submission rests on more than one artifact, each listed on its own nested line

A source never names the uploaded artifact; it records what that artifact was produced from, such as a `.md` or `.docx` rendered to the submitted PDF, a directory packed into the submitted archive, or the schematics a report's figures were exported from. Source files live in `submission/` beside the uploaded file, never in `attachments/`. Use `source:` for exactly one artifact and `sources:` as soon as there are two; never repeat `source:`. A file authored directly as the submission (a filled-in summary sheet, an assignment's own source file) has neither child.

```markdown
- file: [`submission.pdf`](submission/submission.pdf)
    - metadata: [`submission.yml`](submission.yml)
    - filename: `PS5-answer-key.pdf`
    - source: [`submission.md`](submission/submission.md)

- file: [`submission.docx`](submission/submission.docx)
    - metadata: [`submission.yml`](submission.yml)

- file: [`report.pdf`](submission/report.pdf)
    - metadata: [`submission.yml`](submission.yml)
    - sources:
        - [`figure 1.asc`](submission/figure 1.asc)
        - [`figure 2.asc`](submission/figure 2.asc)
```

### With in-class component (labs, tutorials, lectures)

When an in-class component exists, list both YAML metadata files in `## submission` using type-based labels, and add `## children` as the last section:

```markdown
---
aliases:
  - <INSTITUTION> <COURSE> <type> <name>
tags:
  - date/<YYYY>/<MM>/<DD>
  - flashcard/active/special/academia/<INSTITUTION>/<COURSE>/<type>/<name>
  - language/in/English
---

# <name>

- <INSTITUTION> <COURSE>

---

- title: <Canvas title>
- due: <ISO 8601 with timezone>
- points: <N>
- submitting: <Canvas submission type>

---

<verbatim Canvas description>

## attachments

- [`<display-name>`](attachments/<file>)

## submission

- file: [`<uploaded>.<ext>`](submission/<uploaded>.<ext>)
    - metadata: [`submission.yml`](submission.yml)
- in-class submission
    - metadata: [`<type>.yml`](<type>.yml)

## solution

- [`<filename>`](solution/<filename>)

## children

- [<type>](<type>.md)
```

### In-class content file (`lab.md`, `tutorial.md`, `lecture.md`)

When the in-class component comes from a Canvas assignment or assignment submission page, the Canvas header block — `- title:`, `- due:`, `- points:`, `- grade:`, `- submitting:`, and the verbatim Canvas description — belongs to `index.md`, and the content file carries the identity bullets and the authored content instead. Never leave the content file's body as a bare stub.

```markdown
---
aliases:
  - <INSTITUTION> <COURSE> <type> <name> <type>
  - <INSTITUTION> <COURSE> <name> <type>
tags:
  - flashcard/active/special/academia/<INSTITUTION>/<COURSE>/<type>/<name>/<type>
  - language/in/English
---

# <type>

- <INSTITUTION> <COURSE> <name>
- parent: [<name>](index.md)

## <authored content>
```

The Canvas header block sits in `index.md`, drawn from the component YAML (`lab.yml`, `tutorial.yml`, `lecture.yml`) by the rules in "Canvas metadata rules", and never in the content file. The index-only sections (`## attachments`, `## submission`, `## solution`, `## children`) stay in `index.md` as well.

A content file that is not Canvas-sourced keeps the ordinary note format instead.

### Out-of-class content file (`assignment.md`)

An assignment whose authored content exceeds the Canvas record carries it in `assignment.md`, stored at the leaf's mirrored path in the private tree. The file mirrors the Canvas header block of the in-class content files: frontmatter, `# assignment` heading, identity bullets, `---`, the metadata bullets drawn from `submission.yml`, `---`, then the authored content. The problems become question blocks when solutions exist; a specification becomes prose sections grouped by concept, per "Flashcard style per section" in `academic-ingest`. The file does not repeat the verbatim Canvas description; that stays in `index.md` alone.

```markdown
---
aliases:
  - <INSTITUTION> <COURSE> <name> assignment
tags:
  - flashcard/active/special/academia/<INSTITUTION>/<COURSE>/assignments/<name>/assignment
  - language/in/English
---

# assignment

- <INSTITUTION> <COURSE> <name>
- parent: [<name>](index.md)

---

- title: <Canvas title>
- due: <ISO 8601 with timezone>
- points: <N>
- submitting: <Canvas submission type>

---

<authored assignment content>
```

Aliases stay sorted and omit duplicates. Omit metadata bullets absent from the YAML. When `assignment.md` exists, `index.md` gains `## children` as its last section, linking the file as `- [assignment](assignment.md)`.

### Private artifacts and missing files

The artifacts of an out-of-class component live in the private tree by default (see "Public and private split"). A file that lives there still gets ordinary relative links in the public page, written as if it were colocated. Do not rewrite those links to point into `private/`, because the published copy has to resolve on its own.

Keep `## solution` in the same plain file-list style as `## attachments`. The nested `file:` plus `metadata:` layout belongs to `## submission`, and only earns its place when the archived filename details matter (see "Submission entry model" above).

And do not invent a link for a file that is genuinely missing from the archive. `\[missing\]` records the absence; a link to a file that was never committed is a broken link wearing the costume of content.

## Missing data

Use `\[missing\]` for absent fields, such as `points: \[missing\]` when ungraded or `venue: \[missing\]` when not yet assigned. Do not invent or generate placeholder content. See [special.instructions.md](../../instructions/special.instructions.md#missing-data).

## Canvas metadata rules

Canvas prose is copied and Canvas fields are normalised; never the other way round.

- Due date → ISO 8601 with timezone (seconds `:00` for start, `:59` for end)
- Availability windows: ISO datetime range + `, <ISO duration>`
- Description: verbatim Canvas wording, preserving `<span style>` for color
- Update announcements: verbatim with color and bold
- Canvas system messages (e.g., "This assignment was locked...", "No additional details were added for this assignment.") in or near the description body are part of the description and must be preserved verbatim
- Normalize metadata fields only, not the prose body
- `canvas_assignment_id`: numeric ID from the Canvas assignment URL or submission detail page, used to cross-reference PRS content and Canvas grade records

## submission.pdf.yml (PDF rendering metadata)

Some submissions include a `submission.pdf.yml` alongside `submission.yml`. That file controls PDF rendering and display configuration, separate from the Canvas submission metadata.

```yaml
landscape: false
margin:
  top: 0.5in
  right: 0.5in
  bottom: 0.5in
  left: 0.5in
page size: A4
scale: 1.0
```

Fields: `landscape` (page orientation), `margin` (page margins with units: in, cm, mm), `page size` (paper size: A4, letter, etc.), and `scale` (zoom factor, 1.0 = 100%).

Create `submission.pdf.yml` when a PDF needs non-default rendering (landscape, custom margins), when the submission is a cheatsheet or reference card with a specific layout, or when the PDF is displayed inline rather than linked.

`submission.yml` holds Canvas submission metadata (assignment ID, grade, course ID, author); `submission.pdf.yml` holds PDF rendering and display configuration. The two files are independent, and a submission can have either or both.

## Display-vs-link convention

The on-disk filename may differ from the Canvas display name (e.g., `PS7-3.pdf` displayed as `PS7.pdf`):

```markdown
[PS7.pdf](attachments/PS7-3.pdf)

## attachments

- [`PS7.pdf`](attachments/PS7-3.pdf)
```

The same applies to a submission, where the uploaded name goes in a `filename:` child:

```markdown
## submission

- file: [`submission.pdf`](submission.pdf)
    - metadata: [`submission.yml`](submission.yml)
    - filename: `2025_10_07 23_58 Microsoft Lens.pdf`
```

## Batch creation workflow

When creating multiple submissions at once:

1. Populate artifacts from source files first.
2. Extract all Canvas metadata upfront.
3. Create all `index.md` files.
4. Update all parent indexes.
5. Reconcile the course's topic notes with the material (see "Topic-note reconciliation (mandatory)" in `academic-ingest`).
6. Batch-validate.

## Parent index updates

After creating a submission page, add the child link to the parent `index.md` via `academic-crud-index`.

## Validation

Run the humanizer pass over new or changed prose and flashcards, focusing on your own solution prose and card answers; quoted question text stays verbatim (see "Humanizer pass" in `academic-ingest`). Then run `academic-lint`.

## References

- `convert_canvas_submission.py` for Canvas HTML extraction
- `academic-crud-index` for parent index updates
- `academic-crud-attachments` for submission-level attachments
- `academic-video` for video content
- `humanizer` for the AI-writing patterns it removes
- `academic-lint` for validation
