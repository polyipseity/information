"""Tests for the thin CLI wrapper in :mod:`academic-lint.main`.

The module exists primarily to install :mod:`rich.traceback` before
calling the asynchronous :func:`main_mods.validator.main`.  Most of the
functionality is exercised by the validator unit tests, but we still need a
smoke test to cover the entry point and ensure the ``__main__`` behavior
works when the module is executed as a script.

The ``__all__`` tuple is provided to satisfy the repository-wide export
compliance checks which require every Python module to define it.
"""

import subprocess
import sys
from os import PathLike

import main
import pytest
from anyio import Path
from main_mods import validator

# expose an explicit export list so tests for `__all__` pass
"""Public symbols exported by this module (none)."""
__all__ = ()


@pytest.mark.anyio
async def test_main_matches_validator(
    tmp_path: PathLike[str], monkeypatch: pytest.MonkeyPatch
):
    """``main.main`` should behave identically to
    ``main_mods.validator.main``.

    We already test the validator in ``main_mods/test_validator.py`` but
    the wrapper is a simple asynchronous proxy, so this test merely ensures
    the import path is correct and that the thin wrapper returns the
    expected exit code for a trivial invocation.
    """

    # create a minimal markdown file that will trigger a non-zero exit code
    bad_file = Path(tmp_path) / "bad.md"
    await bad_file.write_text(
        """---
tags: []
---
"""
    )

    # validator.main and main.main both call exit(); assert same exit code
    with pytest.raises(SystemExit) as ev:
        await validator.main([str(tmp_path)])

    previous_argv = sys.argv[:]
    try:
        sys.argv[:] = ["main", str(tmp_path)]
        with pytest.raises(SystemExit) as ew:
            await main.main()
    finally:
        sys.argv[:] = previous_argv

    assert ew.value.code == ev.value.code
    assert ev.value.code != 0  # there should be at least one error message


@pytest.mark.anyio
async def test_module_invoked_as_script(
    tmp_path: PathLike[str], capsys: pytest.CaptureFixture[str]
):
    """Executing ``uv run -m main`` should behave like the CLI entry point.

    This regression test forks a subprocess to simulate the normal user
    experience.  We craft a temporary directory with a deliberately bad file
    so that the script exits nonzero and prints at least one message.  Using
    ``uv run -m main`` mirrors how the module would be invoked when installed
    as a script entry point.
    """

    # prepare workspace
    bad_file = Path(tmp_path) / "bad.md"
    await bad_file.write_text(
        """---
xyz: 1
---
"""
    )

    # run the script directly using its filesystem path; this avoids
    # ``-m`` lookup problems when the module isn't installed in sys.path.
    # compute the path relative to *this* test file rather than the temp
    # directory, which keeps the logic simple and robust regardless of where
    # pytest creates tmp_path.

    # ``__file__.parent.parent`` points at the ``academic-lint``
    # skill directory where ``main.py`` lives.
    skill_root = (await Path(__file__).resolve()).parent.parent
    script_path = skill_root / "main.py"
    proc = subprocess.run(
        (sys.executable, str(script_path), str(tmp_path)),
        capture_output=True,
        text=True,
    )

    # the process should exit with a non-zero code and produce some output
    assert proc.returncode != 0
    assert proc.stderr or proc.stdout

    # forward the subprocess output through the current test's stdout/stderr
    # so that capsys can capture and allow additional assertions below.
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)

    captured = capsys.readouterr()
    # now we can assert on the captured streams
    assert (
        "error" in captured.out.lower()
        or "missing" in captured.out.lower()
        or "error" in captured.err.lower()
        or "missing" in captured.err.lower()
    )
