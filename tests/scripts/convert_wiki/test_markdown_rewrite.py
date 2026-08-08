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

    def test_rewrite_parenthetical_stem(self) -> None:
        """Parentheses in .md link targets must not truncate rewriting."""
        text = "See [exp](Exponential%20map%20(Lie%20group).md)."
        rewritten = _rewrite_markdown_links(
            text,
            {"Exponential map (Lie group)": "exponential map (Lie group)"},
        )
        assert rewritten == "See [exp](exponential%20map%20(Lie%20group).md)."

    def test_rewrite_parenthetical_with_fragment(self) -> None:
        """Fragments on parenthetical stems should survive rewriting."""
        text = "See [x](foo%20(bar).md#sec)."
        rewritten = _rewrite_markdown_links(
            text,
            {"foo (bar)": "Foo (bar)"},
        )
        assert rewritten == "See [x](Foo%20(bar).md#sec)."

    def test_rewrite_multiple_links_one_parenthetical(self) -> None:
        """Only matching parenthetical links should migrate."""
        text = "[a](Exponential%20map%20(Lie%20group).md) [b](modern%20physics.md)"
        rewritten = _rewrite_markdown_links(
            text,
            {
                "Exponential map (Lie group)": "exponential map (Lie group)",
                "modern physics": "Modern physics",
            },
        )
        assert (
            rewritten == "[a](exponential%20map%20(Lie%20group).md) "
            "[b](Modern%20physics.md)"
        )

    def test_rewrite_preserves_flashcard_with_parenthetical(self) -> None:
        """Flashcard wrappers with parenthetical links should rewrite targets."""
        text = "{@{See [exp](Exponential%20map%20(Lie%20group).md)}@}"
        rewritten = _rewrite_markdown_links(
            text,
            {"Exponential map (Lie group)": "exponential map (Lie group)"},
        )
        assert rewritten == "{@{See [exp](exponential%20map%20(Lie%20group).md)}@}"

    def test_rewrite_skips_non_md_links(self) -> None:
        """Non-markdown URLs should be left unchanged."""
        text = "See [site](https://example.com) for details."
        rewritten = _rewrite_markdown_links(
            text,
            {"example": "Example"},
        )
        assert rewritten == text


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
