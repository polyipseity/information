#!/usr/bin/env python
# /// script
# dependencies = [
#   "anyio>=3.6.0",
#   "asyncer>=0.0.17",
#   "beautifulsoup4>=4.12.0",
#   "uvloop>=0.22.0; platform_system != 'Windows'",
#   "winloop>=0.5.0; platform_system == 'Windows'",
# ]
# timestamp = "2025-06-08T22:09:21.532+08:00"
# ///

"""Convert multiple choice questions on D2L Brightspace to markdown."""

from anyio import Path
from asyncer import SoonValue, create_task_group, runnify
from bs4 import BeautifulSoup
from bs4.element import Tag


def process_html(question: str) -> str:
    """Parse a D2L Brightspace MCQ HTML fragment and return markdown.

    This function is "fail-fast": it raises ValueError when required
    elements/attributes are missing or malformed.
    """
    soup = BeautifulSoup(question, "html.parser")

    # extract iframe.srcdoc (fail-fast)
    iframe: Tag | None = soup.select_one("iframe")
    if iframe is None:
        raise ValueError("input HTML does not contain an <iframe> element")
    srcdoc = iframe.get("srcdoc")
    if not isinstance(srcdoc, str) or not srcdoc:
        raise ValueError("iframe element missing 'srcdoc' attribute or it is empty")
    soup = BeautifulSoup(srcdoc, "html.parser")

    # extract nested FRM_page.srcdoc (fail-fast)
    frm: Tag | None = soup.select_one("#FRM_page")
    if frm is None:
        raise ValueError("FRM_page element not found in iframe srcdoc")
    frm_srcdoc = frm.get("srcdoc")
    if not isinstance(frm_srcdoc, str) or not frm_srcdoc:
        raise ValueError("#FRM_page missing 'srcdoc' attribute or it is empty")
    html = BeautifulSoup(frm_srcdoc, "html.parser")

    # header (optional)
    header_tag: Tag | None = html.select_one("h2 strong")
    question_header = header_tag.get_text(strip=True).lower() if header_tag else ""

    # question body (required)
    q_tag: Tag | None = html.select_one(
        ".d2l-quiz-question-autosave-container d2l-html-block"
    )
    if q_tag is None:
        raise ValueError("question HTML block not found")
    q_html = q_tag.get("html")
    if not isinstance(q_html, str):
        raise ValueError("question HTML block missing 'html' attribute")
    q_text = q_html.removeprefix("<p>").removesuffix("</p>").strip()

    # options (required)
    options = html.select(".d2l-quiz-answer-container d2l-html-block")
    if not options:
        raise ValueError("no answer option blocks found")
    options_texts: list[str] = []
    for opt in options:
        raw = opt.get("html")
        if not isinstance(raw, str):
            raise ValueError("answer option missing 'html' attribute")
        options_texts.append(raw.removeprefix("<p>").removesuffix("</p>").strip())

    # selected input (fail-fast if none)
    inputs = html.select(".d2l-qc-controls-container input")
    selected: int | None = None
    for idx, inp in enumerate(inputs, start=1):
        if inp.get("checked") is not None:
            selected = idx
            break
    if selected is None:
        raise ValueError("no checked input found for this question")

    options_md = "\n> ".join(f"{i}. {t}" for i, t in enumerate(options_texts, start=1))

    return (
        f"> __{question_header}__ (2 points)\n"
        f">\n"
        f"> {q_text}\n\n"
        f"> ---\n\n"
        f"> {options_md}\n\n"
        f"> ---\n\n"
        f"> - solution: {{@{{{selected}}}@}}"
    )


async def _process_file(path: Path) -> str:
    text = await path.read_text(encoding="utf-8")
    return process_html(text)


async def main():
    root = Path(".")

    # We'll collect SoonValue objects from the task group.  Each
    # call to ``tg.soonify(_process_file)(entry)`` immediately returns a
    # ``SoonValue[str]`` instance whose ``.value`` attribute will be
    # populated once the task completes.  After the ``async with`` block
    # the task group has implicitly awaited all pending work, so we can
    # safely access the return values without raising PendingValueException.
    soon_values: list[SoonValue[str]] = []

    async with create_task_group() as tg:
        async for entry in root.iterdir():
            if entry.name.endswith(".html") and not await entry.is_dir():
                # schedule the task; value will be available after the block
                soon_values.append(tg.soonify(_process_file)(entry))

    # all tasks have finished here
    results = [sv.value for sv in soon_values]
    print("\n\n---\n\n".join(results))


def __main__() -> None:
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
