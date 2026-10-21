"""Readability rules for course notes.

Seven standard readability formulas are computed for each topic note and
compared against a single density limit.  Only one direction is a defect: a
value past its limit means the text is denser than a reader at this level can
take.  Prose written plainly is not a problem, so there is no floor.  One
formula past its limit is usually one long sentence or one long noun phrase;
three or more mean the note is hard on every count, which is why the warning
and the error are separate rules.

Prose and cards are measured apart, because they are read differently.  A
paragraph is read for sense, so its cards and its references are removed
first.  A card is read as a prompt and an answer, so only the card block is
measured, and a note with too few cards to score says nothing.

Maths, code, headings, image lines, and link targets carry no reading
difficulty and are removed before counting, and the words that name the
course's own concepts are treated as familiar.  Gunning Fog's own definition
excludes proper nouns, familiar jargon, and compound words, so that exclusion
is part of the formula rather than a fudge.  The scores describe the shape of
the text, not whether a reader understands it: they are a target to write
toward and never a number to game by padding or shredding a sentence.
"""

import re
from collections.abc import Sequence
from dataclasses import dataclass
from functools import lru_cache
from math import sqrt
from pathlib import Path, PurePosixPath

from .models import Severity, ValidationContext, ValidationMessage
from .registry import RuleRegistry
from .utils import FRONT_RE, is_topic_note

"""Public symbols exported by this module."""
__all__ = (
    "BANDS",
    "RULE_REGISTRY",
    "Band",
    "ReadabilityScores",
    "card_readability_error",
    "card_readability_warning",
    "card_scores",
    "card_text",
    "english_share",
    "measure",
    "prose_text",
    "readability_error",
    "readability_warning",
    "score_text",
    "split_parts",
    "split_sentences",
    "syllables",
    "violation_rule_id",
)

"""Registry of the readability rules; merged by the validator."""
RULE_REGISTRY = RuleRegistry()

"""One metric's density limit.

``below`` marks the metrics that run backwards.  Flesch reading ease rises as
the text gets easier, so a note is too dense when the number falls under its
limit rather than over it.
"""


@dataclass(frozen=True)
class Band:
    """A metric's limit, and which side of it counts as too dense."""

    limit: float
    below: bool = False


"""Density limit per metric.

A value past its limit is a violation.  There is no lower bound: plain, short
sentences are the target, and a formula that rewards padding has no place in
a linter that also asks for concision.
"""
BANDS: dict[str, Band] = {
    "flesch": Band(35.0, below=True),
    "grade": Band(13.0),
    "fog": Band(13.5),
    "smog": Band(13.0),
    "coleman_liau": Band(14.5),
    "ari": Band(13.5),
    "dale_chall": Band(8.8),
}

"""Human-readable name of each metric, in band order."""
_LABELS: dict[str, str] = {
    "flesch": "Flesch reading ease",
    "grade": "Flesch-Kincaid grade",
    "fog": "Gunning fog",
    "smog": "SMOG",
    "coleman_liau": "Coleman-Liau",
    "ari": "automated readability index",
    "dale_chall": "Dale-Chall",
}

"""Shortest note the rules speak about, in words."""
MINIMUM_WORDS = 120
"""Shortest note the rules speak about, in sentences."""
MINIMUM_SENTENCES = 8

"""Shortest card block the card rules speak about, in words."""
MINIMUM_CARD_WORDS = 60
"""Shortest card block the card rules speak about, in sentences."""
MINIMUM_CARD_SENTENCES = 4

"""Sentence SMOG needs before its estimate is meaningful."""
SMOG_SENTENCES = 10

"""Placeholder used while protecting abbreviations and decimal points."""
_DOT = "\ue000"

"""Abbreviations whose full stop does not end a sentence."""
_ABBREVIATIONS = (
    "e.g.",
    "i.e.",
    "etc.",
    "approx.",
    "vs.",
    "cf.",
    "fig.",
    "al.",
    "no.",
)

"""Word pattern; a token always starts with a letter."""
_WORD_RE = re.compile(r"[A-Za-z][A-Za-z'\-]*")

"""Vowel groups, the basis of the syllable count."""
_VOWEL_RE = re.compile(r"[aeiouy]+")

"""Words whose spelling hides a syllable the vowel groups would add."""
_SYLLABLE_OVERRIDES: dict[str, int] = {
    "business": 2,
    "create": 2,
    "every": 2,
    "people": 2,
    "quiet": 2,
    "science": 2,
}

"""Endings that mark an inflection of a familiar word."""
_INFLECTIONS = ("s", "es", "ed", "ing", "ly", "er", "est")


def _load_familiar_words() -> frozenset[str]:
    """Load the New Dale-Chall familiar-words list shipped beside this module."""
    path = Path(__file__).with_name("dale_chall_words.txt")
    return frozenset(
        line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line
    )


"""The familiar words a reader is assumed to know without effort."""
_FAMILIAR = _load_familiar_words()


"""The separator line that opens a section's card block."""
_CARD_SEPARATOR_RE = re.compile(
    r"^\s*flashcards? for (?:this |the )?section\b", re.IGNORECASE
)

"""A heading, which closes a card block and a reference list."""
_HEADING_RE = re.compile(r"^#{1,6}\s")

"""Section names that hold provenance rather than prose."""
_REFERENCE_HEADINGS = frozenset({"references", "reference", "bibliography", "sources"})

"""A thematic break, which is layout rather than prose."""
_THEMATIC_BREAK_RE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")

"""Card markup, which marks a line as a card wherever it appears."""
_CARD_LINE_RE = re.compile(r"::@::|:@:")


def split_parts(text: str) -> tuple[str, str]:
    """Return the note's prose and its card text, separated.

    A card block opens on the separator line the linter asks for, or on any
    line carrying card markup, and runs to the next heading.  The references
    section is provenance, not prose, so it is dropped from both.  Thematic
    breaks, headings, and frontmatter go with them: none of it is read.
    """
    front = FRONT_RE.match(text)
    body = text[front.end() :] if front else text
    prose_lines: list[str] = []
    card_lines: list[str] = []
    in_cards = False
    skip_below = 0
    for line in body.splitlines():
        if _HEADING_RE.match(line):
            in_cards = False
            level = len(line) - len(line.lstrip("#"))
            if skip_below:
                if level <= skip_below:
                    skip_below = 0
                continue
            title = line.lstrip("#").strip().strip(":").lower()
            if title in _REFERENCE_HEADINGS:
                skip_below = level
            continue
        if skip_below:
            continue
        if _THEMATIC_BREAK_RE.match(line):
            continue
        if _CARD_SEPARATOR_RE.match(line):
            in_cards = True
            continue
        if in_cards or _CARD_LINE_RE.search(line):
            card_lines.append(line)
        else:
            prose_lines.append(line)
    return "\n".join(prose_lines), "\n".join(card_lines)


def _clean(text: str) -> str:
    """Strip the markup that carries no reading difficulty.

    A table is a lookup structure read cell by cell, not prose read as a
    sentence, so its rows leave with the code and the maths.  Left in, a
    four-row glossary counts as one enormous sentence and drags every metric
    with it.
    """
    body = text
    body = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)
    body = re.sub(r"~~~.*?~~~", " ", body, flags=re.DOTALL)
    body = re.sub(r"`[^`]*`", " ", body)
    body = re.sub(r"\$\$.*?\$\$", " ", body, flags=re.DOTALL)
    body = re.sub(r"\$[^$]*\$", " ", body)
    body = re.sub(r"<!--.*?-->", " ", body, flags=re.DOTALL)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", body)
    body = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", body)
    body = re.sub(r"\{@\{(.*?)\}@\}", r"\1", body, flags=re.DOTALL)
    body = body.replace("::@::", ". ").replace(":@:", ". ")
    body = re.sub(r"^\s*\|.*$", "", body, flags=re.MULTILINE)
    body = re.sub(r"^\s*[-:]+\s*$", "", body, flags=re.MULTILINE)
    body = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", body, flags=re.MULTILINE)
    return body.replace("|", " ")


def prose_text(text: str) -> str:
    """Return the prose a learner reads, without cards, references, or markup."""
    return _clean(split_parts(text)[0])


def card_text(text: str) -> str:
    """Return the card text a learner is quizzed with, without markup."""
    return _clean(split_parts(text)[1])


def split_sentences(prose: str) -> list[str]:
    """Split *prose* into sentences, protecting abbreviations and decimals."""
    protected = prose
    for abbreviation in _ABBREVIATIONS:
        protected = protected.replace(abbreviation, abbreviation.replace(".", _DOT))
    protected = re.sub(r"(?<=\d)\.(?=\d)", _DOT, protected)
    parts = re.split(r"[.!?]+(?:\s+|$)", protected)
    return [part.replace(_DOT, ".") for part in parts if part.strip()]


def syllables(word: str) -> int:
    """Return the syllable count of *word* by counting vowel groups.

    Common suffixes do not add a syllable: ``-ing`` and ``-es`` fall out of the
    vowel groups by themselves, and a final ``-ed`` after a consonant other
    than ``t`` or ``d`` is silent (``walked`` is one, ``created`` is three).
    A short override table covers the spellings the rule cannot see.
    """
    cleaned = word.lower().strip("'-").replace("'", "")
    if not cleaned:
        return 0
    if "-" in cleaned:
        return sum(syllables(part) for part in cleaned.split("-") if part)
    if cleaned in _SYLLABLE_OVERRIDES:
        return _SYLLABLE_OVERRIDES[cleaned]
    count = len(_VOWEL_RE.findall(cleaned))
    if cleaned.endswith("ed") and len(cleaned) > 3 and cleaned[-3] not in "td":
        count -= 1
    elif cleaned.endswith("e") and count > 1:
        keeps_e = (
            cleaned.endswith("le") and len(cleaned) > 2 and cleaned[-3] not in "aeiouy"
        )
        if not keeps_e:
            count -= 1
    return max(1, count)


def _word_sentences(prose: str) -> list[list[str]]:
    """Return the words of each sentence, dropping sentences with no words."""
    result: list[list[str]] = []
    for sentence in split_sentences(prose):
        words = [token.strip("'-") for token in _WORD_RE.findall(sentence)]
        kept = [word for word in words if word]
        if kept:
            result.append(kept)
    return result


@dataclass(frozen=True)
class ReadabilityScores:
    """The counts and the seven scores computed from one note.

    ``smog`` is ``None`` when the note is too short for the formula to mean
    anything.  Every other score is always present, because
    :func:`score_text` refuses to score a note below the minimum length.
    """

    words: int
    sentences: int
    letters: int
    syllables: int
    complex_words: int
    polysyllables: int
    difficult_words: int
    flesch: float
    grade: float
    fog: float
    smog: float | None
    coleman_liau: float
    ari: float
    dale_chall: float


def _syllable_total(words: Sequence[str]) -> int:
    """Return the total syllable count of *words*."""
    return sum(syllables(word) for word in words)


def measure(prose: str, vocabulary: frozenset[str]) -> ReadabilityScores:
    """Score *prose* against the seven metrics.

    *vocabulary* holds the course's own terms, which count as familiar
    jargon.  A proper noun, meaning a capitalised token that is not the first
    token of its sentence, is excluded from the counts of complex,
    polysyllabic, and difficult words, because a name is not a hard word.
    """
    sentences = _word_sentences(prose)
    words = [word for sentence in sentences for word in sentence]
    letters = sum(
        1 for word in words for char in word if char.isascii() and char.isalpha()
    )
    syllables_total = _syllable_total(words)
    complex_words = 0
    polysyllables = 0
    difficult_words = 0
    for sentence in sentences:
        for index, word in enumerate(sentence):
            lowered = word.lower()
            proper = index > 0 and word[0].isupper()
            if proper or lowered in vocabulary:
                continue
            if syllables(lowered) >= 3:
                complex_words += 1
                polysyllables += 1
            if not _is_familiar(lowered, vocabulary):
                difficult_words += 1

    word_count = len(words)
    sentence_count = len(sentences)
    per_word = syllables_total / word_count
    per_sentence = word_count / sentence_count
    difficult_ratio = difficult_words / word_count
    dale_chall = 0.1579 * (difficult_ratio * 100) + 0.0496 * per_sentence
    if difficult_ratio > 0.05:
        dale_chall += 3.6365

    return ReadabilityScores(
        words=word_count,
        sentences=sentence_count,
        letters=letters,
        syllables=syllables_total,
        complex_words=complex_words,
        polysyllables=polysyllables,
        difficult_words=difficult_words,
        flesch=round(206.835 - 1.015 * per_sentence - 84.6 * per_word, 2),
        grade=round(0.39 * per_sentence + 11.8 * per_word - 15.59, 2),
        fog=round(0.4 * (per_sentence + 100 * complex_words / word_count), 2),
        smog=(
            round(1.0430 * sqrt(polysyllables * 30 / sentence_count) + 3.1291, 2)
            if sentence_count >= SMOG_SENTENCES
            else None
        ),
        coleman_liau=round(
            0.0588 * (letters / word_count * 100)
            - 0.296 * (sentence_count / word_count * 100)
            - 15.8,
            2,
        ),
        ari=round(4.71 * (letters / word_count) + 0.5 * per_sentence - 21.43, 2),
        dale_chall=round(dale_chall, 2),
    )


def _is_familiar(word: str, vocabulary: frozenset[str]) -> bool:
    """Whether *word* is on the familiar list, a course term, or an inflection."""
    if _known(word, vocabulary):
        return True
    for suffix in _INFLECTIONS:
        if not word.endswith(suffix) or len(word) - len(suffix) < 2:
            continue
        stem = word[: -len(suffix)]
        if _known(stem, vocabulary):
            return True
        if len(stem) >= 3 and stem[-1] == stem[-2] and _known(stem[:-1], vocabulary):
            return True
    return False


def _known(word: str, vocabulary: frozenset[str]) -> bool:
    """Whether *word* is on the familiar list or in the course vocabulary."""
    return word in _FAMILIAR or word in vocabulary


def english_share(text: str) -> float:
    """Return the share of letters in *text* that are ASCII letters.

    A note below 60% is written mostly in another script, most often
    classical Chinese, and the English formulas say nothing useful about it.
    """
    letters = [char for char in text if char.isalpha()]
    if not letters:
        return 0.0
    return sum(1 for char in letters if char.isascii()) / len(letters)


@lru_cache(maxsize=None)
def _course_vocabulary(course_dir: str) -> frozenset[str]:
    """Return the words the course's own headings and aliases use.

    Every heading in the course names a concept the notes are entitled to
    use without penalty, which is exactly the familiar jargon Gunning Fog
    tells you to leave out of the complex-word count.
    """
    root = Path(course_dir)
    if not root.is_dir():
        return frozenset()
    words: set[str] = set()
    for note in sorted(root.rglob("*.md")):
        try:
            text = note.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for match in re.finditer(r"^#{1,6}\s+(.+)$", text, flags=re.MULTILINE):
            words.update(_terms(match.group(1)))
        front = FRONT_RE.match(text)
        if front:
            words.update(_alias_terms(front.group(1)))
    return frozenset(words)


def _terms(line: str) -> set[str]:
    """Return the lowercased words of *line* that are at least two letters."""
    return {
        word.lower() for word in _WORD_RE.findall(line) if len(word.strip("'-")) >= 2
    }


def _alias_terms(front: str) -> set[str]:
    """Return the words of the frontmatter's ``aliases`` entries."""
    words: set[str] = set()
    inside = False
    for line in front.splitlines():
        if re.match(r"^aliases\s*:", line):
            inside = True
            words.update(_terms(line.split(":", 1)[1]))
        elif inside and re.match(r"^\s*-\s+", line):
            words.update(_terms(line))
        elif line and not line[0].isspace() and not line.startswith("-"):
            inside = False
    return words


def _course_dir(parts: Sequence[str]) -> str:
    """Return the course directory of a note, which is ``academia/<I>/<C>``."""
    lowered = [part.lower() for part in parts]
    for index, part in enumerate(lowered):
        if part == "academia":
            return str(PurePosixPath(*parts[: index + 3]))
    return str(PurePosixPath(*parts[:-1]))


@lru_cache(maxsize=None)
def _cached_scores(text: str, course_dir: str, cards: bool) -> ReadabilityScores | None:
    """Score one part of *text* once, however many rules ask about it."""
    source = card_text(text) if cards else prose_text(text)
    sentences = _word_sentences(source)
    minimum_words = MINIMUM_CARD_WORDS if cards else MINIMUM_WORDS
    minimum_sentences = MINIMUM_CARD_SENTENCES if cards else MINIMUM_SENTENCES
    if sum(len(sentence) for sentence in sentences) < minimum_words:
        return None
    if len(sentences) < minimum_sentences:
        return None
    if english_share(source) < 0.6:
        return None
    return measure(source, _course_vocabulary(course_dir))


def score_text(text: str, course_dir: str) -> ReadabilityScores | None:
    """Score one note's prose, or return ``None`` when it is too short."""
    return _cached_scores(text, course_dir, False)


def card_scores(text: str, course_dir: str) -> ReadabilityScores | None:
    """Score one note's cards, or return ``None`` when there are too few."""
    return _cached_scores(text, course_dir, True)


@dataclass(frozen=True)
class _Violation:
    """One metric past its density limit."""

    name: str
    value: float
    limit: float
    below: bool


def _violations(scores: ReadabilityScores) -> list[_Violation]:
    """Return the metrics of *scores* that sit past their limit."""
    failed: list[_Violation] = []
    for name, band in BANDS.items():
        value = getattr(scores, name)
        if value is None:
            continue
        dense = value < band.limit if band.below else value > band.limit
        if dense:
            failed.append(_Violation(name, value, band.limit, band.below))
    return failed


def violation_rule_id(
    scores: ReadabilityScores, prefix: str = "readability"
) -> str | None:
    """Return the rule that should report *scores*, or ``None`` when clean.

    One or two metrics past their limit is weak evidence and stays a warning;
    three mean the text is hard on every count and is an error.  Several of
    the seven formulas are strongly correlated, so a single violation is
    usually one long sentence rather than a difficult note.
    """
    count = len(_violations(scores))
    if count == 0:
        return None
    return f"{prefix}_{'warning' if count <= 2 else 'error'}"


def _message(
    rule_id: str, failed: Sequence[_Violation], cards: bool
) -> ValidationMessage:
    """Build the message every readability rule shares."""
    detail = "; ".join(
        f"{_LABELS[violation.name]} {violation.value:.2f} "
        f"(wants {'at least' if violation.below else 'at most'} "
        f"{violation.limit:g})"
        for violation in failed
    )
    if cards:
        subject = f"the card block fails {len(failed)} of 7 readability metrics"
        advice = (
            "Split a prompt that asks two things, and cut the answer to the "
            "term it has to give."
        )
    else:
        subject = f"{len(failed)} of 7 readability metrics are too dense"
        advice = (
            "Restructure rather than reword: merge or split sections, shorten "
            "the longest sentences, and cut clauses that carry no fact."
        )
    return ValidationMessage(
        rule_id,
        f"{subject}: {detail}. {advice}",
        Severity.WARNING if rule_id.endswith("warning") else Severity.ERROR,
    )


def _scores_for(
    ctx: ValidationContext, cards: bool = False
) -> ReadabilityScores | None:
    """Return the scores for a topic note, or ``None`` for anything else."""
    if not is_topic_note(ctx):
        return None
    scorer = card_scores if cards else score_text
    return scorer(ctx.text, _course_dir(ctx.path.parts))


def _report(
    ctx: ValidationContext, rule_id: str, cards: bool
) -> list[ValidationMessage]:
    """Report *ctx* when *rule_id* is the level its scores reach."""
    scores = _scores_for(ctx, cards)
    if (
        scores is None
        or violation_rule_id(scores, "readability" if not cards else "card_readability")
        != rule_id
    ):
        return []
    return [_message(rule_id, _violations(scores), cards)]


@RULE_REGISTRY.register()
def readability_warning(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when one or two prose metrics sit past their limit."""
    return _report(ctx, "readability_warning", False)


@RULE_REGISTRY.register()
def readability_error(ctx: ValidationContext) -> list[ValidationMessage]:
    """Error when three or more prose metrics sit past their limit."""
    return _report(ctx, "readability_error", False)


@RULE_REGISTRY.register()
def card_readability_warning(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when one or two card metrics sit past their limit."""
    return _report(ctx, "card_readability_warning", True)


@RULE_REGISTRY.register()
def card_readability_error(ctx: ValidationContext) -> list[ValidationMessage]:
    """Error when three or more card metrics sit past their limit."""
    return _report(ctx, "card_readability_error", True)
