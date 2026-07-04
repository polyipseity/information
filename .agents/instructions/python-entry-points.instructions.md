---
name: Python entry points
description: Convention for writing Python scripts and modules with __name__ == "__main__" entry points
applyTo: "**/*.py"
---

# Python Entry Points Convention

All runnable Python files must follow one of the two patterns below.

## Shebang requirement

Inline `# /// script` files __must__ begin with `#!/usr/bin/env python` on line 1.

## Async pattern

```python
from asyncer import runnify

async def main(argv: Sequence[str] | None = None) -> None:
    ...

def __main__() -> None:
    runnify(main, backend_options={"use_uvloop": True})()

if __name__ == "__main__":
    __main__()
```

## Sync pattern

```python
def main(argv: Sequence[str] | None = None) -> None:
    ...

def __main__() -> None:
    main()

if __name__ == "__main__":
    __main__()
```

## Rules

- `main()` accepts optional `argv` for testability.
- `__main__()` is always sync, with a docstring.
- Use `exit(code)` for error signals.
- Use `@pytest.mark.anyio` and import `main()` directly in tests.
- Use `os.fspath(path_like)` when converting paths to strings in tests.

## Reference

- Asyncer helpers: see `core-workflows.instructions.md`
- Templates: see `scripts/templates/`
