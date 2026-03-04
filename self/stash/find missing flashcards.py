#!/usr/bin/env python
# /// script
# dependencies = [
#   "anyio>=3.6.0",
# ]
# timestamp = "2025-07-05T01:01:45.317+08:00"
# ///

"""Find missing flashcards."""

from asyncio import gather, run
from collections.abc import Awaitable
from re import compile as re_compile

from anyio import Path

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

    tasks: list[Awaitable[None]] = []
    async for entry in dir_path.iterdir():
        tasks.append(_check_file(entry))
    await gather(*tasks)


if __name__ == "__main__":
    run(main())
