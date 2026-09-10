---
name: academic-crud-submission
description: Create, read, update, and delete submission-bound pages (labs, tutorials, lectures, assignments) with attachments, submissions, and solutions under special/academia/<INSTITUTION>/<COURSE>/. Handles partial information gracefully.
---

# Academic CRUD: Submission pages

Create, read, update, and delete submission-bound pages. Applies to `labs/`, `tutorials/`, `lectures/`, and `assignments/`. All share the same folder hierarchy and page format.

## Target

`<subdirectory>/<name>/index.md` + `attachments/` + `submission/` + `solution/`

## Dual-component model

Labs, tutorials, and lectures can have __two__ Canvas submission components:

- __Out-of-class__ (pre-lab, post-lab, take-home): work completed outside the session, submitted on Canvas. Can happen before, after, or both relative to the session. Metadata: `submission.yml`.
- __In-class__ (lab, tutorial, lecture): work done live during the session, also submitted on Canvas. Metadata: `lab.yml`/`tutorial.yml`/`lecture.yml`.

Assignments have a single component → `submission.yml`.

When the in-class component exists, the `index.md` links to `lab.md`/`tutorial.md`/`lecture.md` as children. The Canvas HTML for the in-class component is converted to the component-specific YAML via `convert_canvas_submission.py`.

| Submission type     | Out-of-class YAML  | In-class YAML      | In-class content   |
| ------------------- | ------------------ | ------------------ | ------------------ |
| Lab                 | `submission.yml`   | `lab.yml`          | `lab.md`           |
| Tutorial            | `submission.yml`   | `tutorial.yml`     | `tutorial.md`      |
| Lecture             | `submission.yml`   | `lecture.yml`      | `lecture.md`       |
| Assignment          | `submission.yml`   | N/A                | N/A                |

## Partial-info workflow

Submissions arrive in stages. Each stage fills in what's available without requiring all information upfront.

### Stage 1: Canvas HTML + attachments

Input: Canvas assignment HTML page + prompt files.

1. Create directory: `<subdir>/<name>/` with `attachments/`, `submission/`, `solution/`
2. Extract Canvas metadata from HTML:
   - Title, due date (ISO 8601 with timezone), points, submission type
   - Description text (verbatim with `<span style>` for color)
   - Update announcements (verbatim)
   - Assignment ID from URL comment
3. Create `index.md` with metadata and description
4. Copy prompt PDFs and data files to `attachments/`
5. Apply display-vs-link convention for versioned PDFs

### Stage 2: Submission file(s)

Input: submitted work (PDF, source markdown, images).

1. Add files to `submission/`
2. Update `index.md` submission section
3. For Apple Notes markdown:
   - Detect UUID attachment paths: `(Attachments|../attachments)/<UUID>.<ext>`
   - Rewrite paths to `../attachments/`
   - Add file-level suppression comments at top
   - Copy referenced UUID-named images to `attachments/`
4. For regular markdown: copy as-is

### Stage 3: submission.yml

Input: Canvas HTML (for metadata extraction).

__Out-of-class component__ (default):

```bash
uv run -m scripts.special.convert_canvas_submission <<< "/path/to/Canvas HTML.html" 2> submission.yml
```

__In-class component__ (labs, tutorials, lectures):

```bash
uv run -m scripts.special.convert_canvas_submission <<< "/path/to/Canvas HTML.html" 2> lab.yml
```

Use `lab.yml` for labs, `tutorial.yml` for tutorials, `lecture.yml` for lectures. Overwrite the existing file if present.

__Assignments__: run the convert script to produce `submission.yml`, overwriting if needed.

Redact author names in the resulting YAML:

```bash
sed -i '' "s/author: .*/author: '[redacted]'/" submission.yml
```

### Stage 4: Solution

Input: solution file(s).

1. Add to `solution/`
2. Update `index.md` solution section

## CRUD operations

### Create

Follow the partial-info workflow above, starting from whatever stage the input provides.

### Read

List submissions in a directory; show details (due date, points, completion stage).

### Update

Fill in the next available stage. Check completion:

- Stage 1 done? → check for `index.md` + `attachments/`
- Stage 2 done? → check for files in `submission/`
- Stage 3 done? → check for `submission.yml` (out-of-class) and, if applicable, `lab.yml`/`tutorial.yml`/`lecture.yml` (in-class)
- Stage 4 done? → check for files in `solution/`

Add what's missing without disturbing existing content.

### Delete

Remove the submission directory and files. Remove from parent `index.md`.

## Index page format

### Out-of-class only (assignments, or labs/tutorials/lectures without in-class component)

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

- submission
  - metadata: [`submission.yml`](submission.yml)
  - source: [`<source>.md`](submission/<source>.md)

## solution

- [`<filename>`](solution/<filename>)
```

The `- submission` label is a generic type used when the specific submission type is not yet determined. When the type is known, replace with the concrete type (e.g., `- file: ...`). See the in-class example below.

### With in-class component (labs, tutorials, lectures)

When an in-class component exists, list both YAML metadata files in `## submission` using type-based labels, and add a `## children` section as the very last section:

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

- submission
  - metadata: [`submission.yml`](submission.yml)
  - source: [`<source>.md`](submission/<source>.md)
- in-class: metadata: [`<type>.yml`](<type>.yml)

## solution

- [`<filename>`](solution/<filename>)

## children

- [<type>](<type>.md)
```

## Missing data

Use `\[missing\]` for absent fields — for example, `points: \[missing\]` when ungraded, or `venue: \[missing\]` when not yet assigned. Do not invent or generate placeholder content for missing values. See [special.instructions.md](../../instructions/special.instructions.md#missing-data).

## Canvas metadata rules

- Due date → ISO 8601 with timezone (seconds `:00` for start, `:59` for end)
- Availability windows: ISO datetime range + `, <ISO duration>`
- Description: verbatim Canvas wording, preserve `<span style>` for color
- Update announcements: verbatim with color and bold
- Canvas system messages (e.g., "This assignment was locked...", "No additional details were added for this assignment.") appearing in or near the description body are part of the description and must be preserved verbatim
- Normalize metadata fields only, not prose body

## submission.pdf.yml (PDF rendering metadata)

Some submissions include a `submission.pdf.yml` file alongside `submission.yml`. This file controls PDF rendering and display configuration, separate from the Canvas submission metadata.

### Format

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

### Fields

- `landscape`: `true` or `false` — page orientation
- `margin`: page margins with units (in, cm, mm)
- `page size`: paper size (A4, letter, etc.)
- `scale`: zoom factor (1.0 = 100%)

### When to create

Create `submission.pdf.yml` when:

- A PDF needs non-default rendering (landscape, custom margins)
- The submission is a cheatsheet or reference card with specific layout
- The PDF is displayed inline rather than linked

### Relationship to submission.yml

- `submission.yml` = Canvas submission metadata (assignment ID, grade, course ID, author)
- `submission.pdf.yml` = PDF rendering/display configuration

They are independent files. A submission can have either or both.

### Examples

ACCT 2010 final examination cheatsheet:

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

## Display-vs-link convention

On-disk filename may differ from Canvas display name (e.g., `PS7-3.pdf` displayed as `PS7.pdf`):

```markdown
[PS7.pdf](attachments/PS7-3.pdf)

## attachments

- [`PS7.pdf`](attachments/PS7-3.pdf)
```

## Batch creation workflow

When creating multiple submissions at once:

1. Populate artifacts from source files first
2. Extract all Canvas metadata upfront
3. Create all index.md files
4. Update all parent indexes
5. Batch-validate

## Parent index updates

After creating a submission page, add child link to the parent `index.md` via `academic-crud-index`.

## Validation

Run `academic-lint` after every edit. If you know which files changed, pass those files specifically. Otherwise lint the whole course folder.

## References

- `convert_canvas_submission.py` Canvas HTML to `submission.yml` / `lab.yml` / `tutorial.yml` / `lecture.yml`
- `academic-crud-index` parent index updates
- `academic-crud-attachments` submission-level attachments
- `academic-lint` validation
