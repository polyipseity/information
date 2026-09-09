# .agents/skills — agent skill catalog (README.md)

Purpose

- Provide a single place for human and agent discoverability of repository skills.
- Skill metadata is now stored directly in each `SKILL.md` document's YAML frontmatter.

Files

- `SKILL.md` — human-readable skill instructions (already present per-skill).

Guidelines for new skills

1. Add `SKILL.md` with YAML frontmatter. The __only__ supported keys are:
   - `name` (required)
   - `description` (required)
   - `argument-hint`
   - `compatibility`
   - `disable-model-invocation`
   - `license`
   - `metadata`
   - `user-invocable`

  > __Note:__ the `applyTo` key is no longer supported in skill frontmatter.  Older skills may still include it, but new skills should omit it entirely or the validator will raise an error.
   Other keys are ignored and may prevent the skill from loading correctly.

   Example: the `create-flashcards` skill uses only
   `name` and `description` plus optional explanatory text; no
   `applyTo` field appears.
2. Ensure the frontmatter contains the allowed keys listed above. Do not invent additional fields.
3. Update `AGENTS.md` and `.agents/instructions` where relevant.

Why this exists

- Makes skills discoverable to agents and maintainers
- Enables automated checks in CI and reduces drift between human docs and metadata

## Academic skills

The `academic-*` skills handle all academic material ingestion:

| Skill | Purpose |
| --- | --- |
| `academic-ingest` | Dispatcher — classify input, resolve course, route to CRUD skill |
| `academic-lint` | Validate academic notes after edits (wraps main.py) |
| `academic-crud-course-index` | Top-level `index.md`, exams, logistics |
| `academic-crud-index-page` | Sub-directory `index.md` (shared utility) |
| `academic-crud-submission-page` | Labs, tutorials, lectures, assignments |
| `academic-crud-topic-note` | Standalone concept and lecture notes |
| `academic-crud-question-page` | Problem sets, iPRs, quizzes |
| `academic-crud-agents` | Course-level `AGENTS.md` files |

The `academic-lint/` folder contains the validator (`main.py`, `main_mods/`), scaffold template (`course-template.md`), Wikipedia helper (`find_wikipedia.py`), and tests (`tests_a7392be/`).

## Running commands safely (avoid polluting skill folders)

Some skill folders contain a `pyproject.toml` for tool configuration (e.g., `ty` type-checker settings). Running `uv run`, `uv sync`, or any `uv` command __inside__ a skill folder will cause `uv` to create a `.venv/` directory and `uv.lock` file there, cluttering the folder and duplicating the project's actual environment.

__Never run `uv` commands from inside a skill folder.__ Always run from the workspace root and reference skill paths as arguments. Examples:

- Tests: `uv run pytest .agents/skills/academic-lint/tests_a7392be/`
- Validator: `uv run .agents/skills/academic-lint/main.py "special/academia/..."`

This applies regardless of whether the command is run implicitly by an agent or explicitly by a human. If you accidentally create `.venv` or `uv.lock` inside a skill folder, delete them immediately (`rm -rf .agents/skills/*/.venv .agents/skills/*/uv.lock`).
