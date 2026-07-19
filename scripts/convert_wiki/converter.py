"""Core Wikipedia HTML-to-Markdown converter.

Contains ``WikiHtmlConverter``, the main class that walks a BeautifulSoup
HTML tree and emits Markdown text via tag-specific handler methods.
"""

import re
from collections.abc import Awaitable, Iterator, Mapping, MutableSet
from contextlib import suppress
from copy import copy
from os import PathLike
from urllib.parse import quote, unquote

from anyio import Path
from asyncer import SoonValue, create_task_group
from bs4 import BeautifulSoup, NavigableString, PageElement, Tag
from bs4.element import PreformattedString
from country_converter import convert
from yarl import URL

from . import config as _cfg
from .types import _HandlerConfig, _RedirectInfo
from .utils import (
    _balance_brackets,
    _bs4_new_element,
    _fix_filename,
    _fix_name_maybe,
    _get_image_filename,
    _markdown_fragment,
    _markdown_link_target,
    _tag_affixes,
)

"""Exported names from this module."""
__all__ = ()

#: Regex for matching header tags (``h1``, ``h2``, etc.).
_HEADER_REGEX = re.compile(r"^h(\d)$")
#: Tags that render as bold or italic.
_BOLD_OR_ITALIC = frozenset({"b", "em", "i", "strong"})
#: Table cell tag names.
_TD_OR_TH = frozenset({"td", "th"})
#: Text-align style extractor.
_TEXT_ALIGN_REGEX = re.compile(
    r"\btext-align\s*:\s*(left|center|right)\b", re.IGNORECASE
)
#: Bold font-weight style detector.
_BOLD_FONT_STYLE_REGEX = re.compile(r"\bfont-weight\s*:\s*bold\b", re.IGNORECASE)
#: Italic font-style detector.
_ITALIC_FONT_STYLE_REGEX = re.compile(r"\bfont-style\s*:\s*italic\b", re.IGNORECASE)
#: Collapse runs of empty blockquote lines.
_COLLAPSE_EMPTY_BLOCKQUOTE_RE = re.compile(r">\n(?:>\n)+")
#: Collapse consecutive spaces.
_COLLAPSE_SPACES_REGEX = re.compile(r" {2,}")
#: Captures the separator-prefixed display text in bold/italic processing.
_PROCESS_STRINGS_BI_REGEX = re.compile(r"^( *)(.*?)([\n ]*)$", re.DOTALL)
#: Extract reference content from ``str.strip()``-style dumps.
_REF_CONTENT_REGEX = re.compile(r"\[(.+?)]")
#: Consecutive newline runs.
_CONSECUTIVE_NEWLINES_REGEX = re.compile(r"\n\n+")
#: Leading whitespace lines at the start of a cell.
_CONSECUTIVE_LEADING_WHITESPACES_REGEX = re.compile(r"(?:^|\n)([ \t]+)", re.MULTILINE)
#: ``| __bold__ |`` bold table headers separated by spaces.
_TABLE_IN_TABLE_HEADER_REGEX = re.compile(r"\| (__.*?__) \|")
#: ``|`` that shouldn't be consumed as part of a pipe table cell.
_TABLE_IN_TABLE_LEADING_VERTICAL_REGEX = re.compile(r"\s*\|")
_TABLE_IN_TABLE_TRAILING_VERTICAL_REGEX = re.compile(r"\|\s*")
#: Whitespace and separator chars for sidebar tight wrapping.
_SIDEBAR_TIGHT_WRAPPING_RE = re.compile(r"[ \t]+", re.MULTILINE)
#: Markdown separator character set used for emphasis adjacency.
_MARKDOWN_SEPARATOR = "<!-- markdown separator -->"


class WikiHtmlConverter:
    """Converts Wikipedia HTML elements to Markdown text.

    Parameters
    ----------
    converted_wiki_dir:
        Directory where converted Wikipedia Markdown notes are stored
        (used for symlink creation on redirects).
    converted_wiki_lang_dir:
        Language-specific subdirectory for converted notes.
    """

    def __init__(
        self,
        *,
        converted_wiki_dir: PathLike[str] = _cfg._CONVERTED_WIKI_DIRECTORY,
        converted_wiki_lang_dir: PathLike[
            str
        ] = _cfg._CONVERTED_WIKI_LANGUAGE_DIRECTORY,
        image_metadata: Mapping[str, str] | None = None,
        names_map: Mapping[str, str] | None = None,
    ) -> None:
        """Initialize converter with directory paths and name map."""
        self._converted_wiki_dir = Path(converted_wiki_dir)
        self._converted_wiki_lang_dir = Path(converted_wiki_lang_dir)
        self._image_metadata = image_metadata or {}
        self._names_map = names_map or _cfg._NAMES_MAP

    async def convert(
        self,
        ele: PageElement,
        *,
        out_to_archive: MutableSet[str],
        list_stack: tuple[int, ...] = (),
        escape: bool = True,
        refs: bool,
        redirect_map: Mapping[str, _RedirectInfo],
    ) -> str:
        """Convert a Wikipedia HTML element tree to a Markdown string."""

        # ---- Formatting-agnostic principle ----
        # HTML-to-Markdown conversion must be invariant under formatting
        # whitespace in the HTML source. All NavigableString text nodes
        # must have their interior formatting whitespace (newlines, tabs,
        # carriage returns) normalized to a single space before any
        # further processing. Structural whitespace from <br>, <p>, <li>,
        # block-level suffixes, and similar semantic elements is injected
        # by the tag handler configs, not the text nodes. Keeping
        # normalization in the NavigableString handler and ensuring all
        # process_strings callbacks downstream only react to structural
        # newlines guarantees this property.

        def escape_markdown(text: str) -> str:
            """Escape Markdown special characters in text."""
            return _cfg._MARKDOWN_ESCAPE_REGEX.sub(lambda match: Rf"\{match[0]}", text)

        # Strip <style> tags — CSS is never content in any conversion context.
        if isinstance(ele, Tag):
            for style_tag in ele.find_all("style"):
                style_tag.decompose()

        if not isinstance(ele, Tag):
            if (
                isinstance(ele, NavigableString)
                and not isinstance(ele, PreformattedString)
                and not isinstance(ele.parent, BeautifulSoup)
            ):
                text = str(ele)
                # See the formatting-agnostic principle documented above.
                text = text.translate(str.maketrans({c: " " for c in "\t\n\r\x0b\x0c"}))
                text = _COLLAPSE_SPACES_REGEX.sub(" ", text)
                if all(c in "\t\n\r\x0b\x0c " for c in text):
                    return ""
                return escape_markdown(text) if escape else text
            return ""

        classes = frozenset(ele.get_attribute_list("class"))
        if {"mw-cite-backlink", "mw-editsection"} & classes:
            return ""

        if "reference" in classes:
            if refs:
                ref_str = "".join(ele.stripped_strings)
                if ref_content := _REF_CONTENT_REGEX.search(ref_str):
                    ref_content = ref_content[1]
                    return (
                        f"<sup>[{escape_markdown(f'[{ref_content}]')}]"
                        f"({_markdown_fragment(f'^ref-{ref_content}')})</sup>"
                    )
            else:
                return ""

        self._out_to_archive = out_to_archive
        self._redirect_map = redirect_map

        config = await self._dispatch(ele, classes, list_stack=list_stack)
        if config is None:
            config = _HandlerConfig()

        joiner = config.joiner
        process_strings = config.process_strings
        if config.list_stack is not None:
            list_stack = config.list_stack

        if "hatnote" in classes:
            config.prefix = f"- {config.prefix.removesuffix('_')}"
            next_sib = ele.find_next_sibling()
            if isinstance(next_sib, Tag) and (
                next_sib.name == "figure"
                or {"catlinks", "math_theorem", "portalbox", "tmulti", "unsolved"}
                & frozenset(next_sib.get_attribute_list("class"))
            ):
                config.suffix = f"{config.suffix.removeprefix('_')}\n\n"
            else:
                config.suffix = f"{config.suffix.removeprefix('_')}\n"
            original_process = process_strings

            def _hatnote_process(strings: str) -> str:
                """Process hatnote text by stripping leading whitespace."""
                return original_process(strings).lstrip("\n ")

            process_strings = _hatnote_process

        if {"sidebar-navbar", "navbar"} & classes:
            parent = ele.parent
            while parent is not None:
                parent_classes = parent.get_attribute_list("class")
                if "sidebar-navbar" in parent_classes or "navbar" in parent_classes:
                    break
                parent = parent.parent
            if parent is None:
                original_process = process_strings

                def process_strings_comment(strings: str) -> str:
                    """Wrap processed text in HTML comment markers."""
                    result = original_process(strings).strip()
                    return f"<!-- {result} --> " if result else result

                process_strings = process_strings_comment
                config.prefix = ""
                config.suffix = ""

        if (
            ele.name == "figure"
            or {
                "catlinks",
                "math_theorem",
                "portalbox",
                "tmulti",
                "unsolved",
            }
            & classes
        ):
            original_process = process_strings
            _catlinks = "catlinks" in classes

            def process_strings_blockquote(strings: str) -> str:
                """Collapse whitespace runs within blockquote content."""
                strings = original_process(strings)
                if _catlinks:
                    strings = "\n\n".join(
                        "\n".join(" ".join(line.split()) for line in para.split("\n"))
                        for para in strings.split("\n\n")
                    )
                else:
                    strings = "\n\n".join(
                        " ".join(para.split()) for para in strings.split("\n\n")
                    )
                result = "".join(
                    f">{line.strip() and ' '}{line}"
                    for line in strings.strip().splitlines(keepends=True)
                )
                return _COLLAPSE_EMPTY_BLOCKQUOTE_RE.sub(">\n", result)

            config.suffix = "\n\n"
            process_strings = process_strings_blockquote

        def process_children() -> Iterator[Awaitable[str]]:
            """Process child elements concurrently using task groups."""
            nonlocal list_stack
            for child in ele.children:
                if (
                    list_stack
                    and list_stack[-1] >= 0
                    and isinstance(child, Tag)
                    and child.name == "li"
                ):
                    list_stack = (*list_stack[:-1], list_stack[-1] + 1)
                yield self.convert(
                    child,
                    out_to_archive=out_to_archive,
                    list_stack=list_stack,
                    escape=escape and ele.name not in {"code", "math"},
                    refs=refs,
                    redirect_map=redirect_map,
                )

        soon_values: list[SoonValue[str]] = []
        async with create_task_group() as tg:
            for coro in process_children():

                async def _run(c=coro) -> str:
                    """Await and return a single coroutine result."""
                    return await c

                soon_values.append(tg.soonify(_run)())

        strings = joiner.join(sv.value for sv in soon_values)
        if config.full_result:
            return process_strings(strings) or ""
        strings = process_strings(strings)
        return strings and f"{config.prefix}{strings}{config.suffix}"

    async def _dispatch(
        self,
        ele: Tag,
        classes: frozenset[str],
        *,
        list_stack: tuple[int, ...],
    ) -> _HandlerConfig | None:
        """Dispatch to a handler for the given element."""
        if header_match := _HEADER_REGEX.match(ele.name):
            return self._handle_header(ele, classes, header_match)

        if ele.name == "a" and "mw-selflink" in classes:
            return self._handle_selflink(ele, classes)

        if "hatnote" not in classes and (
            ele.name in _BOLD_OR_ITALIC
            or _BOLD_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
            or _ITALIC_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
        ):
            return self._handle_bold_italic(ele, classes)

        if {"mw-tmh-play", "oo-ui-buttonElement-button"} & classes:
            return self._handle_audio(ele, classes)

        if (
            ele.name == "img"
            and not {
                "mwe-math-fallback-image-display",
                "mwe-math-fallback-image-inline",
            }
            & classes
        ):
            return self._handle_image(ele, classes)

        if ele.name == "a" and "mw-file-description" not in classes:
            return await self._handle_link(ele, classes)

        if ele.name == "ol":
            return self._handle_ol(ele, classes, list_stack)
        if ele.name == "ul" and "portalbox" in classes:
            return self._handle_portalbox(ele, classes)
        if ele.name == "ul":
            return self._handle_ul(ele, classes, list_stack)
        if ele.name == "li":
            return self._handle_li(ele, classes, list_stack)

        handler = getattr(self, f"_handle_{ele.name}", None)
        if handler is not None:
            return handler(ele, classes)

        return None

    # --- Tag handlers ---

    def _handle_br(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig | None:
        """Render a <br> tag as a newline."""

        def process(strings: str) -> str:
            """Append newline to strings."""
            return f"{strings}\n"

        return _HandlerConfig(process_strings=process)

    def _handle_header(
        self, ele: Tag, classes: frozenset[str], header_match: re.Match[str]
    ) -> _HandlerConfig:
        """Render a heading with Markdown # markers."""
        level = int(header_match[1] or "1")
        prefix = f"{'#' * level} "
        suffix = "\n\n"

        def process(strings: str) -> str:
            """Fix name casing in heading text."""
            return _fix_name_maybe(strings.strip(), names_map=self._names_map)

        return _HandlerConfig(prefix=prefix, suffix=suffix, process_strings=process)

    def _handle_selflink(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render a self-link as a relative Markdown link."""
        href = str(ele.get("href", ""))
        wiki_prefix = f"{_cfg._WIKI_HOST_URL}/wiki/"
        if href.startswith(wiki_prefix):
            title = unquote(href[len(wiki_prefix) :].split("#")[0]).replace("_", " ")
        elif href.startswith("/wiki/"):
            title = unquote(href[6:].split("#")[0]).replace("_", " ")
        else:
            return _HandlerConfig()
        info = self._redirect_map.get(title, _RedirectInfo(to=title))
        to = info.to
        to_filename = _fix_name_maybe(
            to, replace_underscores=True, names_map=self._names_map
        )
        target = _markdown_link_target(
            to_filename,
            _fix_name_maybe(
                info.tofragment,
                replace_underscores=True,
                names_map=self._names_map,
            ),
        )

        def process(strings: str) -> str:
            """Strip and flatten self-link display text."""
            return strings.strip().replace("\n", " <br/> ")

        return _HandlerConfig(
            prefix="[",
            suffix=f"]({target})",
            process_strings=process,
        )

    @staticmethod
    def _needs_separator_before(sibling: PageElement | None) -> bool:
        return (
            isinstance(sibling, NavigableString)
            and sibling.rstrip(_cfg._MARKDOWN_SEPARATOR_CHARACTERS) == sibling
        )

    @staticmethod
    def _needs_separator_after(sibling: PageElement | None) -> bool:
        return (
            isinstance(sibling, NavigableString)
            and sibling.lstrip(_cfg._MARKDOWN_SEPARATOR_CHARACTERS) == sibling
        )

    def _handle_bold_italic(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render bold/italic text with Markdown emphasis markers."""
        bold = (
            ele.name in {"b", "strong"}
            or _BOLD_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
            and "mw-heading" not in classes
        )
        italic = ele.name in {"em", "i"} or _ITALIC_FONT_STYLE_REGEX.search(
            str(ele.get("style", ""))
        )
        bold_str = "__" if bold else ""
        italic_str = "_" if italic else ""
        prefix = f"{bold_str}{italic_str}"
        suffix = f"{italic_str}{bold_str}"
        if "sidebar-title-with-pretitle" in classes:
            prefix = f"{bold_str}<big>"
            suffix = f"</big>{bold_str}"

        if self._needs_separator_before(ele.previous_sibling):
            prefix = f"{_MARKDOWN_SEPARATOR}{prefix}"
        if self._needs_separator_after(ele.next_sibling):
            suffix += _MARKDOWN_SEPARATOR

        config = _HandlerConfig(prefix=prefix, suffix=suffix, full_result=False)

        def process(strings: str) -> str:
            """Handle separator characters around bold/italic regions."""
            match = _PROCESS_STRINGS_BI_REGEX.match(strings)
            if not match:
                return strings
            config.prefix = f"{match[1]}{config.prefix}"
            config.suffix += match[3]
            return match[2]

        config.process_strings = process
        if ele.name in _TD_OR_TH:
            original_process = config.process_strings

            def cell_process(strings: str) -> str:
                """Apply table cell processing for bold headers/cells."""
                return self._process_table_cell(original_process(strings))

            config.process_strings = cell_process
        return config

    def _handle_s(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render <s> as strikethrough Markdown."""
        prefix, suffix = _tag_affixes("s")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _handle_sub(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render <sub> as subscript Markdown."""
        prefix, suffix = _tag_affixes("sub")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _handle_sup(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render <sup> as superscript Markdown."""
        prefix, suffix = _tag_affixes("sup")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _handle_u(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render <u> as underline."""
        prefix, suffix = _tag_affixes("u")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _handle_big(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render <big> text."""
        prefix, suffix = _tag_affixes("big")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    @staticmethod
    def _merge_header_rows(ele: Tag) -> None:
        """Merge consecutive header rows in <tbody> into a single row."""
        trs = [c for c in ele.children if isinstance(c, Tag) and c.name == "tr"]
        header_trs: list[Tag] = []
        target_tr: Tag | None = None
        seen_th = False

        for tr in trs:
            cells = [
                c for c in tr.children if isinstance(c, Tag) and c.name in _TD_OR_TH
            ]
            if not cells:
                continue
            all_th = all(c.name == "th" for c in cells)
            if all_th:
                header_trs.append(tr)
                target_tr = tr
                seen_th = True
            elif not seen_th:
                header_trs.append(tr)
            else:
                break

        if target_tr is None or len(header_trs) <= 1:
            return

        for tr in header_trs:
            if tr is target_tr:
                continue
            extra_cells = [
                c for c in tr.children if isinstance(c, Tag) and c.name in _TD_OR_TH
            ]
            target_cells = [
                c
                for c in target_tr.children
                if isinstance(c, Tag) and c.name in _TD_OR_TH
            ]

            for i, extra_cell in enumerate(extra_cells):
                if i < len(target_cells):
                    target_cell = target_cells[i]
                    children = list(extra_cell.children)
                    if children:
                        br = _bs4_new_element("<br/>")
                        target_cell.insert(0, br)
                        for child in reversed(children):
                            target_cell.insert(0, child.extract())

            tr.decompose()

    @staticmethod
    def _in_table_cell(ele: Tag) -> bool:
        """Check if element is nested inside a <td> or <th>."""
        return any(isinstance(p, Tag) and p.name in _TD_OR_TH for p in ele.parents)

    @staticmethod
    def _in_navbox(ele: Tag) -> bool:
        """Check if element is inside a navbox table."""
        return any(
            isinstance(p, Tag) and "navbox" in (p.get("class") or [])
            for p in ele.parents
        )

    def _handle_block_level(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle block-level elements with spacing suffix."""
        suffix = "\n\n" if self._in_table_cell(ele) else ""
        return _HandlerConfig(suffix=suffix)

    _handle_div = _handle_block_level
    _handle_dd = _handle_block_level
    _handle_dt = _handle_block_level

    def _handle_p(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render a <p> paragraph with appropriate spacing."""

        def process(strings: str) -> str:
            """Collapse whitespace runs in paragraph text."""
            return " ".join(strings.split())

        in_table = self._in_table_cell(ele)
        prefix = "\n" if not in_table else ""
        suffix = "" if in_table else "\n\n"
        return _HandlerConfig(prefix=prefix, suffix=suffix, process_strings=process)

    def _handle_code(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render inline <code> with backtick markers."""

        def process(strings: str) -> str:
            """Wrap code text in backtick delimiters."""
            delimiter = "`"
            while delimiter in strings:
                delimiter += "`"
            if strings.startswith("`") or strings.endswith("`"):
                strings = f" {strings} "
            return f"{delimiter}{strings}{delimiter}"

        return _HandlerConfig(process_strings=process)

    @staticmethod
    def _is_inline_math(ele: Tag) -> bool:
        """Determine if a <math> element should use inline $ delimiters."""
        parent = ele.parent
        if not parent or "inline" not in str(parent.get("class", "")):
            return False
        for _ in range(2):
            parent = parent.parent
            if parent is None:
                return False
        return len(parent) > 1

    @staticmethod
    def _strip_trailing_punctuation(text: str) -> tuple[str, str]:
        """Strip . or , from the end of inline math, preserving \\,."""
        suffix = ""
        for char in ".,":
            if text.endswith(R"\,"):
                continue
            if text.endswith(char):
                suffix += text[-1]
                text = text[:-1]
        return text.rstrip(), suffix

    @staticmethod
    def _escape_flashcard_delimiters(text: str) -> str:
        """Insert spaces around flashcard and LaTeX delimiters inside math."""
        text = (
            text.replace(":@:", ": @ :")
            .replace("?@?", "? @ ?")
            .replace("{@{", "{ @ {")
            .replace("}@}", "} @ }")
        )
        while True:
            new_text = text.replace("{{", "{ {").replace("}}", "} }")
            if new_text == text:
                break
            text = new_text
        return text

    def _handle_math(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render <math> elements with LaTeX delimiters."""
        prefix = suffix = ""
        if alt_text := ele.get("alttext"):
            alt_text = str(alt_text).strip()
            for _prefix in (R"{\displaystyle", R"{\textstyle"):
                if alt_text.startswith(_prefix):
                    alt_text = alt_text.removeprefix(_prefix).lstrip()
                    alt_text = alt_text.removesuffix(R"}")
                    break
            if alt_text.endswith(R"\ "):
                alt_text += "{}"
            else:
                alt_text = alt_text.rstrip()
            alt_text = self._escape_flashcard_delimiters(alt_text)

            inline = self._is_inline_math(ele)
            prefix, suffix = (
                "$" if inline else " $$",
                "$" if inline else "$$",
            )

            if inline:
                alt_text, punct = self._strip_trailing_punctuation(alt_text)
                suffix += punct

            ele.clear()
            ele.append(alt_text)

        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _list_prefix_suffix(
        self,
        ele: Tag,
        classes: frozenset[str],
        list_stack: tuple[int, ...],
        *,
        references_override: bool = False,
    ) -> tuple[str, str]:
        """Compute prefix/suffix for list items based on nesting level."""
        if self._in_table_cell(ele):
            is_sub_list = any(
                isinstance(p, Tag) and p.name == "li" for p in ele.parents
            )
            if is_sub_list or (references_override and "references" in classes):
                if references_override and "references" in classes:
                    prefix = ""
                elif list_stack:
                    prefix = "\n"
                else:
                    prefix = "\n\n"
                suffix = ""
            else:
                prefix = ""
                suffix = ""
        else:
            if references_override and "references" in classes:
                prefix = ""
            elif list_stack:
                prefix = "\n"
            else:
                prefix = "\n\n"
            suffix = "\n\n"
        return prefix, suffix

    def _handle_ol(
        self,
        ele: Tag,
        classes: frozenset[str],
        list_stack: tuple[int, ...],
    ) -> _HandlerConfig:
        """Handle ordered list <ol> elements."""
        prefix, suffix = self._list_prefix_suffix(
            ele, classes, list_stack, references_override=True
        )
        return _HandlerConfig(
            prefix=prefix,
            suffix=suffix,
            list_stack=(*list_stack, 0),
        )

    def _handle_portalbox(
        self, ele: Tag, classes: frozenset[str]
    ) -> _HandlerConfig | None:
        """Handle portal box elements as inline content."""
        if ele.name != "ul":
            return None

        def process(strings: str) -> str:
            """Strip list prefixes and join portal items inline."""
            lines = [line.strip() for line in strings.split("\n")]
            parts = [
                line.removeprefix("- ").removeprefix("* ") for line in lines if line
            ]
            return " ".join(parts)

        return _HandlerConfig(process_strings=process)

    def _handle_ul(
        self,
        ele: Tag,
        classes: frozenset[str],
        list_stack: tuple[int, ...],
    ) -> _HandlerConfig:
        """Handle unordered list <ul> elements."""
        prefix, suffix = self._list_prefix_suffix(ele, classes, list_stack)
        return _HandlerConfig(
            prefix=prefix,
            suffix=suffix,
            list_stack=(*list_stack, -1),
        )

    def _handle_li(
        self,
        ele: Tag,
        classes: frozenset[str],
        list_stack: tuple[int, ...],
    ) -> _HandlerConfig:
        """Handle list item <li> elements."""
        item = list_stack[-1] if list_stack else -1
        if self._in_table_cell(ele) and ele.find(("ul", "ol")) is not None:
            li_suffix = ""
        else:
            li_suffix = "\n"
        if item >= 1:
            prefix = f"{_cfg._LIST_INDENT * (len(list_stack) - 1)}{item}. "
            if str(ele.get("id", "")).startswith("cite_"):

                def process(strings: str, item: int = item) -> str:
                    """Process citation list items with anchor markers."""
                    strings = strings.lstrip("\t\n\r\x0b\x0c \xa0")
                    try:
                        idx = strings.index("\n")
                    except ValueError:
                        idx = len(strings)
                    return f'{strings[:idx]} <a id="^ref-{item}"></a>^ref-{item}{strings[idx:].rstrip()}'

                return _HandlerConfig(
                    prefix=prefix,
                    suffix=li_suffix,
                    process_strings=process,
                )
            return _HandlerConfig(prefix=prefix, suffix=li_suffix)
        else:

            def process(strings: str) -> str:
                """Remove leading/trailing formatting spaces."""
                return strings.strip(" \t\n\r\x0b\x0c")

            return _HandlerConfig(
                prefix=f"{_cfg._LIST_INDENT * (len(list_stack) - 1)}- ",
                suffix=li_suffix,
                process_strings=process,
            )

    def _handle_cite(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <cite> citation elements."""
        prefix = ""
        if ele_id := ele.get("id"):
            ele_id = str(ele_id).replace("_", " ")
            prefix = f'<a id="{ele_id}"></a> '
        return _HandlerConfig(prefix=prefix)

    def _handle_tbody(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <tbody> table body elements."""
        self._normalize_table_cells(ele)
        self._merge_header_rows(ele)
        return _HandlerConfig(prefix="\n", suffix="\n\n")

    def _handle_thead(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <thead> table head elements."""
        self._normalize_table_cells(ele)
        return _HandlerConfig(prefix="\n", suffix="\n\n")

    @staticmethod
    def _normalize_table_cells(ele: Tag) -> None:
        """Normalize table cell layout for consistent column count."""
        for tdh in tuple(ele.find_all(_TD_OR_TH)):
            assert isinstance(tdh, Tag)
            col_span = str(tdh.get("colspan", "1"))
            try:
                col_span = int(col_span)
            except ValueError:
                pass
            else:
                tdh["colspan"] = "1"
                navbox = any(
                    isinstance(p, Tag) and "navbox" in (p.get("class") or [])
                    for p in tdh.parents
                )
                for _ in range(1, col_span):
                    new_tdh = copy(tdh)
                    if "style" in new_tdh.attrs:
                        del new_tdh.attrs["style"]
                    new_tdh.clear()
                    if navbox:
                        tdh.insert_before(new_tdh)
                    else:
                        tdh.insert_after(new_tdh)
                if navbox and "style" in tdh.attrs:
                    style = str(tdh.get("style", ""))
                    tdh["style"] = re.sub(
                        r"\btext-align\s*:\s*[^;]+;?\s*",
                        "",
                        style,
                    ).strip()
                    if not tdh["style"]:
                        del tdh.attrs["style"]
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
                        if not isinstance(current_row := current_row.next_sibling, Tag):
                            break
                        new_tdh = copy(tdh)
                        new_tdh.clear()
                        current_row.insert(col_idx, new_tdh)

    @staticmethod
    def _cell_alignment(cell: Tag) -> str:
        """Derive a GFM alignment marker from a table cell's text-align style."""
        style = str(cell.get("style", ""))
        if ta_match := _TEXT_ALIGN_REGEX.search(style):
            ta = ta_match[1]
            if ta == "center":
                return ":-:"
            elif ta == "right":
                return "--:"
            return ":--"
        return "---"

    @staticmethod
    def _filter_table_cells(
        strings: str,
        *,
        is_navbox: bool,
        total_colspan: int,
    ) -> str:
        """Filter, pad, and clean table cell strings for _handle_tr."""
        cells = [s.strip() for s in strings.split(" | ")]
        if not is_navbox:
            cells = [c for c in cells if c]
        while len(cells) < total_colspan:
            cells.append("")
        result = " | ".join(cells)
        if cells and not cells[0] and result.startswith(" |"):
            result = "|" + result[2:]
        return result

    def _handle_tr(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <tr> table row elements."""
        joiner = " | "
        prefix = "| "
        suffix = " |\n"

        for child in list(ele.children):
            if isinstance(child, NavigableString) and not child.strip():
                child.extract()

        is_navbox = self._in_navbox(ele)

        tag_cells = [
            child
            for child in ele.children
            if isinstance(child, Tag) and child.name in _TD_OR_TH
        ]

        total_colspan = sum(int(str(c.get("colspan", "1"))) for c in tag_cells)

        if tag_cells and all(child.name == "th" for child in tag_cells):
            table = ele.find_parent("table")
            has_scope_row = (
                table is not None and table.find("th", scope="row") is not None
            )

            alignments = [self._cell_alignment(child) for child in tag_cells]
            if has_scope_row and alignments:
                alignments[0] = "--:"
            suffix += f"| {' | '.join(alignments)} |\n"
        else:
            for child in ele.children:
                if isinstance(child, Tag) and child.name == "th":
                    if not _BOLD_FONT_STYLE_REGEX.search(str(child.get("style", ""))):
                        new_b = _bs4_new_element("<b></b>")
                        assert isinstance(new_b, Tag)
                        for child_child in child.contents[:]:
                            new_b.append(child_child.extract())
                        child.append(new_b)
        return _HandlerConfig(
            joiner=joiner,
            prefix=prefix,
            suffix=suffix,
            process_strings=lambda s: self._filter_table_cells(
                s, is_navbox=is_navbox, total_colspan=total_colspan
            ),
        )

    def _handle_td(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Dispatch <td> table cell elements."""
        return _HandlerConfig(process_strings=self._process_table_cell)

    def _handle_th(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Dispatch <th> table header cell elements."""
        if "sidebar-title-with-pretitle" in classes:
            return _HandlerConfig(
                prefix="<big>",
                suffix="</big>",
                process_strings=self._process_table_cell,
            )
        return _HandlerConfig(process_strings=self._process_table_cell)

    @staticmethod
    def _process_table_cell(strings: str) -> str:
        """Process content of a table cell."""
        strings = strings.strip()
        strings = _CONSECUTIVE_NEWLINES_REGEX.sub("\n\n", strings)
        strings = _CONSECUTIVE_LEADING_WHITESPACES_REGEX.sub(
            lambda match: match[0].replace(" ", "&nbsp;").replace("\t", "&emsp;"),
            strings,
        )
        strings = strings.replace("\xa0", " ")
        strings = strings.replace("| |", "|")
        strings = _TABLE_IN_TABLE_HEADER_REGEX.sub(
            lambda match: f"|{match[1]} <p> ", strings
        )
        strings = strings.replace("|\n|", " <p> ")
        strings = _TABLE_IN_TABLE_LEADING_VERTICAL_REGEX.sub(
            lambda match: match[0][: -len("|")], strings
        )
        strings = _TABLE_IN_TABLE_TRAILING_VERTICAL_REGEX.sub(
            lambda match: match[0][len("|") :], strings
        )
        strings = strings.replace("|", "&#124;")
        strings = strings.strip()
        strings = strings.replace("\n\n", " <br/> <br/> ")
        strings = strings.replace("\n", " <br/> ")
        return strings

    def _process_archive_url(self, src: str) -> str:
        """Resolve a media URL to a local archive path."""
        src_url = _cfg._WIKI_HOST_URL.join(URL(str(src)))
        src_url_str = str(src_url)
        for regex, formats in _cfg._ARCHIVE_REGEXES.items():
            if not (match := regex.search(src_url.human_repr())):
                continue
            to_archive = unquote(match[1])
            self._out_to_archive.add(formats[0].format(to_archive))
            src_url_str = quote(formats[1].format(to_archive.replace("_", " ")))
        return src_url_str

    def _handle_audio(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <audio> media elements."""
        if src := ele.get("href"):

            def process(strings: str) -> str:
                """Generate Markdown link for audio file."""
                src_url_str = self._process_archive_url(str(src))
                embed = "!" if {"mw-tmh-player"} & classes else ""
                return f"{embed}[{strings.strip()}]({src_url_str})"

            return _HandlerConfig(
                suffix="" if self._in_table_cell(ele) else "\n\n",
                process_strings=process,
            )
        return _HandlerConfig()

    def _handle_image(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <img> image elements with download and link."""
        if src := ele.get("src"):

            def process(strings: str) -> str:
                """Generate Markdown image syntax with alt text."""
                src_url_str = self._process_archive_url(str(src))
                alt = str(ele.get("alt", "")).strip()
                if not alt:
                    alt = self._fallback_alt(ele)
                    filename = _get_image_filename(ele)
                    if filename and f"File:{filename}" in self._image_metadata:
                        alt = _balance_brackets(alt)
                    else:
                        alt = _cfg._MARKDOWN_ESCAPE_REGEX.sub(
                            lambda m: Rf"\{m[0]}", alt
                        )
                else:
                    alt = _cfg._MARKDOWN_ESCAPE_REGEX.sub(lambda m: Rf"\{m[0]}", alt)
                paragraphs = alt.split("\n\n")
                alt = (" <p> ".join(paragraphs)).strip()
                alt = alt.replace("\n", " <br/> ")
                return f"{strings}![{alt}]({src_url_str})"

            return _HandlerConfig(
                suffix="" if self._in_table_cell(ele) else "\n\n",
                process_strings=process,
            )
        return _HandlerConfig()

    def _fallback_alt(self, ele: Tag) -> str:
        """Compute alt text fallback for an <img> element."""
        filename = _get_image_filename(ele)
        if not filename:
            return ""
        file_title = f"File:{filename}"
        if desc := self._image_metadata.get(file_title, ""):
            return desc
        return file_title

    @staticmethod
    async def _create_redirect_symlinks(
        wiki_dir: PathLike[str],
        wiki_lang_dir: PathLike[str],
        from_filename: str,
        to_filename: str,
    ) -> None:
        """Create redirect symlinks for a renamed page."""
        wiki_dir_path = Path(wiki_dir)
        wiki_lang_dir_path = Path(wiki_lang_dir)
        redirect_file = wiki_lang_dir_path / f"{from_filename}.md"
        if not await redirect_file.exists():
            with suppress(FileExistsError):
                await redirect_file.symlink_to(
                    f"{to_filename}.md",
                    target_is_directory=False,
                )
            with suppress(FileExistsError):
                await (wiki_dir_path / f"{from_filename}.md").symlink_to(
                    str(redirect_file.relative_to(wiki_dir_path)),
                    target_is_directory=False,
                )

    async def _handle_link(
        self, ele: Tag, classes: frozenset[str]
    ) -> _HandlerConfig | None:
        """Handle <a> link elements."""
        if (title := ele.get("title")) and title not in _cfg._BAD_TITLES:
            title = str(title)
            if "new" in classes:
                title = title.removesuffix(_cfg._PAGE_DOES_NOT_EXIST_SUFFIX)
            href = str(ele.get("href", ""))
            to_fragment = href.split("#", 1)[-1] if "#" in href else ""

            info = self._redirect_map.get(title, _RedirectInfo(to=title))
            to = info.to
            if not to_fragment:
                to_fragment = info.tofragment

            def _process_link_text(s: str) -> str:
                """Strip and flatten link display text."""
                return s.strip().replace("\n", " <br/> ")

            if any(to.startswith(prefix) for prefix in _cfg._IGNORED_NAME_PREFIXES):
                pass
            elif url_format := next(
                (
                    (format, to[len(prefix) :])
                    for prefix, format in _cfg._PRESERVED_PAGE_PREFIXES.items()
                    if to.startswith(prefix)
                ),
                None,
            ):
                return _HandlerConfig(
                    prefix="[",
                    suffix=(
                        f"]"
                        f"({url_format[0].format(f'{quote(url_format[1])}{to_fragment and "#"}{quote(to_fragment, safe="")}')})"
                    ),
                    process_strings=_process_link_text,
                )
            elif "extiw" in classes:
                lang_code, extiw_page = to.split(":", 1)
                lang_code = str(convert(lang_code, to="ISO3")).casefold()
                from_filename = _fix_name_maybe(
                    extiw_page,
                    replace_underscores=True,
                    names_map=self._names_map,
                )

                return _HandlerConfig(
                    prefix="[",
                    suffix=(
                        f"]"
                        f"(../{lang_code}/{_markdown_link_target(from_filename, _fix_name_maybe(to_fragment, replace_underscores=True, names_map=self._names_map))})"
                    ),
                    process_strings=_process_link_text,
                )
            else:
                from_filename, to_filename = (
                    _fix_name_maybe(
                        title,
                        replace_underscores=True,
                        names_map=self._names_map,
                    ),
                    _fix_name_maybe(
                        to,
                        replace_underscores=True,
                        names_map=self._names_map,
                    ),
                )

                config = _HandlerConfig(
                    prefix="[",
                    suffix=(
                        f"]"
                        f"({_markdown_link_target(from_filename, _fix_name_maybe(to_fragment, replace_underscores=True, names_map=self._names_map))})"
                    ),
                    process_strings=_process_link_text,
                )
                from_filename, to_filename = (
                    _fix_filename(from_filename),
                    _fix_filename(to_filename),
                )
                if from_filename != to_filename:
                    await self._create_redirect_symlinks(
                        self._converted_wiki_dir,
                        self._converted_wiki_lang_dir,
                        from_filename,
                        to_filename,
                    )
                return config
        elif ele_href := ele.get("href"):
            href = str(ele_href)
            if href.startswith(f"{_cfg._WIKI_HOST_URL}/wiki/") and "#" in href:
                href = _markdown_fragment(
                    _fix_name_maybe(
                        href[href.index("#") + 1 :],
                        replace_underscores=True,
                        names_map=self._names_map,
                    )
                )

            def process(strings: str) -> str:
                """Collapse whitespace in anchor text."""
                return " ".join(strings.split())

            if any(
                isinstance(p, Tag) and p.get("typeof") == "mw:File/Frameless"
                for p in ele.parents
            ) and any(
                isinstance(p, Tag) and "authority-control" in (p.get("class") or [])
                for p in ele.parents
            ):
                config = _HandlerConfig(
                    prefix="<!-- [",
                    suffix=f"]({href}) -->",
                    process_strings=process,
                )
            else:
                config = _HandlerConfig(
                    prefix="[",
                    suffix=f"]({href})",
                    process_strings=process,
                )
            return config

        return None
