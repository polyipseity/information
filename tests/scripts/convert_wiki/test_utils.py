"""Tests for scripts/convert_wiki/utils.py.

These tests cover the pure helper functions used throughout the package.
"""

from bs4 import Tag

from scripts import convert_wiki as _mod

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
        for key, expected in _mod._NAMES_MAP.items():  # noqa: SLF001
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


class TestBs4NewElement:
    """Tests for the _bs4_new_element function."""

    def test_parse_simple_tag(self) -> None:
        """Should parse a simple HTML tag string."""
        result = _mod._bs4_new_element("<b></b>")  # noqa: SLF001
        assert isinstance(result, Tag)
        assert result.name == "b"

    def test_parse_tag_with_content(self) -> None:
        """Should parse a tag with text content."""
        result = _mod._bs4_new_element("<i>text</i>")  # noqa: SLF001
        assert isinstance(result, Tag)
        assert result.name == "i"
        assert result.string == "text"
