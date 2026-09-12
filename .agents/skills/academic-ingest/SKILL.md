---
name: academic-ingest
description: Single entry point for all academic material ingestion. Accepts files, clipboard text, or pasted content; classifies the target destination in the repository and dispatches to the appropriate academic-crud-* skill.
---

# Academic Ingest

Single entry point for all academic material ingestion. Accepts files (PDF, HTML, Markdown, images), clipboard text, or pasted content. Classifies the target destination, resolves the target course, and dispatches to the appropriate `academic-crud-*` skill.

Apply the classification to __each material independently__. A single invocation may produce multiple independent classifications, each dispatched to its own skill.

## Input handling

Accept any combination of:

- File paths (PDF, HTML, Markdown, images)
- Clipboard content (`--clipboard` or pasted text)
- Inline text from the user
- Multiple files in one invocation

Preprocess each input:

1. Read file content (PDF text extraction, HTML parsing, Markdown passthrough)
2. Extract metadata (Canvas URLs, dates, course codes from content)
3. Normalize (strip HTML styling, extract plain text from PDFs)

### Source identification

Identify HTML source type before extraction:

- __Canvas HTML__: URL contains `canvas.ust.hk`; has assignment metadata (title, due date, points, grade). Extract via `convert_canvas_submission`.
- __PRS/iClicker HTML__: URL contains `prsmob.ust.hk/ars/`; has question text and numbered answer choices. Extract quiz content directly — do not run `convert_canvas_submission`.
- __Generic HTML__: neither pattern. Extract readable text.

### Directory ingestion

When the input is a directory (or glob resolving to directories), scan recursively for supported file types. Group files by immediate parent directory — each subdirectory is a potential batch of related materials.

1. List all files recursively, filtering to supported extensions.
2. Group by immediate parent directory.
3. For each group, apply the classification decision tree to the group as a whole (not per-file), using the directory name as the primary classification hint.
4. Report the detected groupings before proceeding:

```text
Detected 5 groups in .pi/academic-ingest/:
  - "ELEC 1100 - quiz 0 (tutorial 1)" → 2 HTML files
  - "ELEC 1100 - quiz 1 (tutorial 2)" → 2 HTML files
  ...
Proceeding with ingestion for each group.
```

## Course resolution

1. __Extract from input:__ Canvas URL (course ID in path), file path (under `special/academia/<INST>/<CRS>/`), frontmatter tags
2. __Directory name parsing:__ When ingesting from a directory, parse the directory name for structural hints:
    - Pattern: `<COURSE> - <type> <N> (<binding> <M>)`
    - Example: `ELEC 1100 - quiz 1 (tutorial 2)` → course=ELEC 1100, type=quiz, number=1, binding=tutorial, target=2
    - Use the binding field to classify: tutorial → `tutorials/<name>/`, lab → `labs/<name>/`, etc.
    - Use the course field to resolve the institution and course directory.
    - This parsing is a hint, not a certainty — confirm with the user when the pattern is ambiguous.
3. __If ambiguous:__ list matching courses (name, institution, note count, last modified) and prompt user to pick
4. __If no match:__ ask user to specify institution and course code, or confirm creation of new course

## Splitting mixed-type materials

When a single input contains multiple content types (e.g., a PDF with lecture notes followed by a problem set), split it into separate materials before classification.

__When to split:__ Sections would route to __different__ CRUD skills (e.g., concept explanation → `topic-note` and exercises → `question`).

__When not to split:__ Sections would route to the __same__ skill (e.g., a question set with diagrams stays one material). A document that is primarily one type with minor supporting material (e.g., a topic note that briefly references a formula) is still a single material.

__How splitting works:__

1. Identify content boundaries (section headings, visual breaks, thematic shifts).
2. Create one material per distinct type, each carrying the same source file path and course context but a separate `rawContent` slice and its own `targetHint`.
3. Classify each material independently through the decision tree below.
4. Dispatch each to its appropriate skill sequentially.
5. Coordinate shared indexes (e.g., ensure `assignments/index.md` exists before adding to it).

After splitting, report what was detected:

```text
Detected mixed content in <filename>. Splitting into 2 materials:
  1. Lecture notes → <topic>.md
  2. Problem set → questions/<name>.md
```

The user can intervene if the split is incorrect (e.g., "Actually, treat the exercises as part of the lecture notes" → reclassify as single material).

## Classification decision tree

Classify by __target destination__ in the repository, not input type. Apply this tree to each material independently (after any splitting above).

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

When the classifier cannot determine the target with confidence, use a two-phase approach.

__Phase 1 — Category narrowing:__

Group candidate targets into three categories. If one category clearly dominates (score ≥ 2× the next), proceed to Phase 2 within that category. Otherwise present the top-level categories:

```text
I'm not sure how to classify this material. It looks like it could be:
1. Knowledge material (lecture notes, course logistics)
2. Assessment material (problem set, lab, assignment)
3. Support material (reference article, attachment)

Which category? [1/2/3]
```

__Phase 2 — Within-category narrowing:__

Once a category is selected (by the user or by confidence), present the specific target types within that category:

```text
Within knowledge material, this could be:
1. Topic note — standalone concept or theorem explanation
2. Course index — syllabus, schedule, or grading info

Which destination? [1/2]
```

Show at most __3 candidates__ per phase, each with a one-line description of why it fits. If the user says "none of these," fall back to free-text input where the user specifies the target type.

## Post-classification steps

After determining the target type for a material, apply these steps before dispatch.

### Missing data

Use `\[missing\]` when a field is present but its value is unknown or unavailable during partial-info ingestion. Do not invent or generate placeholder content for missing values. See [special.instructions.md](../../instructions/special.instructions.md#missing-data).

### 1. Existing-match check

Fuzzy-match the input content against existing notes of the __same target type__ within the resolved course:

- Course-index metadata → check existing `index.md` sections
- Topic notes → check existing `<topic>.md` files
- Submissions → check existing submissions in the matched directory
- Questions → check existing question pages

If a match is found, show the existing note and ask:

- __Update__ the existing note (merge new material into it)
- __Create new__ anyway (add as a separate note)
- __Cancel__

All types support partial information: you can create a note with minimal info and fill in details later. An existing match never overrides type classification — a problem set that shares words with a topic note is still classified as a question set.

### Multi-source merging

When multiple input files classify to the same target directory, merge rather than creating duplicate entries.

1. Identify shared target by matching directory name patterns (e.g., "quiz 1 (tutorial 2)" and "Quiz 01 (in Tutorial 02)" both target `tutorials/tutorial 2/`).
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

When the target is a submission (lab, tutorial, lecture), look up the matching session in the course `index.md` for reference. Do NOT copy schedule metadata into `<type>.yml` or `<type>.md` unless the source HTML explicitly provides it — schedule info belongs in the course `index.md`, not in the submission files.

### Source file disposition

After extracting content from HTML source files:

- Quiz questions → `tutorial.md` / `lab.md` / `lecture.md`
- Grade metadata → `tutorial.yml` / `lab.yml` / `lecture.yml`
- Canvas submission metadata → `submission.yml`
- Prompt PDFs, data files, images → `attachments/` (only actual media/data)
- Original HTML files → not stored in the repository

Do not copy extracted-content HTML into `attachments/`. The `attachments/` directory is for raw referenced files (PDFs, images, data, scripts), not for source documents whose content has been transcripted into markdown.

### Embedded image extraction

When extracting content from PRS/iClicker HTML, check for embedded base64 images (circuit diagrams, pinout diagrams, sensor illustrations). These are quiz-relevant assets and must be extracted:

1. Scan the HTML for `data:image/...;base64,...` URIs.
2. Discard tiny images (< 1 KB) — these are UI icons, not content.
3. Keep substantial images (> 1 KB) — these are likely circuit diagrams or figures referenced by quiz questions.
4. Use the original filename if available. If the image is a bare data URI with no filename, generate a descriptive filename reflecting the content (e.g., `req_circuit.jpg`, `l293_pinout.jpg`).
5. Preserve original alt text from the `<img>` tag if present. If alt text is missing or empty, generate a concise, humanized description of what the image shows (e.g., "Resistor network with 6, 12, 3, and 2 ohm resistors"). Do not use LaTeX math notation in alt text — use plain language descriptions instead.
6. Reference them in the quiz markdown with `![<alt text>](attachments/<name>.jpg)` inside the blockquote question.
7. List them in the `## attachments` section of both `<type>.md` and `index.md` (where applicable — in-class-only `index.md` omits `## attachments`).

### In-class component detection

When the input is a Canvas HTML for a lab, tutorial, or lecture that already has a `submission.yml` in its directory, ask the user whether this is the out-of-class or in-class Canvas page. The in-class page produces `lab.yml`/`tutorial.yml`/`lecture.yml` (not `submission.yml`) and creates a `lab.md`/`tutorial.md`/`lecture.md` content file as a child of `index.md`. That content file is Canvas-sourced, so it mirrors the Canvas header block of the submission `index.md`: frontmatter, `# <type>` heading, identity bullets, the Canvas metadata bullets drawn from the component YAML, and the verbatim Canvas description. Do not leave it as a bare stub; see `academic-crud-submission` for the exact format.

### 2. Attachment handling

If the material contains raw files (PDFs, images, data files, scripts) that are supplementary to the classified content type, use `academic-crud-attachments` to set up the attachments directory at the appropriate level. The material is still classified by its content type — attachments are metadata about how to store supporting files, not a content type themselves.

Attachment directory placement depends on the classified target:

- Topic note → `attachments/` inside the topic's directory
- Submission → `attachments/` inside the submission directory
- Question → `attachments/` inside the question's directory
- Course-level → `attachments/` at course root

This step is optional when no raw files accompany the material.

## Non-Canvas content templates

When the in-class content is not Canvas-sourced, use these templates instead of the Canvas header block format.

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

Use `![](attachments/<name>.jpg)` inside the blockquote when the question references a diagram. List the image in `## attachments` in both the content file and `index.md`.

One line per MC option. `solution` is required. `explanation` is optional — if omitted, remove the `- explanation:` line entirely.

### Cloze flashcards in question blocks

All question quote blocks must include cloze flashcards (`{@{ }@}`) on the `- solution:` and `- explanation:` lines. Do NOT add clozes to the question text or answer choices.

__Solution lines:__ ideally one cloze per solution — cloze the core result, formula, or decisive step. Only for very long solutions (multi-step derivations, lengthy prose) may multiple clozes appear, one per logical step.

__Explanation lines:__ prefer multiple clozes whenever possible — break the explanation into individual claims, conditions, and reasoning steps, each wrapped in its own cloze.

__Cloze syntax:__

- Closing delimiter is `}@}` (3 chars: `}` `@` `}`)
- For LaTeX math: `{@{content $LaTeX math$}@}` — the trailing `$` closes the math, then `}@}` closes the cloze
- For plain text: `{@{content plain text}@}` — closing is `}@}`
- Delegate cloze creation to a dedicated subagent using the `create-flashcards` skill when adding flashcards to multiple questions

Separate consecutive blockquote questions with `<!-- markdownlint MD028 -->`. Strip PRS UI chrome (navigation, error messages, "Pull down to refresh", "Your response is submitted") — keep only question text and answer choices. Preserve LaTeX math notation from the original.

## Dispatch

Route to the correct `academic-crud-*` skill with preprocessed context:

```json
{
  rawContent: <extracted text>,
  metadata: <Canvas metadata, dates, course codes>,
  sourceType: <pdf|html|markdown|text|image>,
  filePath: <original file path>,
  targetHint: <classification result>
}
```

## Post-dispatch

After the dispatched skill completes:

1. Run validation on the created/modified file
2. Report what was created/updated with file paths
3. Suggest next steps (e.g., "Add flashcards", "Update index")

> __Legacy patterns:__ If you encounter deprecated content structures (flat `questions.md`, flat assignment directories, `transcripts/`), consult the `academic-deprecated` skill for migration guidance. Deprecated pattern detection is not part of ingestion classification — it is a separate maintenance concern.

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

Attachment setup uses `academic-crud-attachments` as a post-classification helper for any target type that includes raw files.

## References

- All `academic-crud-*` skills for dispatch targets
- `academic-crud-attachments` for attachment directory setup
- `academic-deprecated` for legacy pattern migration
- `create-flashcards` for flashcard markup guidance
- `academic-lint` for validation
