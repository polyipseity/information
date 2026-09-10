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

## Course resolution

1. __Extract from input:__ Canvas URL (course ID in path), file path (under `special/academia/<INST>/<CRS>/`), frontmatter tags
2. __If ambiguous:__ list matching courses (name, institution, note count, last modified) and prompt user to pick
3. __If no match:__ ask user to specify institution and course code, or confirm creation of new course

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

### In-class component detection

When the input is a Canvas HTML for a lab, tutorial, or lecture that already has a `submission.yml` in its directory, ask the user whether this is the out-of-class or in-class Canvas page. The in-class page produces `lab.yml`/`tutorial.yml`/`lecture.yml` (not `submission.yml`) and creates a `lab.md`/`tutorial.md`/`lecture.md` content file as a child of `index.md`.

### 2. Attachment handling

If the material contains raw files (PDFs, images, data files, scripts) that are supplementary to the classified content type, use `academic-crud-attachments` to set up the attachments directory at the appropriate level. The material is still classified by its content type — attachments are metadata about how to store supporting files, not a content type themselves.

Attachment directory placement depends on the classified target:

- Topic note → `attachments/` inside the topic's directory
- Submission → `attachments/` inside the submission directory
- Question → `attachments/` inside the question's directory
- Course-level → `attachments/` at course root

This step is optional when no raw files accompany the material.

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
