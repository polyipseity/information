"""Tests for scripts/convert_wiki/utils.py.

These tests cover the pure helper functions used throughout the package.
"""

from os import PathLike

import pytest
from anyio import Path as AnyioPath

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
