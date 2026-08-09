"""Tests for the ``_balance_brackets`` helper in ``scripts/convert_wiki.py``."""

import pytest

from scripts.convert_wiki.utils import _balance_brackets

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()


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
        ("see[link text](https://example.org)", "see[link text](https://example.org)"),
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
def test_balance_brackets(input_text: str, expected: str) -> None:
    """Verify bracket-balancing behaves correctly for the given case."""
    assert _balance_brackets(input_text) == expected
