---
name: Prompt files
description: Use when adding or editing .agents/prompts/*.prompt.md. Covers user-scope command-name collisions and frontmatter that a YAML parser accepts.
applyTo: "**/*.prompt.md"
---

# Prompt files

A slash command is a `.prompt.md` file. User scope (`~/.agents/prompts/`) loads before repository scope (`.agents/prompts/`), and the user copy wins: a repository file that reuses a user-scope command name loads as skipped, without warning, so the command runs the user prompt and never the repository one.

## Command names

List both scopes before adding a prompt. A repository file never reuses a user-scope command name; on a collision, rename the repository file to a distinct command or delete it, since a shadowed file defines nothing and drifts from the copy that actually runs.

## Frontmatter

Frontmatter carries `name`, `description`, and `argument-hint`, plus only the keys the harness documents for prompts (`disable-model-invocation` marks a user-invocable command). Instruction-file keys — `applyTo` and `alwaysApply` — belong to `.instructions.md` files and are inert on a prompt.

Quote a value that holds a colon followed by a space, or that opens with a YAML indicator. YAML reads that colon as a nested mapping key and rejects the document, so `argument-hint: 'Optional: incomingBranch=origin/main'` parses where the unquoted form fails; single quotes keep double quotes inside the value intact.

## The check

Parse every prompt in both scopes. One parse per file, and a frontmatter that is not a mapping is a failure:

```bash
uv run python - <<'PY'
import pathlib, re, yaml
for d in (".agents/prompts", str(pathlib.Path.home() / ".agents/prompts")):
    for p in sorted(pathlib.Path(d).glob("*.prompt.md")):
        front = re.match(r"^---\n(.*?)\n---\n", p.read_text(encoding="utf-8"), re.S)
        try:
            data = yaml.safe_load(front.group(1)) if front else None
        except yaml.YAMLError:
            data = None
        print("ok" if isinstance(data, dict) else "FAIL", p)
PY
```
