#!/usr/bin/env python3
"""Entry point wrapper for the academic-notes validator.

This module simply delegates to :mod:`validator` after setting up rich
traceback support.  The heavy lifting lives in the package modules so that
unit tests can import and exercise the core logic without executing the CLI.
"""

from asyncio import run

import rich.traceback
from check_mods.validator import main

__all__ = ("main",)

# install rich traceback formatting (do this early, but after imports so ruff is happy)
rich.traceback.install()

if __name__ == "__main__":
    # `validator.main` accepts an argument list and returns an exit code
    # asynchronously.  `run` from `asyncio` is used so that callers can
    # invoke the CLI directly without caring about the async/await syntax.
    exit(run(main()))
