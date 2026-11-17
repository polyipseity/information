"""Tests for the heading-structure rules.

Each test builds a small topic note and checks one rule, so a failure names
the rule rather than the corpus.
"""

from os import PathLike
from typing import cast

from anyio import Path
from main_mods.models import AstNode, Frontmatter, Severity, ValidationContext
from main_mods.rules import (
    header_generic_article,
    header_hierarchy_flat,
    header_hierarchy_shallow,
    header_hierarchy_thin,
    header_question_form,
    header_sentence_like,
)
from main_mods.utils import (
    FRONT_RE,
    parse_frontmatter,
    parse_session_headers,
)
from main_mods.validator import _MD
from pydantic_yaml import parse_yaml_raw_as

"""Public symbols exported by this module (none)."""
__all__ = ()

"""Frontmatter that makes a fixture count as a topic note."""
_FRONT = "---\ntags: [flashcard/active/special/academia/HKUST/C_1]\n---\n"

"""A topic-note path, so every rule sees a real subject."""
_TOPIC_PATH = Path("/tmp/special/academia/HKUST/C 1/metric.md")


def make_ctx(text: str, path: Path = _TOPIC_PATH) -> ValidationContext:
    """Helper constructing a ValidationContext from raw markdown text."""
    front = parse_frontmatter(text) or ""
    data = parse_yaml_raw_as(Frontmatter, front) if front else Frontmatter()
    match = FRONT_RE.match(text)
    body = text[match.end() :] if match else text
    ast = cast("list[AstNode]", _MD(body))
    return ValidationContext(
        path=path,
        text=text,
        front=front,
        data=data,
        body=body,
        session_headers=parse_session_headers(text, ast),
        ast=ast,
    )


def section_note(count: int, filler: int = 0) -> str:
    """Return a topic note with *count* section-less ``##`` headings."""
    parts = [_FRONT]
    for index in range(count):
        parts.append(f"## section {index}\n")
        parts.extend("filler line\n" for _ in range(filler))
    return "".join(parts)


def test_flat_fires_above_nine():
    """Eleven section-less siblings are one too many."""
    msgs = header_hierarchy_flat(make_ctx(section_note(11)))
    assert len(msgs) == 1
    assert msgs[0].severity is Severity.ERROR
    assert "11 of the sections" in msgs[0].msg
    assert "1.57" in msgs[0].msg


def test_flat_silent_at_nine():
    """Nine section-less siblings are still inside the limit."""
    assert header_hierarchy_flat(make_ctx(section_note(9))) == []


def test_thin_fires_in_the_edge_band():
    """Eight section-less siblings sit at the edge of the limit."""
    msgs = header_hierarchy_thin(make_ctx(section_note(8)))
    assert len(msgs) == 1
    assert msgs[0].severity is Severity.WARNING


def test_thin_silent_below_seven():
    """Six section-less siblings are comfortable."""
    assert header_hierarchy_thin(make_ctx(section_note(6))) == []


def test_shallow_fires_on_a_long_unnested_note():
    """A long note with no ``###`` and five top sections never nests."""
    msgs = header_hierarchy_shallow(make_ctx(section_note(5, filler=30)))
    assert len(msgs) == 1
    assert "never uses '###'" in msgs[0].msg


def test_shallow_silent_when_a_third_level_exists():
    """One ``###`` proves the note knows how to nest."""
    text = _FRONT + "".join(f"## section {i}\n##### deep\n" for i in range(5))
    assert header_hierarchy_shallow(make_ctx(text + "filler\n" * 200)) == []


def test_article_fires_on_generic_lead():
    """A section name that opens on 'the' points at nothing."""
    msgs = header_generic_article(make_ctx(_FRONT + "## the time constant\n"))
    assert len(msgs) == 1
    assert msgs[0].severity is Severity.ERROR
    assert "'the'" in msgs[0].msg


def test_article_silent_on_a_term():
    """The bare term passes."""
    assert header_generic_article(make_ctx(_FRONT + "## time constant\n")) == []


def test_question_fires_on_a_question():
    """Both a question word and a question mark are caught."""
    text = _FRONT + "## why the amplitude falls\n\n## does it converge?\n"
    msgs = header_question_form(make_ctx(text))
    assert len(msgs) == 2


def test_question_silent_on_a_code_token():
    """A heading that is a code span names a token, not a question."""
    assert header_question_form(make_ctx(_FRONT + "## `do`\n")) == []


def test_question_silent_on_a_single_word():
    """A one-word heading names a keyword even when it reads like a verb."""
    text = _FRONT + "## Do\n\n## Is\n\n## Will\n"
    assert header_question_form(make_ctx(text)) == []


def test_question_fires_on_a_single_word_question_mark():
    """A question mark alone is decisive."""
    msgs = header_question_form(make_ctx(_FRONT + "## why?\n"))
    assert len(msgs) == 1


def test_sentence_fires_on_a_clause():
    """Six words with a finite verb after the first read as a sentence."""
    text = _FRONT + "## a stimulus that predicts a temperature change\n"
    msgs = header_sentence_like(make_ctx(text))
    assert len(msgs) == 1
    assert msgs[0].severity is Severity.WARNING


def test_sentence_silent_on_a_short_term():
    """Three words with no verb are a term."""
    assert header_sentence_like(make_ctx(_FRONT + "## energy stored\n")) == []


def test_heading_inside_a_code_fence_is_ignored():
    """A ``##`` line in a fenced block is not a heading."""
    text = _FRONT + "## real section\n\n```\n## the fake section\n```\n"
    assert header_generic_article(make_ctx(text)) == []


def test_container_and_non_topic_files_are_skipped():
    """``index.md`` and a note without the flashcard tag produce nothing."""
    index_path = Path("/tmp/special/academia/HKUST/C 1/index.md")
    plain_path = Path("/tmp/special/academia/HKUST/C 1/metric.md")
    body = _FRONT + "## the time constant\n" + "## section {}\n" * 11
    for rule in (
        header_hierarchy_flat,
        header_hierarchy_thin,
        header_hierarchy_shallow,
        header_generic_article,
        header_question_form,
        header_sentence_like,
    ):
        assert rule(make_ctx(body, index_path)) == []
        assert rule(make_ctx("---\ntags: []\n---\n## the thing\n", plain_path)) == []


def test_messages_carry_a_line_number(tmp_path: PathLike[str]) -> None:
    """Every message points at the heading it reports."""
    del tmp_path
    msgs = header_generic_article(make_ctx(_FRONT + "## intro\n\n## the rule\n"))
    assert len(msgs) == 1
    assert msgs[0].line == 6
