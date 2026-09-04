"""Table-to-Markdown conversion for Wikipedia HTML tables.

Contains ``TableConverter``, a stateless class whose classmethods and
staticmethods implement the table handling logic extracted from
``WikiHtmlConverter``.  Each method mirrors the corresponding
``_handle_*`` method from the converter, modified to accept its
dependencies (e.g. a BeautifulSoup object for tree manipulation) as
explicit parameters.
"""

import re
import urllib.parse
from collections.abc import Mapping
from copy import copy

from bs4 import NavigableString, PageElement, Tag

from .ast_utils import _replace_pipes_outside_math
from .types import _HandlerConfig
from .utils import _fix_name_maybe, _format_separator_cell, _smart_split_row

"""Table cell tag names."""
_TD_OR_TH = frozenset({"td", "th"})
"""Text-align style extractor."""
_TEXT_ALIGN_REGEX = re.compile(
    r"\btext-align\s*:\s*(left|center|right)\b", re.IGNORECASE
)
"""Bold font-weight style detector (needed for _handle_tr)."""
_BOLD_FONT_STYLE_REGEX = re.compile(r"\bfont-weight\s*:\s*bold\b", re.IGNORECASE)
"""Collapse consecutive newlines into at most two."""
_CONSECUTIVE_NEWLINES_REGEX = re.compile(r"\n\n+")
"""Replace leading whitespace with non-breaking spaces."""
_CONSECUTIVE_LEADING_WHITESPACES_REGEX = re.compile(r"(?:^|\n)([ \t]+)", re.MULTILINE)


class TableConverter:
    """Stateless table-to-Markdown conversion utilities.

    All methods are ``@classmethod`` or ``@staticmethod``.  Methods that
    modify the BeautifulSoup tree receive the ``soup`` object as an
    explicit parameter.
    """

    # -- Handlers mirroring WikiHtmlConverter._handle_* --

    @classmethod
    def handle_table(
        cls,
        ele: Tag,
        classes: frozenset[str],  # noqa: ARG003
        soup: Tag,
    ) -> _HandlerConfig | None:
        """Handle ``<table>`` elements, integrating caption as a header row.

        Parameters
        ----------
        ele:
            The ``<table>`` element.
        classes:
            Unused, kept for API compatibility with the dispatch signature.
        soup:
            The root BeautifulSoup object used to create new tags.

        Raises
        ------
        ValueError
            If the table has both a non-empty ``<caption>`` and an all-``<th>``
            header row, since Markdown tables allow only one header row.
        """
        caption = ele.find("caption", recursive=False)
        if caption is None:
            return None

        caption_text = caption.get_text(strip=True)
        if not caption_text:
            caption.decompose()
            return None

        # Find the first structural header row to determine column layout.
        target_tr: Tag | None = None
        for tr in ele.find_all("tr"):
            cells = [
                c for c in tr.children if isinstance(c, Tag) and c.name in _TD_OR_TH
            ]
            if cells and all(c.name == "th" for c in cells):
                raise ValueError(
                    "a table with both a <caption> and a <th> header row is "
                    "invalid: Markdown tables allow only one header row"
                )
            if any(c.name == "th" for c in cells):
                target_tr = tr
                break

        if target_tr is None:
            return None

        # Build a caption row with all <td> cells.
        cells = [
            c for c in target_tr.children if isinstance(c, Tag) and c.name in _TD_OR_TH
        ]
        caption_tr = soup.new_tag("tr")
        has_data_cell = False

        for cell in cells:
            new_cell = soup.new_tag("td")
            if cell.name == "td" and not has_data_cell:
                # First data column: prepend bold caption.
                bold = soup.new_tag("b")
                for child in caption.children:
                    if isinstance(child, Tag) or (
                        isinstance(child, NavigableString) and child.strip()
                    ):
                        bold.append(copy(child))
                new_cell.append(bold)
                new_cell.append(" ")
                has_data_cell = True
            else:
                # Header columns & extra data columns: zero-width space to
                # survive _filter_table_cells while rendering invisibly.
                new_cell.string = "\u200b"
            caption_tr.append(new_cell)

        # Mark caption row explicitly for alignment detection.
        caption_tr["data-caption-row"] = "true"

        # Insert caption row before the original first header row.
        target_tr.insert_before(caption_tr)

        caption.decompose()
        return None

    @classmethod
    def _is_navbox_blockquote_pattern(cls, tbody: Tag) -> bool:
        """Detect navbox tables with a single standalone inner wikitable.

        Returns True when the ``<tbody>`` belongs to a 2-TR navbox-inner
        table whose second row wraps a substantial inner wikitable (≥ 3
        rows).  These tables should be rendered as a blockquote containing
        the inner wikitable as a proper Markdown table, rather than
        flattened into br-separated inline text.
        """
        table = tbody.find_parent("table")
        if table is None:
            return False
        classes = set(table.get_attribute_list("class"))
        if "navbox-inner" not in classes:
            return False
        trs = tbody.find_all("tr", recursive=False)
        if len(trs) != 2:
            return False
        # First TR: single header cell.
        tr0_cells = [
            c for c in trs[0].children if isinstance(c, Tag) and c.name in _TD_OR_TH
        ]
        if len(tr0_cells) != 1:
            return False
        # Second TR: single td cell containing a nested table.
        tr1_cells = [
            c for c in trs[1].children if isinstance(c, Tag) and c.name in _TD_OR_TH
        ]
        if len(tr1_cells) != 1:
            return False
        inner_tables = tr1_cells[0].find_all("table")
        if not inner_tables:
            return False
        # Inner table should have multiple rows (substantial standalone table).
        for it in inner_tables:
            it_rows = it.find_all("tr", recursive=False)
            if not it_rows:
                it_tbody = it.find("tbody", recursive=False)
                if it_tbody:
                    it_rows = it_tbody.find_all("tr", recursive=False)
            if len(it_rows) >= 3:
                return True
        return False

    @classmethod
    def _extract_navbox_blockquote_header(
        cls,
        tbody: Tag,
        *,
        names_map: Mapping[str, str] | None = None,
    ) -> tuple[str, str]:
        """Extract the blockquote title and v/t/e link comment from a navbox header row.

        Returns a tuple of ``(title_md, link_comment)`` where
        *title_md* is the Markdown-formatted title (with resolved relative
        links) and *link_comment* is an HTML comment string containing the
        navbox template links (raw Wikipedia URLs).

        The title div (identified by ``font-size:114%`` in its style) may
        contain ``<a>`` tags whose hrefs are resolved through
        :func:`_fix_name_maybe` to produce local relative links.  Non-link
        text in the title is preserved as-is.
        """
        trs = tbody.find_all("tr", recursive=False)
        header_cell = next(
            (c for c in trs[0].children if isinstance(c, Tag) and c.name in _TD_OR_TH),
            None,
        )
        if header_cell is None:
            return "", ""
        # Build link comment from <a> tags, preserving href as Markdown links.
        links = header_cell.find_all("a")
        link_parts = [f"- [{a.get_text()}]({a.get('href', '')})" for a in links]
        link_comment = f"<!-- {' '.join(link_parts)} -->" if link_parts else ""
        # Extract the title div (font-size:114%).
        title_div = header_cell.find(
            "div",
            style=lambda s: s and "font-size" in s and "114%" in s,
        )
        if title_div is None:
            # Fallback: plain text without links.
            title_text = header_cell.get_text()
            title_text = re.sub(r"^vte\s*", "", title_text)
            title_text = title_text.strip()
            return title_text, link_comment
        # Build Markdown title from the div's <a> tags and text nodes.
        title_parts: list[str] = []
        for child in title_div.children:
            if isinstance(child, NavigableString):
                text = child.strip()
                if text:
                    title_parts.append(text)
            elif isinstance(child, Tag) and child.name == "a":
                href = str(child.get("href", ""))
                display = child.get_text(strip=True)
                # Resolve /wiki/Target → local relative link.
                wiki_title = href.removeprefix("/wiki/").replace("_", " ")
                resolved = _fix_name_maybe(
                    wiki_title,
                    replace_underscores=True,
                    names_map=names_map,
                )
                encoded = urllib.parse.quote(resolved)
                title_parts.append(f"[{display}]({encoded}.md)")
        title_md = " ".join(title_parts)
        return title_md, link_comment

    @classmethod
    def _extract_navbox_section_headers(cls, inner_wikitable: Tag) -> tuple[str, str]:
        """Extract CSS-bold section header text from the inner wikitable.

        The inner wikitable's first row contains two ``<td>`` cells with
        ``font-weight:bold`` styling that serve as section headers for the
        linear and angular columns.  This method extracts their plain text
        and removes them from the DOM so the remaining rows form a
        standard Markdown table.

        Returns
        -------
        A tuple of ``(linear_header, angular_header)`` where each string
        is the plain text of the corresponding section header, or empty
        if the cell was not found.
        """
        tbody = inner_wikitable.find("tbody", recursive=False)
        if tbody is None:
            return "", ""
        trs = tbody.find_all("tr", recursive=False)
        if not trs:
            return "", ""
        first_row = trs[0]
        bold_cells = [
            c
            for c in first_row.children
            if isinstance(c, Tag)
            and c.name == "td"
            and _BOLD_FONT_STYLE_REGEX.search(str(c.get("style", "")))
        ]
        linear_header = ""
        angular_header = ""
        if len(bold_cells) >= 1:
            linear_header = bold_cells[0].get_text(strip=True)
            bold_cells[0].extract()
        if len(bold_cells) >= 2:
            # After extracting the first, the second is still in bold_cells
            # only if it wasn't removed from the list.  Re-find to be safe.
            remaining = [
                c
                for c in first_row.children
                if isinstance(c, Tag)
                and c.name == "td"
                and _BOLD_FONT_STYLE_REGEX.search(str(c.get("style", "")))
            ]
            if remaining:
                angular_header = remaining[0].get_text(strip=True)
                remaining[0].extract()
        return linear_header, angular_header

    # Linear table: indices in the 9-column rendered row.
    _NAVBOX_LINEAR_INDICES = (0, 2, 3, 4)
    # Angular table: indices in the 9-column rendered row.
    _NAVBOX_ANGULAR_INDICES = (5, 6, 7, 8)

    @classmethod
    def _blockquote_wrap_navbox(
        cls,
        s: str,
        *,
        link_comment: str,
        title_md: str,
        linear_header: str,
        angular_header: str,
    ) -> str:
        """Wrap rendered navbox content in a blockquote with two 4-column tables.

        The pipeline renders the inner wikitable as a single Markdown table
        with 9 columns (4 linear + 1 empty separator + 4 angular).  This
        method splits each data row into two groups, constructs separate
        linear and angular Markdown tables, and wraps every line in a
        blockquote prefix (``> ``).
        """
        lines: list[str] = []
        if link_comment:
            lines.append(f"> {link_comment}")
            lines.append(">")
        if title_md:
            lines.append(f"> __{title_md}__")
            lines.append(">")
        if linear_header:
            lines.append(f"> __{linear_header}__")
            lines.append(">")

        header_row: list[str] = []
        data_rows: list[list[str]] = []

        for row in s.split("\n"):
            row = row.strip()
            if not row:
                continue
            cells = _smart_split_row(row)
            if cells is None:
                continue
            # Replace zero-width-space separator filler with empty string.
            cells = ["" if c == "\u200b" else c for c in cells]
            if not cells:
                continue
            # Skip alignment rows (cells contain only dashes).
            if all(c.replace("-", "").replace(":", "") == "" for c in cells):
                continue
            # Detect header row: first row with ≥ 3 cells.
            if not header_row and len(cells) >= 3:
                header_row = cells
                continue
            if len(cells) >= 3:
                data_rows.append(cells)

        def _pick(cells: list[str], indices: tuple[int, int, int, int]) -> list[str]:
            """Select columns by index, returning empty string for missing."""
            return [cells[i] if i < len(cells) else "" for i in indices]

        def _fmt(cells: list[str]) -> str:
            return f"> | {' | '.join(c if c else ' ' for c in cells)} |"

        # Build linear table (columns at _NAVBOX_LINEAR_INDICES).
        if header_row:
            lin_cols = _pick(header_row, cls._NAVBOX_LINEAR_INDICES)
            sep_cells = [_format_separator_cell(3, ":-:") for _ in lin_cols]
            lines.append(_fmt(lin_cols))
            lines.append(f"> | {' | '.join(sep_cells)} |")
        for row_cells in data_rows:
            lines.append(_fmt(_pick(row_cells, cls._NAVBOX_LINEAR_INDICES)))

        if angular_header:
            lines.append(">")
            lines.append(f"> __{angular_header}__")
            lines.append(">")

        # Build angular table (columns at _NAVBOX_ANGULAR_INDICES).
        if header_row:
            ang_cols = _pick(header_row, cls._NAVBOX_ANGULAR_INDICES)
            sep_cells = [_format_separator_cell(3, ":-:") for _ in ang_cols]
            lines.append(_fmt(ang_cols))
            lines.append(f"> | {' | '.join(sep_cells)} |")
        for row_cells in data_rows:
            lines.append(_fmt(_pick(row_cells, cls._NAVBOX_ANGULAR_INDICES)))

        return "\n".join(lines)

    @classmethod
    def handle_tbody(
        cls,
        ele: Tag,
        classes: frozenset[str],  # noqa: ARG003
        soup: Tag,
        *,
        names_map: Mapping[str, str] | None = None,
    ) -> _HandlerConfig:
        """Handle ``<tbody>`` table body elements.

        Parameters
        ----------
        ele:
            The ``<tbody>`` element.
        classes:
            Unused, kept for API compatibility.
        soup:
            The root BeautifulSoup object used to create new tags.
        names_map:
            Optional name map for resolving Wikipedia titles to local
            stems.  Passed through to the navbox blockquote header
            extractor.
        """
        # Check for navbox blockquote pattern BEFORE flattening.
        if cls._is_navbox_blockquote_pattern(ele):
            title_md, link_comment = cls._extract_navbox_blockquote_header(
                ele,
                names_map=names_map,
            )
            trs = ele.find_all("tr", recursive=False)
            inner_wikitable: Tag | None = None
            if len(trs) >= 2:
                # Extract the inner wikitable from the second TR's cell.
                second_td = next(
                    (
                        c
                        for c in trs[1].children
                        if isinstance(c, Tag) and c.name in _TD_OR_TH
                    ),
                    None,
                )
                if second_td is not None:
                    inner_wikitable = second_td.find("table")
                    if inner_wikitable is not None:
                        # Place inner wikitable directly in the <tbody> so
                        # _flatten_nested_tables won't wrap it in inline HTML.
                        inner_wikitable.extract()
                        ele.append(inner_wikitable)
                # Remove navbox header and second TRs.
                for tr in reversed(trs):
                    tr.extract()

            # Extract section headers from the inner wikitable's first row
            # BEFORE the pipeline converts it.  These bold <td> cells serve
            # as section headers for the linear and angular columns.
            linear_header = ""
            angular_header = ""
            if inner_wikitable is not None:
                linear_header, angular_header = cls._extract_navbox_section_headers(
                    inner_wikitable
                )

            # Let the remaining structure (inner wikitable in its own TR)
            # convert normally via the dispatch pipeline.
            cls._flatten_nested_tables(ele, soup)
            cls._normalize_table_cells(ele, soup)

            def _wrap(s: str) -> str:
                """Wrap inner wikitable output in blockquote with navbox headers."""
                result = cls._blockquote_wrap_navbox(
                    s,
                    link_comment=link_comment,
                    title_md=title_md,
                    linear_header=linear_header,
                    angular_header=angular_header,
                )
                return result + "\n\n" if result else result

            return _HandlerConfig(
                full_result=True,
                prefix="",
                suffix="\n\n",
                process_strings=_wrap,
            )
        cls._flatten_nested_tables(ele, soup)
        cls._transform_infobox_caption_rows(ele, soup)
        cls._normalize_table_cells(ele, soup)
        cls._merge_header_rows(ele, soup)
        cls._transform_sidebar_rows(ele, soup)
        cls._insert_mixed_alignment_rows(ele, soup)
        has_thead = ele.find_previous_sibling("thead") is not None
        return _HandlerConfig(prefix="" if has_thead else "\n", suffix="\n\n")

    @classmethod
    def handle_thead(
        cls,
        ele: Tag,
        classes: frozenset[str],  # noqa: ARG003
        soup: Tag,
    ) -> _HandlerConfig:
        """Handle ``<thead>`` table head elements.

        Parameters
        ----------
        ele:
            The ``<thead>`` element.
        classes:
            Unused, kept for API compatibility.
        soup:
            The root BeautifulSoup object used to create new tags.
        """
        cls._normalize_table_cells(ele, soup)
        cls._merge_header_rows(ele, soup)
        return _HandlerConfig(prefix="\n", suffix="")

    @classmethod
    def handle_tr(
        cls,
        ele: Tag,
        classes: frozenset[str],  # noqa: ARG003
        soup: Tag,
    ) -> _HandlerConfig:
        """Handle ``<tr>`` table row elements.

        Parameters
        ----------
        ele:
            The ``<tr>`` element.
        classes:
            Unused, kept for API compatibility.
        soup:
            The root BeautifulSoup object used to create new tags.
        """
        joiner = " | "
        prefix = "| "
        suffix = " |\n"

        for child in list(ele.children):
            if isinstance(child, NavigableString) and not child.strip():
                child.extract()

        tag_cells = [
            child
            for child in ele.children
            if isinstance(child, Tag) and child.name in _TD_OR_TH
        ]

        total_colspan = sum(int(str(c.get("colspan", "1"))) for c in tag_cells)

        # Check for alignment marker row (from _insert_mixed_alignment_rows).
        is_alignment_row = any(c.get("data-alignment-row") for c in [ele])
        if is_alignment_row:
            markers: list[str] = []
            for c in tag_cells:
                a = c.get("data-align", "---")
                markers.append(a if isinstance(a, str) else "---")
            return _HandlerConfig(
                full_result=True,
                prefix="",
                suffix="",
                process_strings=lambda _: f"| {' | '.join(markers)} |\n",
            )

        if tag_cells and all(child.name == "th" for child in tag_cells):
            table = ele.find_parent("table")
            has_scope_row = (
                table is not None and table.find("th", scope="row") is not None
            )

            # Determine alignment from content cells (majority rule),
            # then override with explicit <th> alignment only for columns
            # that have zero <td> cells.
            alignments, cols_with_data = (
                cls._td_cell_alignments(table) if table else ([], set())
            )
            for i, child in enumerate(tag_cells):
                header_align = cls._cell_alignment(child)
                if header_align != "---" and i not in cols_with_data:
                    # Header has explicit alignment & column has no <td> data
                    # → override content default.
                    while len(alignments) <= i:
                        alignments.append("---")
                    alignments[i] = header_align
            # Ensure at least as many alignments as cells.
            while len(alignments) < len(tag_cells):
                alignments.append("---")

            if has_scope_row and alignments:
                alignments[0] = "--:"
            suffix += f"| {' | '.join(alignments)} |\n"
        else:
            for child in ele.children:
                if isinstance(child, Tag) and child.name == "th":
                    if not _BOLD_FONT_STYLE_REGEX.search(str(child.get("style", ""))):
                        new_b = soup.new_tag("b")
                        for child_child in child.contents[:]:
                            new_b.append(child_child.extract())
                        child.append(new_b)
        return _HandlerConfig(
            joiner=joiner,
            prefix=prefix,
            suffix=suffix,
            process_strings=lambda s: cls._filter_table_cells(
                s, total_colspan=total_colspan
            ),
        )

    @classmethod
    def handle_td(
        cls,
        ele: Tag,  # noqa: ARG003
        classes: frozenset[str],  # noqa: ARG003
        soup: Tag,  # noqa: ARG003
    ) -> _HandlerConfig:
        """Dispatch ``<td>`` table cell elements.

        Parameters are kept for API compatibility with the dispatch
        signature even though only the return value matters.
        """
        return _HandlerConfig(process_strings=cls.process_table_cell)

    @classmethod
    def handle_th(
        cls,
        ele: Tag,  # noqa: ARG003
        classes: frozenset[str],  # noqa: ARG003
        soup: Tag,  # noqa: ARG003
    ) -> _HandlerConfig:
        """Dispatch ``<th>`` table header cell elements.

        Parameters are kept for API compatibility with the dispatch
        signature even though only the return value matters.
        """
        return _HandlerConfig(process_strings=cls.process_table_cell)

    # -- Soup-mutating helpers --

    @classmethod
    def _transform_infobox_caption_rows(cls, ele: Tag, soup: Tag) -> None:
        """Rewrite ``infobox-above`` / ``infobox-image`` rows as caption-style rows.

        An ``infobox-above`` ``<th colspan="2">`` title row is converted
        into a two-``<td>`` row: an empty zero-width-space column followed
        by a ``<b>``-wrapped copy of the original cell's children.  An
        ``infobox-image`` ``<td>`` row is converted into a two-``<td>`` row
        with an empty zero-width-space column followed by the original
        cell's children (image + ``infobox-caption`` div).  Both new rows
        are marked ``data-caption-row="true"`` so alignment detection and
        ``_td_cell_alignments`` skip them, mirroring the ``<caption>``
        handling in ``handle_table``.
        """
        for tr in tuple(ele.find_all("tr")):
            cells = [
                c for c in tr.children if isinstance(c, Tag) and c.name in _TD_OR_TH
            ]
            if len(cells) != 1:
                continue
            cell = cells[0]
            cell_classes = cell.get_attribute_list("class")

            if cell.name == "th" and "infobox-above" in cell_classes:
                new_tr = soup.new_tag("tr")
                col1 = soup.new_tag("td")
                col1.string = "\u200b"
                col2 = soup.new_tag("td")
                bold = soup.new_tag("b")
                for child in tuple(cell.children):
                    bold.append(child.extract())
                col2.append(bold)
                col2.append(" ")
                new_tr.append(col1)
                new_tr.append(col2)
                new_tr["data-caption-row"] = "true"
                new_tr["data-caption-title"] = "true"
                tr.replace_with(new_tr)
            elif cell.name == "td" and "infobox-image" in cell_classes:
                new_tr = soup.new_tag("tr")
                col1 = soup.new_tag("td")
                col1.string = "\u200b"
                col2 = soup.new_tag("td")
                for child in tuple(cell.children):
                    col2.append(child.extract())
                new_tr.append(col1)
                new_tr.append(col2)
                new_tr["data-caption-row"] = "true"
                tr.replace_with(new_tr)

    @classmethod
    def _normalize_table_cells(cls, ele: Tag, soup: Tag) -> None:
        """Normalize table cell layout for consistent column count.

        Expands ``colspan`` and ``rowspan`` attributes by inserting
        duplicate or filler cells so that every row has the same number
        of visible cells.
        """
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
                        next_tr = current_row.find_next_sibling("tr")
                        if next_tr is None:
                            break
                        current_row = next_tr
                        # Insert an empty cell to occupy the column position
                        # covered by the rowspan from a previous row.
                        new_tdh = soup.new_tag("td")
                        new_tdh.string = "\u200b"
                        new_tdh["data-filler-cell"] = "true"
                        current_row.insert(col_idx, new_tdh)

    @classmethod
    def _merge_header_rows(cls, ele: Tag, soup: Tag) -> None:
        """Merge consecutive header rows in ``<tbody>`` into a single row."""
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

        # Wrap sidebar-title-with-pretitle cell content in <big> element.
        if target_tr is not None:
            for target_cell in target_tr.children:
                if (
                    isinstance(target_cell, Tag)
                    and target_cell.name in _TD_OR_TH
                    and "sidebar-title-with-pretitle"
                    in target_cell.get_attribute_list("class")
                ):
                    children = list(target_cell.children)
                    big_tag = soup.new_tag("big")
                    for child in children:
                        big_tag.append(child.extract())
                    target_cell.append(big_tag)

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
                        br = soup.new_tag("br")
                        target_cell.insert(0, br)
                        for child in reversed(children):
                            target_cell.insert(0, child.extract())
                    elif target_cell.get_text(strip=True):
                        target_cell.insert(0, soup.new_tag("br"))

            tr.decompose()

    @classmethod
    def _transform_sidebar_rows(cls, ele: Tag, soup: Tag) -> None:
        """Apply Classical-mechanics sidebar formatting to a table in place.

        Wraps specific sidebar cells in ``<b>``/``<i>`` so the Markdown output
        matches the ``cm-sidebar`` template: the title (already wrapped in
        ``<big>`` by ``_merge_header_rows``) becomes ``<b><big>…</big></b>``,
        heading/list-title/below cells get per-item ``<b>`` wrapping, and the
        caption becomes ``<i>…</i>``.
        """
        table = ele.find_parent("table")
        table_classes = (
            set(table.get_attribute_list("class")) if isinstance(table, Tag) else set()
        )
        if not table_classes & {"sidebar", "cm-sidebar"}:
            return

        for cell in ele.find_all(_TD_OR_TH):
            cell_classes = set(cell.get_attribute_list("class"))
            if "sidebar-title-with-pretitle" in cell_classes:
                # _merge_header_rows already wrapped the title link in <big>;
                # bold only that <big>, leaving "Part of a series on" + <br/> outside.
                big = cell.find("big")
                if isinstance(big, Tag):
                    bold = soup.new_tag("b")
                    big.insert_after(bold)
                    bold.append(big.extract())
            elif "sidebar-heading" in cell_classes:
                for li in cell.find_all("li"):
                    cls._wrap_children(li, soup, "b")
            elif "sidebar-below" in cell_classes:
                for li in cell.find_all("li"):
                    cls._wrap_children(li, soup, "b")

        # Section labels (Branches, Fundamentals, …) live in <div> elements
        # nested inside <td class="sidebar-content">, not in <th>/<td> cells.
        for title_div in ele.find_all("div", class_="sidebar-list-title-c"):
            cls._wrap_children(title_div, soup, "b")

        if isinstance(table, Tag):
            for caption in table.find_all("div", class_="sidebar-caption"):
                cls._wrap_children(caption, soup, "i")

    @staticmethod
    def _wrap_children(target: Tag, soup: Tag, tag_name: str) -> None:
        """Move all children of ``target`` into a new ``<tag_name>`` wrapper."""
        children = list(target.children)
        wrapper = soup.new_tag(tag_name)
        for child in children:
            wrapper.append(child.extract())
        target.append(wrapper)

    @classmethod
    def _insert_mixed_alignment_rows(cls, ele: Tag, soup: Tag) -> None:
        """Insert alignment marker rows for mixed ``<th>``/``<td>`` tables."""
        for tr in ele.find_all("tr", recursive=False):
            cells = [
                c for c in tr.children if isinstance(c, Tag) and c.name in _TD_OR_TH
            ]
            if not cells:
                continue
            if not any(c.name == "th" for c in cells):
                continue

            # All-<th> rows are handled by suffix in _handle_tr.
            # Stop here: subsequent mixed rows should NOT get alignment
            # markers to avoid polluting tables with multiple separator
            # sections (e.g. navboxes, authority-control tables).
            if all(c.name == "th" for c in cells):
                break

            # Mixed row: compute alignments from content cells (majority
            # rule), then override with explicit <th> alignment only for
            # columns that have zero <td> cells.
            table_ele = tr.find_parent("table")
            alignments, cols_with_data = (
                cls._td_cell_alignments(table_ele) if table_ele else ([], set())
            )
            for i, c in enumerate(cells):
                if isinstance(c, Tag) and c.name == "th":
                    header_align = cls._cell_alignment(c)
                    if header_align != "---" and i not in cols_with_data:
                        while len(alignments) <= i:
                            alignments.append("---")
                        alignments[i] = header_align
            # Ensure at least as many alignments as cells.
            while len(alignments) < len(cells):
                alignments.append("---")
            # Right-align the scope=row label column, mirroring the
            # all-<th> header path in _handle_tr.
            has_scope_row = (
                table_ele is not None and table_ele.find("th", scope="row") is not None
            )
            if has_scope_row and alignments:
                alignments[0] = "--:"
            marker_tag = soup.new_tag("tr", attrs={"data-alignment-row": "true"})
            for a in alignments:
                td = soup.new_tag("td", attrs={"data-align": a})
                marker_tag.append(td)

            # Case 2: a leading caption row (marked with data-caption-row)
            # precedes the header row → insert the alignment marker
            # immediately AFTER the title caption row.  Infoboxes emit a
            # title caption row (data-caption-title) followed by an optional
            # image/caption row; the separator must sit between the title
            # and the following caption/header row, not after the whole
            # caption run.
            prev_tr = tr.find_previous_sibling("tr")
            if prev_tr is not None and prev_tr.get("data-caption-row") == "true":
                title_tr = prev_tr
                while (
                    prev_caption := title_tr.find_previous_sibling("tr")
                ) is not None and prev_caption.get("data-caption-row") == "true":
                    title_tr = prev_caption
                title_tr.insert_after(marker_tag)
                # Only process the first mixed row; subsequent rows are not
                # alignment-related and should not get markers.
                break

            # Case 2.5: single-row mixed table (no all-<th> header row, no
            # caption) — synthesize an empty all-<td> header row so the
            # label/value row renders as a data row and the marker has a
            # row to follow. All-<td> (not <th>) avoids the all-<th>
            # alignment suffix in _handle_tr.
            cell_rows = [
                row
                for row in cls._table_rows(table_ele)
                if row.get("data-caption-row") != "true"
                and any(
                    isinstance(c, Tag) and c.name in _TD_OR_TH for c in row.children
                )
            ]
            if len(cell_rows) == 1:
                header_row = soup.new_tag("tr")
                for _ in cells:
                    header_row.append(soup.new_tag("td"))
                tr.insert_before(header_row)
                tr.insert_before(marker_tag)
                break

            # Case 3: no caption → insert AFTER header row.
            tr.insert_after(marker_tag)
            # Only process the first mixed row; subsequent rows are not
            # alignment-related and should not get markers.
            break

    @classmethod
    def _flatten_nested_tables(cls, tbody: Tag, soup: Tag) -> None:
        """Replace nested ``<table>`` elements inside ``<td>``/``<th>`` with flat inline HTML.

        Unlike a plain ``get_text()`` call, this preserves child elements
        (``<a>``, ``<b>``, ``<sup>``, etc.) so that links and formatting
        survive the flattening.
        """
        for cell in tbody.find_all(_TD_OR_TH):
            # Process in reverse so inner tables are flattened before outer ones.
            for nested_table in reversed(list(cell.find_all("table"))):
                nodes: list[PageElement] = []
                for i, tr in enumerate(cls._table_rows(nested_table)):
                    if i > 0:
                        nodes.append(soup.new_tag("br"))
                        nodes.append(soup.new_tag("br"))
                    sub_cells = tr.find_all(_TD_OR_TH, recursive=False)
                    for j, sub_cell in enumerate(sub_cells):
                        if j > 0:
                            nodes.append(soup.new_tag("br"))
                        # Wrap <th> children in <b> to preserve navbox-group bold.
                        if sub_cell.name == "th":
                            b_tag = soup.new_tag("b")
                            for child in list(sub_cell.children):
                                b_tag.append(child)
                            nodes.append(b_tag)
                        # Wrap CSS-bold <td> children in <b> to preserve bold.
                        elif sub_cell.name == "td" and _BOLD_FONT_STYLE_REGEX.search(
                            str(sub_cell.get("style", ""))
                        ):
                            b_tag = soup.new_tag("b")
                            for child in list(sub_cell.children):
                                b_tag.append(child)
                            nodes.append(b_tag)
                        else:
                            for child in list(sub_cell.children):
                                nodes.append(child)
                for node in nodes:
                    nested_table.insert_before(node)
                nested_table.extract()

    # -- Static helpers --

    @staticmethod
    def _cell_alignment(cell: Tag) -> str:
        """Derive a GFM alignment marker from a table cell's ``text-align`` style.

        Returns one of:

        - ``"---"`` — no ``text-align`` style found (renderer default,
          typically left).  This is *not* the same as explicit
          left-alignment.
        - ``":--"`` — explicit ``text-align: left``.
        - ``"--:"`` — explicit ``text-align: right``.
        - ``"-:-"`` — explicit ``text-align: center``.
        """
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
    def _table_rows(table: Tag | None) -> list[Tag]:
        """Collect all ``<tr>`` rows in *table*, direct or inside containers.

        Looks at direct ``<tr>`` children first; if there are none, extends
        from ``<tbody>``/``<thead>``/``<tfoot>`` containers.
        """
        if table is None:
            return []
        rows: list[Tag] = table.find_all("tr", recursive=False)
        if not rows:
            for container in table.find_all(
                ("tbody", "thead", "tfoot"), recursive=False
            ):
                rows.extend(container.find_all("tr", recursive=False))
        return rows

    @classmethod
    def _td_cell_alignments(cls, table: Tag) -> tuple[list[str], set[int]]:
        """Compute per-column GFM alignment markers from ``<td>`` cells.

        Scans all ``<tr>`` rows in *table*, collects every ``<td>`` cell,
        and for each column determines the majority alignment via
        ``_cell_alignment``.  Ties default to ``"---"`` (no explicit
        alignment).

        Returns ``(markers, cols_with_data)`` where *markers* has one
        element per column and *cols_with_data* is the set of column
        indices that contained at least one ``<td>`` cell.  Returns
        ``([], set())`` if the table has no ``<td>`` cells.
        """
        col_counts: list[dict[str, int]] = []
        cols_with_data: set[int] = set()

        # Collect alignment counts per column from all <td> cells.
        rows = cls._table_rows(table)
        for tr in rows:
            if tr.get("data-caption-row") == "true":
                continue
            col_idx = 0
            for child in tr.children:
                if not isinstance(child, Tag) or child.name not in _TD_OR_TH:
                    continue
                if child.name == "td":
                    if child.get("data-filler-cell") == "true":
                        col_idx += 1
                        continue
                    cols_with_data.add(col_idx)
                    marker = cls._cell_alignment(child)
                    while len(col_counts) <= col_idx:
                        col_counts.append({})
                    col_counts[col_idx][marker] = col_counts[col_idx].get(marker, 0) + 1
                col_idx += 1

        if not col_counts:
            return [], set()

        # Majority rule per column.
        result: list[str] = []
        for counts in col_counts:
            if not counts:
                result.append("---")
                continue
            majority = max(counts, key=lambda m: (counts[m], m))
            result.append(majority)
        return result, cols_with_data

    @staticmethod
    def _filter_table_cells(
        strings: str,
        *,
        total_colspan: int,
    ) -> str:
        """Filter, pad, and clean table cell strings for ``_handle_tr``.

        Splits the joined cell string on ``" | "``, pads to
        *total_colspan* by appending empty cells, and re-joins.  Empty
        cells are preserved so that column positions match the original
        HTML structure.

        .. note::

           If a cell contains the literal separator ``" | "`` (e.g. in
           inline code or math), the split creates a spurious extra
           cell.  This is a pre-existing limitation inherited from the
           pipe-table format; keep cell content free of bare ``" | "``
           substrings.
        """
        cells = [s.strip() for s in strings.split(" | ")]
        while len(cells) < total_colspan:
            cells.append("")
        result = " | ".join(cells)
        return result

    @staticmethod
    def process_table_cell(strings: str) -> str:
        """Process content of a table cell.

        Strips whitespace, collapses newlines, replaces leading
        whitespace with non-breaking spaces, normalizes pipe characters,
        and converts remaining newlines to ``<br/>`` tags.
        """
        leading_break = strings.startswith("\n")
        strings = strings.strip()
        strings = _CONSECUTIVE_NEWLINES_REGEX.sub("\n\n", strings)
        strings = _CONSECUTIVE_LEADING_WHITESPACES_REGEX.sub(
            lambda match: match[0].replace(" ", "&nbsp;").replace("\t", "&emsp;"),
            strings,
        )
        strings = strings.replace("\xa0", " ")
        strings = strings.replace("| |", "|")
        strings = strings.replace("| __", "|__").replace("__ |", "__ <p> ")
        strings = strings.replace("|\n|", " <p> ")
        # Remove leading and trailing ``|`` per line to prevent confusion
        # with pipe table delimiters.
        lines = strings.split("\n")
        for i, line in enumerate(lines):
            sline = line.lstrip()
            if sline.startswith("|"):
                lines[i] = line[: len(line) - len(sline)] + sline[1:]
        strings = "\n".join(lines)
        lines = strings.split("\n")
        for i, line in enumerate(lines):
            rline = line.rstrip()
            if rline.endswith("|"):
                lines[i] = rline[:-1] + line[len(rline) :]
        strings = "\n".join(lines)
        strings = _replace_pipes_outside_math(strings)
        strings = strings.strip()
        strings = strings.replace("\n\n", " <br/> <br/> ")
        strings = strings.replace("\n", " <br/> ")
        strings = strings.strip()
        if leading_break:
            strings = f" <br/> {strings}" if strings else "<br/>"
        return strings


"""Exported names from this module."""
__all__ = ()
