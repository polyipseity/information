#!/usr/bin/env python
"""Entry point wrapper for the academic-notes validator.

This module simply delegates to :mod:`validator` after setting up rich
traceback support.  The heavy lifting lives in the package modules so that
unit tests can import and exercise the core logic without executing the CLI.
"""

import sys
from collections.abc import Sequence

import rich.traceback
from asyncer import runnify
from check_mods import validator

"""Public symbols exported by this module."""
__all__ = ("main",)


async def main(argv: Sequence[str] | None = None) -> None:
    """Main entry point for the academic-notes validator CLI."""
    # install rich traceback formatting (do this early, but after imports so ruff is happy)
    rich.traceback.install()
    await validator.main(argv)


def __main__() -> None:
    """Synchronous command-line entrypoint exposed by the package."""
    # `validator.main` accepts an argument list and calls exit() when done.
    # We wrap it with `runnify` so callers can invoke the CLI synchronously.
    runnify(main, backend_options={"use_uvloop": True})(sys.argv[1:])


if __name__ == "__main__":
    __main__()
