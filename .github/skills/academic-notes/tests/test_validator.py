import importlib.util
import os
import textwrap
from pathlib import Path

import pytest

# load validator module by filesystem path
spec = importlib.util.spec_from_file_location(
    "validate_academic",
    os.path.abspath(".github/skills/academic-notes/validate_academic.py"),
)
validate_academic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate_academic)


@pytest.fixture
def tmp_course_file(tmp_path):
    return tmp_path / "course.md"


def run_check(text, content=True):
    errs, extras = validate_academic.check_markdown_file(
        Path("dummy.md"), content_checks=content
    )
    return errs, extras


def test_nested_list_error(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        - ELEC 1100
          - ELEC 1100 / foo
            - bar ::@:: baz
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("nested list item does not include full path" in e for e in errs)


def test_flatten_single_child(tmp_course_file):
    # slider test: if parent has single child and no own gloss, it should not error
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        - ELEC 1100
          - ELEC 1100 / foo
            - ELEC 1100 / foo / bar ::@:: baz
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert not errs


def test_asterisk_emphasis_error(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        This sentence uses *asterisk italics* and also **bold**.
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("asterisk-based emphasis" in e for e in errs)


def test_unit_outside_math_error(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        A resistor of 5 kΩ dissipates 0.125 W when 5 V is applied.
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("unit" in e and "outside math" in e for e in errs)


def test_qa_list_without_separator_error(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        - ELEC 1100
          - What is foo? ::@:: A
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("QA-style flashcard list" in e for e in errs)


def test_qa_list_with_separator_no_error(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        - ELEC 1100

        ---
        Flashcards for this section are as follows:

        - What is foo? ::@:: A
        - Another Q :@: B
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert not errs


def test_multiple_separator_error(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        - ELEC 1100 / item ::@:: first ::@:: second
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("multiple flashcard separators" in e for e in errs)


def test_missing_horizontal_rule_error(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        ## Topic
        Some explanation text.
        - ELEC 1100 / Topic ::@:: definition
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("should be preceded by a '---' separator" in e for e in errs)


def test_br_space_error(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        - ELEC 1100 / bib ::@:: Author(Year)<br/>Title
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("preceding space" in e for e in errs)


def test_session_without_flashcards_error(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        ## week 1 lecture 1
        - datetime: 2026-02-01T10:00:00+08:00/2026-02-01T10:50:00+08:00
        - topic: introduction
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("no flashcard markers" in e for e in errs)


def test_no_datetime_error_for_lab_word(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        This note mentions lab gear and a laboratory setup.
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert not errs


def test_subheader_without_flashcards_error(tmp_course_file):
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
        ---
        tags:
         - flashcard/active/special/academia/HKUST/ELEC_1100
        ---

        ## week 1 lecture 1
        - datetime: 2026-02-01T10:00:00+08:00/2026-02-01T10:50:00+08:00
        - topic: introduction

        ### details
        This subsection has no cards.
        """
        )
    )
    errs, extras = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("has no flashcard markers" in e for e in errs)


def test_index_file_exempt_from_header_rule(tmp_course_file):
    # index pages need a header and children list; we include them here but the
    # subsequent subheader should still not trigger a flashcard error.
    tmp_course_file.write_text(
        textwrap.dedent(
            """\
    ---
    tags:
     - flashcard/active/special/academia/HKUST/ELEC_1100
    ---
    # index
    ## children
    - week1

    ## week 1 lecture 1
    - datetime: 2026-02-01T10:00:00+08:00/2026-02-01T10:50:00+08:00
    - topic: introduction

    ### details
    Nothing to card here; index files are exempt.
    """
        )
    )
    # rename file to index.md for test
    path = tmp_course_file.rename(tmp_course_file.parent / "index.md")
    errs, extras = validate_academic.check_markdown_file(path, content_checks=True)
    assert not errs


def test_template_contains_section_placeholder():
    """Ensure the course-template still uses the <section identifier> placeholder."""
    path = Path(".github/skills/academic-notes/course-template.md")
    text = path.read_text(encoding="utf-8")
    assert "<section identifier>" in text
