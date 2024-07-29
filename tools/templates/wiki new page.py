from itertools import chain
from typing import Callable, Mapping
from anyio import Path
from asyncio import run
from pyperclip import copy
from re import Pattern, compile, escape


async def main() -> None:
    name = input("Name? ").strip()

    template = await Path(__file__).with_suffix(".md.txt").read_text()

    tag_replacements = {"–": "-", "—": "-"}
    tag_name = compile(r"[^A-Za-z0-9_/-]").sub(
        lambda match: tag_replacements.get(match[0], "_"), name
    )  # https://help.obsidian.md/Editing+and+formatting/Tags#Tag+format
    if not tag_name or tag_name.isnumeric():
        tag_name += "_"
    replacements: Mapping[Pattern[str], Callable[[str], str]] = {
        compile(escape("(Wikipedia name)")): lambda _, ret=name.replace(" ", "_"): ret,
        compile(escape("(name)")): lambda _, ret=compile(r"\([^\(]+\)$").sub(
            "", name
        ): ret,
        compile(escape("(tag name)")): lambda _: tag_name,
    }

    output = compile("|".join(key.pattern for key in replacements)).sub(
        lambda match: next(
            chain(
                (val for key, val in replacements.items() if key.match(match[0])),
                (lambda ss: ss,),
            )
        )(match[0]),
        template,
    )

    print(output)
    copy(output)
    print(":)")


if __name__ == "__main__":
    run(main())
