"""Tests for the question-block shape rules.

Each test builds a minimal note and checks one rule's verdict, so a rule that
stops catching its shape fails here rather than in a course note.
"""

from pathlib import Path
from typing import cast

from main_mods.models import AstNode, Frontmatter, ValidationContext
from main_mods.question_blocks import (
    answer_explanation_shape,
    answer_solution_names_option,
    answer_solution_one_cloze,
    cloze_giant,
    question_block_fence_nested,
    question_block_figure_missing,
    question_block_label,
    question_block_options_lettered,
    question_block_options_unordered,
    question_block_rule_missing,
    question_block_subquestion_label,
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

"""A block whose question lists numbered choices and whose answer names one."""
CHOICES = """> Which book describes the state?
>
> 1. (a)
> 2. (b)
> 3. (c)
>
> ---
>
> - solution: {@{3. (c)}@}
"""

"""A block whose official key accepts two of its choices."""
TWO_ANSWERS = """> Which price does the sell print at?
>
> 1. 116 dollars
> 2. 115 dollars
> 3. 114 dollars
>
> ---
>
> - solution: {@{2. 115 dollars and 3. 114 dollars}@}
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


def test_question_block_figure_missing_fires_without_the_figure():
    """A block that asks about Figure 3 is read alone, so it carries one."""
    text = """> Consider the book in Figure 3. Which candidate matches?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{1. (a)}@}
"""
    errors = question_block_figure_missing(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_figure_missing"]
    assert "Figure 3" in errors[0].msg


def test_question_block_figure_missing_silent_with_the_figure():
    """An image at blockquote level is the block's own copy of the figure."""
    text = """> Consider the book in Figure 3. Which candidate matches?
>
> ![the three candidate books](attachments/book.png)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    assert not question_block_figure_missing(make_ctx(text))


def test_question_block_subquestion_label_fires_on_a_bare_label():
    """'(b)' names no question, and the card shows the block alone."""
    text = """> (b) (3pt) Suppose the IOC arrives. What is the last price?
>
> 1. 116 dollars
> 2. 115 dollars
>
> ---
>
> - solution: {@{2. 115 dollars}@}
"""
    errors = question_block_subquestion_label(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_subquestion_label"]
    assert "5.a." in errors[0].msg


def test_question_block_subquestion_label_fires_on_a_bare_roman_numeral():
    """'(iv)' names no question, as '(b)' does."""
    text = """> (iv) (2pt) Which book holds the order?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    errors = question_block_subquestion_label(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_subquestion_label"]
    assert "5.a." in errors[0].msg


def test_question_block_subquestion_label_fires_on_a_parenthesised_path():
    """'5(a)' brackets the sub-part, and the label is the path '5.a.'."""
    text = """> 5(a) (2pt) Which one holds?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    errors = question_block_subquestion_label(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_subquestion_label"]
    assert "5.a." in errors[0].msg


def test_question_block_subquestion_label_fires_on_a_capital_numeral():
    """'5.A.' puts the sub-part in upper case, while the label is lower-case."""
    text = """> 5.A. (2pt) Which one holds?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    errors = question_block_subquestion_label(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_subquestion_label"]
    assert "lower-case" in errors[0].msg


def test_question_block_subquestion_label_fires_on_a_missing_trailing_dot():
    """'5.a' stops short of the dot that closes the label."""
    text = """> 5.a (2pt) Which one holds?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    errors = question_block_subquestion_label(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_subquestion_label"]
    assert "5.a." in errors[0].msg


def test_question_block_subquestion_label_fires_on_an_unescaped_numeral():
    """'3.' opens a top-level question, and the numeral owes the escape."""
    text = """> 3. Suppose the market opens. Which book matches?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    errors = question_block_subquestion_label(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_subquestion_label"]
    assert "escapes its numeral" in errors[0].msg
    assert "`3\\.`" in errors[0].msg
    assert "5.a." not in errors[0].msg


def test_question_block_subquestion_label_silent_on_an_escaped_numeral():
    """'3\\\\.' is a top-level question's own number, escaped."""
    text = """> 3\\. Suppose the market opens. Which book matches?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    assert not question_block_subquestion_label(make_ctx(text))


def test_question_block_subquestion_label_silent_on_a_unified_label():
    """'5.a.' is the parent number, a dot, the sub-part and a dot."""
    text = """> 5.a. (2pt) Which one holds?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    assert not question_block_subquestion_label(make_ctx(text))


def test_question_block_subquestion_label_silent_on_labelled_blocks():
    """A first line opening on a number, a path or a choice is labelled."""
    for opening in ("5\\. (2pt) Consider", "10.c. (2pt) Consider", "1. (a)"):
        text = f"""> {opening} the book.
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {{@{{1. (a)}}@}}
"""
        assert not question_block_subquestion_label(make_ctx(text))

    # A block carrying no answer is prose, whatever its first line opens on.
    assert not question_block_subquestion_label(
        make_ctx("> (a) Mentioned in passing.\n")
    )


def test_question_block_subquestion_label_silent_on_a_roman_numeral():
    """'9.iv.' carries a roman numeral where a single letter would sit."""
    text = """> 9.iv. (4pt) Suppose the value is two. Which one holds?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    assert not question_block_subquestion_label(make_ctx(text))


def test_question_block_subquestion_label_silent_among_a_choice_list():
    """A '5.a.' opening is no numbered choice and no nested item."""
    ctx = make_ctx(
        """> 5.a. (2pt) Which one holds?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    )
    assert not question_block_subquestion_label(ctx)
    assert not question_block_options_unordered(ctx)
    assert not question_block_options_lettered(ctx)
    assert not answer_solution_names_option(ctx)


def test_question_block_subquestion_label_fires_on_a_bare_label_below_a_stem():
    """A stem above '(a)' keeps the label out of the card that shows the block."""
    text = """> Consider the order book in Figure 4. Assume the NBBO is 114 and 115.
>
> (a) (2pt) Which one holds?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    errors = question_block_subquestion_label(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_subquestion_label"]
    assert "opens its own block" in errors[0].msg
    assert "restate the premises" in errors[0].msg
    assert errors[0].line == 3


def test_question_block_subquestion_label_fires_on_a_unified_label_below_a_stem():
    """'5.a.' below a stem is the right form in the wrong place."""
    text = """> Consider the order book in Figure 4.
>
> 5.a. (2pt) Which one holds?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    errors = question_block_subquestion_label(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_subquestion_label"]
    assert "opens its own block" in errors[0].msg
    assert errors[0].line == 3


def test_question_block_subquestion_label_fires_on_a_parenthesised_path_below_a_stem():
    """'5(a)' below a stem owes the block, whichever way its form is read."""
    text = """> Consider the order book in Figure 4.
>
> 5(a) (2pt) Which one holds?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    errors = question_block_subquestion_label(make_ctx(text))
    assert [e.rule_id for e in errors] == ["question_block_subquestion_label"]
    assert "opens its own block" in errors[0].msg
    assert errors[0].line == 3


def test_question_block_subquestion_label_fires_on_a_defective_label_below_a_stem():
    """'5.A.' and '5.a' owe their own form's message below a stem as above one."""
    for label in ("5.A.", "5.a"):
        text = f"""> Consider the order book in Figure 4.
>
> {label} (2pt) Which one holds?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {{@{{2. (b)}}@}}
"""
        errors = question_block_subquestion_label(make_ctx(text))
        assert [e.rule_id for e in errors] == ["question_block_subquestion_label"]
        assert "a dot again" in errors[0].msg
        assert errors[0].line == 3


def test_question_block_subquestion_label_silent_on_a_choice_below_a_stem():
    """A choice list opens on a digit and a dot, which is no subquestion label."""
    text = """> Consider the order book in Figure 4. Which one holds?
>
> 1. (a)
> 2. (b)
> 3. (c)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    assert not question_block_subquestion_label(make_ctx(text))


def test_question_block_subquestion_label_silent_on_a_label_in_a_fence():
    """A line inside a fenced code block is code, not a label's line."""
    text = """> Consider the order book below. Which one holds?
>
> ```text
> (a) the first line of the file
> ```
>
> ---
>
> - solution: {@{The first block}@}
"""
    assert not question_block_subquestion_label(make_ctx(text))


def test_question_block_subquestion_label_silent_on_a_labelled_opener_above_a_stem():
    """A block opening '> 5.a.' reads the label first, whatever follows it."""
    text = """> 5.a. (2pt) Consider the order book in Figure 4. Assume the NBBO is 114
> and 115 dollars, and that you placed a P-peg buy order for 100 shares.
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{2. (b)}@}
"""
    assert not question_block_subquestion_label(make_ctx(text))


def test_answer_solution_names_option_silent_on_a_subquestion_label():
    """A free-response block labelled '5.a.' lists no choice to name."""
    text = """> 5.a. (2pt) Which one holds?
>
> ---
>
> - solution: {@{One permit}@}
"""
    assert not answer_solution_names_option(make_ctx(text))


def test_answer_solution_names_option_silent_on_named_choice():
    """A solution naming the choice's number and text answers the block."""
    assert not answer_solution_names_option(make_ctx(CHOICES))


def test_answer_solution_names_option_silent_on_two_options_joined_by_and():
    """A key that accepts two options names both, inside the one cloze."""
    assert not answer_solution_names_option(make_ctx(TWO_ANSWERS))
    assert not answer_solution_one_cloze(make_ctx(TWO_ANSWERS))


def test_answer_solution_names_option_silent_on_two_options_joined_by_a_comma():
    """A comma joins two names as 'and' does."""
    text = TWO_ANSWERS.replace(
        "{@{2. 115 dollars and 3. 114 dollars}@}",
        "{@{2. 115 dollars, 3. 114 dollars}@}",
    )
    assert not answer_solution_names_option(make_ctx(text))


def test_answer_solution_names_option_silent_on_three_options():
    """Three names run on one line, the last joined by ', and'."""
    text = """> Which price does the sell print at?
>
> 1. 116 dollars
> 2. 115 dollars
> 3. 114 dollars
> 4. 113 dollars
>
> ---
>
> - solution: {@{2. 115 dollars, 3. 114 dollars, and 4. 113 dollars}@}
"""
    assert not answer_solution_names_option(make_ctx(text))


def test_answer_solution_names_option_fires_on_a_second_wrong_text():
    """Every name is checked, not just the first."""
    text = """> Which price does the sell print at?
>
> 1. 116 dollars
> 2. 115 dollars
> 3. 114 dollars
>
> ---
>
> - solution: {@{2. 115 dollars and 3. 116 dollars}@}
"""
    errors = answer_solution_names_option(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_names_option"]
    assert "choice 3" in errors[0].msg


def test_answer_solution_names_option_fires_on_a_second_unlisted_number():
    """A later name is held to the block's list like the first."""
    text = """> Which price does the sell print at?
>
> 1. 116 dollars
> 2. 115 dollars
>
> ---
>
> - solution: {@{1. 116 dollars and 4. 113 dollars}@}
"""
    errors = answer_solution_names_option(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_names_option"]
    assert "choice 4" in errors[0].msg


def test_answer_solution_names_option_fires_on_a_bare_number_list():
    """Naming options means '<number>. <text>' each, never a number list."""
    text = """> Which price does the sell print at?
>
> 1. 116 dollars
> 2. 115 dollars
> 3. 114 dollars
>
> ---
>
> - solution: {@{2 and 3}@}
"""
    errors = answer_solution_names_option(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_names_option"]
    assert "no choice marker" in errors[0].msg


def test_answer_solution_names_option_silent_on_math_choice():
    """Inline math stays part of the choice's text on both lines."""
    text = """> Which expression gives the posterior?
>
> 1. $\\delta$
> 2. $\\frac{4\\delta}{1 + 3\\delta}$
>
> ---
>
> - solution: {@{2. $\\frac{4\\delta}{1 + 3\\delta}$}@}
"""
    assert not answer_solution_names_option(make_ctx(text))


def test_answer_solution_names_option_fires_on_missing_number():
    """Prose naming the answer without its choice number names no option."""
    text = """> Which book describes the state?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{the second book}@}
"""
    errors = answer_solution_names_option(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_names_option"]
    assert "no choice marker" in errors[0].msg


def test_answer_solution_names_option_fires_on_unlisted_number():
    """A number the block's list does not hold names no option."""
    text = """> Which book describes the state?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{3. (c)}@}
"""
    errors = answer_solution_names_option(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_names_option"]
    assert "choice 3" in errors[0].msg


def test_answer_solution_names_option_fires_on_another_choice_text():
    """The right number with another choice's text still names no option."""
    text = """> Which book describes the state?
>
> 1. (a)
> 2. (b)
> 3. (c)
>
> ---
>
> - solution: {@{2. (c)}@}
"""
    errors = answer_solution_names_option(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_names_option"]
    assert "choice 2" in errors[0].msg


def test_answer_solution_names_option_fires_on_an_opening_quantity():
    """A quantity opens no choice, so it reports as a missing choice marker."""
    text = """> Which book describes the state?
>
> 1. (a)
> 2. (b)
> 3. (c)
>
> ---
>
> - solution: {@{30 shares remain offered at 116 dollars}@}
"""
    errors = answer_solution_names_option(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_names_option"]
    assert "no choice marker" in errors[0].msg


def test_answer_solution_names_option_fires_on_the_number_outside_the_cloze():
    """A card showing '{@{3}@}. (c)' shows the very text it asks the reader for."""
    text = """> Which book describes the state?
>
> 1. (a)
> 2. (b)
> 3. (c)
>
> ---
>
> - solution: {@{3}@}. (c)
"""
    errors = answer_solution_names_option(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_names_option"]
    assert "leaves text outside it" in errors[0].msg


def test_answer_solution_names_option_fires_on_the_text_outside_the_cloze():
    """The number outside the cloze leaves the choice's own text visible."""
    text = """> Which book describes the state?
>
> 1. (a)
> 2. (b)
> 3. (c)
>
> ---
>
> - solution: 3. {@{(c)}@}
"""
    errors = answer_solution_names_option(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_names_option"]
    assert "leaves text outside it" in errors[0].msg


def test_answer_solution_names_option_silent_on_trailing_punctuation():
    """A full stop belongs to the sentence, so it sits outside the cloze."""
    text = """> Which book describes the state?
>
> 1. (a)
> 2. (b)
> 3. (c)
>
> ---
>
> - solution: {@{3. (c)}@}.
"""
    assert not answer_solution_names_option(make_ctx(text))


def test_answer_solution_names_option_silent_without_a_cloze():
    """A solution carrying no cloze is the one-cloze rule's to report."""
    text = """> Which book describes the state?
>
> 1. (a)
> 2. (b)
> 3. (c)
>
> ---
>
> - solution: 3. (c)
"""
    assert not answer_solution_names_option(make_ctx(text))


def test_answer_solution_names_option_silent_without_a_choice_list():
    """A block that lists no choices is a free-response question."""
    assert not answer_solution_names_option(make_ctx(HOUSE))


def test_answer_solution_one_cloze_silent_on_one_cloze():
    """One cloze holding the option is the shape the rule asks for."""
    assert not answer_solution_one_cloze(make_ctx(CHOICES))


def test_answer_solution_one_cloze_fires_on_two_clozes():
    """A second cloze makes the solution two cards."""
    text = """> Which book describes the state?
>
> ---
>
> - solution: {@{3. (c)}@}, {@{the only one that rests the order}@}
"""
    errors = answer_solution_one_cloze(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_one_cloze"]
    assert "carries 2" in errors[0].msg


def test_answer_solution_one_cloze_fires_on_no_cloze():
    """A solution with no cloze leaves the card nothing to recall."""
    text = """> Which book describes the state?
>
> ---
>
> - solution: 3. (c)
"""
    errors = answer_solution_one_cloze(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_solution_one_cloze"]
    assert "carries none" in errors[0].msg


def test_answer_solution_one_cloze_leaves_a_wrong_number_to_the_naming_rule():
    """One cloze naming an unlisted choice reports naming only, without a crash."""
    text = """> Which book describes the state?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {@{9. (z)}@}
"""
    ctx = make_ctx(text)
    assert not answer_solution_one_cloze(ctx)
    assert [e.rule_id for e in answer_solution_names_option(ctx)] == [
        "answer_solution_names_option"
    ]


def test_answer_explanation_shape_silent_on_a_short_whole_cloze():
    """Fifteen prose words in one cloze is the shape the short branch asks for."""
    text = (
        "> Which book describes the state?\n"
        ">\n"
        "> ---\n"
        ">\n"
        "> - explanation: "
        "{@{The 30 unfilled shares cancel, and the buy rests 80 bid at 115, "
        "a level no listed book shows.}@}\n"
    )
    assert not answer_explanation_shape(make_ctx(text))
    assert not cloze_giant(make_ctx(text))


def test_answer_explanation_shape_fires_on_a_visible_lead_in():
    """A short explanation is one cloze whole, so text beside it reports the shape."""
    text = (
        "> Which book describes the state?\n"
        ">\n"
        "> ---\n"
        ">\n"
        "> - explanation: "
        "The 30 unfilled shares {@{cancel, and the buy rests 80 bid at 115, "
        "a level no listed book shows}@}.\n"
    )
    errors = answer_explanation_shape(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_explanation_shape"]
    assert "whole line in one cloze" in errors[0].msg
    assert "punctuation inside" in errors[0].msg


def test_answer_explanation_shape_leaves_a_long_whole_cloze_to_the_cap():
    """Past twenty words a whole cloze meets the floor, and the word cap catches it."""
    text = (
        "> Which book describes the state?\n"
        ">\n"
        "> ---\n"
        ">\n"
        "> - explanation: "
        "{@{The sell takes the ten shares bid at the top of the book and the "
        "remainder rests at the price the buy order named, so the last traded "
        "price never leaves the range the question shows and no other book in "
        "the figure matches the state.}@}\n"
    )
    assert not answer_explanation_shape(make_ctx(text))
    errors = cloze_giant(make_ctx(text))
    assert [e.rule_id for e in errors] == ["cloze_giant"]


def test_answer_explanation_shape_silent_on_the_long_branch():
    """Thirty words in three short clozes is the shape the long branch asks for."""
    text = (
        "> Which book describes the state?\n"
        ">\n"
        "> ---\n"
        ">\n"
        "> - explanation: "
        "{@{The sell takes shares bid at the top of the book}@} and "
        "{@{the remainder rests at the price the buy order named}@}, "
        "{@{so the traded price never leaves the range}@}.\n"
    )
    assert not answer_explanation_shape(make_ctx(text))
    assert not cloze_giant(make_ctx(text))


def test_answer_explanation_shape_fires_below_the_floor():
    """A long explanation hiding 60% leaves the rest of its reasoning to read."""
    text = (
        "> Which book describes the state?\n"
        ">\n"
        "> ---\n"
        ">\n"
        "> - explanation: "
        "{@{The sell takes shares bid}@} at the top of the book and "
        "{@{the remainder rests at the price}@} the buy order named, so "
        "{@{the traded price never leaves the range}@}.\n"
    )
    errors = answer_explanation_shape(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_explanation_shape"]
    assert "clozes 60% of its words" in errors[0].msg
    assert "at least 85%" in errors[0].msg
    assert "at most 12 words each" in errors[0].msg


def test_answer_explanation_shape_fires_on_no_cloze():
    """An explanation with no cloze hides nothing on a line shown as a card."""
    text = """> Which book describes the state?
>
> ---
>
> - explanation: The sell takes the ten shares bid at the top of the book.
"""
    errors = answer_explanation_shape(make_ctx(text))
    assert [e.rule_id for e in errors] == ["answer_explanation_shape"]


def test_cloze_giant_fires_past_the_cap():
    """A wrapped continuation line carries no label, so its long cloze is split."""
    long_cloze = (
        "the first reader to arrive takes the data lock on behalf of every reader"
    )
    text = f"""> Who takes the data lock?
>
> ---
>
> - explanation: the lock is taken by
>   {{@{{{long_cloze}}}@}} so the writer waits.
"""
    errors = cloze_giant(make_ctx(text))
    assert [e.rule_id for e in errors] == ["cloze_giant"]


def test_cloze_giant_silent_at_the_cap():
    """Twelve words of prose is inside the cap."""
    text = """> Who takes the data lock?
>
> ---
>
> - explanation: the lock is taken by
>   {@{the first reader to arrive takes it for the group and then}@} the last.
"""
    assert not cloze_giant(make_ctx(text))


def test_cloze_giant_silent_when_the_cloze_hides_math():
    """Math and code inside a cloze are not words of prose."""
    text = """> What is the bound?
>
> ---
>
> - explanation: the limit is
>   {@{$\\lim_{n\\to\\infty} P[|X_n - X| > \\varepsilon] = 0$ for every $\\varepsilon > 0$}@}
"""
    assert not cloze_giant(make_ctx(text))


def test_cloze_giant_silent_on_the_solution_cloze():
    """A solution's one cloze holds the whole answer, so it has no shorter form."""
    choice_text = (
        "the first reader to arrive takes the data lock on behalf of every waiting "
        "reader"
    )
    text = f"""> Who takes the data lock?
>
> 1. (a)
> 2. (b)
>
> ---
>
> - solution: {{@{{2. {choice_text}}}@}}
"""
    assert not cloze_giant(make_ctx(text))


def test_cloze_giant_silent_on_the_explanation_beside_it():
    """An explanation's one cloze holds the reasoning whole, as a solution's does."""
    long_cloze = (
        "the first reader to arrive takes the data lock on behalf of every waiting "
        "reader"
    )
    text = f"""> Who takes the data lock?
>
> ---
>
> - solution: {{@{{2. {long_cloze}}}@}}
> - explanation: {{@{{{long_cloze}}}@}}
"""
    assert not cloze_giant(make_ctx(text))


def test_cloze_giant_fires_on_a_long_explanation_piece():
    """A long explanation's ordinary cloze is capped, since it leaves text outside."""
    long_cloze = (
        "the first reader to arrive takes the data lock on behalf of every waiting"
    )
    text = f"""> Who takes the data lock?
>
> ---
>
> - explanation: {{@{{{long_cloze}}}@}} reader.
"""
    errors = cloze_giant(make_ctx(text))
    assert [e.rule_id for e in errors] == ["cloze_giant"]


def test_cloze_giant_silent_before_the_file_adopts_the_shape():
    """Legacy content keeps its long clozes until it separates question and answer."""
    text = """> Who takes the data lock?
>
> - explanation: {@{the first reader to arrive takes the data lock on behalf of every}@} reader.
"""
    assert not cloze_giant(make_ctx(text))
