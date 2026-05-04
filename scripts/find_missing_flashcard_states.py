#!/usr/bin/env python
"""Find missing flashcard states."""

from re import compile as re_compile

from anyio import Path
from asyncer import create_task_group, runnify

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()

"""Regex matching a single flashcard-state date annotation (e.g. ``!2024-01-15``)."""
FLASHCARD_STATE_REGEX = re_compile(r"!\d{4}-\d{2}-\d{2}")


async def _check_file(file_path: Path) -> None:
    """Print file_path if it contains fewer flashcard states than flashcard markers."""
    if await file_path.is_dir() or await file_path.is_symlink():
        return
    text = await file_path.read_text()

    flashcard_count = text.count("{@{") + text.count(":@:") + text.count("::@::")
    flashcard_state_count = len(FLASHCARD_STATE_REGEX.findall(text))

    if flashcard_count > flashcard_state_count:
        print(file_path)


async def main() -> None:
    """Prompt for a directory path and check all entries for missing flashcard states."""
    dir_path = Path(input("Path? "))

    async with create_task_group() as tg:
        async for entry in dir_path.iterdir():
            tg.start_soon(_check_file, entry)


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
