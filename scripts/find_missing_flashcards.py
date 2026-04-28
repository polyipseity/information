#!/usr/bin/env python
"""Find missing flashcards."""

from re import compile as re_compile

from anyio import Path
from asyncer import create_task_group, runnify

FLASHCARD_STATE_REGEX = re_compile(r"!\d{4}-\d{2}-\d{2}")


async def _check_file(file_path: Path) -> None:
    if await file_path.is_dir() or await file_path.is_symlink():
        return
    text = await file_path.read_text()

    flashcard_count = text.count("{@{") + text.count(":@:") + text.count("::@::")
    flashcard_state_count = len(FLASHCARD_STATE_REGEX.findall(text))

    if flashcard_count > flashcard_state_count:
        print(file_path)


async def main() -> None:
    dir_path = Path(input("Path? "))

    async with create_task_group() as tg:
        async for entry in dir_path.iterdir():
            tg.start_soon(_check_file, entry)


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
