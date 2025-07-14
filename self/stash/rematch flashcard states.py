"""
---
requirements: pip install pyperclip>=1.9.0
timestamp: 2025-07-14T09:29:17.420+08:00
---

Rematch flashcard states using paragraphing.
"""

from functools import reduce
from itertools import chain
from pyperclip import copy, paste
from re import DOTALL, compile

FLASHCARD_STATES_REGEX = compile(r"\s*<!--SR:(.+?)-->", flags=DOTALL)
FLASHCARD_STATE_REGEX = compile(r"!\d{4}-\d{2}-\d{2},\d+,\d+")
LINE_ENDINGS_REGEX = compile(r"\r\n|[\n\v\f\r\x85\u2028\u2029]")


def normalize_line_endings(target: str = "\n"):
    return LINE_ENDINGS_REGEX.sub("\n", target)


def main() -> None:
    input("Text (will read from clipboard)? ")
    text = paste()
    text = normalize_line_endings(text)

    flashcard_states = list[str]()
    text = FLASHCARD_STATES_REGEX.sub(
        lambda match, flashcard_states=flashcard_states: (
            flashcard_states.append(match[1]),
            "",
        )[-1],
        text,
    )
    flashcard_states = tuple(
        chain.from_iterable(
            (match[0] for match in FLASHCARD_STATE_REGEX.finditer(states))
            for states in flashcard_states
        )
    )

    paragraphs = text.split("\n\n")
    flashcard_counts = tuple(paragraph.count("{@{") for paragraph in paragraphs)
    flashcard_cum_counts = reduce(
        lambda left, right: (left.append(left[-1] + right), left)[-1],
        flashcard_counts,
        [0],
    )

    result = "\n\n".join(
        (
            f"{paragraph} <!--SR:{''.join(flashcard_states[flashcard_cum_counts[idx]:flashcard_cum_counts[idx + 1]])}-->"
            if flashcard_counts[idx] > 0
            else paragraph
        )
        for idx, paragraph in enumerate(paragraphs)
    )
    print(result)
    copy(result)


if __name__ == "__main__":
    main()
