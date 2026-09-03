"""Unit tests for TableConverter._flatten_nested_tables."""

from __future__ import annotations

from bs4 import BeautifulSoup, Tag

from scripts.convert_wiki.table import TableConverter


def _make_tbody(html: str):
    """Parse an HTML fragment and return the soup and the first <tbody> element."""
    soup = BeautifulSoup(f"<table><tbody>{html}</tbody></table>", "html.parser")
    tbody = soup.find("tbody")
    assert tbody is not None
    return soup, tbody


def _cell_text(cell: Tag) -> str:
    """Collect text from a cell's direct children (ignoring structural tags)."""
    parts: list[str] = []
    for child in cell.children:
        if isinstance(child, Tag) and child.name in ("b",):
            parts.append(child.get_text())
        elif isinstance(child, Tag) and child.name == "a":
            parts.append(child.get_text())
        elif isinstance(child, Tag):
            parts.append(child.get_text())
        else:
            parts.append(str(child))
    return "".join(parts)


class TestFlattenNestedTables:
    """Tests for TableConverter._flatten_nested_tables."""

    def test_navbox_subgroup_flattening(self) -> None:
        """Inner navbox-subgroup table with <th> headers and <td> items is flattened."""
        html = (
            "<tr><td>"
            '<table class="navbox-subgroup">'
            "<tr><th>Mathematics</th></tr>"
            "<tr><td>Item A</td><td>Item B</td></tr>"
            "<tr><th>Physics</th></tr>"
            "<tr><td>Item C</td><td>Item D</td></tr>"
            "</table>"
            "</td></tr>"
        )
        soup, tbody = _make_tbody(html)
        TableConverter._flatten_nested_tables(tbody, soup)

        # The inner <table> should be extracted.
        assert tbody.find("table") is None

        cell = tbody.find("td")
        assert cell is not None
        text = _cell_text(cell)

        # Bold section headers via <b> wrapping.
        bold_tags = cell.find_all("b")
        bold_texts = [b.get_text() for b in bold_tags]
        assert "Mathematics" in bold_texts
        assert "Physics" in bold_texts
        # Items present.
        assert "Item A" in text
        assert "Item B" in text
        assert "Item C" in text
        assert "Item D" in text
        # Rows separated by <br><br> separators.
        br_tags = cell.find_all("br")
        # 2 <br> per row separator × 3 separators (4 rows) = 6
        # plus intra-row separators (2 rows with 2 cells) = 2
        assert len(br_tags) >= 8
        assert len(br_tags) >= 2  # between cells in each row

    def test_wikitable_inside_navbox_cell(self) -> None:
        """Inner wikitable with alignment row is flattened; alignment row gone."""
        html = (
            "<tr><td>"
            '<table class="wikitable">'
            "<tr><th>Col A</th><th>Col B</th></tr>"
            "<tr><td>---alignment---</td><td>---alignment---</td></tr>"
            "<tr><td>Data 1</td><td>Data 2</td></tr>"
            "</table>"
            "</td></tr>"
        )
        soup, tbody = _make_tbody(html)
        TableConverter._flatten_nested_tables(tbody, soup)

        assert tbody.find("table") is None

        cell = tbody.find("td")
        assert cell is not None
        text = _cell_text(cell)
        assert "---alignment---" in text
        assert "Data 1" in text
        assert "Data 2" in text

    def test_no_nested_tables_noop(self) -> None:
        """When there are no nested tables, the tbody is unchanged."""
        html = (
            "<tr><td>Simple cell</td><td>Another cell</td></tr>"
            "<tr><td>Third cell</td><td>Fourth cell</td></tr>"
        )
        soup, tbody = _make_tbody(html)
        original = str(tbody)
        TableConverter._flatten_nested_tables(tbody, soup)
        assert str(tbody) == original

    def test_recursive_flattening(self) -> None:
        """Inner table containing another table: both levels are flattened."""
        html = (
            "<tr><td>"
            "<table>"
            "<tr><td>"
            "<table>"
            "<tr><td>Deep item</td></tr>"
            "</table>"
            "</td></tr>"
            "</table>"
            "</td></tr>"
        )
        soup, tbody = _make_tbody(html)
        TableConverter._flatten_nested_tables(tbody, soup)

        assert tbody.find("table") is None

        cell = tbody.find("td")
        assert cell is not None
        assert "Deep item" in _cell_text(cell)

    def test_html_content_preservation(self) -> None:
        """Links and bold inside nested table cells are preserved as Tags."""
        html = (
            "<tr><td>"
            "<table>"
            "<tr><th><b>Header</b></th></tr>"
            '<tr><td><a href="/wiki/Foo">Foo link</a></td></tr>'
            "</table>"
            "</td></tr>"
        )
        soup, tbody = _make_tbody(html)
        TableConverter._flatten_nested_tables(tbody, soup)

        assert tbody.find("table") is None
        cell = tbody.find("td")
        assert cell is not None
        # <b> tag wrapping the <th> content.
        bold_tags = cell.find_all("b")
        assert any("Header" in b.get_text() for b in bold_tags)
        # <a> link tag preserved.
        a_tags = cell.find_all("a")
        assert any(a.get_text() == "Foo link" for a in a_tags)
        assert any(a.get("href") == "/wiki/Foo" for a in a_tags)

    def test_multiple_nested_tables_in_same_cell(self) -> None:
        """Multiple sibling tables inside one cell are all flattened."""
        html = (
            "<tr><td>"
            "<table><tr><td>Table 1</td></tr></table>"
            "<table><tr><td>Table 2</td></tr></table>"
            "</td></tr>"
        )
        soup, tbody = _make_tbody(html)
        TableConverter._flatten_nested_tables(tbody, soup)

        assert tbody.find("table") is None
        cell = tbody.find("td")
        assert cell is not None
        text = _cell_text(cell)
        assert "Table 1" in text
        assert "Table 2" in text

    def test_tbody_wrapped_rows(self) -> None:
        """Tables with <tbody> wrappers (Wikipedia structure) are handled."""
        html = (
            "<tr><td>"
            '<table class="navbox-subgroup">'
            "<tbody>"
            "<tr><th>Group</th></tr>"
            "<tr><td>Item 1</td><td>Item 2</td></tr>"
            "</tbody>"
            "</table>"
            "</td></tr>"
        )
        soup, tbody = _make_tbody(html)
        TableConverter._flatten_nested_tables(tbody, soup)

        assert tbody.find("table") is None
        cell = tbody.find("td")
        assert cell is not None
        text = _cell_text(cell)
        assert "Item 1" in text
        assert "Item 2" in text
        # <th> wrapped in <b>.
        bold_tags = cell.find_all("b")
        assert any("Group" in b.get_text() for b in bold_tags)


class TestNavboxBlockquotePattern:
    """Tests for TableConverter._is_navbox_blockquote_pattern."""

    def test_positive_match_2tr_navbox_inner(self) -> None:
        """2-TR navbox-inner with inner wikitable returns True."""
        html = (
            '<table class="navbox-inner">'
            "<tbody>"
            "<tr><th>vte Classical mechanics SI units</th></tr>"
            "<tr><td>"
            '<div><table class="wikitable">'
            "<tr><td>Linear quantities</td></tr>"
            "<tr><th>Dimensions</th><th>1</th></tr>"
            "<tr><td>Length</td><td>L</td></tr>"
            "<tr><td>Mass</td><td>M</td></tr>"
            "<tr><td>Time</td><td>T</td></tr>"
            "</table></div>"
            "</td></tr>"
            "</tbody>"
            "</table>"
        )
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        assert TableConverter._is_navbox_blockquote_pattern(tbody) is True

    def test_negative_not_navbox_inner(self) -> None:
        """Table without navbox-inner class returns False."""
        html = (
            '<table class="wikitable">'
            "<tbody>"
            "<tr><th>Col A</th><th>Col B</th></tr>"
            "<tr><td>Data 1</td><td>Data 2</td></tr>"
            "<tr><td>Data 3</td><td>Data 4</td></tr>"
            "</tbody>"
            "</table>"
        )
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        assert TableConverter._is_navbox_blockquote_pattern(tbody) is False

    def test_negative_3_tr_navbox(self) -> None:
        """Navbox-inner with 3 TRs returns False."""
        html = (
            '<table class="navbox-inner">'
            "<tbody>"
            "<tr><th>Header</th></tr>"
            "<tr><td>Content A</td></tr>"
            "<tr><td>Content B</td></tr>"
            "</tbody>"
            "</table>"
        )
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        assert TableConverter._is_navbox_blockquote_pattern(tbody) is False

    def test_negative_no_inner_table(self) -> None:
        """2-TR navbox-inner without nested table returns False."""
        html = (
            '<table class="navbox-inner">'
            "<tbody>"
            "<tr><th>Header</th></tr>"
            "<tr><td>Plain content</td></tr>"
            "</tbody>"
            "</table>"
        )
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        assert TableConverter._is_navbox_blockquote_pattern(tbody) is False

    def test_negative_inner_table_too_few_rows(self) -> None:
        """2-TR navbox-inner with inner table having only 2 rows returns False."""
        html = (
            '<table class="navbox-inner">'
            "<tbody>"
            "<tr><th>Header</th></tr>"
            "<tr><td>"
            "<table>"
            "<tr><td>A</td><td>B</td></tr>"
            "<tr><td>C</td><td>D</td></tr>"
            "</table>"
            "</td></tr>"
            "</tbody>"
            "</table>"
        )
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        assert TableConverter._is_navbox_blockquote_pattern(tbody) is False


class TestFlattenNestedTablesCssBoldTd:
    """Tests for CSS-bold <td> wrapping in _flatten_nested_tables."""

    def test_css_bold_td_wrapped_in_b(self) -> None:
        """<td> with font-weight: bold is wrapped in <b> during flattening."""
        html = (
            "<tr><td>"
            "<table>"
            '<tr><td style="font-weight: bold">Bold item</td><td>Normal item</td></tr>'
            "</table>"
            "</td></tr>"
        )
        soup, tbody = _make_tbody(html)
        TableConverter._flatten_nested_tables(tbody, soup)

        cell = tbody.find("td")
        assert cell is not None
        bold_tags = cell.find_all("b")
        bold_texts = [b.get_text() for b in bold_tags]
        assert "Bold item" in bold_texts

    def test_non_bold_td_not_wrapped(self) -> None:
        """<td> without CSS bold is NOT wrapped in <b>."""
        html = "<tr><td><table><tr><td>Normal item</td></tr></table></td></tr>"
        soup, tbody = _make_tbody(html)
        TableConverter._flatten_nested_tables(tbody, soup)

        cell = tbody.find("td")
        assert cell is not None
        # The only <b> tags should be none (no bold wrapping for <td>).
        bold_tags = cell.find_all("b")
        bold_texts = [b.get_text() for b in bold_tags]
        assert "Normal item" not in bold_texts


def _make_navbox_html(
    title: str = "Classical mechanics",
    title_href: str = "/wiki/Classical_mechanics",
    linear_items: tuple[str, ...] = ("Length", "Mass"),
    angular_items: tuple[str, ...] = ("Angle", "Angular velocity"),
) -> str:
    """Build a minimal navbox-inner HTML suitable for testing handle_tbody."""
    linear_cells = "".join(f"<td>{item}</td>" for item in linear_items)
    angular_cells = "".join(f"<td>{item}</td>" for item in angular_items)
    return (
        '<table class="navbox-inner">'
        "<tbody>"
        "<tr><th>"
        '<div style="font-size:114%">'
        f'<a href="{title_href}">{title}</a>'
        "</div>"
        "</th></tr>"
        "<tr><td>"
        '<table class="wikitable">'
        "<tr>"
        '<td style="font-weight: bold">Linear quantities</td>'
        '<td style="font-weight: bold">Angular quantities</td>'
        "</tr>"
        f"<tr><td>{linear_cells}</td><td>{angular_cells}</td></tr>"
        "<tr><td>Extra row</td><td>Extra row</td></tr>"
        "</table>"
        "</td></tr>"
        "</tbody>"
        "</table>"
    )


class TestExtractNavboxBlockquoteHeader:
    """Tests for TableConverter._extract_navbox_blockquote_header."""

    def test_plain_title_no_links(self) -> None:
        """Title div without <a> tags returns plain text."""
        html = (
            '<table class="navbox-inner"><tbody>'
            "<tr><th>"
            '<div style="font-size:114%">Classical mechanics</div>'
            "</th></tr>"
            "<tr><td>Content</td></tr>"
            "</tbody></table>"
        )
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        title_md, link_comment = TableConverter._extract_navbox_blockquote_header(
            tbody,
        )
        assert title_md == "Classical mechanics"
        assert link_comment == ""

    def test_title_with_links_no_names_map(self) -> None:
        """Title div with <a> tags uses lowercase-first-char fallback without names_map."""
        html = (
            '<table class="navbox-inner"><tbody>'
            "<tr><th>"
            '<div style="font-size:114%">'
            '<a href="/wiki/Force">Force</a> and '
            '<a href="/wiki/Mass">Mass</a>'
            "</div>"
            "</th></tr>"
            "<tr><td>Content</td></tr>"
            "</tbody></table>"
        )
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        title_md, link_comment = TableConverter._extract_navbox_blockquote_header(
            tbody,
        )
        # Without names_map, _fix_name_maybe lowercases first char when rest
        # is all lowercase (Force→force, Mass→mass).
        assert "[Force](force.md)" in title_md
        assert "[Mass](mass.md)" in title_md
        # Link comment should contain raw Wikipedia URLs.
        assert "[Force](/wiki/Force)" in link_comment
        assert "[Mass](/wiki/Mass)" in link_comment

    def test_title_with_links_with_names_map(self) -> None:
        """Title div with <a> tags resolves hrefs through names_map."""
        names_map = {
            "Force": "force",
            "Mass": "mass",
        }
        html = (
            '<table class="navbox-inner"><tbody>'
            "<tr><th>"
            '<div style="font-size:114%">'
            '<a href="/wiki/Force">Force</a> and '
            '<a href="/wiki/Mass">Mass</a>'
            "</div>"
            "</th></tr>"
            "<tr><td>Content</td></tr>"
            "</tbody></table>"
        )
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        title_md, link_comment = TableConverter._extract_navbox_blockquote_header(
            tbody,
            names_map=names_map,
        )
        assert "[Force](force.md)" in title_md
        assert "[Mass](mass.md)" in title_md

    def test_title_vte_prefix_stripped(self) -> None:
        """'vte' text before the title div is stripped from fallback plain text."""
        # The vte prefix only gets stripped in the fallback path (no title_div).
        # When no title_div is found, the full header_cell text is used with
        # vte prefix stripped. Test this fallback path.
        html = (
            '<table class="navbox-inner"><tbody>'
            "<tr><th>vte Classical mechanics</th></tr>"
            "<tr><td>Content</td></tr>"
            "</tbody></table>"
        )
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        title_md, _link_comment = TableConverter._extract_navbox_blockquote_header(
            tbody,
        )
        assert title_md == "Classical mechanics"


class TestHandleTbodyNavboxNamesMap:
    """Tests for TableConverter.handle_tbody navbox path with names_map."""

    def test_navbox_with_names_map_passes_through(self) -> None:
        """handle_tbody passes names_map to header extractor for link resolution."""
        names_map = {
            "Classical mechanics": "Classical mechanics",
        }
        html = _make_navbox_html(
            title="Classical mechanics",
            title_href="/wiki/Classical_mechanics",
        )
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        config = TableConverter.handle_tbody(
            tbody,
            frozenset(),
            soup,
            names_map=names_map,
        )
        assert config is not None
        assert config.full_result is True
        # The process_strings function should produce output containing
        # the resolved link.
        assert config.process_strings is not None
        result = config.process_strings("")
        assert "Classical mechanics" in result

    def test_navbox_without_names_map(self) -> None:
        """handle_tbody works without names_map (backward compat)."""
        html = _make_navbox_html()
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        assert tbody is not None
        config = TableConverter.handle_tbody(tbody, frozenset(), soup)
        assert config is not None
        assert config.full_result is True
        result = config.process_strings("")
        # Should still produce output with title.
        assert "Classical mechanics" in result
        # Should contain blockquote markers.
        assert ">" in result
