"""LaTeX conversion for the convert_wiki pipeline.

Converts HTML fragments from Wikipedia texhtml spans (``<math>`` alttext,
``<span class="sfrac">``, radical notations, and nested formatting) into
LaTeX strings.
"""

import re
from collections.abc import Iterable

from bs4 import BeautifulSoup, NavigableString, PageElement, Tag

"""Accent glyphs Wikipedia stacks above a base in its legacy math markup."""
_ACCENT_COMMANDS: dict[str, str] = {
    "\u22c5": "\\dot",  # dot operator
    "\u02d9": "\\dot",  # dot above
    "\u00af": "\\bar",  # macron
    "\u203e": "\\bar",  # overline
    "\u02c6": "\\hat",  # modifier letter circumflex
    "\u02dc": "\\tilde",  # small tilde
    "\u02c7": "\\check",  # caron
    "\u00a8": "\\ddot",  # diaeresis
}
"""LaTeX commands for unicode math letters with no short ASCII spelling."""
_MATH_LETTER_COMMANDS: dict[str, str] = {
    "\u0127": "\\hbar",  # h with stroke
    "\u210f": "\\hbar",  # planck constant
}
"""Regex matching the ``line-height`` of a legacy stacked math block."""
_BLOCK_LINE_HEIGHT_REGEX = re.compile(r"line-height:\s*([0-9.]+)")


class LatexConverter:
    """Handles conversion of HTML math fragments to LaTeX.

    All methods are classmethods or staticmethods — no instance state
    needed.
    """

    @classmethod
    def texhtml_to_latex(cls, ele: PageElement) -> str:
        """Convert a texhtml HTML subtree to a LaTeX string."""
        if isinstance(ele, NavigableString):
            text = str(ele).strip()
            if not text:
                return ""
            return cls._escape_latex_text(text)
        if not isinstance(ele, Tag):
            return ""
        tag = ele.name
        classes = frozenset(ele.get_attribute_list("class"))
        style = str(ele.get("style", ""))
        # sr-only spans are invisible a11y separators.
        if "sr-only" in classes:
            return ""
        # Math fractions.
        if "sfrac" in classes:
            return cls.texhtml_to_latex_sfrac(ele)
        # Subscript/superscript.
        if tag == "sub":
            return f"_{{{cls.texhtml_to_latex_children(ele.children)}}}"
        if tag == "sup":
            return f"^{{{cls.texhtml_to_latex_children(ele.children)}}}"
        # Bold/italic.
        if tag in ("b", "strong"):
            return f"\\mathbf{{{cls.texhtml_to_latex_children(ele.children)}}}"
        if tag in ("i", "em"):
            return cls.texhtml_to_latex_children(ele.children)
        # Radical radicand (border-top span inside a nowrap).
        if "border-top" in style:
            return cls.texhtml_to_latex_children(ele.children)
        # Fallback: recurse into children (nowrap, num, den, tion, etc.).
        return cls.texhtml_to_latex_children(ele.children)

    @classmethod
    def texhtml_to_latex_children(cls, children: Iterable[PageElement]) -> str:
        """Process children in batch, detecting radical patterns across siblings."""
        result_parts: list[str] = []
        child_list = list(children)
        i = 0
        while i < len(child_list):
            child = child_list[i]
            # Skip word joiners (U+2060) and whitespace-only text nodes.
            if isinstance(child, NavigableString) and (
                "\u2060" in str(child) or not str(child).strip()
            ):
                i += 1
                continue
            # Detect radical patterns: [sup?] √ [border-top span]
            if (
                isinstance(child, Tag)
                and child.name == "sup"
                and i + 2 < len(child_list)
            ):
                next1 = child_list[i + 1]
                next2 = child_list[i + 2]
                if (
                    cls._is_sqrt_entity(next1)
                    and isinstance(next2, Tag)
                    and "border-top" in str(next2.get("style", ""))
                ):
                    index = cls.texhtml_to_latex_children(child.children)
                    radicand = cls.texhtml_to_latex(next2)
                    result_parts.append(f"\\sqrt[{index}]{{{radicand}}}")
                    i += 3
                    continue
            if cls._is_sqrt_entity(child) and i + 1 < len(child_list):
                next1 = child_list[i + 1]
                if isinstance(next1, Tag) and "border-top" in str(
                    next1.get("style", "")
                ):
                    radicand = cls.texhtml_to_latex(next1)
                    result_parts.append(f"\\sqrt{{{radicand}}}")
                    i += 2
                    continue
            result_parts.append(cls.texhtml_to_latex(child))
            i += 1
        return "".join(result_parts)

    @classmethod
    def texhtml_to_latex_sfrac(cls, ele: Tag) -> str:
        """Convert a ``sfrac`` span to LaTeX.

        Two layouts exist. The class-based one puts ``span.num`` and
        ``span.den`` inside a ``tion`` wrapper; the style-based one has no
        classes and encodes the parts as stacked ``display: block`` children
        whose ``line-height`` says which part is which. A shrunk first block
        holding an accent glyph is an accent over its base, not a numerator,
        so it is read before the fraction reading. A layout neither reading
        covers is a defect and raises rather than emitting an empty fraction.
        """
        num_span = ele.find(("span",), class_="num")
        den_span = ele.find(("span",), class_="den")
        if isinstance(num_span, Tag) and isinstance(den_span, Tag):
            numerator = cls.texhtml_to_latex_children(num_span.children)
            denominator = cls.texhtml_to_latex_children(den_span.children)
            return f"\\frac{{{numerator}}}{{{denominator}}}"
        blocks = cls._stacked_blocks(ele)
        if len(blocks) == 2:
            top, bottom = blocks
            accent = cls._accent_command(top)
            if accent is not None:
                base = cls.texhtml_to_latex_children(bottom.children)
                return f"{accent}{{{base}}}"
            if [cls._line_height(block) for block in blocks] == ["0.3", "0.7"]:
                numerator = cls.texhtml_to_latex_children(top.children)
                denominator = cls.texhtml_to_latex_children(bottom.children)
                return f"\\frac{{{numerator}}}{{{denominator}}}"
        raise ValueError(f"unreadable sfrac layout: {ele.decode_contents()[:200]}")

    @staticmethod
    def _stacked_blocks(ele: Tag) -> list[Tag]:
        """Return the ``display: block`` children that stack a legacy fraction."""
        return [
            child
            for child in ele.find_all("span")
            if "display: block" in str(child.get("style", ""))
        ]

    @staticmethod
    def _line_height(ele: Tag) -> str | None:
        """Return the ``line-height`` of a stacked block, if it declares one."""
        match = _BLOCK_LINE_HEIGHT_REGEX.search(str(ele.get("style", "")))
        return match.group(1) if match else None

    @classmethod
    def _accent_command(cls, ele: Tag) -> str | None:
        """Return the accent command for a block holding only an accent glyph."""
        text = ele.get_text(strip=True)
        if len(text) == 1 and text in _ACCENT_COMMANDS:
            return _ACCENT_COMMANDS[text]
        return None

    @classmethod
    def replace_texhtml_math_with_math(cls, ele: Tag, soup: BeautifulSoup) -> None:
        """Replace legacy texhtml spans that plain text cannot carry.

        Wikipedia renders part of a formula as HTML instead of MathML: a radical
        drawn as a root sign above a bordered span, a fraction or an accent
        stacked out of styled blocks, and the script that belongs to them. As
        text the vinculum is lost, a fraction collapses to an empty one, and the
        script is left behind as a stray ``<sup>``, so these spans become
        ``<math>`` elements instead. A span holding plain italic letters needs
        no math and is left alone, since prose would otherwise turn into a run
        of single-letter formulas.

        *soup* must be the ``BeautifulSoup`` instance that owns *ele* (to create
        new tags).
        """
        for span in list(ele.find_all("span", class_="texhtml")):
            if not cls._needs_math(span):
                continue
            math_tag = soup.new_tag("math", alttext=cls.texhtml_to_latex(span))
            wrapper = soup.new_tag("span", attrs={"class": "mwe-math-mathml-inline"})
            wrapper.append(math_tag)
            span.replace_with(wrapper)

    @classmethod
    def _needs_math(cls, ele: Tag) -> bool:
        """Whether a texhtml span carries structure that text cannot show."""
        if ele.find(("span",), class_="sfrac") is not None:
            return True
        return any(
            cls._is_sqrt_entity(descendant)
            or "border-top" in str(descendant.get("style", ""))
            for descendant in ele.find_all("span")
        )

    @classmethod
    def replace_sfrac_with_math(cls, ele: Tag, soup: BeautifulSoup) -> None:
        """Replace sfrac elements with inline ``<math>`` elements.

        *soup* must be the ``BeautifulSoup`` instance that owns *ele* (to
        create new tags).
        """
        for sfrac in list(ele.find_all("span", class_="sfrac")):
            if not isinstance(sfrac, Tag):
                continue
            latex = cls.texhtml_to_latex_sfrac(sfrac)
            math_tag = soup.new_tag("math", alttext=latex)
            wrapper = soup.new_tag("span", attrs={"class": "mwe-math-mathml-inline"})
            wrapper.append(math_tag)
            sfrac.replace_with(wrapper)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _escape_latex_text(text: str) -> str:
        """Escape LaTeX special characters and convert Unicode Greek in plain text."""
        _LATEX_GREEK: dict[str, str] = {
            "\u0391": "A",
            "\u0392": "B",
            "\u0393": "{\\Gamma}",
            "\u0394": "{\\Delta}",
            "\u0395": "E",
            "\u0396": "Z",
            "\u0397": "H",
            "\u0398": "{\\Theta}",
            "\u0399": "I",
            "\u039a": "K",
            "\u039b": "{\\Lambda}",
            "\u039c": "M",
            "\u039d": "N",
            "\u039e": "{\\Xi}",
            "\u039f": "O",
            "\u03a0": "{\\Pi}",
            "\u03a1": "P",
            "\u03a3": "{\\Sigma}",
            "\u03a4": "T",
            "\u03a5": "{\\Upsilon}",
            "\u03a6": "{\\Phi}",
            "\u03a7": "X",
            "\u03a8": "{\\Psi}",
            "\u03a9": "{\\Omega}",
            "\u03b1": "{\\alpha}",
            "\u03b2": "{\\beta}",
            "\u03b3": "{\\gamma}",
            "\u03b4": "{\\delta}",
            "\u03b5": "{\\varepsilon}",
            "\u03b6": "{\\zeta}",
            "\u03b7": "{\\eta}",
            "\u03b8": "{\\theta}",
            "\u03b9": "{\\iota}",
            "\u03ba": "{\\kappa}",
            "\u03bb": "{\\lambda}",
            "\u03bc": "{\\mu}",
            "\u03bd": "{\\nu}",
            "\u03be": "{\\xi}",
            "\u03bf": "o",
            "\u03c0": "{\\pi}",
            "\u03c1": "{\\rho}",
            "\u03c2": "{\\varsigma}",
            "\u03c3": "{\\sigma}",
            "\u03c4": "{\\tau}",
            "\u03c5": "{\\upsilon}",
            "\u03c6": "{\\varphi}",
            "\u03c7": "{\\chi}",
            "\u03c8": "{\\psi}",
            "\u03c9": "{\\omega}",
        }
        _LATEX_SPECIAL = str.maketrans(
            {
                "\\": "\\textbackslash{}",
                "&": "\\&",
                "%": "\\%",
                "$": "\\$",
                "#": "\\#",
                "_": "\\_",
                "{": "\\{",
                "}": "\\}",
                "~": "\\textasciitilde{}",
            }
        )
        text = text.translate(_LATEX_SPECIAL)
        for char, latex in _LATEX_GREEK.items():
            text = text.replace(char, latex)
        for char, latex in _MATH_LETTER_COMMANDS.items():
            text = text.replace(char, latex)
        return text

    @staticmethod
    def _is_sqrt_entity(ele: PageElement) -> bool:
        """Check if *ele* is a ``<span typeof="mw:Entity">`` containing √."""
        return (
            isinstance(ele, Tag)
            and ele.name == "span"
            and "mw:Entity" in str(ele.get("typeof", ""))
            and "\u221a" in ele.get_text()
        )


"""Public API of this module (empty)."""
__all__ = ()
