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

## Testing the init wrapper

- Add unit and integration tests for any change to `init.py`. Place tests under `tests/` (for example `tests/test_init.py` or `tests/init/test_generate.py`) and use `pytest.mark.asyncio` for async test functions.
- Include end-to-end tests that run `python -m init generate` on small sample files and verify expected fences are generated and existing content is preserved. Use `tmp_path: os.PathLike[str]` (annotate the `tmp_path` fixture as `PathLike[str]`) and the `anyio` file-like fixtures from other repo tests when available. When converting path-like objects to strings inside tests or the wrapper, use `os.fspath(path_like)`.
- When changing behaviour that affects generated content (pytextgen fences, section ids, export signatures), add tests that assert the exact generated content and ensure regeneration is stable across runs.
