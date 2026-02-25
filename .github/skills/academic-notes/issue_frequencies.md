# Academic notes — Validator issue frequencies

This file summarizes validator findings (run with `--content`) across `special/academia/*` to help prioritize fixes and guide authors.

Example run used (HKUST snapshot):

```shell
python .github/skills/academic-notes/validate_academic.py --content special/academia/HKUST
```

Summary (example issue instances found):

- total issue instances: 265

Top issue classes (by frequency):

1. index missing 'children' section — 74
   - Note: many course `index.md` files omit an explicit `children:` YAML list. Adding `children:` improves navigation and automated indexing.

2. missing flashcard activation tag in 'tags:' — 65
   - Note: course files should include a `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` tag in frontmatter so flashcard tooling recognizes them.

3. appears to include 'week' entries but no 'datetime:' found — 65
   - Note: Session/week entries often mention `week` or use inline `topic ::@::` forms; prefer adding `datetime:` (ISO interval) per session for schedule/automation.

4. index.md missing '# index' heading — 61
   - Note: Many assignment or sub-index files lack the leading `# index` heading. Keeping it maintains consistent chronology and parsing.

Additional advisory warnings that frequently appear include:

- sessions marked `status: unscheduled` that also include a `topic:` field.
- exam sections placed before regular lecture/lab/tutorial entries.
- duplicate week numbers (often around holidays).
- semester headings in institution indexes that are out of chronological order.
- lines containing more than one `::@::` or `:@:` separator; cards should use a single separator.
- `<br/>` breaks written without a preceding space, which often occurs in bibliographic
  glosses and can break rendering.

Guidance for authors and agents

- When creating or editing course `index.md` files, start with `# index`, include a `children:` YAML key listing child pages in teaching order, and ensure `tags:` contains the course flashcard activation tag.
- For weekly/session notes, include `datetime:` in ISO interval format where possible. If exact times are unknown, include at least the date or a short ISO interval with a best-effort time.
- Preserve inline glosses (`::@::`) and taxonomy chains; when normalizing, suggest converting single-line `takeaway ::@:: X` to a structured `takeaway:` in a PR rather than mass-automating.

This file is generated from a validator run and should be updated periodically as notes are improved.
