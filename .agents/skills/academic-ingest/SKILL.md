---
name: academic-ingest
description: Single entry point for all academic material ingestion. Accepts files, clipboard text, or pasted content; classifies the target destination in the repository and dispatches to the appropriate academic-crud-* skill.
---

# Academic Ingest

Single entry point for all academic material ingestion. Accepts files (PDF, HTML, Markdown, images), clipboard text, or pasted content. Classifies the target destination, resolves the target course, and dispatches to the appropriate `academic-crud-*` skill.

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

## Classification decision tree

Classify by __target destination__ in the repository, not input type.

```text
Input
│
├─ User specifies target type?
│  ├─ Yes → use it directly
│  └─ No → auto-classify ↓
│
├─ Content belongs to existing note? (fuzzy match)
│  ├─ Yes → confirm with user → update existing via appropriate crud skill
│  └─ No → classify target ↓
│
├─ Course-level metadata? (syllabus, schedule, grading, exam scores/stats/reports)
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
│  │  ├─ Unbound (PS, HW, project) → academic-crud-submission (assignments/<name>/)
│  │  └─ Ambiguous → prompt user to pick directory
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
├─ Attachments? (raw files: PDFs, images, data, scripts at any level)
│  ├─ Yes → academic-crud-attachments (attachments/<file>)
│
├─ Wikipedia articles for reference? (transcludes/ directory)
│  ├─ Yes → academic-crud-transcludes (transcludes/<article>.md)
│
├─ Deprecated pattern? (flat questions.md, flat assignment dirs, transcripts/)
│  ├─ Yes → warn user, suggest migration, route to active skill
│
└─ Unclear → prompt user with candidates
```

### Ambiguity resolution

When the classifier cannot determine the target, present candidates:

```text
This looks like it could be:
1. A lecture topic note (concept explanation, no submission)
2. A lecture-bound submission (has due date, attachments)
3. A question set (practice problems, no submission)

Which destination? [1/2/3]
```

## Duplicate detection

Before dispatching to a Create operation:

1. Fuzzy-match the input title against existing notes in the resolved course
2. If a match is found, show the existing note and ask:
   - Update the existing note (merge new material)
   - Create a new note anyway
   - Cancel

## Multi-skill coordination

When input contains multiple material types (e.g., lecture slides + problem set):

1. Classify each input independently
2. Dispatch to each appropriate skill sequentially
3. Coordinate shared indexes (e.g., ensure `assignments/index.md` exists before adding to it)

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

## Skills dispatched to

| Target | Skill |
| --- | --- |
| Top-level `index.md`, exams, logistics | `academic-crud-course-index` |
| Sub-directory `index.md` | `academic-crud-index` |
| `<topic>.md` standalone notes | `academic-crud-topic-note` |
| Submission pages (labs, tutorials, lectures, assignments) | `academic-crud-submission` |
| Question pages (no submission) | `academic-crud-question` |
| `AGENTS.md` | `academic-crud-agents` |
| Attachments at any level | `academic-crud-attachments` |
| Wikipedia transcludes | `academic-crud-transcludes` |
| Deprecated patterns | `academic-deprecated` (warn only) |

## References

- All `academic-crud-*` skills for dispatch targets
- `create-flashcards` for flashcard markup guidance
- `academic-lint` for validation
