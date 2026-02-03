# AGENTS

Personal Markdown knowledgebase with flashcards, tutorials, and archived online content.

## Quick reference

- **`general/`**: Wikipedia encyclopedia articles (verbatim, flashcard-enabled)
- **`special/`**: Coursework, tutorials, frameworks, language texts  
- **`archives/`**: Archived media and web content (Wikimedia Commons, sparse)
- **`tools/`**: Python scripts (init, convert wiki, pack, publish, templates)

**Git submodules**: `self/`, `private/`, `tools/pytextgen/`, `tools/pyarchivist/`

**Submodule hierarchy**: Innermost `AGENTS.md` takes priority. Many submodules (e.g., `self/ledger`) have their own `.github/instructions/` and `.github/skills/`.

## Quick start: Common workflows

**Creating notes**:

```bash
# Scaffold new wiki-sourced note (see wiki-ingestion skill)
python -m "templates.new wiki page"
python -m "convert wiki"  # Paste Wikipedia HTML from clipboard
python -m init generate <file>  # Generate flashcards from cloze markup
```

**Maintaining content**:

```bash
# Regenerate all generated blocks (see pytextgen skill)
python -m init generate -C  # Force cache rebuild

# Clear stale content before troubleshooting (see pytextgen skill)
python -m init clear --type CONTENT <optional-paths>
```

**Organizing & publishing**:

```bash
# Before packaging/publishing, regenerate everything (see tools skill)
python -m init generate -C

# Create PageRank-optimized bundle (see tools skill)
python -m pack -o pack.zip -n 25 --damping-factor 0.5 <paths>

# Mirror private→public filtered history (see tools skill)
python -m publish --paths-file paths.txt
```

For detailed workflows, see [core-workflows.instructions.md](.github/instructions/core-workflows.instructions.md).

## Dependencies

- Python 3.8+ with `requirements.txt` packages
- Node.js 24+ with `package.json` packages (commitlint, markdownlint)
- External: `git`, `git-filter-repo`
- Obsidian plugins: Extended MathJax (for `preamble.sty`)

## Setup

Install Node.js dependencies and activate Git hooks:

```bash
pnpm install
pnpm run prepare  # Activates husky hooks
```

**Tooling & scripts:** Prefer using `pnpm` script wrappers when available. Run `pnpm run <script>` from the repository root to ensure project-local tools and the lockfile are used.

Common scripts (see `package.json`):

- `pnpm run check` — repository checks (runs `check:md`)
- `pnpm run format` — formatting helpers (runs `format:md`)
- `pnpm run commitlint` — validate commit messages
- `pnpm run prepare` — register Husky hooks

This enables:

- **Commit message validation** (commitlint) - enforces Conventional Commits
- **Markdown formatting checks** (markdownlint) - validates `**/*.md` files
- **Pre-commit hooks** - auto-fixes and validates Markdown before commits
- **CI workflows** - GitHub Actions runs the same checks on push/PR

## Custom instructions

Instruction files auto-apply via glob patterns. See `.github/instructions/` for details:

### Content notes

- [content-organization.instructions.md](.github/instructions/content-organization.instructions.md) → `**` (repository structure overview)
- [editing-conventions.instructions.md](.github/instructions/editing-conventions.instructions.md) → `**/*.md` (general editing rules)
- [markdown-notes.instructions.md](.github/instructions/markdown-notes.instructions.md) → `general/**/*.md`
- [special.instructions.md](.github/instructions/special.instructions.md) → `special/**/*.md`, `special/**/*.py`
- [archives.instructions.md](.github/instructions/archives.instructions.md) → `archives/**/*.md`
- [commit-convention.instructions.md](.github/instructions/commit-convention.instructions.md) → `**` (enforce conventional commit usage for agent-made commits; prompt for flashcard counts and append machine-readable trailers when changes affect `general/`, `special/`, or `self/`)

### Workflows

- [core-workflows.instructions.md](.github/instructions/core-workflows.instructions.md) → `**` (command-line workflows)

### Tools

- [init-wrapper.instructions.md](.github/instructions/init-wrapper.instructions.md) → `init.py`

### LaTeX & config

- [latex-preamble.instructions.md](.github/instructions/latex-preamble.instructions.md) → `preamble.sty`
- [config-folders.instructions.md](.github/instructions/config-folders.instructions.md) → `.git/**`, `.obsidian/**`, `.vscode/**`

### Submodule guards

- [submodule-self.instructions.md](.github/instructions/submodule-self.instructions.md) → `self/**`
- [submodule-private.instructions.md](.github/instructions/submodule-private.instructions.md) → `private/**`
- [submodule-pytextgen.instructions.md](.github/instructions/submodule-pytextgen.instructions.md) → `tools/pytextgen/**`
- [submodule-pyarchivist.instructions.md](.github/instructions/submodule-pyarchivist.instructions.md) → `tools/pyarchivist/**`

## Agent skills

Enable `chat.useAgentSkills` in VS Code for auto-loading. See `.github/skills/` for details:

### Content creation & ingestion

- **[wiki-ingestion](.github/skills/wiki-ingestion/SKILL.md)** — Import Wikipedia articles, normalize links/media, scaffold new notes
- **[tools-templates](.github/skills/tools-templates/SKILL.md)** — Template scaffolding, YAML conventions, pytextgen fence templates
- **[pytextgen](.github/skills/pytextgen/SKILL.md)** — Regenerate/clear content blocks, fence syntax, cloze markup, debugging

### Tools & workflows

- **[tools](.github/skills/tools/SKILL.md)** — Repository-wide tooling overview, tool coordination, dependency management
- **[tools-special](.github/skills/tools-special/SKILL.md)** — LMS converters (Canvas/HKUST Zinc), course catalog fetchers, academic workflows
- **[pyarchivist](.github/skills/pyarchivist/SKILL.md)** — Archive online content, auto-maintain `index.md`, media management

**Skill flow**: Most workflows use multiple skills in sequence; see individual skill files for cross-references and integration guidance.
