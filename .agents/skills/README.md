# .agents/skills — agent skill catalog (README.md)

Each skill is one `SKILL.md`: a name, a description, and instructions an agent can follow. This file is the index — the academic skills in one table, then the rules for adding a new one.

## Adding a skill

1. Write `SKILL.md` with YAML frontmatter. The __only__ supported keys are:
   - `name` (required)
   - `description` (required)
   - `argument-hint`
   - `compatibility`
   - `disable-model-invocation`
   - `license`
   - `metadata`
   - `user-invocable`

   > __Note:__ the `applyTo` key is no longer supported in skill frontmatter. Older skills may still include it, but new skills should omit it entirely, or the validator will raise an error. Other keys are ignored and may prevent the skill from loading.

2. Do not invent fields beyond that list.
3. Update `AGENTS.md` and `.agents/instructions` where relevant.

## Academic skills

The `academic-*` skills handle all academic material ingestion:

| Skill | Purpose |
| --- | --- |
| `academic-ingest` | Dispatcher — classify input, resolve course, route to CRUD skill |
| `academic-vision` | Look at images the material carries: classify a figure, read what only the picture shows, verify a drawing or crop before it reaches a note |
| `academic-video` | Read a linked video's content from its subtitles, defer the ones without them, and ask the user to have those watched before the run ends |
| `academic-lint` | Validate academic notes after edits (wraps main.py) |
| `academic-crud-course-index` | Top-level `index.md`, exams, logistics |
| `academic-crud-index` | Sub-directory `index.md` (shared utility) |
| `academic-crud-submission` | Labs, tutorials, lectures, assignments |
| `academic-crud-topic-note` | Standalone concept and lecture notes |
| `academic-crud-question` | Problem sets, iPRs, quizzes |
| `academic-crud-agents` | Course-level `AGENTS.md` files |
| `academic-crud-attachments` | Attachments directories at any level |
| `academic-crud-transcludes` | Wikipedia articles included by reference |
| `academic-deprecated` | Deprecated patterns (documentation-only) |

The `academic-lint/` folder holds the validator (`main.py`, `main_mods/`) and tests (`tests_a7392be/`). The Wikipedia helper (`find_wikipedia.py`) lives in `academic-crud-topic-note/`, and the scaffold template (`course-template.md`) lives in `academic-crud-course-index/`.

## Running commands safely (avoid polluting skill folders)

Some skill folders contain a `pyproject.toml` for tool configuration (for example, `ty` type-checker settings). Running `uv run`, `uv sync`, or any `uv` command __inside__ a skill folder makes `uv` create a `.venv/` directory and `uv.lock` file there, cluttering the folder and duplicating the project environment. __Never run `uv` commands from inside a skill folder__; run from the workspace root and pass skill paths as arguments.

Running from the workspace root is not sufficient by itself: `uv run <script>` resolves the project from the __script's__ directory, so a skill script picks up that skill's dependency-free `pyproject.toml`, builds a per-skill environment, and fails on third-party imports. Invoke skill scripts through the workspace interpreter, `uv run python <script> ...`, so the environment comes from the workspace root:

- Tests: `uv run pytest .agents/skills/academic-lint/tests_a7392be/`
- Validator: `uv run python .agents/skills/academic-lint/main.py "special/academia/..."`
- Wikipedia titles: `uv run python .agents/skills/academic-crud-topic-note/find_wikipedia.py "<query>"`

This applies whether the command is run by an agent or a human. If you accidentally create `.venv` or `uv.lock` inside a skill folder, delete them immediately (`rm -rf .agents/skills/*/.venv .agents/skills/*/uv.lock`).
