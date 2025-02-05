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

_MONTH_NAMES = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)


@final
class AssignmentPageType(StrEnum):
    ASSIGNMENT = "assignment"
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
    __TIME_REGEX: Pattern[str] = re_compile(r"\d+([ap]m)"),
    __FORMATS: Sequence[tuple[Callable[[str, datetime], str], str]] = (
        (lambda s, dt: s, "%b %d, %Y at %H:%M:%S%p"),
        (lambda s, dt: s, "%b %d, %Y by %H:%M:%S%p"),
        (lambda s, dt: s, "%b %d, %Y at %H:%M%p"),
        (lambda s, dt: s, "%b %d, %Y by %H:%M%p"),
        (lambda s, dt: s, "%b %d, %Y at %H%p"),
        (lambda s, dt: s, "%b %d, %Y by %H%p"),
        (lambda s, dt: f"{dt.year} {s}", "%Y  %b %d at %H:%M:%S%p"),
        (lambda s, dt: f"{dt.year} {s}", "%Y  %b %d by %H:%M:%S%p"),
        (lambda s, dt: f"{dt.year} {s}", "%Y  %b %d at %H:%M%p"),
        (lambda s, dt: f"{dt.year} {s}", "%Y  %b %d by %H:%M%p"),
        (lambda s, dt: f"{dt.year} {s}", "%Y  %b %d at %H%p"),
        (lambda s, dt: f"{dt.year} {s}", "%Y  %b %d by %H%p"),
    ),
) -> ParseDatetimeResult | None:
    start_index = -1
    for month_name in _MONTH_NAMES:
        with suppress(ValueError):
            start_index = string.index(month_name)
    if (
        start_index == -1
        or (time_match := __TIME_REGEX.search(string, pos=start_index)) is None
    ):
        return None
    end_index = time_match.end()

    string = string[start_index:end_index].replace("\n", " ")
    delta = timedelta(hours=12) if time_match[1] == "pm" else timedelta()
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
        case AssignmentPageType.ASSIGNMENT:
            if (
                title_ele := soup.select_one(".assignment-title .title-content")
            ) is None:
                return None
            title = title_ele.text.strip()

            content_ele = soup.select_one('*[data-resource-type="assignment.body"]')
            content = "" if content_ele is None else html_to_text(content_ele)

        case AssignmentPageType.SUBMISSION:
            if (
                title_ele := soup.select_one(
                    ".submission-details-header__heading:not(.submission_header)"
                )
            ) is None:
                return None
            title = title_ele.text.strip()

            content = ""

        case _:
            raise ValueError(page_type)

    return ParseTitleAndContentResult(title=title, content=content)


@final
class ParseGradeResult(NamedTuple):
    possible_grade: int | float | str
    entered_grade: int | float | str
    graded_anonymously: bool | None


def parse_grade(
    soup: BeautifulSoup, *, page_type: AssignmentPageType
) -> ParseGradeResult | None:
    match page_type:
        case AssignmentPageType.ASSIGNMENT:
            module_eles = soup.select(".details .content .module")
            try:
                module_ele = next(
                    div
                    for div in module_eles
                    if any("Grade: " in string for string in div.strings)
                )
            except StopIteration:
                return None

            if (possible_grade_ele := module_ele.select_one("span")) is None:
                return None
            possible_grade = possible_grade_ele.text.strip().split(maxsplit=1)[0][1:]

            if (entered_grade_ele := possible_grade_ele.parent) is None:
                return None
            try:
                entered_grade = next(
                    string[len("Grade: ") :]
                    for string in (
                        child.text.strip() for child in entered_grade_ele.children
                    )
                    if string.startswith("Grade: ")
                )
            except StopIteration:
                return None

            try:
                graded_anonymously = (
                    next(
                        string[len("Graded Anonymously: ") :]
                        for string in (
                            child.text.strip() for child in module_ele.children
                        )
                        if string.startswith("Graded Anonymously: ")
                    ).casefold()
                    == "yes"
                )
            except StopIteration:
                graded_anonymously = None
        case AssignmentPageType.SUBMISSION:
            if (entered_grade_ele := soup.select_one(".entered_grade")) is None:
                return None
            entered_grade = entered_grade_ele.text.strip()
            possible_grade = (
                ""
                if (possible_grade_ele := entered_grade_ele.next_sibling) is None
                or not (possible_grade_text := possible_grade_ele.text.strip())
                else possible_grade_text.split(maxsplit=1)[-1]
            )
            graded_anonymously = None

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

    return ParseGradeResult(
        possible_grade=possible_grade,
        entered_grade=entered_grade,
        graded_anonymously=graded_anonymously,
    )


@final
class ParsePropertiesResult(NamedTuple):
    properties: Mapping[str, object]
    submission_datetime: datetime | str


def parse_properties(
    soup: BeautifulSoup,
    *,
    page_type: AssignmentPageType,
    reference_datetime: datetime,
) -> ParsePropertiesResult:
    properties_raw = dict[str, str]()
    match page_type:
        case AssignmentPageType.ASSIGNMENT:
            submission_datetime_ele = soup.select_one(
                ".details .content > :first-child"
            )

            if (
                property_parent := soup.select_one(".student-assignment-overview")
            ) is not None:
                for property_ele in property_parent.children:
                    if not isinstance(property_ele, Tag) or property_ele.name != "li":
                        continue
                    if (key_ele := property_ele.select_one(".title")) is None:
                        continue
                    if (val_ele := property_ele.select_one(".value")) is None:
                        continue
                    properties_raw[key_ele.text.strip().casefold()] = (
                        val_ele.text.strip()
                    )

        case AssignmentPageType.SUBMISSION:
            submission_datetime_ele = soup.select_one(
                ".submission-details-header__time:not(.hidden)"
            )

            property_eles = soup.select(".submission-details-header__attempts_info")
            for property_ele in property_eles:
                if (key_ele := property_ele.select_one(".bold")) is None:
                    continue
                if (val_ele := property_ele.select_one(":not(.bold)")) is None:
                    continue
                properties_raw[key_ele.text.strip().casefold()] = val_ele.text.strip()

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

    for key, val in properties_raw.items():
        generic = True
        match key:
            case "available":
                if (
                    dt1 := parse_datetime(val, reference_datetime=reference_datetime)
                ) is not None:
                    if (
                        dt2 := parse_datetime(
                            val[dt1.end_index :], reference_datetime=reference_datetime
                        )
                    ) is not None:
                        properties[key] = {"start": dt1.result, "end": dt2.result}
                    else:
                        # after, until
                        if "after" in val:
                            properties[key] = {"start": dt1.result, "end": None}
                        else:
                            properties[key] = {"start": None, "end": dt1.result}
                    generic = False
            case "due":
                if (
                    dt := parse_datetime(val, reference_datetime=reference_datetime)
                ) is not None:
                    properties[key] = dt.result
                    generic = False
            case "file types":
                properties[key] = (
                    tuple(
                        val2.lstrip().removeprefix("and ").strip()
                        for val2 in val.split(",")
                    )
                    if val
                    else ()
                )
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
        properties=properties, submission_datetime=submission_datetime
    )


@final
class ParseCommentResult(NamedTuple):
    id: int | str
    content: str
    author: str
    datetime: datetime | str
    attachments: Sequence[str]


def parse_comments(
    soup: BeautifulSoup,
    *,
    page_type: AssignmentPageType,
    reference_datetime: datetime,
) -> Sequence[ParseCommentResult]:
    ret = list[ParseCommentResult]()

    match page_type:
        case AssignmentPageType.ASSIGNMENT:
            if (comments_ele := soup.select_one(".comments")) is not None:
                for comment_ele in comments_ele.children:
                    if not isinstance(
                        comment_ele, Tag
                    ) or "comment" not in comment_ele.get_attribute_list("class"):
                        continue

                    id = " ".join(comment_ele.get_attribute_list("id", ["comment--1"]))[
                        len("comment-") :
                    ]
                    with suppress(ValueError):
                        id = int(id)

                    content_ele = comment_ele.select_one(".comment_content")
                    content = "" if content_ele is None else html_to_text(content_ele)

                    if (
                        signature_ele := comment_ele.select_one(".signature")
                    ) is not None:
                        signature_text = signature_ele.text.strip()
                        dt = parse_datetime(
                            signature_text, reference_datetime=reference_datetime
                        )
                        if dt is None:
                            author, dt = signature_text, ""
                        else:
                            author, dt = (
                                signature_text[: dt.start_index]
                                .rstrip()
                                .removesuffix(",")
                                .rstrip(),
                                dt.result,
                            )
                    else:
                        author, dt = "", ""

                    attachments_ele = comment_ele.select(".comment_attachment")
                    attachments = tuple(ele.text.strip() for ele in attachments_ele)

                    ret.append(
                        ParseCommentResult(
                            id=id,
                            content=content,
                            author=author,
                            datetime=dt,
                            attachments=attachments,
                        )
                    )

        case AssignmentPageType.SUBMISSION:
            if (comments_ele := soup.select_one(".comment_list")) is not None:
                for comment_ele in comments_ele.children:
                    if not isinstance(
                        comment_ele, Tag
                    ) or "comment" not in comment_ele.get_attribute_list("class"):
                        continue

                    id = " ".join(
                        comment_ele.get_attribute_list("id", ["submission_comment_-1"])
                    )[len("submission_comment_") :]
                    with suppress(ValueError):
                        id = int(id)

                    content_ele = comment_ele.select_one(".comment")
                    content = "" if content_ele is None else html_to_text(content_ele)

                    author_ele = comment_ele.select_one(".author_name")
                    author = "" if author_ele is None else author_ele.text.strip()

                    if (
                        datetime_ele := comment_ele.select_one(".posted_at")
                    ) is not None:
                        dt = parse_datetime(
                            datetime_ele.text, reference_datetime=reference_datetime
                        )
                        dt = datetime_ele.text.strip() if dt is None else dt.result
                    else:
                        dt = ""

                    attachments_ele = comment_ele.select(".comment_attachment")
                    attachments = tuple(ele.text.strip() for ele in attachments_ele)

                    ret.append(
                        ParseCommentResult(
                            id=id,
                            content=content,
                            author=author,
                            datetime=dt,
                            attachments=attachments,
                        )
                    )

        case _:
            raise ValueError(page_type)

    return ret


def convert(
    html_text: str,
    *,
    __URL_REGEX: Pattern[str] = re_compile(
        r"url: https://canvas.ust.hk/courses/(\d+)/assignments/(\d+)(?:/submissions/(\d+))?"
    ),
    __DATE_REGEX: Pattern[str] = re_compile(r"saved date: ([^(\n]*)"),
) -> str | None:
    if not (url_match := __URL_REGEX.search(html_text)) or not (
        date_match := __DATE_REGEX.search(html_text)
    ):
        return None
    course_id, assign_id, stu_id = (
        int(url_match[1]),
        int(url_match[2]),
        int(url_match[3]) if url_match[3] else -1,
    )
    try:
        saved_datetime = datetime.strptime(
            date_match[1].strip(), "%a %b %d %Y %H:%M:%S %Z%z"
        )
    except ValueError:
        return None

    page_type = (
        AssignmentPageType.ASSIGNMENT if stu_id == -1 else AssignmentPageType.SUBMISSION
    )
    soup = BeautifulSoup(html_text, "html.parser")

    if (
        course_name_ele := soup.select_one(
            f'*[href="https://canvas.ust.hk/courses/{course_id}"]'
        )
    ) is None or (
        title_content := parse_title_and_content(soup, page_type=page_type)
    ) is None:
        return None
    if (grade := parse_grade(soup, page_type=page_type)) is None:
        grade = ParseGradeResult("", "", None)

    course_name = course_name_ele.text.strip()
    title, content = title_content
    possible_grade, entered_grade, graded_anonymously = grade
    properties, submission_datetime = parse_properties(
        soup, page_type=page_type, reference_datetime=saved_datetime
    )
    comments = parse_comments(
        soup, page_type=page_type, reference_datetime=saved_datetime
    )

    data: Mapping[str, object] = {  # type: ignore
        "type": "submission/HKUST Canvas",
        "course": {
            "id": course_id,
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
                    "id": -1,
                },
            ),
            "grade": {
                "possible": possible_grade,
                "entered": entered_grade,
                "graded anonymously": graded_anonymously,
            },
            "comments": {
                comment.id: {
                    "id": comment.id,
                    "content": comment.content,
                    "author": comment.author,
                    "datetime": comment.datetime,
                    "attachments": comment.attachments,
                }
                for comment in comments
            },
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
