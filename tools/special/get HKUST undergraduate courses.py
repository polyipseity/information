from asyncio import TaskGroup, run
from contextlib import asynccontextmanager
from dataclasses import dataclass
from operator import itemgetter
from sys import stdout
from typing import AsyncIterator, Mapping

from aiohttp import ClientSession, TCPConnector
from anyio import AsyncFile, Path
from asyncstdlib import chain as a_chain
from bs4 import BeautifulSoup
from yarl import URL


_MAX_CONCURRENT_REQUESTS_PER_HOST = 2
_UNDERGRADUATE_COURSES_URL = URL("https://prog-crs.hkust.edu.hk/ugcourse")


@dataclass(frozen=True, kw_only=True, slots=True)
class Subject:
    code: str
    name: str
    credit: str


async def fetch_subjects(
    *,
    session: ClientSession,
) -> Mapping[str, URL]:
    async with session.get(_UNDERGRADUATE_COURSES_URL) as req:
        subjects_text = await req.text()

    subjects_html = BeautifulSoup(subjects_text, "html.parser")
    subjects = dict[str, URL]()
    for subject_el in subjects_html.select(".subject"):
        if (subject_key_el := subject_el.select_one("a")) is None:
            raise ValueError(subject_el)
        if not isinstance(subject_val := subject_key_el.get("href"), str):
            raise ValueError(subject_val)

        if (subject_val_el := subject_el.select_one(".subject-code")) is None:
            raise ValueError(subject_el)
        if not (subject_key := subject_val_el.string):
            raise ValueError(subject_val_el)

        subjects[subject_key] = _UNDERGRADUATE_COURSES_URL.join(URL(subject_val))

    return dict(sorted(subjects.items(), key=itemgetter(0)))


async def fetch_subject_courses(
    href: URL,
    *,
    session: ClientSession,
) -> AsyncIterator[Subject]:
    async with session.get(href) as req:
        text = await req.text()
    html = BeautifulSoup(text, "html.parser")
    for course_el in html.select(".crse-header"):
        if (code_el := course_el.select_one(".crse-code")) is None:
            raise ValueError(course_el)
        if not (code := code_el.string):
            raise ValueError(code_el)

        if (title_el := course_el.select_one(".crse-title")) is None:
            raise ValueError(course_el)
        if not (title := title_el.string):
            raise ValueError(title_el)

        if (unit_el := course_el.select_one(".crse-unit")) is None:
            raise ValueError(course_el)
        if not (unit := unit_el.string):
            raise ValueError(unit_el)

        yield Subject(code=code, name=title, credit=unit[: unit.index(" ")])


@asynccontextmanager
async def open_dest(dest_filepath: Path | str) -> AsyncIterator[AsyncFile[str]]:
    if dest_filepath:
        dest_filepath = Path(dest_filepath)
        if not await dest_filepath.exists():
            await dest_filepath.write_bytes(b"")
        async with await dest_filepath.open("rt+", encoding="UTF-8") as io:
            yield io
    else:
        yield AsyncFile(stdout)


async def main() -> None:
    dest_filepath = input("Destination? ")

    async with TaskGroup() as tg, open_dest(dest_filepath) as dest_file, ClientSession(
        connector=TCPConnector(limit_per_host=_MAX_CONCURRENT_REQUESTS_PER_HOST),
        headers={"Accept-Encoding": "gzip"},
    ) as session:
        dest_readable = dest_file.readable()  # type: ignore

        courses = dict[str, str]()
        seek = None
        if dest_readable:
            async for _ in dest_file:
                break  # Reads 1 line
            async for line in dest_file:
                line = line.rstrip()
                key, val = line.split(",", 1)
                courses[key] = val
            seek = tg.create_task(dest_file.seek(0))

        subjects = await fetch_subjects(session=session)
        async for course in a_chain[Subject].from_iterable(
            fetch_subject_courses(href, session=session) for href in subjects.values()
        ):
            courses[course.code] = f"{course.name},{course.credit}"

        if seek is not None:
            await seek
        await dest_file.write("code,name,credit\n")
        for key, val in courses:
            await dest_file.write(f"{key},{val}\n")
        if dest_readable:
            await dest_file.truncate()


if __name__ == "__main__":
    run(main())
