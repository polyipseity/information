---
description: "Use when ingesting multiple files from a directory. Scans, classifies, merges, and creates submission pages in batch."
name: "Batch academic ingestion"
applyTo: "**"
alwaysApply: false
---

# Batch academic ingestion workflow

When ingesting multiple files from a directory, follow this workflow instead of processing files one-by-one.

## 1. Scan

List all files recursively, group by immediate parent directory. Each subdirectory is a batch targeting one destination.

```text
Detected 5 groups in .pi/academic-ingest/:
  - "ELEC 1100 - quiz 0 (tutorial 1)" → 2 HTML files
  - "ELEC 1100 - quiz 1 (tutorial 2)" → 2 HTML files
  ...
```

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

Look up each session in the course `index.md` for datetime, venue, and topic.

## 5. Merge

When multiple source types target the same directory, assign contributions:

- PRS HTML → quiz content → `tutorial.md`
- Canvas HTML → grade metadata → `tutorial.yml`
- PDF prompt files → `attachments/` (only actual media/data)
- Source HTML files → __discarded after extraction__ (not stored in repo)

## 6. Create

For each target directory, in dependency order:

1. Create directory structure (`index.md`, component YAML, content file, `attachments/`)
2. Write component YAML first (`tutorial.yml`, `submission.yml`)
3. Write content file (`tutorial.md`) with extracted quiz questions
4. Write `index.md` with metadata and children link
5. Copy only actual media/data to `attachments/` (PDFs, images, data files)

Do not copy HTML source files into `attachments/`.

## 7. Update

Add child links to parent indexes (`tutorials/index.md`, course `index.md`).

## 8. Validate

Run `academic-lint` on all created/modified files.

## 9. Report

Summarize what was created, with file paths and any issues.

```text
Created 5 tutorial submissions:
  - tutorials/tutorial 1/ (2 quiz questions, ungraded)
  - tutorials/tutorial 2/ (1 quiz question, grade: 2/2)
  - tutorials/tutorial 3/ (2 quiz questions, grade: 1/2)
  - tutorials/tutorial 6/ (2 quiz questions, grade: 2/2)
  - tutorials/tutorial 7/ (2 quiz questions, grade: 1/2)
Updated course index.md with tutorials/ link and quiz references.
```
