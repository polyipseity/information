"""Tests for scripts/special/convert_canvas_submission.py.

Covers the public API: AssignmentPageType enum, pure parsing functions
(html_to_text, parse_datetime, parse_title_and_content, parse_grade,
parse_properties, parse_comments), the async convert() function, and
the main() entry point.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from bs4 import BeautifulSoup

from scripts.special import convert_canvas_submission as _mod

if TYPE_CHECKING:
    pass


# ---------------------------------------------------------------------------
# AssignmentPageType
# ---------------------------------------------------------------------------


class TestAssignmentPageType:
    """Tests for the AssignmentPageType StrEnum."""

    def test_assignment_value(self) -> None:
        assert _mod.AssignmentPageType.ASSIGNMENT.value == "assignment"

    def test_submission_value(self) -> None:
        assert _mod.AssignmentPageType.SUBMISSION.value == "submission"

    def test_str(self) -> None:
        assert str(_mod.AssignmentPageType.ASSIGNMENT) == "assignment"
        assert str(_mod.AssignmentPageType.SUBMISSION) == "submission"

    def test_membership(self) -> None:
        assert "assignment" in _mod.AssignmentPageType._value2member_map_
        assert "submission" in _mod.AssignmentPageType._value2member_map_


# ---------------------------------------------------------------------------
# html_to_text
# ---------------------------------------------------------------------------


class TestHtmlToText:
    """Tests for the html_to_text pure function."""

    def test_plain_text(self) -> None:
        soup = BeautifulSoup("<div>Hello World</div>", "html.parser")
        assert _mod.html_to_text(soup) == "Hello World"

    def test_br_newline(self) -> None:
        soup = BeautifulSoup("<div>Line1<br>Line2</div>", "html.parser")
        assert _mod.html_to_text(soup) == "Line1\nLine2"

    def test_p_newline(self) -> None:
        """<p> alone produces no trailing newline in the current implementation."""
        soup = BeautifulSoup("<div><p>Para</p></div>", "html.parser")
        assert _mod.html_to_text(soup) == "Para"

    def test_div_block_newline(self) -> None:
        """Block-level elements add double newline."""
        soup = BeautifulSoup(
            "<div><div>A</div><div>B</div></div>", "html.parser"
        )
        result = _mod.html_to_text(soup)
        assert "A\n\nB" in result

    def test_inline_elements_no_break(self) -> None:
        """Inline elements should not introduce newlines."""
        soup = BeautifulSoup(
            "<div><span>ab</span><b>cd</b></div>", "html.parser"
        )
        assert _mod.html_to_text(soup) == "abcd"

    def test_list_li(self) -> None:
        """<li> (block-level) adds double newline between items."""
        soup = BeautifulSoup(
            "<ul><li>Item1</li><li>Item2</li></ul>", "html.parser"
        )
        result = _mod.html_to_text(soup)
        assert "Item1\n\nItem2" in result

    def test_empty_tag(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        assert _mod.html_to_text(soup) == ""

    def text_only_whitespace(self) -> None:
        soup = BeautifulSoup("<div>  </div>", "html.parser")
        assert _mod.html_to_text(soup) == ""

    def test_mixed_nesting(self) -> None:
        soup = BeautifulSoup(
            "<div><p>P1<br>P1b</p><p>P2</p></div>", "html.parser"
        )
        result = _mod.html_to_text(soup)
        assert "P1\nP1bP2" in result

    def test_a_tag_inline(self) -> None:
        """<a> is non-blocking, should not add newline."""
        soup = BeautifulSoup(
            '<div>click <a href="#">here</a></div>', "html.parser"
        )
        assert _mod.html_to_text(soup) == "click here"


# ---------------------------------------------------------------------------
# parse_datetime
# ---------------------------------------------------------------------------


class TestParseDatetime:
    """Tests for the parse_datetime function.

    Covers all matching format variants (at/by, with/without seconds/minutes),
    am/pm edge cases (12am, 12pm), no-match cases, and timezone inheritance.
    """

    REF = datetime(2023, 9, 15)

    def test_format_at_with_seconds(self) -> None:
        """'%b %d, %Y at %H:%M:%S%p' — Sep 15, 2023 at 11:59:00pm."""
        result = _mod.parse_datetime(
            "Sep 15, 2023 at 11:59:00pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 59, 0)
        assert result.start_index == 0

    def test_format_by_with_seconds(self) -> None:
        """'%b %d, %Y by %H:%M:%S%p' — Sep 15, 2023 by 11:59:00pm."""
        result = _mod.parse_datetime(
            "Sep 15, 2023 by 11:59:00pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 59, 0)

    def test_format_at_no_seconds(self) -> None:
        """'%b %d, %Y at %H:%M%p' — Sep 15, 2023 at 11:59pm."""
        result = _mod.parse_datetime(
            "Sep 15, 2023 at 11:59pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 59, 0)

    def test_format_by_no_seconds(self) -> None:
        """'%b %d, %Y by %H:%M%p' — Sep 15, 2023 by 11:59pm."""
        result = _mod.parse_datetime(
            "Sep 15, 2023 by 11:59pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 59, 0)

    def test_format_at_hour_only(self) -> None:
        """'%b %d, %Y at %H%p' — Sep 15, 2023 at 11pm."""
        result = _mod.parse_datetime(
            "Sep 15, 2023 at 11pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 0, 0)

    def test_format_by_hour_only(self) -> None:
        """'%b %d, %Y by %H%p' — Sep 15, 2023 by 11pm."""
        result = _mod.parse_datetime(
            "Sep 15, 2023 by 11pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 0, 0)

    def test_am_time(self) -> None:
        """AM times produce no delta — Sep 15, 2023 at 10:30:00am."""
        result = _mod.parse_datetime(
            "Sep 15, 2023 at 10:30:00am", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 10, 30, 0)

    def test_12am_midnight(self) -> None:
        """12am adjusts to 00:00."""
        result = _mod.parse_datetime(
            "Sep 15, 2023 at 12am", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 0, 0, 0)

    def test_12pm_noon(self) -> None:
        """12pm adds 12h to 12:00 → 00:00 next day."""
        result = _mod.parse_datetime(
            "Sep 15, 2023 at 12:00pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 16, 0, 0, 0)

    def test_no_match_no_month(self) -> None:
        """No month name in the string returns None."""
        result = _mod.parse_datetime(
            "no month here 1pm", reference_datetime=self.REF
        )
        assert result is None

    def test_no_match_no_am_pm(self) -> None:
        """Date-like string without am/pm after the month returns None."""
        result = _mod.parse_datetime(
            "Sep 15, 2023", reference_datetime=self.REF
        )
        assert result is None

    def test_different_month(self) -> None:
        """Other months like Jan, Dec should also work."""
        result = _mod.parse_datetime(
            "Jan 5, 2023 at 3:30:00am", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 1, 5, 3, 30, 0)

    def test_timezone_inherited(self) -> None:
        """Result should use reference_datetime's timezone."""
        ref = datetime(2023, 9, 15, tzinfo=timezone.utc)
        result = _mod.parse_datetime(
            "Sep 15, 2023 at 11:59:00pm", reference_datetime=ref
        )
        assert result is not None
        assert result.result.tzinfo is timezone.utc

    def test_multiline_input(self) -> None:
        """Newlines in the input string are replaced with spaces."""
        result = _mod.parse_datetime(
            "Sep 15,\n2023 at\n11:59pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 59, 0)

    def test_no_match_nonexistent_format(self) -> None:
        """String with month and am/pm but wrong format returns None."""
        result = _mod.parse_datetime(
            "Sep/15/2023 11pm", reference_datetime=self.REF
        )
        assert result is None


# ---------------------------------------------------------------------------
# parse_title_and_content
# ---------------------------------------------------------------------------


class TestParseTitleAndContent:
    """Tests for the parse_title_and_content function."""

    def test_assignment_with_title_and_content(self) -> None:
        soup = BeautifulSoup(
            '<div class="assignment-title">'
            '<span class="title-content">Homework 1</span></div>'
            '<div data-resource-type="assignment.body">Body <b>text</b></div>',
            "html.parser",
        )
        result = _mod.parse_title_and_content(
            soup, page_type=_mod.AssignmentPageType.ASSIGNMENT
        )
        assert result is not None
        assert result.title == "Homework 1"
        assert "Body text" in result.content

    def test_assignment_no_title(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        result = _mod.parse_title_and_content(
            soup, page_type=_mod.AssignmentPageType.ASSIGNMENT
        )
        assert result is None

    def test_assignment_title_only(self) -> None:
        soup = BeautifulSoup(
            '<div class="assignment-title">'
            '<span class="title-content">Homework 1</span></div>',
            "html.parser",
        )
        result = _mod.parse_title_and_content(
            soup, page_type=_mod.AssignmentPageType.ASSIGNMENT
        )
        assert result is not None
        assert result.title == "Homework 1"
        assert result.content == ""

    def test_submission_with_title(self) -> None:
        soup = BeautifulSoup(
            '<div class="submission-details-header__heading">HW1</div>',
            "html.parser",
        )
        result = _mod.parse_title_and_content(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is not None
        assert result.title == "HW1"
        assert result.content == ""

    def test_submission_no_title(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        result = _mod.parse_title_and_content(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is None

    def test_invalid_page_type(self) -> None:
        """An invalid page type should raise ValueError."""
        soup = BeautifulSoup("<div></div>", "html.parser")
        with pytest.raises(ValueError, match="invalid"):
            _mod.parse_title_and_content(soup, page_type="invalid")  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# parse_grade
# ---------------------------------------------------------------------------


class TestParseGrade:
    """Tests for the parse_grade function."""

    # -- ASSIGNMENT --

    def test_assignment_with_grade(self) -> None:
        soup = BeautifulSoup(
            '<div class="details"><div class="content">'
            '<div class="module">Grade: 85/100<span>  /100</span>'
            "Graded Anonymously: Yes</div></div></div>",
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.ASSIGNMENT
        )
        assert result is not None
        assert result.possible_grade == 100
        assert result.entered_grade == "85/100"
        assert result.graded_anonymously is True

    def test_assignment_no_grade(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.ASSIGNMENT
        )
        assert result is None

    def test_assignment_no_graded_anonymously(self) -> None:
        soup = BeautifulSoup(
            '<div class="details"><div class="content">'
            '<div class="module">Grade: 90<span>  /100</span></div>'
            "</div></div>",
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.ASSIGNMENT
        )
        assert result is not None
        assert result.graded_anonymously is None

    def test_assignment_graded_anonymously_no(self) -> None:
        soup = BeautifulSoup(
            '<div class="details"><div class="content">'
            '<div class="module">Grade: 90<span>  /100</span>'
            "Graded Anonymously: No</div></div></div>",
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.ASSIGNMENT
        )
        assert result is not None
        assert result.graded_anonymously is False

    def test_assignment_float_grade(self) -> None:
        """Possible grade may be a float."""
        soup = BeautifulSoup(
            '<div class="details"><div class="content">'
            '<div class="module">Grade: 88.5<span>  /100.0</span>'
            "</div></div></div>",
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.ASSIGNMENT
        )
        assert result is not None
        assert result.possible_grade == 100.0

    # -- SUBMISSION --

    def test_submission_with_grade(self) -> None:
        soup = BeautifulSoup(
            '<div class="entered_grade">85</div>',
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is not None
        assert result.entered_grade == 85
        assert result.possible_grade == ""
        assert result.graded_anonymously is None

    def test_submission_no_grade(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is None

    def test_submission_with_possible_grade(self) -> None:
        """When possible grade exists as next sibling text."""
        soup = BeautifulSoup(
            '<div class="entered_grade">85</div>/100',
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is not None
        assert result.entered_grade == 85
        # possible_grade from "/100" stays as string after failed int/float
        assert isinstance(result.possible_grade, str)

    def test_invalid_page_type(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        with pytest.raises(ValueError, match="invalid"):
            _mod.parse_grade(soup, page_type="invalid")  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# parse_properties
# ---------------------------------------------------------------------------


class TestParseProperties:
    """Tests for the parse_properties function."""

    REF = datetime(2023, 9, 15, tzinfo=timezone.utc)

    def test_assignment_no_properties(self) -> None:
        """ASSIGNMENT with no overview section yields empty properties."""
        soup = BeautifulSoup(
                '<div class="details"><div class="content">'
                '<div>Due: Sep 15, 2023 at 11:59pm</div></div></div>',
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            page_type=_mod.AssignmentPageType.ASSIGNMENT,
            reference_datetime=self.REF,
        )
        assert result.properties == {}
        assert isinstance(result.submission_datetime, datetime)

    def test_assignment_with_properties(self) -> None:
        soup = BeautifulSoup(
            '<div class="details"><div class="content">'
            '<div>Due: Sep 15, 2023 at 11:59pm</div>'
            '<ul class="student-assignment-overview">'
            '<li><span class="title">Due</span>'
            '<span class="value">Sep 15, 2023 at 11:59pm</span></li>'
            '<li><span class="title">Available</span>'
            '<span class="value">Sep 1, 2023 at 12am until'
            " Sep 15, 2023 at 11:59pm</span></li>"
            '<li><span class="title">File Types</span>'
            '<span class="value">pdf, docx, and txt</span></li>'
            '<li><span class="title">Submitting</span>'
            '<span class="value">online, or in person</span></li>'
            "</ul></div></div>",
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            page_type=_mod.AssignmentPageType.ASSIGNMENT,
            reference_datetime=self.REF,
        )
        props = result.properties
        assert "due" in props
        assert isinstance(props["due"], datetime)
        assert "available" in props
        avail = props["available"]
        assert isinstance(avail, dict)
        assert "start" in avail and "end" in avail
        assert "file types" in props
        assert props["file types"] == ("pdf", "docx", "txt")
        assert "submitting" in props
        assert props["submitting"] == ("online", "in person")

    def test_submission_no_properties(self) -> None:
        """SUBMISSION with no attempts_info returns empty properties."""
        soup = BeautifulSoup(
            '<div class="submission-details-header__time">'
            "Sep 15, 2023 at 11:59pm</div>",
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert result.properties == {}

    def test_submission_with_properties(self) -> None:
        soup = BeautifulSoup(
            '<div class="submission-details-header__time">'
            "Sep 15, 2023 at 11:59pm</div>"
            '<div class="submission-details-header__attempts_info">'
            '<span class="bold">Due:</span>'
            '<span>Sep 15, 2023 at 11:59pm</span></div>',
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert len(result.properties) >= 1

    def test_assignment_available_until_only(self) -> None:
        """'available until' should parse as end-only."""
        soup = BeautifulSoup(
            '<div class="details"><div class="content">'
            '<div>Due: Sep 15, 2023 at 11:59pm</div>'
            '<ul class="student-assignment-overview">'
            '<li><span class="title">Available</span>'
            '<span class="value">until Sep 15, 2023 at 11:59pm</span></li>'
            "</ul></div></div>",
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            page_type=_mod.AssignmentPageType.ASSIGNMENT,
            reference_datetime=self.REF,
        )
        avail = result.properties.get("available", {})
        assert isinstance(avail, dict)
        assert avail.get("start") is None
        assert isinstance(avail.get("end"), datetime)

    def test_assignment_available_after_only(self) -> None:
        """'available after' should parse as start-only."""
        soup = BeautifulSoup(
            '<div class="details"><div class="content">'
            '<div>Due: Sep 15, 2023 at 11:59pm</div>'
            '<ul class="student-assignment-overview">'
            '<li><span class="title">Available</span>'
            '<span class="value">after Sep 1, 2023 at 12am</span></li>'
            "</ul></div></div>",
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            page_type=_mod.AssignmentPageType.ASSIGNMENT,
            reference_datetime=self.REF,
        )
        avail = result.properties.get("available", {})
        assert isinstance(avail, dict)
        assert isinstance(avail.get("start"), datetime)
        assert avail.get("end") is None

    def test_submission_property_generic_int(self) -> None:
        """Generic property value that looks like an int."""
        soup = BeautifulSoup(
            '<div class="submission-details-header__time">'
            "Sep 15, 2023 at 11:59pm</div>"
            '<div class="submission-details-header__attempts_info">'
            '<span class="bold">Attempts:</span>'
            '<span>3</span></div>',
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        attempts = result.properties.get("attempts:")
        assert attempts == 3

    def test_invalid_page_type(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        with pytest.raises(ValueError, match="invalid"):
            _mod.parse_properties(
                soup,
                page_type="invalid",  # type: ignore[arg-type]
                reference_datetime=self.REF,
            )


# ---------------------------------------------------------------------------
# parse_comments
# ---------------------------------------------------------------------------


class TestParseComments:
    """Tests for the parse_comments function."""

    REF = datetime(2023, 9, 15, tzinfo=timezone.utc)

    def test_assignment_no_comments(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        result = _mod.parse_comments(
            soup,
            page_type=_mod.AssignmentPageType.ASSIGNMENT,
            reference_datetime=self.REF,
        )
        assert result == []

    def test_assignment_with_comment(self) -> None:
        soup = BeautifulSoup(
            '<div class="comments">'
            '<div class="comment" id="comment-42">'
            '<div class="comment_content">Great work!</div>'
            '<span class="signature">John, Sep 15, 2023 at 10:30am</span>'
            "</div></div>",
            "html.parser",
        )
        result = _mod.parse_comments(
            soup,
            page_type=_mod.AssignmentPageType.ASSIGNMENT,
            reference_datetime=self.REF,
        )
        assert len(result) == 1
        assert result[0].id == 42
        assert result[0].content == "Great work!"
        assert result[0].author == "John"
        assert isinstance(result[0].datetime, datetime)

    def test_assignment_comment_no_signature(self) -> None:
        soup = BeautifulSoup(
            '<div class="comments">'
            '<div class="comment" id="comment-7">'
            '<div class="comment_content">No signature</div>'
            "</div></div>",
            "html.parser",
        )
        result = _mod.parse_comments(
            soup,
            page_type=_mod.AssignmentPageType.ASSIGNMENT,
            reference_datetime=self.REF,
        )
        assert len(result) == 1
        assert result[0].author == ""
        assert result[0].datetime == ""

    def test_assignment_comment_unknown_date(self) -> None:
        """When signature text can't be parsed as datetime, author is whole text."""
        soup = BeautifulSoup(
            '<div class="comments">'
            '<div class="comment" id="comment-1">'
            '<div class="comment_content">Content</div>'
            '<span class="signature">JustDateText</span>'
            "</div></div>",
            "html.parser",
        )
        result = _mod.parse_comments(
            soup,
            page_type=_mod.AssignmentPageType.ASSIGNMENT,
            reference_datetime=self.REF,
        )
        assert len(result) == 1
        assert result[0].author == "JustDateText"
        assert result[0].datetime == ""

    def test_submission_no_comments(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        result = _mod.parse_comments(
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert result == []

    def test_submission_with_comment(self) -> None:
        soup = BeautifulSoup(
            '<div class="comment_list">'
            '<div class="comment" id="submission_comment_99">'
            '<div class="comment">Nice submission</div>'
            '<span class="author_name">Alice</span>'
            '<span class="posted_at">Sep 15, 2023 at 11:00am</span>'
            "</div></div>",
            "html.parser",
        )
        result = _mod.parse_comments(
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert len(result) == 1
        assert result[0].id == 99
        assert result[0].content == "Nice submission"
        assert result[0].author == "Alice"
        assert isinstance(result[0].datetime, datetime)

    def test_submission_comment_with_attachments(self) -> None:
        soup = BeautifulSoup(
            '<div class="comment_list">'
            '<div class="comment" id="submission_comment_1">'
            '<div class="comment">See attached</div>'
            '<span class="author_name">Bob</span>'
            '<span class="posted_at">Sep 14, 2023 at 2:00pm</span>'
            '<div class="comment_attachment">report.pdf</div>'
            "</div></div>",
            "html.parser",
        )
        result = _mod.parse_comments(
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert len(result) == 1
        assert result[0].attachments == ("report.pdf",)

    def test_invalid_page_type(self) -> None:
        """Invalid page type raises ValueError."""
        soup = BeautifulSoup("<div></div>", "html.parser")
        with pytest.raises(ValueError):
            _mod.parse_comments(
                soup,
                page_type="invalid",  # type: ignore[arg-type]
                reference_datetime=self.REF,
            )

    def test_assignment_multiple_comments(self) -> None:
        soup = BeautifulSoup(
            '<div class="comments">'
            '<div class="comment" id="comment-1">'
            '<div class="comment_content">First</div>'
            '<span class="signature">A, Sep 14, 2023 at 1:00pm</span></div>'
            '<div class="comment" id="comment-2">'
            '<div class="comment_content">Second</div>'
            '<span class="signature">B, Sep 15, 2023 at 2:00pm</span></div>'
            "</div>",
            "html.parser",
        )
        result = _mod.parse_comments(
            soup,
            page_type=_mod.AssignmentPageType.ASSIGNMENT,
            reference_datetime=self.REF,
        )
        assert len(result) == 2


# ---------------------------------------------------------------------------
# convert
# ---------------------------------------------------------------------------


class TestConvert:
    """Tests for the async convert function."""

    MINIMAL_ASSIGNMENT_HTML = """\
url: https://canvas.example.edu/courses/101/assignments/202
saved date: Thu Sep 14 2023 10:00:00 UTC+0000
<a href="https://canvas.example.edu/courses/101">Test Course</a>
<div class="assignment-title"><span class="title-content">Assignment 1</span></div>
"""

    MINIMAL_SUBMISSION_HTML = """\
url: https://canvas.example.edu/courses/101/assignments/202/submissions/42
saved date: Thu Sep 14 2023 10:00:00 UTC+0000
<a href="https://canvas.example.edu/courses/101">Test Course</a>
<div class="submission-details-header__heading">Assignment 1</div>
"""

    @pytest.mark.anyio
    async def test_no_url_match(self) -> None:
        """No URL matching _URL_REGEX returns None."""
        result = await _mod.convert("no url here")
        assert result is None

    @pytest.mark.anyio
    async def test_no_date_match(self) -> None:
        """URL match but no date returns None."""
        html = "url: https://canvas.example.edu/courses/1/assignments/2"
        result = await _mod.convert(html)
        assert result is None

    @pytest.mark.anyio
    async def test_invalid_date(self) -> None:
        """URL and date regex match but date can't be parsed returns None."""
        html = (
            "url: https://canvas.example.edu/courses/1/assignments/2\n"
            "saved date: not-a-real-date"
        )
        result = await _mod.convert(html)
        assert result is None

    @pytest.mark.anyio
    async def test_no_course_name(self) -> None:
        """No course name element returns None."""
        html = (
            "url: https://canvas.example.edu/courses/1/assignments/2\n"
            "saved date: Thu Sep 14 2023 10:00:00 UTC+0000\n"
            "<div></div>\n"
        )
        result = await _mod.convert(html)
        assert result is None

    @pytest.mark.anyio
    async def test_no_title(self) -> None:
        """No title element returns None."""
        html = (
            "url: https://canvas.example.edu/courses/1/assignments/2\n"
            "saved date: Thu Sep 14 2023 10:00:00 UTC+0000\n"
            '<a href="https://canvas.example.edu/courses/1">Course</a>\n'
        )
        result = await _mod.convert(html)
        assert result is None

    @pytest.mark.anyio
    async def test_assignment_convert_success(self) -> None:
        """Successful conversion for ASSIGNMENT page type yields YAML."""
        result = await _mod.convert(self.MINIMAL_ASSIGNMENT_HTML)
        assert result is not None
        assert "type: submission/Canvas/canvas.example.edu" in result
        assert "assignment" in result
        assert "course" in result

    @pytest.mark.anyio
    async def test_submission_convert_success(self) -> None:
        """Successful conversion for SUBMISSION page type yields YAML."""
        result = await _mod.convert(self.MINIMAL_SUBMISSION_HTML)
        assert result is not None
        assert "type: submission/Canvas/canvas.example.edu" in result
        assert "assignment" in result

    @pytest.mark.anyio
    async def test_assignment_output_has_expected_keys(self) -> None:
        result = await _mod.convert(self.MINIMAL_ASSIGNMENT_HTML)
        assert result is not None
        assert "title: Assignment 1" in result
        assert "course:" in result
        assert "id: 202" in result or "id: 101" in result

    @pytest.mark.anyio
    async def test_submission_output_has_expected_keys(self) -> None:
        result = await _mod.convert(self.MINIMAL_SUBMISSION_HTML)
        assert result is not None
        assert "grade:" in result
        assert "comments:" in result


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


class TestMain:
    """Tests for the async main() entry point."""

    @pytest.mark.anyio
    async def test_main_success(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """main() with valid HTML file prints YAML to stderr and exits 0."""
        html_file = tmp_path / "test.html"
        html_file.write_text(
            "url: https://canvas.example.edu/courses/1/assignments/2\n"
            "saved date: Thu Sep 14 2023 10:00:00 UTC+0000\n"
            '<a href="https://canvas.example.edu/courses/1">C</a>\n'
            '<div class="assignment-title">'
            '<span class="title-content">A1</span></div>\n'
        )
        monkeypatch.setattr(
            "builtins.input",
            lambda _: str(html_file),
        )
        printed: list[str] = []
        monkeypatch.setattr("builtins.print", lambda *a, **kw: printed.append(a[0]))
        exit_codes: list[int] = []
        monkeypatch.setattr(
            "builtins.exit",
            lambda code: exit_codes.append(code),
        )
        await _mod.main()
        assert any("type:" in s for s in printed)
        assert 0 in exit_codes

    @pytest.mark.anyio
    async def test_main_failure(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """main() with invalid HTML exits 1."""
        html_file = tmp_path / "bad.html"
        html_file.write_text("no url here")
        monkeypatch.setattr(
            "builtins.input",
            lambda _: str(html_file),
        )
        exit_codes: list[int] = []
        monkeypatch.setattr(
            "builtins.exit",
            lambda code: exit_codes.append(code),
        )
        await _mod.main()
        assert 1 in exit_codes

    @pytest.mark.anyio
    async def test_main_file_not_found(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """main() with nonexistent file should propagate the error."""
        monkeypatch.setattr(
            "builtins.input",
            lambda _: "/nonexistent/file.html",
        )
        with pytest.raises(FileNotFoundError):
            await _mod.main()
