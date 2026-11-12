"""Tests for the answer-line style the reference note fixed by hand.

Every fixture here is copied from the note at
``private/special/academia/HKUST/FINA 4103/assignments/homework 1/assignment.md``,
whose own lines are the style: a short answer hides its whole sentence in one
cloze, and a derivation hides each step's payload while keeping the frame that
reads it visible.  The accepted cases pin that shape and the rejected ones pin
where it stops, so a rule edited later cannot quietly drop either half.
"""

from collections.abc import Callable
from pathlib import Path as SyncPath

import pytest
from anyio import Path
from main_mods.models import Severity, ValidationContext, ValidationMessage
from main_mods.question_blocks import answer_explanation_shape, cloze_giant
from main_mods.rules import answer_formula_alone, cloze_glue
from main_mods.validator import check_markdown_file

from .test_question_blocks import make_ctx

"""Public symbols exported by this module (none)."""
__all__ = ()


"""Frontmatter that makes a fixture a flashcard-enabled academic note.

``cloze_glue`` judges only a note carrying the flashcard tag, so every fixture
carries it; a fixture without it would pass that rule by never being measured.
"""
FRONT = """---
tags:
  - flashcard/inactive/special/academia/HKUST/FINA_4103
---

"""


def note(block: str) -> str:
    """Return *block* behind the frontmatter a flashcard note opens with."""
    return FRONT + block


def repo_root() -> SyncPath:
    """Return the repository root, the nearest ancestor carrying ``AGENTS.md``."""
    for parent in SyncPath(__file__).resolve().parents:
        if (parent / "AGENTS.md").is_file():
            return parent
    raise RuntimeError("no AGENTS.md above this test file")


"""The note the answer-line style is fixed against."""
REFERENCE_NOTE = (
    repo_root()
    / "private/special/academia/HKUST/FINA 4103/assignments/homework 1/assignment.md"
)

"""Skip the golden test when this clone carries no ``private`` submodule."""
requires_reference_note = pytest.mark.skipif(
    not REFERENCE_NOTE.is_file(),
    reason="the reference note is in the private submodule, absent from a fresh clone",
)

"""The rules whose verdict the reference note's shape fixes."""
ANSWER_RULES: tuple[Callable[[ValidationContext], list[ValidationMessage]], ...] = (
    answer_explanation_shape,
    cloze_giant,
    cloze_glue,
    answer_formula_alone,
)

"""An 11-word explanation hidden whole, the note's line 111."""
ELEVEN = note(
    "> - explanation: {@{Your peg rests behind the 120 displayed at 113, "
    "hidden from general traders.}@}\n"
)

"""A 19-word explanation hidden whole, the note's line 130."""
NINETEEN = note(
    "> - explanation: {@{The peg rests at 113 behind the 120 displayed "
    "shares, so the 100-share sell fills at 113 and the peg stays "
    "untouched.}@}\n"
)

"""A 56-word derivation clozing 62% of its words, the note's line 302.

Its visible text reads ``loses . Such a fill arrives with , so the expected
loss is .``: each step's payload is hidden and the sentence frame stays.
"""
DERIVATION_56 = note(
    "> - explanation: {@{The stale ask 0.8 against $V = 1$}@} loses"
    " {@{$1 - 0.8 = 0.2$ on each fill that trades there}@}. Such a fill"
    " arrives with {@{probability 0.8 without the fast connection and 0.4"
    " with it}@}, so the expected loss is {@{$0.8 \\times 0.2 = 0.16$ against"
    " $0.4 \\times 0.2 = 0.08$}@}. The fee is {@{paid once, not per share}@},"
    " so the comparison is {@{between those two expectations}@}, and"
    " {@{the $0.16 - 0.08 = 0.08$ saved bounds the fee}@}. The largest option"
    " {@{under 0.08 is $c = 0.079$}@}.\n"
)

"""A 26-word derivation clozing 77% of its words, the note's line 325."""
DERIVATION_26 = note(
    "> - explanation: {@{The posterior after a positive review}@} is {@{the"
    " good-and-positive branch over both branches, $\\frac{p\\delta}{p\\delta"
    " + (1 - p)(1 - \\delta)}$}@}. Substituting {@{$p = 4/5$ gives"
    " $\\frac{(4/5)\\delta}{(4/5)\\delta + (1/5)(1 - \\delta)}$}@}, and"
    " multiplying {@{numerator and denominator by 5 gives $\\frac{4\\delta}"
    "{4\\delta + 1 - \\delta} = \\frac{4\\delta}{1 + 3\\delta}$}@}, which is"
    " {@{the second option}@}.\n"
)

"""A 43-word derivation clozing 84% of its words, the note's line 370."""
DERIVATION_43 = note(
    "> - explanation: {@{The posterior after a negative review}@} is {@{the"
    " bad-and-negative branch over both branches, $\\frac{(1 - p)\\delta}{(1 -"
    " p)\\delta + p(1 - \\delta)}$}@}. The numerator is {@{the prior on bad,"
    " $1 - p$, times the chance of a negative review given bad, $\\delta$}@}."
    " The denominator adds {@{the good branch}@}, {@{the prior $p$ times the"
    " chance of a negative review given good, $1 - \\delta$}@}.\n"
)

"""A solution naming its choice's number and text, the note's block 5.b."""
SOLUTION = note(
    ">\n"
    "> 1. 116 dollars\n"
    "> 2. 115 dollars\n"
    "> 3. 114 dollars\n"
    "> 4. 113 dollars\n"
    "> 5. none of the answers are correct\n"
    ">\n"
    "> ---\n"
    ">\n"
    "> - solution: {@{4. 113 dollars}@}\n"
)

"""A 30-word explanation hidden whole: past the cap and over the ceiling."""
THIRTY = note(
    "> - explanation: {@{The peg rests at 113 behind the 120 displayed shares,"
    " the hundred-share sell fills at that price, the peg stays untouched, and"
    " the displayed bid keeps its queue position on the book.}@}\n"
)

"""A 27-word explanation clozing 30% of its words, under the floor."""
SHORT_COVERAGE = note(
    "> - explanation: {@{The peg rests at 113 behind the 120 displayed"
    " shares}@} so the hundred-share sell fills at that price and the"
    " displayed bid holds its queue position on the book.\n"
)

"""A 26-word explanation clozing 77% yet leaving a 6-word sentence visible."""
VISIBLE_SENTENCE = note(
    "> - explanation: {@{The peg rests at 113 behind the 120 displayed"
    " shares}@}, {@{the hundred-share sell fills at that price and the peg"
    " stays untouched}@}. The displayed bid keeps its queue.\n"
)

"""A 19-word explanation hidden but for the word it leaves outside the cloze."""
VISIBLE_LEAD_IN = note(
    "> - explanation: The {@{peg rests at 113 behind the 120 displayed shares,"
    " so the 100-share sell fills at 113 and the peg stays untouched.}@}\n"
)

"""A 25-word explanation hidden whole in one cloze, 5 words past the cap."""
TWENTY_FIVE = note(
    "> - explanation: {@{The peg rests at 113 behind the 120 displayed shares,"
    " the hundred-share sell fills at that price, the peg stays untouched, the"
    " displayed bid keeps its queue.}@}\n"
)

"""An 18-word explanation whose second cloze hides only a connective."""
GLUE = note(
    "> - explanation: {@{The peg rests at 113 behind the 120 displayed"
    " shares}@}, so the fill is {@{not always}@} visible to general traders.\n"
)

"""A 14-word explanation whose first cloze hides a formula and nothing else."""
FORMULA_ALONE = note(
    "> - explanation: The saved {@{$0.16 - 0.08 = 0.08$}@} bounds {@{the fee"
    " the broker can charge}@} once the race is won.\n"
)


def answer_messages(text: str) -> list[ValidationMessage]:
    """Return every message the four answer-line rules report for *text*."""
    ctx = make_ctx(text)
    return [message for rule in ANSWER_RULES for message in rule(ctx)]


def messages_from(
    rule: Callable[[ValidationContext], list[ValidationMessage]], text: str
) -> list[ValidationMessage]:
    """Return the messages *rule* alone reports for *text*."""
    return list(rule(make_ctx(text)))


def test_answer_style_accepts_eleven_word_explanation_in_one_cloze():
    """An 11-word explanation is one cloze holding its whole sentence."""
    assert not answer_messages(ELEVEN)


def test_answer_style_accepts_nineteen_word_explanation_in_one_cloze():
    """A 19-word explanation is still short enough to hide whole."""
    assert not answer_messages(NINETEEN)


def test_answer_style_accepts_fifty_six_word_derivation_at_sixty_two_percent():
    """Longest reference derivation: payloads hidden, frame every step reads."""
    assert not answer_messages(DERIVATION_56)


def test_answer_style_accepts_twenty_six_word_derivation_at_seventy_seven_percent():
    """A posterior derivation hides each substitution and keeps the joins."""
    assert not answer_messages(DERIVATION_26)


def test_answer_style_accepts_forty_three_word_derivation_at_eighty_four_percent():
    """A near-ceiling derivation still leaves the sentence frame to read."""
    assert not answer_messages(DERIVATION_43)


def test_answer_style_accepts_solution_naming_choice_number_and_text():
    """A solution is one cloze naming the choice's number and its text."""
    assert not answer_messages(SOLUTION)


def test_answer_explanation_shape_rejects_thirty_word_explanation_in_one_cloze():
    """A whole-sentence cloze past 20 words hides the frame and busts the cap."""
    messages = answer_messages(THIRTY)
    assert sorted(message.rule_id for message in messages) == [
        "answer_explanation_shape",
        "cloze_giant",
    ]


def test_answer_explanation_shape_rejects_explanation_clozing_thirty_percent():
    """A long explanation hiding under the 60% floor shows most of its answer."""
    messages = messages_from(answer_explanation_shape, SHORT_COVERAGE)
    assert [message.rule_id for message in messages] == ["answer_explanation_shape"]
    assert "floor" in messages[0].msg


def test_answer_explanation_shape_rejects_explanation_with_a_sentence_visible():
    """Coverage inside the band does not excuse a sentence carrying no cloze."""
    messages = messages_from(answer_explanation_shape, VISIBLE_SENTENCE)
    assert [message.rule_id for message in messages] == ["answer_explanation_shape"]
    assert "with no cloze" in messages[0].msg


def test_answer_explanation_shape_rejects_nineteen_word_explanation_with_lead_in():
    """A short explanation with text outside its cloze leaves that text unseen."""
    messages = messages_from(answer_explanation_shape, VISIBLE_LEAD_IN)
    assert [message.rule_id for message in messages] == ["answer_explanation_shape"]
    assert "outside the cloze" in messages[0].msg


def test_cloze_giant_warns_on_a_twenty_five_word_cloze():
    """One cloze hiding 25 words swallows the step it was meant to quiz."""
    messages = messages_from(cloze_giant, TWENTY_FIVE)
    assert [message.rule_id for message in messages] == ["cloze_giant"]
    assert messages[0].severity is Severity.WARNING


def test_cloze_glue_rejects_a_connective_inside_a_sentence():
    """A cloze hiding only 'not always' gives the card nothing to recall."""
    messages = messages_from(cloze_glue, GLUE)
    assert [message.rule_id for message in messages] == ["cloze_glue"]
    assert messages[0].severity is Severity.ERROR


def test_answer_formula_alone_warns_on_a_formula_only_cloze():
    """A formula hidden alone asks for a symbol string, not a fact."""
    messages = messages_from(answer_formula_alone, FORMULA_ALONE)
    assert [message.rule_id for message in messages] == ["answer_formula_alone"]
    assert messages[0].severity is Severity.WARNING


@requires_reference_note
@pytest.mark.anyio
async def test_reference_note_lints_with_zero_findings():
    """The reference note is the style's reference, so it must lint clean.

    Every rule runs over the note as the validator runs them over a course
    tree, through ``main_mods.validator.check_markdown_file``.  A finding here
    means a rule and the note have drifted apart: either the style moved
    deliberately and the note must follow, or a rule now rejects a shape it
    was written to accept.
    """
    messages = await check_markdown_file(Path(str(REFERENCE_NOTE)))
    assert not messages, [
        (message.rule_id, message.line, message.msg) for message in messages
    ]
