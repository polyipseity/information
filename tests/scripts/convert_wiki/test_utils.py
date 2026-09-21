"""Tests for scripts/convert_wiki/utils.py.

These tests cover the pure helper functions used throughout the package.
"""

from os import PathLike

import pytest
from anyio import Path as AnyioPath
from bs4 import BeautifulSoup, Tag

from scripts.convert_wiki import config as _cfg
from scripts.convert_wiki import table as _tbl
from scripts.convert_wiki import utils as _mod
from scripts.convert_wiki.stems import _stem_for_title
from scripts.convert_wiki.symlinks import _resolve_local_target_filename

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestFindChildExact:
    """Tests for exact basename lookup."""

    @pytest.mark.anyio
    async def test_distinguishes_case(self, tmp_path: PathLike[str]) -> None:
        """Wrong casing must not match canonical basename."""
        parent = AnyioPath(tmp_path)
        await (parent / "Exponential map.md").write_text("x", encoding="UTF-8")

        assert await _mod._find_child_exact(parent, "Exponential map.md") is not None  # noqa: SLF001
        assert await _mod._find_child_exact(parent, "exponential map.md") is None  # noqa: SLF001

    @pytest.mark.anyio
    async def test_ignores_case_insensitive_exists(
        self,
        tmp_path: PathLike[str],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        """Exact lookup must not treat kernel exists() as a casing match."""
        parent = AnyioPath(tmp_path)
        on_disk = parent / "Exponential map.md"
        await on_disk.write_text("x", encoding="UTF-8")

        original_exists = AnyioPath.exists

        async def fake_exists(self: AnyioPath) -> bool:
            """Return True for case-insensitive matches of ``exponential map.md``."""
            if self.name.lower() == "exponential map.md":
                return True
            return await original_exists(self)

        monkeypatch.setattr(AnyioPath, "exists", fake_exists)

        assert await _mod._find_child_exact(parent, "exponential map.md") is None  # noqa: SLF001


class TestCreateRedirectSymlinks:
    """Tests for the _create_redirect_symlinks function."""

    @pytest.mark.anyio
    async def test_missing_creates_lang_and_mirror(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should create both symlinks when neither exists."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()

        await _mod._create_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page", "to page"
        )

        lang_link = lang_dir / "from page.md"
        mirror = wiki_dir / "from page.md"
        assert await lang_link.is_symlink()
        assert str(await lang_link.readlink()) == "to page.md"
        assert await mirror.is_symlink()
        assert str(await mirror.readlink()) == "eng/from page.md"

    @pytest.mark.anyio
    async def test_retargets_stale_symlink(self, tmp_path: PathLike[str]) -> None:
        """Should retarget an existing symlink pointing elsewhere."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("old target.md", target_is_directory=False)
        await (wiki_dir / "from page.md").symlink_to(
            "eng/from page.md", target_is_directory=False
        )

        await _mod._create_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page", "new target"
        )

        assert await lang_link.is_symlink()
        assert str(await lang_link.readlink()) == "new target.md"
        # Top-level mirror must remain intact.
        assert await (wiki_dir / "from page.md").is_symlink()

    @pytest.mark.anyio
    async def test_same_target_is_noop(self, tmp_path: PathLike[str]) -> None:
        """Should leave a symlink with the matching target untouched."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("to page.md", target_is_directory=False)
        await (wiki_dir / "from page.md").symlink_to(
            "eng/from page.md", target_is_directory=False
        )

        await _mod._create_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page", "to page"
        )

        assert str(await lang_link.readlink()) == "to page.md"
        assert await lang_link.is_symlink()

    @pytest.mark.anyio
    async def test_real_file_is_untouched(self, tmp_path: PathLike[str]) -> None:
        """Should never replace a real file at the redirect path."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        real_file = lang_dir / "from page.md"
        await real_file.write_text("precious content")

        await _mod._create_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page", "to page"
        )

        assert not await real_file.is_symlink()
        assert await real_file.read_text() == "precious content"
        # The top-level mirror is still created.
        assert await (wiki_dir / "from page.md").is_symlink()

    @pytest.mark.anyio
    async def test_top_mirror_missing_is_created(self, tmp_path: PathLike[str]) -> None:
        """Should create the top-level mirror when only the lang link exists."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("to page.md", target_is_directory=False)

        await _mod._create_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page", "to page"
        )

        mirror = wiki_dir / "from page.md"
        assert await mirror.is_symlink()
        assert str(await mirror.readlink()) == "eng/from page.md"

    @pytest.mark.anyio
    async def test_existing_mirror_real_file_untouched(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should never replace a real file at the top-level mirror path."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("to page.md", target_is_directory=False)
        mirror = wiki_dir / "from page.md"
        await mirror.write_text("precious mirror")

        await _mod._create_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page", "to page"
        )

        assert not await mirror.is_symlink()
        assert await mirror.read_text() == "precious mirror"

    @pytest.mark.anyio
    async def test_top_mirror_symlink_retargeted(self, tmp_path: PathLike[str]) -> None:
        """Existing top-level mirror symlinks should retarget to the lang link."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("to page.md", target_is_directory=False)
        mirror = wiki_dir / "from page.md"
        await mirror.symlink_to("eng/stale page.md", target_is_directory=False)

        await _mod._create_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page", "to page"
        )

        assert await mirror.is_symlink()
        assert str(await mirror.readlink()) == "eng/from page.md"

    @pytest.mark.anyio
    async def test_creates_canonical_name_when_only_wrong_case_exists(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Wrong-cased symlink must not satisfy canonical create checks."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        wrong = lang_dir / "From page.md"
        await wrong.symlink_to("to page.md", target_is_directory=False)

        await _mod._create_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page", "to page"
        )

        canonical = lang_dir / "from page.md"
        assert await canonical.is_symlink()
        assert str(await canonical.readlink()) == "to page.md"
        assert not await wrong.exists()


class TestRemoveRedirectSymlinks:
    """Tests for the _remove_redirect_symlinks function."""

    @pytest.mark.anyio
    async def test_removes_lang_symlink_and_mirror(
        self, tmp_path: PathLike[str]
    ) -> None:
        """Should unlink the lang symlink and the top-level mirror."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        lang_link = lang_dir / "from page.md"
        await lang_link.symlink_to("to page.md", target_is_directory=False)
        mirror = wiki_dir / "from page.md"
        await mirror.symlink_to("eng/from page.md", target_is_directory=False)

        await _mod._remove_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page"
        )

        assert not await lang_link.exists()
        assert not await mirror.exists()

    @pytest.mark.anyio
    async def test_real_file_kept(self, tmp_path: PathLike[str]) -> None:
        """Should never unlink a real file at either path."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()
        real_file = lang_dir / "from page.md"
        await real_file.write_text("precious content")

        await _mod._remove_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page"
        )

        assert await real_file.read_text() == "precious content"

    @pytest.mark.anyio
    async def test_absent_paths_are_noop(self, tmp_path: PathLike[str]) -> None:
        """Should do nothing when neither path exists."""
        wiki_dir = AnyioPath(tmp_path)
        lang_dir = wiki_dir / "eng"
        await lang_dir.mkdir()

        await _mod._remove_redirect_symlinks(  # noqa: SLF001
            wiki_dir, lang_dir, "from page"
        )

        assert not await (lang_dir / "from page.md").exists()
        assert not await (wiki_dir / "from page.md").exists()


class TestGetImageFilename:
    """Tests for the _get_image_filename function."""

    def test_lagrange_query_string_stripped(self) -> None:
        """Query strings should be stripped before deriving the filename."""
        img = BeautifulSoup(
            '<img src="https://upload.wikimedia.org/wikipedia/commons/8/8e/'
            "Lagrange_portrait.jpg?utm_source=en.wikipedia.org"
            '&amp;utm_campaign=parser&amp;utm_content=thumbnail"/>',
            "html.parser",
        ).find("img")
        assert isinstance(img, Tag)
        result = _mod._get_image_filename(img)  # noqa: SLF001
        assert result == "Lagrange portrait.jpg"

    def test_lagrange_clean_upload_url(self) -> None:
        """A clean upload URL without query should yield the same filename."""
        img = BeautifulSoup(
            '<img src="https://upload.wikimedia.org/wikipedia/commons/8/8e/'
            'Lagrange_portrait.jpg"/>',
            "html.parser",
        ).find("img")
        assert isinstance(img, Tag)
        result = _mod._get_image_filename(img)  # noqa: SLF001
        assert result == "Lagrange portrait.jpg"

    def test_filename_from_thumb_host_thumbnail(self) -> None:
        """Thumbnail URLs on thumb.wikimedia.org yield the original filename."""
        img = BeautifulSoup(
            '<img src="//thumb.wikimedia.org/wikipedia/commons/thumb/a/a0/'
            "Einstein_patentoffice.jpg/250px-Einstein_patentoffice.jpg"
            '?utm_source=en.wikipedia.org"/>',
            "html.parser",
        ).find("img")
        assert isinstance(img, Tag)
        result = _mod._get_image_filename(img)  # noqa: SLF001
        assert result == "Einstein patentoffice.jpg"

    def test_filename_from_thumb_host_percent_encoded(self) -> None:
        """Percent-encoded thumb-host filenames are decoded."""
        img = BeautifulSoup(
            '<img src="//thumb.wikimedia.org/wikipedia/commons/thumb/2/29/'
            'Sinh%2Bcosh%2Btanh.svg/250px-Sinh%2Bcosh%2Btanh.svg.png"/>',
            "html.parser",
        ).find("img")
        assert isinstance(img, Tag)
        result = _mod._get_image_filename(img)  # noqa: SLF001
        assert result == "Sinh+cosh+tanh.svg"

    @pytest.mark.parametrize(
        ("url", "expected"),
        [
            (
                "//thumb.wikimedia.org/wikipedia/commons/transcoded/9/93/"
                "X.ogv/X.ogv.480p.vp9.webm",
                "X.ogv",
            ),
            (
                "//thumb.wikimedia.org/wikipedia/en/transcoded/9/93/"
                "X.ogv/X.ogv.360p.mpeg4.mov",
                "X.ogv",
            ),
            (
                "//thumb.wikimedia.org/wikipedia/commons/transcoded/2/29/"
                "Sinh%2Bcosh%2Btanh.svg/Sinh%2Bcosh%2Btanh.svg.480p.vp9.webm",
                "Sinh+cosh+tanh.svg",
            ),
            (
                "//thumb.wikimedia.org/wikipedia/commons/transcoded/9/93/"
                "X.ogv/X.ogv.480p.vp9.webm?utm_source=en.wikipedia.org",
                "X.ogv",
            ),
        ],
    )
    def test_filename_from_thumb_host_transcoded(self, url: str, expected: str) -> None:
        """Transcoded URLs on thumb.wikimedia.org yield the source filename.

        The transcoded segment names the derivative, so the original file is
        the directory above it: that is what the archive holds, and a query
        string must not become part of the name.
        """
        img = BeautifulSoup(f'<img src="{url}"/>', "html.parser").find("img")
        assert isinstance(img, Tag)
        result = _mod._get_image_filename(img)  # noqa: SLF001
        assert result == expected


class TestBalanceBrackets:
    """Tests for the _balance_brackets function."""

    @pytest.mark.parametrize(
        ("input_text", "expected"),
        [
            # Category 1: No brackets / trivial
            ("", ""),
            ("hello world", "hello world"),
            ("   ", "   "),
            # Category 2: Single balanced pair
            ("[Dirac equation]", "[Dirac equation]"),
            ("the [equation]", "the [equation]"),
            # Category 3: Lone unbalanced brackets
            ("[", R"\["),
            ("]", R"\]"),
            ("abc[def", R"abc\[def"),
            ("abc]def", R"abc\]def"),
            # Category 4: Multiple brackets — mixed balance
            ("[a][b][c]", "[a][b][c]"),
            ("abc]def[ghi]", R"abc\]def[ghi]"),
            ("][", R"\]\["),
            ("[[a]", R"\[[a]"),
            ("[[a]]", "[[a]]"),
            # Category 5: Consecutive unbalanced of same type
            ("]]]", R"\]\]\]"),
            ("[[[", R"\[\[\["),
            ("]][[", R"\]\]\[\["),
            # Category 6: Nested brackets
            ("[[inner] outer]", "[[inner] outer]"),
            ("[[[deep]]]", "[[[deep]]]"),
            ("[[inner]", R"\[[inner]"),
            ("[outer[inner]", R"\[outer[inner]"),
            # Category 7: Real-world Markdown links (Commons API descriptions)
            ("the[Dirac equation](url)", "the[Dirac equation](url)"),
            (
                "see[link text](https://example.org)",
                "see[link text](https://example.org)",
            ),
            (
                "A description with [link](url) and [another](url2)",
                "A description with [link](url) and [another](url2)",
            ),
            # Category 8: The actual Modernphysicsfields.svg alt text
            (
                "A simplified view of the history of physics, showing the[Dirac equation]"
                "(https://en.wikipedia.org/wiki/Dirac_equation) which unifies quantum "
                "mechanics with special relativity, as well as the[Standard Model]"
                "(https://en.wikipedia.org/wiki/Standard_Model) and a possible[theory of "
                "everything](https://en.wikipedia.org/wiki/Theory_of_everything). These "
                "days the search continues.",
                "A simplified view of the history of physics, showing the[Dirac equation]"
                "(https://en.wikipedia.org/wiki/Dirac_equation) which unifies quantum "
                "mechanics with special relativity, as well as the[Standard Model]"
                "(https://en.wikipedia.org/wiki/Standard_Model) and a possible[theory of "
                "everything](https://en.wikipedia.org/wiki/Theory_of_everything). These "
                "days the search continues.",
            ),
            # Category 9: Input already containing backslash-escaped brackets
            (R"\[literal\]", R"\[literal\]"),
            (R"text \[ literal ]", R"text \[ literal ]"),
        ],
    )
    def test_balance_brackets(self, input_text: str, expected: str) -> None:
        """Verify bracket-balancing behaves correctly for the given case."""
        assert _mod._balance_brackets(input_text) == expected  # noqa: SLF001


class TestSmartSplitRow:
    """Tests for _smart_split_row.

    Covers math-aware pipe splitting, backslash-escaped pipes, and
    zero-width character stripping.
    """

    def test_simple_row(self) -> None:
        """Standard pipe-table row."""
        result = _tbl._smart_split_row("| a | b |")  # noqa: SLF001
        assert result == ["a", "b"]

    def test_row_with_spaces(self) -> None:
        """Row with varying whitespace."""
        result = _tbl._smart_split_row("|  foo  |  bar  |")  # noqa: SLF001
        assert result == ["foo", "bar"]

    def test_row_not_starting_with_pipe(self) -> None:
        """Line not starting with | → returns None."""
        assert _tbl._smart_split_row("a | b") is None  # noqa: SLF001

    def test_row_not_ending_with_pipe(self) -> None:
        """Line not ending with | → returns None."""
        assert _tbl._smart_split_row("| a | b") is None  # noqa: SLF001

    def test_empty_cell(self) -> None:
        """Row with empty cell (double pipe)."""
        result = _tbl._smart_split_row("| a |  |")  # noqa: SLF001
        assert result == ["a", ""]

    def test_empty_row(self) -> None:
        """Row with just two pipes."""
        result = _tbl._smart_split_row("||")  # noqa: SLF001
        assert result == [""]

    def test_separator_row(self) -> None:
        """Separator row parsed as cells."""
        result = _tbl._smart_split_row("| --- | :-- |")  # noqa: SLF001
        assert result == ["---", ":--"]

    def test_row_with_zero_width_chars(self) -> None:
        """Zero-width characters are stripped from cell content."""
        result = _tbl._smart_split_row("| a\u200bb |")  # noqa: SLF001
        assert result == ["ab"]

    def test_row_with_multiple_cells(self) -> None:
        """Row with many cells."""
        result = _tbl._smart_split_row("| a | b | c | d |")  # noqa: SLF001
        assert result == ["a", "b", "c", "d"]

    def test_pipe_in_math_inline(self) -> None:
        """Pipe inside $...$ should not split cells.

        The $...$ span is treated atomically: the ``|`` inside it is a
        protected pipe character, not a cell separator.
        """
        result = _tbl._smart_split_row("| $a | b$ | c |")  # noqa: SLF001
        # The pipe inside $...$ is protected; the outer pipes delimit 2 cells
        assert result == ["$a | b$", "c"]

    def test_pipe_in_math_display(self) -> None:
        """Pipe inside $$...$$ should not split cells."""
        result = _tbl._smart_split_row("| $$a | b$$ | c |")  # noqa: SLF001
        # The pipe inside $$...$$ is protected; outer pipes delimit 2 cells
        assert result == ["$$a | b$$", "c"]

    def test_pipe_in_code_span(self) -> None:
        """Pipe inside backtick code span should not split cells."""
        result = _tbl._smart_split_row("| `a | b` | c |")  # noqa: SLF001
        # The | inside the code span is protected; outer pipes delimit 2 cells
        assert result == ["`a | b`", "c"]

    def test_escaped_pipe(self) -> None:
        """Backslash-escaped pipe should not split cells."""
        result = _tbl._smart_split_row("| a \\| b | c |")  # noqa: SLF001
        assert result == ["a \\| b", "c"]

    def test_nested_math_and_code(self) -> None:
        """Mixed math and code spans in one table row."""
        result = _tbl._smart_split_row(  # noqa: SLF001
            "| $x|y$ | `code|here` | normal |"
        )
        # $...$ and `...` spans protect their internal pipes
        assert result == ["$x|y$", "`code|here`", "normal"]

    def test_consecutive_pipes_empty_cells(self) -> None:
        """Consecutive pipe characters create empty cells."""
        result = _tbl._smart_split_row("| a || b |")  # noqa: SLF001
        assert result == ["a", "", "b"]

    def test_leading_trailing_spaces_stripped(self) -> None:
        """Leading/trailing spaces in cells are stripped."""
        result = _tbl._smart_split_row("|  a  |  b  |")  # noqa: SLF001
        assert result == ["a", "b"]

    def test_no_pipes_inside_cell(self) -> None:
        """HTML-encoded pipes don't create cell boundaries."""
        result = _tbl._smart_split_row("| a &#124; b | c |")  # noqa: SLF001
        assert result == ["a &#124; b", "c"]

    def test_multiple_math_spans(self) -> None:
        """Multiple $...$ spans in one cell, each with a pipe."""
        result = _tbl._smart_split_row("| $a|b$ $c|d$ | e |")  # noqa: SLF001
        # Both $...$ spans protect their internal pipes; the whole content
        # between outer pipes is one cell
        assert result == ["$a|b$ $c|d$", "e"]


class TestReformatTableBlock:
    """Tests for _reformat_table_block (core table reformatter)."""

    def test_simple_table(self) -> None:
        """Simple two-column table with padding."""
        lines = ["| a | b |", "| --- | --- |", "| c | d |"]
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        assert result == [
            "| a   | b   |",
            "| --- | --- |",
            "| c   | d   |",
        ]

    def test_aligned_table(self) -> None:
        """Table with alignment markers."""
        lines = ["| a | b |", "| :-: | --: |", "| c | d |"]
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        # Center column padded, right column padded
        assert ":---" in result[1] or ":-:" in result[1]
        assert "-----:" in result[1] or "--:" in result[1]

    def test_uneven_column_widths(self) -> None:
        """Table with uneven widths → padded to widest value."""
        lines = ["| short | verylongcontent |", "| --- | --- |", "| a | b |"]
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        # Column 2 should be wider than column 1
        cell2_len = len(result[0].split(" | ")[1])  # not stripping trailing |
        assert cell2_len >= len("verylongcontent") + 1  # +1 for padding

    def test_table_with_leading_dash_separator(self) -> None:
        """Compact separator without leading pipe isn't matched by _reformat_table_block."""
        lines = ["| a |", "---", "| b |"]
        # The --- line doesn't start with | so it breaks the block
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        # Should detect invalid separator row and return unchanged
        assert result == lines

    def test_no_table_with_only_2_rows(self) -> None:
        """Block with < 2 lines returns unchanged."""
        lines = ["| a |"]
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        assert result == lines

    def test_no_separator_row(self) -> None:
        """Block without separator row returns unchanged."""
        lines = ["| a | b |", "| c | d |"]
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        assert result == lines

    def test_table_with_pipes_in_content(self) -> None:
        """Table cell with &#124; (HTML-encoded pipe) works."""
        lines = ["| a &#124; b | c |", "| --- | --- |", "| d | e |"]
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        assert "&#124;" in result[0] or "&#124;" in result[0]

    def test_invalid_mixed_separator_row(self) -> None:
        """Row mixing text and separator cells returns unchanged."""
        lines = ["| a | b |", "| --- | c |", "| d | e |"]
        # The separator row mix of "---" and "c" should be rejected
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        assert result == lines

    def test_pipe_in_math_cell(self) -> None:
        """Pipe inside $...$ in a cell should not break table structure."""
        lines = ["| a | $x | y$ |", "| :-: | :-: |", "| 1 | 2 |"]
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        assert len(result) == 3, "Table should have 3 rows"
        assert "$x | y$" in result[0], (
            "Pipe in math should be preserved as cell content"
        )

    def test_escaped_pipe_in_cell(self) -> None:
        """Backslash-escaped pipe in cell content."""
        lines = ["| a | b \\| c |", "| --- | :-- |", "| d | e |"]
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        assert len(result) == 3
        assert "b \\| c" in result[0]

    def test_math_pipe_and_normal_pipe(self) -> None:
        """Math pipes coexist with normal cell boundaries."""
        lines = [
            "| conditional | value |",
            "| --- | --- |",
            "| $P(A | B)$ | 0.5 |",
        ]
        result = _tbl._reformat_table_block(lines)  # noqa: SLF001
        assert len(result) == 3
        assert "$P(A | B)$" in result[2]


class TestReformatTable:
    """Integration tests for _reformat_table (finds and reformats all
    table blocks in text)."""

    def test_single_table(self) -> None:
        """Single table in text."""
        text = "| a | b |\n| --- | --- |\n| c | d |"
        result = _tbl._reformat_table(text)  # noqa: SLF001
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
        result = _tbl._reformat_table(text)  # noqa: SLF001
        assert "| a   | b   |" in result
        # Each column has minimum width 3 (GFM minimum), so single-char cells
        # are padded to width 3.
        assert "| x   | y   | z   |" in result

    def test_no_tables(self) -> None:
        """No tables → unchanged."""
        text = "Just some text\n\nMore text"
        assert _tbl._reformat_table(text) == text  # noqa: SLF001

    def test_table_not_starting_with_pipe(self) -> None:
        """Line not starting with pipe → not a table block."""
        text = "a | b\n---\nc | d"
        assert _tbl._reformat_table(text) == text  # noqa: SLF001

    def test_mixed_text_and_tables(self) -> None:
        """Table padded correctly within surrounding text."""
        text = "Some text\n| longword | a |\n| --- | --- |\n| b | c |\nMore text"
        result = _tbl._reformat_table(text)  # noqa: SLF001
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
        result = _tbl._reformat_table(text)  # noqa: SLF001
        lines = result.split("\n")
        assert "$x|y$" in lines[0]
        assert "normal" in lines[4]
        assert "data" in lines[6]

    def test_escaped_pipe_preserved(self) -> None:
        """Backslash-escaped pipes preserved in output."""
        text = "| cmd \\| args | desc |\n| --- | --- |\n| echo | test |"
        result = _tbl._reformat_table(text)  # noqa: SLF001
        assert "cmd \\| args" in result.split("\n")[0]

    def test_empty_table_block_not_modified(self) -> None:
        """Non-table pipe lines should pass through unchanged."""
        text = "| just a single pipe line"
        assert _tbl._reformat_table(text) == text  # noqa: SLF001

    def test_blockquoted_table_aligned(self) -> None:
        """A single-level ``> ``-prefixed pipe table is padded to equal widths."""
        text = "> | short | longcontent |\n> | --- | --- |\n> | a | b |"
        result = _tbl._reformat_table(text)  # noqa: SLF001
        lines = result.split("\n")
        # All three rows share identical pipe positions (true column alignment).
        assert (
            [p for p in range(len(lines[0])) if lines[0][p] == "|"]
            == [p for p in range(len(lines[1])) if lines[1][p] == "|"]
            == [p for p in range(len(lines[2])) if lines[2][p] == "|"]
        )
        # Column 2 is wider than column 1 (padded to widest content).
        assert len(lines[0].split("|")[2]) > len(lines[0].split("|")[1])
        # The ``> `` prefix is preserved on every row.
        assert all(line.startswith("> ") for line in lines)

    def test_nested_blockquoted_table_aligned(self) -> None:
        """A nested ``> > ``-prefixed pipe table keeps its prefix and aligns."""
        text = "> > | short | longcontent |\n> > | --- | --- |\n> > | a | b |"
        result = _tbl._reformat_table(text)  # noqa: SLF001
        lines = result.split("\n")
        assert (
            [p for p in range(len(lines[0])) if lines[0][p] == "|"]
            == [p for p in range(len(lines[1])) if lines[1][p] == "|"]
            == [p for p in range(len(lines[2])) if lines[2][p] == "|"]
        )
        assert len(lines[0].split("|")[2]) > len(lines[0].split("|")[1])
        # The full ``> > `` prefix is preserved on every row.
        assert all(line.startswith("> > ") for line in lines)


class TestResolveLocalTargetFilename:
    """Tests for redirect target filename resolution."""

    @pytest.mark.anyio
    async def test_requires_exact_casing(self, tmp_path: PathLike[str]) -> None:
        """Wrong-cased on-disk targets must not satisfy canonical names."""
        lang_dir = AnyioPath(tmp_path)
        await (lang_dir / "Final page.md").write_text("x", encoding="UTF-8")

        resolved = await _resolve_local_target_filename(
            lang_dir=lang_dir,
            to_title="Intermediate",
            final_to_title="Final page",
            names_map={"Intermediate": "intermediate", "Final page": "final page"},
        )

        assert resolved == "intermediate.md"

    @pytest.mark.anyio
    async def test_prefers_exact_final_target(self, tmp_path: PathLike[str]) -> None:
        """Chain resolution should use final target when present with exact casing."""
        lang_dir = AnyioPath(tmp_path)
        await (lang_dir / "final page.md").write_text("x", encoding="UTF-8")

        resolved = await _resolve_local_target_filename(
            lang_dir=lang_dir,
            to_title="Intermediate",
            final_to_title="Final page",
            names_map={"Intermediate": "intermediate", "Final page": "final page"},
        )

        assert resolved == "final page.md"


class TestStemForTitle:
    """Tests for _stem_for_title."""

    def test_uses_name_map(self) -> None:
        """Mapped titles should resolve to the configured stem."""
        names_map = {"Modern physics": "Modern physics"}
        assert _stem_for_title("Modern physics", names_map) == "Modern physics"

    def test_matches_legacy_target_filename_behavior(self) -> None:
        """Should match the old reconcile _target_filename heuristic."""
        title = next(iter(_cfg._NAMES_MAP))
        assert _stem_for_title(title) == _stem_for_title(title, _cfg._NAMES_MAP)


# ---------------------------------------------------------------------------
# MediaWiki legacy fragment decoding
# ---------------------------------------------------------------------------


class TestDecodeLegacyFragment:
    """Tests for the single-pass legacy fragment scanner."""

    def test_unicode_escape(self) -> None:
        """En-dash (E2 80 93) should be decoded from a .HH run."""
        assert (
            _mod._decode_legacy_fragment("The%20Segal.E2.80.93Bargmann")  # noqa: SLF001
            == "The Segal\u2013Bargmann"
        )

    def test_ascii_punctuation_escapes(self) -> None:
        """Standard ASCII punctuation escapes should be decoded."""
        assert _mod._decode_legacy_fragment("a.22b") == 'a"b'  # noqa: SLF001
        assert _mod._decode_legacy_fragment("a.27b") == "a'b"  # noqa: SLF001
        assert _mod._decode_legacy_fragment("a.28b") == "a(b"  # noqa: SLF001
        assert _mod._decode_legacy_fragment("a.29b") == "a)b"  # noqa: SLF001
        assert _mod._decode_legacy_fragment("a.2Cb") == "a,b"  # noqa: SLF001
        assert _mod._decode_legacy_fragment("a.3Db") == "a=b"  # noqa: SLF001
        assert _mod._decode_legacy_fragment("a.3Fb") == "a?b"  # noqa: SLF001

    def test_literal_set_preserved(self) -> None:
        """Runs whose bytes are in the literal set stay verbatim."""
        assert _mod._decode_legacy_fragment("math_Eq.1") == "math_Eq.1"  # noqa: SLF001
        assert _mod._decode_legacy_fragment("a.2Eb") == "a.2Eb"  # noqa: SLF001
        assert _mod._decode_legacy_fragment("a.3Ab") == "a.3Ab"  # noqa: SLF001
        assert _mod._decode_legacy_fragment("a.7Ab") == "a.7Ab"  # noqa: SLF001

    def test_control_char_decoded_by_scanner(self) -> None:
        """A .19 sequence (control byte 0x19) is decoded by the scanner.

        C0 control characters are spec-reachable (``urlencode`` escapes them),
        so the scanner decodes them. Preservation happens at the acceptance
        level (``_plain_fragment``), not at the scanner level.
        """
        assert _mod._decode_legacy_fragment("al.1994") == "al\x1994"  # noqa: SLF001

    def test_percent_escape_decoded(self) -> None:
        """Percent-encoded runs should be decoded."""
        assert _mod._decode_legacy_fragment("Schr%C3%B6dinger") == "Schr\u00f6dinger"  # noqa: SLF001

    def test_mixed_percent_and_legacy(self) -> None:
        """Both escape types in one source should each be decoded."""
        result = _mod._decode_legacy_fragment("A.E2.80.93B%20C")  # noqa: SLF001
        assert result == "A\u2013B C"

    def test_no_rescan_decoded_percent(self) -> None:
        """A decoded .25 (literal %) must not be re-scanned as percent."""
        assert _mod._decode_legacy_fragment("A.25B%20C") == "A%B C"  # noqa: SLF001

    def test_percent25_no_rescan(self) -> None:
        """%25 (percent-encoded %) followed by hex text must not leak."""
        assert _mod._decode_legacy_fragment("A%2528B") == "A%28B"  # noqa: SLF001

    def test_invalid_utf8_preserved(self) -> None:
        """A run that is not valid UTF-8 stays literal."""
        # 0x80 alone: a continuation byte, invalid as a start byte.
        assert _mod._decode_legacy_fragment("a.80b") == "a.80b"  # noqa: SLF001

    def test_lowercase_hex_accepted(self) -> None:
        """Lowercase hex should be accepted defensively."""
        result = _mod._decode_legacy_fragment("a.e2.80.93b")  # noqa: SLF001
        assert result == "a\u2013b"

    def test_literal_text_copied(self) -> None:
        """Non-escape text is copied verbatim."""
        assert _mod._decode_legacy_fragment("hello world") == "hello world"  # noqa: SLF001

    def test_greek_omega(self) -> None:
        """CF.89 → ω (omega)."""
        assert _mod._decode_legacy_fragment(".CF.89") == "\u03c9"  # noqa: SLF001

    def test_empty_string(self) -> None:
        """An empty fragment returns empty."""
        assert _mod._decode_legacy_fragment("") == ""  # noqa: SLF001


class TestIsKnownFragment:
    """Tests for _is_known_fragment resolution."""

    def test_exact_match(self) -> None:
        assert _mod._is_known_fragment("foo", frozenset({"foo"}), None)  # noqa: SLF001

    def test_underscore_variant(self) -> None:
        assert _mod._is_known_fragment("foo_bar", frozenset({"foo bar"}), None)  # noqa: SLF001

    def test_names_map_hit(self) -> None:
        assert _mod._is_known_fragment("Foo", frozenset(), {"Foo": "x"})  # noqa: SLF001

    def test_names_map_underscore_variant(self) -> None:
        assert _mod._is_known_fragment("foo_bar", frozenset(), {"foo bar": "x"})  # noqa: SLF001

    def test_miss(self) -> None:
        assert not _mod._is_known_fragment("missing", frozenset(), {"other": "x"})  # noqa: SLF001


class TestPlainFragmentAcceptance:
    """Tests for _plain_fragment acceptance logic."""

    def test_legacy_decoded_when_in_names_map(self) -> None:
        """Candidate in names map should be accepted."""
        result = _mod._plain_fragment(  # noqa: SLF001
            "The%20Segal.E2.80.93Bargmann%20transform",
            names_map={
                "The Segal\u2013Bargmann transform": "the Segal\u2013Bargmann transform"
            },
        )
        assert result == "The Segal\u2013Bargmann transform"

    def test_legacy_decoded_when_in_known_fragments(self) -> None:
        """Candidate in known_fragments should be accepted."""
        result = _mod._plain_fragment(  # noqa: SLF001
            "x.E2.80.93y",
            known_fragments=frozenset({"x\u2013y"}),
        )
        assert result == "x\u2013y"

    def test_rejected_falls_back_to_percent_only(self) -> None:
        """Unknown candidate falls back to unquote-only."""
        result = _mod._plain_fragment(  # noqa: SLF001
            "The%20Segal.E2.80.93Bargmann%20transform",
            names_map={},
        )
        assert result == "The Segal.E2.80.93Bargmann transform"

    def test_control_char_candidate_rejected(self) -> None:
        """A candidate containing a control char is rejected (no known anchor)."""
        result = _mod._plain_fragment(  # noqa: SLF001
            "al.1994",
            names_map={},
        )
        # .19 decodes to \x19 (control char) which is not a known anchor;
        # the fallback is percent-only = unquote('al.1994') = 'al.1994'.
        assert result == "al.1994"

    def test_percent_only_when_no_legacy_escapes(self) -> None:
        """Percent-only fragments decode via unquote."""
        result = _mod._plain_fragment("Schr%C3%B6dinger_equation")  # noqa: SLF001
        assert result == "Schr\u00f6dinger_equation"

    def test_plain_text_unchanged(self) -> None:
        """Plain text passes through unchanged."""
        assert _mod._plain_fragment("hello") == "hello"  # noqa: SLF001
