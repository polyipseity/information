from glob import iglob
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

_names_map = {
    filename[:-3]: filename[:-3]
    for filename in iglob("*.md", root_dir="../general/")
    if filename[:1].isupper()
}
_names_map_manual = {
    "Balmer series": "Balmer series",
    "Bok globule": "Bok globule",
    "Euclidean distance": "Euclidean distance",
    "Euclidean norm": "Euclidean norm",
    "Euclidean space": "Euclidean space",
    "Jeans instability": "Jeans instability",
    "Jeans mass": "Jeans mass",
    "Latin": "Latin",
    "X-ray": "X-ray",
    "Discrete Fourier series": "discrete Fourier series",
    "Discrete Fourier transform": "discrete Fourier transform",
    "Discrete-time Fourier transform": "discrete-time Fourier transform",
    "Squared Euclidean distance": "squared Euclidean distance",
}
if _names_map_overlap := frozenset(_names_map).intersection(_names_map_manual):
    raise ValueError(_names_map_overlap)
_NAMES_MAP = _names_map | _names_map_manual


def _fix_name_maybe(name: str) -> str:
    return _NAMES_MAP.get(
        name,
        (
            f"{name[:1].lower()}{name[1:]}"
            if len(name) <= 1 or name[1:].islower()
            else name
        ),
    )


def _markdown_fragment(fragment: str) -> str:
    return fragment and f"#{fragment.replace(':', '').replace(' ', '%20')}"


def _markdown_link(page: str, fragment: str) -> str:
    return f"{page.replace(' ', '%20')}.md{_markdown_fragment(fragment)}"


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
                prefix = f"{match[1]}{prefix}"
                suffix += match[3]
                return match[2]

            process_strings = process_strings0
        case "s" | "sub" | "sup" | "u":
            prefix, suffix = _tag_affixes(ele.name)
        case "a":
            process = True
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
            elif href := str(ele.get("href", "")):
                if href.startswith("https://en.wikipedia.org/wiki/") and "#" in href:
                    href = _fix_name_maybe(
                        href[href.index("#") + 1 :].replace("_", " ")
                    )
                prefix, suffix = "[", f"]({_markdown_fragment(href)})"
            else:
                process = False
            if process:
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
            suffix = "\n"
        case "math":
            if alt_text := str(ele.get("alttext", "")):
                ele.clear()
                ele.append(
                    alt_text.removeprefix(R"{\displaystyle ").removesuffix(R"}").strip()
                )
                math_affix = (
                    "$"
                    if (parent := ele.parent)
                    and (parent := parent.parent)
                    and (parent := parent.parent)
                    and len(parent) > 1
                    else "$$"
                )
                prefix, suffix = math_affix, math_affix
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
    strings = process_strings(strings)

    if pop_list_stack:
        list_stack.pop()

    return strings and f"{prefix}{strings}{suffix}"


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
