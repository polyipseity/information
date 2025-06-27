"""
---
requirements: pip install beautifulsoup4>=4.12.0
timestamp: 2025-06-11T19:12:43.410+08:00
---

Download linked attachments.
"""

from bs4 import BeautifulSoup
from os import listdir
from pathlib import Path
from requests import get
from time import sleep


AUTHORIZATION = "Basic <token>"
ATTACHMENT_URL_PREFIX = "https://example.com/"

if __name__ == "__main__":
    for subdir in listdir():
        subdir = Path(subdir)
        if not subdir.is_dir():
            continue

        for html_filename in listdir(subdir):
            if not html_filename.endswith(".html"):
                continue

            html_path = subdir / html_filename

            html_text = html_path.read_text()
            url = html_text.splitlines()[2].removeprefix(" url: ").strip()
            html = BeautifulSoup(html_text, "html.parser")

            for a_tag in html.select("a"):
                href = str(a_tag.get("href", ""))
                if not href.startswith(ATTACHMENT_URL_PREFIX):
                    continue

                attachment_filename = href[href.rindex("/") + len("/") :]
                attachment_path = subdir / attachment_filename
                if attachment_path.exists():
                    print(f"Already exists: {attachment_path}")
                    continue
                """
                idx = 0
                attachment_path_stem = attachment_path.stem
                while attachment_path.exists():
                    print(f"File already exists: {attachment_path}")
                    idx += 1
                    attachment_path = attachment_path.with_stem(f"{attachment_path_stem} ({idx})")
                """

                print(f"Downloading: {attachment_path}")
                with get(
                    href, stream=True, headers={"Authorization": AUTHORIZATION}
                ) as req:
                    if req.status_code == 404:
                        print(f"Not found: {href}")
                        continue
                    req.raise_for_status()

                    with open(attachment_path, "wb", buffering=0) as attachment:
                        for chunk in req.iter_content(chunk_size=8192):
                            attachment.write(chunk)

                sleep(1)
