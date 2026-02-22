---
name: academic-notes
description: Content-first conventions, examples, and light tooling for authoring and validating academic course notes across institutions (HKUST, other universities, colleges).
---

# Academic notes — skill overview

This skill documents content-first conventions, examples, and lightweight tooling
for authoring and validating academic course notes across institutions.  It is
intended for any course material stored under `special/academia/<INSTITUTION>`
(regardless of university, department, or subject).

The skill has three primary audiences:

1. **Content authors (humans or agents)** writing course pages, lecture notes,
   labs, tutorials, and assignments.
2. **Maintainers** who review submissions, normalize style, and ensure metadata
   quality across the repository.
3. **Automated tooling** (validators, helpers) that surface common issues and
   provide search assistance.

> ⚠️ **Important — evolving skill & long-term feedback**
>
> This skill captures subtle, content-driven conventions that emerge from
> many semesters of note-taking and peer review.  It evolves continuously; new
> patterns appear and old habits are corrected.  Treat the skill as a living
> document.  Agents and maintainers **MUST** solicit, record, and incorporate
> user feedback into the instructions over time.  See the continuous
> improvement workflow (`continuous_improvement.md`) for how to submit feedback,
> track action items, and propose small, reviewable changes.

## Core components

The `academic-notes` skill is implemented as a collection of markdown files and
Python scripts located under `.github/skills/academic-notes/`.  Key artifacts
include:

- **`SKILL.md`** — this overview and high-level guidance (current file).
- **`patterns.md`** — catalog of observed authoring patterns and preferred
  normalizations; use it when writing or reviewing notes.
- **`examples.md`** — numerous concrete snippets showing how to structure
  frontmatter, sessions, assignments, cross‑references, flashcard markup, etc.
- **`checklist.md`** — an author checklist summarizing required and recommended
  steps before committing course content.
- **`issue_frequencies.md`** — auto‑generated summary of validator warnings
  across the repository; useful for prioritizing improvements.
- **`flashcards.md`** — focused guidance on using `::@::` glosses and frontmatter
  tags to enable flashcard generation.
- **`continuous_improvement.md`** — describes the feedback loop and how to keep
  the skill up to date with real‑world course content.
- **`validate_academic.py`** — validator script; run with `--content` for
  advisory checks (see documentation block inside script).
- **`find_wikipedia.py`** — helper for searching Wikipedia and suggesting
  canonical titles when linking to `general/` pages.

Maintainers should periodically run the validator across `special/academia` and
update `issue_frequencies.md` to reflect common problems.

## Authoring guidelines (summary)

When you create a new course note or update an existing one, follow these
steps:

- Keep lecture/lab/tutorial sessions in strict chronological order by their
  `datetime` values; these entries may interleave.  Exam sections (midterm,
  final) should always appear **after** all other session types even if the
  dates overlap.  The validator now emits a warning when exams precede other
  sessions.
- For institution-level indexes, ensure semester headings (`### 2025 fall`, etc.)
  progress chronologically; the validator also checks this and warns if the
  sequence is out of order.

1. Start with the **course-template** (`course-template.md`); fill in aliases,
   tags (note the underscore convention for flashes), name, credits, and a
   brief description.
2. Add a `logistics` section with a nested grading `scheme:` block specifying
   weights for labs, exams, projects, etc.  Must include a `sections:`
   list containing lecture/tutorial/lab stream codes, venues, and weekly
   time patterns (see `patterns.md` for format).
3. Maintain a `children:` list in frontmatter or as a YAML section under the
   heading; keep child pages (lectures, labs, assignments) in teaching order.
4. Use the recommended session structure for lectures/labs/tutorials/exams
   (see examples).  Include `datetime:` entries with ISO intervals; if the time
   is unknown, at least provide the date portion.
5. Capture **content‑first details**: learning outcomes, takeaways,
   instructor emphasis, worked examples, and link to canonical `general/`
   articles for formal definitions.
6. Insert `::@::` glosses for flashcard-worthy facts; follow `flashcards.md`
   for best practices.
7. Run the validator (`validate_academic.py`) to catch missing metadata or
   structural issues; address warnings where practical.
8. Add assignments, questions, attachments, and other accessories in their
   designated subfolders and list them under `children`.
9. Use the author checklist (`checklist.md`) before committing to ensure
   nothing important is overlooked.

### Flashcard activation tags

Tags must follow the pattern

```text
flashcard/active/special/academia/<institution>/<page>
```

`<page>` normally mirrors the course code using underscores (`COMP_3031`).
Spaces should never be percent‑encoded in tags.  Validators flag missing or
malformed tags.  Flashcard state is regenerated with `uv run -m init generate`.

### Linking to general content

Course notes should **never** create or modify files under `general/`.
Instead, link to existing encyclopedia articles by name (percent-encoded).
Agents may use `find_wikipedia.py` to query titles and choose the best match.

### Content patterns and normalizations

Refer to `patterns.md` for a comprehensive list of idioms that appear in
existing notes, along with recommended normalizations.  Common patterns
include:

- Inline glosses using `::@::` to attach definitions and takeaways.
- Taxonomy or chain notation connecting related concepts with arrows.
- Takeaway shorthand lines that should be promoted to structured
  `takeaway:` fields.

When performing normalizations, prefer small, targeted PRs with human review.
Do not mass‑apply regex-based rewrites without explicit maintainer approval.

## Validator usage

The `validate_academic.py` script is the primary automation for this skill.
Run it with:

```bash
python .github/skills/academic-notes/validate_academic.py special/academia/HKUST
```

Use the `--content` flag to switch from strict linting to advisory mode.  The
script emits warnings for missing frontmatter keys, absent flashcard tags,
incorrect `datetime:` formats, exam placement, duplicate week numbers, and
other common mistakes.  It now also warns when a session marked
`status: unscheduled` still has a `topic:` field, or when semester headings are
out of order.  The output is intended to help authors self-correct; maintainers
may enforce particular rules as needed.

Example summary (see `issue_frequencies.md` for the latest global report):

- Missing `children:` YAML key.
- Course files without flashcard activation tags.
- Session entries lacking `datetime:`.

Issues are tracked and frequently updated in `issue_frequencies.md`.

## Continuous improvement

This skill is not static.  To keep it accurate and helpful:

- **Collect feedback** from users and agents.  Logs are stored under
  `.github/skills/academic-notes/reports/` (create the directory if needed).
- **Update the documentation** (`patterns.md`, `examples.md`, `checklist.md`)
  whenever a new idiom or frequently occurring issue is observed.
- **Extend the validator** when recurring errors are identified, making sure
  to exercise new rules via tests or sample files.
- **Publish issue frequency summaries** after each major validation run to
  highlight areas where authors consistently struggle.

See `continuous_improvement.md` for a formal workflow and example.

## Contributing changes

- Propose small, atomic PRs that modify one aspect of the skill or fix a
  specific normalization.  Include rationale and before/after examples.
- The skill directory may contain helper Python scripts (e.g. the validator
  or Wikipedia helper).  Tests for those scripts **should be placed in the
  `tests/` subdirectory of the skill itself** (`.github/skills/academic-notes/tests/`), not in the repo’s top-level `tests/` tree.  This keeps
  skill-specific checks close to the code they exercise while avoiding
  pollution of the global test namespace.
- Update or add tests in that skill-local tests folder when extending the
  validator script; don’t scatter academic-notes tests throughout the root
  `tests/` directory unless they are shared with other components.
- Run `pnpm run format` and `pnpm run check` before submitting, and ensure
  `pnpm run test` passes locally.
- When editing skill documentation itself, mention in the PR description that
  the change affects `academic-notes` and reference relevant issue numbers or
  feedback notes.

By continually refining this skill, we can ensure that academic course notes
remain a useful, high-quality resource across the repository.
