---
name: Academic notes conventions
description: Guidelines and automated checks for files under special/academia (institution-agnostic)
applyTo: "special/academia/**,private/special/academia/**"
---

# Academic notes instruction

The authoritative long-form policy lives in `.agents/skills/academic-notes/SKILL.md`. Read it before acting. This file only contains cross-cutting rules that must auto-load.

- Read `../skills/academic-notes/SKILL.md` before acting.
- Read `../skills/academic-notes/course-template.md` as the scaffold for new course indexes.
- The validator is at `.agents/skills/academic-notes/check.py`; run `uv run .agents/skills/academic-notes/check.py <path>` to validate the smallest relevant scope after editing.

## Cross-cutting rules

- Use underscore-normalized flashcard tags: `flashcard/active/special/academia/HKUST/COMP_3031`.
  Spaces → underscores; keep consistent with institution/course code formatting.
- Do not put instructor or TA names or email addresses in course notes.
- Course-local `AGENTS.md` files must use heading `# <course code> agent instructions` and must not contain flashcard markup.
- Do not use chapter numbers as durable references in prose, flashcards, routes, or agent guidance. Use topic names and in-repo section links instead.
- Prefer QA cards for topic notes; cloze only inside embedded accounting journal-entry worked examples.
- Questions-page solutions use cloze `{@{ }@}`, not QA cards.
- When changing a topic note, update its prose, flashcards, and every affected `index.md` section link in the same task.

## Tools

- Skill: `.agents/skills/academic-notes/`
- Template: `.agents/skills/academic-notes/course-template.md`
- Validator: `.agents/skills/academic-notes/check.py`

## Reference

- [assignment-creation](../skills/assignment-creation/SKILL.md) — for assignment-style leaf indexes (labs, homework folders)
- [special.instructions.md](special.instructions.md) — general special/ conventions
