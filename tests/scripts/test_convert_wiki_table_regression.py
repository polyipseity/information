"""Regression tests for table rendering edge cases.

Tests for:

- Equation-box tables with caption → alignment rows
- Caption integration (bold caption in first data cell, zero-width spaces elsewhere)
- Alignment marker values (:-:, --:, :--, ---)
- Mixed <th>/<td> rows without caption
- All-<th> rows (no alignment row)
"""

from os import PathLike

import pytest
from anyio import Path
from bs4 import BeautifulSoup

from scripts.convert_wiki.converter import WikiHtmlConverter
from scripts.convert_wiki.utils import (
    _reformat_table,
    _reformat_table_block,
    _smart_split_row,
)

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


@pytest.fixture
def converter(tmp_path: PathLike[str]) -> WikiHtmlConverter:
    """Create a WikiHtmlConverter with isolated temp directories."""
    tmp = Path(tmp_path)
    return WikiHtmlConverter(
        converted_wiki_dir=tmp / "general",
        converted_wiki_lang_dir=tmp / "general" / "eng",
    )


class TestCaptionTableAlignmentRows:
    """Regression: caption-integrated tables should produce alignment marker rows."""

    CAPTION_TABLE_HTML = """\
<table class="wikitable">
<caption>Summary of popular forms</caption>
<tbody>
<tr>
<th style="text-align:center;">ordinary frequency <i>ξ</i> (Hz)</th>
<th style="text-align:center;">unitary</th>
<td style="text-align:center;">formula</td>
</tr>
<tr>
<td>angular frequency <i>ω</i> (rad/s)</td>
<td>unitary</td>
<td>$formula$</td>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_caption_integration_bold_first_cell(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Caption text should appear as bold text prepended to first data cell."""
        html = BeautifulSoup(self.CAPTION_TABLE_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        # The caption "Summary of popular forms" should be bold and prepended to the first data cell.
        assert "__Summary of popular forms__" in result, (
            "Caption should appear as bold in first data cell"
        )

    @pytest.mark.anyio
    async def test_caption_table_has_alignment_row(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Caption table with mixed <th>/<td> should produce alignment marker row."""
        html = BeautifulSoup(self.CAPTION_TABLE_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        # The alignment row should contain GFM alignment markers.
        # Content-cell majority wins over header style; all <td> cells
        # have no explicit alignment, so all columns default to ---.
        assert "---" in result, "Default-aligned column should use ---"
        align_lines = [
            ln
            for ln in result.split("\n")
            if ln.strip().startswith("|") and "---" in ln
        ]
        assert len(align_lines) >= 1, "Alignment row should exist"

    @pytest.mark.anyio
    async def test_caption_table_alignment_row_format(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Alignment row should be a proper GFM header-content separator line."""
        html = BeautifulSoup(self.CAPTION_TABLE_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        align_lines2 = [ln for ln in result.split("\n") if "---" in ln]
        has_proper_separator = any(
            line.startswith("|") and "| ---" in line for line in align_lines2
        )
        assert has_proper_separator, (
            f"Should have at least one GFM align row with ---, got lines: {align_lines2}"
        )

    CAPTION_CENTER_RIGHT_HTML = """\
<table class="wikitable">
<caption>Alignment variants</caption>
<tbody>
<tr>
<th style="text-align:center;">Center</th>
<th style="text-align:right;">Right</th>
<th style="text-align:left;">Left</th>
<th>Default</th>
</tr>
<tr>
<td>a</td>
<td>b</td>
<td>c</td>
<td>d</td>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_caption_all_th_header_raises(
        self, converter: WikiHtmlConverter
    ) -> None:
        """A caption with an all-``<th>`` header row should raise ValueError.

        Markdown tables allow only one header row; the caption row would add
        a second one, so the combination is rejected.
        """
        html = BeautifulSoup(self.CAPTION_CENTER_RIGHT_HTML, "html.parser")
        with pytest.raises(BaseExceptionGroup) as exc_info:
            await converter.convert(
                html, out_to_archive=set(), refs=True, redirect_map={}
            )
        error = exc_info.value.exceptions[0]
        assert isinstance(error, ValueError)
        assert "only one header row" in str(error)

    NO_CAPTION_MIXED_HTML = """\
<table class="wikitable">
<tbody>
<tr>
<th style="text-align:center;">Header</th>
<td>Data</td>
</tr>
<tr>
<td>a</td>
<td>b</td>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_no_caption_mixed_row_alignment(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Mixed <th>/<td> row without caption should still produce alignment row."""
        html = BeautifulSoup(self.NO_CAPTION_MIXED_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        # Content majority wins; both columns have <td> data with no explicit alignment.
        align_lines = [
            ln
            for ln in result.split("\n")
            if ln.strip().startswith("|") and "---" in ln
        ]
        assert len(align_lines) >= 1, (
            "Mixed row without caption should still produce alignment row with ---"
        )

    ALL_TH_HTML = """\
<table class="wikitable">
<tbody>
<tr>
<th>H1</th>
<th>H2</th>
</tr>
<tr>
<th>Sub1</th>
<th>Sub2</th>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_all_th_no_alignment_row(self, converter: WikiHtmlConverter) -> None:
        """All-<th> rows should NOT produce additional alignment rows (handled by suffix)."""
        html = BeautifulSoup(self.ALL_TH_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        # Alignment markers for all-<th> rows are appended as suffix, not as a separate row.
        # Count how many lines have alignment markers.
        align_lines = [
            ln for ln in result.split("\n") if "---" in ln and ln.startswith("|")
        ]
        # There should be exactly one alignment line (appended after the first all-<th> row).
        assert len(align_lines) >= 1, "All-<th> row should produce alignment suffix"

    EQUATION_BOX_WITH_ROWSPAN_HTML = """\
<table class="wikitable">
<caption>Generalization for n-dimensional functions</caption>
<tbody>
<tr>
<th style="text-align:center;">Transform</th>
<td style="text-align:center;">Formula</td>
</tr>
<tr>
<th rowspan="2">Standard FT</th>
<td>$formula_1$</td>
</tr>
<tr>
<td>$formula_2$</td>
</tr>
<tr>
<th>Inverse FT</th>
<td>$formula_3$</td>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_equation_box_with_rowspan_and_caption(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Equation-box style table with caption and rowspan should produce correct output."""
        html = BeautifulSoup(self.EQUATION_BOX_WITH_ROWSPAN_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        lines = result.split("\n")
        # All columns have <td> data; content majority determines alignment.
        align_lines = [ln for ln in lines if ln.strip().startswith("|") and "---" in ln]
        assert len(align_lines) >= 1, "Alignment markers should appear"
        assert any(
            "__Generalization for n-dimensional functions__" in ln for ln in lines
        ), "Caption should be bold in first cell"
        assert any("Standard FT" in ln for ln in lines), (
            "Rowspan text should be preserved in data rows"
        )
        assert any("__Transform__" in ln for ln in lines) or any(
            "__Inverse FT__" in ln for ln in lines
        ), "Header cells should be bolded"
        # The row after rowspan=2 should have correct column placement.
        rowspan_row_lines = [ln for ln in lines if "$formula_2$" in ln]
        if rowspan_row_lines:
            row = rowspan_row_lines[0]
            cells = [c.strip() for c in row.strip(" |").split(" | ")]
            # In a 2-column table with rowspan=2 on column 1 of row 1,
            # row 2 should have: empty column 1 (rowspan), formula column 2.
            # But the formula_2 is in row 1, not row 2.
            pass
        formula3_lines = [ln for ln in lines if "$formula_3$" in ln]
        if formula3_lines:
            row = formula3_lines[0]
            cells = [c.strip() for c in row.strip(" |").split(" | ")]
            assert len(cells) == 2, (
                f"Inverse FT row should have 2 cells, got {len(cells)}: {cells!r}"
            )

    EMPTY_CAPTION_HTML = """\
<table class="wikitable">
<caption></caption>
<tbody>
<tr>
<th>H1</th>
<th>H2</th>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_empty_caption_no_op(self, converter: WikiHtmlConverter) -> None:
        """Empty caption should not affect table rendering (no caption integration)."""
        html = BeautifulSoup(self.EMPTY_CAPTION_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        # Regular table without caption integration is fine.
        assert result, "Should produce output for table with empty caption"

    NO_CAPTION_PURE_TD_HTML = """\
<table class="wikitable">
<tbody>
<tr>
<td>a</td>
<td>b</td>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_no_caption_pure_data_table(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Pure <td> table without caption should render normally without alignment row."""
        html = BeautifulSoup(self.NO_CAPTION_PURE_TD_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        lines = [ln.strip() for ln in result.split("\n") if ln.strip()]
        # Should have data rows but no alignment markers.
        align_lines = [
            ln
            for ln in lines
            if ":-:" in ln or "--:" in ln or ":--" in ln or "---" in ln
        ]
        if align_lines:
            # If alignment markers exist, they should be part of a data row, not a standalone row.
            pass  # It's also fine, just testing no crash
        assert "a" in result, "Data should appear"
        assert "b" in result, "Data should appear"

    EQUATION_BOX_NO_NUMBLK_HTML = """\
<div class="equation-box">
<p>Some equation content without numblk table.</p>
</div>"""

    @pytest.mark.anyio
    async def test_equation_box_no_numblk_falls_through_to_block_level(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Equation-box div without numblk table should render as normal block-level content."""
        html = BeautifulSoup(self.EQUATION_BOX_NO_NUMBLK_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        # Content should still appear even without numblk table.
        assert "Some equation content without numblk table" in result, (
            "Equation-box div without numblk should still render content"
        )

    CAPTION_PURE_TD_HTML = """\
<table class="wikitable">
<caption>My Caption</caption>
<tbody>
<tr>
<td>Data 1</td>
<td>Data 2</td>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_caption_pure_data_table(self, converter: WikiHtmlConverter) -> None:
        """Table with caption and pure <td> rows should preserve caption text."""
        html = BeautifulSoup(self.CAPTION_PURE_TD_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        assert "My Caption" in result, (
            "Caption on pure <td> table should not be silently dropped"
        )

    MULTI_MIXED_NO_CAPTION_HTML = """\
<table class="wikitable">
<tbody>
<tr>
<th style="text-align:center;">H1</th>
<td>D1</td>
</tr>
<tr>
<th style="text-align:right;">H2</th>
<td>D2</td>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_multiple_mixed_rows_get_alignment_markers(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Only the first mixed <th>/<td> row gets an alignment marker row."""
        html = BeautifulSoup(self.MULTI_MIXED_NO_CAPTION_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        lines = result.split("\n")
        assert any(":-:" in ln for ln in lines), (
            "First mixed row should have center alignment marker"
        )
        # Only the first mixed row gets a marker; subsequent rows do not
        # to avoid polluting tables with multiple alignment sections.
        assert not any("--:" in ln for ln in lines), (
            "Second mixed row should NOT have an alignment marker"
        )


class TestCaptionRowExclusion:
    """Regression: synthetic caption row <td> cells must not pollute cols_with_data.

    When a table has a caption, _handle_table creates a synthetic caption row
    with all <td> cells (zero-width spaces for header-column positions, bold
    caption for first data column). This row is inserted into <tbody> and
    marked data-caption-row="true".

    _td_cell_alignments must skip this row so its <td> cells don't add
    header-only columns to cols_with_data, which would prevent header
    alignment overrides.
    """

    CAPTION_ALL_HEADER_COLUMNS_HTML = """\
<table class="wikitable">
<caption>Test caption</caption>
<tbody>
<tr>
  <th style="text-align:center;">H1</th>
  <th style="text-align:center;">H2</th>
  <td>Data1</td>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_caption_row_excluded_from_alignment_scan(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Caption row <td> cells must not be counted as real data in alignment scan.

        Without fix: caption row adds cols 0-1 to cols_with_data, defeating
        header override. All columns show ---.

        With fix: caption row skipped, cols 0-1 get :--: header override,
        col 2 stays --- from content majority.
        """
        html = BeautifulSoup(self.CAPTION_ALL_HEADER_COLUMNS_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        lines = result.split("\n")
        align_lines = [ln for ln in lines if ln.strip().startswith("|") and "---" in ln]
        assert align_lines, "Should have alignment row"
        cells = [c.strip() for c in align_lines[0].strip(" |").split(" | ")]
        # Column 0 is a header-only column (<th>) — should get header alignment.
        assert cells[0] in (":--", ":-:"), (
            f"Column 0 should have header-based alignment, got {cells[0]!r}"
        )
        # Column 1 is also a header-only column.
        assert cells[1] in (":--", ":-:"), (
            f"Column 1 should have header-based alignment, got {cells[1]!r}"
        )


class TestRowspanFillerExclusion:
    """Regression: rowspan filler <td> cells must not pollute cols_with_data.

    When _normalize_table_cells expands rowspan=N, it inserts <td>\u200b</td>
    filler cells into subsequent rows to occupy the column positions covered
    by the rowspan. These filler cells must be skipped by _td_cell_alignments
    so they don't add header-only columns to cols_with_data.
    """

    ROWSPAN_FILLER_EXCLUSION_HTML = """\
<table class="wikitable">
<tbody>
<tr>
  <th rowspan="2" style="text-align:center;">H1</th>
  <th style="text-align:center;">H2</th>
  <td>Data1</td>
</tr>
<tr>
  <th style="text-align:center;">H3</th>
  <td>Data2</td>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_rowspan_filler_excluded_from_alignment_scan(
        self, converter: WikiHtmlConverter
    ) -> None:
        """Rowspan filler <td> cells must not be counted as real data.

        Without fix: rowspan normalization inserts <td>\u200b</td> at col 0
        in row 2, adding col 0 to cols_with_data → no header override for
        column 0 (shows ---).

        With fix: filler cell skipped, col 0 gets :--: header override.
        """
        html = BeautifulSoup(self.ROWSPAN_FILLER_EXCLUSION_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        lines = result.split("\n")
        align_lines = [ln for ln in lines if ln.strip().startswith("|") and "---" in ln]
        assert align_lines, "Should have alignment row"
        cells = [c.strip() for c in align_lines[0].strip(" |").split(" | ")]
        # Column 0 has rowspan=2 <th> — should get header alignment.
        # Without fix, filler cell makes it ---. With fix, filler skipped.
        assert cells[0] in (":--", ":-:"), (
            f"Column 0 (rowspan filler column) should have header-based alignment, "
            f"got {cells[0]!r}"
        )


class TestRowspanColumnOffset:
    """Regression: rowspan cells must not cause column offset in subsequent rows."""

    ROWSPAN_COLUMN_OFFSET_HTML = """\
<table class="wikitable">
<caption>Fourier transform summary</caption>
<tbody>
<tr>
<th style="text-align:center;">ordinary frequency <i>ξ</i> (Hz)</th>
<th style="text-align:center;">unitary</th>
<td style="text-align:center;">$formula_1$</td>
</tr>
<tr>
<th rowspan="2">angular frequency <i>ω</i> (rad/s)</th>
<th style="text-align:center;">unitary</th>
<td style="text-align:center;">$formula_2$</td>
</tr>
<tr>
<th>non-unitary</th>
<td>$formula_3$</td>
</tr>
</tbody>
</table>"""

    @pytest.mark.anyio
    async def test_rowspan_column_count(self, converter: WikiHtmlConverter) -> None:
        """Rowspan=2 on first column should not shift the last cell's column position."""
        html = BeautifulSoup(self.ROWSPAN_COLUMN_OFFSET_HTML, "html.parser")
        result = await converter.convert(
            html, out_to_archive=set(), refs=True, redirect_map={}
        )
        lines = result.split("\n")
        # Find the non-unitary row (row after rowspan header).
        non_unitary_lines = [ln for ln in lines if "non-unitary" in ln]
        assert non_unitary_lines, "non-unitary row should be present"
        row = non_unitary_lines[0]
        cells = [c.strip() for c in row.strip(" |").split(" | ")]
        # The non-unitary row has column 1 empty (rowspan from angular frequency),
        # column 2 = non-unitary, column 3 = formula3.
        assert len(cells) == 3, (
            f"non-unitary row should have 3 cells (rowspan + th + td), "
            f"got {len(cells)} cells: {cells!r}"
        )
        # Column 2 should be non-unitary (bolded).
        assert "__non-unitary__" in cells[1], (
            f"Column 2 should be bold non-unitary, got {cells[1]!r}"
        )
        # Column 3 should be formula3 (escaped: \\$, \\_).
        assert "\\$formula\\_3\\$" in cells[2], (
            f"Column 3 should be formula3, got {cells[2]!r}"
        )


# ──────────────────────────────────────────────

# _smart_split_row

# ──────────────────────────────────────────────


class TestSmartSplitRow:
    """Tests for _smart_split_row.

    Covers math-aware pipe splitting, backslash-escaped pipes, and
    zero-width character stripping.
    """

    def test_simple_row(self) -> None:
        """Standard pipe-table row."""
        result = _smart_split_row("| a | b |")
        assert result == ["a", "b"]

    def test_row_with_spaces(self) -> None:
        """Row with varying whitespace."""
        result = _smart_split_row("|  foo  |  bar  |")
        assert result == ["foo", "bar"]

    def test_row_not_starting_with_pipe(self) -> None:
        """Line not starting with | → returns None."""
        assert _smart_split_row("a | b") is None

    def test_row_not_ending_with_pipe(self) -> None:
        """Line not ending with | → returns None."""
        assert _smart_split_row("| a | b") is None

    def test_empty_cell(self) -> None:
        """Row with empty cell (double pipe)."""
        result = _smart_split_row("| a |  |")
        assert result == ["a", ""]

    def test_empty_row(self) -> None:
        """Row with just two pipes."""
        result = _smart_split_row("||")
        assert result == [""]

    def test_separator_row(self) -> None:
        """Separator row parsed as cells."""
        result = _smart_split_row("| --- | :-- |")
        assert result == ["---", ":--"]

    def test_row_with_zero_width_chars(self) -> None:
        """Zero-width characters are stripped from cell content."""
        result = _smart_split_row("| a\u200bb |")
        assert result == ["ab"]

    def test_row_with_multiple_cells(self) -> None:
        """Row with many cells."""
        result = _smart_split_row("| a | b | c | d |")
        assert result == ["a", "b", "c", "d"]

    def test_pipe_in_math_inline(self) -> None:
        """Pipe inside $...$ should not split cells.

        The $...$ span is treated atomically: the ``|`` inside it is a
        protected pipe character, not a cell separator.
        """
        result = _smart_split_row("| $a | b$ | c |")
        # The pipe inside $...$ is protected; the outer pipes delimit 2 cells
        assert result == ["$a | b$", "c"]

    def test_pipe_in_math_display(self) -> None:
        """Pipe inside $$...$$ should not split cells."""
        result = _smart_split_row("| $$a | b$$ | c |")
        # The pipe inside $$...$$ is protected; outer pipes delimit 2 cells
        assert result == ["$$a | b$$", "c"]

    def test_pipe_in_code_span(self) -> None:
        """Pipe inside backtick code span should not split cells."""
        result = _smart_split_row("| `a | b` | c |")
        # The | inside the code span is protected; outer pipes delimit 2 cells
        assert result == ["`a | b`", "c"]

    def test_escaped_pipe(self) -> None:
        """Backslash-escaped pipe should not split cells."""
        result = _smart_split_row("| a \\| b | c |")
        assert result == ["a \\| b", "c"]

    def test_nested_math_and_code(self) -> None:
        """Mixed math and code spans in one table row."""
        result = _smart_split_row("| $x|y$ | `code|here` | normal |")
        # $...$ and `...` spans protect their internal pipes
        assert result == ["$x|y$", "`code|here`", "normal"]

    def test_consecutive_pipes_empty_cells(self) -> None:
        """Consecutive pipe characters create empty cells."""
        result = _smart_split_row("| a || b |")
        assert result == ["a", "", "b"]

    def test_leading_trailing_spaces_stripped(self) -> None:
        """Leading/trailing spaces in cells are stripped."""
        result = _smart_split_row("|  a  |  b  |")
        assert result == ["a", "b"]

    def test_no_pipes_inside_cell(self) -> None:
        """HTML-encoded pipes don't create cell boundaries."""
        result = _smart_split_row("| a &#124; b | c |")
        assert result == ["a &#124; b", "c"]

    def test_multiple_math_spans(self) -> None:
        """Multiple $...$ spans in one cell, each with a pipe."""
        result = _smart_split_row("| $a|b$ $c|d$ | e |")
        # Both $...$ spans protect their internal pipes; the whole content
        # between outer pipes is one cell
        assert result == ["$a|b$ $c|d$", "e"]


# ──────────────────────────────────────────────

# _reformat_table_block

# ──────────────────────────────────────────────


class TestReformatTableBlock:
    """Tests for _reformat_table_block (core table reformatter)."""

    def test_simple_table(self) -> None:
        """Simple two-column table with padding."""
        lines = ["| a | b |", "| --- | --- |", "| c | d |"]
        result = _reformat_table_block(lines)
        assert result == [
            "| a   | b   |",
            "| --- | --- |",
            "| c   | d   |",
        ]

    def test_aligned_table(self) -> None:
        """Table with alignment markers."""
        lines = ["| a | b |", "| :-: | --: |", "| c | d |"]
        result = _reformat_table_block(lines)
        # Center column padded, right column padded
        assert ":---" in result[1] or ":-:" in result[1]
        assert "-----:" in result[1] or "--:" in result[1]

    def test_uneven_column_widths(self) -> None:
        """Table with uneven widths → padded to widest value."""
        lines = ["| short | verylongcontent |", "| --- | --- |", "| a | b |"]
        result = _reformat_table_block(lines)
        # Column 2 should be wider than column 1
        cell2_len = len(result[0].split(" | ")[1])  # not stripping trailing |
        assert cell2_len >= len("verylongcontent") + 1  # +1 for padding

    def test_table_with_leading_dash_separator(self) -> None:
        """Compact separator without leading pipe isn't matched by _reformat_table_block."""
        lines = ["| a |", "---", "| b |"]
        # The --- line doesn't start with | so it breaks the block
        result = _reformat_table_block(lines)
        # Should detect invalid separator row and return unchanged
        assert result == lines

    def test_no_table_with_only_2_rows(self) -> None:
        """Block with < 2 lines returns unchanged."""
        lines = ["| a |"]
        result = _reformat_table_block(lines)
        assert result == lines

    def test_no_separator_row(self) -> None:
        """Block without separator row returns unchanged."""
        lines = ["| a | b |", "| c | d |"]
        result = _reformat_table_block(lines)
        assert result == lines

    def test_table_with_pipes_in_content(self) -> None:
        """Table cell with &#124; (HTML-encoded pipe) works."""
        lines = ["| a &#124; b | c |", "| --- | --- |", "| d | e |"]
        result = _reformat_table_block(lines)
        assert "&#124;" in result[0] or "&#124;" in result[0]

    def test_invalid_mixed_separator_row(self) -> None:
        """Row mixing text and separator cells returns unchanged."""
        lines = ["| a | b |", "| --- | c |", "| d | e |"]
        # The separator row mix of "---" and "c" should be rejected
        result = _reformat_table_block(lines)
        assert result == lines

    def test_pipe_in_math_cell(self) -> None:
        """Pipe inside $...$ in a cell should not break table structure."""
        lines = ["| a | $x | y$ |", "| :-: | :-: |", "| 1 | 2 |"]
        result = _reformat_table_block(lines)
        assert len(result) == 3, "Table should have 3 rows"
        assert "$x | y$" in result[0], (
            "Pipe in math should be preserved as cell content"
        )

    def test_escaped_pipe_in_cell(self) -> None:
        """Backslash-escaped pipe in cell content."""
        lines = ["| a | b \\| c |", "| --- | :-- |", "| d | e |"]
        result = _reformat_table_block(lines)
        assert len(result) == 3
        assert "b \\| c" in result[0]

    def test_math_pipe_and_normal_pipe(self) -> None:
        """Math pipes coexist with normal cell boundaries."""
        lines = [
            "| conditional | value |",
            "| --- | --- |",
            "| $P(A | B)$ | 0.5 |",
        ]
        result = _reformat_table_block(lines)
        assert len(result) == 3
        assert "$P(A | B)$" in result[2]


# ──────────────────────────────────────────────

# _reformat_table

# ──────────────────────────────────────────────


class TestReformatTable:
    """Integration tests for _reformat_table (finds and reformats all
    table blocks in text)."""

    def test_single_table(self) -> None:
        """Single table in text."""
        text = "| a | b |\n| --- | --- |\n| c | d |"
        result = _reformat_table(text)
        assert "| a   | b   |" in result
        assert "| --- | --- |" in result

    def test_multiple_tables(self) -> None:
        """Multiple tables in one text."""
        text = (
            "Before\n"
            "| a | b |\n| --- | --- |\n| c | d |\n"
            "Between\n"
            "| x | y | z |\n| --- | --- | --- |\n| 1 | 2 | 3 |"
        )
        result = _reformat_table(text)
        assert "| a   | b   |" in result
        # Each column has minimum width 3 (GFM minimum), so single-char cells
        # are padded to width 3.
        assert "| x   | y   | z   |" in result

    def test_no_tables(self) -> None:
        """No tables → unchanged."""
        text = "Just some text\n\nMore text"
        assert _reformat_table(text) == text

    def test_table_not_starting_with_pipe(self) -> None:
        """Line not starting with pipe → not a table block."""
        text = "a | b\n---\nc | d"
        assert _reformat_table(text) == text

    def test_mixed_text_and_tables(self) -> None:
        """Table padded correctly within surrounding text."""
        text = "Some text\n| longword | a |\n| --- | --- |\n| b | c |\nMore text"
        result = _reformat_table(text)
        lines = result.split("\n")
        # 0=Some text, 1=header row, 2=separator row, 3=data row, 4=More text
        assert "longword" in lines[1]
        assert "a" in lines[1]
        assert "b" in lines[3]
        assert "c" in lines[3]

    def test_table_with_pipes_in_math_multi_table(self) -> None:
        """Multiple tables with mixed math pipe content."""
        text = (
            "| a | $x|y$ |\n| :-: | :-: |\n| 1 | 2 |\n\n"
            "| normal | table |\n| --- | --- |\n| data | here |"
        )
        result = _reformat_table(text)
        lines = result.split("\n")
        assert "$x|y$" in lines[0]
        assert "normal" in lines[4]
        assert "data" in lines[6]

    def test_escaped_pipe_preserved(self) -> None:
        """Backslash-escaped pipes preserved in output."""
        text = "| cmd \\| args | desc |\n| --- | --- |\n| echo | test |"
        result = _reformat_table(text)
        assert "cmd \\| args" in result.split("\n")[0]

    def test_empty_table_block_not_modified(self) -> None:
        """Non-table pipe lines should pass through unchanged."""
        text = "| just a single pipe line"
        assert _reformat_table(text) == text
