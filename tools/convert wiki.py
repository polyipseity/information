from aiohttp import ClientSession, TCPConnector
from anyio import Path
from asyncio import gather, run
from bs4 import BeautifulSoup, NavigableString, PageElement, Tag
from bs4.element import PreformattedString
from contextlib import contextmanager, suppress
from copy import copy
from jaraco.clipboard import paste_html  # type: ignore
from json import load
from logging import INFO, basicConfig
from os import chdir, getcwd, scandir, symlink
from pathlib import PurePath
from pyarchivist.Wikimedia_Commons.main import (
    Args as pyarchivist_Wikimedia_Commons_Args,
    main as pyarchivist_Wikimedia_Commons_main,
)
from pyperclip import copy as clip_copy  # type: ignore
from re import DOTALL, MULTILINE, Pattern, compile
from string import punctuation, whitespace
from sys import argv, version
from typing import Callable, Mapping, MutableSet
from urllib.parse import quote, unquote
from yarl import URL


@contextmanager
def _with_cwd(cwd: Path):
    old_cwd = getcwd()
    chdir(cwd)
    try:
        yield
    finally:
        chdir(old_cwd)


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
_MAX_CONCURRENT_REQUESTS_PER_HOST = 2
_LIST_INDENT = "    "
_MARKDOWN_SEPARATOR_CHARACTERS = f"{punctuation}{whitespace}\xa0".translate(
    {
        ord("/"): "",
        ord("_"): "",
    }
)
_MARKDOWN_SEPARATOR = "<!-- markdown separator -->"
_PAGE_DOES_NOT_EXIST_SUFFIX = " (page does not exist)"
_BAD_TITLES = frozenset({"Edit this at Wikidata"})
_IGNORED_NAME_PREFIXES = frozenset[str]()
_PRESERVED_PAGE_PREFIXES = {
    "Category:": f"{_WIKI_HOST_URL}/wiki/Category:{{}}",
    "File:": f"{_WIKI_HOST_URL}/wiki/File:{{}}",
    "Help:": f"{_WIKI_HOST_URL}/wiki/Help:{{}}",
    "Portal:": f"{_WIKI_HOST_URL}/wiki/Portal:{{}}",
    "Special:": f"{_WIKI_HOST_URL}/wiki/Special:{{}}",
    "Talk:": f"{_WIKI_HOST_URL}/wiki/Talk:{{}}",
    "Template:": f"{_WIKI_HOST_URL}/wiki/Template:{{}}",
    "Template talk:": f"{_WIKI_HOST_URL}/wiki/Template%20talk:{{}}",
    "Wikipedia:": f"{_WIKI_HOST_URL}/wiki/Wikipedia:{{}}",
    "commons:": "https://commons.wikimedia.org/wiki/{}",
    "oeis:": "https://oeis.org/{}",
    "q:": "https://en.wikiquote.org/wiki/{}",
    "v:": "https://en.wikiversity.org/wiki/{}",
    "wikibooks:": "https://en.wikibooks.org/wiki/{}",
    "wikiversity:": "https://en.wikiversity.org/wiki/{}",
    "wikt:": "https://en.wiktionary.org/wiki/{}",
    "wiktionary:": "https://en.wiktionary.org/wiki/{}",
}
_ARCHIVE_REGEXES = {
    compile(
        r"^https://upload.wikimedia.org/wikipedia/[^/]*/[0-9a-f]/[0-9a-f]{2}/([^/]*)$"
    ): ("File:{}", "../../archives/Wikimedia Commons/{}"),
    compile(
        r"^https://upload.wikimedia.org/wikipedia/[^/]*/thumb/[0-9a-f]/[0-9a-f]{2}/([^/]*)/.*$"
    ): ("File:{}", "../../archives/Wikimedia Commons/{}"),
    compile(
        r"^https://upload.wikimedia.org/wikipedia/[^/]*/transcoded/[0-9a-f]/[0-9a-f]{2}/([^/]*)/.*$"
    ): ("File:{}", "../../archives/Wikimedia Commons/{}"),
    compile(r"^https://[^\.]*.?wikipedia.org/wiki/File:(.*)$"): (
        "File:{}",
        "../../archives/Wikimedia Commons/{}",
    ),
}
_CONVERTED_WIKI_DIRECTORY = Path("../general")
_CONVERTED_WIKI_LANGUAGE_DIRECTORY = _CONVERTED_WIKI_DIRECTORY / "eng"

with open(f"{NAME}.names map.json", "rt", encoding="UTF-8") as names_map_file:
    _names_map_manual: dict[str, str] = load(names_map_file)
_names_map = {
    key: val
    for entry in scandir(_CONVERTED_WIKI_DIRECTORY)
    if (filename := entry.name).endswith(".md")
    for key, val in (
        (f"{filename[:1].upper()}{filename[1:-3]}", filename[:-3]),
        (
            f"{filename[:1].upper()}{filename[1:-3]}".replace("'", "’"),
            filename[:-3].replace("'", "’"),
        ),
        (f"{filename[:1].lower()}{filename[1:-3]}", filename[:-3]),
        (
            f"{filename[:1].lower()}{filename[1:-3]}".replace("'", "’"),
            filename[:-3].replace("'", "’"),
        ),
    )
}
if _names_map_overlap := frozenset(_names_map).intersection(_names_map_manual):
    raise ValueError(_names_map_overlap)
_NAMES_MAP = _names_map | _names_map_manual


def _bs4_new_element(tag_str: str) -> PageElement:
    soup = BeautifulSoup(tag_str, "html.parser")
    return soup.contents[0].extract()


def _fix_name_maybe(
    name: str,
    *,
    normalize: bool = True,
    replace_underscores: bool = False,
) -> str:
    if normalize:
        name = name.replace("\u00a0", " ")
    if (ret := _NAMES_MAP.get(name)) is not None:
        return ret
    if replace_underscores:
        name = name.replace("_", " ")
    ret = _NAMES_MAP.get(
        name,
        (
            f"{name[:1].lower()}{name[1:]}"
            if len(name) <= 1 or name[1:].islower()
            else name
        ),
    )
    return ret


def _fix_filename(
    filename: str,
    *,
    __BAD_CHARACTERS: Pattern[str] = compile(r"[/:\\]"),
) -> str:
    return __BAD_CHARACTERS.sub("_", filename)


def _markdown_fragment(fragment: str) -> str:
    return (
        fragment
        and f"#{fragment.replace(':', '').replace(' ', '%20').replace('/', '%2F')}"
    )


def _markdown_link_target(page: str, fragment: str) -> str:
    return f"{_fix_filename(page).replace(' ', '%20')}.md{_markdown_fragment(fragment)}"


def _tag_affixes(name: str) -> tuple[str, str]:
    return f"<{name}>", f"</{name}>"


async def wiki_html_to_plaintext(
    ele: PageElement,
    *,
    out_to_archive: MutableSet[str],
    list_stack: tuple[int, ...] = (),
    escape: bool = True,
    refs: bool,
    session: ClientSession,
    __HEADER_REGEX: Pattern[str] = compile(r"h(\d?)"),
    __BOLD_FONT_STYLE_REGEX: Pattern[str] = compile(r"font-weight: *bold"),
    __ITALIC_FONT_STYLE_REGEX: Pattern[str] = compile(r"font-style: *italic"),
    __MARKDOWN_ESCAPE_REGEX: Pattern[str] = compile(r"[#$()*<>\\[\\\]_`|]"),
    __PROCESS_STRINGS_BI_REGEX: Pattern[str] = compile(r"^( *)(.*?)( *)$", DOTALL),
    __REF_CONTENT_REGEX: Pattern[str] = compile(r"\[([^]]*)\]"),
    __CONSECUTIVE_NEWLINES_REGEX: Pattern[str] = compile(r"\n+"),
    __CONSECUTIVE_LEADING_WHITESPACES_REGEX: Pattern[str] = compile(
        r"^[ \t]+", MULTILINE
    ),
    __TABLE_IN_TABLE_HEADER_REGEX: Pattern[str] = compile(r"\| (__.*?__) \|"),
    __TABLE_IN_TABLE_LEADING_VERTICAL_REGEX: Pattern[str] = compile(r"\s*\|"),
    __TABLE_IN_TABLE_TRAILING_VERTICAL_REGEX: Pattern[str] = compile(r"\|\s*"),
) -> str:
    def escape_markdown(text: str):
        return __MARKDOWN_ESCAPE_REGEX.sub(lambda match: Rf"\{match[0]}", text)

    if not isinstance(ele, Tag):
        return (
            (escape_markdown(ele) if escape else ele)
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
            ref_str = "".join(ele.stripped_strings)
            if ref_content := __REF_CONTENT_REGEX.search(ref_str):
                ref_content = ref_content[1]
                return f"<sup>[{escape_markdown(f'[{ref_content}]')}]({_markdown_fragment(f'^ref-{ref_content}')})</sup>"
        else:
            return ""

    process_strings: Callable[[str], str] = lambda strings: strings
    joiner, prefix, suffix = "", "", ""
    match ele.name:
        # newlines
        case "br":
            process_strings = lambda strings: f"{strings}\n"
        # headers; should come before bold
        case name if header_match := __HEADER_REGEX.match(name):
            prefix, suffix = f"{'#' * int(header_match[1] or '1')} ", "\n\n"
            process_strings = lambda strings: _fix_name_maybe(strings.strip())
        # links: self-links; should come before bold
        case _ if ele.name == "a" and "mw-selflink" in classes:
            process_strings = lambda strings: strings.strip().replace("\n", " <br/> ")
            prefix, suffix = (
                "[",
                f"]({_WIKI_HOST_URL / 'wiki/Help:Self_link'})",
            )
        # bold, italic, bold & italic
        case _ if (
            ele.name in {"b", "i", "strong"}
            or __BOLD_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
            or __ITALIC_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
        ):
            bold = (
                ele.name in {"b", "strong"}
                or __BOLD_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
                and "mw-heading" not in classes
            )
            italic = ele.name in {"i"} or __ITALIC_FONT_STYLE_REGEX.search(
                str(ele.get("style", ""))
            )
            bold = "__" if bold else ""
            italic = "_" if italic else ""

            prefix, suffix = f"{bold}{italic}", f"{italic}{bold}"
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

            def process_strings_bi(strings: str):
                nonlocal prefix, suffix
                match = __PROCESS_STRINGS_BI_REGEX.match(strings)
                assert match
                prefix = f"{match[1]}{prefix}"
                suffix += match[3]
                return match[2]

            process_strings = process_strings_bi
        # literal tags
        case "s" | "sub" | "sup" | "u":
            prefix, suffix = _tag_affixes(ele.name)
        # newlines
        case "div" | "dd" | "dt" | "p":  # <dl>
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
                alt_text = str(alt_text).strip()
                orig_alt_text_len = len(alt_text)
                alt_text = alt_text.removeprefix(R"{\displaystyle").lstrip()
                if len(alt_text) == orig_alt_text_len:
                    alt_text = alt_text.removeprefix(R"{\textstyle").lstrip()
                if len(alt_text) < orig_alt_text_len:
                    alt_text = (
                        alt_text.removesuffix(R"}")
                        # .rstrip() # The trailing space may be preceded by a backslash.
                    )
                if alt_text.endswith(R"\ "):
                    alt_text += "{}"
                else:
                    alt_text = alt_text.rstrip()
                alt_text = (
                    alt_text.replace(R":@:", R": @ :")
                    .replace(R"?@?", R"? @ ?")
                    .replace(R"{@{", R"{ @ {")
                    .replace(R"}@}", R"} @ }")
                )
                while (
                    alt_text_2 := alt_text.replace(R"{{", "{ {").replace(R"}}", "} }")
                ) != alt_text:
                    alt_text = alt_text_2

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

                prefix, suffix = "$" if inline else " $$", "$" if inline else "$$"

                if inline:
                    for char in ".,":
                        if alt_text.endswith(R"\,"):
                            continue
                        if alt_text.endswith(char):
                            suffix += alt_text[-1]
                            alt_text = alt_text[:-1]
                    alt_text = alt_text.rstrip()

                ele.clear()
                ele.append(alt_text)
        # lists
        case "ol":
            prefix, suffix = ("\n" if list_stack else "\n\n"), "\n\n"
            list_stack += (0,)
        case "ul":
            prefix, suffix = ("\n" if list_stack else "\n\n"), "\n\n"
            list_stack += (-1,)
        case "li":
            if list_stack and (item := list_stack[-1]) >= 1:
                prefix, suffix = f"{_LIST_INDENT * (len(list_stack) - 1)}{item}. ", "\n"
                if str(ele.get("id", "")).startswith("cite_"):

                    def process_strings_li_cite(strings: str):
                        try:
                            idx = strings.index("\n")
                        except ValueError:
                            idx = len(strings)
                        return f'{strings[:idx]} <a id="^ref-{item}"></a>^ref-{item}{strings[idx:].rstrip()}'

                    process_strings = process_strings_li_cite
            else:
                prefix, suffix = f"{_LIST_INDENT * (len(list_stack) - 1)}- ", "\n"
        # citations
        case "cite":
            if id := ele.get("id"):
                id = str(id).replace("_", " ")
                prefix = f'<a id="{id}"></a> '
        # tables
        case "tbody" | "thead":
            prefix, suffix = "\n", "\n\n"

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
            else:
                for child in ele.children:
                    if isinstance(child, Tag) and child.name == "th":
                        new_b = _bs4_new_element("<b></b>")
                        for child_child in child.contents[:]:
                            new_b.append(child_child.extract())
                        child.append(new_b)

        case "td" | "th":

            def process_strings_tdh(strings: str):
                strings = strings.strip()

                strings = __CONSECUTIVE_NEWLINES_REGEX.sub("\n", strings)
                strings = __CONSECUTIVE_LEADING_WHITESPACES_REGEX.sub(
                    lambda match: match[0]
                    .replace(" ", "&nbsp;")
                    .replace("\t", "&emsp;"),
                    strings,
                )

                # tables in tables
                strings = strings.replace("| |", "|")  # empty cells
                strings = __TABLE_IN_TABLE_HEADER_REGEX.sub(
                    lambda match: f"|{match[1]} <p> ", strings
                )
                strings = strings.replace("|\n|", " <p> ")
                strings = __TABLE_IN_TABLE_LEADING_VERTICAL_REGEX.sub(
                    lambda match: match[0][: -len("|")], strings
                )
                strings = __TABLE_IN_TABLE_TRAILING_VERTICAL_REGEX.sub(
                    lambda match: match[0][len("|") :], strings
                )
                strings = strings.replace("|", "&#124;")

                strings = strings.strip()
                strings = strings.replace("\n", " <br/> ")
                return strings

            process_strings = process_strings_tdh
        # audios
        case _ if {"mw-tmh-play", "oo-ui-buttonElement-button"} & classes:
            if src := ele.get("href"):

                def process_strings_audio(strings: str, ele: Tag = ele):
                    src_url = _WIKI_HOST_URL.join(URL(str(src)))
                    src_url_str = str(src_url)

                    for regex, formats in _ARCHIVE_REGEXES.items():
                        if not (match := regex.search(src_url.human_repr())):
                            continue
                        to_archive = unquote(match[1])
                        out_to_archive.add(formats[0].format(to_archive))
                        src_url_str = quote(
                            formats[1].format(to_archive.replace("_", " "))
                        )

                    embed = "!" if {"mw-tmh-player"} & classes else ""
                    return f"{embed}[{strings.strip()}]({src_url_str})"

                suffix = "\n\n"
                process_strings = process_strings_audio
        # images
        case _ if (
            ele.name == "img"
            and not {
                "mwe-math-fallback-image-display",
                "mwe-math-fallback-image-inline",
            }
            & classes
        ):
            if src := ele.get("src"):

                def process_strings_img(strings: str, ele: Tag = ele):

                    src_url = _WIKI_HOST_URL.join(URL(str(src)))
                    src_url_str = str(src_url)

                    for regex, formats in _ARCHIVE_REGEXES.items():
                        if not (match := regex.search(src_url.human_repr())):
                            continue
                        to_archive = unquote(match[1])
                        out_to_archive.add(formats[0].format(to_archive))
                        src_url_str = quote(
                            formats[1].format(to_archive.replace("_", " "))
                        )

                    return f"{strings}![{escape_markdown(str(ele.get("alt", "")).strip())}]({src_url_str})"

                suffix = "\n\n"
                process_strings = process_strings_img
        # links
        case _ if ele.name == "a" and "mw-file-description" not in classes:
            process = True
            if (title := ele.get("title")) and title not in _BAD_TITLES:
                title = str(title)
                if "new" in classes:
                    title = title.removesuffix(_PAGE_DOES_NOT_EXIST_SUFFIX)
                href = str(ele.get("href", ""))
                to_fragment = href.split("#", 1)[-1] if "#" in href else ""
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
                    # prefix, suffix = (
                    #     "[",
                    #     f"]({_markdown_link_target(_fix_name_maybe(
                    #         to, replace_underscores=True,
                    #     ), _fix_name_maybe(
                    #         to_fragment, replace_underscores=True,
                    #     ))})",
                    # )
                    from_filename, to_filename = _fix_name_maybe(
                        title, replace_underscores=True
                    ), _fix_name_maybe(to, replace_underscores=True)
                    prefix, suffix = (
                        "[",
                        f"]({_markdown_link_target(from_filename, _fix_name_maybe(to_fragment, replace_underscores=True))})",
                    )
                    from_filename, to_filename = _fix_filename(
                        from_filename
                    ), _fix_filename(to_filename)
                    if from_filename != to_filename:
                        redirect_file = (
                            _CONVERTED_WIKI_LANGUAGE_DIRECTORY / f"{from_filename}.md"
                        )
                        if not await redirect_file.exists():
                            # no async
                            with _with_cwd(_CONVERTED_WIKI_LANGUAGE_DIRECTORY):
                                with suppress(FileExistsError):
                                    # `src` <- `dst`
                                    symlink(
                                        f"{to_filename}.md",
                                        redirect_file.relative_to(
                                            _CONVERTED_WIKI_LANGUAGE_DIRECTORY
                                        ),
                                        target_is_directory=False,
                                    )
                            with _with_cwd(_CONVERTED_WIKI_DIRECTORY):
                                with suppress(FileExistsError):
                                    # `src` <- `dst`
                                    symlink(
                                        redirect_file.relative_to(
                                            _CONVERTED_WIKI_DIRECTORY
                                        ),
                                        f"{from_filename}.md",
                                        target_is_directory=False,
                                    )
            elif href := ele.get("href"):
                href = str(href)
                if href.startswith(f"{_WIKI_HOST_URL}/wiki/") and "#" in href:
                    href = _markdown_fragment(
                        _fix_name_maybe(
                            href[href.index("#") + 1 :], replace_underscores=True
                        )
                    )
                prefix, suffix = "[", f"]({href})"
            else:
                process = False

            if process:

                def process_strings_a(strings: str):
                    return strings.strip().replace("\n", " <br/> ")

                process_strings = process_strings_a
        # unhandled tags
        case _:
            pass

    if "hatnote" in classes:
        prefix = f"- {prefix.removesuffix('_')}"
        suffix = f"{suffix.removeprefix('_')}\n\n"

    # blockquotes: categories, figures, portals, ...
    if (
        ele.name == "figure"
        or {
            "catlinks",
            # "gallerybox",
            "math_theorem",
            "portalbox",
            "tmulti",
            "unsolved",
        }
        & classes
    ):

        def process_strings_blockquote(strings: str):
            return "".join(
                f">{line.strip() and ' '}{line}"
                for line in strings.strip().splitlines(keepends=True)
            )

        suffix = "\n\n"
        process_strings = process_strings_blockquote

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
                escape=ele.name not in {"code", "math"},
                refs=refs,
                session=session,
            )

    strings = joiner.join(await gather(*process_children()))
    strings = process_strings(strings)

    return strings and f"{prefix}{strings}{suffix}"


async def main() -> None:
    refs = "--no-refs" not in argv[1:]

    input("HTML (will read from clipboard)? ")
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
            html,
            out_to_archive=out_to_archive,
            session=session,
            refs=refs,
        )
    output = (
        output.replace("\xa0", " ")  # replace non-breaking spaces with spaces
        .replace("\u200a", "&hairsp;")  # replace hair spaces with its HTML entity
        .strip()
    )

    if out_to_archive:
        try:
            basicConfig(level=INFO)
            await pyarchivist_Wikimedia_Commons_main(
                pyarchivist_Wikimedia_Commons_Args(
                    inputs=tuple(out_to_archive),
                    dest=Path("../archives/Wikimedia Commons/"),
                    index=Path("../archives/Wikimedia Commons/index.md"),
                    ignore_individual_errors=True,
                )
            )
        except SystemExit:
            pass

    print(output)
    clip_copy(output)
    print(":)")


if __name__ == "__main__":
    run(main())
