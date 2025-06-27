"""
---
requirements: pip install beautifulsoup4>=4.12.0
timestamp: 2025-06-08T22:09:21.532+08:00
---

Convert multiple choice questions on D2L Brightspace to markdown.
"""

from os import listdir
from bs4 import BeautifulSoup
from pathlib import Path


def process_html(question: str) -> str:
    html = BeautifulSoup(question, "html.parser")
    html = BeautifulSoup(
        str((html.select_one("iframe") or {})["srcdoc"]), "html.parser"
    )
    html = BeautifulSoup(
        str((html.select_one("#FRM_page") or {})["srcdoc"]), "html.parser"
    )

    question_header = html.select_one("h2 strong")
    question_header = question_header.text.strip().lower() if question_header else ""
    question = (
        str(
            (
                html.select_one(".d2l-quiz-question-autosave-container d2l-html-block")
                or {}
            )["html"]
        )
        .removeprefix("<p>")
        .removesuffix("</p>")
        .strip()
    )
    options = html.select(".d2l-quiz-answer-container d2l-html-block")
    option_texts = tuple(
        str(opt["html"]).removeprefix("<p>").removesuffix("</p>").strip()
        for opt in options
    )
    selected = next(
        idx
        for idx, opt in enumerate(
            html.select(".d2l-qc-controls-container input"), start=1
        )
        if opt.get("checked") != None
    )

    return fR"""> __{question_header}__ \(2 points\)
>
> {question}
>
> ---
>
> {"\n> ".join(f'{idx}. {opt}' for idx, opt in enumerate(option_texts, start=1))}
>
> ---
>
> - solution: {{@{{{selected}}}@}}"""


if __name__ == "__main__":
    ret = list[str]()
    for filename in listdir():
        if not filename.endswith(".html"):
            continue
        ret.append(process_html(Path(filename).read_text()))
    print("\n\n---\n\n".join(ret))
