"""Tests for scripts.convert_wiki.markdown_rewrite."""

from scripts.convert_wiki.markdown_rewrite import (
    _align_plain_to_raw,
    _resolve_plain_rewrite,
    _rewrite_article_heading,
    _rewrite_markdown_headings,
    _rewrite_markdown_links,
    _rewrite_plain_span,
)

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


class TestResolvePlainRewrite:
    """Tests for _resolve_plain_rewrite."""

    def test_name_map_hit(self) -> None:
        names_map = {"modern physics": "Modern physics"}
        assert _resolve_plain_rewrite("modern physics", names_map=names_map) == (
            "Modern physics"
        )

    def test_lowercase_fallback(self) -> None:
        names_map = {
            "Fourier transform": "Fourier transform",
            "fourier transform": "Fourier transform",
        }
        assert _resolve_plain_rewrite("fourier transform", names_map=names_map) == (
            "Fourier transform"
        )

    def test_migrations_on_top(self) -> None:
        names_map = {"modern physics": "modern physics"}
        migrations = {"modern physics": "Modern physics"}
        assert (
            _resolve_plain_rewrite(
                "modern physics", names_map=names_map, migrations=migrations
            )
            == "Modern physics"
        )

    def test_replace_underscores_flag(self) -> None:
        names_map = {
            "legendre transformation on manifolds": "Legendre transformation on manifolds"
        }
        assert (
            _resolve_plain_rewrite(
                "legendre_transformation_on_manifolds",
                names_map=names_map,
                replace_underscores=True,
            )
            == "Legendre transformation on manifolds"
        )

    def test_no_migrations_returns_name_map_result(self) -> None:
        names_map = {"modern physics": "Modern physics"}
        assert (
            _resolve_plain_rewrite(
                "modern physics", names_map=names_map, migrations=None
            )
            == "Modern physics"
        )


class TestRewritePlainSpan:
    """Tests for _rewrite_plain_span and_align_plain_to_raw."""

    def test_markup_free_fast_path(self) -> None:
        assert _rewrite_plain_span(
            "Modern physics", "Modern physics", "Modern physics"
        ) == ("Modern physics")

    def test_plain_equals_raw_returns_new(self) -> None:
        assert _rewrite_plain_span(
            "modern physics", "modern physics", "Modern physics"
        ) == ("Modern physics")

    def test_emphasis_stripped_raw(self) -> None:
        raw = "modern _physics_"
        assert _rewrite_plain_span(raw, "modern physics", "Modern physics") == (
            "Modern _physics_"
        )

    def test_escaped_parens_raw(self) -> None:
        raw = r"Phase space coordinates \(_p_, _q_\) and Hamiltonian _H_"
        plain = "Phase space coordinates (p, q) and Hamiltonian H"
        new = "phase space coordinates (p, q) and Hamiltonian H"
        assert _rewrite_plain_span(raw, plain, new) == (
            r"phase space coordinates \(_p_, _q_\) and Hamiltonian _H_"
        )

    def test_markup_after_plain(self) -> None:
        raw = "modern physics _and more_"
        assert _rewrite_plain_span(
            raw, "modern physics and more", "Modern physics and more"
        ) == ("Modern physics _and more_")

    def test_insert_spanning_markup(self) -> None:
        raw = "modern _physics_"
        assert _rewrite_plain_span(raw, "modern physics", "modern applied physics") == (
            "modern applied _physics_"
        )

    def test_alignment_failure_returns_raw(self) -> None:
        assert _rewrite_plain_span("abc", "xyz", "xyz") == "abc"

    def test_align_helper_subsequence(self) -> None:
        assert _align_plain_to_raw("a_b_c", "abc") == [0, 2, 4]


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

    def test_rewrite_links_with_apostrophe(self) -> None:
        """Apostrophe links should be rewritten despite mistune %27 encoding."""
        text = "[d'Alembert](Jean%20le%20Rond%20d'Alembert.md)"
        rewritten = _rewrite_markdown_links(
            text,
            {"Jean le Rond d'Alembert": "Jean Le Rond d'Alembert"},
        )
        assert rewritten == "[d'Alembert](Jean%20Le%20Rond%20d'Alembert.md)"

    def test_rewrite_links_apostrophe_no_migration_no_change(self) -> None:
        """Apostrophe links without a matching migration stay byte-identical."""
        text = "[d'Alembert](Jean%20Le%20Rond%20d'Alembert.md)"
        rewritten = _rewrite_markdown_links(
            text,
            {"modern physics": "Modern physics"},
        )
        assert rewritten == text

    def test_rewrite_links_apostrophe_fragment(self) -> None:
        """Fragments on apostrophe links should round-trip."""
        text = "[d'Alembert](Jean%20le%20Rond%20d'Alembert.md#biography)"
        rewritten = _rewrite_markdown_links(
            text,
            {"Jean le Rond d'Alembert": "Jean Le Rond d'Alembert"},
        )
        assert rewritten == "[d'Alembert](Jean%20Le%20Rond%20d'Alembert.md#biography)"


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


"""Effective name map after the test mapping merges over the base map."""
_EFFECTIVE = {
    "Modern physics": "Modern physics",
    "modern physics": "modern physics",
    "Fourier transform": "Fourier transform",
    "fourier transform": "Fourier transform",
}
"""Stem migrations implied by the effective name map."""
_MIGRATIONS = {"modern physics": "Modern physics"}


class TestRewriteMarkdownHeadings:
    """Tests for _rewrite_markdown_headings."""

    def test_rewrites_all_heading_levels(self) -> None:
        """Should re-case headings at every level ``#``-``######``."""
        text = "".join(f"{'#' * level} modern physics\n" for level in range(1, 7))
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == "".join(
            f"{'#' * level} Modern physics\n" for level in range(1, 7)
        )

    def test_migration_required_for_lowercase_variant(self) -> None:
        """The effective map alone keeps lowercase variants lowercase."""
        text = "## modern physics\n"
        assert _rewrite_markdown_headings(text, _EFFECTIVE) == text
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == "## Modern physics\n"

    def test_preserves_frontmatter_including_comments(self) -> None:
        """YAML frontmatter (even ``# comment`` lines) must stay untouched."""
        text = (
            "---\naliases:\n  - modern physics\n# comment\n---\n\n## modern physics\n"
        )
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == (
            "---\naliases:\n  - modern physics\n# comment\n---\n\n## Modern physics\n"
        )

    def test_skips_fenced_code_blocks(self) -> None:
        """``#``-lines inside fenced code must not be rewritten or steal tokens."""
        text = "```python\n# modern physics\nprint('x')\n```\n\n## modern physics\n"
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert (
            rewritten
            == "```python\n# modern physics\nprint('x')\n```\n\n## Modern physics\n"
        )

    def test_preserves_trailing_hashes(self) -> None:
        """Trailing closing ``#``s and leading markers must be kept."""
        text = "## modern physics ###\n"
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == "## Modern physics ###\n"

    def test_rewrites_duplicate_heading_text(self) -> None:
        """Every occurrence of the same heading text should be rewritten."""
        text = "## modern physics\n\nBody.\n\n### modern physics\n"
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == "## Modern physics\n\nBody.\n\n### Modern physics\n"

    def test_idempotent_on_canonical_headings(self) -> None:
        """Canonical headings under the effective map must not change."""
        text = "## Modern physics\n\n### Fourier transform\n"
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == text

    def test_rewrites_whole_link_heading(self) -> None:
        """A heading that is entirely a link rewrites its text, not the target."""
        text = "## [modern physics](modern%20physics.md)\n"
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == "## [Modern physics](modern%20physics.md)\n"

    def test_skips_partially_marked_heading(self) -> None:
        """Mixed markup headings are left untouched (plain text not contiguous)."""
        text = "## [modern physics](modern%20physics.md) notes\n"
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == text

    def test_skips_setext_and_nested_headings(self) -> None:
        """Setext, blockquote, and list headings are out of scope."""
        text = "modern physics\n---\n\n> ## modern physics\n\n- item\n  ## modern physics\n"
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == text

    def test_unchanged_for_empty_or_headingless_input(self) -> None:
        """Empty and heading-less text must round-trip unchanged."""
        assert _rewrite_markdown_headings("", _EFFECTIVE, _MIGRATIONS) == ""
        text = "Just prose.\n"
        assert _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS) == text

    def test_preserves_line_endings(self) -> None:
        """Original line endings (CRLF) must survive rewriting."""
        text = "## modern physics\r\n"
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == "## Modern physics\r\n"

    def test_empty_names_map_returns_unchanged(self) -> None:
        """An empty names map must not rewrite anything."""
        text = "## modern physics\n"
        assert _rewrite_markdown_headings(text, {}) == text

    def test_rewrites_heading_with_inline_markup(self) -> None:
        """Escaped parens and emphasis markup must be preserved while the
        plain-text projection is rewritten (the special-header case)."""
        text = "### Phase space coordinates \\(_p_, _q_\\) and Hamiltonian _H_\n"
        names_map = {
            "Phase space coordinates (p, q) and Hamiltonian H": (
                "phase space coordinates (p, q) and Hamiltonian H"
            )
        }
        rewritten = _rewrite_markdown_headings(text, names_map)
        assert rewritten == (
            "### phase space coordinates \\(_p_, _q_\\) and Hamiltonian _H_\n"
        )

    def test_rewrites_emphasis_only_heading(self) -> None:
        """A heading whose plain text is wrapped in emphasis keeps the markup."""
        text = "## _modern physics_\n"
        rewritten = _rewrite_markdown_headings(text, _EFFECTIVE, _MIGRATIONS)
        assert rewritten == "## _Modern physics_\n"

    def test_rewrites_markup_after_plain_heading(self) -> None:
        """Markup trailing the plain text is preserved on rewrite."""
        text = "## modern physics _and more_\n"
        names_map = {"modern physics and more": "Modern physics and more"}
        rewritten = _rewrite_markdown_headings(text, names_map)
        assert rewritten == "## Modern physics _and more_\n"
