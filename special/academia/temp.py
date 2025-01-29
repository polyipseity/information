from glob import iglob
from pathlib import Path


def process_markdown_file(path: Path):
    content = path.read_text()
    if "- name: " not in content:
        return
    lines = content.splitlines()
    name = next(line for line in lines if line.startswith("- name: "))[
        len("- name: ") :
    ].strip()

    for idx, line in enumerate(lines[2:], 2):
        if line[4:] > name or line.startswith("tags:"):
            lines.insert(idx, f"  - {name}\n  - {name} index")
            break

    path.write_text("\n".join(lines) + "\n")


def main():
    for file in iglob("**/index.md", recursive=True):
        process_markdown_file(Path(file))


if __name__ == "__main__":
    main()
