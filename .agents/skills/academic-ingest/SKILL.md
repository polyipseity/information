---
name: academic-ingest
description: Single entry point for all academic material ingestion. Accepts files, clipboard text, or pasted content; classifies the target destination in the repository and dispatches to the appropriate academic-crud-* skill.
---

# Academic Ingest

Single entry point for all academic material ingestion. Accepts files (PDF, HTML, Markdown, images), clipboard text, or pasted content. Classifies the target destination, resolves the target course, and dispatches to the appropriate `academic-crud-*` skill.

Apply the classification to __each material independently__. A single invocation may produce multiple independent classifications, each dispatched to its own skill.

## Scope guardrails

__Hard rule: create only what the source material warrants.__ The classification decision tree determines the target __type__, but the source content determines __how much__ to create. A generic HTML course homepage is course-level metadata — it produces only the course `index.md`. It does NOT produce lab directories, homework folders, session entries, or any other scaffolding unless the source explicitly provides that content.

| Source type | Creates | Does NOT create |
| --- | --- | --- |
| Course homepage (generic HTML) | Course `index.md` only | Subdirectories, sessions, assignments |
| Canvas assignment page | Submission leaf (`index.md` + YAML) | Course-level sessions, other submissions |
| PRS/iClicker quiz HTML | In-class content file (`<type>.md`) | Course-level metadata, submission YAML |
| Canvas announcement | Blockquote in matching session | New sessions, new files |

__Lectures, labs, and tutorials are separate.__ A course homepage lists lecture sections, lab sections, and tutorial sections independently under `## logistics`. They are distinct session types with different section-type names and section keys:

- `lecture` sections: keys `L1`, `L2`, `L3` (2-3 per week typical)
- `labs` sections: keys `LA1`, `LA2`, `LA3` (1 per week typical)
- `tutorials` sections: keys `T1`, `T2`, `T3` (1 per week typical)

Never conflate them into a single type, create joint session entries, or mix types within a week heading. `## logistics` lists the enrolled sections with their venues and times; every session that actually meets gets its own `## week N <type>` heading in the course `index.md`. A course with 2 lectures + 1 lab + 1 tutorial per week therefore has 4 session headings per week, not 4 entries in `## logistics` — see "Session ordering" in `academic-crud-course-index`.

__When in doubt, create less.__ Scaffolding for future content (labs, assignments, tutorials) should only appear when:

1. The source material explicitly enumerates items (e.g., "Lab 1, Lab 2, Lab 3"), OR
2. The user explicitly requests it.

A course homepage that mentions "labs" as a grading component does NOT warrant creating a `labs/` directory.

__Never write current status or provenance.__ What has been ingested so far, what still remains, and how a derived value was established all go stale on the next ingest. Omit them; prefer less content whenever possible.

__Structure comes from the content, not the source.__ A source's layout never decides which notes or sections exist. Extracted text is raw material: its concepts define the file boundaries and the section boundaries, and its own headings are renamed to the sub-concepts they carry. A lecture deck must not produce a note about a lecture — see the merge and split tests in `academic-crud-topic-note`.

## Source file preservation

__Hard rule: ingestion never deletes, moves, renames, or truncates a source file.__

The rule is about the __file__, not the folder. Sources arrive wherever the user put them — an ad-hoc ingest directory, a downloads folder, an attachments directory, a path passed on the command line, or a location outside the repository entirely. No location is privileged, special-cased, or exempt.

- Leave every source byte-identical at its original path after ingestion completes.
- Do not delete a source because its content was "not stored in the repository". "Not stored" means __not copied into the tracked content tree__ (`special/academia/...`). It never authorises deleting the original.
- Do not move, rename, or truncate a source to tidy up, deduplicate, or mark it as processed.
- `.extracted/` outputs are additions beside a source, never replacements for it. Never remove a source to "clean up" after extraction.
- Disposing of ingested sources is the user's decision. If cleanup looks desirable, ask — do not act.

## Convention authority

Every ingestion convention lives in these skills and instructions. Do not infer a convention by inspecting another course's content — a sibling course may be wrong, stale, or atypical, and copying it propagates the error.

When a convention is missing or ambiguous, say so and report it as a skill defect. Do not fill the gap by imitating content you found elsewhere in the repository, and do not invent a format.

## Document extraction (mandatory)

__Hard rule: run this before classifying anything.__ A document is not "read" until it has been extracted with the repository extractor:

```bash
uv run -m scripts.special.convert_document <input> <output_dir>
```

`<output_dir>` is the `.extracted/` folder described below. Extraction happens __in place, next to the source__, whether or not the source lives inside the repository.

__Never substitute an ad-hoc extractor.__ `pdftotext`, a direct `pymupdf` call, `pdfplumber`, or any similar tool returns text only — no page images, no manifest, nothing to cache-check. These are not acceptable substitutes for `convert_document.py`, and using one is a skill violation even when the text looks correct.

__Post-conditions__ — do not proceed to classification until all hold:

- `text.md` exists and is nonempty
- `pages/` holds one image per page/slide
- `manifest.json` records the source SHA-256, format, page count, and timestamp
- The recorded page count matches the source document

__Full coverage__: every page must be accounted for. Page text ends up in the note or its attachments; page images carrying figures the prose depends on are referenced from the note. A note that silently drops pages is an incomplete extraction, not a summary. If a source has no extractable text (scanned images only), say so explicitly and work from the page images.

Document-like formats (PDF, DOCX, PPTX) produce extraction outputs that are persisted near the source:

- __Single file input__: `<stem>.extracted/` sibling folder (e.g., `lecture.pdf` → `lecture.extracted/`)
- __Directory input__: `.extracted/` subfolder inside the directory (e.g., `materials/` → `materials/.extracted/`)

Each `.extracted/` folder contains:

- `text.md` — extracted markdown text
- `pages/` — page/slide PNG images at 150 DPI
- `manifest.json` — source file hash, format, page count, timestamp

__Cache check__: Before running `convert_document.py`, check if `.extracted/` exists with a valid `manifest.json` matching the source file's SHA-256 hash. If valid, reuse the cached extraction. Use `--force` to re-extract.

`.extracted/` is a derived artifact — not tracked in `index.md` `## children`, not linked from content files. Safe to delete and re-extract. This applies to `.extracted/` alone, never to the source document — see "Source file preservation".

## Input handling

Accept any combination of:

- File paths (PDF, HTML, Markdown, images)
- Clipboard content (`--clipboard` or pasted text)
- Inline text from the user
- Multiple files in one invocation

Preprocess each input:

1. Read file content:
   - HTML: parse and extract readable text (see Source identification above)
   - Markdown: passthrough
   - Images: pass to vision model if vision-aware, otherwise describe limitations
   - Documents (PDF, DOCX, PPTX): extract per "Document extraction (mandatory)", then classify role (content vs attachment) per "Document format handling"
2. Extract metadata (Canvas URLs, dates, course codes from content)
3. Normalize (strip HTML styling, extract plain text from PDFs)

### Source identification

Identify HTML source type before extraction:

- __Canvas HTML__: URL contains `canvas.ust.hk`; has assignment metadata (title, due date, points, grade). Extract via `convert_canvas_submission`.
- __Canvas announcement__: URL contains `canvas.ust.hk` and page type is "Topic" (discussion/announcement). Has a title and body text but no grade/submission metadata. Extract title and body verbatim (omit author name and platform chrome like "This topic is closed for comments").
- __PRS/iClicker HTML__: URL contains `prsmob.ust.hk/ars/`; has question text and numbered answer choices. Extract quiz content directly — do not run `convert_canvas_submission`.
- __Generic HTML__: neither pattern. Extract readable text.

### Document format handling (PDF, DOCX, PPTX)

Document-like formats are NOT opaque. Extraction is mandatory and runs before classification — see "Document extraction (mandatory)" for the command, the cache check, and the post-conditions. After extraction, classify the document:

1. __Vision-awareness check__: Before processing, determine if the current model accepts image inputs. Check `PI_MODEL` and `PI_PROVIDER` environment variables.
   - __If vision-aware__: The agent can directly read page images to understand visual content (diagrams, formulas, handwritten annotations, layout). Use both text and images during classification and content extraction.
   - __If NOT vision-aware__: Rely on extracted text only. Page images are persisted in `.extracted/pages/` for future reference or manual review, but the agent cannot interpret them during ingestion.

2. __Role classification__ (after extraction, before dispatch): Determine whether the document is __content__ or an __attachment__:
   - __Content document__: The document IS the course material (lecture slides, topic notes, exam paper). Disposition: extracted text → `.md` file; page images → `attachments/pages/`; original file → left in place at its original path, not copied into the repository (the `.md` + images are canonical).
   - __Attachment document__: The document ACCOMPANIES course material (prompt PDF, reference data, supplementary reading). Disposition: original → `attachments/`; page images → `attachments/pages/` only when visual content needs inline reference; extracted text → used during agent processing but not persisted as a separate `.md` (the original is canonical).
   - __When ambiguous__: Ask the user — "Is this document the course content itself, or a file that accompanies the content?"

3. __Ensure `.gitignore`__: When creating an `.extracted/` folder, create a `.gitignore` inside it containing `*` to ignore all cached contents. This prevents extraction outputs from being committed.

### Directory ingestion

When the input is a directory (or glob resolving to directories), scan recursively for supported file types. Group files by immediate parent directory — each subdirectory is a potential batch of related materials.

For a multi-group input, follow `.agents/prompts/academic-ingest-batch.prompt.md` rather than working through files one at a time. That prompt is the single source of truth for the batch steps — do not restate them here.

1. List all files recursively, filtering to supported extensions.
2. Group by immediate parent directory.
3. For each group, apply the classification decision tree to the group as a whole (not per-file), using the directory name as the primary classification hint.
4. Report the detected groupings before proceeding:

```text
Detected 5 groups in <ingest directory>/:
  - "ELEC 1100 - quiz 0 (tutorial 1)" → 2 HTML files
  - "ELEC 1100 - quiz 1 (tutorial 2)" → 2 HTML files
  ...
Proceeding with ingestion for each group.
```

## Course resolution

1. __Extract from input:__ Canvas URL (course ID in path, used only to resolve the course — never record platform links in the target notes), file path (under `special/academia/<INST>/<CRS>/`), frontmatter tags
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

### Topic note naming (mandatory when the target is a topic note)

Fix the name before creating or renaming any `<topic>.md`. This is required, not stylistic — see "Topic note naming" in `academic-crud-topic-note` for the full rules.

```bash
uv run python .agents/skills/academic-crud-topic-note/find_wikipedia.py "<concept>"
```

The filename stem and the H1 title are the same sentence-case string: `operating system`, never `Operating System`. No lint rule inspects the H1 title or the filename, so a title-case name passes validation silently.

### Missing data

__Hard rule: always use `\[missing\]`.__ When a field is present but its value is unknown or unavailable during partial-info ingestion, write `\[missing\]` as the value. This is the ONLY acceptable placeholder. Never use:

- bare `none`, `N/A`, `TBD`, `?`, or empty strings
- `\(none\)` for non-statistics fields (that format is reserved for exam statistics)
- invented values ("TBA", "upcoming", "not yet available")

The `\[missing\]` format is escaped so it does not create a wiki link in Obsidian. The brackets indicate "field exists, value absent" — distinguish this from omitting the field entirely (which means "field not applicable").

See [special.instructions.md](../../instructions/special.instructions.md#missing-data) for the full convention.

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

After extracting content from a source file, the extracted material lands as follows. Nothing in this list authorises deleting or moving the source — see "Source file preservation".

- Quiz questions → `tutorial.md` / `lab.md` / `lecture.md`
- Grade metadata → `tutorial.yml` / `lab.yml` / `lecture.yml`
- Canvas submission metadata → `submission.yml`
- Canvas announcement body → course `index.md` session entry (blockquote)
- Prompt PDFs, data files, images → `attachments/` (only actual media/data)
- Original HTML files → left in place at their original path; not copied into the repository
- Original document files (PDF, DOCX, PPTX) — see role classification:
    - Content documents: original left in place; the `.md` and `attachments/pages/` images are the canonical copy; never deleted
    - Attachment documents: copied into `attachments/` (raw file for provenance and re-extraction); source left in place
- Extracted page images — `attachments/pages/<stem>/` (referenced from content when visual content matters)
- Extracted text — content documents: `.md` file; attachment documents: ephemeral reference (original is canonical)
- `.extracted/` folders — derived cache artifacts, not tracked in `index.md`

Do not copy extracted-content HTML into `attachments/`. The `attachments/` directory is for raw referenced files (PDFs, images, data, scripts), not for source documents whose content has been transcripted into markdown.

### Embedded image extraction

When extracting content from PRS/iClicker HTML, check for embedded base64 images (circuit diagrams, pinout diagrams, sensor illustrations). These are quiz-relevant assets and must be extracted:

1. Scan the HTML for `data:image/...;base64,...` URIs.
2. Skip tiny images (< 1 KB) — these are UI icons, not content.
3. Keep substantial images (> 1 KB) — these are likely circuit diagrams or figures referenced by quiz questions.
4. Use the original filename if available. If the image is a bare data URI with no filename, generate a descriptive filename reflecting the content (e.g., `req_circuit.jpg`, `l293_pinout.jpg`).
5. Preserve original alt text from the `<img>` tag if present. If alt text is missing or empty, generate a concise, humanized description of what the image shows (e.g., "Resistor network with 6, 12, 3, and 2 ohm resistors"). Do not use LaTeX math notation in alt text — use plain language descriptions instead.
6. Reference them in the quiz markdown with `![<alt text>](attachments/<name>.jpg)` inside the blockquote question.
7. List them in the `## attachments` section of both `<type>.md` and `index.md` (where applicable — in-class-only `index.md` omits `## attachments`).

### Canvas announcement extraction

When the source is a Canvas discussion/topic page (title starts with "Topic:" or page structure indicates a discussion), extract the announcement content:

1. Extract the title (text after "Topic:" or the discussion heading).
2. Extract the body text verbatim, preserving line breaks and formatting.
3. Strip the author name, timestamp, and platform chrome ("This topic is closed for comments", "Sort by", navigation elements).
4. Match the announcement to the session where the related content lives. Assignment-related announcements go in the lecture entry that links the assignment (last lecture on or before due date). Activity-related announcements go in the matching lab or tutorial entry.
5. Place the title (bolded) and body as a blockquote after a `---` separator in the matched session entry's free text area (after the session metadata).
6. When multiple announcements target the same session, list them as separate blockquotes with a blank line between them.

Do NOT run `convert_canvas_submission` on announcement pages — they have no grade or submission metadata.

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
  sourceType: <pdf|html|markdown|text|image|document>,
  filePath: <original file path>,
  targetHint: <classification result>,
  documentRole: <content|attachment>,
  pageImages: <list of page image paths, if available>,
  extractionDir: <path to .extracted/ folder>
}
```

## Post-dispatch

After the dispatched skill completes:

1. __Humanizer pass.__ Rewrite the new prose and flashcards for verbosity before validating — see "Humanizer pass" below.
2. Run validation on the created/modified file
3. Add a link to the assignment in the last lecture entry on or before its due date in the course `index.md`
4. Report what was created/updated with file paths
5. Suggest next steps (e.g., "Add flashcards", "Update index")

### Humanizer pass

Every note this skill dispatches to gets a verbosity-reduction pass over __both the prose and the flashcards__, using the `humanizer` skill. Run it once the content is written and before `academic-lint`.

Cut, in order of payoff:

- openers that only announce the structure ("Three objects have to be kept apart", "There are two ways to obtain it")
- trailing justification clauses ("which is why…", "so that…", "which makes… possible")
- hedging, and appositives that restate their subject
- card prompts that repeat their own answer, and answers that repeat their prompt
- lists padded to three items

Keep every fact. Do not touch heading text (session entries link to `#section%20anchors`), flashcard markup (`{@{ }@}`, `::@::`, `:@:`), LaTeX, pytextgen fences, or anything quoted verbatim from the source.

The result should read as a short card prompt carrying the symbols needed to answer it with an answer of one or two clauses, and prose with one idea per sentence rather than a sentence announcing what comes next.

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
