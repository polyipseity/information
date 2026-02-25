---
name: Academic notes conventions
description: Guidelines and automated checks for files under special/academia (institution-agnostic)
applyTo: "special/academia/**,private/special/academia/**"
---

# Academic notes instruction

This instruction file surfaces the essential, quick-reference guidance from the `academic-notes` skill for agents and maintainers working on course folders under `special/academia` (including the private mirror path `private/special/academia`). **Agents must read every file in `.github/skills/academic-notes/` and every line of those files before acting; do not assume the concise guidance is exhaustive.** It is intentionally concise — consult the full skill docs for examples and tooling.

## Scope & purpose

- Applies to: `special/academia/**` and mirrored `private/special/academia/**` course folders.
- Purpose: give agents a compact checklist for authoring, validating, and triaging course notes using the `academic-notes` conventions and helpers.

## Quick guidance for agents

- Do NOT create or edit `general/` files automatically. Suggest canonical Wikipedia titles (use the helper) and leave `general/` edits to maintainers.
- Require a flashcard activation tag in course files: `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` (case-insensitive). The validator will flag missing tags. Notes may use any of the three markup types – cloze `{@{ }@}`, two-sided `::@::`, or one-sided `:@:` – but remember that the latter two must stay on a single line.
- Use the validator conservatively: run `validate_academic.py --content` for advisory guidance; it will flag missing tags, exams before sessions, duplicate week numbers, unscheduled sessions carrying topics, out-of-order semester headings, and similar structural issues. Treat its output as suggestions unless maintainers request strict enforcement.
- Treat submodules (including `private/`, `tools/pytextgen/`, `tools/pyarchivist/`) as read-only unless the user explicitly grants permission.
- Prefer small, reviewable changes to skill docs and helper scripts; document rationale and link to the continuous improvement note when proposing edits.

## Tools & locations

- Skill docs, examples, and helper scripts: `.github/skills/academic-notes/`
- Validator: `.github/skills/academic-notes/validate_academic.py`
- Wikipedia helper: `.github/skills/academic-notes/find_wikipedia.py`
- Continuous improvement workflow: `.github/skills/academic-notes/continuous_improvement.md`

## Short author checklist

1. Add YAML frontmatter including `title`, `aliases`, `tags:` (must include the `special/academia/<INSTITUTION>` tag).
2. Add or confirm flashcard activation tag in `tags:` when flashcards are desired.
3. Ensure `index.md` pages contain `# index` and a `children:` or `## children` section where appropriate.
4. For weekly pages, include `datetime:` ranges and concise `topic:` / `learning_outcomes:` or `takeaway:` entries.
5. Run `python .github/skills/academic-notes/validate_academic.py --content <path>` and resolve obvious authoring omissions before opening a PR.

## Continuous improvement

This instruction set and the skill are living artifacts. If you discover missing examples, ambiguous rules, or repeated validation warnings, follow the steps in `continuous_improvement.md` to record feedback, draft a minimal clarification, and present it for maintainer review.

## Developer tooling & tests (academic notes)

- When adding tooling or scripts that process academic notes (for example, LMS converters), include unit tests and integration tests that exercise representative course pages and edge cases (missing metadata, unexpected frontmatter). Place tests in the skill’s own `tests/` subfolder (`.github/skills/academic-notes/tests/`); mirroring paths inside that directory (e.g., `tests/tools/test_convert_canvas.py`) keeps them close to the code they exercise and avoids cluttering the repository-level `tests/` tree.
- Validators updated for academic notes must come with tests that assert expected warnings and validation results. Run `pnpm run check` and `pnpm run test` locally before proposing CI changes; when working on a subset of files, supply explicit paths to these commands so they complete faster than scanning the whole repo.
