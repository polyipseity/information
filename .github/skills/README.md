# .github/skills — agent skill catalog (README.md)

Purpose

- Provide a single place for human and agent discoverability of repository skills.
- Skill metadata is now stored directly in each `SKILL.md` document's YAML frontmatter.

Files

- `SKILL.md` — human-readable skill instructions (already present per-skill).

Guidelines for new skills

1. Add `SKILL.md` with YAML frontmatter. The **only** supported keys are:
   - `name` (required)
   - `description` (required)
   - `argument-hint`
   - `compatibility`
   - `disable-model-invocation`
   - `license`
   - `metadata`
   - `user-invocable`

  > **Note:** the `applyTo` key is no longer supported in skill
  > frontmatter.  Older skills may still include it, but new skills
  > should omit it entirely or the validator will raise an error.
   Other keys are ignored and may prevent the skill from loading correctly.

   Example: the newly added `flashcard-creation` skill uses only
   `name` and `description` plus optional explanatory text; no
   `applyTo` field appears.
2. Ensure the frontmatter contains the allowed keys listed above. Do not invent additional fields.
3. Update `AGENTS.md` and `.github/instructions` where relevant.

Why this exists

- Makes skills discoverable to agents and maintainers
- Enables automated checks in CI and reduces drift between human docs and metadata

If you want me to reorder, merge, or split skills I can apply the changes accordingly.

Migration note: `tools-templates` and `tools-special` were merged into `tools/SKILL.md` — cross-references were updated accordingly.
