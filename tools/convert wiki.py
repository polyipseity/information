from itertools import chain
from typing import Callable, Mapping
from asyncio import run
from pyperclip import copy
from re import Pattern, compile, escape


async def main() -> None:
    print("Wikitext?")

    wikitext = list[str]()
    while True:
        try:
            text = input()
        except EOFError:
            break
        wikitext.append(text)
    wikitext = "\n".join(wikitext)

    def markdown_link(link: str, display: str):
        link = f"{link[:1].lower()}{link[1:]}"
        return f"[{display}]({link.replace(' ', '%20')}.md)"

    replacements: Mapping[Pattern[str], Callable[[str], str]] = {
        compile(escape("'''")): lambda _: "__",
        compile(escape("''")): lambda _: "_",
        compile(r"\[\[[^\|]*\|[^\]]*\]\]"): lambda ss: markdown_link(
            *ss[2:-2].split("|", 2)
        ),
        compile(r"\[\[[^\|]*\]\]"): lambda ss: markdown_link(ss2 := ss[2:-2], ss2),
    }

    output = compile("|".join(key.pattern for key in replacements)).sub(
        lambda match: next(
            chain(
                (val for key, val in replacements.items() if key.match(match[0])),
                (lambda ss: ss,),
            )
        )(match[0]),
        wikitext,
    )

    copy(output)
    print(":)")


if __name__ == "__main__":
    run(main())
