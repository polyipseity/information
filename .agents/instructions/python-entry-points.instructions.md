---
name: Python entry points
description: Convention for writing Python scripts and modules with __name__ == "__main__" entry points
applyTo: "**/*.py"
---

# Python Entry Points Convention

This document establishes a repository-wide convention for how Python scripts and modules expose entry points for direct execution. All runnable Python files — whether scripts in `scripts/`, `scripts/`, `special/`, or module `__main__.py` files — must follow this pattern.

## Shebang Requirement

All Python files with inline `# /// script` metadata **must** begin with the shebang `#!/usr/bin/env python` on the very first line (line 1). This enables direct execution on Unix-like systems and signals that the file is a runnable script.

```python
#!/usr/bin/env python
# /// script
# dependencies = ["package1", "package2"]
# requires-python = ">=3.13.0"
# ///

# rest of code follows...
```

## Overview

The convention distinguishes between:

1. **Async logic**: The main application logic (called `main0` or `main` depending on signature)
2. **Sync dispatch wrapper**: A `__main__()` function that bridges sync and async using Asyncer's `runnify`
3. **Entry point guard**: The classic `if __name__ == "__main__":` block that invokes the wrapper

## Rationale

- **Separation of concerns**: Core logic remains decoupled from entry-point machinery, enabling easier testing and code reuse.
- **Asyncer integration**: Using `runnify` with `use_uvloop` provides reliable event-loop management, cross-platform compatibility, and performance optimization via uvloop.
- **Consistency**: All scripts follow the same pattern, making codebases predictable and reducing cognitive load when onboarding or refactoring.
- **Testability**: The async main function can be imported and tested directly without triggering the entry point guard.
- **Type hints**: Functions are properly annotated with return types, enabling static analysis and documentation.

## Pattern: Async Entry Points

For scripts with async logic, use this structure:

```python
import sys
from typing import Sequence
from logging import basicConfig, INFO

# Import application logic and utils...
from asyncer import runnify
import anyio

# ... (main application code) ...

async def main(argv: Sequence[str] | None = None) -> None:
    """Main entry point (async).

    Performs the primary logic of the script. Should accept optional argv
    for testing; if omitted, uses sys.argv[1:].
    """
    # application logic here
    pass


def __main__() -> None:
    """Entry point for running the script directly.

    Wraps the async main() using runnify with uvloop backend.
    """
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
```

**Key points**:

- The async `main()` function is the true application entry point. Its signature is `main(argv: Sequence[str] | None = None) -> None` or similar (use `None` default for friendly testing).
- The `__main__()` wrapper is **always sync** and has a docstring explaining its purpose.
- Use `runnify(main, backend_options={"use_uvloop": True})()` to run async code from sync context (uvloop is optional but recommended for performance on Unix; it is automatically skipped on Windows by Asyncer).
- The guard `if __name__ == "__main__":` is placed at the end of the file; call only `__main__()` inside the guard.

### Example: Async Script with CLI Arguments

```python
"""Convert wiki HTML to Markdown notes."""

import sys
from asyncer import runnify, asyncify
import anyio
from pathlib import Path


async def process_html(html: str) -> str:
    """Process HTML string asynchronously."""
    # Blocking work wrapped with asyncify
    result = await asyncify(some_blocking_function)(html)
    return result


async def main(argv: list[str] | None = None) -> None:
    """Main async entry point.

    Reads from clipboard (or file), processes, and outputs result.
    """
    if argv is None:
        argv = sys.argv[1:]

    # Application logic
    print("Processing...")
    # ...


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
```

## Pattern: Sync Entry Points

For scripts without async code, the pattern is simpler:

```python
import sys
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> None:
    """Main entry point (sync)."""
    if argv is None:
        argv = sys.argv[1:]

    # application logic
    pass


def __main__() -> None:
    """Entry point for running the script directly."""
    main()


if __name__ == "__main__":
    __main__()
```

**Key points**:

- `main()` is sync (no `async` keyword).
- `__main__()` simply calls `main()` directly.
- Include a docstring in `__main__()` for clarity.
- Maintain the same file structure and guard structure for consistency across async and sync scripts.

## Pattern: Module `__main__.py` (Multi-Module Dispatch)

For packages with subcommands (e.g., `scripts/pytextgen/`, where users can call `python -m pytextgen`, `python -m pytextgen.generate`, etc.), use the same pattern:

```python
"""pytextgen entry point."""

import sys
from asyncer import runnify


async def main(argv: list[str] | None = None) -> None:
    """Main async dispatcher.

    Routes to subcommands based on argv[0].
    """
    if argv is None:
        argv = sys.argv[1:]

    # dispatch logic
    # ...


def __main__() -> None:
    """Entry point for running the module directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
```

**Key points**:

- Module `__main__.py` files follow the **exact same pattern** as standalone scripts.
- Use `async def main()` for async dispatcher logic or `def main()` for sync.
- Always include the `__main__()` wrapper and `if __name__ == "__main__":` guard for consistency.

## Passing Arguments for Testing

Scripts should accept optional `argv` parameters so they can be tested without triggering the CLI entry point:

```python
async def main(argv: Sequence[str] | None = None) -> None:
    """Entry point accepting optional argv for testing."""
    if argv is None:
        argv = sys.argv[1:]
    # ... use argv ...


# In tests:
import pytest

@pytest.mark.anyio
async def test_main_with_args():
    """Test main() with explicit arguments."""
    await main(["arg1", "arg2"])
```

This pattern allows both:

1. **Direct execution**: `python script.py arg1 arg2` (uses CLI args)
2. **Programmatic testing**: Call `await main(["arg1", "arg2"])` directly in tests

## Integrating with argparse and Click

When using argument parsing libraries, keep them inside `main()`:

```python
import argparse
from asyncer import runnify


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="My script")
    parser.add_argument("input", help="Input file")
    parser.add_argument("--verbose", "-v", action="store_true")
    return parser.parse_args(argv)


async def main(argv: list[str] | None = None) -> None:
    """Main entry point."""
    if argv is None:
        argv = sys.argv[1:]

    args = parse_args(argv)
    # Application logic using args
    print(f"Input: {args.input}")


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
```

## Type Hints and Documentation

- **Type hints**: Always include return type hints on `main()` and `__main__()`. For sync entry points, `-> None` is common. For async, `async def main(...) -> None` follows the same convention.
- **Docstrings**: Include a module-level docstring at the top of the file. Include docstrings on `main()` and `__main__()` explaining their purpose.
- **Example docstring**:

  ```python
  """Convert wiki HTML to Markdown.

  Usage:
      python -m convert_wiki

  Reads HTML from clipboard, normalizes to Markdown, and outputs to stdout.
  """
  ```

## Error Handling

- Call `exit(code)` or `return exit(code)` to signal error conditions. The exit code convention:
  - `exit(0)`: Success
  - `exit(1)`: General error
  - `exit(2)`: Argument parsing error
  - `exit(3)`: File/IO error
  - Higher codes: Domain-specific errors

- Example:

  ```python
  async def main(argv: list[str] | None = None) -> None:
      """Process a file."""
      if argv is None:
          argv = sys.argv[1:]

      args = parse_args(argv)

      try:
          result = await process_file(args.input)
          print(result)
      except FileNotFoundError as e:
          print(f"Error: {e}", file=sys.stderr)
          return exit(3)
      except ValueError as e:
          print(f"Validation error: {e}", file=sys.stderr)
          return exit(2)

      return exit(0)  # explicit success
  ```

## Submodule & External Tool Scripts

Scripts in Git submodules (`scripts/pytextgen/`, `scripts/pyarchivist/`, `self/ledger/`, `self/arts/`) must follow this convention within their own repositories. When updating those submodules:

1. Check the submodule's own `.agents/instructions/python-entry-points.instructions.md` first (if it exists).
2. If no entry-point instructions exist in the submodule, apply this repository's convention.
3. Submit changes upstream if the submodule maintainer agrees to adopt the convention.

**Repository submodules with entry points**:

- `scripts/pytextgen/src/pytextgen/__main__.py` — already follows the pattern
- `scripts/pytextgen/src/pytextgen/generate/__main__.py` — already follows the pattern
- `scripts/pytextgen/src/pytextgen/clear/__main__.py` — already follows the pattern
- `scripts/pyarchivist/src/pyarchivist/__main__.py` — already follows the pattern
- `scripts/pyarchivist/src/pyarchivist/Wikimedia_Commons/__main__.py` — already follows the pattern
- `self/ledger/scripts/*.py` — follow this convention
- `self/arts/scripts/*.py` — follow this convention

## Implementation Checklist

When writing a new Python script or updating an existing one:

- [ ] Define `main()` as the primary logic (async or sync)
- [ ] Accept optional `argv` parameter in `main()` for testing: `main(argv: Sequence[str] | None = None)`
- [ ] Define `__main__()` sync wrapper function with a docstring
- [ ] Use `runnify(main, backend_options={"use_uvloop": True})()` for async, or just `main()` for sync
- [ ] Place `if __name__ == "__main__":` guard at file end, calling only `__main__()`
- [ ] Include return type hints: `-> None` for both `main()` and `__main__()`
- [ ] Add module-level docstring explaining script purpose and usage
- [ ] Add docstrings to `main()` and `__main__()`
- [ ] Test by importing `main()` directly in pytest (use `@pytest.mark.anyio` for async tests)
- [ ] Verify `python script.py --help` works if using argparse
- [ ] Run `bun run check` and `bun run format` to validate formatting

## Testing Pattern

```python
# tests/test_my_script.py
import pytest
from pathlib import Path


@pytest.mark.anyio
async def test_main_success(tmp_path: Path):
    """Test main() with valid input."""
    from my_script import main
    await main(["--input", str(tmp_path / "input.txt")])
    # assertions...


@pytest.mark.anyio
async def test_main_error_handling(tmp_path: Path):
    """Test main() handles errors gracefully."""
    from my_script import main
    await main(["--input", "/nonexistent/path"])
    # assertions...
```

**Testing rules**:

- Import `main` directly in tests; do not trigger the `if __name__ == "__main__":` guard
- Use `@pytest.mark.anyio` for async tests (with AnyIO pytest plugin)
- Pass explicit `argv` to `main()` to control test inputs
- Use `pytest` fixtures like `tmp_path: PathLike[str]` for temporary files/directories
- Convert path-like objects to strings with `os.fspath(path_like)` when needed

## Related Guidance

- **Async helpers**: See `.agents/instructions/agent-quickstart.instructions.md` for Asyncer usage (`runnify`, `asyncify`, `soonify`, `create_task_group`)
- **Script templates**: See `scripts/templates/` for scaffold examples
- **Error handling**: Follow the project's error conventions (exit codes, stderr output)
- **Logging**: Use Python's `logging` module with `basicConfig(level=INFO)` in `main()` when appropriate

## Frequently Asked Questions

**Q: Why wrap an async main in a sync `__main__()` function instead of calling `runnify()` directly in the guard?**

A: This allows the sync wrapper to be tested/documented as a separate unit and makes the entry-point invocation more explicit and readable. It also mirrors the sync pattern exactly, reducing cognitive overhead.

**Q: What if my script is purely sync?**

A: Use the sync pattern: `main()` calls the logic, `__main__()` calls `main()` without `runnify`, and the guard remains the same.

**Q: Can I use `asyncio` directly instead of Asyncer?**

A: No. The project uses AnyIO for cross-platform structured concurrency, with Asyncer providing convenient wrappers (`runnify`, `asyncify`, etc.). Avoid importing `asyncio` directly in new code.

**Q: Should I call `sys.exit()` or `exit()` in main?**

A: Use `exit(code)` or `return exit(code)` consistently. Both work; `exit()` is from builtins and is slightly more portable. Using `return exit(code)` makes the intent clear (early exit with status).

**Q: Why always include `uvloop` backend option even on Windows?**

A: Asyncer automatically skips uvloop on Windows and falls back to the standard asyncio event loop. Including the option makes the code portable and allows uvloop to be used on Unix/Linux/macOS without conditionals.

**Q: Can scripts accept positional arguments without argparse?**

A: Yes, `argv` is a plain list. You can parse it manually if argparse is overkill. However, for CLI scripts, argparse is preferred for consistency and automatic `--help` support.

---

For more context on async/concurrency patterns in the repo, see `.agents/instructions/agent-quickstart.instructions.md` and the examples in `tests/test_async_concurrency.py`.
