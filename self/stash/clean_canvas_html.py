#!/usr/bin/env python
# /// script
# dependencies = [
#   "anyio>=3.6.0",
#   "asyncer>=0.0.17",
#   "beautifulsoup4>=4.12.0",
#   "uvloop>=0.22.0; platform_system != 'Windows'",
#   "winloop>=0.5.0; platform_system == 'Windows'",
# ]
# timestamp = "2024-08-16T18:05:13+08:00"
# ///

"""Remove identifiers from Canvas HTML files."""

from glob import iglob

from anyio import Path
from asyncer import create_task_group, runnify
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
    async with create_task_group() as tg:
        for path_str in iglob("**/*.html", recursive=True):
            tg.start_soon(_process_HTML, Path(path_str))


def __main__():
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
