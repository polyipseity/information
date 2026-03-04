#!/usr/bin/env python
# /// script
# dependencies = [
#   "anyio>=3.6.0",
# ]
# timestamp = "2025-07-05T01:01:45.317+08:00"
# ///

"""Find missing flashcards."""

from asyncio import run
from os import listdir
from re import compile as re_compile

from anyio import Path

FLASHCARD_STATE_REGEX = re_compile(r"!\d{4}-\d{2}-\d{2}")


async def main() -> None:
    dir_path = Path(input("Path? "))

    for filename in listdir(dir_path):
        file_path = dir_path / filename
        if await file_path.is_dir() or await file_path.is_symlink():
            continue
        text = await file_path.read_text()

        flashcard_count = text.count("{@{") + text.count(":@:") + text.count("::@::")
        flashcard_state_count = len(FLASHCARD_STATE_REGEX.findall(text))

        if flashcard_count > flashcard_state_count:
            print(file_path)


if __name__ == "__main__":
    run(main())
