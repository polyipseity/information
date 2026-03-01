"""Lightweight rule tests for the academic-notes validator.

Each function constructs a minimal ValidationContext and exercises a rule
function, verifying expected messages or lack thereof.
"""

import re
from os import PathLike

import pytest
from anyio import Path
from check_mods.models import Frontmatter, Severity, ValidationContext
from check_mods.rules import (
    RULE_REGISTRY,
    aliases_sorted,
    header_style_rule,
    index_children_rule,
    index_heading_rule,
    index_semester_order_rule,
    latex_block_no_newline,
    latex_disallowed_delimiters,
    latex_environment_not_wrapped,
    latex_single_line,
    latex_spacing_before,
    metadata_aliases_present,
    metadata_flash_tag,
    metadata_tags_present,
    no_soft_wrap,
    one_sided_calc_warning,
    session_datetime_order,
    session_duplicate_heading,
    tag_language,
    two_sided_calc_warning,
    unit_outside_math,
)
from check_mods.utils import FRONT_RE, parse_frontmatter
from check_mods.validator import check_markdown_file
from pydantic_yaml import parse_yaml_raw_as

# explicit imports reduce namespace clutter and make references clear


__all__ = ()


def make_ctx(text: str, path: Path = Path("/tmp/course/index.md")) -> ValidationContext:
    """Helper constructing a ValidationContext from raw markdown text."""
    front = parse_frontmatter(text) or ""
    if front:
        try:
            data = parse_yaml_raw_as(Frontmatter, front)
        except Exception:  # pragma: no cover
            data = Frontmatter()
    else:
        data = Frontmatter()

    body = text
    m = FRONT_RE.match(text)
    if m:
        body = text[m.end() :]
    session_headers = []
    for m2 in re.finditer(
        r"^##\s+week\s+(\d+)(?:\s+(\w+))?", text, re.IGNORECASE | re.MULTILINE
    ):
        week = m2.group(1)
        typ = (m2.group(2) or "").lower()
        session_headers.append((week, typ, m2.group(0), m2.start()))
    return ValidationContext(
        path=path,
        text=text,
        front=front,
        data=data,
        body=body,
        session_headers=session_headers,
    )


def test_metadata_aliases_present():
    """The aliases present rule should fire when frontmatter lacks aliases."""
    txt = "---\ntags: []\n---\n"
    ctx = make_ctx(txt)
    msgs = metadata_aliases_present(ctx)
    assert msgs and msgs[0].msg.startswith("no 'aliases:'")
    # also verify the rule is registered in the module registry
    ids = [rid for rid, _ in RULE_REGISTRY.items()]
    assert "metadata_aliases_present" in ids
    txt = "---\naliases:[a]\ntags:[]\n---\n"
    ctx = make_ctx(txt)
    assert not metadata_aliases_present(ctx)


def test_metadata_tags_present_and_flash():
    """Rules should detect missing tags and missing flash activation."""

    txt = "---\naliases: [a]\n---\n"
    ctx = make_ctx(txt)
    msgs = metadata_tags_present(ctx)
    # flash rule should not fire when tags are entirely absent
    assert any("no 'tags:'" in m.msg for m in msgs)

    txt = "---\ntags: []\n---\n"
    ctx = make_ctx(txt)
    msgs = metadata_flash_tag(ctx)
    assert msgs and msgs[0].msg.startswith("missing flashcard")


def test_aliases_sorted_and_tag_language():
    """Aliases order and language tag rules fire appropriately."""

    txt = "---\naliases: [b, a]\ntags: [language/in/English]\n---\n"
    ctx = make_ctx(txt)
    assert aliases_sorted(ctx)
    assert not tag_language(ctx)
    # wrong language
    txt = "---\naliases: [a]\ntags: []\n---\n"
    ctx = make_ctx(txt)
    assert tag_language(ctx)


def test_index_rules():
    """Index-specific rules should only apply to index.md and detect problems."""

    txt = "# some page\n"
    ctx = make_ctx(txt, path=Path("/tmp/index.md"))
    assert index_heading_rule(ctx)
    assert index_children_rule(ctx)

    txt = "# index\n## children\n### 2023 fall\n### 2022 spring\n"
    ctx = make_ctx(txt, path=Path("/tmp/index.md"))
    msgs = index_semester_order_rule(ctx)
    assert msgs and "chronological" in msgs[0].msg


def test_header_style_generic():
    """header_style_rule should emit a warning and explain suppression guidance."""

    txt = "## BadHeader\n"
    ctx = make_ctx(txt, path=Path("/tmp/file.md"))
    msgs = header_style_rule(ctx)
    assert msgs
    assert msgs[0].severity == Severity.WARNING
    assert "lowercase" in msgs[0].msg
    # message now mentions suppression directive so look for either keyword
    assert "check:" in msgs[0].msg or "suppress" in msgs[0].msg


def test_two_sided_calc_warning():
    """Warn when right-hand side has LaTeX but left side does not."""

    txt = "- kcl equation example ::@:: With $I_1,I_2,I_3$ entering and $I_4,I_5$ leaving, $I_1+I_2+I_3=I_4+I_5$.\n"
    ctx = make_ctx(txt)
    msgs = two_sided_calc_warning(ctx)
    assert msgs
    assert msgs[0].severity == Severity.WARNING
    assert "left" in msgs[0].msg and "calculation" in msgs[0].msg

    # if left side also contains LaTeX, no warning
    txt2 = "- calc $a$ ::@:: result $b$\n"
    ctx2 = make_ctx(txt2)
    assert not two_sided_calc_warning(ctx2)

    # one-sided behaviour
    txt3 = "- time const ::@:= RC :@: $RC$\n"
    ctx3 = make_ctx(txt3)
    msgs3 = one_sided_calc_warning(ctx3)
    assert msgs3 and msgs3[0].severity == Severity.WARNING
    assert "one-sided" in msgs3[0].msg
    # two-sided cards should not trigger the one-sided rule even if they
    # contain a ":@:" substring
    assert not one_sided_calc_warning(make_ctx("- a :@: $b$ ::@:: dummy\n"))


def test_session_rules():
    """Session-related rules around duplicates and datetime ordering."""

    txt = "## week 1 lecture\n## week 1 lecture\n"
    ctx = make_ctx(txt)
    msgs = session_duplicate_heading(ctx)
    assert msgs and "duplicate session heading" in msgs[0].msg

    txt = (
        "## week 1 lecture\n- datetime: 2023-01-02T10:00\n"
        "## week 2 lecture\n- datetime: 2023-01-01T09:00\n"
    )
    ctx = make_ctx(txt)
    msgs = session_datetime_order(ctx)
    assert msgs and "not after previous" in msgs[0].msg


def test_unit_outside_math_behavior():
    """Unit rule fires only when math ends in a number and a unit follows."""

    # adjacent to math should be flagged
    txt = "The current is $I=5$ A in this example.\n"
    ctx = make_ctx(txt)
    msgs = unit_outside_math(ctx)
    assert msgs, "unit after math should be caught"
    assert msgs[0].line == 1

    # non-adjacent cases should not trigger
    for txt in (
        "Line one\nCurrent is 5 A here.\n",
        "Show $5 A$ inside math and 6\n",
        "First $x=1$ line\nThen 10 V at start of second line.\n",
    ):
        ctx = make_ctx(txt)
        assert not unit_outside_math(ctx)


def test_latex_spacing_before_paren():
    """Spacing rule allows '(' before dollar but not letters directly."""

    txt = "This is an equation ($x=1$) in parentheses.\n"
    ctx = make_ctx(txt)
    msgs = latex_spacing_before(ctx)
    assert not msgs, "paren before dollar should be allowed"

    txt = "Badexample$x=1$ without space\n"
    ctx = make_ctx(txt)
    msgs = latex_spacing_before(ctx)
    assert msgs, "missing space should be caught even inside text"


def test_latex_disallowed_delimiters():
    r"""Only \(\) or \[\] should be flagged; generic \\ is fine."""
    txt = "Use \\(...\\) style instead of $...$\n"
    ctx = make_ctx(txt)
    msgs = latex_disallowed_delimiters(ctx)
    assert msgs, "should flag forbidden delimiters"

    txt = "This line has a TeX macro \\Omega and a linebreak \\ but no delimiters.\n"
    ctx = make_ctx(txt)
    msgs = latex_disallowed_delimiters(ctx)
    assert not msgs, "plain double backslash should not trigger the rule"


def test_latex_environment_unwrapped():
    """An unwrapped \begin{align*} block should trigger a warning."""
    txt = (
        "\\begin{align*}\n"
        "-5 + 25(I_1-I_2) &= 0,\\\n"
        "50 I_1 + 75 I_2 + 25(I_2 - I_1) &= 0,\n"
        "\\end{align*}\n"
    )
    ctx = make_ctx(txt)
    msgs = latex_environment_not_wrapped(ctx)
    assert msgs, "unwrapped environment should be caught"

    # wrapping in $$ should suppress the warning
    txt2 = "$$\\begin{align*} a \\end{align*}$$\n"
    ctx = make_ctx(txt2)
    assert not latex_environment_not_wrapped(ctx)


def test_latex_single_line_multiline():
    """Inline math spanning lines should be flagged and column end truncated."""
    txt = "$\nfoo\n$"
    ctx = make_ctx(txt)
    msgs = latex_single_line(ctx)
    assert msgs, "multi-line inline math should produce an error"
    m = msgs[0]
    # should point to first line, first column only
    assert m.line == 1
    assert m.col == 1
    assert m.col_end == 1


def test_block_latex_no_newline():
    """Block math delimited by $$ must not contain real newline chars."""
    txt = "$$a \\\n b$$\n"
    ctx = make_ctx(txt)
    msgs = latex_block_no_newline(ctx)
    assert msgs, "newline in block latex should be reported"

    txt2 = "$$a \\\\ b$$\n"  # uses \\\\ for a line break
    ctx = make_ctx(txt2)
    assert not latex_block_no_newline(ctx)


def test_no_soft_wrap_paragraph_and_list():
    """Paragraphs and list items may not be soft-wrapped.

    - A lone newline inside prose should trigger an error.
    - Consecutive blank lines, explicit breaks, or structural boundaries are
      allowed.
    - Similarly, a list item that spans multiple physical lines without using
      ``<br/>``/``<p>`` should be flagged, whereas separate items are fine.
    """
    # simple paragraph violation
    txt = "First line\nsecond line\n"
    ctx = make_ctx(txt)
    msgs = no_soft_wrap(ctx)
    assert msgs and "paragraph" in msgs[0].msg

    # double newline is allowed
    txt = "First line\n\nsecond line\n"
    ctx = make_ctx(txt)
    assert not no_soft_wrap(ctx)

    # explicit backslash escape allowed
    txt = "Line one\\\nline two\n"
    ctx = make_ctx(txt)
    assert not no_soft_wrap(ctx)

    # trailing two spaces allowed
    txt = "Line one  \nline two\n"
    ctx = make_ctx(txt)
    assert not no_soft_wrap(ctx)

    # list item split across lines triggers error
    txt = "- item part1\n  continuation\n"
    ctx = make_ctx(txt)
    msgs = no_soft_wrap(ctx)
    assert msgs and "list item" in msgs[0].msg

    # two separate items are fine
    txt = "- first\n- second\n"
    ctx = make_ctx(txt)
    assert not no_soft_wrap(ctx)

    # <br/> inside item is allowed
    txt = "- line1<br/>\nline2\n"
    ctx = make_ctx(txt)
    assert not no_soft_wrap(ctx)


@pytest.mark.anyio
async def test_suppression_ignore_next_line(tmp_path: PathLike[str]):
    """Directive on its own line suppresses error on the next line."""
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "<!-- check: ignore-next-line[unit_outside_math]: spacing fixed -->\n"
        "Value $I=5$ A is here.\n"
    )
    file = Path(tmp_path) / "test.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert not msgs, "error should be suppressed by directive"


@pytest.mark.anyio
async def test_suppression_ignore_line_and_trimming(tmp_path: PathLike[str]):
    """ignore-line on same line works and rule names are trimmed."""
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "Value $I=5$ A is here.<!-- check: ignore-line[ unit_outside_math ]: because -->\n"
    )
    file = Path(tmp_path) / "line.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert not msgs


@pytest.mark.anyio
async def test_suppression_missing_rationale(tmp_path: PathLike[str]):
    """Directive without rationale emits a warning message in check_markdown_file."""
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        + "<!-- check: ignore-line[unit_outside_math]:   -->\n"
    )
    file = Path(tmp_path) / "empty.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert any("missing rationale" in m.msg for m in msgs)


@pytest.mark.anyio
async def test_suppression_multiple_rules(tmp_path: PathLike[str]):
    """Directive can list multiple rules and should silence both."""
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "<!-- check: ignore-next-line[ unit_outside_math , latex_spacing_before ]: multi -->\n"
        "Bad spacing$x=1$ and unit $I=5$ A\n"
    )
    file = Path(tmp_path) / "multi.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert not msgs
