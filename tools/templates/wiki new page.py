# -*- coding: UTF-8 -*-
from anyio import Path
from asyncio import run
from pyperclip import copy
from re import compile, escape


async def main() -> None:
    name = input("Name? ").strip()

    template = await Path(__file__).with_suffix(".md.txt").read_text()

    tag_replacements = {"–": "-", "—": "-"}
    tag_name = compile(r"[^A-Za-z0-9_/-]").sub(
        lambda match: tag_replacements.get(match[0], "_"), name
    )  # https://help.obsidian.md/Editing+and+formatting/Tags#Tag+format
    if not tag_name or tag_name.isnumeric():
        tag_name += "_"
    replacements = {
        "(Wikipedia name)": name.replace(" ", "_"),
        "(name)": name,
        "(tag name)": tag_name,
    }

    output = compile("|".join(escape(key) for key in replacements)).sub(
        lambda m: replacements[m[0]], template
    )

    copy(output)
    print(":)")


if __name__ == "__main__":
    run(main())
