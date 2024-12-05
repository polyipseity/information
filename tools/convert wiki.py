from aiohttp import ClientSession, TCPConnector
from anyio import Path
from asyncio import gather, run
from bs4 import BeautifulSoup, NavigableString, PageElement, Tag
from bs4.element import PreformattedString
from copy import copy
from glob import iglob
from jaraco.clipboard import paste_html  # type: ignore
from json import load
from logging import INFO, basicConfig
from pathlib import PurePath
from pyarchivist.Wikimedia_Commons.main import (
    Args as pyarchivist_Wikimedia_Commons_Args,
    main as pyarchivist_Wikimedia_Commons_main,
)
from pyperclip import copy as clip_copy  # type: ignore
from re import DOTALL, Pattern, compile
from string import punctuation, whitespace
from sys import argv, version
from typing import Callable, Mapping, MutableSet
from urllib.parse import quote
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
_MARKDOWN_SEPARATOR = "<!-- markdown separator -->"
_MARKDOWN_SEPARATOR_CHARACTERS = f"{punctuation}{whitespace}".replace("_", "")
_BAD_TITLES = frozenset({"Edit this at Wikidata"})
_IGNORED_NAME_PREFIXES = frozenset[str]()
_PRESERVED_PAGE_PREFIXES = {
    "Category:": f"{_WIKI_HOST_URL}/wiki/Category:{{}}",
    "Help:": f"{_WIKI_HOST_URL}/wiki/Help:{{}}",
    "Portal:": f"{_WIKI_HOST_URL}/wiki/Portal:{{}}",
    "Special:": f"{_WIKI_HOST_URL}/wiki/Special:{{}}",
    "Talk:": f"{_WIKI_HOST_URL}/wiki/Talk:{{}}",
    "Template:": f"{_WIKI_HOST_URL}/wiki/Template:{{}}",
    "Template talk:": f"{_WIKI_HOST_URL}/wiki/Template%20talk:{{}}",
    "Wikipedia": f"{_WIKI_HOST_URL}/wiki/Wikipedia:{{}}",
    "commons": "https://commons.wikimedia.org/wiki/{}",
    "oeis:": "https://oeis.org/{}",
    "q:": "https://en.wikiquote.org/wiki/{}",
    "v:": "https://en.wikiversity.org/wiki/{}",
    "wikiversity:": "https://en.wikiversity.org/wiki/{}",
    "wikt:": "https://en.wiktionary.org/wiki/{}",
    "wiktionary:": "https://en.wiktionary.org/wiki/{}",
}
_ARCHIVE_REGEXES = {
    compile(
        r"^https://upload.wikimedia.org/wikipedia/[^/]*/thumb/[0-9a-f]/[0-9a-f]{2}/([^/]*)/.*$"
    ): ("File:{}", "../archives/Wikimedia Commons/{}"),
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


def _tag_affixes(name: str) -> tuple[str, str]:
    return f"<{name}>", f"</{name}>"


async def wiki_html_to_plaintext(
    ele: PageElement,
    *,
    out_to_archive: MutableSet[str],
    list_stack: tuple[int, ...] = (),
    math: bool = False,
    refs: bool,
    session: ClientSession,
    __HEADER_PATTERN: Pattern[str] = compile(r"h(\d?)"),
    __BOLD_FONT_STYLE_REGEX: Pattern[str] = compile(r"font-weight: *bold"),
    __ITALIC_FONT_STYLE_REGEX: Pattern[str] = compile(r"font-style: *italic"),
    __MARKDOWN_ESCAPE_REGEX: Pattern[str] = compile(r"[#$()*<>\\[\\\]_`|]"),
    __PROCESS_STRINGS_BI_REGEX: Pattern[str] = compile(r"^( *)(.*?)( *)$", DOTALL),
    __REF_CONTENT_REGEX: Pattern[str] = compile(r"\[([^]]*)\]"),
) -> str:
    def escape_markdown(text: str):
        return __MARKDOWN_ESCAPE_REGEX.sub(lambda match: Rf"\{match[0]}", text)

    if not isinstance(ele, Tag):
        return (
            (ele if math else escape_markdown(ele))
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
            ref_content = __REF_CONTENT_REGEX.search("".join(ele.stripped_strings))
            ref_content = ref_content[1] if ref_content else 0
            return f"<sup>[{escape_markdown(f'[{ref_content}]')}]({_markdown_fragment(f'^ref-{ref_content}')})</sup>"
        return ""

    process_strings: Callable[[str], str] = lambda strings: strings
    joiner = ""
    prefix, suffix = "", ""
    match ele.name:
        # headers, should come before bold
        case name if (header_match := __HEADER_PATTERN.match(name)):
            prefix, suffix = f"{'#' * int(header_match[1] or '1')} ", "\n\n"
            process_strings = lambda strings: _fix_name_maybe(strings.strip())
        # bold
        case _ if (
            ele.name == "b" or __BOLD_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
        ) and "mw-heading" not in ele.get_attribute_list("class"):
            prefix, suffix = "__", "__"
            if (
                ele.previous_sibling
                and isinstance(ele.previous_sibling, NavigableString)
                and ele.previous_sibling.rstrip(_MARKDOWN_SEPARATOR_CHARACTERS)
                == ele.previous_sibling
            ):
                prefix = f"{_MARKDOWN_SEPARATOR}{prefix}"
            if (
                ele.next_sibling
                and isinstance(ele.next_sibling, NavigableString)
                and ele.next_sibling.lstrip(_MARKDOWN_SEPARATOR_CHARACTERS)
                == ele.next_sibling
            ):
                suffix += _MARKDOWN_SEPARATOR

            def process_strings_b(strings: str):
                nonlocal prefix, suffix
                match = __PROCESS_STRINGS_BI_REGEX.match(strings)
                assert match
                prefix = f"{match[1]}{prefix}"
                suffix += match[3]
                return match[2]

            process_strings = process_strings_b
        # italic
        case _ if ele.name == "i" or __ITALIC_FONT_STYLE_REGEX.search(
            str(ele.get("style", ""))
        ):
            prefix, suffix = "_", "_"
            if (
                ele.previous_sibling
                and isinstance(ele.previous_sibling, NavigableString)
                and ele.previous_sibling.rstrip(_MARKDOWN_SEPARATOR_CHARACTERS)
                == ele.previous_sibling
            ):
                prefix = f"{_MARKDOWN_SEPARATOR}{prefix}"
            if (
                ele.next_sibling
                and isinstance(ele.next_sibling, NavigableString)
                and ele.next_sibling.lstrip(_MARKDOWN_SEPARATOR_CHARACTERS)
                == ele.next_sibling
            ):
                suffix += _MARKDOWN_SEPARATOR

            def process_strings_i(strings: str):
                nonlocal prefix, suffix
                match = __PROCESS_STRINGS_BI_REGEX.match(strings)
                assert match
                prefix = f"{match[1]}{prefix}"
                suffix += match[3]
                return match[2]

            process_strings = process_strings_i
        # literal tags
        case "s" | "sub" | "sup" | "u":
            prefix, suffix = _tag_affixes(ele.name)
        # newlines
        case "dd" | "dt" | "p":  # <dl>
            suffix = "\n\n"
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
                alt_text = (
                    alt_text.replace(R":@:", R": @ :")
                    .replace(R"?@?", R"? @ ?")
                    .replace(R"{@{", R"{ @ {")
                    .replace(R"}@}", R"} @ }")
                    .strip()
                )

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
        # tables
        case "tbody" | "thead":
            suffix = "\n\n"

            # normalize cells
            for tdh in tuple(ele.find_all(("td", "th"))):
                assert isinstance(tdh, Tag)
                col_span = str(tdh.get("colspan", "1"))
                try:
                    col_span = int(col_span)
                except ValueError:
                    pass
                else:
                    tdh["colspan"] = "1"
                    for _ in range(1, col_span):
                        new_tdh = copy(tdh)
                        new_tdh.clear()
                        tdh.insert_after(new_tdh)
            for tdh in tuple(ele.find_all(("th", "td"))):
                assert isinstance(tdh, Tag)
                row_span = str(tdh.get("rowspan", "1"))
                try:
                    row_span = int(row_span)
                except ValueError:
                    pass
                else:
                    if (current_row := tdh.parent) is not None:
                        col_idx = current_row.index(tdh)
                        tdh["rowspan"] = "1"
                        for _ in range(1, row_span):
                            if (current_row := current_row.next_sibling) is None:
                                break
                            new_tdh = copy(tdh)
                            new_tdh.clear()
                            current_row.insert(col_idx, new_tdh)
        case "tr":
            joiner = " | "
            prefix, suffix = "| ", " |\n"
            if ele.contents and all(
                isinstance(child, Tag) and child.name == "th" for child in ele.contents
            ):
                suffix += f"|{' - |' * len(ele.contents)}\n"
        case "td" | "th":

            def process_strings_tdh(strings: str):
                return (
                    strings.strip()
                    .replace("\n\n", " <p> ")
                    .replace("\n", " <br/> ")
                    .strip()
                )

            process_strings = process_strings_tdh
        # images
        case (
            _
        ) if ele.name == "img" and "mwe-math-fallback-image-inline" not in ele.get_attribute_list(
            "class"
        ):

            def process_strings_img(strings: str, ele: Tag = ele):
                if src := ele.get("src"):
                    src_url = _WIKI_HOST_URL.join(URL(str(src)))
                    src_url_str = str(src_url)

                    for regex, formats in _ARCHIVE_REGEXES.items():
                        if not (match := regex.search(src_url.human_repr())):
                            continue
                        to_archive = match[1]
                        out_to_archive.add(formats[0].format(to_archive))
                        src_url_str = quote(
                            formats[1].format(to_archive.replace("_", " "))
                        )

                    return f"{strings}![]({src_url_str})"
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
        case (
            _
        ) if ele.name == "a" and "mw-file-description" not in ele.get_attribute_list(
            "class"
        ):
            if (title := ele.get("title")) and title not in _BAD_TITLES:
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
                        (await req.json()).get("query", {}).get("redirects", ({},))[0]
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
                        _fix_name_maybe(href[href.index("#") + 1 :].replace("_", " "))
                    )
                prefix, suffix = "[", f"]({href})"
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
                child,
                out_to_archive=out_to_archive,
                list_stack=list_stack,
                math=ele.name == "math",
                refs=refs,
                session=session,
            )

    strings = joiner.join(await gather(*process_children()))
    strings = process_strings(strings)

    return strings and f"{prefix}{strings}{suffix}"


async def main() -> None:
    refs = "--no-refs" not in argv[1:]

    input("HTML? (will read from clipboard)")
    html_text = paste_html()  # type: ignore
    assert isinstance(html_text, str)

    html = BeautifulSoup(html_text, "html.parser")

    out_to_archive = set[str]()
    async with ClientSession(
        connector=TCPConnector(limit_per_host=_MAX_CONCURRENT_REQUESTS_PER_HOST),
        headers={
            "Accept-Encoding": "gzip",
            "User-Agent": USER_AGENT,
        },
    ) as session:
        output = await wiki_html_to_plaintext(
            html, out_to_archive=out_to_archive, session=session, refs=refs
        )
    output = output.replace(
        "\xa0", " "  # replace non-breaking spaces with spaces
    ).strip()

    if out_to_archive:
        try:
            basicConfig(level=INFO)
            await pyarchivist_Wikimedia_Commons_main(
                pyarchivist_Wikimedia_Commons_Args(
                    inputs=tuple(out_to_archive),
                    dest=Path("../archives/Wikimedia Commons/"),
                    index=Path("../archives/Wikimedia Commons/index.md"),
                )
            )
        except SystemExit as exc:
            if exc.code:
                raise

    print(output)
    clip_copy(output)
    print(":)")


if __name__ == "__main__":
    run(main())
