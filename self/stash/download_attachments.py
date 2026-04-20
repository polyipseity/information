#!/usr/bin/env python
# /// script
# dependencies = [
#   "anyio>=3.6.0",
#   "asyncer>=0.0.17",
#   "beautifulsoup4>=4.12.0",
#   "requests>=2.32.0",
#   "uvloop>=0.22.0; platform_system != 'Windows'",
#   "winloop>=0.5.0; platform_system == 'Windows'",
# ]
# requires-python = ">=3.13.0"
# timestamp = "2025-06-11T19:12:43.410+08:00"
# ///

"""Download linked attachments."""

from anyio import Path, sleep
from asyncer import asyncify, create_task_group, runnify
from bs4 import BeautifulSoup
from requests import get

AUTHORIZATION = "Basic <token>"
ATTACHMENT_URL_PREFIX = "https://example.com/"


def _perform_download(href: str, attachment_path: Path) -> None:
    """Blocking helper to fetch a href and write to attachment_path."""
    with get(href, stream=True, headers={"Authorization": AUTHORIZATION}) as req:
        if req.status_code == 404:
            print(f"Not found: {href}")
            return
        req.raise_for_status()

        with open(attachment_path, "wb", buffering=0) as attachment:
            for chunk in req.iter_content(chunk_size=8192):
                attachment.write(chunk)


async def handle_single_attachment(href: str, subdir: Path) -> None:
    """Download one attachment if missing, respecting prefix and sleep delay."""
    if not href.startswith(ATTACHMENT_URL_PREFIX):
        return
    attachment_filename = href[href.rindex("/") + len("/") :]
    attachment_path = subdir / attachment_filename
    if await attachment_path.exists():
        print(f"Already exists: {attachment_path}")
        return

    print(f"Downloading: {attachment_path}")
    await asyncify(_perform_download)(href, attachment_path)
    await sleep(1)


async def download_html_attachments(html_path: Path, subdir: Path) -> None:
    """Extract links from an HTML file and download each matching attachment."""
    html_text = await html_path.read_text()
    # keep the original url line for debugging if needed
    _url = html_text.splitlines()[2].removeprefix(" url: ").strip()
    html = BeautifulSoup(html_text, "html.parser")

    for a_tag in html.select("a"):
        href = str(a_tag.get("href", ""))
        await handle_single_attachment(href, subdir)


async def main() -> None:
    root = Path(".")
    async with create_task_group() as tg:
        async for subdir in root.iterdir():
            if not await subdir.is_dir():
                continue
            async for html_path in subdir.iterdir():
                if html_path.name.endswith(".html"):
                    tg.start_soon(download_html_attachments, html_path, subdir)


def __main__() -> None:
    """Synchronous command-line entrypoint exposed by the package."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
