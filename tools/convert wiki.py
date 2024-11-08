from glob import iglob
from pathlib import PurePath
from re import DOTALL, compile
from urllib.parse import quote
from aiohttp import ClientSession, TCPConnector
from asyncio import gather, run
from typing import Callable, Mapping
from bs4 import BeautifulSoup, NavigableString, PageElement, Tag
from bs4.element import PreformattedString
from jaraco.clipboard import paste_html  # type: ignore
from json import load
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

_WIKI_HOST_URL = URL.build(scheme="https", host="en.wikipedia.org")
_LIST_INDENT = "    "
_MAX_CONCURRENT_REQUESTS_PER_HOST = 2
_IGNORED_NAME_PREFIXES = frozenset({"Help:"})
_PRESERVED_PAGE_PREFIXES = {
    "Special:": f"{_WIKI_HOST_URL}/wiki/{{}}",
    "commons": "https://commons.wikimedia.org/wiki/{}",
    "oeis:": "https://oeis.org/{}",
    "wikt:": "https://en.wiktionary.org/wiki/{}",
}

with open(f"{NAME}.names map.json", "rt") as names_map_file:
    _names_map_manual = load(names_map_file)
_names_map = {
    filename[:-3]: filename[:-3]
    for filename in iglob("*.md", root_dir="../general/")
    if filename[:1].isupper()
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
    return (
        fragment
        and f"#{fragment.replace(':', '').replace(' ', '%20').replace('/', '%2F')}"
    )


def _markdown_link_target(page: str, fragment: str) -> str:
    return (
        f"{page.replace('/', '_').replace(' ', '%20')}.md{_markdown_fragment(fragment)}"
    )


def _markdown_link_name(name: str) -> str:
    return name.replace("\\", "\\\\").replace(R"[", R"\[").replace(R"]", R"\]")


def _tag_affixes(name: str) -> tuple[str, str]:
    return f"<{name}>", f"</{name}>"


async def wiki_html_to_plaintext(
    ele: PageElement,
    *,
    session: ClientSession,
    refs: bool,
    list_stack: tuple[int, ...] = (),
) -> str:
    if not isinstance(ele, Tag):
        return (
            ele
            if isinstance(ele, NavigableString)
            and not isinstance(ele, PreformattedString)
            and not isinstance(ele.parent, BeautifulSoup)
            else ""
        )

    classes = frozenset(ele.get_attribute_list("class"))
    if {"mw-cite-backlink", "mw-editsection"} & classes:
        return ""

    if "reference" in classes:
        if refs:
            ref_idx = compile(r"\d+").search("".join(ele.stripped_strings))
            ref_idx = int(ref_idx[0]) if ref_idx else 0
            return f"<sup>[{_markdown_link_name(f'[{ref_idx}]')}]({_markdown_fragment(f'^ref-{ref_idx}')})</sup>"
        return ""

    process_strings: Callable[[str], str] = lambda strings: strings
    prefix, suffix = "", ""
    match ele.name:
        # bold, italic, style
        case _ if ele.name in {"b", "i"} or compile(r"font-style: *italic").search(
            str(ele.get("style", ""))
        ):
            times = 2 if ele.name == "b" else 1
            prefix, suffix = "_" * times, "_" * times
            process_strings_bi_pattern = compile(r"^( *)(.*?)( *)$", DOTALL)

            def process_strings_bi(strings: str):
                nonlocal prefix, suffix
                match = process_strings_bi_pattern.match(strings)
                assert match
                prefix = f"{match[1]}{prefix}"
                suffix += match[3]
                return match[2]

            process_strings = process_strings_bi
        # literal tags
        case "s" | "sub" | "sup" | "u":
            prefix, suffix = _tag_affixes(ele.name)
        # newlines
        case "dd" | "p":  # <dl>
            suffix = "\n\n"
        # headers
        case name if (header_match := compile(r"h(\d?)").match(name)):
            prefix, suffix = f"{'#' * int(header_match[1] or '1')} ", "\n\n"
            process_strings = lambda strings: _fix_name_maybe(strings.strip())
        # code
        case "code":

            def process_strings_code(strings: str):
                nonlocal prefix, suffix
                delimiter = "`"
                while delimiter in strings:
                    delimiter += "`"
                prefix, suffix = delimiter, delimiter
                if strings.startswith("`") or strings.endswith("`"):
                    strings = f" {strings} "
                return strings

            process_strings = process_strings_code
        # mathematics
        case "math":
            if alt_text := ele.get("alttext"):
                alt_text = str(alt_text)
                alt_text_len = len(alt_text)
                alt_text = alt_text.removeprefix(R"{\displaystyle ")
                if len(alt_text) == alt_text_len:
                    alt_text = alt_text.removeprefix(R"{\textstyle ")
                if len(alt_text) <= alt_text_len:
                    alt_text = alt_text.removesuffix(R"}")
                while (
                    alt_text2 := alt_text.replace(R"{{", R"{ {")
                    .replace(R"}}", R"} }")
                    .replace(R"::", R": :")
                ) != alt_text:
                    alt_text = alt_text2
                alt_text = alt_text.strip()

                is_not_separate_paragraph = (
                    (parent := ele.parent)
                    and (parent := parent.parent)
                    and (parent := parent.parent)
                    and len(parent) > 1
                )
                is_inline = (parent := ele.parent) and "inline" in str(
                    parent.get("class", "")
                )
                inline = is_not_separate_paragraph and is_inline

                prefix, suffix = "$" if inline else "$$", "$" if inline else "$$"

                # for char in ".,":
                #     if alt_text.endswith(char):
                #         suffix += alt_text[-1]
                #         alt_text = alt_text[:-1]
                # alt_text = alt_text.strip()

                ele.clear()
                ele.append(alt_text)
        # lists
        case "ol":
            if list_stack:
                prefix = "\n"
            suffix = "\n\n"
            list_stack += (0,)
        case "ul":
            if list_stack:
                prefix = "\n"
            suffix = "\n\n"
            list_stack += (-1,)
        case "li":
            if list_stack and (item := list_stack[-1]) >= 1:
                prefix, suffix = f"{_LIST_INDENT * (len(list_stack) - 1)}{item}. ", "\n"
                if str(ele.get("id", "")).startswith("cite_"):
                    suffix = f' <a id="^ref-{item}"></a>^ref-{item}{suffix}'
            else:
                prefix, suffix = f"{_LIST_INDENT * (len(list_stack) - 1)}- ", "\n"
        # images
        case "img":
            if "mwe-math-fallback-image-inline" not in ele.get_attribute_list("class"):

                def process_strings_img(strings: str, ele: Tag = ele):
                    if src := ele.get("src"):
                        return f"{strings}![]({_WIKI_HOST_URL.join(URL(str(src)))})"
                    return strings

                suffix = "\n\n"
                process_strings = process_strings_img
        # figures
        case _ if ele.name == "figure" or "tmulti" in ele.get_attribute_list("class"):

            def process_strings_figure(strings: str):
                return "".join(
                    f">{line.strip() and ' '}{line}"
                    for line in strings.splitlines(keepends=True)
                )

            suffix = "\n\n"
            process_strings = process_strings_figure
        # links
        case "a":
            if "mw-file-description" not in ele.get_attribute_list("class"):
                process = True
                if title := ele.get("title"):
                    title = str(title)
                    href = str(ele.get("href", ""))
                    to_fragment = (
                        href.split("#", 1)[-1].replace("_", " ") if "#" in href else ""
                    )
                    async with session.get(
                        URL.build(
                            scheme=_WIKI_HOST_URL.scheme,
                            host=str(_WIKI_HOST_URL.host),
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
                            (await req.json())
                            .get("query", {})
                            .get("redirects", ({},))[0]
                        )
                        to = redirect.get("to", title)
                        if not to_fragment:
                            to_fragment = redirect.get("tofragment", "")
                    if url_format := next(
                        (
                            (format, to[len(prefix) :])
                            for prefix, format in _PRESERVED_PAGE_PREFIXES.items()
                            if to.startswith(prefix)
                        ),
                        None,
                    ):
                        prefix, suffix = (
                            "[",
                            f"]({url_format[0].format(f'{quote(url_format[1])}{to_fragment and '#'}{quote(to_fragment, safe="")}')})",
                        )
                    elif not any(
                        to.startswith(prefix) for prefix in _IGNORED_NAME_PREFIXES
                    ):
                        prefix, suffix = (
                            "[",
                            f"]({_markdown_link_target(_fix_name_maybe(to), _fix_name_maybe(to_fragment))})",
                        )
                elif href := ele.get("href"):
                    href = str(href)
                    if href.startswith(f"{_WIKI_HOST_URL}/wiki/") and "#" in href:
                        href = _markdown_fragment(
                            _fix_name_maybe(
                                href[href.index("#") + 1 :].replace("_", " ")
                            )
                        )
                    prefix, suffix = "[", f"]({href})"
                else:
                    process = False
                if process:
                    process_strings = _markdown_link_name
        # unhandled tags
        case _:
            pass

    if "hatnote" in classes:
        prefix = f"- {prefix.removesuffix('_')}"
        suffix = f"{suffix.removeprefix('_')}\n\n"

    def process_children():
        nonlocal list_stack
        for child in ele.children:
            if (
                list_stack
                and list_stack[-1] >= 0
                and isinstance(child, Tag)
                and child.name == "li"
            ):
                list_stack = (*list_stack[:-1], list_stack[-1] + 1)
            yield wiki_html_to_plaintext(
                child, session=session, refs=refs, list_stack=list_stack
            )

    strings = "".join(await gather(*process_children()))
    strings = process_strings(strings)

    return strings and f"{prefix}{strings}{suffix}"


async def main() -> None:
    refs = "--no-refs" not in argv[1:]

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
