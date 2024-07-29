from itertools import chain
from asyncio import run
from bs4 import BeautifulSoup, NavigableString, PageElement, Tag
from bs4.element import PreformattedString
from jaraco.clipboard import paste_html
from pyperclip import copy


async def main() -> None:
    input("HTML? (will read from clipboard)")
    html_text = paste_html()
    assert isinstance(html_text, str)

    html = BeautifulSoup(html_text, "html.parser")

    def html_to_plaintext(ele: PageElement) -> str:
        if not isinstance(ele, Tag):
            return (
                ele
                if isinstance(ele, NavigableString)
                and not isinstance(ele, PreformattedString)
                else ""
            )

        def tag_affixes(name: str):
            return f"<{name}>", f"</{name}>"

        match ele.name:
            case "b":
                prefix, suffix = "__", "__"
            case "i":
                prefix, suffix = "_", "_"
            case "s" | "sub" | "sup" | "u":
                prefix, suffix = tag_affixes(ele.name)
            case _:
                prefix, suffix = "", ""

        return "".join(
            chain((prefix,), map(html_to_plaintext, ele.children), (suffix,))
        )

    output = html_to_plaintext(html).replace(
        "\xa0", " "
    )  # replace non-breaking spaces with spaces

    print(output)
    copy(output)
    print(":)")


if __name__ == "__main__":
    run(main())
