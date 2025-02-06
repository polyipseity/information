from anyio import Path
from asyncio import run
from bs4 import BeautifulSoup, Tag
from contextlib import suppress
from copy import copy
from datetime import datetime, timedelta
from enum import StrEnum
from io import StringIO
from re import Pattern, compile as re_compile
from sys import stderr
from typing import Callable, Collection, Mapping, NamedTuple, Sequence, final
from yaml import safe_dump


@final
class AssignmentPageType(StrEnum):
    SUBMISSION = "submission"


@final
class ParseDatetimeResult(NamedTuple):
    result: datetime
    start_index: int
    end_index: int


def html_to_text(
    tag: Tag,
    *,
    __NON_BREAKING_ELEMENTS: Collection[str] = (
        "a",
        "abbr",
        "acronym",
        "audio",
        "b",
        "bdi",
        "bdo",
        "big",
        "button",
        "canvas",
        "cite",
        "code",
        "data",
        "datalist",
        "del",
        "dfn",
        "em",
        "embed",
        "i",
        "iframe",
        "img",
        "input",
        "ins",
        "kbd",
        "label",
        "map",
        "mark",
        "meter",
        "noscript",
        "object",
        "output",
        "picture",
        "progress",
        "q",
        "ruby",
        "s",
        "samp",
        "script",
        "select",
        "slot",
        "small",
        "span",
        "strong",
        "sub",
        "sup",
        "svg",
        "template",
        "textarea",
        "time",
        "u",
        "tt",
        "var",
        "video",
        "wbr",
    ),
) -> str:
    tag = copy(tag)
    for element in tag.find_all():
        if element.name not in __NON_BREAKING_ELEMENTS:
            match element.name:
                case "br":
                    element.append("\n")
                case "p":
                    pass
                case _:
                    element.append("\n\n")
    return tag.text.strip()


def parse_datetime(
    string: str,
    *,
    reference_datetime: datetime,
    __FORMATS: Sequence[tuple[Callable[[str, datetime], str], str]] = (
        (lambda s, dt: s, "%d/%m/%Y at %H:%M:%S%p"),
        (lambda s, dt: f"{dt.year} {s}", "%d %b %Y at %H:%M:%S"),
        (lambda s, dt: f"{dt.year} {s}", "%Y  %d %b at %H:%M:%S"),
        (lambda s, dt: s, "%d %b %Y"),
    ),
) -> ParseDatetimeResult | None:
    string = string.replace(" Sept ", " Sep ")
    if "上午" in string:
        string = f"{string[:string.index('上午')]}{string[string.index('上午')+len('上午'):]}am"
    if "下午" in string:
        string = f"{string[:string.index('下午')]}{string[string.index('下午')+len('下午'):]}pm"

    start_index = 0
    end_index = len(string)

    string = string[start_index:end_index].replace("\n", " ")
    delta = timedelta(hours=12) if string.endswith("pm") else timedelta()
    if string.endswith("12am") or string.endswith("12pm"):
        delta -= timedelta(hours=12)

    for transformer, format in __FORMATS:
        string2 = transformer(string, reference_datetime)
        try:
            ret = datetime.strptime(string2, format)
        except ValueError:
            continue
        ret += delta
        ret = ret.replace(tzinfo=reference_datetime.tzinfo)
        return ParseDatetimeResult(
            result=ret, start_index=start_index, end_index=end_index
        )

    return None


@final
class ParseTitleAndContentResult(NamedTuple):
    title: str
    content: str


def parse_title_and_content(
    soup: BeautifulSoup, *, page_type: AssignmentPageType
) -> ParseTitleAndContentResult | None:
    match page_type:
        case AssignmentPageType.SUBMISSION:
            if (title_ele := soup.select_one("h1")) is None:
                return None
            title = title_ele.text.strip()

            content_ele = title_ele.find_next(attrs={"class": "leading-4"})
            content = html_to_text(content_ele) if isinstance(content_ele, Tag) else ""

        case _:
            raise ValueError(page_type)

    return ParseTitleAndContentResult(title=title, content=content)


@final
class ParseGradeResult(NamedTuple):
    possible_grade: int | float | str
    entered_grade: int | float | str
    graded_anonymously: bool | None
    breakdown: Mapping[str, int | float | str]


def parse_grade(
    soup: BeautifulSoup, *, page_type: AssignmentPageType
) -> ParseGradeResult | None:
    match page_type:
        case AssignmentPageType.SUBMISSION:
            if (
                (grade_ele := soup.find(string="Total Score")) is None
                or (grade_ele := grade_ele.parent) is None
                or (grade_ele := grade_ele.parent) is None
                or (grade_ele := grade_ele.next_sibling) is None
            ):
                return None
            grade_comps = grade_ele.text.strip().split("/", maxsplit=1)
            while len(grade_comps) < 2:
                grade_comps.append("")
            entered_grade, possible_grade, *_ = grade_comps
            graded_anonymously = None

            breakdown = dict[str, float | int | str]()
            if (
                test_cases_ele := soup.find(string="Test Cases")
            ) is not None and isinstance(
                test_cases_ele := test_cases_ele.find_next("ul"), Tag
            ):
                for test_case_ele in test_cases_ele.select("li"):
                    correct = (
                        test_case_ele.find(attrs={"data-icon": "check"}) is not None
                    )
                    name = test_case_ele.select_one(".text-sm")
                    name = "" if name is None else name.text.strip()
                    breakdown[name] = correct

        case _:
            raise ValueError(page_type)

    try:
        possible_grade = int(possible_grade)
    except ValueError:
        with suppress(ValueError):
            possible_grade = float(possible_grade)
    try:
        entered_grade = int(entered_grade)
    except ValueError:
        with suppress(ValueError):
            entered_grade = float(entered_grade)
    for breakdown_key in breakdown:
        breakdown_val = breakdown[breakdown_key]
        try:
            breakdown[breakdown_key] = int(breakdown_val)
        except ValueError:
            with suppress(ValueError):
                breakdown[breakdown_key] = float(breakdown_val)

    return ParseGradeResult(
        possible_grade=possible_grade,
        entered_grade=entered_grade,
        graded_anonymously=graded_anonymously,
        breakdown=breakdown,
    )


@final
class ParsePropertiesResult(NamedTuple):
    properties: Mapping[str, object]
    submission_datetime: datetime | str
    submission_id: int | str


def parse_properties(
    soup: BeautifulSoup,
    selected_assignment_ele: Tag,
    *,
    page_type: AssignmentPageType,
    reference_datetime: datetime,
) -> ParsePropertiesResult:
    properties_raw = dict[str, str]()
    match page_type:
        case AssignmentPageType.SUBMISSION:
            submission_datetime_ele = soup.find(
                string="Auto Grader graded your submission on"
            )
            submission_datetime_ele = (
                None
                if submission_datetime_ele is None
                else submission_datetime_ele.next_sibling
            )
            submission_id_ele = soup.find(
                string=re_compile(r"^Submission Report #\d+$")
            )

            retries_remaining_ele = soup.find(
                string=re_compile(r"^Remaining Submission Attempts:\d+$")
            )
            properties_raw["retries remaining"] = (
                ""
                if retries_remaining_ele is None
                else retries_remaining_ele.text.strip()
            )

            type_ele = selected_assignment_ele.select_one(".rounded-md")
            properties_raw["type"] = "" if type_ele is None else type_ele.text.strip()

            release_datetime_ele = selected_assignment_ele.select_one(".text-gray-600")
            properties_raw["release datetime"] = (
                ""
                if release_datetime_ele is None
                else release_datetime_ele.text.strip()
            )

            due_ele = selected_assignment_ele.find(
                attrs={"data-icon": "calendar-exclamation"}
            )
            due_ele = None if due_ele is None else due_ele.parent
            due_ele = None if due_ele is None else due_ele.next_sibling
            properties_raw["due"] = (
                ""
                if due_ele is None
                else due_ele.text.strip()[len("Due on ") :].lstrip()
            )

            retry_limit_ele = selected_assignment_ele.find(
                attrs={"data-icon": "rotate-right"}
            )
            retry_limit_ele = (
                None if retry_limit_ele is None else retry_limit_ele.parent
            )
            retry_limit_ele = (
                None if retry_limit_ele is None else retry_limit_ele.next_sibling
            )
            properties_raw["retry limit"] = (
                "" if retry_limit_ele is None else retry_limit_ele.text.strip()
            )
        case _:
            raise ValueError(page_type)

    properties = dict[str, object]()

    submission_datetime = ""
    if submission_datetime_ele is not None:
        if (
            submission_datetime := parse_datetime(
                submission_datetime_ele.text, reference_datetime=reference_datetime
            )
        ) is not None:
            submission_datetime = submission_datetime.result
        else:
            submission_datetime = submission_datetime_ele.text.strip()

    submission_id = -1
    if submission_id_ele is not None:
        submission_id = submission_id_ele.text[
            submission_id_ele.text.index("#") + len("#") :
        ].rstrip()
        with suppress(ValueError):
            submission_id = int(submission_id)

    for key, val in properties_raw.items():
        generic = True
        match key:
            case "due" | "release datetime":
                reference_datetime2 = reference_datetime
                if key == "release datetime":
                    reference_datetime2 = reference_datetime2.replace(
                        hour=0, minute=0, second=0
                    )
                if (
                    dt := parse_datetime(val, reference_datetime=reference_datetime2)
                ) is not None:
                    properties[key] = dt.result
                    generic = False
            case "retries remaining" | "retry limit":
                try:
                    val2 = int(
                        (val[val.index(":") + len(":") :].split(maxsplit=1) or ("",))[0]
                    )
                except ValueError:
                    properties[key] = -1
                else:
                    properties[key] = val2
                generic = False
            case _:
                pass

        if generic:

            def parse_datetime0(val: str):
                if (
                    ret := parse_datetime(val, reference_datetime=reference_datetime)
                ) is None:
                    return None
                return ret.result

            for parse, bad_vals, bad_excs in (
                (int, (), (ValueError,)),
                (float, (), (ValueError,)),
                (parse_datetime0, (None,), ()),
                (str, (), ()),
            ):
                try:
                    parsed_val = parse(val)
                except bad_excs:
                    continue
                if parsed_val in bad_vals:
                    continue
                properties[key] = parsed_val
                break

    return ParsePropertiesResult(
        properties=properties,
        submission_datetime=submission_datetime,
        submission_id=submission_id,
    )


def convert(
    html_text: str,
    *,
    __URL_REGEX: Pattern[str] = re_compile(
        r"url: https://zinc.cse.ust.hk/assignments/(\d+)"
    ),
    __DATE_REGEX: Pattern[str] = re_compile(r"saved date: ([^(\n]*)"),
) -> str | None:
    if not (url_match := __URL_REGEX.search(html_text)) or not (
        date_match := __DATE_REGEX.search(html_text)
    ):
        return None
    assign_id = int(url_match[1])
    try:
        saved_datetime = datetime.strptime(
            date_match[1].strip(), "%a %b %d %Y %H:%M:%S %Z%z"
        )
    except ValueError:
        return None

    page_type = AssignmentPageType.SUBMISSION
    soup = BeautifulSoup(html_text, "html.parser")

    if (
        (
            selected_assign_ele := soup.select_one(
                f'a[href="https://zinc.cse.ust.hk/assignments/{assign_id}"]'
            )
        )
        is None
        or (course_name_ele := selected_assign_ele.select_one(".font-semibold")) is None
        or (title_content := parse_title_and_content(soup, page_type=page_type)) is None
        or (grade := parse_grade(soup, page_type=page_type)) is None
    ):
        return None

    course_name = course_name_ele.text.strip()
    title, content = title_content
    possible_grade, entered_grade, graded_anonymously, breakdown = grade
    properties, submission_datetime, submission_id = parse_properties(
        soup,
        selected_assign_ele,
        page_type=page_type,
        reference_datetime=saved_datetime,
    )

    data: Mapping[str, object] = {  # type: ignore
        "type": "submission/HKUST Zinc",
        "course": {
            "id": -1,
            "name": course_name,
        },
        "assignment": {
            "id": assign_id,
            "title": title,
            "content": content,
            "properties": properties,
            "submissions": (
                {
                    "datetime": submission_datetime,
                    "id": submission_id,
                },
            ),
            "grade": {
                "possible": possible_grade,
                "entered": entered_grade,
                "graded anonymously": graded_anonymously,
                "breakdown": breakdown,
            },
            "comments": {},
        },
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


async def main() -> int:
    file_path = input("HTML file? ")

    file_text = await Path(file_path).read_text()
    result = convert(file_text)

    if result is None:
        return 1
    print(result, file=stderr, end="")

    return 0


if __name__ == "__main__":
    exit(run(main()))
