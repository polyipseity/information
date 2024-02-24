import os
import re

callout_pattern = re.compile(
    r"> \[![^]]*\][+-]? (.*?)$(.*?)" + "\n" + r"(?!>)", re.DOTALL | re.MULTILINE
)

for filepath in os.listdir():
    if not filepath.endswith(".md"):
        continue
    with open(filepath, "r+t") as file:
        content = file.read()
        for match in callout_pattern.finditer(content):
            content = content.replace(
                match[0],
                f"""## {match[1]}\n{'\n'.join(line.removeprefix('> ').removeprefix('>') for line in match[2].strip().splitlines())}\n""",
            )
        file.seek(0)
        file.truncate()
        file.write(content)
