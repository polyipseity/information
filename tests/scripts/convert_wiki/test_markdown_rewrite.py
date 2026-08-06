"""Tests for scripts.convert_wiki.markdown_rewrite."""

from scripts.convert_wiki.markdown_rewrite import (
    _rewrite_article_heading,
    _rewrite_markdown_links,
)

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestRewriteMarkdownLinks:
    """Tests for _rewrite_markdown_links."""

    def test_rewrite_link_target(self) -> None:
        """Should rewrite encoded markdown link targets."""
        text = "See [physics](modern%20physics.md) for details."
        rewritten = _rewrite_markdown_links(
            text,
            {"modern physics": "Modern physics"},
        )
        assert rewritten == "See [physics](Modern%20physics.md) for details."

    def test_rewrite_preserves_fragment(self) -> None:
        """Fragments should survive link rewrites."""
        text = "See [physics](modern%20physics.md#section)."
        rewritten = _rewrite_markdown_links(
            text,
            {"modern physics": "Modern physics"},
        )
        assert rewritten == "See [physics](Modern%20physics.md#section)."

    def test_rewrite_preserves_flashcard_markup(self) -> None:
        """Flashcard wrappers should remain intact while links inside change."""
        text = "{@{See [physics](modern%20physics.md)}@}"
        rewritten = _rewrite_markdown_links(
            text,
            {"modern physics": "Modern physics"},
        )
        assert rewritten == "{@{See [physics](Modern%20physics.md)}@}"


class TestRewriteArticleHeading:
    """Tests for _rewrite_article_heading."""

    def test_rewrites_first_heading(self) -> None:
        """Should replace the first markdown heading."""
        text = "# modern physics\n\nBody."
        rewritten = _rewrite_article_heading(text, "Modern physics")
        assert rewritten.startswith("# Modern physics\n")

    def test_preserves_frontmatter(self) -> None:
        """YAML frontmatter should be preserved."""
        text = "---\naliases:\n  - modern physics\n---\n\n# modern physics\n"
        rewritten = _rewrite_article_heading(text, "Modern physics")
        assert (
            "---\naliases:\n  - modern physics\n---\n\n# Modern physics\n" == rewritten
        )
