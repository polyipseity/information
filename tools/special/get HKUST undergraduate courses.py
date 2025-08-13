from aiohttp import ClientSession, TCPConnector
from asyncio import run
from asyncstdlib import chain as a_chain, tuple as a_tuple
from bs4 import BeautifulSoup
from typing import NamedTuple
from yarl import URL

_MAX_CONCURRENT_REQUESTS_PER_HOST = 2
_UNDERGRADUATE_COURSES_URL = URL("https://prog-crs.hkust.edu.hk/ugcourse")


async def main() -> None:
    async with ClientSession(
        connector=TCPConnector(limit_per_host=_MAX_CONCURRENT_REQUESTS_PER_HOST),
        headers={"Accept-Encoding": "gzip"},
    ) as session:
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
        subjects = sorted(subjects.items(), key=lambda item: item[0])

        class Subject(NamedTuple):
            code: str
            name: str
            credit: str

        async def fetch_subject_courses(href: URL):
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

                yield Subject(code, title, unit[: unit.index(" ")])

        courses = await a_tuple(
            a_chain[Subject].from_iterable(
                fetch_subject_courses(href) for _, href in subjects
            )
        )

        for course in courses:
            print(f"{course.code},{course.name},{course.credit}")


if __name__ == "__main__":
    run(main())
