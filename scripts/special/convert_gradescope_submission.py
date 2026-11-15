#!/usr/bin/env python
"""Convert Gradescope submission pages to YAML.

A ``View Submission`` page carries the grade, the per-question scores, and the
answer given to each question, so it converts to the same shape the Canvas
converter emits: ``course``, ``assignment``, ``grade``, and ``questions``.
A page that is still being edited carries the answers but no grade, and its
question list converts the same way.
"""

from collections.abc import Mapping, Sequence
from io import StringIO
from re import Pattern
from re import compile as re_compile
from sys import stderr

from anyio import Path
from asyncer import runnify
from bs4 import BeautifulSoup, Tag
from yaml import safe_dump

"""Exported names from this module (none: standalone script, not importable as a library)."""
__all__ = ()

"Path of a Gradescope assignment or submission page, as the saved page records it."
_URL_RE: Pattern[str] = re_compile(
    r"url: https://([^/]+)/courses/(\d+)/assignments/(\d+)(?:/submissions/(\d+|new))?"
)

"The heading id of a leaf question, which carries the question's own index."
_INDEX_RE: Pattern[str] = re_compile(r"^Question_(?P<index>[\d.]+)_heading$")

"A points label, `2 Points` or `18 Points`."
_POINTS_RE: Pattern[str] = re_compile(r"(?P<points>\d+(?:\.\d+)?)\s+[Pp]oint")

"The score line of the whole submission, `30 / 30 pts`."
_TOTAL_RE: Pattern[str] = re_compile(
    r"(?P<entered>\d+(?:\.\d+)?)\s*/\s*(?P<possible>\d+(?:\.\d+)?)"
)


def clean_text(text: str) -> str:
    """Collapse the runs of whitespace a rendered page leaves in its text."""
    return " ".join(text.split())


def inline_text(element: Tag) -> str:
    """Return *element*'s text, each rendered formula restored to its TeX source.

    A formula reaches the page as rendered markup whose TeX survives in an
    annotation, so reading the text alone would record a jumble of glyphs.
    """
    for math_ele in element.select(".math"):
        annotation = math_ele.select_one("annotation")
        if annotation is not None:
            math_ele.replace_with(f"${annotation.get_text()}$")
    return clean_text(element.get_text())


def parse_number(text: str) -> int | float | None:
    """Return *text* as a number, or ``None`` when it carries none."""
    match = re_compile(r"-?\d+(?:\.\d+)?").search(text)
    if match is None:
        return None
    value = float(match[0])
    return int(value) if value.is_integer() else value


def parse_scores(soup: BeautifulSoup) -> Mapping[str, int | float | None]:
    """Return the score of each leaf question, keyed by its index."""
    scores = dict[str, int | float | None]()
    for entry in soup.select(".submissionOutlineQuestion-childQuestion"):
        index_ele = entry.select_one(".submissionOutlineQuestion--index")
        score_ele = entry.select_one(".submissionOutlineQuestion--score")
        if index_ele is None or score_ele is None:
            continue
        scores[clean_text(index_ele.get_text())] = parse_number(score_ele.get_text())
    return scores


def parse_answer(body: Tag) -> str | None:
    """Return the answer given in *body*, a choice as `1. <text>` or a typed value.

    A graded answer is the ticked choice of a group of read-only radio inputs;
    a free-response answer is the text the student typed, which the page marks
    read-only once graded.  An unanswered question returns ``None``.
    """
    radios = body.select('input[type="radio"]')
    for position, radio in enumerate(radios, start=1):
        if not radio.has_attr("checked"):
            continue
        radio_id = str(radio.get("id") or "")
        label = body.select_one(f'label[for="{radio_id}"]')
        if label is None:
            return None
        text_ele = label.select_one(".markdownText")
        if text_ele is None:
            return None
        return f"{position}. {inline_text(text_ele)}"
    typed = body.select_one(".form--textInput")
    if typed is not None:
        text = clean_text(typed.get_text())
        if text:
            return text
    return None


def parse_questions(soup: BeautifulSoup) -> Sequence[Mapping[str, object]]:
    """Return every leaf question of the page, in the order the page lists them.

    A question that groups others carries both the ``--question-child`` and the
    ``--question-parent`` class, and only the leaves carry an index of their own.
    """
    scores = parse_scores(soup)
    questions = list[Mapping[str, object]]()
    for body in soup.select(".onlineAssignment--question-child"):
        if "onlineAssignment--question-parent" in (body.get("class") or []):
            continue
        heading = body.select_one(".questionHeading--title")
        if heading is None:
            continue
        match = _INDEX_RE.match(str(heading.get("id") or ""))
        if match is None:
            continue
        index = match["index"]
        question = dict[str, object]({"index": index})
        points_ele = body.select_one(".questionHeading--points")
        if points_ele is not None and (
            points_match := _POINTS_RE.search(points_ele.get_text())
        ):
            question["points"] = parse_number(points_match["points"])
        if (score := scores.get(index)) is not None:
            question["score"] = score
        if (answer := parse_answer(body)) is not None:
            question["answer"] = answer
        questions.append(question)
    return questions


def parse_course(soup: BeautifulSoup) -> Mapping[str, object]:
    """Return the course the page belongs to, its code and its full name."""
    course = dict[str, object]()
    code_ele = soup.select_one(".sidebar--title a")
    name_ele = soup.select_one(".sidebar--subtitle")
    if code_ele is not None and (code := clean_text(code_ele.get_text())):
        course["code"] = code
    if name_ele is not None and (name := clean_text(name_ele.get_text())):
        course["name"] = name
    return course


def parse_assignment(soup: BeautifulSoup) -> Mapping[str, object]:
    """Return the assignment header the page shows: title, status, and grade."""
    assignment = dict[str, object]()
    if (
        title_ele := soup.select_one(".submissionOutlineHeader--assignmentTitle")
    ) is not None:
        if title := clean_text(title_ele.get_text()):
            assignment["title"] = title
    if "title" not in assignment and soup.title is not None:
        page_title = clean_text(soup.title.get_text()).removesuffix(" | Gradescope")
        if page_title not in ("View Submission", "Submit"):
            assignment["title"] = page_title.removeprefix("Submit ")
    if (
        status_ele := soup.select_one(
            ".submissionOutlineHeader--statusContainer .statusIndicatorHeading"
        )
    ) is not None:
        if status := clean_text(status_ele.get_text()):
            assignment["status"] = status.casefold()
    return assignment


def parse_grade(soup: BeautifulSoup) -> Mapping[str, object] | None:
    """Return the grade the page records, or ``None`` while it is ungraded."""
    total_ele = soup.select_one(".submissionOutlineHeader--totalPoints")
    if total_ele is None:
        return None
    match = _TOTAL_RE.search(total_ele.get_text())
    if match is None:
        return None
    return {
        "entered": parse_number(match["entered"]),
        "possible": parse_number(match["possible"]),
    }


def convert(html_text: str) -> str | None:
    """Convert a Gradescope page to its YAML text, or ``None`` when it is not one."""
    url_match = _URL_RE.search(html_text)
    if url_match is None or "gradescope" not in url_match[1]:
        return None
    host, course_id, assignment_id, submission_id = url_match.groups()

    soup = BeautifulSoup(html_text, "html.parser")
    assignment = dict[str, object](parse_assignment(soup))
    assignment["id"] = int(assignment_id)
    if (grade := parse_grade(soup)) is not None:
        assignment["grade"] = grade
    assignment["questions"] = parse_questions(soup)
    if submission_id is not None and submission_id != "new":
        assignment["submissions"] = ({"id": int(submission_id)},)

    data: Mapping[str, object] = {
        "type": f"submission/Gradescope/{host}",
        "course": {"id": int(course_id), **parse_course(soup)},
        "assignment": assignment,
    }

    with StringIO() as data_io:
        safe_dump(
            data,
            data_io,
            allow_unicode=True,
            default_flow_style=False,
            encoding="UTF-8",
            sort_keys=True,
        )
        return data_io.getvalue()


async def main() -> None:
    """Prompt for an HTML file path and print the converted YAML output."""
    file_path = input("HTML file? ")

    file_text = await Path(file_path).read_text()
    result = convert(file_text)

    if result is None:
        return exit(1)
    print(result, file=stderr, end="")

    return exit(0)


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
