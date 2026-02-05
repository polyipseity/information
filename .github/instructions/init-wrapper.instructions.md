---
name: Init wrapper
description: Guardrails for the async pytextgen wrapper init.py
applyTo: "init.py"
---

# Init Wrapper Guidelines

- Preserve CLI interface (`-c/--cached`, `-C/--no-cached`, passthrough `arguments`).
- Do not change exclusion list (`.git`, `.obsidian`, `tools`) or newline normalization logic (replace platform newlines with `\n`).
- Keep caching behavior: store `(mtime,text)` in platform app cache keyed by folder inode; respect `--no-cached` to clear.
- Maintain async/anyio usage (`anyio.Path`, `TaskGroup`, `sync_to_async`, `_OPEN_TXT_OPTS`) and pytextgen parser wiring (`entry.invoke` pattern).
- Avoid hardcoding absolute paths; keep module shims for `tools.pytextgen` import.
