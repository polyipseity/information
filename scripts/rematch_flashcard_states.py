#!/usr/bin/env python
"""Rematch flashcard states using paragraphing."""

from functools import reduce
from itertools import chain
from re import DOTALL, compile

from pyperclip import copy, paste

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()

"""Regex matching all flashcard-state blocks (``<!--SR:...-->``)."""
FLASHCARD_STATES_REGEX = compile(r"\s*<!--SR:(.+?)-->", flags=DOTALL)
"""Regex matching a single flashcard-state entry within an ``<!--SR:...-->`` block.

Matches both the legacy format (``!YYYY-MM-DD,stability,difficulty``) and the
new FSRS format (``!fsrs,<9 comma-separated fields>``). The two formats may
coexist within one state block.
"""
FLASHCARD_STATE_REGEX = compile(
    r"!"
    r"(?:"
    r"\d{4}-\d{2}-\d{2},\d+,\d+"  # legacy: !YYYY-MM-DD,int,int
    r"|"
    r"fsrs,"  # fsrs: !fsrs,ISO_date,stability,difficulty,elapsed,scheduled,reps,lapses,state,last_review
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z,"
    r"\d+(?:\.\d+)?,"
    r"\d+(?:\.\d+)?,"
    r"\d+,\d+,\d+,\d+,\d+,"
    r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z"
    r")"
)
"""Regex matching any line-ending sequence for normalization."""
LINE_ENDINGS_REGEX = compile(r"\r\n|[\n\v\f\r\x85\u2028\u2029]")


def normalize_line_endings(target: str = "\n") -> str:
    """Replace all line-ending sequences in target with ``\n``."""
    return LINE_ENDINGS_REGEX.sub("\n", target)


def main() -> None:
    """Read text from clipboard, reattach flashcard states per paragraph, and copy result."""
    input("Text (will read from clipboard)? ")
    text = paste().strip()
    text = normalize_line_endings(text)

    flashcard_state_blocks: list[str] = []
    text = FLASHCARD_STATES_REGEX.sub(
        lambda match, flashcard_state_blocks=flashcard_state_blocks: (
            flashcard_state_blocks.append(match[1]),
            "",
        )[-1],
        text,
    )
    flashcard_states = tuple(
        chain.from_iterable(
            (match[0] for match in FLASHCARD_STATE_REGEX.finditer(states))
            for states in flashcard_state_blocks
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
            f"{paragraph} <!--SR:{''.join(flashcard_states[flashcard_cum_counts[idx] : flashcard_cum_counts[idx + 1]])}-->"
            if flashcard_counts[idx] > 0
            else paragraph
        )
        for idx, paragraph in enumerate(paragraphs)
    )
    print(result)
    copy(result)


def __main__() -> None:
    """Entry point for running the script directly."""
    main()


if __name__ == "__main__":
    __main__()
