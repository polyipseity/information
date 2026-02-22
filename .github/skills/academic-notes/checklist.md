# Academic notes author checklist (detailed)

Before committing a new or updated course note under `special/academia`, run through this checklist.

Required (must-have) ✅

1. YAML frontmatter exists and is delimited by `---` at top of file.
2. `aliases` include the canonical course code and a human-readable name (for `index.md`).
3. `tags` include `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` (required in course note files where flashcards are desired).
4. Do NOT create, modify, or edit files under `general/`. Course-note authors and agents must only edit files inside the course folder.
5. `# index` present for `index.md` files.
6. `## children` lists child pages in teaching order (or a `children:` YAML key).
7. Each `week` entry has `datetime` and `topic` (recommended to include timezone offset).
8. **Ordering rules**: lecture/lab/tutorial entries must follow chronological order; exams must come after all other sessions. In index files, semester headings should be chronologically ordered.

Recommended (helpful) ⚠️
8. Use `assignments/`, `questions/`, and `attachments/` subfolders for respective content.
9. Link to `general/` canonical pages instead of copying long definitions.
10. Filenames are friendly and human-readable; use spaces and percent-encode when needed for links.
11. Run `python .github/skills/academic-notes/validate_academic.py` to detect common errors; use `--content` for guidance on minimal content signals.

Content checklist (content-first guidance):
12. Each lecture/tutorial includes at least one `learning_outcomes:` bullet or a concise `takeaway:` line (recommended for easier revision).
13. Include at least one worked example or solution sketch for important techniques covered that week (recommended).
14. Link slides and recordings in `attachments/` or `attachments/index.md` when available (recommended).
15. Add `::@::` concise definitions for flashcard-worthy items and check `flashcards.md` rules (recommended).

Note on existing inline idioms:

- Many notes use `term ::@:: gloss` or `takeaway ::@:: ...` inline inside the session body. This is acceptable; prefer converting these into structured `- topic:` / `- takeaway:` / `learning_outcomes:` entries in a follow-up PR rather than making large automatic rewrites. When suggesting normalization, list affected files in the PR description so maintainers can review changes.

Commit-msg tip: include `academic-notes: add <INSTITUTION>/<COURSE> ...` for changes that modify course content or introduce new course notes.

Run the validator in content mode to get guidance on minimal content signals:

```bash
python .github/skills/academic-notes/validate_academic.py --content special/academia/<INSTITUTION>
```

See also: `issue_frequencies.md` for a recent frequency summary of validator findings and quick remediation notes (auto-generated from a validator run).
