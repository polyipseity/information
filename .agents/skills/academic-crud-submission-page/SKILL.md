---
name: academic-crud-submission-page
description: Create, read, update, and delete submission-bound pages (labs, tutorials, lectures, assignments) with attachments, submissions, and solutions under special/academia/<INSTITUTION>/<COURSE>/. Handles partial information gracefully.
---

# Academic CRUD: Submission pages

Create, read, update, and delete submission-bound pages. Applies to `labs/`, `tutorials/`, `lectures/`, and `assignments/`. All share the same folder hierarchy and page format.

## Target

`<subdirectory>/<name>/index.md` + `attachments/` + `submission/` + `solution/`

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

1. Extract:

   ```bash
   uv run -m scripts.special.convert_canvas_submission <<< "/path/to/Canvas HTML.html" 2> submission.yml
   ```

2. Redact author names:

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
- Stage 3 done? → check for `submission.yml`
- Stage 4 done? → check for files in `solution/`

Add what's missing without disturbing existing content.

### Delete

Remove the submission directory and files. Remove from parent `index.md`.

## Index page format

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

- submission: [`<filename>`](submission/<filename>)
  - metadata: [`submission.yml`](submission.yml)
  - source: [`<source>.md`](submission/<source>.md)

## solution

- [`<filename>`](solution/<filename>)
```

## Canvas metadata rules

- Due date → ISO 8601 with timezone (seconds `:00` for start, `:59` for end)
- Availability windows: ISO datetime range + `, <ISO duration>`
- Description: verbatim Canvas wording, preserve `<span style>` for color
- Update announcements: verbatim with color and bold
- Normalize metadata fields only, not prose body

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

After creating a submission page, add child link to the parent `index.md` via `academic-crud-index-page`.

## Validation

```bash
uv run .agents/skills/academic-notes/check.py "special/academia/<INSTITUTION>/<COURSE>/<subdir>/<name>/index.md"
```

## References

- `convert_canvas_submission.py` Canvas HTML to `submission.yml`
- `academic-crud-index-page` parent index updates
- `.agents/skills/academic-notes/check.py` validator
