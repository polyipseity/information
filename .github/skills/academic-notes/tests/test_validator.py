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
