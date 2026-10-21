"""Tests for the readability rules.

The fixtures pin the formulas to values that can be checked by hand: a
synthetic text with exactly 119 words, 639 letters, and 5 sentences for
Coleman-Liau, and a six-monosyllable sentence for Flesch reading ease.  The
syllable table exists because every formula except Coleman-Liau and the
automated readability index depends on it.
"""

from dataclasses import replace

import pytest
from anyio import Path
from main_mods.models import Frontmatter, Severity, ValidationContext
from main_mods.readability import (
    BANDS,
    RULE_REGISTRY,
    ReadabilityScores,
    card_readability_error,
    card_readability_warning,
    card_scores,
    card_text,
    english_share,
    measure,
    prose_text,
    readability_error,
    readability_warning,
    score_text,
    split_parts,
    split_sentences,
    syllables,
    violation_rule_id,
)

"""Public symbols exported by this module (none)."""
__all__ = ()

"""A note path inside a real course, so the topic-note predicate holds."""
NOTE_PATH = Path("/tmp/special/academia/HKUST/ELEC 2400/note.md")

"""Text that is hard on every metric: long words, no short connectives."""
HEAVY = " ".join(
    [
        "Electromagnetic characterization demonstrates considerable "
        "intermodulation variability."
    ]
    * 24
)

"""Nine short sentences, one too few for SMOG to be meaningful."""
LIGHT = " ".join(
    ["The student reads a book about a simple circuit and a small lamp today."] * 9
)

"""Scores that sit inside every band, used as the level test's baseline."""
BASELINE = ReadabilityScores(
    words=200,
    sentences=12,
    letters=900,
    syllables=300,
    complex_words=20,
    polysyllables=20,
    difficult_words=10,
    flesch=50.0,
    grade=12.5,
    fog=12.5,
    smog=12.0,
    coleman_liau=12.5,
    ari=12.5,
    dale_chall=8.0,
)


def make_ctx(text: str, name: str = "note.md") -> ValidationContext:
    """Build a topic-note context without touching the filesystem."""
    return ValidationContext(
        path=Path(f"/tmp/special/academia/HKUST/ELEC 2400/{name}"),
        text=text,
        front="",
        data=Frontmatter(
            tags=["flashcard/active/special/academia/HKUST/ELEC_2400"],
        ),
        body=text,
        session_headers=[],
        ast=None,
    )


def test_prose_text_removes_markup():
    """Maths, code, headings, images, and hrefs must not reach the counters."""
    text = (
        "---\ntags: []\n---\n"
        "## the energy\n"
        "See [the capacitor](capacitor.md) for $E = 1/2 C V^2$ and `C`.\n"
        "![a drawing](figure.svg)\n"
        "{@{ energy }@}\n"
    )
    prose = prose_text(text)
    assert "the energy" not in prose
    assert "tags" not in prose
    assert "1/2" not in prose
    assert "figure.svg" not in prose
    assert "capacitor" in prose
    assert "energy" in prose


def test_card_text_splits_a_card_into_two_sentences():
    """A two-sided card holds two sentences, not one run-on."""
    sentences = split_sentences(card_text("question ::@:: answer"))
    assert [sentence.strip() for sentence in sentences] == ["question", "answer"]


def test_prose_and_cards_are_separate():
    """A card block leaves the prose, and the prose leaves the cards."""
    text = (
        "## section\n"
        "Plain prose about a resistor.\n"
        "\n"
        "---\n"
        "\n"
        "Flashcards for this section are as follows:\n"
        "- what a resistor does ::@:: it limits current\n"
    )
    prose, cards = split_parts(text)
    assert "Plain prose" in prose
    assert "resistor does" not in prose
    assert "limits current" in cards
    assert "Plain prose" not in cards


def test_card_block_ends_at_the_next_heading():
    """A heading closes the card block, so later prose is measured as prose."""
    text = (
        "Flashcards for this section are as follows:\n"
        "- one ::@:: two\n"
        "## next\n"
        "Prose after the cards.\n"
    )
    prose, cards = split_parts(text)
    assert "Prose after the cards" in prose
    assert "Prose after the cards" not in cards


def test_references_section_is_not_prose():
    """Provenance is a citation list, so it is measured as neither part."""
    text = (
        "## body\n"
        "A sentence of prose.\n"
        "## references\n"
        "- McDermott, K. B. & Roediger, H. L. III (2023). Memory.\n"
    )
    prose, cards = split_parts(text)
    assert "A sentence of prose" in prose
    assert "McDermott" not in prose + cards


def test_thematic_break_is_not_a_sentence():
    """A rule line is layout, and counting it would deflate the sentence mean."""
    prose, _ = split_parts("One sentence.\n\n---\n\nAnother sentence.\n")
    assert "---" not in prose


def test_maths_is_not_counted_as_words():
    """A formula contributes no words to the sentence it sits in."""
    scores = measure(prose_text("Energy is $E = mc^2$ stored."), frozenset())
    assert scores.words == 3


@pytest.mark.parametrize(
    ("word", "count"),
    [
        ("cat", 1),
        ("table", 2),
        ("running", 2),
        ("business", 2),
        ("science", 2),
        ("beautiful", 3),
        ("queue", 1),
        ("the", 1),
        ("apple", 2),
        ("people", 2),
        ("self-contained", 3),
    ],
)
def test_syllables(word: str, count: int):
    """The vowel-group count follows the published guidance on suffixes."""
    assert syllables(word) == count


def test_coleman_liau_reference_text():
    """119 words, 639 letters, 5 sentences must score 14.53 on Coleman-Liau."""
    words = ["a" * 6] * 44 + ["a" * 5] * 75
    sentences = []
    index = 0
    for size in (24, 24, 24, 24, 23):
        sentences.append(" ".join(words[index : index + size]) + ".")
        index += size
    scores = measure(prose_text(" ".join(sentences)), frozenset())
    assert scores.words == 119
    assert scores.sentences == 5
    assert scores.letters == 639
    assert scores.coleman_liau == pytest.approx(14.53, abs=0.01)


def test_flesch_reference_sentence():
    """Six one-syllable words in one sentence score 116.14."""
    scores = measure(prose_text("The cat sat on the mat."), frozenset())
    assert scores.words == 6
    assert scores.sentences == 1
    assert scores.syllables == 6
    assert scores.flesch == pytest.approx(116.14, abs=0.02)


def test_short_note_is_skipped():
    """Below 120 words a score is noise, so nothing is reported."""
    text = " ".join(["This sentence has ten simple words in it total."] * 5)
    assert score_text(text, "/tmp/no-such-course") is None


def test_non_english_note_is_skipped():
    """A note in another script is not measured in English units."""
    text = "老子是道家學派的創始人。他主張無為而治。"
    assert english_share(text) == 0.0
    assert score_text(text, "/tmp/no-such-course") is None


def test_smog_is_skipped_below_ten_sentences():
    """SMOG needs about ten sentences; the other six metrics still score."""
    scores = score_text(LIGHT, "/tmp/no-such-course")
    assert scores is not None
    assert scores.sentences == 9
    assert scores.smog is None
    assert scores.flesch is not None


def test_only_dense_text_violates():
    """Plain and simple prose is the target, so nothing fires below the limit."""
    assert violation_rule_id(replace(BASELINE, flesch=95.0)) is None
    assert violation_rule_id(replace(BASELINE, grade=4.0)) is None
    assert violation_rule_id(replace(BASELINE, dale_chall=2.0)) is None


def test_level_follows_the_violation_count():
    """One or two violations warn; three make it an error; none say nothing."""
    assert violation_rule_id(BASELINE) is None
    assert violation_rule_id(replace(BASELINE, flesch=20.0)) == "readability_warning"
    two = replace(BASELINE, flesch=20.0, grade=20.0)
    assert violation_rule_id(two) == "readability_warning"
    three = replace(BASELINE, flesch=20.0, grade=20.0, fog=20.0)
    assert violation_rule_id(three) == "readability_error"


def test_rules_report_a_heavy_note_as_an_error():
    """A note outside every band produces one error and no warning."""
    ctx = make_ctx(HEAVY)
    errors = readability_error(ctx)
    assert len(errors) == 1
    assert errors[0].severity is Severity.ERROR
    assert errors[0].rule_id == "readability_error"
    assert "of 7 readability metrics are too dense" in errors[0].msg
    assert readability_warning(ctx) == []


def test_rules_ignore_a_container_page():
    """An index page is not a topic note, so it is never scored."""
    ctx = make_ctx(HEAVY, name="index.md")
    assert readability_warning(ctx) == []
    assert readability_error(ctx) == []


def test_card_rules_score_the_card_block_alone():
    """Dense cards in a clean note are reported by the card rules only."""
    cards = "".join(
        "- electromagnetic characterization demonstration ::@:: "
        "considerable intermodulation variability appears in the "
        "characterization\n"
        for _ in range(6)
    )
    ctx = make_ctx(
        "## section\nA short and plain sentence of prose.\n\n---\n\n"
        "Flashcards for this section are as follows:\n" + cards
    )
    assert readability_warning(ctx) == []
    assert readability_error(ctx) == []
    assert len(card_readability_error(ctx)) == 1
    assert card_readability_warning(ctx) == []


def test_card_rules_skip_a_note_with_few_cards():
    """Four cards are needed before a card block is worth scoring."""
    text = (
        "## section\nProse.\nFlashcards for this section are as follows:\n"
        "- electromagnetic characterization ::@:: intermodulation variability\n"
    )
    ctx = make_ctx(text)
    assert card_scores(text, "/tmp/no-such-course") is None
    assert card_readability_warning(ctx) == []
    assert card_readability_error(ctx) == []


def test_rules_are_registered_under_their_own_names():
    """The validator merges this registry, so ids must match function names."""
    ids = {rid for rid, _ in RULE_REGISTRY.items()}
    assert ids == {
        "readability_warning",
        "readability_error",
        "card_readability_warning",
        "card_readability_error",
    }
    assert set(BANDS) == {
        "flesch",
        "grade",
        "fog",
        "smog",
        "coleman_liau",
        "ari",
        "dale_chall",
    }
