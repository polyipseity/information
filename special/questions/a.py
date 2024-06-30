from os import listdir
from pathlib import Path


for a in listdir():
    p = Path(a)
    if p.suffix == ".md":
        txt = p.read_text().splitlines()
        for idx, item in enumerate(txt):
            if "- date/" in item:
                break
        txt.insert(
            idx + 1,
            "  - flashcard/special/questions/"
            + p.stem.replace("+", "_").replace(".", "_"),
        )
        p.write_text("\n".join(txt) + "\n")
