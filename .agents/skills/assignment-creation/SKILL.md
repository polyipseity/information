---
name: assignment-creation
description: Create and maintain assignment pages (problem sets, homework, project milestones) under special/academia/<INSTITUTION>/<COURSE>/assignments/.
---

# Assignment creation

Use this skill when creating new assignment pages or adding assignment-related
content (problem sets, homework, project milestones, lab rounds, deliverable
pages) to course knowledge bases under `special/academia/`.

Flashcards and other generated content are rebuilt automatically by the build
system; do __not__ run `init generate` manually.

For general academic-note conventions (frontmatter, topic notes, lecture
content, flashcards, LaTeX), see the
[academic-notes](../academic-notes/SKILL.md) skill.

## Guiding principle: follow existing conventions

Before creating a new assignment page, examine 1–3 existing assignment pages
in the same course to identify the conventions already in use. Match the
existing style unless there is a compelling reason to deviate. Pay particular
attention to:

- __Naming__ — folder naming (`problem set 1` vs `ps1` vs `homework 1` vs
  `hw1`), file naming, heading capitalization
- __Frontmatter__ — alias combinations (which institution/course
  abbreviations), tag path patterns, tag categories
- __Metadata__ — which fields are included, their order, formatting style
- __Description__ — verbatim Canvas wording vs summarized, how colors and
  formatting are preserved
- __Section structure__ — section ordering, which sections are present or
  absent, heading level conventions
- __Companion pages__ — which companion pages exist (`lab.md`, `prelab.md`,
  etc.), how they are structured
- __Submission and solution__ — format, level of detail, which artifacts are
  tracked and how

Consistency across assignments in the same course makes the knowledgebase
more predictable to navigate.

## Directory structure

Each course with assignments should have an `assignments/` folder under the
course root. The top-level `assignments/index.md` lists all assignments.

Each assignment lives in its own subfolder:

```text
assignments/
├── index.md                                    # lists all assignments
└── <assignment-name>/
    ├── index.md                                # assignment page
    ├── attachments/                            # prompt PDFs, data files, images
    ├── submission/                             # submitted work (PDFs, source files)
    ├── solution/                               # official or self-made solutions
    └── submission.yml                          # Canvas export metadata (optional)
```

Common naming patterns:

- Problem sets: `problem set 1/`, `problem set 2/`
- Homework: `homework 1/`, `homework 2/`
- Project milestones: `milestone 1/`, `milestone 2/`

## Creating a new assignment

__Batch creation workflow:__ When creating multiple assignments in one pass
(e.g., PS2–PS11), follow this order to minimize rework:

0. __Populate artifacts from source files__ — if a course source directory
   exists (e.g., `.course_sources/`), copy all artifacts (solution PDFs,
   submission PDFs, Apple Notes markdown, prompt PDFs, images) into each
   assignment folder in batch before writing index.md files. See the
   [Source file management](#source-file-management) section below.
1. __Extract submission.yml from Canvas HTMLs__ — see the
   [Submission metadata file](#submission-metadata-file) section below for
   how to drive `convert_canvas_submission.py` in batch. Do this after
   step 0 and before step 1, since the YAML feeds into verification later.
2. Extract all Canvas data upfront — parse every Canvas HTML page and record
   its metadata (due dates, points, submission type, description text, update
   announcements, PDF filenames) in one batch.
3. Create all assignment files — write each index.md using the extracted data.
4. Update all indexes — update `assignments/index.md` and the course root
   `index.md` in a single pass.
5. Batch-validate — run `bun run check:md --no-globs <all files>` and verify
   each against its Canvas source.

Steps 0 and 2 are independent and can be parallelized across assignments
using shell loops.

This avoids the inefficiency of creating one assignment, discovering a pattern
change, and having to retroactively fix earlier ones.

### 1. Prerequisites

Before creating an assignment page, ensure you have:

- __Existing assignments__ in the same course to use as style references.
  Examine their naming, frontmatter, metadata, section ordering, and
  companion pages to match conventions (see the guiding principle above).
- The __course root__ directory and `index.md` already exist.
- The __Canvas HTML source__ of the assignment, typically saved in a
  `.course_sources/` or a similar course-specific source directory. Search for
  the assignment by name in the Canvas HTML exports.
- Any __attachments__ (prompt PDFs, data files, images) from the Canvas
  assignment page.

> __Critical: Canvas-first data source.__ All metadata (due dates, points,
> submission type, description text, PDF filenames, update announcements, color
> styling) MUST be extracted from the actual Canvas HTML page. __Never fabricate
> or guess__ these values — the user will catch and demand fixes. If the Canvas
> HTML is unavailable, ask the user to provide it before proceeding.

### 2. Set up the directory structure

Create the assignment directory and subdirectories:

```bash
mkdir -p assignments/<assignment-name>/{attachments,submission,solution}
```

### 3. Create the assignment index.md

The assignment's `index.md` follows a specific structure with these components
in order:

1. __YAML frontmatter__ with aliases and tags
2. __Heading and course line__
3. __Metadata block__ (between `---` separators): Canvas-derived title, due
   date, points, submitting type, etc.
4. __Description prose__ (optional): verbatim Canvas wording with formatting
   preserved
5. __Attachment links__ (optional): inline PDF/data links
6. __`## attachments`__: file list of assignment prompt materials
7. __`## submission`__: submitted work (PDF, source markdown, metadata)
8. __`## solution`__: official or self-made solution

#### YAML frontmatter

Use exhaustive alias combinations following the course pattern:

```yaml
---
aliases:
  - HKUST MATH 2431 PS1
  - HKUST MATH 2431 problem set 1
  - HKUST MATH2431 PS1
  - HKUST MATH2431 problem set 1
  - MATH 2431 PS1
  - MATH 2431 problem set 1
tags:
  - date/2026/02/13 # due date
  - flashcard/active/special/academia/HKUST/MATH_2431/assignments/problem_set_1
  - language/in/English
---
```

The aliases should cover all reasonable combinations of:

- Institution abbreviation + course code + assignment name
- Course code alone + assignment name
- Short form (PS1, HW1) and long form (problem set 1, homework 1)
- The tag path uses underscore-normalized segments matching the filesystem path.

#### Metadata block

After the heading, separate metadata with `---` lines:

```markdown
# problem set 1

- HKUST MATH 2431

---

- title: Problem Set 1
- due: 2026-02-13T13:30:00+08:00
- points: 8
- submitting: a text entry box or a file upload
```

Normalize timestamps to ISO 8601 with timezone. For assignments with
availability windows, use a range: `available: 2025-09-25T00:00:00+08:00/2025-10-03T23:59:59+08:00, P8DT23H59M59S`.

#### Description formatting

Reproduce Canvas HTML verbatim, preserving formatting with Markdown and inline
`<span style>` for colors:

```markdown
---

Problem Set 1, due on <span style="color: #0e68b3">**Friday 13/02/2026, until 13:30 (1:30 PM)**</span> Hong Kong Time (UTC +8), to be uploaded on Canvas <span style="color: #e62429">**(note the updated deadline)**</span>.

**<span style="color: #e62429">Update (05/02/2026, 10:30 AM): Question 4 updated, and mandatory problem changed from 4 to 3</span>**; if you already submitted your solutions, Question 4 will be graded **or** Question 3 in case you update your solution.

[PS1-v4.pdf](attachments/PS1-v4.pdf)
```

Rules:

- Keep visible Canvas wording __verbatim__.
- Preserve color with `<span style>` tags.
- Use Markdown for bold, italics, links, paragraphing, and line breaks.
- Keep inline prose dates and times as-is (the normalized metadata block above
  carries the machine-readable equivalents).

__Deadline extension text:__ Canvas often adds extension notices in colored
span tags. Reproduce them exactly, including the exact phrasing and color.
Common patterns seen in practice:

```markdown
(Note: This assignment deadline has been extended)

<span style="color: #e62429">**(note the extended deadline)**</span>

<span style="color: #e62429">**(Attention: Extended deadline!)**</span>
```

__Update announcements:__ Canvas pages may have inline update notices
(e.g., "Small clarification on Problem 1", "Question 4 updated"). Preserve
both the heading and body verbatim, with the same color and bold styling:

```markdown
**<span style="color: #e62429">Update (04/03/2026, 10:20 PM): Small clarification on Problem 1</span>**

**<span style="color: #e62429">Update (16/03/2026, 12:15 PM): Question 4 updated</span>**; if you already
submitted your solutions, the new version is optional.
```

#### Attachments section

List the assignment prompt files with links:

```markdown
## attachments

- [`PS1-v4.pdf`](attachments/PS1-v4.pdf)
```

__PDF display name vs actual file link:__ When the on-disk file has a versioned
name (e.g., `PS7-3.pdf`, `PS10-1.pdf`) but Canvas references a base name
(`PS7.pdf`, `PS10.pdf`), display the Canvas name while linking to the actual
file. This keeps the page consistent with what students see on Canvas while
still serving the correct file:

```markdown
[PS7.pdf](attachments/PS7-3.pdf)

## attachments

- [`PS7.pdf`](attachments/PS7-3.pdf)
```

#### Submission section

Record submitted work. This can include:

- The submitted PDF
- The source file (e.g., Apple Notes markdown export)
- `submission.yml` with Canvas export metadata

```markdown
## submission

- submission: [`HKUST MATH 2431 - problem set 1.pdf`](submission/HKUST%20MATH%202431%20-%20problem%20set%201.pdf)
  - metadata: [`submission.yml`](submission.yml)
  - source: [`HKUST MATH 2431 problem set 1.md`](submission/HKUST%20MATH%202431%20problem%20set%201.md)
```

When an answer list is available (e.g., quizzes with short answers), include
the numbered list:

```markdown
## submission

1. ...
2. ...
```

When the submission section needs archived-filename provenance or similar
metadata, keep that extra structure only in `## submission`, for example
`- file: [submission.pdf](submission.pdf)` followed by nested metadata
bullets such as `- filename: ...`.

When the task still wants the public page to preserve the normal artifact
routes, keep standard relative links in public `## submission` /
`## solution` sections _as if the files were colocated_, for example
`[submission.pdf](submission.pdf)` or
`[HW1_Sol.pdf](solution/HW1_Sol.pdf)`. Do __not__ rewrite those links to
`private/` paths in the public note.

#### Submission metadata file

The `submission.yml` file stores Canvas export metadata. Its structure:

```yaml
assignment:
  comments: {}
  content: ""
  grade:
    entered: 8
    graded anonymously: false
    possible: 8
  id: 425065
  properties:
    due: 2026-02-13 13:30:00-07:00
    points: 8
    submitting:
      - a text entry box or a file upload
  submissions:
    - datetime: 2026-02-11 13:26:00-07:00
      id: -1
  title: Problem Set 1
course:
  id: 69402
  name: MATH2431
```

Extract this from the Canvas assignment HTML page using the
`convert_canvas_submission.py` tool, which reads a SingleFile-saved HTML
and writes the YAML structure to stderr.

__Tool characteristics:__

- __Interactive by design__ — no CLI arguments. It calls `input("HTML file? ")`
  and expects the file path on stdin, then writes the YAML document to stderr.
- __Single-file only__ — one invocation per assignment page.
- __Input__ — a SingleFile (or equivalent full-page) HTML export of the Canvas
  assignment page. The HTML must contain the Canvas URL in a comment
  (`` `url: ...` ``) and a saved-date comment; otherwise the tool silently
  exits with code 1.
- __Output__ — a single YAML mapping to stderr (exit code 0 on success).

__Driving the tool non-interactively:__

Use a here-string to supply the file path on stdin and redirect stderr to
capture the YAML:

```bash
uv run -m scripts.special.convert_canvas_submission \
  <<< "/path/to/Canvas HTML.html" \
  2> submission.yml
```

__Canvas HTML filenames may be inconsistent__ — the same course can have
mixed naming conventions (e.g., `"HKUST Canvas - Problem Set N …"` for some
assignments and `"Problem Set N …"` for others). Always `ls` the source
directory to discover the actual filenames before writing loops.

__Batch extraction loop:__

```bash
# Discover actual filenames first
ls <source-dir>/

# Then adapt the loop to the naming convention found
for N in $(seq <first> <last>); do
  html_path=$(find <source-dir> -maxdepth 1 -name "*Problem Set $N*" -type f)
  if [ -n "$html_path" ]; then
    uv run -m scripts.special.convert_canvas_submission \
      <<< "$html_path" \
      2> "assignments/problem set $N/submission.yml"
  fi
done
```

__Comment author redaction:__ After saving `submission.yml`, replace every `author:` value (which contains a real name) with `'[redacted]'` to protect privacy:

```bash
sed -i '' "s/author: .*/author: '[redacted]'/" assignments/problem\ set\ */submission.yml
```

This redacts grader/comment author names while preserving the rest of the YAML structure. Run this after extracting all files.

Preserve the YAML output as-is — do not edit the extracted file (except for the author redaction above).

#### Markdown submission source preservation

Some submissions are written as Markdown files. Judge whether the file is an
Apple Notes export (needs special handling) or regular Markdown.

__Judging if a file is an Apple Notes markdown export:__

The file may already have our modifications (attachment path rewrites,
suppression comments at top). Look past those and examine the body.

A file is likely from Apple Notes if it has one or more of:

- __UUID attachment paths__ — Image references match
  `(Attachments|../attachments)/<UUID>.<ext>` (e.g.,
  `Attachments/A1B2C3D4-...png`). Most reliable indicator.
- __No YAML frontmatter__ — The body starts directly with content.
- __Apple formatting quirks__ — Unusual heading styles or list spacing
  characteristic of Apple Notes output.

A file is __not__ an Apple Notes export if it has YAML frontmatter,
flashcard/pytextgen markup, or consistently manual formatting throughout.

If unsure, treat as regular Markdown (no path rewrites, no suppression
comments). The user can correct.

__For Apple Notes markdown exports:__

1. Copy into `submission/` as `"<Course Name> problem set N.md"` (source may
   use hyphens; normalize to no hyphens).
2. __Only__ make these changes:
   - Rewrite image paths `Attachments/XXX.ext` → `../attachments/XXX.ext`.
   - Add file-level markdownlint and validator suppression comments at the
     very top.
3. __Do NOT__ make other changes. Preserve spelling, formatting, images,
   and structure exactly. Edit in Apple Notes and re-export if needed.

__For regular Markdown submissions:__

Copy as-is. Do not add suppression comments or rewrite attachment paths.

#### Solution section

Link to the solution file:

```markdown
## solution

- [`SL1.pdf`](solution/SL1.pdf)
```

### 4. Add attachments

Place all assignment prompt files (PDFs, data CSVs, images) in the
`attachments/` directory. Keep filenames as-is from the source.

When an Apple Notes markdown submission (identified using the criteria in
[Markdown submission source preservation](#markdown-submission-source-preservation))
embeds HEIC, PNG, or other image formats, also place those images in
`attachments/` and update the attachment paths as described in that section.

### 5. Update assignments/index.md

The top-level `assignments/index.md` lists all assignments. Add a new child
link for the new assignment:

```markdown
---
aliases:
  - HKUST MATH 2431 assignment
  - HKUST MATH 2431 assignments
  - HKUST MATH2431 assignment
  - HKUST MATH2431 assignments
tags:
  - flashcard/active/special/academia/HKUST/MATH_2431/assignments
  - function/index
  - language/in/English
---

# index

- HKUST MATH 2431

## children

- [problem set 1](problem%20set%201/index.md)
```

### 6. Update course index.md

Add an `- assignment:` entry in the course's `index.md` under the last lecture
entry on or before the due date. Place it after `- topic:` and `- status:`:

```markdown
## week N lecture

- datetime: 2026-02-11T13:30:00+08:00/2026-02-11T14:50:00+08:00
- topic: ...
- assignment: [problem set 1](assignments/problem%20set%201/index.md)
```

If the lecture already has a `topic:` and optional `status:`, add
`assignment:` after them.

### 7. Verify against Canvas sources

After creating or updating assignment pages, systematically verify each one
against its Canvas HTML source. Check these fields:

- __Due date__ — ISO 8601 timestamp matches Canvas, including timezone
- __Points__ — exact integer or float
- __Submission type__ — matches Canvas wording (e.g., "a text entry box or a
  file upload")
- __Description body__ — verbatim match, including all update announcements
  and colored span tags
- __PDF filenames__ — display name matches Canvas; link target matches
  on-disk file
- __Metadata block__ — title, due date, points, submitting all present
- __`submission.yml` presence__ — exists and is non-empty
- __`assignment.id` match__ — the extracted `id` field matches the known
  Canvas assignment ID for that page. This catches cases where the wrong
  HTML file was used. Known IDs from Canvas can be read from the
  `url: https://<host>/courses/<course_id>/assignments/<assign_id>` comment
  in the source HTML.

If the course has multiple assignments, verify them all in one pass and report
any discrepancies to the user for resolution.

### 8. Source file management

When the course has a source directory (e.g., `.course_sources/`), populate
the assignment folder from source files. Copy (do not symlink) files — this
keeps the archive self-contained and stable even if cleaned up later.

__There is no fixed source hierarchy.__ Every course source directory is
organized differently (by the user's personal convention, LMS export format,
or ad-hoc collection). The examples below illustrate the _kind_ of work
involved, not a structure to expect in any other course. Always start by
exploring the actual source directory with `ls`/`tree`/`find` to discover
its real layout before writing copy commands.

To populate an assignment folder, you typically need to locate and copy
these artifact types wherever they happen to live in the source tree:

#### Solution files

Locate solution PDFs somewhere in the source tree (e.g., in a
`questions/` subdirectory) and copy:

```bash
cp <path-in-source>/SL{N}.pdf assignments/problem\ set\ {N}/solution/
```

#### Submission PDFs

Find the submission PDF (often named after the course and assignment) and
copy it into the assignment's `submission/` folder:

```bash
cp <path-in-source>/"Course Name - problem set N.pdf" \
   assignments/problem\ set\ {N}/submission/
```

#### Markdown submission source (with path rewrites)

Judge per
[Markdown submission source preservation](#markdown-submission-source-preservation).
If Apple Notes: detect naming pattern, create with suppression header and
path rewrites, copy referenced UUID-named images from source attachments.
Otherwise copy as-is.

A shell pipeline illustrating the process (paths are specific to one source
layout; adapt to the actual layout):

```bash
# Detect source file name (may be with or without hyphen)
if [ -f "$SOURCES/Course Name problem set N.md" ]; then
  SRC="$SOURCES/Course Name problem set N.md"
else
  SRC="$SOURCES/Course Name - problem set N.md"
fi
DST="$PS_DIR/submission/Course Name problem set N.md"

# Write suppression header + rewritten content
# (suppressions: file-level markdownlint and validator comments)
echo '<!-- markdownlint-disable ... -->' > "$DST"
# Add validator suppression comment too
echo '<!-- check: ignore-file[...]: Apple Notes markdown — do not modify -->' >> "$DST"
sed 's|Attachments/|../attachments/|g' "$SRC" >> "$DST"

# Copy all UUID-named image files referenced in the source
grep -o '[A-F0-9]\{8\}-[A-F0-9]\{4\}-[A-F0-9]\{4\}-[A-F0-9]\{4\}-[A-F0-9]\{12\}\.[a-z]*' "$SRC" \
  | while read -r uuid_file; do
      cp "$ATTACHMENTS_SRC/$uuid_file" "$PS_DIR/attachments/"
    done
```

#### Assignment prompt PDFs

Find prompt PDFs in the source tree and copy into `attachments/`:

```bash
cp <path-in-source>/PS{N}*.pdf assignments/problem\ set\ {N}/attachments/
```

When the on-disk file is versioned (e.g., `PS7-3.pdf`) but Canvas references
a base name (`PS7.pdf`), apply the
[display-vs-link naming convention](#pdf-display-name-vs-actual-file-link).

#### Submission metadata

If a `submission.yml` already exists somewhere in the source (e.g., from a
previous Canvas export extraction), copy it into the assignment folder.
Otherwise, extract it from the Canvas HTML file using
`convert_canvas_submission.py`. See the
[Submission metadata file](#submission-metadata-file) section for the
invocation pattern (here-string for stdin, stderr redirect for output).

#### Batch copy workflow

When populating multiple assignments at once from a shared source directory,
first explore the source layout thoroughly, then combine copy operations
into loops:

```bash
# Explore source layout first
tree <source> -L 3

# Then adapt loops to the actual layout
for N in $(seq <first> <last>); do
  cp <source>/<path-to-solution-files> assignments/problem\ set\ $N/solution/
done
```

Validate each loop's output before proceeding to the next.

## Assignment-style leaf index pages

Some leaf folders represent a single Canvas or LMS assignment-like artifact,
such as a lab round, homework, project milestone, or similar deliverable page
with local attachments. Canvas quizzes are the main exception: keep quiz notes
in `questions/quiz N.md` (and the mirrored private quiz file when archived)
rather than in `assignments/online quiz N/index.md`.

__Follow existing conventions__ — before creating a leaf index page, check an
existing leaf index from the same course for section ordering, metadata style,
and companion page patterns. The rules below describe the standard form, but
the course may have established variations (e.g., extra sections, different
heading levels) that should be preserved for consistency.

Use these rules when the source is a Canvas assignment HTML page:

- Keep the visible Canvas wording verbatim in the description body.
- Preserve color with `<span style>` and use Markdown for bold, italics,
  links, paragraphing, and line breaks.
- Treat the Canvas title header as metadata inside `## description`, not as a
  Markdown heading. The first property in that section should be exactly
  `- title: <Canvas title header verbatim>`.
- Normalize any Canvas-derived metadata value that contains a date, datetime,
  or duration into ISO 8601. Use timezone-aware ISO datetimes for point events
  such as `Due` or `locked at`; use an ISO datetime range and append `, <ISO
duration>` when both endpoints are known; use an ISO duration for pure
  durations. If only the closing endpoint is known, prefer a key such as
  `- Available until: 2026-04-09T13:30:59+08:00` rather than a human-readable
  phrase. Canvas start timestamps should use seconds `:00`; Canvas end
  timestamps should use seconds `:59`.
- Apply that normalization to Canvas __metadata fields only__, not to the
  ordinary prose body of `## description`. Keep description prose verbatim even
  when it contains human-readable dates or times, such as `This assignment was
locked Mar 5 at 1:30pm.` or colored `Due on` notice text copied from Canvas.
  The normalized metadata bullets should carry the machine-readable timing,
  while the surrounding Canvas wording stays as originally shown.
- For these assignment-style leaf indexes, use this section order:
  index metadata (with no extra `---` after the parent line), `## children`,
  `## description`, `## attachments`, `## submission`, and `## solution`.
- Omit generic `## logistics` and `## overview` sections on these pages.
- Include an explicit attachments list pointing to the local `attachments/`
  files. Apply the same display-vs-link convention: display the Canvas PDF
  name but link to the actual on-disk file if they differ.
- Leave `## submission` and `## solution` empty until actual repository
  content is provided.
- If the user wants only the statement or public handouts exposed publicly,
  keep those files in the public `attachments/` folder and move only
  submission or solution artifacts into the mirrored `private/` subtree.
- When a solution artifact exists, format `## solution` the same way as
  `## attachments`: use a plain markdown file list such as
  `- [HW1_Sol.pdf](solution/HW1_Sol.pdf)`.
- Follow the general submission and solution rules from the Creating a
  new assignment workflow above (the `#### Submission section` and the
  solution and attachment rules). The leaf `## submission` /
  `## solution` sections behave identically to the standard assignment
  pattern.
- Preserve the visible Canvas wording that mentions private-only or missing
  artifacts. If a referenced file truly is absent from the archive, keep the
  wording as plain text or add a short absence note rather than inventing a
  fake file.

When an assignment-style leaf folder also has companion pages such as
`lab.md`, `prelab.md`, `submission.md`, or similar pages:

- Let `index.md` own the Canvas wording, logistics, availability, file types,
  and attachments list.
- Use the companion pages for new knowledge points, worked cases,
  implementation pitfalls, or interpretation habits that are specific to the
  assignment family.
- Keep companion-page prose and flashcards about pure knowledge only. Avoid
  workflow checklists, student expectations, assessment framing, or other
  logistics-like prose in `lab.md`, `prelab.md`, and similar pages.
- Do not embed course-specific file references (filenames, submission scripts,
  temporary handout names, or exported worksheet names) in durable companion-
  page prose unless the file itself is the subject. Keep those references in
  archive metadata, `attachments/`, or submission records instead.
- When the source material includes concrete programming work such as MATLAB,
  companion pages should also preserve the local implementation knowledge:
  short code idioms, function choices, indexing patterns, plotting habits, and
  data-representation details that make the assignment's subject matter
  operational. Prefer a few concise snippets over full script dumps.
- For code-centered flashcards in companion pages, keep enough local context in
  the prompt to make the card standalone: include the relevant MATLAB fragment,
  variable roles, or input-output relationship instead of asking only a short
  generic question about a function name.
- When a code-centered flashcard still feels too abstract, also put the local
  given on the left-hand side: the specific waveform, filter, index formula, or
  before/after workflow that the student is supposed to remember.
- When the user asks for "more context," prefer adding that context to the
  __left-hand side prompt itself__ rather than only expanding the answer. The
  question should carry the local givens before the separator.
- Avoid meta-summary sections whose main job is to describe what the note
  covers. Companion pages should read like normal subject-matter notes: start
  with the content itself, and use ordinary reference sentences when routing to
  durable topic notes.
- Keep prelab pages restricted to preparation-stage knowledge and setup habits.
  Move solved assignment-specific values, extracted peaks, chosen cutoffs,
  reconstructed formulas, and post-hoc response interpretation into `lab.md`
  instead of leaving those results in `prelab.md`.
- If a concept already has a durable topic note, link to that note instead of
  re-teaching the theory in the companion page.
- Do not add flashcards for theory that is already covered in the topic note;
  keep companion-page flashcards focused on page-specific knowledge or worked
  cases.

## Course index linkage

When updating the course `index.md`, place `assignments/` immediately after
`## children` and before session entries when the course has an assignments
section. This order applies to course-root `index.md`, not to the assignment-
specific `assignments/index.md`.

Example course index child order:

```markdown
## children

- [AGENTS](AGENTS.md)
- [assignments](assignments/index.md)
- [questions/](questions/index.md)
- [topic 1](topic%201.md)
- ...
```

## Flashcards

Assignment creation rarely involves creating flashcards in the assignment
pages themselves. Flashcards for solution techniques and problem-solving
methods belong in the relevant topic notes or question pages. Assignment
index pages are reference pages, not learning pages.

## Related skills

- [academic-notes](../academic-notes/SKILL.md) — Course note structure,
  frontmatter, topic notes, lecture content, LaTeX conventions, quizzes,
  and general academic note-taking workflow.
