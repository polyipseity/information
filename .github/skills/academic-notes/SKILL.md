---
name: academic-notes
description: Content-first conventions, examples, and light tooling for authoring and validating academic course notes across institutions (HKUST, other universities, colleges).
---

# Academic notes — skill overview

This skill documents content-first conventions and lightweight tooling for maintaining course notes across academic institutions. The guidance applies to notes from any university, department, or course collection under `special/academia/`.

> ⚠️ Important — evolving skill & long-term feedback
>
> This skill captures subtle, content-first conventions that take time and iterative feedback to apply well. The guidance and tools evolve — please treat the skill as a living document. Agents and maintainers MUST solicit, record, and incorporate user feedback into the instructions over time. See the continuous improvement workflow for how to submit feedback, track action items, and propose small, reviewable changes: `./continuous_improvement.md`.

Key responsibilities:

- Provide clear, content-first authoring guidance (learning outcomes, takeaways, worked examples).
- Maintain examples and normalization recommendations for common inline idioms (inline glosses, taxonomy chains, takeaway shorthand).
- Provide helper scripts to assist with linking canonical `general/` pages (Wikipedia title suggestions) and a lightweight validator to surface missing metadata.

Governance & constraints:

- Do NOT create or edit `general/` files automatically. Agents should only propose links to `general/` and leave file creation to designated maintainers.
- Flashcard activation tags are required in course note files; pattern: `flashcard/active/special/academia/<INSTITUTION>/<PAGE>` (case-insensitive). Validators will flag missing tags.
- Use the validator in `--content` mode for advisory checks; treat results as suggestions unless a maintainer requests strict enforcement.

Location of skill artifacts:

- `.github/skills/academic-notes/` — documentation, examples, and validator/helper scripts.

When contributing changes to this skill, prefer small, reviewable PRs that explain normalization rationale and list affected files.
