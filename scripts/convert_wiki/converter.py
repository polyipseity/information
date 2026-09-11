"""Core Wikipedia HTML-to-Markdown converter.

Contains ``WikiHtmlConverter``, the main class that walks a BeautifulSoup
HTML tree and emits Markdown text via tag-specific handler methods.
"""

import re
from collections.abc import Iterable, Mapping, MutableSet
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
from .latex import LatexConverter
from .table import _TD_OR_TH, _TEXT_ALIGN_REGEX, TableConverter
from .types import _HandlerConfig, _RedirectInfo
from .utils import (
    _balance_brackets,
    _create_redirect_symlinks,
    _fix_filename,
    _fix_name_maybe,
    _get_image_filename,
    _markdown_fragment,
    _markdown_link_target,
    _strip_url_query,
    _tag_affixes,
)

"""Exported names from this module."""
__all__ = ()

"""Regex for matching header tags (``h1``, ``h2``, etc.)."""
_HEADER_REGEX = re.compile(r"^h(\d)$")
"""Tags that render as bold or italic."""
_BOLD_OR_ITALIC = frozenset({"b", "em", "i", "strong"})
"""Tags that render as lists."""
_LIST_TAGS = frozenset({"ol", "ul"})
"""Inline-level HTML tags for whitespace-preservation checks."""
_INLINE_TAGS = frozenset({"a", "span", "em", "i", "b", "strong", "img"})
"""Bold font-weight style detector."""
_BOLD_FONT_STYLE_REGEX = re.compile(r"\bfont-weight\s*:\s*bold\b", re.IGNORECASE)
"""Italic font-style detector."""
_ITALIC_FONT_STYLE_REGEX = re.compile(r"\bfont-style\s*:\s*italic\b", re.IGNORECASE)
"""Collapse runs of empty blockquote lines."""
_COLLAPSE_EMPTY_BLOCKQUOTE_RE = re.compile(r">\n(?:>\n)+")
"""Collapse consecutive spaces."""
_COLLAPSE_SPACES_REGEX = re.compile(r" {2,}")
"""Whitespace runs except hair space (U+200A)."""
_WHITESPACE_EXCEPT_HAIR_RE = re.compile(r"[^\S\u200a]+")
"""Captures the separator-prefixed display text in bold/italic processing."""
_PROCESS_STRINGS_BI_REGEX = re.compile(r"^( *)(.*?)([\n ]*)$", re.DOTALL)
"""Matches bare URLs for autolink wrapping."""
_BARE_URL_REGEX = re.compile(r"(?:https?://|www\.)[^\s<>]+")
"""Whitespace and separator chars for sidebar tight wrapping."""
_SIDEBAR_TIGHT_WRAPPING_RE = re.compile(r"[ \t]+", re.MULTILINE)
"""Containers where sole formula rows are display math."""
_DISPLAY_MATH_CONTAINERS = frozenset({"dd", "dt"})
"""Box-like classes whose content renders specially."""
_BOXED_CLASSES = frozenset(
    {
        "catlinks",
        "equation-box",
        "math_proof",
        "math_theorem",
        "portalbox",
        "tmulti",
        "unsolved",
    }
)
"""Box-like classes whose content renders as a blockquote."""
_BLOCKQUOTE_CLASSES = frozenset(_BOXED_CLASSES - {"equation-box"})
"""
Span classes whose handler emits markers or block spacing.

``_handle_span`` returns ``None``, so a span is normally flattened and
contributes nothing of its own.  These classes are the exception: ``hatnote``
prefixes a list marker, ``sidebar-navbar``/``navbar`` may wrap their text in an
HTML comment, ``sistersitebox`` and ``thumb`` add block spacing, and the boxed
classes render as blockquotes.  ``_is_transparent_span`` needs this set so its
verdict agrees with what ``convert`` actually emits for a span.
"""
_OPAQUE_SPAN_CLASSES = _BOXED_CLASSES | frozenset(
    {"hatnote", "navbar", "sidebar-navbar", "sistersitebox", "thumb"}
)
"""
Tags that render a glyph or a line break with no child content.

``_renders_nothing`` must not treat these as empty just because they have no
text: they are rendered tokens in their own right.
"""
_ATOMIC_TAGS = frozenset({"br", "hr", "img"})
"""Inline tags that can form an equation-box title."""
_EQUATION_BOX_TITLE_TAGS = frozenset({"b", "strong", "i", "em", "span"})
"""Block-level tags that separate an equation-box title from its body."""
_EQUATION_BOX_BODY_BLOCK_TAGS = frozenset(
    {"p", "div", "table", "ul", "ol", "dl", "blockquote", "pre", "figure"}
)
"""LaTeX environments whose trailing punct belongs on the last row."""
_DISPLAY_MATH_ENVIRONMENTS: tuple[str, ...] = (
    "aligned",
    "align",
    "align*",
    "gather",
    "gather*",
    "multline",
    "split",
    "cases",
    "array",
    "matrix",
    "pmatrix",
    "bmatrix",
    "vmatrix",
    "Bmatrix",
)


def _wrap_bare_url(text: str) -> str:
    """Wrap a bare URL in autolink brackets (e.g. ``www.example.com`` → ``<www.example.com>``)."""
    if _BARE_URL_REGEX.fullmatch(text):
        return f"<{text}>"
    return text


def _collapse_whitespace(text: str) -> str:
    """Collapse whitespace runs, preserving hair spaces (U+200A)."""
    text = text.strip(" \t\n\r\x0b\x0c")
    return " ".join(_WHITESPACE_EXCEPT_HAIR_RE.split(text))


def _set_text_align(cell: Tag, align: str) -> None:
    """Append ``text-align`` to *cell*'s style unless it already declares one."""
    style = str(cell.get("style", ""))
    if _TEXT_ALIGN_REGEX.search(style):
        return
    cell["style"] = f"{style}text-align: {align};"


def _strip_cell_bold(cell: Tag) -> None:
    """Remove ``font-weight: bold`` from *cell*'s style.

    Wikipedia equation-number cells are bolded at the cell level *and* on the
    inner reference span; the cell-level bold is redundant and would otherwise
    double-wrap the number as ``____N____``. Drop it so only the span's bold
    survives. The style attribute is removed entirely when emptied.
    """
    style = str(cell.get("style", ""))
    stripped = _BOLD_FONT_STYLE_REGEX.sub("", style).strip().rstrip(";").strip()
    if stripped:
        cell["style"] = stripped
    else:
        cell.attrs.pop("style", None)


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
        soup: BeautifulSoup | None = None,
    ) -> None:
        """Initialize converter with directory paths and name map."""
        self._converted_wiki_dir = Path(converted_wiki_dir)
        self._converted_wiki_lang_dir = Path(converted_wiki_lang_dir)
        self._image_metadata = image_metadata or {}
        self._names_map = names_map or _cfg._NAMES_MAP
        self._soup: BeautifulSoup = (
            soup if soup is not None else BeautifulSoup("", "html.parser")
        )

    async def convert(
        self,
        ele: PageElement,
        *,
        out_to_archive: MutableSet[str],
        list_stack: tuple[int, ...] = (),
        escape: bool = True,
        refs: bool,
        redirect_map: Mapping[str, _RedirectInfo],
        seen_heading_texts: set[str] | None = None,
    ) -> str:
        """Convert a Wikipedia HTML element tree to a Markdown string."""
        # Heading-dedup state is per-document: created once at the external
        # entry and threaded through the recursion so repeated convert() calls
        # on the same instance start clean (MD024 formatting-agnostic test).
        seen_heading_texts = set() if seen_heading_texts is None else seen_heading_texts

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
            # Drop CS1-maintenance citation-comment spans — these are
            # citation-metadata noise (e.g. "CS1 maint: multiple names"),
            # not article content, and their literal "link" text fails
            # descriptive-link-text linting.
            for cs1_maint in ele.find_all("span", class_="cs1-maint"):
                cs1_maint.decompose()

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
                    # Preserve a single space between two adjacent inline
                    # tokens that would otherwise merge: two emphasis elements
                    # (``<b>M</b> <b>L</b>`` → ``__M__ __L__``), two links
                    # (``[a](x) [b](y)`` → ``[a](x)[b](y)`` if dropped), or two
                    # plain-text runs (``Physics<span> </span>portal`` → the
                    # space is the only separation).  The space separates two
                    # distinct tokens and must survive whitespace collapsing.
                    # A link directly followed by an emphasis (e.g.
                    # ``[x](y)_z_``) is intentionally tight, so the space stays
                    # collapsed there.  Math fragments wrapped in a ``texhtml``
                    # span (e.g. ``<i>m</i> <i>x</i>``) are also an exception:
                    # adjacent variables are conventionally tight.
                    #
                    # The decision uses *rendered* adjacency, not raw siblings:
                    # ``_handle_span`` flattens transparent spans, so a
                    # whitespace run at a span edge has no direct sibling yet
                    # still separates two rendered tokens.
                    prev = self._effective_sibling(ele, following=False)
                    nxt = self._effective_sibling(ele, following=True)
                    if not self._in_texhtml(ele) and (
                        (
                            isinstance(prev, Tag)
                            and isinstance(nxt, Tag)
                            and (
                                (
                                    self._is_inline_emphasis(prev)
                                    and self._is_inline_emphasis(nxt)
                                )
                                or (
                                    self._is_inline_link(prev)
                                    and self._is_inline_link(nxt)
                                )
                                or (
                                    self._is_inline_link(prev)
                                    and nxt.name in _INLINE_TAGS
                                )
                                or (
                                    prev.name in _INLINE_TAGS
                                    and self._is_inline_link(nxt)
                                )
                            )
                        )
                        or self._text_edges_would_merge(prev, nxt)
                    ):
                        return " "
                    if (
                        self._in_texhtml(ele)
                        and isinstance(prev := ele.previous_sibling, Tag)
                        and isinstance(nxt := ele.next_sibling, Tag)
                        and self._is_inline_emphasis(prev)
                        and self._is_inline_emphasis(nxt)
                    ):
                        return _cfg._MARKDOWN_SEPARATOR
                    return ""
                return escape_markdown(text) if escape else text
            return ""

        classes = frozenset(ele.get_attribute_list("class"))
        if {"mw-cite-backlink", "mw-editsection"} & classes:
            return ""

        if "reference" in classes:
            if refs:
                ref_link = ele.find("a", href=lambda v: v and "#cite_note-" in v)
                if ref_link:
                    ref_content = ref_link.get_text(strip=True).strip("[]")
                    if " " in ref_content:
                        group, number = ref_content.split(" ", 1)
                        fragment = f"^{group}-{number}"
                    else:
                        fragment = f"^ref-{ref_content}"
                    return (
                        f"<sup>[{escape_markdown(f'[{ref_content}]')}]"
                        f"({_markdown_fragment(fragment)})</sup>"
                    )
            else:
                return ""

        if (
            isinstance(ele, Tag)
            and ele.name == "div"
            and "mw:Transclusion" in str(ele.get("typeof", ""))
        ):
            if "annotated image" in str(ele.get("data-mw", "")):
                for ann_div in ele.find_all(
                    "div", id=lambda v: v and v.startswith("annotation_")
                ):
                    ann_div.decompose()
                for noviewer in ele.find_all("span", class_="noviewer"):
                    noviewer.decompose()

        self._out_to_archive = out_to_archive
        self._redirect_map = redirect_map

        config = await self._dispatch(
            ele, classes, list_stack=list_stack, seen_heading_texts=seen_heading_texts
        )
        if config is None:
            config = _HandlerConfig()

        # Ensure a single blank line separates a single-newline block from a
        # following heading (markdownlint MD022/MD032). Blocks already ending
        # in "\n\n" are left untouched to avoid double blank lines.
        if config.suffix == "\n":
            nxt = self._effective_sibling_skipping(
                ele, following=True, skip_whitespace=True
            )
            if isinstance(nxt, Tag) and (
                _HEADER_REGEX.match(nxt.name)
                or "mw-heading" in frozenset(nxt.get_attribute_list("class"))
            ):
                config.suffix = "\n\n"

        joiner = config.joiner
        process_strings = config.process_strings
        if config.list_stack is not None:
            list_stack = config.list_stack

        if "hatnote" in classes:
            config.prefix = f"- {config.prefix.removesuffix('_')}"
            # Find the next non-empty sibling, skipping whitespace and empty spans.
            nxt = ele.find_next_sibling()
            while isinstance(nxt, Tag) and "mw-empty-elt" in frozenset(
                nxt.get_attribute_list("class")
            ):
                nxt = nxt.find_next_sibling()
            if isinstance(nxt, Tag) and (
                nxt.name == "figure"
                or nxt.name == "blockquote"
                or _BOXED_CLASSES & frozenset(nxt.get_attribute_list("class"))
            ):
                config.suffix = f"{config.suffix.removeprefix('_')}\n\n"
            elif self._effective_sibling_is_heading(ele):
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

        has_thumb_with_caption = (
            "thumb" in classes
            and isinstance(ele, Tag)
            and ele.find("div", class_="thumbcaption") is not None
        )
        has_box_title = _BLOCKQUOTE_CLASSES & classes and bool(
            self._find_box_title(ele, has_numblk=False)
        )
        if "sistersitebox" in classes:
            original_process = process_strings

            def process_strings_sistersitebox(strings: str) -> str:
                """Collapse sistersitebox image + text onto one blockquote line."""
                strings = original_process(strings)
                collapsed = " ".join(strings.split())
                return f"> {collapsed}"

            config.suffix = "\n\n"
            process_strings = process_strings_sistersitebox
        elif (
            ele.name == "figure"
            or _BLOCKQUOTE_CLASSES & classes
            or has_thumb_with_caption
        ):
            original_process = process_strings

            def process_strings_blockquote(strings: str) -> str:
                """Collapse whitespace runs within blockquote content."""
                strings = original_process(strings)
                # Collapse per line, preserving newlines between the box
                # title and its paragraphs (e.g. ``__Proof__`` gets its own
                # ``> `` line inside the blockquote).
                strings = "\n\n".join(
                    "\n".join(_collapse_whitespace(line) for line in para.split("\n"))
                    for para in strings.split("\n\n")
                )
                result = "\n".join(
                    f">{content and ' '}{content}"
                    for content in (
                        _collapse_whitespace(line).strip()
                        for line in strings.strip().splitlines()
                    )
                )
                result = _COLLAPSE_EMPTY_BLOCKQUOTE_RE.sub(">\n", result)
                # Separate the box title from its body with a blank ``> `` line.
                if has_box_title:
                    result = re.sub(
                        r"^(> [^\n]+)\n(> \S)", r"\1\n>\n\2", result, count=1
                    )
                return result

            config.suffix = "\n\n"
            process_strings = process_strings_blockquote

        if ele.name in _DISPLAY_MATH_CONTAINERS or ele.name == "p":
            self._normalize_external_math_punctuation(ele)

        soon_values, list_stack = await self._convert_children(
            ele,
            list_stack=list_stack,
            out_to_archive=out_to_archive,
            escape=escape,
            refs=refs,
            redirect_map=redirect_map,
            seen_heading_texts=seen_heading_texts,
        )
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
        seen_heading_texts: set[str],
    ) -> _HandlerConfig | None:
        """Dispatch to a handler for the given element."""
        if header_match := _HEADER_REGEX.match(ele.name):
            return self._handle_header(
                ele,
                classes,
                level=int(header_match[1]),
                seen_heading_texts=seen_heading_texts,
            )

        # A document ``<title>`` is the page's level-1 heading.  Only the
        # document title (direct child of ``<head>``) qualifies: SVG and other
        # inline ``<title>`` elements are descriptive text, not headings.
        if (
            ele.name == "title"
            and isinstance(ele.parent, Tag)
            and ele.parent.name == "head"
        ):
            return self._handle_header(
                ele, classes, level=1, seen_heading_texts=seen_heading_texts
            )

        if ele.name == "a" and "mw-selflink" in classes:
            return self._handle_selflink(ele, classes)

        if "hatnote" not in classes and self._renders_emphasis(ele):
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
            return await self._handle_anchor(ele, classes)

        if ele.name == "ol":
            return self._handle_ol(ele, classes, list_stack)
        if ele.name == "ul" and "portalbox" in classes:
            return self._handle_portalbox(ele, classes)
        if ele.name == "ul":
            return self._handle_ul(ele, classes, list_stack)
        if ele.name == "li":
            return self._handle_li(ele, classes, list_stack)

        if ele.name == "video":
            return self._handle_video(ele, classes)

        handler = getattr(self, f"_handle_{ele.name}", None)
        if handler is not None:
            return handler(ele, classes)

        return None

    async def _convert_children(
        self,
        ele: Tag,
        *,
        list_stack: tuple[int, ...],
        out_to_archive: MutableSet[str],
        escape: bool,
        refs: bool,
        redirect_map: Mapping[str, _RedirectInfo],
        seen_heading_texts: set[str],
    ) -> tuple[list[SoonValue[str]], tuple[int, ...]]:
        """Process child elements concurrently using task groups."""
        soon_values: list[SoonValue[str]] = []
        async with create_task_group() as tg:
            for child in ele.children:
                if (
                    list_stack
                    and list_stack[-1] >= 0
                    and isinstance(child, Tag)
                    and child.name == "li"
                ):
                    list_stack = (*list_stack[:-1], list_stack[-1] + 1)
                soon_values.append(
                    tg.soonify(self.convert)(
                        child,
                        out_to_archive=out_to_archive,
                        list_stack=list_stack,
                        escape=escape and ele.name not in {"code", "math"},
                        refs=refs,
                        redirect_map=redirect_map,
                        seen_heading_texts=seen_heading_texts,
                    )
                )
        return soon_values, list_stack

    # --- Tag handlers ---

    def _handle_br(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig | None:
        """Render a <br> tag as a newline."""

        def process(strings: str) -> str:
            """Append newline to strings."""
            return f"{strings}\n"

        return _HandlerConfig(process_strings=process)

    def _handle_header(
        self,
        ele: Tag,
        classes: frozenset[str],
        level: int,
        seen_heading_texts: set[str],
    ) -> _HandlerConfig:
        """Render a heading with Markdown # markers."""
        prefix = f"{'#' * level} "
        suffix = "\n\n"

        def process(strings: str) -> str:
            """Fix name casing in heading text; suppress MD024 on repeats."""
            text = _fix_name_maybe(strings.strip(), names_map=self._names_map)
            key = text.casefold()
            if key in seen_heading_texts:
                return f"<!-- markdownlint-disable-next-line MD024 -->\n{prefix}{text}"
            seen_heading_texts.add(key)
            return f"{prefix}{text}"

        return _HandlerConfig(prefix="", suffix=suffix, process_strings=process)

    def _handle_selflink(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render a self-link as a relative Markdown link."""
        href = str(ele.get("href", ""))
        wiki_prefix = f"{_cfg._WIKI_HOST_URL}/wiki/"
        if href.startswith(wiki_prefix):
            title = unquote(href[len(wiki_prefix) :].split("#")[0]).replace("_", " ")
        elif href.startswith("/wiki/"):
            title = unquote(href[6:].split("#")[0]).replace("_", " ")
        else:
            title = ele.get_text(strip=True)
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
        """Whether a separator is needed before the block."""
        if isinstance(sibling, NavigableString):
            return sibling.rstrip(_cfg._MARKDOWN_SEPARATOR_CHARACTERS) == sibling
        if isinstance(sibling, Tag):
            # Transparent spans emit nothing; descend to their last rendered
            # child to find what abuts the block on the rendered side.
            last: PageElement = sibling
            while isinstance(last, Tag) and last.name == "span" and last.contents:
                last = last.contents[-1]
            if isinstance(last, NavigableString):
                return last.rstrip(_cfg._MARKDOWN_SEPARATOR_CHARACTERS) == last
            return isinstance(last, Tag) and (
                last.name in _BOLD_OR_ITALIC
                or bool(_BOLD_FONT_STYLE_REGEX.search(str(last.get("style", ""))))
                or bool(_ITALIC_FONT_STYLE_REGEX.search(str(last.get("style", ""))))
            )
        return False

    @staticmethod
    def _needs_separator_after(sibling: PageElement | None) -> bool:
        """Whether a separator is needed after the block."""
        return (
            isinstance(sibling, NavigableString)
            and sibling.lstrip(_cfg._MARKDOWN_SEPARATOR_CHARACTERS) == sibling
        )

    @staticmethod
    def _text_edges_would_merge(
        prev: PageElement | None, nxt: PageElement | None
    ) -> bool:
        """Whether two plain-text neighbours would merge without a space.

        Parsoid renders an explicit character reference as an ``mw:Entity`` span
        whose body is the referenced character: U+0020 for ``&#32;``, U+00A0 for
        ``&nbsp;``.  Only an ASCII-whitespace body reaches the whitespace
        collapsing above; when such a span sits between two words its text is the
        only separation, so both rendered neighbours must be text and neither may
        already supply a space.
        """
        if not isinstance(prev, NavigableString) or not isinstance(
            nxt, NavigableString
        ):
            return False
        before, after = str(prev), str(nxt)
        return (
            bool(before)
            and bool(after)
            and not before[-1].isspace()
            and not after[0].isspace()
        )

    @staticmethod
    def _renders_emphasis(ele: Tag) -> bool:
        """Whether *ele* is routed to ``_handle_bold_italic``.

        Covers the explicit emphasis tags and any element whose inline style
        forces bold or italic.  ``_dispatch`` and ``_is_transparent_span`` both
        use this, so the routing decision and the transparency model cannot
        drift apart.
        """
        return bool(
            ele.name in _BOLD_OR_ITALIC
            or _BOLD_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
            or _ITALIC_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
        )

    @classmethod
    def _is_transparent_span(cls, ele: PageElement | None) -> bool:
        """Whether *ele* is a ``<span>`` that renders nothing of its own.

        Such a span is flattened by ``_handle_span``: its children take its
        place in the rendered output, so the wrapper's own siblings become
        their rendered neighbours.  A span is opaque when ``_dispatch`` routes
        it to an emphasis handler (which emits ``__``/``_`` markers), or when
        ``convert`` gives it a class-driven prefix, suffix, or block spacing.
        """
        if not isinstance(ele, Tag) or ele.name != "span":
            return False
        classes = frozenset(ele.get_attribute_list("class"))
        if "hatnote" not in classes and cls._renders_emphasis(ele):
            return False
        return not classes & _OPAQUE_SPAN_CLASSES

    @classmethod
    def _renders_nothing(cls, ele: PageElement) -> bool:
        """Whether *ele* contributes no text, image, or separating space.

        An empty ``<span>`` renders nothing, and neither does an emphasis span
        whose whole body is whitespace: ``convert`` drops the collapsed result,
        so the markers around it never appear.  A *transparent* span holding
        whitespace is the exception — the whitespace branch turns that text into
        the separating space, so the wrapper does render something.
        """
        if isinstance(ele, PreformattedString):
            # Comments, CDATA, and doctypes are markup, never content.
            return True
        if isinstance(ele, NavigableString):
            return not str(ele).strip()
        if not isinstance(ele, Tag):
            return False
        if ele.name in _ATOMIC_TAGS:
            return False
        if ele.find("img") is not None:
            return False
        if any(
            not isinstance(s, PreformattedString) and str(s).strip()
            for s in ele.strings
        ):
            return False
        return not (cls._is_transparent_span(ele) and ele.contents)

    @classmethod
    def _effective_sibling(
        cls, ele: PageElement, *, following: bool
    ) -> PageElement | None:
        """Return the sibling adjacent to *ele* in rendered output order.

        ``_handle_span`` emits nothing and flattens its children, so an
        element that is the only child of a transparent ``<span>`` has no
        direct sibling yet is adjacent to the wrapper's sibling in the output.
        Walk up through such wrappers until a real sibling is found or an
        opaque boundary (block element or root) is reached.
        """
        return cls._effective_sibling_skipping(
            ele, following=following, skip_whitespace=False
        )

    @classmethod
    def _effective_sibling_skipping(
        cls,
        ele: PageElement,
        *,
        following: bool,
        skip_whitespace: bool,
        skip_nothing_rendering: bool = False,
    ) -> PageElement | None:
        """Like ``_effective_sibling`` but optionally skips unrendered siblings.

        Whitespace-only ``NavigableString`` siblings carry no rendered content,
        so structural decisions (e.g. a blank line before a following heading)
        must look past them.  ``_needs_separator_before`` and
        ``_needs_separator_after`` intentionally rely on the raw whitespace
        result, so callers there must pass ``skip_whitespace=False``.

        ``skip_nothing_rendering`` additionally steps over elements that render
        nothing, such as an empty ``<span>``.  Whitespace-only text is never
        skipped by that flag: it is what supplies the separation in the first
        place, so replacing it with the element beyond would be wrong.
        """
        node: PageElement = ele
        while True:
            sibling = node.next_sibling if following else node.previous_sibling
            if sibling is None:
                parent = node.parent
                if not isinstance(parent, Tag) or not cls._is_transparent_span(parent):
                    return None
                node = parent
                continue
            if (
                skip_whitespace
                and isinstance(sibling, NavigableString)
                and not sibling.strip()
            ):
                node = sibling
                continue
            if (
                skip_nothing_rendering
                and isinstance(sibling, Tag)
                and cls._renders_nothing(sibling)
            ):
                node = sibling
                continue
            return sibling

    @classmethod
    def _rendered_neighbour(
        cls, ele: PageElement, *, following: bool
    ) -> PageElement | None:
        """Nearest neighbour in rendered order that renders content.

        ``_needs_separator_before`` and ``_needs_separator_after`` ask what
        abuts an emphasis run in the rendered output.  A neighbour that renders
        nothing is not that abutment, so the search continues past it — that is
        what lets ``<b>a</b><span></span><b>b</b>`` keep its two runs apart.
        """
        return cls._effective_sibling_skipping(
            ele,
            following=following,
            skip_whitespace=False,
            skip_nothing_rendering=True,
        )

    @staticmethod
    def _effective_sibling_is_heading(ele: PageElement) -> bool:
        """Check if the effective next sibling is a heading.

        Handles the case where the next sibling is a ``<section>`` wrapper
        containing a heading as a direct child (not nested deeper).
        """
        node: PageElement = ele
        while True:
            sibling = node.next_sibling
            if sibling is None:
                return False
            if isinstance(sibling, NavigableString):
                if not sibling.strip():
                    node = sibling
                    continue
                return False
            if isinstance(sibling, Tag):
                if _HEADER_REGEX.match(sibling.name):
                    return True
                if "mw-heading" in frozenset(sibling.get_attribute_list("class")):
                    return True
                # <section> wrapper: check only direct children for headings
                # (not recursive, to avoid false positives from nested sections)
                if sibling.name == "section":
                    for child in sibling.children:
                        if isinstance(child, Tag) and (
                            _HEADER_REGEX.match(child.name)
                            or "mw-heading"
                            in frozenset(child.get_attribute_list("class"))
                        ):
                            return True
                    return False
                return False
            return False

    @classmethod
    def _has_emphasis_ancestor(cls, ele: Tag, *, bold: bool) -> bool:
        """Return whether an ancestor already renders the same emphasis.

        Wrappers that never emit Markdown emphasis are skipped: ``mw-heading``
        (rendered with ``#`` markers), ``hatnote`` (rendered as a list item,
        whose own CSS emphasis is deliberately not emitted), and bold wrappers
        around a bare list (whose bold is pushed onto the list items).
        """
        for ancestor in ele.parents:
            if not isinstance(ancestor, Tag):
                continue
            if {"mw-heading", "hatnote"} & frozenset(
                ancestor.get_attribute_list("class")
            ):
                continue
            if bold and cls._is_list_only(ancestor):
                continue
            style = str(ancestor.get("style", ""))
            if bold:
                if ancestor.name in {"b", "strong"} or _BOLD_FONT_STYLE_REGEX.search(
                    style
                ):
                    return True
            elif ancestor.name in {"em", "i"} or _ITALIC_FONT_STYLE_REGEX.search(style):
                return True
        return False

    @staticmethod
    def _sole_bold_child(ele: Tag) -> Tag | None:
        """Return the single ``<b>``/``<strong>`` child if *ele* contains only bold + whitespace.

        Only checks ``<b>`` and ``<strong>`` (not ``<em>``/``<i>``), because
        bold-only paragraphs in Wikipedia "See also" sections are category
        headers that trigger MD036.
        """
        _BOLD_ONLY = frozenset({"b", "strong"})
        content_children = [
            c
            for c in ele.children
            if not (isinstance(c, NavigableString) and not c.strip())
        ]
        if (
            len(content_children) == 1
            and isinstance(content_children[0], Tag)
            and content_children[0].name in _BOLD_ONLY
        ):
            return content_children[0]
        return None

    @classmethod
    def _is_list_only(cls, ele: Tag) -> bool:
        """Return whether *ele*'s content consists solely of lists.

        Emphasis around a whole list has no Markdown representation: wrapping
        the rendered list (``__- a <br/> - b__``) leaves the item markers inside
        the emphasis span.  Such wrappers push the emphasis onto each item
        instead, and this predicate recognises them.
        """
        children = [
            c
            for c in ele.children
            if not (isinstance(c, NavigableString) and not c.strip())
        ]
        if not children:
            return False
        return all(
            isinstance(child, Tag)
            and (child.name in _LIST_TAGS or cls._is_list_only(child))
            for child in children
        )

    def _bold_list_items(self, ele: Tag) -> None:
        """Wrap every list item's content in ``<b>`` so bold survives."""
        for list_ele in ele.find_all(list(_LIST_TAGS)):
            for item in list_ele.find_all("li", recursive=False):
                TableConverter._wrap_children(item, self._soup, "b")

    def _handle_bold_italic(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render bold/italic text with Markdown emphasis markers.

        Emphasis already opened by an ancestor is not re-opened: Markdown has
        no nested-bold concept, and Wikipedia markup routinely nests bold
        containers (e.g. a CSS-bold ``sidebar-list-title`` around a
        presenter-synthesised ``<b>``), which would otherwise render as the
        meaningless ``____text____``.
        """
        bold = (
            ele.name in {"b", "strong"}
            or _BOLD_FONT_STYLE_REGEX.search(str(ele.get("style", "")))
            and "mw-heading" not in classes
        )
        italic = ele.name in {"em", "i"} or _ITALIC_FONT_STYLE_REGEX.search(
            str(ele.get("style", ""))
        )
        if bold and self._is_list_only(ele):
            # A bolded list is rendered by bolding each item, not by wrapping
            # the whole list (which would leave ``- `` markers inside ``__``).
            self._bold_list_items(ele)
            bold = False
        if bold and self._has_emphasis_ancestor(ele, bold=True):
            bold = False
        if italic and self._has_emphasis_ancestor(ele, bold=False):
            italic = False
        bold_str = "__" if bold else ""
        italic_str = "_" if italic else ""
        prefix = f"{bold_str}{italic_str}"
        suffix = f"{italic_str}{bold_str}"
        if self._needs_separator_before(self._rendered_neighbour(ele, following=False)):
            prefix = f"{_cfg._MARKDOWN_SEPARATOR}{prefix}"
        if self._needs_separator_after(self._rendered_neighbour(ele, following=True)):
            suffix += _cfg._MARKDOWN_SEPARATOR

        # Equation-reference numbers (the ``math_N`` / ``math_Eq.N`` spans
        # inside numblk tables) need two fixes that the generic handler
        # misses: (1) an ``<a id>`` anchor so prose links to the equation
        # resolve, and (2) parentheses around bare-integer numbers, which
        # Wikipedia renders via CSS pseudo-elements. Both paths (numblk in a
        # ``div.equation-box`` and standalone numblk tables) route the number
        # span through here, so this is the single unified fix point.
        if self._is_equation_reference(ele):
            prefix = f"{self._equation_reference_anchor(ele)}{prefix}"
            self._wrap_bare_integer_number(ele)

        config = _HandlerConfig(prefix=prefix, suffix=suffix, full_result=False)

        def process(strings: str) -> str:
            """Handle separator characters around bold/italic regions."""
            match = _PROCESS_STRINGS_BI_REGEX.match(strings)
            if not match:
                return _wrap_bare_url(strings)
            config.prefix = f"{match[1]}{config.prefix}"
            config.suffix += match[3]
            return _wrap_bare_url(match[2])

        config.process_strings = process
        if ele.name in _TD_OR_TH:
            original_process = config.process_strings

            def cell_process(strings: str) -> str:
                """Apply table cell processing for bold headers/cells."""
                return TableConverter.process_table_cell(original_process(strings))

            config.process_strings = cell_process
        return config

    def _handle_s(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render <s> as strikethrough Markdown."""
        prefix, suffix = _tag_affixes("s")
        return _HandlerConfig(prefix=prefix, suffix=suffix)

    @staticmethod
    def _is_equation_reference(ele: Tag) -> bool:
        """Detect a numblk equation-reference number span.

        These carry an ``id`` of the form ``math_N`` / ``math_Eq.N`` and the
        ``nourlexpansion`` / ``reference`` classes. The ``id`` is the anchor
        target that prose links (``#math_N``) point at.
        """
        if not (ele_id := ele.get("id")):
            return False
        if not re.fullmatch(r"math[_.].+", str(ele_id)):
            return False
        classes = frozenset(ele.get_attribute_list("class"))
        return bool(classes & {"nourlexpansion", "reference"})

    def _equation_reference_anchor(self, ele: Tag) -> str:
        """Build the Markdown ``<a id>`` anchor for an equation reference.

        The anchor id must match the fragment used by prose links. A bare
        ``math_1`` is referenced raw (``#math_1``), while a dotted
        ``math_Eq.1`` is referenced via the normalized Wikipedia fragment
        (``#math%20Eq.1``), so the id is normalized the same way
        (underscores -> spaces) to keep the two in sync.
        """
        ele_id = str(ele["id"])
        if "." in ele_id:
            anchor_id = _fix_name_maybe(
                ele_id, replace_underscores=True, names_map=self._names_map
            )
        else:
            anchor_id = ele_id
        return f'<a id="{anchor_id}"></a> '

    @staticmethod
    def _wrap_bare_integer_number(ele: Tag) -> None:
        """Wrap a bare-integer equation number in parentheses in place.

        Wikipedia renders the surrounding parentheses via CSS
        pseudo-elements; the converter must materialize them. Labels such as
        ``Eq.1`` and the ``numblk-raw-n`` opt-out class are left untouched.
        """
        if "numblk-raw-n" in frozenset(ele.get_attribute_list("class")):
            return
        text = ele.get_text(strip=True)
        if re.fullmatch(r"\d+", text):
            ele.clear()
            ele.string = f"({text})"

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

    def _handle_span(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig | None:
        """Handle <span> elements: replace sfrac sub-trees with <math>."""
        self._replace_sfrac_with_math(ele)
        return None

    def _replace_sfrac_with_math(self, ele: Tag) -> None:
        """Replace sfrac elements with inline <math> elements."""
        LatexConverter.replace_sfrac_with_math(ele, self._soup)

    @staticmethod
    def _in_list_item(ele: Tag) -> bool:
        """Return True when *ele* is nested inside a list item (<li>)."""
        return any(isinstance(p, Tag) and p.name == "li" for p in ele.parents)

    @staticmethod
    def _in_table_cell(ele: Tag) -> bool:
        """Check if element is nested inside a <td> or <th>."""
        return any(isinstance(p, Tag) and p.name in _TD_OR_TH for p in ele.parents)

    @staticmethod
    def _in_texhtml(ele: PageElement) -> bool:
        """Check if *ele* is nested inside a ``texhtml`` math span."""
        parent = ele.parent
        while isinstance(parent, Tag):
            if "texhtml" in frozenset(parent.get_attribute_list("class")):
                return True
            parent = parent.parent
        return False

    @staticmethod
    def _is_inline_emphasis(ele: Tag) -> bool:
        """Return True for inline emphasis elements.

        Covers the explicit emphasis tags (``b``, ``em``, ``i``, ``strong``)
        and ``<span>`` elements whose inline style forces bold or italic
        (e.g. ``font-weight: bold`` / ``font-style: italic``).
        """
        if ele.name in _BOLD_OR_ITALIC:
            return True
        if ele.name == "span":
            style = str(ele.get("style", ""))
            return bool(
                _BOLD_FONT_STYLE_REGEX.search(style)
                or _ITALIC_FONT_STYLE_REGEX.search(style)
            )
        return False

    @staticmethod
    def _is_inline_link(ele: Tag) -> bool:
        """Return True for inline link (anchor) elements."""
        return ele.name == "a"

    @staticmethod
    def _in_inline_context(ele: Tag) -> bool:
        """Check if element is inside a handler that provides block spacing.

        Returns True when the image/audio appears inside an element whose
        handler already injects its own block-level spacing (``\n`` or
        ``\n\n``), so the image/audio should NOT add its own ``\n\n``.

        Excludes ``<p>`` because the ``<p>`` handler's ``\n\n`` suffix
        goes *after* the entire element, not between its children.
        Excludes ``<div>`` and ``<figure>`` for similar block-level
        separation reasons.
        """
        for p in ele.parents:
            if not isinstance(p, Tag):
                continue
            if p.name in {"li", "td", "th", "div", "figure"}:
                return p.name != "div" and p.name != "figure"
        return False

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

    def _handle_div(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig | None:
        """Handle <div> elements, with special handling for equation-box divs."""
        if "shortdescription" in classes:
            return _HandlerConfig(suffix="\n\n")
        if "thumbcaption" in classes and not self._in_table_cell(ele):
            # Figure captions are block-level content: give them their own
            # ``> `` line (blank ``> `` separation from following siblings),
            # e.g. multi-image ``tmulti`` thumbnails with per-image captions.
            return _HandlerConfig(suffix="\n\n")
        if (
            "sidebar-caption" in classes or "infobox-caption" in classes
        ) and self._in_table_cell(ele):
            # Inside an infobox/sidebar cell, the caption follows the image
            # or math on the same cell line; separate it with a ``<p>``
            # marker (the cell-internal separator convention) rather than a
            # block break.
            return _HandlerConfig(prefix=" <p> ")
        if "equation-box" not in classes:
            return self._handle_block_level(ele, classes)

        # Find the numblk table.
        numblk = ele.find("table", class_="numblk")
        title = self._equation_box_title(ele, has_numblk=numblk is not None)

        # No title and no numbering: nothing to table-ify -> plain block.
        if not title and numblk is None:
            return self._handle_block_level(ele, classes)

        # The box's declared alignment, inherited by all its cells.
        align = ""
        if m := _TEXT_ALIGN_REGEX.search(str(ele.get("style", ""))):
            align = m[1]

        # Remove spacer columns (width=0px <td>) from numblk rows.
        if numblk is not None:
            for tdh in tuple(numblk.find_all(_TD_OR_TH)):
                style = str(tdh.get("style", ""))
                if re.search(r"width\s*:\s*0", style, re.IGNORECASE):
                    tdh.decompose()

        # Build a new table whose cells carry the box's alignment; the
        # TableConverter derives alignment markers from these cells.
        new_table = self._soup.new_tag("table")
        tbody = self._soup.new_tag("tbody")
        new_table.append(tbody)

        # Header row: title in <th>; equation-number <th> only when a
        # numblk table (numbering) is present.
        header_row = self._soup.new_tag("tr")
        th1 = self._soup.new_tag("th")
        if align:
            _set_text_align(th1, align)
        # ``title`` is the list of leading inline nodes (e.g. ``<b>`` plus a
        # trailing parenthetical text run).  Append each so inline formatting
        # and the parenthetical are preserved in the header cell.
        for _title_node in title:
            th1.append(_title_node)
        header_row.append(th1)
        if numblk is not None:
            th2 = self._soup.new_tag("th")
            if align:
                _set_text_align(th2, align)
            header_row.append(th2)
        tbody.append(header_row)

        if numblk is not None:
            # Append cleaned numblk rows, propagating the box's alignment
            # onto cells that do not declare their own.
            for tr in numblk.find_all("tr"):
                new_tr = copy(tr)
                if align:
                    for cell in new_tr.find_all(_TD_OR_TH):
                        _set_text_align(cell, align)
                # The equation-number cell is the last cell. Wikipedia bolds
                # it *and* its inner reference span; drop the redundant
                # cell-level bold so the number renders as a single
                # ``__N__`` rather than ``____N____``.
                if cells := tuple(new_tr.find_all(_TD_OR_TH)):
                    _strip_cell_bold(cells[-1])
                tbody.append(new_tr)
        else:
            # No numblk table: place the remaining content in a single
            # body cell (no empty equation-number column).
            body_row = self._soup.new_tag("tr")
            body_cell = self._soup.new_tag("td")
            if align:
                _set_text_align(body_cell, align)
            for child in list(ele.children):
                body_cell.append(copy(child))
            body_row.append(body_cell)
            tbody.append(body_row)

        # Replace div children with the new table.
        ele.clear()
        ele.append(new_table)

        return None

    def _handle_figcaption(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render ``<figcaption>`` as block-level caption content."""
        return _HandlerConfig(suffix="" if self._in_table_cell(ele) else "\n\n")

    @staticmethod
    def _find_box_title(
        ele: Tag, *, has_numblk: bool
    ) -> list[Tag | NavigableString] | None:
        """Detect the leading title of a box div without extracting it.

        The title is the run of leading inline nodes (bare text and inline
        tags such as ``<b>``/``<strong>``) before the first block-level
        body element (e.g. ``<p>``) or numblk table.  This captures a title
        followed by a trailing parenthetical text run, e.g.
        ``<b>Routhian</b> (n + s degrees of freedom)``, so the whole run can
        be merged into the header cell.  Returns None when the box has no
        distinct title (e.g. pure equation content).
        """
        title_nodes: list[Tag | NavigableString] = []
        for child in list(ele.children):
            if isinstance(child, NavigableString):
                if not child.strip():
                    continue
                if not has_numblk and not any(
                    isinstance(sib, Tag) and sib.name in _EQUATION_BOX_BODY_BLOCK_TAGS
                    for sib in ele.children
                ):
                    return None
                title_nodes.append(child)
                continue
            if isinstance(child, Tag) and child.name in _EQUATION_BOX_TITLE_TAGS:
                title_nodes.append(child)
                continue
            return title_nodes if title_nodes else None
        return title_nodes if title_nodes else None

    @staticmethod
    def _equation_box_title(
        ele: Tag, *, has_numblk: bool
    ) -> list[Tag | NavigableString]:
        """Extract the leading title of an equation-box div.

        The title is the run of leading inline nodes (bare text and inline
        tags such as ``<b>``/``<strong>``) before the first block-level
        body element or numblk table.  The title nodes are removed from
        *ele* so the remaining children form the body.  Returns an empty
        list when the box has no distinct title (e.g. pure equation
        content).
        """
        title = WikiHtmlConverter._find_box_title(ele, has_numblk=has_numblk)
        if title is None:
            return []
        for node in title:
            node.extract()
        return title

    _handle_dd = _handle_block_level
    _handle_dt = _handle_block_level

    def _handle_dl(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render <dl> definition lists, one row per line."""
        # Join sibling rows with "\n" instead of the default "" so that each
        # <dd>/<dt> (e.g. a sole-math row) stays on its own line.  Whitespace-
        # only text between rows is dropped first, otherwise it would join as
        # empty strings and produce stray blank lines (changing single-row
        # output).  Keep the current no-joiner behavior inside table cells.
        in_table = self._in_table_cell(ele)
        in_list = self._in_list_item(ele)
        joiner = "" if in_table else "\n"
        if joiner:
            for child in tuple(ele.children):
                if isinstance(child, NavigableString) and not child.strip():
                    child.extract()
        # Terminate the block with a blank line like <p> does, so a sole-math
        # <dd> row is symmetric (blank line before and after).  Inside a list
        # item, however, the <dl> is inline content of the <li>: use the cell-
        # internal ``<p>`` separator so the <li> stays on one line (e.g. a
        # citation whose reference text spans a definition list).  The
        # separator already supplies the space, so drop any leading whitespace
        # on the text node that follows the <dl> to avoid a double space.
        if in_table:
            suffix = ""
        elif in_list:
            # The <dl> is inline content of the <li>: use the cell-internal
            # ``<p>`` separator so the <li> stays on one line.  The separator
            # already supplies a space; if the text node that follows the <dl>
            # also carries a leading space (preserved by the inline-string
            # handler), drop the suffix's trailing space to avoid a double
            # space.  Otherwise keep the trailing space so the separator is not
            # collapsed into the following text.
            nxt = ele.next_sibling
            if isinstance(nxt, NavigableString) and str(nxt)[:1] in " \t\n\r\x0b\x0c":
                suffix = " <p>"
            else:
                suffix = " <p> "
        else:
            suffix = "\n\n"
        return _HandlerConfig(joiner=joiner, suffix=suffix)

    def _handle_p(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Render a <p> paragraph with appropriate spacing."""

        def process(strings: str) -> str:
            """Collapse whitespace runs in paragraph text."""
            return _collapse_whitespace(strings)

        in_table = self._in_table_cell(ele)
        prefix = "\n" if not in_table else ""
        suffix = "" if in_table else "\n\n"

        # Bold-only paragraphs (e.g., "See also" category headers) trigger
        # MD036 (no-emphasis-as-heading).  Suppress per-line rather than
        # converting to a heading, preserving the original bold rendering.
        # The comment must be on the immediately preceding line (no blank line
        # between comment and content) for markdownlint to apply the suppression.
        if not in_table and self._sole_bold_child(ele) is not None:
            prefix = "\n<!-- markdownlint-disable-next-line MD036 -->\n"

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
    def _math_outer_span(math_ele: Tag) -> Tag | None:
        """Return the ``mwe-math-element`` wrapper around a ``<math>`` tag."""
        parent: PageElement | None = math_ele
        while parent is not None:
            if isinstance(parent, Tag):
                class_str = " ".join(parent.get_attribute_list("class"))
                if "mwe-math-element" in class_str:
                    return parent
            parent = parent.parent
        return None

    @staticmethod
    def _following_punctuation_sibling(outer_span: Tag) -> str:
        """Return ``.`` or ``,`` when the next substantive sibling is punct-only."""
        sibling: PageElement | None = outer_span.next_sibling
        while isinstance(sibling, NavigableString) and not sibling.strip():
            sibling = sibling.next_sibling
        if isinstance(sibling, NavigableString):
            stripped = sibling.strip()
            if stripped in {".", ","}:
                return stripped
        return ""

    @staticmethod
    def _decompose_punctuation_sibling(outer_span: Tag) -> None:
        """Remove a punct-only text sibling immediately following *outer_span*."""
        sibling: PageElement | None = outer_span.next_sibling
        while isinstance(sibling, NavigableString) and not sibling.strip():
            sibling = sibling.next_sibling
        if isinstance(sibling, NavigableString):
            stripped = sibling.strip()
            if stripped in {".", ","}:
                sibling.extract()

    @staticmethod
    def _substantive_child_count(container: Tag) -> int:
        """Count non-whitespace children of *container*."""
        return sum(
            1
            for child in container.children
            if not (isinstance(child, NavigableString) and not child.strip())
        )

    @staticmethod
    def _contains_display_environment(alt_text: str) -> bool:
        """Return whether *alt_text* closes a known display math environment."""
        return any(rf"\end{{{env}}}" in alt_text for env in _DISPLAY_MATH_ENVIRONMENTS)

    @staticmethod
    def _qualifies_for_external_punct_absorption(
        container: Tag, outer_span: Tag, alt_text: str
    ) -> bool:
        """Return whether external punct after *outer_span* should be absorbed."""
        if not WikiHtmlConverter._following_punctuation_sibling(outer_span):
            return False
        if WikiHtmlConverter._substantive_child_count(container) != 2:
            return False
        if container.name in _DISPLAY_MATH_CONTAINERS:
            return True
        return WikiHtmlConverter._contains_display_environment(alt_text)

    @staticmethod
    def _inject_external_punctuation(alt_text: str, punct: str) -> str:
        """Insert ``\\,`` + *punct* inside display envs or at end of *alt_text*."""
        suffix = R"\," + punct
        best_idx = -1
        for env in _DISPLAY_MATH_ENVIRONMENTS:
            end_token = rf"\end{{{env}}}"
            idx = alt_text.rfind(end_token)
            if idx > best_idx:
                best_idx = idx
        if best_idx >= 0:
            return alt_text[:best_idx].rstrip() + suffix + alt_text[best_idx:]
        return alt_text.rstrip() + suffix

    @staticmethod
    def _math_sibling_container(math_ele: Tag) -> Tag | None:
        """Return the element whose substantive children drive inline/block classification."""
        outer_span = WikiHtmlConverter._math_outer_span(math_ele)
        if outer_span is not None:
            parent = outer_span.parent
            return parent if isinstance(parent, Tag) else None
        parent: PageElement | None = math_ele.parent
        if not isinstance(parent, Tag):
            return None
        for _ in range(2):
            parent = parent.parent
            if not isinstance(parent, Tag):
                return None
        return parent

    @staticmethod
    def _is_inline_math(ele: Tag, *, alt_text: str = "") -> bool:
        """Determine if a <math> element should use inline $ delimiters."""
        parent = ele.parent
        if not parent or "inline" not in str(parent.get("class", "")):
            return False
        outer_span = WikiHtmlConverter._math_outer_span(ele)
        container = WikiHtmlConverter._math_sibling_container(ele)
        if not isinstance(container, Tag):
            return False
        if (
            outer_span is not None
            and WikiHtmlConverter._qualifies_for_external_punct_absorption(
                container, outer_span, alt_text
            )
        ):
            return False
        return WikiHtmlConverter._substantive_child_count(container) > 1

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
    def _prepare_math_alttext(raw: str) -> str:
        """Strip Wikipedia math wrappers from an ``alttext`` attribute value."""
        alt_text = str(raw).strip()
        for _prefix in (R"{\displaystyle", R"{\textstyle"):
            if alt_text.startswith(_prefix):
                alt_text = alt_text.removeprefix(_prefix).lstrip()
                alt_text = alt_text.removesuffix(R"}")
                break
        if alt_text.endswith(R"\ "):
            alt_text += "{}"
        else:
            alt_text = alt_text.rstrip()
        return alt_text

    def _normalize_external_math_punctuation(self, container: Tag) -> None:
        """Absorb external punct into ``alttext`` before concurrent child conversion."""
        for child in list(container.children):
            if not isinstance(child, Tag):
                continue
            class_str = " ".join(child.get_attribute_list("class"))
            if "mwe-math-element" not in class_str:
                continue
            outer_span = child
            math = outer_span.find("math")
            if not isinstance(math, Tag):
                continue
            raw_alttext = math.get("alttext")
            if not raw_alttext:
                continue
            alt_text = self._prepare_math_alttext(str(raw_alttext))
            if not self._qualifies_for_external_punct_absorption(
                container, outer_span, alt_text
            ):
                continue
            punct = self._following_punctuation_sibling(outer_span)
            if not punct:
                continue
            math["alttext"] = self._inject_external_punctuation(alt_text, punct)
            self._decompose_punctuation_sibling(outer_span)

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
            alt_text = self._prepare_math_alttext(str(alt_text))
            alt_text = self._escape_flashcard_delimiters(alt_text)
            # Workaround for KaTeX 0.16.21 (bundled in VS Code's markdown-math
            # extension): \! and \negthinspace before _/^ trigger an "unknown
            # group type: 'internal'" ParseError.  \mkern-3mu renders
            # identically and is handled correctly by all KaTeX versions.
            # Can remove once VS Code upgrades past KaTeX 0.16.21.
            alt_text = re.sub(
                r"\\(?:\!|negthinspace)(?=[_^])", r"\\mkern-3mu", alt_text
            )

            inline = self._is_inline_math(ele, alt_text=alt_text)
            prefix, suffix = (
                "$" if inline else "$$",
                "$" if inline else "$$",
            )

            if inline:
                alt_text, punct = self._strip_trailing_punctuation(alt_text)
                suffix += punct

            ele.clear()
            ele.append(alt_text)

        return _HandlerConfig(prefix=prefix, suffix=suffix)

    def _texhtml_to_latex(self, ele: PageElement) -> str:
        """Convert a texhtml HTML subtree to a LaTeX string."""
        return LatexConverter.texhtml_to_latex(ele)

    def _texhtml_to_latex_children(self, children: Iterable[PageElement]) -> str:
        """Process children in batch, detecting radical patterns across siblings."""
        return LatexConverter.texhtml_to_latex_children(children)

    def _texhtml_to_latex_sfrac(self, ele: Tag) -> str:
        """Convert a ``sfrac`` span to LaTeX ``\\frac``."""
        return LatexConverter.texhtml_to_latex_sfrac(ele)

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

        # Insert space between adjacent markdown constructs (e.g.,
        # ``![icon](url)[link](url)``) that lack whitespace separation.
        _ADJACENT_RE = re.compile(r"\)(?=\[)")

        def process(strings: str) -> str:
            """Strip list prefixes and join portal items inline."""
            lines = [line.strip() for line in strings.split("\n")]
            parts = [
                line.removeprefix("- ").removeprefix("* ") for line in lines if line
            ]
            # Separate portal items with a blank line so each renders on its
            # own ``> `` line inside a blockquote (e.g. the "see also" box).
            return _ADJACENT_RE.sub(r"\g<0> ", "\n\n".join(parts))

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
        if "gallerybox" in classes:

            def process(strings: str) -> str:
                """Wrap gallery item content in blockquote markers."""
                parts = strings.strip().split("\n\n", 1)
                lines: list[str] = []
                for i, part in enumerate(parts):
                    if i > 0:
                        lines.append(">")
                    for line in part.strip().split("\n"):
                        lines.append(f"> {line}")
                return "\n".join(lines)

            return _HandlerConfig(
                prefix="",
                suffix="\n",
                joiner="\n",
                process_strings=process,
            )

        item = list_stack[-1] if list_stack else -1
        li_suffix = "\n"
        if item >= 1:
            prefix = f"{_cfg._LIST_INDENT * (len(list_stack) - 1)}{item}. "
            if str(ele.get("id", "")).startswith("cite_"):
                group = next(
                    (
                        str(parent.get("data-mw-group"))
                        for parent in ele.parents
                        if parent.name == "ol" and parent.get("data-mw-group")
                    ),
                    None,
                )
                name = group or "ref"

                def process(strings: str, item: int = item, name: str = name) -> str:
                    """Process citation list items with anchor markers."""
                    strings = strings.lstrip("\t\n\r\x0b\x0c \xa0")
                    try:
                        idx = strings.index("\n")
                    except ValueError:
                        idx = len(strings)
                    return f'{strings[:idx]} <a id="^{name}-{item}"></a>^{name}-{item}{strings[idx:].rstrip()}'

                return _HandlerConfig(
                    prefix=prefix,
                    suffix=li_suffix,
                    process_strings=process,
                )

            def process(strings: str) -> str:
                """Strip leading formatting whitespace from list text."""
                return strings.lstrip("\t\n\r\x0b\x0c \xa0")

            return _HandlerConfig(
                prefix=prefix,
                suffix=li_suffix,
                process_strings=process,
            )
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

    @staticmethod
    def _is_in_equation_box(ele: Tag) -> bool:
        """Return True if *ele* is nested inside a ``div.equation-box``."""
        parent = ele.parent
        while isinstance(parent, Tag):
            if parent.name == "div" and "equation-box" in parent.get_attribute_list(
                "class"
            ):
                return True
            parent = parent.parent
        return False

    def _handle_table(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig | None:
        """Handle <table> elements, integrating caption as a header row.

        A standalone ``numblk`` table (a sibling of an equation-box div, not
        a descendant) is rendered as a two-column equation table: an empty
        header row plus an alignment marker row, so its equation/number body
        row aligns like a numblk nested inside an equation-box div.  This
        mirrors the header+alignment layout that ``_handle_div`` builds for
        the nested case.
        """
        if "numblk" in classes and not WikiHtmlConverter._is_in_equation_box(ele):
            align = ""
            box = ele.find_previous("div", class_="equation-box")
            if isinstance(box, Tag) and (
                m := _TEXT_ALIGN_REGEX.search(str(box.get("style", "")))
            ):
                align = m[1]

            # Drop empty spacer cells (no text and no explicit width:0px style).
            for tdh in tuple(ele.find_all(_TD_OR_TH)):
                if not tdh.get_text(strip=True) and not re.search(
                    r"width\s*:\s*0", str(tdh.get("style", "")), re.IGNORECASE
                ):
                    tdh.decompose()

            tbody = ele.find("tbody") or ele
            header_row = self._soup.new_tag("tr")
            th1 = self._soup.new_tag("th")
            th2 = self._soup.new_tag("th")
            if align:
                _set_text_align(th1, align)
                _set_text_align(th2, align)
            header_row.append(th1)
            header_row.append(th2)
            tbody.insert(0, header_row)

            if align:
                for tr in tbody.find_all("tr"):
                    if tr is header_row:
                        continue
                    for cell in tr.find_all(_TD_OR_TH):
                        _set_text_align(cell, align)
                    if cells := tuple(tr.find_all(_TD_OR_TH)):
                        _strip_cell_bold(cells[-1])

            return TableConverter.handle_table(ele, classes, self._soup)

        return TableConverter.handle_table(ele, classes, self._soup)

    def _handle_tbody(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <tbody> table body elements."""
        return TableConverter.handle_tbody(
            ele,
            classes,
            self._soup,
            names_map=self._names_map,
        )

    def _handle_thead(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <thead> table head elements."""
        return TableConverter.handle_thead(ele, classes, self._soup)

    def _handle_tr(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <tr> table row elements."""
        return TableConverter.handle_tr(ele, classes, self._soup)

    def _handle_td(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Dispatch <td> table cell elements."""
        return TableConverter.handle_td(ele, classes, self._soup)

    def _handle_th(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Dispatch <th> table header cell elements."""
        return TableConverter.handle_th(ele, classes, self._soup)

    def _process_archive_url(self, src: str) -> str:
        """Resolve a media URL to a local archive path."""
        src_url = _strip_url_query(_cfg._WIKI_HOST_URL.join(URL(str(src))))
        src_url_str = str(src_url)
        for regex, formats in _cfg._ARCHIVE_REGEXES.items():
            if not (match := regex.search(src_url.human_repr())):
                continue
            to_archive = unquote(match[1])
            self._out_to_archive.add(formats[0].format(to_archive))
            src_url_str = quote(formats[1].format(to_archive.replace("_", " ")))
        return src_url_str

    def _derive_media_alt(self, *, ele: Tag, explicit_alt: str | None = None) -> str:
        """Derive alt text for a media embed — the canonical image mechanism.

        1. Prefer ``explicit_alt`` (the element's ``alt`` attribute) when non-empty.
        2. Otherwise fall back to the uploaded filename: ``File:<name>`` with
           underscores→spaces, or an ``image_metadata`` description when present.
        3. Markdown-escape the label; for a description, balance brackets instead.
        4. Normalize paragraphs (``\\n\\n`` → `` <p> ``) and line breaks
           (``\\n`` → `` <br/> ``).
        """
        alt = (explicit_alt or "").strip()
        if not alt:
            filename = _get_image_filename(ele)
            if not filename:
                return ""
            file_title = f"File:{filename}"
            if desc := self._image_metadata.get(file_title, ""):
                alt = desc
            else:
                alt = file_title
            if filename and file_title in self._image_metadata:
                alt = _balance_brackets(alt)
            else:
                alt = _cfg._MARKDOWN_ESCAPE_REGEX.sub(lambda m: Rf"\{m[0]}", alt)
        else:
            alt = _cfg._MARKDOWN_ESCAPE_REGEX.sub(lambda m: Rf"\{m[0]}", alt)
        paragraphs = alt.split("\n\n")
        alt = (" <p> ".join(paragraphs)).strip()
        alt = alt.replace("\n", " <br/> ")
        return alt

    def _build_media_config(
        self,
        *,
        ele: Tag,
        src: str,
        embed: bool,
        explicit_alt: str | None = None,
    ) -> _HandlerConfig:
        """Build a handler config that emits a media link/embed.

        Alt text is derived here via ``_derive_media_alt`` — never by the caller —
        so every media embed (image, video, audio) applies the canonical mechanism.
        """
        text = self._derive_media_alt(ele=ele, explicit_alt=explicit_alt).strip()
        src_url_str = self._process_archive_url(str(src))
        link = f"{'!' if embed else ''}[{text}]({src_url_str})"
        return _HandlerConfig(
            suffix="" if self._in_inline_context(ele) else "\n\n",
            process_strings=lambda _strings: link,
        )

    def _handle_audio(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <audio> media elements."""
        if (src := ele.get("href")) is None:
            return _HandlerConfig()
        return self._build_media_config(
            ele=ele,
            src=str(src),
            embed="mw-tmh-player" in classes,
        )

    def _handle_image(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <img> image elements with download and link."""
        if (src := ele.get("src")) is None:
            return _HandlerConfig()
        return self._build_media_config(
            ele=ele,
            src=str(src),
            embed=True,
            explicit_alt=str(ele.get("alt", "")),
        )

    def _handle_video(self, ele: Tag, classes: frozenset[str]) -> _HandlerConfig:
        """Handle <video> media elements, routing through the shared helper."""
        if (resource := ele.get("resource")) is not None:
            src = str(resource)
        elif (data_mwtitle := ele.get("data-mwtitle")) is not None:
            src = f"/wiki/File:{data_mwtitle}"
        else:
            source = next((c for c in ele.find_all("source", recursive=False)), None)
            if source is not None:
                src = str(source.get("resource") or source.get("src"))
            elif (poster := ele.get("poster")) is not None:
                src = str(poster)
            else:
                return _HandlerConfig()
        return self._build_media_config(ele=ele, src=src, embed=True)

    def _fallback_alt(self, ele: Tag) -> str:
        """Compute alt text fallback for an <img> element."""
        filename = _get_image_filename(ele)
        if not filename:
            return ""
        file_title = f"File:{filename}"
        if desc := self._image_metadata.get(file_title, ""):
            return desc
        return file_title

    async def _handle_anchor(
        self, ele: Tag, classes: frozenset[str]
    ) -> _HandlerConfig | None:
        """Handle ``<a>`` link elements."""
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
                    await _create_redirect_symlinks(
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
            elif href.startswith("#") and len(href) > 1:
                href = _markdown_fragment(
                    _fix_name_maybe(
                        href[1:],
                        replace_underscores=True,
                        names_map=self._names_map,
                    )
                )

            def process(strings: str) -> str:
                """Collapse whitespace in anchor text."""
                return _collapse_whitespace(strings)

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
