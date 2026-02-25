import importlib.util
import os
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
    file = tmp_path / "course.md"
    return file


# helper not used currently but left for possible future reuse


def run_check(text, content=True):
    errs, warns = validate_academic.check_markdown_file(
        Path("dummy.md"), content_checks=content
    )
    return errs, warns


def test_nested_list_warning(tmp_course_file):
    tmp_course_file.write_text("""---
tags:
 - flashcard/active/special/academia/HKUST/ELEC_1100
---

- ELEC 1100
  - ELEC 1100 / foo
    - bar ::@:: baz
""")
    errs, warns = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("nested list item does not include full path" in w for w in warns)


def test_flatten_single_child(tmp_course_file):
    # slider test: if parent has single child and no own gloss, it should not warn
    tmp_course_file.write_text("""---
tags:
 - flashcard/active/special/academia/HKUST/ELEC_1100
---

- ELEC 1100
  - ELEC 1100 / foo
    - ELEC 1100 / foo / bar ::@:: baz
""")
    errs, warns = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert not any("nested list item does not include full path" in w for w in warns)


def test_asterisk_emphasis_warning(tmp_course_file):
    tmp_course_file.write_text("""---
tags:
 - flashcard/active/special/academia/HKUST/ELEC_1100
---

This sentence uses *asterisk italics* and also **bold**.
""")
    errs, warns = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("asterisk-based emphasis" in w for w in warns)


def test_multi_level_grouping(tmp_course_file):
    tmp_course_file.write_text("""---
tags:
 - flashcard/active/special/academia/HKUST/ELEC_1100
---

- ELEC 1100
  - ELEC 1100 / a / b
    - ELEC 1100 / a / b / c ::@:: d
""")
    errs, warns = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert not errs
    assert not any("nested list item" in w for w in warns)


def test_qa_list_without_separator_warning(tmp_course_file):
    # simple QA pair without preceding rule should produce a warning
    tmp_course_file.write_text("""---
tags:
 - flashcard/active/special/academia/HKUST/ELEC_1100
---

- ELEC 1100
  - What is foo? ::@:: A
""")
    errs, warns = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("QA-style flashcard list" in w for w in warns)


def test_qa_list_with_separator_no_warning(tmp_course_file):
    # QA list properly prefaced by separator phrase should not warn
    tmp_course_file.write_text("""---
tags:
 - flashcard/active/special/academia/HKUST/ELEC_1100
---

- ELEC 1100

---
Flashcards for this section are as follows:

- What is foo? ::@:: A
- Another Q :@: B
""")
    errs, warns = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert not any("QA-style flashcard list" in w for w in warns)


def test_multiple_separator_warning(tmp_course_file):
    # a line with more than one separator should warn
    tmp_course_file.write_text("""---
tags:
 - flashcard/active/special/academia/HKUST/ELEC_1100
---

- ELEC 1100 / item ::@:: first ::@:: second
""")
    errs, warns = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("multiple flashcard separators" in w for w in warns)


def test_br_space_warning(tmp_course_file):
    # <br/> without preceding space should produce a warning
    tmp_course_file.write_text("""---
tags:
 - flashcard/active/special/academia/HKUST/ELEC_1100
---

- ELEC 1100 / bib ::@:: Author(Year)<br/>Title
""")
    errs, warns = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("preceding space" in w for w in warns)


def test_session_without_flashcards_warning(tmp_course_file):
    # file contains a lecture entry but no flashcard markers -> warning
    tmp_course_file.write_text("""---
tags:
 - flashcard/active/special/academia/HKUST/ELEC_1100
---

## week 1 lecture 1
- datetime: 2026-02-01T10:00:00+08:00/2026-02-01T10:50:00+08:00
- topic: introduction
""")
    errs, warns = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("no flashcard markers" in w for w in warns)


def test_subheader_without_flashcards_warning(tmp_course_file):
    # a secondary header with text but no flashcards should also trigger a warning
    tmp_course_file.write_text("""---
tags:
 - flashcard/active/special/academia/HKUST/ELEC_1100
---

## week 1 lecture 1
- datetime: 2026-02-01T10:00:00+08:00/2026-02-01T10:50:00+08:00
- topic: introduction

### details
This subsection has no cards.
""")
    errs, warns = validate_academic.check_markdown_file(
        tmp_course_file, content_checks=True
    )
    assert any("has no flashcard markers" in w for w in warns)


def test_index_file_exempt_from_header_rule(tmp_course_file):
    # index.md should not warn about missing flashcards under subheaders
    tmp_course_file.write_text("""---
    tags:
     - flashcard/active/special/academia/HKUST/ELEC_1100
    ---

    ## week 1 lecture 1
    - datetime: 2026-02-01T10:00:00+08:00/2026-02-01T10:50:00+08:00
    - topic: introduction

    ### details
    Nothing to card here; index files are exempt.
    """)
    # rename file to index.md for test
    path = tmp_course_file.rename(tmp_course_file.parent / "index.md")
    errs, warns = validate_academic.check_markdown_file(path, content_checks=True)
    assert not any("has no flashcard markers" in w for w in warns)


def test_template_contains_section_placeholder():
    """Ensure the course-template still uses the <section identifier> placeholder."""
    path = Path(".github/skills/academic-notes/course-template.md")
    text = path.read_text(encoding="utf-8")
    assert "<section identifier>" in text
