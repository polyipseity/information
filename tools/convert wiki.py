from pathlib import PurePath
from re import DOTALL, compile
from aiohttp import ClientSession, TCPConnector
from asyncio import gather, run
from typing import Callable, Mapping, MutableSequence
from bs4 import BeautifulSoup, NavigableString, PageElement, Tag
from bs4.element import PreformattedString
from jaraco.clipboard import paste_html
from pyperclip import copy
from sys import version
from yarl import URL

NAME = PurePath(__file__).name
AUTHORS = (
    {
        "name": "William So",
        "email": "polyipseity@gmail.com",
    },
)
VERSION = "∞"
USER_AGENT = f"{NAME}/{VERSION} ({AUTHORS[0]['email']}) Python/{version}"
_MAX_CONCURRENT_REQUESTS_PER_HOST = 2
_NAMES_DO_NOT_FIX = frozenset(
    {
        "Balmer series",
        "Bok globule",
        "Hayashi track",
        "Henyey track",
        "Jeans instability",
        "Jeans mass",
        "Latin",
        "Pauli exclusion principle",
    }
)


def _fix_name_maybe(name: str) -> str:
    return (
        f"{name[:1].lower()}{name[1:]}"
        if name not in _NAMES_DO_NOT_FIX and (len(name) <= 1 or name[1:].islower())
        else name
    )


def _markdown_link(page: str, fragment: str) -> str:
    return f"{page.replace(' ', '%20')}.md{fragment and '#'}{fragment.replace(':', '').replace(' ', '%20')}"


def _tag_affixes(name: str) -> tuple[str, str]:
    return f"<{name}>", f"</{name}>"


async def wiki_html_to_plaintext(
    ele: PageElement,
    *,
    session: ClientSession,
    list_stack: MutableSequence[int] = [],
) -> str:
    if not isinstance(ele, Tag):
        return (
            ele
            if isinstance(ele, NavigableString)
            and not isinstance(ele, PreformattedString)
            and not isinstance(ele.parent, BeautifulSoup)
            else ""
        )

    if "reference" in ele.get_attribute_list("class"):
        return ""

    process_strings: Callable[[str], str] = lambda strings: strings
    prefix, suffix = "", ""
    pop_list_stack = False
    match ele.name:
        case "p":
            suffix = "\n\n"
        case "b" | "i":
            times = 2 if ele.name == "b" else 1
            prefix, suffix = "_" * times, "_" * times

            process_strings0_pattern = compile(r"^( *)(.*?)( *)$", DOTALL)

            def process_strings0(strings: str):
                nonlocal prefix, suffix
                match = process_strings0_pattern.match(strings)
                assert match
                prefix = f"{strings[1]}{prefix}"
                suffix += strings[3]
                return strings[2]

            process_strings = process_strings0
        case "s" | "sub" | "sup" | "u":
            prefix, suffix = _tag_affixes(ele.name)
        case "a":
            if title := str(ele.get("title", "")):
                href = str(ele.get("href", ""))
                to_fragment = (
                    href.split("#", 1)[-1].replace("_", " ") if "#" in href else ""
                )
                async with session.get(
                    URL.build(
                        scheme="https",
                        host="en.wikipedia.org",
                        path="/w/api.php",
                        query={
                            "format": "json",
                            "formatversion": 2,
                            "action": "query",
                            "titles": title,
                            "redirects": "",
                        },
                    )
                ) as req:
                    redirect: Mapping[str, str] = (
                        (await req.json()).get("query", {}).get("redirects", ({},))[0]
                    )
                    to = redirect.get("to", title)
                    if not to_fragment:
                        to_fragment = redirect.get("tofragment", "")
                prefix, suffix = (
                    "[",
                    f"]({_markdown_link(_fix_name_maybe(to), _fix_name_maybe(to_fragment))})",
                )
                process_strings = (
                    lambda strings: strings.replace("\\", "\\\\")
                    .replace(R"[", R"\[")
                    .replace(R"]", R"\]")
                )
        case "ol":
            pop_list_stack = True
            list_stack.append(0)
        case "ul":
            pop_list_stack = True
            list_stack.append(-1)
        case "li":
            if list_stack and (item := list_stack[-1] + 1) >= 1:
                list_stack[-1] = item
                prefix = f"{'  ' * (len(list_stack) - 1)}{item}. "
            else:
                prefix = f"{'  ' * (len(list_stack) - 1)}- "
        case _:
            pass

    strings = "".join(
        await gather(
            *(
                wiki_html_to_plaintext(child, session=session, list_stack=list_stack)
                for child in ele.children
            )
        )
    )
    if pop_list_stack:
        list_stack.pop()
    return strings and f"{prefix}{process_strings(strings)}{suffix}"


async def main() -> None:
    input("HTML? (will read from clipboard)")
    html_text = paste_html()
    assert isinstance(html_text, str)

    html = BeautifulSoup(html_text, "html.parser")

    async with ClientSession(
        connector=TCPConnector(limit_per_host=_MAX_CONCURRENT_REQUESTS_PER_HOST),
        headers={
            "Accept-Encoding": "gzip",
            "User-Agent": USER_AGENT,
        },
    ) as session:
        output = await wiki_html_to_plaintext(html, session=session)
    output = output.replace("\xa0", " ")  # replace non-breaking spaces with spaces

    print(output)
    copy(output)
    print(":)")


if __name__ == "__main__":
    run(main())
