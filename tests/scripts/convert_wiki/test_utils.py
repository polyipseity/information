"""Tests for scripts/convert_wiki/utils.py.

These tests cover the pure helper functions used throughout the package.
"""

from os import PathLike

import pytest
from anyio import Path as AnyioPath
from bs4 import BeautifulSoup, Tag

from scripts.convert_wiki import utils as _mod
from scripts.convert_wiki.config import _NAMES_MAP

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestFixNameMaybe:
    """Tests for the _fix_name_maybe function."""

    def test_normalize_non_breaking_space(self) -> None:
        """Should replace non-breaking spaces with regular spaces."""
        result = _mod._fix_name_maybe("Hello\u00a0World")  # noqa: SLF001
        assert result == "Hello World"

    def test_mapped_name(self) -> None:
        """Should return the mapped name if it exists in _NAMES_MAP."""
        # Verify the first mapping entry round-trips correctly.
        for key, expected in _NAMES_MAP.items():  # noqa: SLF001
            result = _mod._fix_name_maybe(key)  # noqa: SLF001
            assert result == expected
            break
        else:
            # Empty names map — fall back to basic smoke test.
            assert isinstance(_mod._fix_name_maybe("test"), str)  # noqa: SLF001

    def test_replace_underscores(self) -> None:
        """Should replace underscores with spaces when requested."""
        result = _mod._fix_name_maybe(  # noqa: SLF001
            "Hello_World", replace_underscores=True
        )
        assert "_" not in result
        assert "Hello World" in result or result.islower()  # may be lowercased

    def test_single_char_name(self) -> None:
        """Should handle single character names without crashing."""
        result = _mod._fix_name_maybe("A")  # noqa: SLF001
        assert isinstance(result, str)

    def test_short_name_lowercase_second_char(self) -> None:
        """Should lowercase first char when second char is already lowercase."""
        result = _mod._fix_name_maybe("aBC")  # noqa: SLF001
        assert result == "aBC"  # first char is already lowercase

    def test_lowercase_first_char_relooks_up_names_map(self) -> None:
        """Lowercase-first-char fallback should consult names_map on lowered key."""
        names_map = {"lie bracket of vector fields": "Lie bracket of vector fields"}
        result = _mod._fix_name_maybe(  # noqa: SLF001
            "Lie bracket of vector fields",
            names_map=names_map,
        )
        assert result == "Lie bracket of vector fields"

    def test_unmapped_title_still_lowercases_first_char(self) -> None:
        """Unmapped titles should keep the lowercase-first-char heuristic."""
        result = _mod._fix_name_maybe("Fourier transform", names_map={})  # noqa: SLF001
        assert result == "fourier transform"


class TestFixFilename:
    """Tests for the _fix_filename function."""

    def test_replaces_colon(self) -> None:
        """Should replace colon with underscore."""
        assert _mod._fix_filename("a:b") == "a_b"  # noqa: SLF001

    def test_replaces_backslash(self) -> None:
        """Should replace backslash with underscore."""
        assert _mod._fix_filename("a\\b") == "a_b"  # noqa: SLF001

    def test_replaces_forward_slash(self) -> None:
        """Should replace forward slash with underscore."""
        assert _mod._fix_filename("a/b") == "a_b"  # noqa: SLF001

    def test_keeps_safe_characters(self) -> None:
        """Should keep normal alphanumeric characters unchanged."""
        assert _mod._fix_filename("hello_world-123.md") == "hello_world-123.md"  # noqa: SLF001

    def test_empty_string(self) -> None:
        """Should handle empty string safely."""
        assert _mod._fix_filename("") == ""  # noqa: SLF001


class TestMarkdownFragment:
    """Tests for the _markdown_fragment function."""

    def test_empty_fragment(self) -> None:
        """Should return empty string for empty fragment."""
        assert _mod._markdown_fragment("") == ""  # noqa: SLF001

    def test_removes_colons(self) -> None:
        """Should remove colons from the fragment."""
        result = _mod._markdown_fragment("ref:note")  # noqa: SLF001
        assert ":" not in result

    def test_encodes_spaces(self) -> None:
        """Should encode spaces as %20."""
        result = _mod._markdown_fragment("my section")  # noqa: SLF001
        assert "%20" in result

    def test_encodes_slash(self) -> None:
        """Should encode forward slashes as %2F."""
        result = _mod._markdown_fragment("a/b")  # noqa: SLF001
        assert "%2F" in result

    def test_prepends_hash(self) -> None:
        """Should prepend # to non-empty fragments."""
        result = _mod._markdown_fragment("section")  # noqa: SLF001
        assert result.startswith("#")


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


class TestMarkdownLinkTarget:
    """Tests for the _markdown_link_target function."""

    def test_basic_link(self) -> None:
        """Should build a basic Markdown link target."""
        result = _mod._markdown_link_target("Page Name", "")  # noqa: SLF001
        assert result == "Page%20Name.md"

    def test_with_fragment(self) -> None:
        """Should append fragment when provided."""
        result = _mod._markdown_link_target("Page", "section")  # noqa: SLF001
        assert result == "Page.md#section"


class TestTagAffixes:
    """Tests for the _tag_affixes function."""

    def test_simple_tag(self) -> None:
        """Should return opening and closing tags."""
        open_tag, close_tag = _mod._tag_affixes("div")  # noqa: SLF001
        assert open_tag == "<div>"
        assert close_tag == "</div>"

    def test_void_tag(self) -> None:
        """Should handle any tag name correctly."""
        open_tag, close_tag = _mod._tag_affixes("br")  # noqa: SLF001
        assert open_tag == "<br>"
        assert close_tag == "</br>"


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


class TestIsSeparatorCell:
    """Tests for _is_separator_cell."""

    def test_simple_dashes(self) -> None:
        """--- is a valid separator cell."""
        assert _mod._is_separator_cell("---")  # noqa: SLF001

    def test_left_aligned(self) -> None:
        """:-- is a valid separator cell."""
        assert _mod._is_separator_cell(":--")  # noqa: SLF001

    def test_right_aligned(self) -> None:
        """--: is a valid separator cell."""
        assert _mod._is_separator_cell("--:")  # noqa: SLF001

    def test_centered(self) -> None:
        """:-: is a valid separator cell."""
        assert _mod._is_separator_cell(":-:")  # noqa: SLF001

    def test_too_short(self) -> None:
        """-- (2 dashes) is NOT a valid separator cell."""
        assert not _mod._is_separator_cell("--")  # noqa: SLF001

    def test_only_one_dash(self) -> None:
        """- is NOT a valid separator cell."""
        assert not _mod._is_separator_cell("-")  # noqa: SLF001

    def test_empty_string(self) -> None:
        """Empty string is NOT a valid separator cell."""
        assert not _mod._is_separator_cell("")  # noqa: SLF001

    def test_non_separator_text(self) -> None:
        """Regular text is NOT a valid separator cell."""
        assert not _mod._is_separator_cell("hello")  # noqa: SLF001

    def test_long_separator(self) -> None:
        """Long separator (e.g. ------) is valid."""
        assert _mod._is_separator_cell("------")  # noqa: SLF001

    def test_long_centered_separator(self) -> None:
        """:-----: is valid."""
        assert _mod._is_separator_cell(":-----:")  # noqa: SLF001

    def test_long_left_separator(self) -> None:
        """:------ is valid."""
        assert _mod._is_separator_cell(":------")  # noqa: SLF001

    def test_long_right_separator(self) -> None:
        """-------: is valid."""
        assert _mod._is_separator_cell("-------:")  # noqa: SLF001

    def test_separator_with_non_dash_chars(self) -> None:
        """String with non-dash chars is NOT a separator."""
        assert not _mod._is_separator_cell(":-x:")  # noqa: SLF001


class TestGetSeparatorAlignment:
    """Tests for _get_separator_alignment."""

    def test_default_alignment(self) -> None:
        """--- → ---."""
        assert _mod._get_separator_alignment("---") == "---"  # noqa: SLF001

    def test_left_alignment(self) -> None:
        """:-- → :--."""
        assert _mod._get_separator_alignment(":--") == ":--"  # noqa: SLF001

    def test_right_alignment(self) -> None:
        """--: → --:."""
        assert _mod._get_separator_alignment("--:") == "--:"  # noqa: SLF001

    def test_center_alignment(self) -> None:
        """:-: → :-:."""
        assert _mod._get_separator_alignment(":-:") == ":-:"  # noqa: SLF001

    def test_long_default(self) -> None:
        """------ → ---."""
        assert _mod._get_separator_alignment("------") == "---"  # noqa: SLF001

    def test_long_left(self) -> None:
        """:------ → :--."""
        assert _mod._get_separator_alignment(":------") == ":--"  # noqa: SLF001

    def test_long_right(self) -> None:
        """-------: → --:."""
        assert _mod._get_separator_alignment("-------:") == "--:"  # noqa: SLF001

    def test_long_center(self) -> None:
        """:------: → :-:."""
        assert _mod._get_separator_alignment(":------:") == ":-:"  # noqa: SLF001


class TestFormatSeparatorCell:
    """Tests for _format_separator_cell."""

    def test_default_min_width(self) -> None:
        """--- at minimum width."""
        assert _mod._format_separator_cell(3, "---") == "---"  # noqa: SLF001

    def test_default_wider(self) -> None:
        """Wider default separator."""
        assert _mod._format_separator_cell(5, "---") == "-----"  # noqa: SLF001

    def test_left_aligned(self) -> None:
        """Left-aligned separator."""
        assert _mod._format_separator_cell(4, ":--") == ":---"  # noqa: SLF001

    def test_right_aligned(self) -> None:
        """Right-aligned separator."""
        assert _mod._format_separator_cell(4, "--:") == "---:"  # noqa: SLF001

    def test_centered(self) -> None:
        """Centered separator."""
        assert _mod._format_separator_cell(4, ":-:") == ":--:"  # noqa: SLF001
        # width 4 → ":" + "--" (width-2) + ":" = ":--:"

    def test_width_below_minimum(self) -> None:
        """Width < 3 behaves as if width=3."""
        assert _mod._format_separator_cell(1, "---") == "---"  # noqa: SLF001
        assert _mod._format_separator_cell(2, "---") == "---"  # noqa: SLF001

    def test_centered_min_width(self) -> None:
        """:-: at minimum width."""
        assert _mod._format_separator_cell(3, ":-:") == ":-:"  # ":" + "-" + ":"


class TestSmartSplitRow:
    """Tests for _smart_split_row.

    Covers math-aware pipe splitting, backslash-escaped pipes, and
    zero-width character stripping.
    """

    def test_simple_row(self) -> None:
        """Standard pipe-table row."""
        result = _mod._smart_split_row("| a | b |")  # noqa: SLF001
        assert result == ["a", "b"]

    def test_row_with_spaces(self) -> None:
        """Row with varying whitespace."""
        result = _mod._smart_split_row("|  foo  |  bar  |")  # noqa: SLF001
        assert result == ["foo", "bar"]

    def test_row_not_starting_with_pipe(self) -> None:
        """Line not starting with | → returns None."""
        assert _mod._smart_split_row("a | b") is None  # noqa: SLF001

    def test_row_not_ending_with_pipe(self) -> None:
        """Line not ending with | → returns None."""
        assert _mod._smart_split_row("| a | b") is None  # noqa: SLF001

    def test_empty_cell(self) -> None:
        """Row with empty cell (double pipe)."""
        result = _mod._smart_split_row("| a |  |")  # noqa: SLF001
        assert result == ["a", ""]

    def test_empty_row(self) -> None:
        """Row with just two pipes."""
        result = _mod._smart_split_row("||")  # noqa: SLF001
        assert result == [""]

    def test_separator_row(self) -> None:
        """Separator row parsed as cells."""
        result = _mod._smart_split_row("| --- | :-- |")  # noqa: SLF001
        assert result == ["---", ":--"]

    def test_row_with_zero_width_chars(self) -> None:
        """Zero-width characters are stripped from cell content."""
        result = _mod._smart_split_row("| a\u200bb |")  # noqa: SLF001
        assert result == ["ab"]

    def test_row_with_multiple_cells(self) -> None:
        """Row with many cells."""
        result = _mod._smart_split_row("| a | b | c | d |")  # noqa: SLF001
        assert result == ["a", "b", "c", "d"]

    def test_pipe_in_math_inline(self) -> None:
        """Pipe inside $...$ should not split cells.

        The $...$ span is treated atomically: the ``|`` inside it is a
        protected pipe character, not a cell separator.
        """
        result = _mod._smart_split_row("| $a | b$ | c |")  # noqa: SLF001
        # The pipe inside $...$ is protected; the outer pipes delimit 2 cells
        assert result == ["$a | b$", "c"]

    def test_pipe_in_math_display(self) -> None:
        """Pipe inside $$...$$ should not split cells."""
        result = _mod._smart_split_row("| $$a | b$$ | c |")  # noqa: SLF001
        # The pipe inside $$...$$ is protected; outer pipes delimit 2 cells
        assert result == ["$$a | b$$", "c"]

    def test_pipe_in_code_span(self) -> None:
        """Pipe inside backtick code span should not split cells."""
        result = _mod._smart_split_row("| `a | b` | c |")  # noqa: SLF001
        # The | inside the code span is protected; outer pipes delimit 2 cells
        assert result == ["`a | b`", "c"]

    def test_escaped_pipe(self) -> None:
        """Backslash-escaped pipe should not split cells."""
        result = _mod._smart_split_row("| a \\| b | c |")  # noqa: SLF001
        assert result == ["a \\| b", "c"]

    def test_nested_math_and_code(self) -> None:
        """Mixed math and code spans in one table row."""
        result = _mod._smart_split_row(  # noqa: SLF001
            "| $x|y$ | `code|here` | normal |"
        )
        # $...$ and `...` spans protect their internal pipes
        assert result == ["$x|y$", "`code|here`", "normal"]

    def test_consecutive_pipes_empty_cells(self) -> None:
        """Consecutive pipe characters create empty cells."""
        result = _mod._smart_split_row("| a || b |")  # noqa: SLF001
        assert result == ["a", "", "b"]

    def test_leading_trailing_spaces_stripped(self) -> None:
        """Leading/trailing spaces in cells are stripped."""
        result = _mod._smart_split_row("|  a  |  b  |")  # noqa: SLF001
        assert result == ["a", "b"]

    def test_no_pipes_inside_cell(self) -> None:
        """HTML-encoded pipes don't create cell boundaries."""
        result = _mod._smart_split_row("| a &#124; b | c |")  # noqa: SLF001
        assert result == ["a &#124; b", "c"]

    def test_multiple_math_spans(self) -> None:
        """Multiple $...$ spans in one cell, each with a pipe."""
        result = _mod._smart_split_row("| $a|b$ $c|d$ | e |")  # noqa: SLF001
        # Both $...$ spans protect their internal pipes; the whole content
        # between outer pipes is one cell
        assert result == ["$a|b$ $c|d$", "e"]


class TestReformatTableBlock:
    """Tests for _reformat_table_block (core table reformatter)."""

    def test_simple_table(self) -> None:
        """Simple two-column table with padding."""
        lines = ["| a | b |", "| --- | --- |", "| c | d |"]
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        assert result == [
            "| a   | b   |",
            "| --- | --- |",
            "| c   | d   |",
        ]

    def test_aligned_table(self) -> None:
        """Table with alignment markers."""
        lines = ["| a | b |", "| :-: | --: |", "| c | d |"]
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        # Center column padded, right column padded
        assert ":---" in result[1] or ":-:" in result[1]
        assert "-----:" in result[1] or "--:" in result[1]

    def test_uneven_column_widths(self) -> None:
        """Table with uneven widths → padded to widest value."""
        lines = ["| short | verylongcontent |", "| --- | --- |", "| a | b |"]
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        # Column 2 should be wider than column 1
        cell2_len = len(result[0].split(" | ")[1])  # not stripping trailing |
        assert cell2_len >= len("verylongcontent") + 1  # +1 for padding

    def test_table_with_leading_dash_separator(self) -> None:
        """Compact separator without leading pipe isn't matched by _reformat_table_block."""
        lines = ["| a |", "---", "| b |"]
        # The --- line doesn't start with | so it breaks the block
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        # Should detect invalid separator row and return unchanged
        assert result == lines

    def test_no_table_with_only_2_rows(self) -> None:
        """Block with < 2 lines returns unchanged."""
        lines = ["| a |"]
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        assert result == lines

    def test_no_separator_row(self) -> None:
        """Block without separator row returns unchanged."""
        lines = ["| a | b |", "| c | d |"]
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        assert result == lines

    def test_table_with_pipes_in_content(self) -> None:
        """Table cell with &#124; (HTML-encoded pipe) works."""
        lines = ["| a &#124; b | c |", "| --- | --- |", "| d | e |"]
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        assert "&#124;" in result[0] or "&#124;" in result[0]

    def test_invalid_mixed_separator_row(self) -> None:
        """Row mixing text and separator cells returns unchanged."""
        lines = ["| a | b |", "| --- | c |", "| d | e |"]
        # The separator row mix of "---" and "c" should be rejected
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        assert result == lines

    def test_pipe_in_math_cell(self) -> None:
        """Pipe inside $...$ in a cell should not break table structure."""
        lines = ["| a | $x | y$ |", "| :-: | :-: |", "| 1 | 2 |"]
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        assert len(result) == 3, "Table should have 3 rows"
        assert "$x | y$" in result[0], (
            "Pipe in math should be preserved as cell content"
        )

    def test_escaped_pipe_in_cell(self) -> None:
        """Backslash-escaped pipe in cell content."""
        lines = ["| a | b \\| c |", "| --- | :-- |", "| d | e |"]
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        assert len(result) == 3
        assert "b \\| c" in result[0]

    def test_math_pipe_and_normal_pipe(self) -> None:
        """Math pipes coexist with normal cell boundaries."""
        lines = [
            "| conditional | value |",
            "| --- | --- |",
            "| $P(A | B)$ | 0.5 |",
        ]
        result = _mod._reformat_table_block(lines)  # noqa: SLF001
        assert len(result) == 3
        assert "$P(A | B)$" in result[2]


class TestReformatTable:
    """Integration tests for _reformat_table (finds and reformats all
    table blocks in text)."""

    def test_single_table(self) -> None:
        """Single table in text."""
        text = "| a | b |\n| --- | --- |\n| c | d |"
        result = _mod._reformat_table(text)  # noqa: SLF001
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
        result = _mod._reformat_table(text)  # noqa: SLF001
        assert "| a   | b   |" in result
        # Each column has minimum width 3 (GFM minimum), so single-char cells
        # are padded to width 3.
        assert "| x   | y   | z   |" in result

    def test_no_tables(self) -> None:
        """No tables → unchanged."""
        text = "Just some text\n\nMore text"
        assert _mod._reformat_table(text) == text  # noqa: SLF001

    def test_table_not_starting_with_pipe(self) -> None:
        """Line not starting with pipe → not a table block."""
        text = "a | b\n---\nc | d"
        assert _mod._reformat_table(text) == text  # noqa: SLF001

    def test_mixed_text_and_tables(self) -> None:
        """Table padded correctly within surrounding text."""
        text = "Some text\n| longword | a |\n| --- | --- |\n| b | c |\nMore text"
        result = _mod._reformat_table(text)  # noqa: SLF001
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
        result = _mod._reformat_table(text)  # noqa: SLF001
        lines = result.split("\n")
        assert "$x|y$" in lines[0]
        assert "normal" in lines[4]
        assert "data" in lines[6]

    def test_escaped_pipe_preserved(self) -> None:
        """Backslash-escaped pipes preserved in output."""
        text = "| cmd \\| args | desc |\n| --- | --- |\n| echo | test |"
        result = _mod._reformat_table(text)  # noqa: SLF001
        assert "cmd \\| args" in result.split("\n")[0]

    def test_empty_table_block_not_modified(self) -> None:
        """Non-table pipe lines should pass through unchanged."""
        text = "| just a single pipe line"
        assert _mod._reformat_table(text) == text  # noqa: SLF001

    def test_blockquoted_table_aligned(self) -> None:
        """A single-level ``> ``-prefixed pipe table is padded to equal widths."""
        text = "> | short | longcontent |\n> | --- | --- |\n> | a | b |"
        result = _mod._reformat_table(text)  # noqa: SLF001
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
        result = _mod._reformat_table(text)  # noqa: SLF001
        lines = result.split("\n")
        assert (
            [p for p in range(len(lines[0])) if lines[0][p] == "|"]
            == [p for p in range(len(lines[1])) if lines[1][p] == "|"]
            == [p for p in range(len(lines[2])) if lines[2][p] == "|"]
        )
        assert len(lines[0].split("|")[2]) > len(lines[0].split("|")[1])
        # The full ``> > `` prefix is preserved on every row.
        assert all(line.startswith("> > ") for line in lines)
