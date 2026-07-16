"""Tests for scripts/special/convert_hkust_zinc_submission.py.

Covers the public API: AssignmentPageType enum, pure parsing functions
(html_to_text, parse_datetime, parse_title_and_content, parse_grade,
parse_properties), and the async convert() function.  Note that this
module has no main() entry point.
"""

from datetime import datetime, timezone
from typing import cast

import pytest
from bs4 import BeautifulSoup

from scripts.special import convert_hkust_zinc_submission as _mod

"""Public API of this test module (empty: no symbols are exported)."""
__all__ = ()

# ---------------------------------------------------------------------------
# AssignmentPageType
# ---------------------------------------------------------------------------


class TestAssignmentPageType:
    """Tests for the AssignmentPageType StrEnum (SUBMISSION only)."""

    def test_submission_value(self) -> None:
        assert _mod.AssignmentPageType.SUBMISSION.value == "submission"

    def test_str(self) -> None:
        assert str(_mod.AssignmentPageType.SUBMISSION) == "submission"

    def test_only_submission(self) -> None:
        """Only SUBMISSION member should exist."""
        members = list(_mod.AssignmentPageType)
        assert members == [_mod.AssignmentPageType.SUBMISSION]


# ---------------------------------------------------------------------------
# html_to_text
# ---------------------------------------------------------------------------


class TestHtmlToText:
    """Tests for the html_to_text pure function (shared logic with Canvas)."""

    def test_plain_text(self) -> None:
        soup = BeautifulSoup("<div>Hello World</div>", "html.parser")
        assert _mod.html_to_text(soup) == "Hello World"

    def test_br_newline(self) -> None:
        soup = BeautifulSoup("<div>Line1<br>Line2</div>", "html.parser")
        assert _mod.html_to_text(soup) == "Line1\nLine2"

    def test_div_block_newline(self) -> None:
        soup = BeautifulSoup(
            "<div><div>A</div><div>B</div></div>", "html.parser"
        )
        result = _mod.html_to_text(soup)
        assert "A\n\nB" in result

    def test_inline_elements_no_break(self) -> None:
        soup = BeautifulSoup(
            "<div><span>ab</span><b>cd</b></div>", "html.parser"
        )
        assert _mod.html_to_text(soup) == "abcd"

    def test_empty_tag(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        assert _mod.html_to_text(soup) == ""

    def test_list_items(self) -> None:
        soup = BeautifulSoup(
            "<ul><li>A</li><li>B</li></ul>", "html.parser"
        )
        result = _mod.html_to_text(soup)
        assert "A\n\nB" in result


# ---------------------------------------------------------------------------
# parse_datetime
# ---------------------------------------------------------------------------


class TestParseDatetime:
    """Tests for the Zinc-specific parse_datetime function.

    Handles Chinese AM/PM markers (上午/下午 → am/pm), Sept → Sep
    normalisation, dd/mm/YYYY format, and dd Mon YYYY date-only format.
    """

    REF = datetime(2023, 9, 15)

    def test_dd_slash_mm_yyyy_with_seconds_pm(self) -> None:
        """'%d/%m/%Y at %H:%M:%S%p' — 15/09/2023 at 11:59:00pm."""
        result = _mod.parse_datetime(
            "15/09/2023 at 11:59:00pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 59, 0)
        assert result.start_index == 0

    def test_dd_slash_mm_yyyy_with_seconds_am(self) -> None:
        """'%d/%m/%Y at %H:%M:%S%p' — 15/09/2023 at 10:30:00am."""
        result = _mod.parse_datetime(
            "15/09/2023 at 10:30:00am", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 10, 30, 0)

    def test_12am_midnight(self) -> None:
        """12am adjusts to 00:00."""
        result = _mod.parse_datetime(
            "15/09/2023 at 12:00:00am", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 0, 0)

    def test_12pm_noon(self) -> None:
        """12pm stays at 12:00."""
        result = _mod.parse_datetime(
            "15/09/2023 at 12:00:00pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 12, 0)

    def test_chinese_pm(self) -> None:
        """下午 → pm should be replaced."""
        result = _mod.parse_datetime(
            "15/09/2023 at 11:59:00下午", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 59, 0)

    def test_chinese_am(self) -> None:
        """上午 → am should be replaced."""
        result = _mod.parse_datetime(
            "15/09/2023 at 10:30:00上午", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 10, 30, 0)

    def test_sept_to_sep(self) -> None:
        """'Sept' → 'Sep' normalisation for format '%d %b %Y'."""
        result = _mod.parse_datetime(
            "15 Sept 2023", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 0, 0, 0)

    def test_date_only_dd_mon_yyyy(self) -> None:
        """Date-only string matching '%d %b %Y'."""
        result = _mod.parse_datetime(
            "15 Sep 2023", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 0, 0, 0)

    def test_no_match_invalid_format(self) -> None:
        """String that doesn't match any format returns None."""
        result = _mod.parse_datetime(
            "Sep 15, 2023", reference_datetime=self.REF
        )
        assert result is None

    def test_no_match_gibberish(self) -> None:
        """Completely unrelated string returns None."""
        result = _mod.parse_datetime(
            "hello world", reference_datetime=self.REF
        )
        assert result is None

    def test_timezone_inherited(self) -> None:
        """Result should use reference_datetime's timezone."""
        ref = datetime(2023, 9, 15, tzinfo=timezone.utc)
        result = _mod.parse_datetime(
            "15/09/2023 at 11:59:00pm", reference_datetime=ref
        )
        assert result is not None
        assert result.result.tzinfo is timezone.utc

    def test_multiline(self) -> None:
        """Newlines are replaced with spaces."""
        result = _mod.parse_datetime(
            "15/09/2023\nat 11:59:00pm", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 59, 0)

    def test_chinese_am_with_seconds(self) -> None:
        """上午 with seconds — 15/09/2023 at 11:59:00上午 → 11:59am."""
        result = _mod.parse_datetime(
            "15/09/2023 at 11:59:00上午", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 11, 59, 0)

    def test_chinese_pm_strips_suffix_correctly(self) -> None:
        """下午 replacement leaves correct time after am/pm."""
        result = _mod.parse_datetime(
            "15/09/2023 at 11:59:00下午", reference_datetime=self.REF
        )
        assert result is not None
        assert result.result == datetime(2023, 9, 15, 23, 59, 0)


# ---------------------------------------------------------------------------
# parse_title_and_content
# ---------------------------------------------------------------------------


class TestParseTitleAndContent:
    """Tests for the Zinc-specific parse_title_and_content function."""

    def test_submission_with_title_and_content(self) -> None:
        soup = BeautifulSoup(
            "<h1>Lab 1</h1>"
            '<div class="leading-4">Description text</div>',
            "html.parser",
        )
        result = _mod.parse_title_and_content(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is not None
        assert result.title == "Lab 1"
        assert "Description text" in result.content

    def test_submission_no_h1(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        result = _mod.parse_title_and_content(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is None

    def test_submission_no_content_element(self) -> None:
        """h1 exists but no .leading-4 sibling — content is empty."""
        soup = BeautifulSoup("<h1>Title Only</h1>", "html.parser")
        result = _mod.parse_title_and_content(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is not None
        assert result.title == "Title Only"
        assert result.content == ""

    def test_invalid_page_type(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        with pytest.raises(ValueError, match="invalid"):
            _mod.parse_title_and_content(
                soup, page_type=cast(_mod.AssignmentPageType, "invalid")
            )


# ---------------------------------------------------------------------------
# parse_grade
# ---------------------------------------------------------------------------


class TestParseGrade:
    """Tests for the Zinc-specific parse_grade with breakdown field."""

    def test_submission_with_grade(self) -> None:
        soup = BeautifulSoup(
            "<div><div>Total Score</div></div><div>85/100</div>",
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is not None
        assert result.entered_grade == 85
        assert result.possible_grade == 100
        assert result.graded_anonymously is None
        assert result.breakdown == {}

    def test_submission_no_grade(self) -> None:
        """No 'Total Score' element returns None."""
        soup = BeautifulSoup("<div></div>", "html.parser")
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is None

    def test_submission_with_breakdown(self) -> None:
        soup = BeautifulSoup(
            "<div><div>Total Score</div></div><div>85/100</div>"
            "<div>Test Cases</div>"
            "<ul>"
            '<li><span data-icon="check"></span>'
            '<span class="text-sm">Test A</span></li>'
            '<li><span data-icon="xmark"></span>'
            '<span class="text-sm">Test B</span></li>'
            "</ul>",
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is not None
        assert result.breakdown == {"Test A": True, "Test B": False}

    def test_submission_with_partial_breakdown(self) -> None:
        """Test case without .text-sm child gets empty-string key."""
        soup = BeautifulSoup(
            "<div><div>Total Score</div></div><div>90/100</div>"
            "<div>Test Cases</div>"
            "<ul>"
            '<li><span data-icon="check"></span></li>'
            "</ul>",
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is not None
        # Test case with no .text-sm → name = ""
        assert "" in result.breakdown
        assert result.breakdown[""] == 1

    def test_entered_grade_float(self) -> None:
        soup = BeautifulSoup(
            "<div><div>Total Score</div></div><div>88.5/100.0</div>",
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is not None
        assert result.entered_grade == 88.5
        assert result.possible_grade == 100.0

    def test_grade_no_divider(self) -> None:
        """Grade without '/' — possible is empty string."""
        soup = BeautifulSoup(
            "<div><div>Total Score</div></div><div>85</div>",
            "html.parser",
        )
        result = _mod.parse_grade(
            soup, page_type=_mod.AssignmentPageType.SUBMISSION
        )
        assert result is not None
        assert result.entered_grade == 85
        assert result.possible_grade == ""

    def test_invalid_page_type(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        with pytest.raises(ValueError, match="invalid"):
            _mod.parse_grade(
                soup, page_type=cast(_mod.AssignmentPageType, "invalid")
            )


# ---------------------------------------------------------------------------
# parse_properties
# ---------------------------------------------------------------------------


class TestParseProperties:
    """Tests for the Zinc-specific parse_properties function.

    Requires a selected_assignment_ele Tag in addition to the soup.
    """

    REF = datetime(2023, 9, 15, tzinfo=timezone.utc)

    def test_submission_basic(self) -> None:
        """SUBMISSION with minimal elements."""
        soup = BeautifulSoup(
            "<div>Auto Grader graded your submission on"
            "<span>15/09/2023 at 11:59:00pm</span></div>"
            "<div>Submission Report #42</div>",
            "html.parser",
        )
        # Provide a dummy selected_assignment_ele (use the soup root)
        result = _mod.parse_properties(
            soup,
            soup,  # minimal; no type/due/retry fields
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert isinstance(result.submission_datetime, datetime)
        assert result.submission_id == 42

    def test_submission_no_submission_id(self) -> None:
        """No 'Submission Report' text — submission_id is -1."""
        soup = BeautifulSoup(
            "<div>Auto Grader graded your submission on"
            "<span>15/09/2023 at 11:59:00pm</span></div>",
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert result.submission_id == -1

    def test_submission_no_report_match(self) -> None:
        """No 'Submission Report #\\d+' text — submission_id is -1."""
        soup = BeautifulSoup(
            "<div>No submission report here</div>",
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert result.submission_id == -1

    def test_submission_no_datetime_element(self) -> None:
        """No 'Auto Grader graded...' text — submission_datetime is empty."""
        soup = BeautifulSoup(
            "<div>Submission Report #1</div>", "html.parser"
        )
        result = _mod.parse_properties(
            soup,
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert result.submission_datetime == ""

    def test_submission_datetime_unparseable(self) -> None:
        """When datetime text can't be parsed, raw string is returned."""
        soup = BeautifulSoup(
            "<div>Auto Grader graded your submission on"
            "<span>unknown-date</span></div>",
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert result.submission_datetime == "unknown-date"

    def test_retries_remaining(self) -> None:
        soup = BeautifulSoup(
            "<div>Auto Grader graded your submission on"
            "<span>15/09/2023 at 11:59:00pm</span></div>"
            "<div>Remaining Submission Attempts:5</div>",
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert result.properties.get("retries remaining") == 5

    def test_retries_remaining_no_colon(self) -> None:
        """When retries text has no colon, value is -1."""
        soup = BeautifulSoup(
            "<div>Remaining Submission Attempts</div>",
            "html.parser",
        )
        result = _mod.parse_properties(
            soup,
            soup,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert result.properties.get("retries remaining") == -1

    def test_selected_assignment_properties(self) -> None:
        """Properties from selected_assignment_ele are extracted."""
        html = (
            '<a href="https://zinc.cse.ust.hk/assignments/1">'
            '<div class="rounded-md">Lab</div>'
            '<div class="text-gray-600">Released on 1 Sep 2023</div>'
            '<div data-icon="calendar-exclamation"></div>'
            "<div>Due on 15/09/2023 at 11:59:00pm</div>"
            '<div data-icon="rotate-right"></div>'
            "<div>3</div>"
            "</a>"
        )
        soup = BeautifulSoup(html, "html.parser")
        selected = soup.select_one('a[href*="zinc"]')
        assert selected is not None
        result = _mod.parse_properties(
            soup,
            selected,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        props = result.properties
        assert props.get("type") == "Lab"
        # release datetime is "Released on 1 Sep 2023" — not parsed as datetime
        # because Zinc parse_datetime doesn't match that format (no am/pm, no dd/mm).
        # So it stays as a generic string via the fallback path.
        assert "release datetime" in props
        # due — now found via find_next_sibling(), parsed as datetime
        assert isinstance(props.get("due"), datetime)
        # retry limit — "3" has no colon, so index(":") raises ValueError → -1
        assert props.get("retry limit") == -1

    def test_selected_assignment_retry_limit_with_colon(self) -> None:
        """Retry limit text with colon is parsed as int."""
        html = (
            '<a href="https://zinc.cse.ust.hk/assignments/1">'
            '<div data-icon="rotate-right"></div>'
            "<div>Retry Limit: 3</div>"
            "</a>"
        )
        soup = BeautifulSoup(html, "html.parser")
        selected = soup.select_one("a")
        assert selected is not None
        result = _mod.parse_properties(
            soup,
            selected,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        assert result.properties.get("retry limit") == 3

    def test_selected_assignment_due_prefix_stripped(self) -> None:
        """'Due on ' prefix is stripped before datetime parsing."""
        html = (
            '<a href="https://zinc.cse.ust.hk/assignments/1">'
            '<div data-icon="calendar-exclamation"></div>'
            "<div>Due on 15/09/2023 at 11:59:00pm</div>"
            "</a>"
        )
        soup = BeautifulSoup(html, "html.parser")
        selected = soup.select_one("a")
        assert selected is not None
        result = _mod.parse_properties(
            soup,
            selected,
            page_type=_mod.AssignmentPageType.SUBMISSION,
            reference_datetime=self.REF,
        )
        due = result.properties.get("due")
        # Due is now found via find_next_sibling() and parsed as datetime
        assert due == datetime(2023, 9, 15, 23, 59, 0, tzinfo=timezone.utc)

    def test_invalid_page_type(self) -> None:
        soup = BeautifulSoup("<div></div>", "html.parser")
        with pytest.raises(ValueError, match="invalid"):
            _mod.parse_properties(
                soup,
                soup,
                page_type=cast(_mod.AssignmentPageType, "invalid"),
                reference_datetime=self.REF,
            )


# ---------------------------------------------------------------------------
# convert
# ---------------------------------------------------------------------------


class TestConvert:
    """Tests for the async convert function (Zinc-specific URL/date patterns)."""

    MINIMAL_HTML = """\
url: https://zinc.cse.ust.hk/assignments/42
saved date: Thu Sep 14 2023 10:00:00 UTC+0000
<a href="https://zinc.cse.ust.hk/assignments/42">
<span class="font-semibold">COMP 2012</span>
<div data-icon="calendar-exclamation"></div><div>Due on 15/09/2023 at 11:59:00pm</div>
</a>
<h1>Lab 1</h1>
<div>Auto Grader graded your submission on<span>15/09/2023 at 11:59:00pm</span></div>
<div>Submission Report #42</div>
<div>Remaining Submission Attempts:5</div>
<div><div>Total Score</div></div><div>85/100</div>
"""

    @pytest.mark.anyio
    async def test_no_url_match(self) -> None:
        """No URL matching _URL_REGEX returns None."""
        result = await _mod.convert("no url here")
        assert result is None

    @pytest.mark.anyio
    async def test_no_date_match(self) -> None:
        """URL match but no date returns None."""
        html = "url: https://zinc.cse.ust.hk/assignments/1"
        result = await _mod.convert(html)
        assert result is None

    @pytest.mark.anyio
    async def test_invalid_date(self) -> None:
        """URL and date regex match but date can't be parsed returns None."""
        html = (
            "url: https://zinc.cse.ust.hk/assignments/1\n"
            "saved date: not-a-real-date"
        )
        result = await _mod.convert(html)
        assert result is None

    @pytest.mark.anyio
    async def test_no_selected_assignment(self) -> None:
        """No <a> element matching the assignment URL returns None."""
        html = (
            "url: https://zinc.cse.ust.hk/assignments/42\n"
            "saved date: Thu Sep 14 2023 10:00:00 UTC+0000\n"
            # href deliberately wrong
            '<a href="https://zinc.cse.ust.hk/assignments/99">'
            '<span class="font-semibold">Course</span></a>\n'
        )
        result = await _mod.convert(html)
        assert result is None

    @pytest.mark.anyio
    async def test_no_course_name(self) -> None:
        """No .font-semibold inside selected <a> returns None."""
        html = (
            "url: https://zinc.cse.ust.hk/assignments/42\n"
            "saved date: Thu Sep 14 2023 10:00:00 UTC+0000\n"
            '<a href="https://zinc.cse.ust.hk/assignments/42"></a>\n'
        )
        result = await _mod.convert(html)
        assert result is None

    @pytest.mark.anyio
    async def test_no_title(self) -> None:
        """No <h1> element returns None."""
        html = (
            "url: https://zinc.cse.ust.hk/assignments/42\n"
            "saved date: Thu Sep 14 2023 10:00:00 UTC+0000\n"
            '<a href="https://zinc.cse.ust.hk/assignments/42">'
            '<span class="font-semibold">Course</span></a>\n'
        )
        result = await _mod.convert(html)
        assert result is None

    @pytest.mark.anyio
    async def test_no_grade(self) -> None:
        """No 'Total Score' element returns None."""
        html = (
            "url: https://zinc.cse.ust.hk/assignments/42\n"
            "saved date: Thu Sep 14 2023 10:00:00 UTC+0000\n"
            '<a href="https://zinc.cse.ust.hk/assignments/42">'
            '<span class="font-semibold">Course</span></a>\n'
            "<h1>Title</h1>\n"
        )
        result = await _mod.convert(html)
        assert result is None

    @pytest.mark.anyio
    async def test_convert_success(self) -> None:
        """Successful conversion yields YAML with expected structure."""
        result = await _mod.convert(self.MINIMAL_HTML)
        assert result is not None
        assert "type: submission/HKUST Zinc" in result
        assert "course:" in result
        assert "assignment:" in result
        assert "grade:" in result

    @pytest.mark.anyio
    async def test_convert_output_keys(self) -> None:
        result = await _mod.convert(self.MINIMAL_HTML)
        assert result is not None
        assert "COMP 2012" in result
        assert "Lab 1" in result
        assert "breakdown:" in result
        assert "comments: {}" in result

    @pytest.mark.anyio
    async def test_convert_with_breakdown(self) -> None:
        html = self.MINIMAL_HTML + (
            '<div>Test Cases</div><ul>'
            '<li><span data-icon="check"></span>'
            '<span class="text-sm">TC1</span></li>'
            '<li><span data-icon="xmark"></span>'
            '<span class="text-sm">TC2</span></li>'
            "</ul>"
        )
        result = await _mod.convert(html)
        assert result is not None
        assert "TC1" in result
        assert "TC2" in result
        # Breakdown values are int(True)→1 and int(False)→0 from source code
        assert "TC1: 1" in result
        assert "TC2: 0" in result
