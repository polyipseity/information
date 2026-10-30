"""Tests for the question-block shape rules.

Each test builds a minimal note and checks one rule's verdict, so a rule that
stops catching its shape fails here rather than in a course note.
"""

from pathlib import Path
from typing import cast

from main_mods.models import AstNode, Frontmatter, ValidationContext
from main_mods.question_blocks import (
    cloze_giant,
    question_block_fence_nested,
    question_block_label,
    question_block_options_lettered,
    question_block_options_unordered,
    question_block_rule_missing,
)
from main_mods.utils import _MD, FRONT_RE, parse_frontmatter, parse_session_headers
from pydantic_yaml import parse_yaml_raw_as

"""Public symbols exported by this module (none)."""
__all__ = ()


def make_ctx(text: str, name: str = "lab.md") -> ValidationContext:
    """Build a validation context for *text*, filed under *name*."""
    front = parse_frontmatter(text) or ""
    if front:
        try:
            data = parse_yaml_raw_as(Frontmatter, front)
        except Exception:  # pragma: no cover
            data = Frontmatter()
    else:
        data = Frontmatter()
    body = text
    match = FRONT_RE.match(text)
    if match:
        body = text[match.end() :]
    try:
        ast = cast("list[AstNode]", _MD(body))
    except Exception:
        ast = []
    return ValidationContext(
        path=Path("/tmp/course") / name,
        text=text,
        front=front,
        data=data,
        body=body,
        session_headers=parse_session_headers(text, ast),
        ast=ast,
    )


"""A block in the house shape: question paragraph, rule, answer items."""
HOUSE = """> What does the semaphore start at?
>
> ---
>
> - solution: {@{One permit}@}
"""

"""The older shape: a labelled question item with bulleted choices."""
LABELLED = """> - question: Which values can it hold?
>     - 1
>     - 2
> - solution: {@{Either}@}
"""


def test_question_block_label_fires_on_labelled_item():
    """A '- question:' label item is the shape the house format drops."""
    errors = question_block_label(make_ctx(LABELLED))
    assert [e.rule_id for e in errors] == ["question_block_label"]


def test_question_block_label_silent_on_house_shape():
    """A house-shaped block carries no label."""
    assert not question_block_label(make_ctx(HOUSE))


def test_question_block_label_silent_on_prose_blockquote():
    """A blockquote with no answer item is prose, whatever it opens with."""
    text = "> Question: why is the sky blue?\n"
    assert not question_block_label(make_ctx(text))


def test_question_block_fence_nested_fires_under_a_list_item():
    """A fence indented under a list item is not at blockquote level."""
    text = """> - question: What does this print?
>
>     ```c
>     int main() {}
>     ```
> - solution: {@{Nothing}@}
"""
    errors = question_block_fence_nested(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_fence_nested"]


def test_question_block_fence_nested_silent_at_blockquote_level():
    """The house shape writes the fence as '> ```'."""
    text = (
        HOUSE
        + """
> ```c
> int main() {}
> ```
"""
    )
    assert not question_block_fence_nested(make_ctx(text))


def test_question_block_options_unordered_fires_on_bulleted_choices():
    """Choices written as bullets cannot be told from the question."""
    text = """> Which values can it hold?
>
>     - 1
>     - 2
> - solution: {@{Either}@}
"""
    assert question_block_options_unordered(make_ctx(text))


def test_question_block_options_unordered_silent_under_a_sub_part():
    """A question that is itself a list drives sub-parts, not choices."""
    text = """> - (a) Consider the triangle.
>     - Define the constant.
>     - Compute the marginals.
> - solution: {@{Two}@}
"""
    assert not question_block_options_unordered(make_ctx(text))


def test_question_block_options_unordered_silent_on_numbered_choices():
    """A numbered list is the house shape for real source choices."""
    text = """> Which values can it hold?
>
>     1. 1
>     2. 2
>
> ---
>
> - solution: {@{Either}@}
"""
    assert not question_block_options_unordered(make_ctx(text))


def test_question_block_options_unordered_silent_on_roman_sub_parts():
    """A nested roman-labelled sub-part is part of the question, not a choice."""
    text = """> Consider the triangle.
>
>     - i. Find the constant.
>     - ii. Compute the marginals.
>
> ---
>
> - solution: {@{Two}@}
"""
    assert not question_block_options_unordered(make_ctx(text))


def test_question_block_options_lettered_fires_on_letter_markers():
    """Choices are numbered, so a letter marker is an error."""
    text = """> Which values can it hold?
>
>     (a) 1
>     (b) 2
>
> ---
>
> - solution: {@{Either}@}
"""
    errors = question_block_options_lettered(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_options_lettered"]


def test_question_block_options_lettered_silent_on_roman_marker():
    """A single 'i' reads as a roman numeral, so it is numbering."""
    text = """> Consider the triangle.
>
>     - i. Find the constant.
>
> ---
>
> - solution: {@{Two}@}
"""
    assert not question_block_options_lettered(make_ctx(text))


def test_question_block_options_lettered_silent_on_digit_markers():
    """Digit markers are the shape the rule asks for."""
    text = """> Which values can it hold?
>
>     1. 1
>     2. 2
>
> ---
>
> - solution: {@{Either}@}
"""
    assert not question_block_options_lettered(make_ctx(text))


def test_question_block_rule_missing_fires_on_lone_deviation():
    """One block without the rule, in a file that otherwise carries it."""
    text = (
        HOUSE
        + """
<!-- markdownlint MD028 -->

> Where does the second permit come from?
>
> - solution: {@{The first release}@}
"""
    )
    errors = question_block_rule_missing(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_rule_missing"]


def test_question_block_rule_missing_silent_when_file_never_adopts_it():
    """A file whose blocks all lack the rule is legacy content, not a slip."""
    text = """> Where does the first permit come from?
>
> - solution: {@{The initial value}@}
>
> <!-- markdownlint MD028 -->
>
> Where does the second one come from?
>
> - solution: {@{The first release}@}
"""
    assert not question_block_rule_missing(make_ctx(text))


def test_question_block_rule_missing_silent_outside_content_files():
    """A question page answers in the older layout without complaint."""
    text = (
        HOUSE
        + """
<!-- markdownlint MD028 -->

> Where does the second permit come from?
>
> - solution: {@{The first release}@}
"""
    )
    assert not question_block_rule_missing(make_ctx(text, "questions.md"))


def test_cloze_giant_fires_past_the_cap():
    """A cloze hiding more than twelve words of prose is split."""
    long_cloze = (
        "the first reader to arrive takes the data lock on behalf of every reader"
    )
    text = f"""> Who takes the data lock?
>
> ---
>
> - explanation: {{@{{{long_cloze}}}@}} so the writer waits.
"""
    errors = cloze_giant(make_ctx(text))
    assert [e.rule_id for e in errors] == ["cloze_giant"]


def test_cloze_giant_silent_at_the_cap():
    """Twelve words of prose is inside the cap."""
    text = """> Who takes the data lock?
>
> ---
>
> - explanation: {@{the first reader takes it for the group}@} and the last releases it.
"""
    assert not cloze_giant(make_ctx(text))


def test_cloze_giant_silent_when_the_cloze_hides_math():
    """Math and code inside a cloze are not words of prose."""
    text = """> What is the bound?
>
> ---
>
> - solution: {@{$\\lim_{n\\to\\infty} P[|X_n - X| > \\varepsilon] = 0$ for every $\\varepsilon > 0$}@}
"""
    assert not cloze_giant(make_ctx(text))


def test_cloze_giant_silent_before_the_file_adopts_the_shape():
    """Legacy content keeps its long clozes until it separates question and answer."""
    text = """> Who takes the data lock?
>
> - explanation: {@{the first reader to arrive takes the data lock on behalf of every}@} reader.
"""
    assert not cloze_giant(make_ctx(text))
