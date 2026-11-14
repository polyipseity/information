"""A suppression comment on an answer line is markup, not answer prose.

A rule that measures an answer line measures what the card shows, so a
``<!-- check: ignore-line[...]: reason -->`` at the end of the line may not
reach any of those rules.  The owner's five hand-corrected formula-alone lines
keep a formula alone and settle it with exactly such a comment, which is why
the lines are the fixtures here: the same line with the comment and without it
has to measure the same coverage, report the same sentences, and stay in band.
"""

from main_mods.question_blocks import (
    _answer_coverage,
    _sentences_without_cloze,
    answer_explanation_shape,
)
from main_mods.rules import _split_answer_label

from .test_answer_style import (
    DERIVATION_26,
    ELEVEN,
    SHORT_COVERAGE,
    messages_from,
    note,
)

"""Public symbols exported by this module (none)."""
__all__ = ()

"""A reason the size of the ones the notes carry, for the synthetic fixtures."""
REASON = "the visible frame names the formula, which is the answer"

"""The one-line comment each fixture's answer line ends with."""
COMMENT = " <!-- check: ignore-line[answer_formula_alone]: " + REASON + " -->"

"""The five answer lines the note suppresses, and what masking has to leave.

Columns: the note and line the fixture is copied from, the answer line itself,
the reason its own suppression gives, and the share of its prose words the
clozes hide, to three places.  The share is the line's own, so a comment that
leaked into the measurement would move it.
"""
PROBE_LINES = (
    (
        "FINA 2303 quiz 2:32",
        r"> - explanation: Assume {@{the par value is \$1}@}. The current {@{price of the bond is: $$\frac {0.03} {0.025} \left(1 - \frac 1 {{1.025}^{20} } \right) + \frac 1 {{1.025}^{20} } \approx \$1.07794581 \,.$$}@} The price {@{after 2 years is: $$\frac {0.03} {0.015} \left(1 - \frac 1 {{1.015}^{16} } \right) + \frac 1 {{1.015}^{16} } \approx \$1.21196896 \,.$$}@} {@{The capital gain rate}@} is {@{$$\frac {1.21196896 - 1.07794581} {1.07794581} \approx 0.12433199 = 12.433199\% \,.$$}@}",
        "the visible frame 'is' names the formula, which is the answer",
        "0.727",
    ),
    (
        "ISOM 2700 quiz 2:71",
        r"> - explanation: Consider {@{one machine and its queue}@}. {@{The average number of customers}@} in the system = {@{0.375/\(1–0.375\) = 0.6}@}. There are two machines, so {@{the answer is 0.6\*2 = 1.2}@}.",
        "the visible frame 'in the system =' names the formula, which is the answer",
        "0.591",
    ),
    (
        "ISOM 2700 quiz 2:107",
        r"> - explanation: {@{The average waiting time in queue}@} is: {@{$$\frac {\rho} {\mu - \lambda} = \frac 1 \mu \frac {\rho} {1 - \rho} \,.$$}@} {@{A certain increase in arrival rate}@} increases {@{$\rho$ by the same amount}@}. {@{$\rho / (1 - \rho)$ means the average waiting time in queue}@} would {@{increase by more than that certain amount}@}.",
        "the visible frame 'is:' names the formula, which is the answer",
        "0.906",
    ),
    (
        "ELEC 2400 week 2 tutorial 1:105",
        r"> - explanation:  Every {@{arrow points into the node}@}, so no {@{current carries a negative sign for its direction}@} and the equation is {@{the bare sum of the four values}@}. {@{A sum of four currents that all run inward}@} can only be {@{zero if some of the values are negative}@}, which means {@{at least one of the four currents in fact runs outward, against its arrow}@}. {@{The values $3$, $2$, $-4$, and $-1$}@} satisfy it as {@{$(+3) + (+2) + (-4) + (-1) = 0$}@}, and so do their {@{negations,  $(-3) + (-2) + (+4) + (+1) = 0$ }@}, since {@{negating all four values negates the sum}@}.",
        "the visible frame 'satisfy it as' names the formula, which is the answer",
        "0.750",
    ),
    (
        "private ELEC 2100 quiz 3:60",
        r"> Explanation: Since {@{$(2+j\omega)(2-j\omega)=4+\omega^2$}@}, {@{the spectrum is real and even}@}; under {@{Fourier-transform symmetry}@}, that means {@{the time-domain signal is real and even rather than complex-valued}@}.",
        "the visible frame 'Since' presents the formula as the premise",
        "0.818",
    ),
)


def suppressing(note_text: str, reason: str = REASON) -> str:
    """Return *note_text* with a formula-alone suppression on its answer line."""
    lines = note_text.split("\n")
    last = max(index for index, line in enumerate(lines) if line.strip())
    lines[last] += f" <!-- check: ignore-line[answer_formula_alone]: {reason} -->"
    return "\n".join(lines)


def test_suppression_comment_is_invisible_to_a_derivation_in_the_band():
    """A derivation in the band stays silent with the comment on its line."""
    assert not messages_from(answer_explanation_shape, DERIVATION_26)
    commented = suppressing(DERIVATION_26)
    assert not messages_from(answer_explanation_shape, commented)


def test_suppression_comment_is_invisible_to_a_line_under_the_floor():
    """A line under the floor reports the same share, comment or not."""
    plain = messages_from(answer_explanation_shape, SHORT_COVERAGE)
    commented = messages_from(answer_explanation_shape, suppressing(SHORT_COVERAGE))
    assert [message.msg for message in commented] == [message.msg for message in plain]
    assert "floor" in plain[0].msg


def test_suppression_comment_alone_is_no_sentence():
    """A comment on an answer line shows nothing to measure on its own."""
    label, text = _split_answer_label("> - explanation: " + COMMENT)
    assert label == "explanation"
    assert _sentences_without_cloze(text) == []
    assert _answer_coverage(text) == 1.0


def test_suppression_comment_leaves_a_short_answer_whole():
    """One cloze still holds a short answer whole with a comment after it."""
    assert not messages_from(answer_explanation_shape, ELEVEN)
    assert not messages_from(answer_explanation_shape, suppressing(ELEVEN))


def test_the_five_suppressed_lines_measure_as_the_note_does():
    """Each suppressed line keeps its own measurement and stays in the band.

    Measured from the line alone and from the line with its comment, since the
    comment may move neither the share nor the sentence count, and
    ``answer_explanation_shape`` stays silent on the whole line.
    """
    for source, line, reason, share in PROBE_LINES:
        commented = (
            f"{line} <!-- check: ignore-line[answer_formula_alone]: {reason} -->"
        )
        for measured in (line, commented):
            text = _split_answer_label(measured)[1]
            assert f"{_answer_coverage(text):.3f}" == share, source
            assert _sentences_without_cloze(text) == [], source
        messages = messages_from(answer_explanation_shape, note(commented + "\n"))
        assert not messages, (source, messages)
