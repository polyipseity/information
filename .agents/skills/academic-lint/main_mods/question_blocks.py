"""Rules that hold blockquote question blocks to one shape.

The shape: the question is the blockquote's own paragraphs, a ``> ---`` line
separates it from the answer, and the answer is ``- solution:``,
``- explanation:`` or ``- annotation:`` items carrying the clozes.  Choices,
when a source really supplies them, are a numbered nested list; an author
never invents them and never writes them as bullets or letters.

Two rules here carry a legacy allowance, because the older notes were written
before the shape existed and a tree-wide error would fail them on arrival:
``question_block_rule_missing`` speaks only about a single block that departs
from a file's own habit, and ``cloze_giant`` judges content files that already
separate question from answer everywhere.  The measure behind that choice is
in the rule docstrings.
"""

import re
from collections.abc import Iterator

from .models import ValidationContext, ValidationMessage
from .registry import RuleRegistry
from .utils import locate

"""Public symbols exported by this module."""
__all__ = (
    "RULE_REGISTRY",
    "cloze_giant",
    "question_block_fence_nested",
    "question_block_label",
    "question_block_options_lettered",
    "question_block_options_unordered",
    "question_block_rule_missing",
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

"""A code fence indented under a blockquote list item."""
_NESTED_FENCE_RE = re.compile(r"^[ \t]*>[ \t]{4,}```")

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

"""A digit marker, which numbers the item and makes it a choice."""
_DIGIT_MARKER_RE = re.compile(r"\d+[.)]")

"""Single letters that read as roman numerals, so the marker is numbering."""
_ROMAN_LETTERS = frozenset("ivxIVX")

"""A cloze deletion and the text it hides."""
_CLOZE_RE = re.compile(r"\{@\{(?P<body>.*?)\}@\}", re.DOTALL)

"""Math written inline, which a cloze may hide whole without hiding prose."""
_MATH_RE = re.compile(r"\$[^$\n]*\$")

"""Code written inline, treated like math when counting words."""
_CODE_RE = re.compile(r"`[^`\n]*`")

"""Markup characters left over once math and code are gone."""
_MARKUP_RE = re.compile(r"[\\^_{}<>/|=+*\[\]()]")

"""A token that is a word rather than punctuation or a symbol."""
_WORD_RE = re.compile(r"[A-Za-z]{2,}")

"""The longest cloze allowed on an answer line, in words of prose."""
_MAX_CLOZE_WORDS = 12

"""The content files whose sections hold question blocks."""
_CONTENT_FILES = frozenset({"lab.md", "tutorial.md", "lecture.md"})


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
    """Count the words of prose in *text*, ignoring math, code and markup."""
    text = _MATH_RE.sub(" ", text)
    text = _CODE_RE.sub(" ", text)
    text = _MARKUP_RE.sub(" ", text)
    return sum(1 for word in text.split() if _WORD_RE.search(word))


def _long_clozes(line: str) -> list[int]:
    """Return the word counts of the clozes in *line* that exceed the cap."""
    counts = [_prose_words(match.group("body")) for match in _CLOZE_RE.finditer(line)]
    return [count for count in counts if count > _MAX_CLOZE_WORDS]


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


def _reports(
    rule_id: str, msg: str, ctx: ValidationContext, offset: int
) -> ValidationMessage:
    """Build one message at *offset* in *ctx*."""
    line, col = locate(ctx.text, offset)
    return ValidationMessage(rule_id=rule_id, msg=msg, line=line, col=col)


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
def cloze_giant(ctx: ValidationContext) -> list[ValidationMessage]:
    """Reject a cloze hiding more than 12 words of prose on an answer line.

    A cloze hides one fact; a longer one hides the whole sentence, and the
    reader cannot recover it from what stays visible.  Math and code inside
    the cloze do not count as words, so a formula may be hidden whole.

    Reported only in a content file that separates question from answer
    everywhere it asks one: cloze length in the 226 legacy clozes across 33
    files is a separate sweep, and those files stay silent until they adopt
    the shape.
    """
    errors: list[ValidationMessage] = []
    if ctx.path.name.lower() not in _CONTENT_FILES:
        return errors
    answering = [lines for _, lines in _blocks(ctx.text) if _answers(lines)]
    if not answering or not all(
        any(_RULE_RE.match(line) for _, line in lines) for lines in answering
    ):
        return errors
    for block_start, lines in _blocks(ctx.text):
        if not _answers(lines):
            continue
        for offset, line in lines:
            if not _ANSWER_RE.match(line):
                continue
            counts = _long_clozes(line)
            if not counts:
                continue
            errors.append(
                _reports(
                    "cloze_giant",
                    f"a cloze here hides {counts[0]} words; split it so each "
                    f"cloze hides at most {_MAX_CLOZE_WORDS}",
                    ctx,
                    block_start + offset,
                )
            )
    return errors
