---
description: "Use when ingesting multiple files from a directory. Scans, classifies, merges, and creates submission pages in batch."
name: "Batch academic ingestion"
applyTo: "**"
alwaysApply: false
---

# Batch academic ingestion workflow

When ingesting multiple files from a directory, follow this workflow instead of processing files one-by-one.

## 0. Preserve sources

__Never delete, move, rename, or truncate a source file.__ Extraction reads a source; it never consumes it. "Not stored in the repo" means not copied into the tracked content tree — it is not permission to delete anything. Disposal is the user's decision.

Document inputs (PDF, DOCX, PPTX) must be extracted with `uv run -m scripts.special.convert_document` per the `academic-ingest` skill. Do not substitute `pdftotext`, a direct `pymupdf` call, or `pdfplumber`.

## 1. Scan

List all files recursively, group by immediate parent directory. Each subdirectory is a batch targeting one destination.

```text
Detected 5 groups in <ingest directory>/:
  - "ELEC 1100 - quiz 0 (tutorial 1)" → 2 HTML files
  - "ELEC 1100 - quiz 1 (tutorial 2)" → 2 HTML files
  ...
```

The ingest directory is wherever the user placed the files. It is not fixed, and no location is privileged or exempt from the preservation rule above.

## 2. Identify

Classify each file's source type:

- __Canvas HTML__: URL contains `canvas.ust.hk` → assignment metadata, grades
- __PRS/iClicker HTML__: URL contains `prsmob.ust.hk/ars/` → quiz questions
- __PDF/image__: prompt files, data → `attachments/`
- __Generic HTML__: readable text

## 3. Parse

Extract course, session number, and binding from directory names:

- Pattern: `<COURSE> - <type> <N> (<binding> <M>)`
- Example: `ELEC 1100 - quiz 1 (tutorial 2)` → course=ELEC 1100, target=tutorials/tutorial 2/

## 4. Cross-reference

Look up each session in the course `index.md` for reference only. Do NOT copy schedule metadata into submission files.

## 5. Merge

When multiple source types target the same directory, assign contributions:

- PRS HTML → quiz content → `<type>.md`
- Canvas HTML → grade metadata → `<type>.yml` (via `convert_canvas_submission`)
- PDF prompt files → `attachments/` (only actual media/data)
- Source HTML files → __left in place at their original path__ (not copied into the repo)

## 6. Create

For each target directory, in dependency order:

1. Create directory structure (`index.md`, component YAML, content file, `attachments/`)
2. Write component YAML first (`<type>.yml`, `submission.yml`)
3. Write content file (`<type>.md`) with extracted quiz questions
4. Write `index.md` with submission and children only (no metadata section)
5. Copy only actual media/data to `attachments/` (PDFs, images, data files)

Do not copy HTML source files into `attachments/`.

## 7. Update

Add child links to parent indexes (`tutorials/index.md`, course `index.md`). Children-list format and order come from the `academic-crud-index` skill: folders first, then files, Python string order within each group.

## 8. Reconcile topic notes

Whatever the group's type — lecture, lab, or tutorial — compare the material against the course's existing topic notes and extend, prune, or leave each concept, or create the note that is missing. A `<type>.md` file is not the final home of a durable concept. See "Topic-note reconciliation (mandatory)" in the `academic-ingest` skill, and list the outcome for each note in the report.

## 9. Validate

Run `academic-lint` on all created/modified files.

## 10. Report

Summarize what was created, with file paths and any issues.

```text
Created 5 tutorial submissions:
  - tutorials/tutorial 1/ (2 quiz questions, ungraded)
  - tutorials/tutorial 2/ (1 quiz question, grade: 2/2)
  - tutorials/tutorial 3/ (2 quiz questions, grade: 1/2)
  - tutorials/tutorial 6/ (2 quiz questions, grade: 2/2)
  - tutorials/tutorial 7/ (2 quiz questions, grade: 1/2)
Updated course index.md with tutorials/ link and quiz references.
Reconciled topic notes:
  - voltage.md: extended (measuring voltage; ground reference)
  - Ohm's law.md: extended (resistor)
  - electric power.md: no change (already covered)
```
