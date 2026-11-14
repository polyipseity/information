"""Rules that hold blockquote question blocks to one shape.

The shape: the question is the blockquote's own paragraphs, a ``> ---`` line
separates it from the answer, and the answer is ``- solution:``,
``- explanation:`` or ``- annotation:`` items carrying the clozes.  Choices,
when a source really supplies them, sit at blockquote level one space after
the marker, ``> 1. (a)``; an author never invents them and never writes them
as bullets or letters.  The answer lines are measured as well: a solution
names the choice it answers and carries one cloze, and an explanation of at
most twenty words is one cloze holding the line whole, while a longer one
hides each step's payload, keeps the frame, and leaves between 45% and 95% of
its words inside a cloze.  That band is the one the owner's forty
hand-corrected answer lines keep, 0.50 to 0.906: a line may show a little more
of its answer than the reference note does, and hide a little more, without
the rule mistaking either edge for a defect.

One rule here carries a legacy allowance, because the older notes were written
before the shape existed and a tree-wide error would fail them on arrival:
``question_block_rule_missing`` speaks only about a single block that departs
from a file's own habit.  ``cloze_giant`` keeps that allowance for a prose card
alone, measures every labelled answer line wherever it lives, and warns rather
than errors while the long clozes the tree already carries wait for their own
sweep.  The measure behind each choice is in the rule docstrings.
"""

import re
from collections.abc import Iterator, Mapping, Sequence
from string import punctuation

from .models import Severity, ValidationContext, ValidationMessage
from .readability import split_sentences
from .registry import RuleRegistry
from .rules import (
    _ANY_LABEL_RE,
    _answer_item_records,
    _answer_items,
    _scan_cloze_tokens,
    _split_answer_label,
)
from .utils import locate

"""Public symbols exported by this module."""
__all__ = (
    "RULE_REGISTRY",
    "answer_explanation_shape",
    "answer_sentence_all_hidden",
    "answer_solution_names_option",
    "answer_solution_one_cloze",
    "cloze_giant",
    "question_block_fence_nested",
    "question_block_figure_missing",
    "question_block_label",
    "question_block_options_lettered",
    "question_block_options_unordered",
    "question_block_rule_missing",
    "question_block_subquestion_label",
)

"""The rules defined here, for the validator to include."""
RULE_REGISTRY = RuleRegistry()

"""A blockquote list item answering the block's question."""
_ANSWER_RE = re.compile(
    r"^[ \t]*>[ \t]*(?:-[ \t]*)?(?:solution|explanation|annotation)[ \t]*:",
    re.IGNORECASE,
)

"""A ``- question:`` label item, the shape the house format drops."""
_LABEL_RE = re.compile(r"^[ \t]*>[ \t]*-[ \t]*question[ \t]*:", re.IGNORECASE)

"""A ``> ---`` line separating a question from its answer."""
_RULE_RE = re.compile(r"^[ \t]*>[ \t]*-{3,}[ \t]*$")

"""The blockquote marker a line opens with, which is structure and not text."""
_QUOTE_RE = re.compile(r"^[ \t]*>[ \t]?")

"""A figure a block refers to, by number."""
_FIGURE_RE = re.compile(r"\bfigures?[ \t]+\d+", re.IGNORECASE)

"""A Markdown image, which is how a block carries the figure it names."""
_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")

"""A subquestion label in the unified form: ``5.a.``, ``9.iv.``, ``10.c.``."""
_SUBQUESTION_LABEL_RE = re.compile(r"^\d+\.(?:[a-z]|[ivxlcdm]{2,})\.(?![A-Za-z0-9])")

"""A bare subquestion label, which says nothing of its parent question."""
_BARE_SUBQUESTION_LABEL_RE = re.compile(
    r"^\((?:[A-Za-z]|[ivxlcdm]{2,})\)(?![A-Za-z0-9])", re.IGNORECASE
)

"""A subquestion label bracketing the sub-part instead of dotting it, ``5(a)``."""
_BRACKETED_SUBQUESTION_LABEL_RE = re.compile(r"^\d+\([A-Za-z]+\)")

"""A subquestion label opening on its parent number, a dot and a sub-part."""
_DOTTED_SUBQUESTION_LABEL_RE = re.compile(r"^\d+\.[A-Za-z]+")

"""A top-level question's numeral left unescaped, which reads as a list marker."""
_UNESCAPED_NUMERAL_RE = re.compile(r"^(?P<number>\d+)\.[ \t]+(?!\()")

"""The message a label's form is reported with, on the first line or a later one."""
_DOTTED_LABEL_MESSAGE = (
    "the subquestion's label is the parent number, a dot, a lower-case "
    "letter or roman numeral, and a dot again, as '5.a.' or '9.iv.'"
)

"""The message a label written below a stem is reported with."""
_STEM_LABEL_MESSAGE = (
    "a subquestion's label opens its own block: a stem above it hides the "
    "label from the card, so give the subquestion its own block and restate "
    "the premises it needs"
)

"""A code fence indented under a blockquote list item."""
_NESTED_FENCE_RE = re.compile(r"^[ \t]*>[ \t]{4,}```")

"""A code fence at blockquote level, whose lines are code rather than text."""
_QUOTE_FENCE_RE = re.compile(r"^(?:```|~~~)")

"""A blockquote list item nested one level under the question."""
_NESTED_ITEM_RE = re.compile(
    r"^[ \t]*>[ \t]{4,}(?P<marker>[-*+]|\d+[.)])[ \t]+(?P<text>\S.*)$"
)

"""A numbering token opening an item, which makes it a labelled sub-part."""
_NUMBERING_RE = re.compile(
    r"^(?:\(\d+\)|\d+[.)]|\([ivxlcdm]+\)|[ivxlcdm]+[.)]|\([A-Za-z]\)|[A-Za-z][.)])",
    re.IGNORECASE,
)

"""A nested item marked with a letter instead of a number."""
_LETTER_ITEM_RE = re.compile(
    r"^[ \t]*>[ \t]{4,}(?:\((?P<paren>[A-Za-z])\)|(?P<bare>[A-Za-z])[.)])[ \t]+\S"
)

"""A list item at blockquote level, which makes the block a list of sub-parts."""
_TOP_LEVEL_ITEM_RE = re.compile(r"^[ \t]*>[ \t]{1,2}-[ \t]+\S")

"""A choice at blockquote level: a number, then the choice's own text."""
_CHOICE_LINE_RE = re.compile(r"^[ \t]*>[ \t]*(?P<number>\d+)[.)][ \t]+(?P<text>\S.*)$")

"""A digit marker, which numbers the item and makes it a choice."""
_DIGIT_MARKER_RE = re.compile(r"\d+[.)]")

"""Single letters that read as roman numerals, so the marker is numbering."""
_ROMAN_LETTERS = frozenset("ivxIVX")

"""A cloze deletion and the text it hides."""
_CLOZE_RE = re.compile(r"\{@\{(?P<body>.*?)\}@\}", re.DOTALL)

"""Display math: a ``$$…$$`` block, a ``\\[…\\]`` block, or an aligned environment.

The environments are the ones ``_DISPLAY_MATH_BLOCK_RE`` in ``rules.py``
names, and a block may span lines, as one does inside a cloze.
"""
_DISPLAY_MATH_RE = re.compile(
    r"\$\$.*?\$\$"
    r"|\\\[.*?\\\]"
    r"|\\begin\{(?P<environment>aligned|align|gathered|split)\}"
    r".*?\\end\{(?P=environment)\}",
    re.DOTALL,
)

"""Math written inline, which a cloze may hide whole without hiding prose.

A backslash escapes a dollar, so ``\\$1`` is a literal amount and neither
opens nor closes a match: ``latex_disallowed_delimiters`` reads ``\\[`` as text
for the same reason.  A dollar also refuses a neighbouring dollar, the bound
``latex_single_line`` keeps, so an inline match never takes half a ``$$`` pair
apart; display math is stripped before this pattern runs.
"""
_MATH_RE = re.compile(r"(?<![\\$])\$(?!\$)[^$\n]*(?<!\\)\$")

"""Code written inline, treated like math when counting words."""
_CODE_RE = re.compile(r"`[^`\n]*`")

"""Markup characters left over once math and code are gone."""
_MARKUP_RE = re.compile(r"[\\^_{}<>/|=+*\[\]()]")

"""An HTML tag, which arranges the text without stating anything itself."""
_HTML_TAG_RE = re.compile(r"<[^>]*>")

"""The characters that state a value: a maths symbol, beside its digits.

Letters and digits state one by themselves.  A maths symbol does too, since
``ρ=−1`` is the premise a sentence turns on, while an ellipsis only trails the
sentence and is no part of it.
"""
_MATH_SYMBOLS = frozenset("+-*/=<>^×÷−≤≥≠≈±·√∑∫∂%")

"""A token that is a word rather than punctuation or a symbol."""
_WORD_RE = re.compile(r"[A-Za-z]{2,}")

"""One option a solution names: a number, its marker, then the choice's text.

The text ends where the join to the next name opens, so several names run one
line and a choice's own comma joins nothing.
"""
_ANSWER_NAME_RE = re.compile(
    r"(?P<number>\d+)[.)][ \t]+(?P<text>\S.*?)"
    r"(?=(?:,\s*and\s+|\s+and\s+|,\s*|;\s*|&)\s*\d+[.)][ \t]|\Z)",
    re.DOTALL,
)

"""Trailing sentence punctuation and inline markup a text comparison drops."""
_TRAILING_DROPPED = punctuation

"""The least share of an answer line's prose words its clozes hide.

The owner's forty hand-corrected answer lines hide at least 0.50 of their
prose words, so the floor sits below the lowest of them: a line may show a
little more of its answer than the reference note does and still read as one
card per step.
"""
_ANSWER_COVERAGE_MIN = 0.45

"""The most share of an answer line's prose words its clozes hide.

The same corpus hides at most 0.906, so the ceiling sits above it: a line may
hide a little more and still keep the frame that reads it.
"""
_ANSWER_COVERAGE_MAX = 0.95

"""The most prose words one cloze hides, and the length an answer line is clozed whole at."""
_ANSWER_CLOZE_WORDS = 20

"""The fewest prose words a sentence needs before its cloze is judged."""
_SENTENCE_MIN_WORDS = 4

"""A mark standing where a cloze sat, for the sentence splitter to keep."""
_CLOZE_MARK = "\x00"

"""A run of two periods or more, which trails a sentence rather than ending it."""
_ELLIPSIS_RE = re.compile(r"\.{2,}")

"""The stand-in an ellipsis takes while a line is split into sentences."""
_ELLIPSIS_MARK = "\x01"

"""What a long answer line's clozes are taught to hide."""
_ANSWER_SHAPE_ADVICE = (
    f"past {_ANSWER_CLOZE_WORDS} words the line hides each step's payload and "
    f"keeps the frame that reads it, in clozes of at most "
    f"{_ANSWER_CLOZE_WORDS} words each"
)

"""The content files whose sections hold question blocks."""
_CONTENT_FILES = frozenset({"lab.md", "tutorial.md", "lecture.md"})

"""A line break closing a line that an item continues on the line below."""
_BR_TAIL_RE = re.compile(r"<br\s*/?>[ \t]*$", re.IGNORECASE)

"""The gap a continued answer line leaves after its quote marker.

One space of the marker itself, then the four-space indent the item's text sits
at, so the line reads ``>`` then five spaces then the text.
"""
_ITEM_INDENT = 5


def _item_is_one_cloze(text: str) -> bool:
    """Return whether one cloze holds *text* whole, punctuation and all.

    Only whitespace may sit around the cloze: the item is then one card with
    nothing visible to prompt it, which is the shape a short answer takes.
    """
    _, spans, _, _, _ = _scan_cloze_tokens(text)
    return len(spans) == 1 and text.strip() == text[spans[0][0] : spans[0][1] + 3]


def _blocks(text: str) -> Iterator[tuple[int, list[tuple[int, str]]]]:
    """Yield ``(offset, lines)`` for each blockquote block in *text*.

    ``lines`` holds ``(offset_inside_block, line)`` pairs so a caller can hand
    an exact position to :func:`locate`.  A block is a maximal run of lines
    starting with ``>``.
    """
    block: list[tuple[int, str]] = []
    block_start = 0
    offset = 0
    for line in text.splitlines(keepends=True):
        if line.startswith(">"):
            if not block:
                block_start = offset
            block.append((offset - block_start, line.rstrip("\r\n")))
        elif block:
            yield block_start, block
            block = []
        offset += len(line)
    if block:
        yield block_start, block


def _answers(lines: list[tuple[int, str]]) -> bool:
    """Return whether the block carries an answer item."""
    return any(_ANSWER_RE.match(line) for _, line in lines)


def _first_answer(lines: list[tuple[int, str]]) -> int:
    """Return the index of the block's first answer item, or ``-1``."""
    for index, (_, line) in enumerate(lines):
        if _ANSWER_RE.match(line):
            return index
    return -1


def _prose_words(text: str) -> int:
    """Count the words of prose in *text*, ignoring math, code and markup.

    Display math goes before inline math: an inline match takes the ``$$``
    delimiters for two empty expressions and leaves the block's own commands
    and letters counted as words.
    """
    text = _DISPLAY_MATH_RE.sub(" ", text)
    text = _MATH_RE.sub(" ", text)
    text = _CODE_RE.sub(" ", text)
    text = _MARKUP_RE.sub(" ", text)
    return sum(1 for word in text.split() if _WORD_RE.search(word))


def _answer_coverage(text: str) -> float:
    """Return the share of *text*'s prose words that its clozes hide.

    A text with no prose word of its own, such as one carrying only a formula,
    is fully covered: nothing is left visible for the reader to recall.
    """
    hidden = sum(
        _prose_words(match.group("body")) for match in _CLOZE_RE.finditer(text)
    )
    total = _prose_words(_CLOZE_RE.sub(r"\g<body>", text))
    return hidden / total if total else 1.0


def _sentences_without_cloze(text: str) -> list[str]:
    """Return the sentences of *text* that a reader would see without a blank.

    Each cloze becomes one marker character before the text is split, so a
    period inside a cloze cannot end a sentence and a sentence carrying the
    marker is one the card quizzes.  A sentence of fewer than
    ``_SENTENCE_MIN_WORDS`` prose words is a fragment left as frame, not a
    payload, so it is not judged.
    """
    marked = _CLOZE_RE.sub(_CLOZE_MARK, text)
    return [
        sentence
        for sentence in split_sentences(marked)
        if _CLOZE_MARK not in sentence and _prose_words(sentence) >= _SENTENCE_MIN_WORDS
    ]


def _visible_residue(text: str) -> str:
    """Return what *text* states once its tags, spaces and punctuation go.

    A letter, a digit and a maths symbol state something the reader can read
    the card by; whitespace, punctuation and an ellipsis only shape the
    sentence around it.  A sentence left with none of the former is one the
    clozes hide whole, so the reader is shown nothing to recall it from.
    """
    return "".join(
        char
        for char in _HTML_TAG_RE.sub(" ", text)
        if char.isalnum() or char in _MATH_SYMBOLS
    )


def _sentence_fragments(text: str) -> list[str]:
    """Return the sentences of *text*, each cloze standing as one marker.

    A cloze becomes a marker before the split, so a period inside a cloze
    cannot end the sentence that carries it.  An ellipsis is stood in for
    first, because it trails a sentence rather than ending one: ``I mean...
    {@{it is a convention}@}`` is one sentence whose frame is visible, and
    splitting at the ellipsis would leave the cloze alone as a fragment that
    reads as hidden whole.
    """
    marked = _CLOZE_RE.sub(_CLOZE_MARK, text)
    marked = _ELLIPSIS_RE.sub(_ELLIPSIS_MARK, marked)
    return [
        fragment.replace(_ELLIPSIS_MARK, "...") for fragment in split_sentences(marked)
    ]


def _hidden_whole_sentence(text: str) -> str | None:
    """Return the sentence *text* hides whole, or ``None`` if it hides none.

    A sentence is hidden whole when it carries a cloze and nothing outside its
    clozes states anything, so ``{@{Twenty days, from the 18.6-year cycle}@}.``
    is one, while ``Thus, simply {@{add up the activity time: 5+15+60 = 80
    minutes}@}.`` is not.  Whether a short answer is exempt is the caller's
    question: it alone knows whether the answer is one line, and a short answer
    written across lines is a derivation like any other.
    """
    for sentence in _sentence_fragments(text):
        if _CLOZE_MARK not in sentence:
            continue
        if not _visible_residue(sentence.replace(_CLOZE_MARK, " ")):
            return sentence
    return None


def _long_clozes(line: str) -> list[int]:
    """Return the word counts of the clozes in *line* over ``_ANSWER_CLOZE_WORDS``."""
    counts = [_prose_words(match.group("body")) for match in _CLOZE_RE.finditer(line)]
    return [count for count in counts if count > _ANSWER_CLOZE_WORDS]


def _top_level_item(line: str) -> bool:
    """Return whether *line* is a list item at blockquote level."""
    return bool(_TOP_LEVEL_ITEM_RE.match(line))


def _choice_items(lines: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Return the bulleted items that sit before the block's answer.

    Only the items before the first answer item count: anything after it is
    part of the answer.  A digit marker numbers the item, so the item is
    already in the shape the choices rule asks for.  A block whose question is
    itself a list drives sub-parts, not choices, so it is left alone.
    """
    stop = _first_answer(lines)
    if stop < 0:
        return []
    if any(_top_level_item(line) for _, line in lines[:stop]):
        return []
    items: list[tuple[int, str]] = []
    for offset, line in lines[:stop]:
        match = _NESTED_ITEM_RE.match(line)
        if not match or _DIGIT_MARKER_RE.fullmatch(match.group("marker")):
            continue
        items.append((offset, match.group("text")))
    return items


def _lettered_items(lines: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Return the nested items marked with a letter before the block's answer."""
    stop = _first_answer(lines)
    if stop < 0:
        return []
    return [
        (offset, line) for offset, line in lines[:stop] if _LETTER_ITEM_RE.match(line)
    ]


def _choice_lines(lines: list[tuple[int, str]]) -> list[tuple[int, int, str]]:
    """Return ``(offset, number, text)`` for each numbered choice of the block.

    A choice is one line at blockquote level, ``> 1. (a)``: the number indexes
    the block's list and the rest of the line is the choice's own text.  Only
    the lines before the first answer count, and a block with no such line has
    no choices at all.
    """
    stop = _first_answer(lines)
    if stop < 0:
        return []
    choices: list[tuple[int, int, str]] = []
    for offset, line in lines[:stop]:
        match = _CHOICE_LINE_RE.match(line)
        if match:
            choices.append((offset, int(match.group("number")), match.group("text")))
    return choices


def _answer_item(lines: list[tuple[int, str]], label: str) -> tuple[int, str] | None:
    """Return ``(offset, text)`` for the block's first item in *label*'s slot.

    The item's text is everything it says: the words after its label and every
    continuation line below it, joined as one answer, with each cloze left in
    place so a caller can tell what it hides from what it shows.
    """
    for offset, name, text, _line_count in _answer_items(lines):
        if name == label:
            return offset, text
    return None


def _quoted_text(line: str) -> str:
    """Return *line* without its blockquote marker."""
    return _QUOTE_RE.sub("", line, count=1).strip()


def _text_lines(lines: list[tuple[int, str]]) -> Iterator[tuple[int, str]]:
    """Yield ``(offset, content)`` for each quoted text line in *lines*.

    A blank line carries no text, a line inside a fenced code block is code,
    and a line continuing an answer item is part of that item rather than a
    line of its own, so none of them is judged as a label's line.
    """
    continuation = {
        offset
        for _label, records in _answer_item_records(lines)
        for offset, _raw, _text, _start, _blank in records[1:]
    }
    in_fence = False
    for offset, line in lines:
        content = _quoted_text(line)
        if _QUOTE_FENCE_RE.match(content):
            in_fence = not in_fence
            continue
        if in_fence or not content or offset in continuation:
            continue
        yield offset, content


def _unwrap_clozes(text: str) -> str:
    """Return *text* with every cloze replaced by what it hides."""
    return _CLOZE_RE.sub(r"\g<body>", text).strip()


def _normalized_answer_text(text: str) -> str:
    """Return *text* in the form two answer texts are compared in.

    Whitespace collapses, case folds, and trailing sentence punctuation and
    inline markup drop, so ``(c)`` and ``(c).`` agree.  Inline math and code
    stay part of the text, since a choice may be nothing else.
    """
    return " ".join(text.split()).casefold().rstrip(_TRAILING_DROPPED)


def _answer_names(text: str) -> list[tuple[int, str]]:
    """Return ``(number, text)`` for each option a solution names.

    A name is ``<number>. <choice text>``, and names run one after another
    joined by ``and``, a comma, ``&`` or a semicolon.  The text has to open on
    a name, so a solution opening on prose names no option, and an empty list
    means no option is named at all.
    """
    matches = list(_ANSWER_NAME_RE.finditer(text))
    if not matches or matches[0].start() != 0:
        return []
    return [
        (int(match.group("number")), match.group("text").strip()) for match in matches
    ]


def _answer_name_problem(
    names: Sequence[tuple[int, str]], listed: Mapping[int, str]
) -> str | None:
    """Return what is wrong with the options *names* gives, or ``None``.

    Each name is checked against the block's own choice list: the number has
    to exist there, and the text has to be that choice's text.
    """
    for number, answer_text in names:
        if number not in listed:
            return (
                f"the solution names choice {number}, while this question "
                "lists none by that number"
            )
        if _normalized_answer_text(answer_text) != _normalized_answer_text(
            listed[number]
        ):
            return (
                f"the solution's text is not choice {number}'s text; copy "
                "the choice itself"
            )
    return None


def _opens_on_label(content: str) -> bool:
    """Return whether *content* opens on a subquestion label.

    A label is the unified path (``5.a.``), a bare sub-part (``(a)``), a
    bracketed one (``5(a)``), or a dotted one whose form is defective
    (``5.a``, ``5.A.``).  A choice opens on a digit and a dot, ``1. (a)``,
    which is no label.
    """
    return any(
        pattern.match(content)
        for pattern in (
            _SUBQUESTION_LABEL_RE,
            _BARE_SUBQUESTION_LABEL_RE,
            _BRACKETED_SUBQUESTION_LABEL_RE,
            _DOTTED_SUBQUESTION_LABEL_RE,
        )
    )


def _label_form_problem(content: str) -> str | None:
    """Return what is wrong with the form of the label *content* opens on.

    Only the label's own shape is judged, so a line opening on a numeral and
    a space is no label at all: a choice (``1. 116 dollars``) is silent here.
    A unified path is silent, and each defective form carries the message
    that names the shape it owes.
    """
    if _SUBQUESTION_LABEL_RE.match(content):
        return None
    if _BARE_SUBQUESTION_LABEL_RE.match(content):
        return (
            "the subquestion's label carries its parent question too, as "
            "'5.a.', because the block is read on its own"
        )
    if _BRACKETED_SUBQUESTION_LABEL_RE.match(content):
        return (
            "the subquestion's label is '5.a.', not '5(a)': the parent number, "
            "a dot, the sub-part, and a dot again"
        )
    if _DOTTED_SUBQUESTION_LABEL_RE.match(content):
        return _DOTTED_LABEL_MESSAGE
    return None


def _subquestion_label_problem(content: str) -> str | None:
    """Return what is wrong with the label opening a block's first line.

    The label carries the whole path, so a reader who sees it alone learns the
    question it belongs to: the parent number, a dot, the sub-part as a
    lower-case letter or roman numeral, and a dot again (``5.a.``, ``9.iv.``).
    A block opening on an escaped numeral (``5\\.``) or on a choice
    (``1. (a)``) is labelled already, and an opening that labels nothing says
    nothing about a parent.  An unescaped numeral (``3. Suppose``) is the
    other defect a first line can carry: the number is a question's own, and
    missing the escape turns it into a list marker.
    """
    numeral = _UNESCAPED_NUMERAL_RE.match(content)
    if numeral:
        return (
            f"a top-level question escapes its numeral, `{numeral.group('number')}\\.`; "
            "an unescaped number at the start of a line reads as a list marker"
        )
    return _label_form_problem(content)


def _stem_hidden_label_problem(content: str) -> str | None:
    """Return what is wrong with a label opening a block's later line.

    A card reads the block from its first line, so a label written under a
    stem is hidden from the reader: the subquestion owes a block of its own,
    labelled on that block's first line and carrying the premises it needs.
    A label whose own form is defective, ``5.a`` or ``5.A.``, keeps the
    message the first line already gives it, so one defect has one wording.
    """
    if not _opens_on_label(content):
        return None
    if _SUBQUESTION_LABEL_RE.match(content):
        return _STEM_LABEL_MESSAGE
    if _DOTTED_SUBQUESTION_LABEL_RE.match(content):
        return _DOTTED_LABEL_MESSAGE
    return _STEM_LABEL_MESSAGE


def _reports(
    rule_id: str,
    msg: str,
    ctx: ValidationContext,
    offset: int,
    *,
    severity: Severity = Severity.ERROR,
) -> ValidationMessage:
    """Build one message at *offset* in *ctx*, an error unless *severity* says otherwise."""
    line, col = locate(ctx.text, offset)
    return ValidationMessage(
        rule_id=rule_id, msg=msg, line=line, col=col, severity=severity
    )


@RULE_REGISTRY.register()
def question_block_label(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject a ``- question:`` label item inside an answering block.

    The house shape writes the question as the blockquote's own paragraphs, so
    the label is a leftover of the older shape.  A blockquote with no answer
    item is prose, and a ``Question:`` line inside it is not a label.
    """
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        for offset, line in lines:
            if _LABEL_RE.match(line):
                errors.append(
                    _reports(
                        "question_block_label",
                        "question blocks carry no '- question:' label: write the "
                        "question as the blockquote's own paragraph",
                        ctx,
                        block_start + offset,
                    )
                )
                break
    return errors


@RULE_REGISTRY.register()
def question_block_fence_nested(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject a code fence indented under a list item inside a question block.

    A fence belongs at blockquote level, as ``> ```` `, so the code reads as
    part of the question rather than as a sub-item of an option list.
    """
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        for offset, line in lines:
            if _NESTED_FENCE_RE.match(line):
                errors.append(
                    _reports(
                        "question_block_fence_nested",
                        "code in a question block sits at blockquote level, as "
                        "'> ```', not indented under a list item",
                        ctx,
                        block_start + offset,
                    )
                )
                break
    return errors


@RULE_REGISTRY.register()
def question_block_options_unordered(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject choices written as an unlabelled bullet list.

    A source that lists choices gets a numbered list, one line per choice.  An
    item that opens with a numbering token of its own is a labelled sub-part
    of the question, not an alternative to choose between, so it stays silent.
    """
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        for offset, text in _choice_items(lines):
            if _NUMBERING_RE.match(text):
                continue
            errors.append(
                _reports(
                    "question_block_options_unordered",
                    "choices are a numbered list, one per line ('>     1. ...'); "
                    "an unlabelled bullet list cannot be told from the question",
                    ctx,
                    block_start + offset,
                )
            )
            break
    return errors


@RULE_REGISTRY.register()
def question_block_options_lettered(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject choices numbered with letters instead of digits.

    ``(a)``, ``a)`` and ``A.`` are markers for choices, and the house shape
    numbers them.  A single ``i``, ``v`` or ``x`` reads as a roman numeral, so
    it counts as numbering and stays silent.
    """
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        for offset, line in _lettered_items(lines):
            match = _LETTER_ITEM_RE.match(line)
            if not match:
                continue
            letter = match.group("paren") or match.group("bare")
            if letter in _ROMAN_LETTERS:
                continue
            errors.append(
                _reports(
                    "question_block_options_lettered",
                    "choices are numbered, not lettered: write '>     1. ...' "
                    "rather than '(a)', 'a)' or 'A.'",
                    ctx,
                    block_start + offset,
                )
            )
            break
    return errors


@RULE_REGISTRY.register()
def question_block_rule_missing(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject a ``> ---`` gap where the file's other blocks all carry one.

    Reported only in a content file whose other answering blocks separate
    question from answer: the 695 of 804 answering blocks written before the
    shape existed belong to files that never adopted it, and flagging them
    would bury the signal.  A lone deviation is the one worth an error.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() not in _CONTENT_FILES:
        return errors
    answering = [lines for _, lines in _blocks(ctx.text) if _answers(lines)]
    missing = [
        (start, lines)
        for start, lines in _blocks(ctx.text)
        if _answers(lines) and not any(_RULE_RE.match(line) for _, line in lines)
    ]
    if len(answering) < 2 or len(missing) != 1:
        return errors
    block_start, lines = missing[0]
    stop = _first_answer(lines)
    offset = lines[stop][0] if stop >= 0 else lines[0][0]
    errors.append(
        _reports(
            "question_block_rule_missing",
            "this question block has no '> ---' between the question and its "
            "answer, while every other block in the note has one",
            ctx,
            block_start + offset,
        )
    )
    return errors


@RULE_REGISTRY.register()
def question_block_figure_missing(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject a block that names a figure and shows none.

    A block is read on its own: the card shows the block, never its siblings,
    so a block asking about Figure 3 carries that figure itself.  An image
    anywhere in the block carries it, and a block with no answer item is
    prose.
    """
    rule = "question_block_figure_missing"
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        if any(_IMAGE_RE.search(line) for _, line in lines):
            continue
        for offset, line in lines:
            match = _FIGURE_RE.search(line)
            if not match:
                continue
            errors.append(
                _reports(
                    rule,
                    f"the block names {match.group(0)} and shows no figure; a "
                    "block is read on its own, so it carries its own copy of "
                    "the figure",
                    ctx,
                    block_start + offset,
                )
            )
            break
    return errors


@RULE_REGISTRY.register()
def question_block_subquestion_label(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject a subquestion label that does not carry the whole path.

    A block is read on its own, so ``(a)`` and ``5(a)`` both say nothing the
    reader can use: the label is the path ``5.a.``, the parent number, a dot,
    the sub-part as a lower-case letter or roman numeral, and a dot again.

    Every text line of a block that carries an answer is judged, because the
    card reads the block from its top.  The first line is judged as the
    label's own place: an escaped numeral (``5\\.``) or a choice (``1. (a)``)
    is labelled already, and an unescaped numeral (``3. Suppose``) owes the
    escape.  A label opening any later line is an error whatever its form,
    since the stem above it keeps it out of the card.  A line inside a fenced
    code block is code, and a block with no answer item is prose.
    """
    rule = "question_block_subquestion_label"
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        for index, (offset, content) in enumerate(_text_lines(lines)):
            problem = (
                _subquestion_label_problem(content)
                if index == 0
                else _stem_hidden_label_problem(content)
            )
            if problem is not None:
                errors.append(_reports(rule, problem, ctx, block_start + offset))
                break
    return errors


@RULE_REGISTRY.register()
def answer_solution_names_option(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject a solution that does not name the choice it answers.

    A question that lists numbered choices is answered by naming them:
    ``- solution: {@{3. (c)}@}``.  The number indexes the block's own list,
    opens it with either marker (``3.`` or ``3)``), and the text after it is
    that choice's own text, so a reader learns which option was right without
    re-deriving it.  A bare quantity opens no choice and names none, and a
    source label such as ``(c)`` is choice content rather than the numbering,
    so neither satisfies the rule.

    A question whose key accepts more than one option names them all, each as
    ``<number>. <choice text>``, joined by ``and``, a comma, ``&`` or a
    semicolon: ``{@{2. 115 dollars and 3. 114 dollars}@}``.  A bare number list
    names no option, since the shape is still a name per option.

    The answer sits inside the solution's one cloze, since a card that shows
    ``{@{3}@}. (c)`` shows the very text it asks for.  Trailing sentence
    punctuation is no exception: it belongs to the sentence, not to the
    answer, so ``{@{3. (c)}@}.`` is silent.

    One error per block: a solution opening with no choice number, one naming
    a number the list does not hold, one naming a number with another choice's
    text, and one leaving text outside its cloze each report once, and the
    first name that fails is the one reported.
    """
    rule = "answer_solution_names_option"
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        choices = _choice_lines(lines)
        if not choices:
            continue
        answer = _answer_item(lines, "solution")
        if answer is None:
            continue
        offset, text = answer
        listed: dict[int, str] = {}
        for _, number, choice_text in choices:
            listed.setdefault(number, choice_text)
        names = _answer_names(_unwrap_clozes(text))
        if not names:
            msg = (
                "a solution names the choice it answers, as "
                "'- solution: {@{3. (c)}@}'; this one carries no choice marker"
            )
        else:
            problem = _answer_name_problem(names, listed)
            if problem is not None:
                msg = problem
            elif len(_CLOZE_RE.findall(text)) != 1:
                continue
            elif not _normalized_answer_text(_CLOZE_RE.sub("", text)):
                continue
            else:
                msg = (
                    "the answer sits inside the solution's one cloze, as "
                    "'- solution: {@{3. (c)}@}'; this one leaves text outside it"
                )
        errors.append(_reports(rule, msg, ctx, block_start + offset))
    return errors


@RULE_REGISTRY.register()
def answer_solution_one_cloze(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject a solution that carries anything but exactly one cloze.

    A solution is one answer and one card: the cloze holds it whole, as
    ``{@{3. (c)}@}`` does, with no part of the answer left visible.  A second
    cloze makes the line two cards and the reasoning that needs one belongs in
    ``- explanation:``; no cloze leaves the card with nothing to recall.
    """
    rule = "answer_solution_one_cloze"
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        for offset, label, text, _line_count in _answer_items(lines):
            if label != "solution":
                continue
            count = len(_CLOZE_RE.findall(text))
            if count == 1:
                continue
            if count == 0:
                msg = (
                    "a solution is one cloze holding the answer, and this one "
                    "carries none"
                )
            else:
                msg = (
                    f"a solution is one cloze holding the answer, and this one "
                    f"carries {count}; put the reasoning in '- explanation:'"
                )
            errors.append(_reports(rule, msg, ctx, block_start + offset))
    return errors


@RULE_REGISTRY.register()
def answer_item_repeated(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject a second answer item in a slot that already has one.

    A block holds at most one ``- solution:``, one ``- explanation:`` and one
    ``- annotation:``.  A step that needs more room continues on the lines
    below its label rather than opening a second item, because two items in one
    slot are two answers to one question: the card that shows the second gives
    the reader no way to tell it from the first.  A different slot is a
    different answer, so ``- solution:`` beside ``- explanation:`` stays right,
    and a sub-part of its own (``11.a.``, ``11.b.``) is a block of its own with
    its items of its own.
    """
    rule = "answer_item_repeated"
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        seen: set[str] = set()
        for offset, label, _text, _line_count in _answer_items(lines):
            if label in seen:
                errors.append(
                    _reports(
                        rule,
                        f"this block already carries its '- {label}:' item, "
                        "and a step that needs more room continues on the "
                        "line below it, indented four spaces past the quote "
                        "space, rather than opening a second one",
                        ctx,
                        block_start + offset,
                    )
                )
                continue
            seen.add(label)
    return errors


@RULE_REGISTRY.register()
def answer_item_continuation(ctx: ValidationContext) -> list[ValidationMessage]:
    """Hold a continued answer item to the line it is written on.

    A step below an answer's first line is written ``>`` then five spaces (the
    quote space plus a four-space indent) then its text, and the line above it
    ends in ``<br/>``: that tag is the break, so without it the two lines run
    together as one sentence.  A new paragraph instead leaves a blank ``>``
    line between them, and needs no tag.  A line left at the quote marker's own
    margin is not part of the item at all: it reads as the block's own text and
    the answer loses it, so it reports too.
    """
    rule = "answer_item_continuation"
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        position_of = {offset: position for position, (offset, _) in enumerate(lines)}
        for _label, records in _answer_item_records(lines):
            for position, (offset, _raw, _text, start, blank_before) in enumerate(
                records[1:]
            ):
                if start - 1 != _ITEM_INDENT:
                    errors.append(
                        _reports(
                            rule,
                            "a line continuing an answer item is indented four "
                            "spaces past the quote marker's own space, so it "
                            "reads '>' then five spaces then the text",
                            ctx,
                            block_start + offset,
                        )
                    )
                    continue
                if blank_before:
                    continue
                if _BR_TAIL_RE.search(records[position][1]):
                    continue
                errors.append(
                    _reports(
                        rule,
                        "the line above this one does not end in '<br/>', so "
                        "the two run together as one sentence; end the line "
                        "above with the tag, or separate the paragraphs with "
                        "a blank '>' line",
                        ctx,
                        block_start + offset,
                    )
                )
            last_offset = records[-1][0]
            following_position = position_of[last_offset] + 1
            if following_position >= len(lines):
                continue
            following_offset, following = lines[following_position]
            content = _quoted_text(following)
            if not content.strip() or content == "---":
                continue
            if _split_answer_label(following)[0] is not None:
                continue
            if _ANY_LABEL_RE.match(following):
                continue
            errors.append(
                _reports(
                    rule,
                    "this line sits at the quote marker's own margin, where "
                    "it reads as the block's text rather than part of the "
                    "answer item above it; indent it four spaces past the "
                    "quote space to continue that item",
                    ctx,
                    block_start + following_offset,
                )
            )
    return errors


@RULE_REGISTRY.register()
def answer_explanation_shape(ctx: ValidationContext) -> list[ValidationMessage]:
    """Hold an explanation to the cloze shape its length calls for.

    An explanation is shown as a card too.  One of at most
    ``_ANSWER_CLOZE_WORDS`` prose words is clozed whole: one cloze holding
    everything after the label, punctuation inside, so nothing visible sits
    beside it.  A longer one is a derivation, and its card keeps the sentence
    frame that reads it: every sentence carries a cloze hiding its own step's
    payload, and the line's prose-word coverage stays inside
    ``_ANSWER_COVERAGE_MIN`` to ``_ANSWER_COVERAGE_MAX``.  Below the floor the
    line shows most of its answer; above the ceiling it hides the frame too.
    Math and code are not prose, so a formula may sit outside the clozes.  An
    ``- annotation:`` line is a slot of its own and stays out of scope.
    """
    rule = "answer_explanation_shape"
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        for offset, label, text, line_count in _answer_items(lines):
            if label != "explanation":
                continue
            if not _CLOZE_RE.search(text):
                msg = (
                    "an explanation is shown as cards, so it carries at least "
                    "one cloze hiding the reasoning it turns on"
                )
            elif (
                line_count == 1
                and _prose_words(_CLOZE_RE.sub(r"\g<body>", text))
                <= _ANSWER_CLOZE_WORDS
            ):
                if _item_is_one_cloze(text):
                    continue
                msg = (
                    f"an explanation of at most {_ANSWER_CLOZE_WORDS} words "
                    "on one line hides as one cloze holding its whole "
                    "sentence, from the label onward with the punctuation "
                    "inside, so the card reads that sentence once; this one "
                    "leaves text outside the cloze"
                )
            else:
                coverage = _answer_coverage(text)
                visible = _sentences_without_cloze(text)
                if (
                    _ANSWER_COVERAGE_MIN <= coverage <= _ANSWER_COVERAGE_MAX
                    and not visible
                ):
                    continue
                if coverage < _ANSWER_COVERAGE_MIN:
                    msg = (
                        f"an explanation clozes {coverage:.0%} of its words, "
                        f"under the {_ANSWER_COVERAGE_MIN:.0%} floor, so most "
                        f"of the answer stays visible; {_ANSWER_SHAPE_ADVICE}"
                    )
                elif coverage > _ANSWER_COVERAGE_MAX:
                    msg = (
                        f"an explanation clozes {coverage:.0%} of its words, "
                        f"over the {_ANSWER_COVERAGE_MAX:.0%} ceiling, so the "
                        "frame is hidden too and the card has nothing to "
                        f"read; {_ANSWER_SHAPE_ADVICE}"
                    )
                else:
                    words = _prose_words(visible[0])
                    msg = (
                        f"an explanation clozes {coverage:.0%} of its words "
                        f"yet leaves a sentence of {words} words with no "
                        f"cloze, and every sentence carries a cloze; "
                        f"{_ANSWER_SHAPE_ADVICE}"
                    )
            errors.append(_reports(rule, msg, ctx, block_start + offset))
    return errors


@RULE_REGISTRY.register()
def answer_sentence_all_hidden(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject a long answer line that hides one of its sentences whole.

    A long line keeps the frame that reads it and hides each step's payload,
    sentence by sentence.  Hiding a whole sentence leaves the card showing
    nothing to recall that step from, which is a step the reader has no frame
    for.  A sentence whose outside holds a letter, a digit or a maths symbol
    is readable, so ``Now divide {@{the first number by the second}@}.`` is
    not a defect: its frame is visible.

    Only an ``- explanation:`` or ``- annotation:`` line is judged, and only
    past ``_ANSWER_CLOZE_WORDS`` prose words, since a short line is one cloze
    holding the sentence whole by design.  A ``- solution:`` line is out of
    scope for the same reason.  One message per line, at the line's own
    position.
    """
    rule = "answer_sentence_all_hidden"
    errors: list[ValidationMessage] = []
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        for offset, label, text, line_count in _answer_items(lines):
            if label not in {"explanation", "annotation"}:
                continue
            if _hidden_whole_sentence(text) is None:
                continue
            words = _prose_words(_CLOZE_RE.sub(r"\g<body>", text))
            if line_count == 1 and words <= _ANSWER_CLOZE_WORDS:
                continue
            errors.append(
                _reports(
                    rule,
                    f"a sentence of this {words}-word answer hides whole "
                    "inside its clozes, so the card shows no frame to read "
                    "that step; keep the words that introduce it, such as "
                    "its subject or a 'so', outside the clozes, and hide only "
                    "the payload the step turns on",
                    ctx,
                    block_start + offset,
                )
            )
    return errors


@RULE_REGISTRY.register()
def cloze_giant(ctx: ValidationContext) -> list[ValidationMessage]:
    """Warn when a cloze hides more than ``_ANSWER_CLOZE_WORDS`` words of prose.

    A card reads the frame it is shown, so one cloze hides one step of the
    reasoning: a cloze past the cap swallows the whole sentence and leaves the
    reader no frame to recover it from.  Math and code inside the cloze are not
    words of prose, so a formula may be hidden whole.

    Every labelled answer line is measured, wherever it lives: an
    ``- explanation:``, an ``- annotation:`` or any other labelled answer line
    of any note reports.  The whole item is measured, its continuation lines
    with it, so a cloze carried onto the line below is judged with the step it
    belongs to.  A ``- solution:`` line is exempt, since its single cloze holds
    the answer whole or names the options verbatim and may legitimately run
    long.  A line carrying no answer label and continuing no item is a prose
    card, and the two legacy gates hold it unchanged: it is measured only in a
    content file that separates question from answer everywhere it asks one.

    A cloze holding a short line whole needs no exemption of its own.  The cap
    is the length a line is clozed whole at, so such a cloze is under the cap
    by construction and the cap alone accepts it.

    A warning rather than an error: the long clozes the tree already carries
    are rewritten in a later sweep, so this rule names them meanwhile instead
    of failing them on arrival.
    """
    rule = "cloze_giant"
    errors: list[ValidationMessage] = []
    answering = [lines for _, lines in _blocks(ctx.text) if _answers(lines)]
    prose_measured = ctx.path.name.lower() in _CONTENT_FILES and all(
        any(_RULE_RE.match(line) for _, line in lines) for lines in answering
    )
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        items = list(_answer_items(lines))
        in_item = {
            offset
            for _label, records in _answer_item_records(lines)
            for offset, _raw, _text, _start, _blank in records
        }
        measured = [
            (offset, text)
            for offset, label, text, _count in items
            if label != "solution"
        ]
        if prose_measured:
            measured += [
                (offset, line) for offset, line in lines if offset not in in_item
            ]
        for offset, text in measured:
            counts = _long_clozes(text)
            if not counts:
                continue
            errors.append(
                _reports(
                    rule,
                    f"a cloze here hides {counts[0]} words; hide one step of "
                    "the reasoning, not the whole sentence, in at most "
                    f"{_ANSWER_CLOZE_WORDS} words, with the mathematics "
                    "inside it not counted",
                    ctx,
                    block_start + offset,
                    severity=Severity.WARNING,
                )
            )
    return errors
