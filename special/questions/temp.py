import os

for filepath in os.listdir():
    if not filepath.endswith(".md"):
        continue
    with open(filepath, "r+t") as file:
        content = file.read()
        content = content.replace(
            "---\n\n", f"---\n\n# {filepath.removesuffix('.md')}\n\n"
        )
        file.seek(0)
        file.truncate()
        file.write(content)
