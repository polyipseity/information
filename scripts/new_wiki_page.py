"""Scaffold a new Wikipedia-sourced note with frontmatter and a template.

Prompts for the article name, builds the YAML frontmatter and a skeleton
note body, then copies the result to the system clipboard.
"""

from re import sub
from unicodedata import normalize

from asyncer import runnify
from pyperclip import copy

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()


async def main() -> None:
    """Prompt for article name, build note skeleton, and copy it to clipboard."""
    name = normalize("NFC", input("Name? ")).strip()

    tag_replacements = {"–": "-", "—": "-"}
    tag_name = sub(
        r"[^A-Za-z0-9À-ÿ_-]",
        lambda match: tag_replacements.get(match.group(0), "_"),
        name,
    )
    if not tag_name or tag_name.isnumeric():
        tag_name += "_"

    wikipedia_name = name.replace(" ", "_")
    title = sub(r" \([^()]+\)$", "", name)
    output = f"""---
aliases:
  - {title}
tags:
  - flashcard/active/general/eng/{tag_name}
  - language/in/English
---

# {title}

## references

This text incorporates [content](https://en.wikipedia.org/wiki/{wikipedia_name}) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
"""

    print(output)
    copy(output)
    print(":)")


def __main__():
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
