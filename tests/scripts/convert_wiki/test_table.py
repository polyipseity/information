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
