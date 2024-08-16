from glob import iglob
from pathlib import PurePath
from re import DOTALL, compile
from aiohttp import ClientSession, TCPConnector
from asyncio import gather, run
from typing import Callable, Mapping, MutableSequence
from bs4 import BeautifulSoup, NavigableString, PageElement, Tag
from bs4.element import PreformattedString
from jaraco.clipboard import paste_html  # type: ignore
from pyperclip import copy  # type: ignore
from sys import argv, version
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
    "Cepheus (constellation)": "Cepheus (constellation)",
    "Discrete Fourier series": "discrete Fourier series",
    "Discrete Fourier transform": "discrete Fourier transform",
    "Discrete-time Fourier transform": "discrete-time Fourier transform",
    "Discrete Hartley transform": "discrete Hartley transform",
    "Euclidean distance": "Euclidean distance",
    "Euclidean norm": "Euclidean norm",
    "Euclidean space": "Euclidean space",
    "Jeans instability": "Jeans instability",
    "Jeans mass": "Jeans mass",
    "Latin": "Latin",
    "Polaris": "Polaris",
    "Squared Euclidean distance": "squared Euclidean distance",
    "Super soft X-ray source": "super soft X-ray source",
    "X-ray": "X-ray",
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


def _markdown_link_target(page: str, fragment: str) -> str:
    return f"{page.replace(' ', '%20')}.md{_markdown_fragment(fragment)}"


def _markdown_link_name(name: str) -> str:
    return name.replace("\\", "\\\\").replace(R"[", R"\[").replace(R"]", R"\]")


def _tag_affixes(name: str) -> tuple[str, str]:
    return f"<{name}>", f"</{name}>"


async def wiki_html_to_plaintext(
    ele: PageElement,
    *,
    session: ClientSession,
    refs: bool,
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
        if refs:
            ref_idx = compile(r"\d+").search("".join(ele.stripped_strings))
            ref_idx = int(ref_idx[0]) if ref_idx else 0
            return f"<sup>[{_markdown_link_name(f'[{ref_idx}]')}]({_markdown_fragment(f'^ref-{ref_idx}')})</sup>"
        return ""

    process_strings: Callable[[str], str] = lambda strings: strings
    prefix, suffix = "", ""
    pop_list_stack = False
    match ele.name:
        case "p":
            suffix = "\n\n"
        case name if name in ("b", "i") or compile(r"font-style: *italic").search(
            str(ele.get("style", ""))
        ):
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
            if title := ele.get("title"):
                title = str(title)
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
                    f"]({_markdown_link_target(_fix_name_maybe(to), _fix_name_maybe(to_fragment))})",
                )
            elif href := ele.get("href"):
                href = str(href)
                if href.startswith("https://en.wikipedia.org/wiki/") and "#" in href:
                    href = _markdown_fragment(
                        _fix_name_maybe(href[href.index("#") + 1 :].replace("_", " "))
                    )
                prefix, suffix = "[", f"]({href})"
            else:
                process = False
            if process:
                process_strings = _markdown_link_name
        case "ol":
            suffix = "\n\n"
            pop_list_stack = True
            list_stack.append(0)
        case "ul":
            suffix = "\n\n"
            pop_list_stack = True
            list_stack.append(-1)
        case "li":
            if list_stack and (item := list_stack[-1] + 1) >= 1:
                list_stack[-1] = item
                prefix = f"{'  ' * (len(list_stack) - 1)}{item}. "
                if str(ele.get("id", "")).startswith("cite_"):
                    suffix = f' <a id="^ref-{item}"></a>^ref-{item}\n'
            else:
                prefix, suffix = f"{'  ' * (len(list_stack) - 1)}- ", "\n"
        case "math":
            if alt_text := ele.get("alttext"):
                alt_text = str(alt_text)
                alt_text_len = len(alt_text)
                alt_text = alt_text.removeprefix(R"{\displaystyle ")
                if len(alt_text) == alt_text_len:
                    alt_text = alt_text.removeprefix(R"{\textstyle ")
                if len(alt_text) <= alt_text_len:
                    alt_text = alt_text.removesuffix(R"}")
                alt_text = alt_text.replace(R"{{", R"{ {").replace(R"}}", R"} }")

                inline = (
                    (parent := ele.parent)
                    and (parent := parent.parent)
                    and (parent := parent.parent)
                    and len(parent) > 1
                )

                prefix, suffix = "$" if inline else "$$", "$" if inline else "$$\n\n"

                ele.clear()
                ele.append(alt_text)
        case name if (header_match := compile(r"h(\d?)").match(name)):
            prefix, suffix = f"{'#' * int(header_match[1] or '1')} ", "\n\n"
            process_strings = lambda strings: _fix_name_maybe(strings.strip())
        case _:
            pass

    strings = "".join(
        await gather(
            *(
                wiki_html_to_plaintext(
                    child, session=session, refs=refs, list_stack=list_stack
                )
                for child in ele.children
            )
        )
    )
    strings = process_strings(strings)

    if pop_list_stack:
        list_stack.pop()

    return strings and f"{prefix}{strings}{suffix}"


async def main() -> None:
    refs = "refs" in argv[1:]

    input("HTML? (will read from clipboard)")
    html_text = paste_html()  # type: ignore
    assert isinstance(html_text, str)

    html = BeautifulSoup(html_text, "html.parser")

    async with ClientSession(
        connector=TCPConnector(limit_per_host=_MAX_CONCURRENT_REQUESTS_PER_HOST),
        headers={
            "Accept-Encoding": "gzip",
            "User-Agent": USER_AGENT,
        },
    ) as session:
        output = await wiki_html_to_plaintext(html, session=session, refs=refs)
    output = output.replace(
        "\xa0", " "  # replace non-breaking spaces with spaces
    ).strip()

    print(output)
    copy(output)
    print(":)")


if __name__ == "__main__":
    run(main())
