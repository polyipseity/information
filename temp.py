import glob
import anyio
import asyncio
import re

a = tuple(glob.glob("**/*.md", recursive=True, include_hidden=True))
print(a)


async def read(path: str):
    async with await anyio.open_file(path, "r+t") as ff:
        all = await ff.read()
        matches = re.compile(r"> \$\$(.*?)\$\$", re.DOTALL).finditer(all)
        for match in matches:
            cnt: str = match[1]
            if "*" in cnt:
                print(f"{path}")
            lines = cnt.split("\n")
            lines = (
                lines[0],
                *(line if line.startswith(">") else f"> {line}" for line in lines[1:]),
            )
            all = all.replace(match[0], f"> $${'\n'.join(lines)}$$")
        await ff.seek(0)
        await ff.write(all)


async def main():
    await asyncio.gather(*map(read, a))


asyncio.run(main())
