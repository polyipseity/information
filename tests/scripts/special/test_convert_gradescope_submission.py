"""Tests for scripts/special/convert_gradescope_submission.py.

The fixtures below are cut from a real ``View Submission`` page and a real
``Submit`` page, keeping the markup the converter reads and nothing else.
"""

from collections.abc import Mapping
from typing import TypedDict

from yaml import safe_load

from scripts.special import convert_gradescope_submission as _mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

"""A graded submission page: header, outline scores, and two leaf questions."""
GRADED_PAGE = """<!doctype html>
<html><head><title>View Submission | Gradescope</title></head><body>
<!-- url: https://www.gradescope.com/courses/1384476/assignments/8790744/submissions/436096084 -->
<div class="sidebar--title sidebar--title-course"><a href="/courses/1384476">ELEC 3120</a></div>
<div class="sidebar--subtitle">Computer Networks</div>
<div class="submissionOutlineHeader">
  <h1 class="submissionOutlineHeader--assignmentTitle">Homework 2</h1>
  <div class="submissionOutlineHeader--statusContainer">
    <div class="statusIndicatorHeading statusIndicatorHeading-small">Graded</div>
  </div>
  <p class="submissionOutlineHeader--totalPoints">30 / 30 pts</p>
  <ul><li class="submissionOutlineHeader--groupMember">A Student</li></ul>
</div>
<li class="submissionOutlineQuestion submissionOutlineQuestion-childQuestion">
  <span class="submissionOutlineQuestion--index">1.1</span>
  <span class="submissionOutlineQuestion--weightAndScore">
    <span class="submissionOutlineQuestion--score">2</span> / 2 pts
  </span>
</li>
<li class="submissionOutlineQuestion submissionOutlineQuestion-childQuestion">
  <span class="submissionOutlineQuestion--index">2.1</span>
  <span class="submissionOutlineQuestion--weightAndScore">
    <span class="submissionOutlineQuestion--score">3</span> / 3 pts
  </span>
</li>
<div class="onlineAssignment--question onlineAssignment--question-child onlineAssignment--question-parent">
  <h2 class="questionHeading--title" id="Question_1_heading">Q1 Warmup</h2>
  <span class="questionHeading--points">18 Points</span>
</div>
<div class="onlineAssignment--question onlineAssignment--question-child">
  <h3 class="questionHeading--title questionHeading--title-child"
      id="Question_1.1_heading">Q1.1 Multiplexing?</h3>
  <span class="questionHeading--points">2 Points</span>
  <div class="form--radioOptions">
    <span class="form--choice"><input checked id="q11_Both" type="radio">
      <label for="q11_Both"><span class="sr-only">Choice 1 of 2: </span><span
        class="markdownText markdownText-inline"><span
        class="markdownText-inline--paragraph">Both</span></span></label></span>
    <span class="form--choice"><input disabled id="q11_TCP" type="radio">
      <label for="q11_TCP"><span class="sr-only">Choice 2 of 2: </span><span
        class="markdownText markdownText-inline"><span
        class="markdownText-inline--paragraph">TCP</span></span></label></span>
  </div>
</div>
<div class="onlineAssignment--question onlineAssignment--question-child">
  <h3 class="questionHeading--title questionHeading--title-child"
      id="Question_2.1_heading">Q2.1 </h3>
  <span class="questionHeading--points">3 Points</span>
  <div class="form--group"><div class="form--textInput form--textInput-readOnly">
    <span>140625</span></div></div>
</div>
<div class="onlineAssignment--question onlineAssignment--question-child">
  <h3 class="questionHeading--title questionHeading--title-child"
      id="Question_2.2_heading">Q2.2 Throughput?</h3>
  <span class="questionHeading--points">2 Points</span>
  <div class="form--radioOptions">
    <span class="form--choice"><input disabled id="q22_A" type="radio">
      <label for="q22_A"><span class="sr-only">Choice 1 of 4: </span><span
        class="markdownText markdownText-inline"><span
        class="markdownText-inline--paragraph">one</span></span></label></span>
    <span class="form--choice"><input disabled id="q22_B" type="radio">
      <label for="q22_B"><span class="sr-only">Choice 2 of 4: </span><span
        class="markdownText markdownText-inline"><span
        class="markdownText-inline--paragraph">two</span></span></label></span>
    <span class="form--choice"><input checked id="q22_C" type="radio">
      <label for="q22_C"><span class="sr-only">Choice 3 of 4: </span><span
        class="markdownText markdownText-inline"><span
        class="markdownText-inline--paragraph"><span class="math"><math><semantics>
        <annotation encoding="application/x-tex">\\frac{C}{\\sqrt{p}}</annotation>
        </semantics></math></span></span></span></label></span>
  </div>
</div>
</body></html>
"""

"""A page still being edited: no header, no grade, and `/submissions/new`."""
DRAFT_PAGE = """<!doctype html>
<html><head><title>Submit Homework 2 | Gradescope</title></head><body>
<!-- url: https://www.gradescope.com/courses/1384476/assignments/8790744/submissions/new -->
<div class="sidebar--title sidebar--title-course"><a>ELEC 3120</a></div>
<div class="sidebar--subtitle">Computer Networks</div>
<div class="onlineAssignment--question onlineAssignment--question-child">
  <h3 class="questionHeading--title questionHeading--title-child"
      id="Question_1.1_heading">Q1.1 Multiplexing?</h3>
  <span class="questionHeading--points">2 Points</span>
  <div class="form--radioOptions">
    <span class="form--choice"><input checked id="q11_Both" type="radio">
      <label for="q11_Both"><span class="sr-only">Choice 1 of 2: </span><span
        class="markdownText markdownText-inline"><span
        class="markdownText-inline--paragraph">Both</span></span></label></span>
  </div>
</div>
</body></html>
"""


class QuestionYaml(TypedDict, total=False):
    """One leaf question as the YAML records it."""

    index: str
    points: int | float
    score: int | float
    answer: str


class AssignmentYaml(TypedDict, total=False):
    """The assignment block of a converted page."""

    id: int
    title: str
    status: str
    grade: Mapping[str, object]
    questions: list[QuestionYaml]
    submissions: list[Mapping[str, int]]


class PageYaml(TypedDict):
    """The YAML shape a converted page carries."""

    type: str
    course: Mapping[str, object]
    assignment: AssignmentYaml


def converted(page: str) -> PageYaml:
    """Return the YAML *page* converts to, as a mapping."""
    result = _mod.convert(page)
    assert result is not None
    return safe_load(result)


def test_a_gradescope_page_converts() -> None:
    """The page type names the host, and the ids come from the page URL."""
    data = converted(GRADED_PAGE)
    assert data["type"] == "submission/Gradescope/www.gradescope.com"
    assert data["course"] == {
        "code": "ELEC 3120",
        "id": 1384476,
        "name": "Computer Networks",
    }
    assert data["assignment"]["id"] == 8790744


def test_the_header_records_grade_and_status() -> None:
    """The outline header carries the title, the status word and the score."""
    assignment = converted(GRADED_PAGE)["assignment"]
    assert assignment["title"] == "Homework 2"
    assert assignment["status"] == "graded"
    assert assignment["grade"] == {"entered": 30, "possible": 30}


def test_only_leaf_questions_are_listed() -> None:
    """A group question carries the parent class too, and has no index of its own."""
    questions = converted(GRADED_PAGE)["assignment"]["questions"]
    assert [question["index"] for question in questions] == ["1.1", "2.1", "2.2"]


def test_a_ticked_choice_is_recorded_with_its_number() -> None:
    """A choice answer carries the position the page lists it at, as a note would."""
    questions = converted(GRADED_PAGE)["assignment"]["questions"]
    assert questions[0]["answer"] == "1. Both"


def test_a_typed_answer_is_recorded_as_written() -> None:
    """A free-response answer is the text the student typed."""
    questions = converted(GRADED_PAGE)["assignment"]["questions"]
    assert questions[1]["answer"] == "140625"


def test_a_formula_answer_keeps_its_tex() -> None:
    """The rendered glyphs are replaced by the annotation the page carries."""
    questions = converted(GRADED_PAGE)["assignment"]["questions"]
    assert questions[2]["answer"] == "3. $\\frac{C}{\\sqrt{p}}$"


def test_an_outline_score_reaches_its_question() -> None:
    """The score sits in the outline and is matched to the question by index."""
    questions = converted(GRADED_PAGE)["assignment"]["questions"]
    assert (questions[0]["points"], questions[0]["score"]) == (2, 2)
    assert questions[2]["points"] == 2
    assert "score" not in questions[2]


def test_a_graded_page_names_its_submission() -> None:
    """The submission id in the URL is the id the page was graded from."""
    assignment = converted(GRADED_PAGE)["assignment"]
    assert assignment["submissions"] == [{"id": 436096084}]


def test_a_draft_page_records_no_grade() -> None:
    """Nothing has been graded, so the grade and the submission both stay out."""
    assignment = converted(DRAFT_PAGE)["assignment"]
    assert "grade" not in assignment
    assert "submissions" not in assignment
    assert assignment["title"] == "Homework 2"


def test_an_unrelated_page_is_not_converted() -> None:
    """A page with no Gradescope URL carries nothing this converter reads."""
    assert _mod.convert("<html><body>nothing</body></html>") is None


def test_a_canvas_page_is_left_to_the_canvas_converter() -> None:
    """Canvas pages share the URL shape, so the host decides."""
    page = """<html><body>
<!-- url: https://canvas.ust.hk/courses/70004/assignments/425438 -->
</body></html>"""
    assert _mod.convert(page) is None
