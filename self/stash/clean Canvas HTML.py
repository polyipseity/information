"""
---
requirements: pip install anyio>=3.6.0 beautifulsoup4>=4.12.0
timestamp: 2024-08-16T18:05:13+08:00
---

Remove identifiers from Canvas HTML files.
"""

from asyncio import gather, run
from glob import iglob

from anyio import Path
from bs4 import BeautifulSoup


async def _process_HTML(path: Path):
    text = await path.read_text()

    html_tag = BeautifulSoup(text, "html.parser")

    for head_tag in (head_tags := html_tag.find_all("head")):
        for title_tag in head_tag.find_all("title"):
            title_tag.extract()
        for meta_tag in head_tag.find_all("meta"):
            meta_tag.extract()

    content_wrapper_tag = html_tag.find("div", {"id": "content-wrapper"})

    text = f"""<html>
{"\n".join(map(str, head_tags))}
<body>
{content_wrapper_tag}
</body>
</html>"""

    await path.write_text(text)


async def main():
    await gather(
        *(
            _process_HTML(Path(path_str))
            for path_str in iglob("**/*.html", recursive=True)
        )
    )


if __name__ == "__main__":
    run(main())
