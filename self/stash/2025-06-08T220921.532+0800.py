import bs4
import os
from pathlib import Path

# convert multiple choice questions from D2L Brightspace


def process_html(question: str) -> str:
    bs = bs4.BeautifulSoup(question, "html.parser")
    bs = bs4.BeautifulSoup(bs.select_one("iframe").get("srcdoc"), "html.parser")
    bs = bs4.BeautifulSoup(bs.select_one("#FRM_page").get("srcdoc"), "html.parser")

    question_header = bs.select_one("h2 strong").text.strip().lower()
    question = (
        bs.select_one(".d2l-quiz-question-autosave-container d2l-html-block")
        .get("html")
        .removeprefix("<p>")
        .removesuffix("</p>")
        .strip()
    )
    options = bs.select(".d2l-quiz-answer-container d2l-html-block")
    option_texts = tuple(
        opt.get("html").removeprefix("<p>").removesuffix("</p>").strip()
        for opt in options
    )
    selected = next(
        idx
        for idx, opt in enumerate(
            bs.select(".d2l-qc-controls-container input"), start=1
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
    for filename in os.listdir():
        if not filename.endswith(".html"):
            continue
        ret.append(process_html(Path(filename).read_text()))
    print("\n\n---\n\n".join(ret))
