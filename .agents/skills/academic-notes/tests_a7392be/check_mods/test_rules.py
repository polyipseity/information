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
    folder_link_trailing_slash_rule,
    header_flashcard_presence,
    header_style_rule,
    index_children_format_rule,
    index_children_order_rule,
    index_children_rule,
    index_heading_rule,
    index_semester_order_rule,
    latex_block_no_newline,
    latex_disallowed_delimiters,
    latex_environment_not_wrapped,
    latex_single_line,
    latex_spacing_after,
    latex_spacing_before,
    metadata_aliases_present,
    metadata_flash_tag,
    metadata_tags_present,
    no_control_characters,
    no_lecture_summary,
    no_soft_wrap_list,
    no_soft_wrap_paragraph,
    numeric_text_not_latex,
    one_sided_calc_warning,
    qa_hierarchical_path,
    qa_nested_indentation,
    section_example_heading,
    session_datetime_order,
    session_duplicate_heading,
    session_heading_format,
    session_missing_topic,
    session_unscheduled_with_topic,
    tag_language,
    tag_path_flash,
    topic_note_redundant_filename_prefix,
    two_sided_calc_warning,
    unit_outside_math,
)
from check_mods.utils import FRONT_RE, parse_frontmatter
from check_mods.validator import check_markdown_file
from pydantic_yaml import parse_yaml_raw_as

# explicit imports reduce namespace clutter and make references clear


"""Public symbols exported by this module (none)."""
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
    # Same pattern as validator: week N type [number]; type = lecture|lab|tutorial only (status has no bearing on heading)
    session_headers: list[tuple[str, str, str, int]] = []
    _re = re.compile(
        r"^##\s+week\s+(\d+)\s+((?:lecture|lab|tutorial)(?:\s+\d+)?|no\s+class)\s*$",
        re.IGNORECASE | re.MULTILINE,
    )
    for m2 in _re.finditer(text):
        week = m2.group(1)
        typ = m2.group(2).strip().lower()
        session_headers.append((week, typ, m2.group(0).strip(), m2.start()))
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


def test_rule_ids_match_function_names():
    """Every registered rule should use its function name as the identifier.

    This ensures a single, consistent naming convention: rule IDs are
    derived from the Python function name and normalised to lowercase with
    underscores.  The validator relies on this invariant for suppression
    directives and error reporting.
    """
    for rid, func in RULE_REGISTRY.items():
        assert rid == func.__name__, (
            f"rule id {rid!r} does not match function name {func.__name__!r}"
        )


def test_control_characters_detected():
    """The control-character rule should fire when an illegal character is present."""
    # embed a BEL character (U+0007) which is not allowed
    txt = "First line\x07Second line\n"
    ctx = make_ctx(txt)
    msgs = no_control_characters(ctx)
    assert msgs, "control character should be reported"
    assert "U+0007" in msgs[0].msg
    # file without control chars should be clean
    assert not no_control_characters(make_ctx("normal text\n"))


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


@pytest.mark.anyio
async def test_index_children_format_and_order_rules():
    """Children section must be a flat list of links sorted by folder/file."""

    txt = "# index\n\n## children\n- [assignments](assignments/)\n- [a](a.md)\n- [b](b.md)\n"
    ctx = make_ctx(txt, path=Path("/tmp/index.md"))
    assert not index_children_format_rule(ctx)
    assert not await index_children_order_rule(ctx)

    # nested bullets are rejected
    txt = "# index\n\n## children\n  - [a](a.md)\n- [b](b.md)\n"
    ctx = make_ctx(txt, path=Path("/tmp/index.md"))
    msgs = index_children_format_rule(ctx)
    assert msgs and "top-level" in msgs[0].msg

    # folders must come before files
    txt = "# index\n\n## children\n- [a](a.md)\n- [assignments](assignments/)\n"
    ctx = make_ctx(txt, path=Path("/tmp/index.md"))
    msgs = await index_children_order_rule(ctx)
    assert msgs and "folder entries" in msgs[0].msg

    # files must be alphabetically ordered
    txt = "# index\n\n## children\n- [assignments](assignments/)\n- [b](b.md)\n- [a](a.md)\n"
    ctx = make_ctx(txt, path=Path("/tmp/index.md"))
    msgs = await index_children_order_rule(ctx)
    assert msgs and "alphabetical" in msgs[0].msg


def test_header_style_generic():
    """header_style_rule should emit a warning and clarify suppression.

    Capitalization is not a mere style preference; proper nouns only may be
    exempted.  The message should mention "proper noun" to guide authors."""

    txt = "## BadHeader\n"
    ctx = make_ctx(txt, path=Path("/tmp/file.md"))
    msgs = header_style_rule(ctx)
    assert msgs
    assert msgs[0].severity == Severity.WARNING
    assert "lowercase" in msgs[0].msg
    assert "proper noun" in msgs[0].msg


def test_header_flashcard_presence_applies_to_all_levels():
    """Flashcard presence rules should apply to headers at any level.

    A top-level header (#) should be checked just like a subsection.
    """

    txt = "# Topic\nThis section has no flashcards.\n"
    ctx = make_ctx(txt, path=Path("/tmp/file.md"))
    msgs = header_flashcard_presence(ctx)
    assert msgs and msgs[0].rule_id == "header_flashcard_presence"

    # When flashcards exist under the header, no message should be emitted.
    txt2 = "# Topic\nSome text\n\nTerm ::@:: Definition\n"
    ctx2 = make_ctx(txt2, path=Path("/tmp/file.md"))
    assert not header_flashcard_presence(ctx2)


@pytest.mark.anyio
async def test_folder_link_slash_ignores_index_md(tmp_path: PathLike[str]):
    """Links to index.md should not be treated as a folder for trailing-slash rules."""

    # Create a temporary directory with an index.md to ensure the link resolves.
    dir_path = Path(tmp_path)
    await (dir_path / "index.md").write_text("# index\n")

    # Create a context for a different file in the same directory.
    ctx = make_ctx("[index](index.md)\n", path=Path(dir_path / "note.md"))

    msgs = await folder_link_trailing_slash_rule(ctx)
    assert not msgs, "A link to index.md should not require a trailing slash"


def test_example_section_heading():
    """Files should not define standalone example sections.

    The rule fires on any header whose text contains the word "example"
    (case insensitive). Authors are instructed to remove the entire section
    and merge examples into appropriate conceptual headings.
    """

    txt = "## Example\nSome illustrative material\n"
    ctx = make_ctx(txt)
    msgs = section_example_heading(ctx)
    assert msgs and msgs[0].rule_id == "section_example_heading"
    # message should mention example sections, integration into conceptual
    # paragraphs, and discourage suppressing calculation warnings
    assert "example sections" in msgs[0].msg
    assert "integrate" in msgs[0].msg
    assert "two_sided_calc_warning" in msgs[0].msg

    # different casing and within a longer title should also trigger
    txt2 = "### Resistive circuit examples and notes\nContent\n"
    ctx2 = make_ctx(txt2)
    msgs2 = section_example_heading(ctx2)
    assert msgs2

    # unrelated heading should be ignored
    txt3 = "## Explanation of example-less topic\n"
    ctx3 = make_ctx(txt3)
    assert not section_example_heading(ctx3)


def test_tag_path_flash_quotes_and_spaces():
    """The path-derived flash tag rule should normalize spaces and quotes.

    Filenames containing spaces, single quotes or double quotes should be
    converted to underscores when constructing the expected tag.  The rule
    reports an error if none of the tags contain the normalized path segment.
    """

    # construct a path that exercises spaces and both kinds of quotes
    path = Path('/tmp/special/academia/HKUST/ELEC 1100/Week\'s "Notes".md')
    # build the context with a matching tag
    txt = "---\ntags: [flashcard/active/special/academia/HKUST/ELEC_1100/Week_s_Notes]\n---\n"
    ctx = make_ctx(txt, path=path)
    # no error should be raised when the normalized tag is present
    assert not tag_path_flash(ctx)

    # missing tag should trigger an error mentioning the normalized path
    txt = "---\ntags: [flashcard/active/special/academia/HKUST/ELEC_1100]\n---\n"
    ctx = make_ctx(txt, path=path)
    msgs = tag_path_flash(ctx)
    assert msgs and "Week_s_Notes" in msgs[0].msg

    # different casing and within a longer title should also trigger
    txt2 = "### Resistive circuit examples and notes\nContent\n"
    ctx2 = make_ctx(txt2)
    msgs2 = section_example_heading(ctx2)
    assert msgs2

    # unrelated heading should be ignored
    txt3 = "## Explanation of example-less topic\n"
    ctx3 = make_ctx(txt3)
    assert not section_example_heading(ctx3)


def test_no_lecture_summary():
    """Files containing a "lecture summary" heading, bullet, or summary-card should error."""

    # heading case
    txt = "## lecture summary\nSome text\n"
    ctx = make_ctx(txt)
    msgs = no_lecture_summary(ctx)
    assert msgs and msgs[0].rule_id == "no_lecture_summary"

    # bullet case should also be caught
    txt2 = "- lecture summary ::@:: stuff\n"
    ctx2 = make_ctx(txt2)
    msgs2 = no_lecture_summary(ctx2)
    assert msgs2 and msgs2[0].rule_id == "no_lecture_summary"

    # summary sentence card should trigger
    txt3 = "- summary sentence ::@:: this is just a sentence\n"
    ctx3 = make_ctx(txt3)
    msgs3 = no_lecture_summary(ctx3)
    assert msgs3 and msgs3[0].rule_id == "no_lecture_summary"


def test_two_sided_calc_warning():
    """Warn when right-hand side has LaTeX but left side does not."""

    txt = "- kcl equation example ::@:: With $I_1,I_2,I_3$ entering and $I_4,I_5$ leaving, $I_1+I_2+I_3=I_4+I_5$.\n"
    ctx = make_ctx(txt)
    msgs = two_sided_calc_warning(ctx)
    assert msgs
    assert msgs[0].severity == Severity.WARNING
    # warning should insist on copying/duplicating data, allow long prompts, and discourage suppression
    assert "Right-hand side" in msgs[0].msg
    assert "before" in msgs[0].msg and "after" in msgs[0].msg
    assert "context" in msgs[0].msg
    assert "example" in msgs[0].msg.lower()
    assert (
        "suppress" in msgs[0].msg
        or "ignore-line" in msgs[0].msg
        or "check directive" in msgs[0].msg
    )

    # if left side also contains LaTeX, no warning
    txt2 = "- calc $a$ ::@:: result $b$\n"
    ctx2 = make_ctx(txt2)
    assert not two_sided_calc_warning(ctx2)

    # numeric data without dollar signs on the left should emit the warning
    txt2b = "- heater draws 8.5\times10^{20} electrons in 10 s ::@:: $q=Ne$\n"
    ctx2b = make_ctx(txt2b)
    assert two_sided_calc_warning(ctx2b)

    # the real-world example from the repository should not warn either
    txt2c = (
        "- current example heater: A heater draws $8.5\\times10^{20}$ electrons "
        "in $10\\,\\textrm{s}$ ($e=1.6\\times10^{-19}\\,\\textrm{C}$); find $q$ and $I$. "
        "::@:: $q=Ne\\approx136\\,\\textrm{C}$ and $I=q/t\\approx13.6\\,\\textrm{A}$\n"
    )
    ctx2c = make_ctx(txt2c)
    assert not two_sided_calc_warning(ctx2c)

    # one-sided behaviour
    txt3 = "- time const ::@:= RC :@: $RC$\n"
    ctx3 = make_ctx(txt3)
    msgs3 = one_sided_calc_warning(ctx3)
    assert msgs3 and msgs3[0].severity == Severity.WARNING
    # message should mention right-hand side and prompt, and warn about examples
    assert "Right-hand side" in msgs3[0].msg
    assert "before" in msgs3[0].msg and "after" in msgs3[0].msg
    assert "prompt" in msgs3[0].msg
    assert "example" in msgs3[0].msg.lower()
    assert (
        "suppress" in msgs3[0].msg
        or "ignore-line" in msgs3[0].msg
        or "check directive" in msgs3[0].msg
    )
    assert "ignore-line" in msgs3[0].msg or "check directive" in msgs3[0].msg

    # numeric prompt should emit warning without dollar signs
    txt3b = "- charge 5 C :@: $q=It$\n"
    ctx3b = make_ctx(txt3b)
    assert one_sided_calc_warning(ctx3b)

    # two-sided cards should not trigger the one-sided rule even if they
    # contain a ":@:" substring
    assert not one_sided_calc_warning(make_ctx("- a :@: $b$ ::@:: dummy\n"))


def test_session_rules():
    """Session-related rules around duplicates and datetime ordering."""

    txt = "## week 1 lecture\n## week 1 lecture\n"
    ctx = make_ctx(txt)
    msgs = session_duplicate_heading(ctx)
    assert msgs and "duplicate session heading" in msgs[0].msg

    # "lecture" and "lecture 2" are distinct types (allowed format: week N type [number])
    txt_distinct = "## week 1 lecture\n- datetime: 2023-01-01\n## week 1 lecture 2\n- datetime: 2023-01-02\n"
    ctx_distinct = make_ctx(txt_distinct)
    assert not session_duplicate_heading(ctx_distinct), (
        "week 1 lecture and week 1 lecture 2 should not be treated as duplicates"
    )

    # Invalid session heading format is flagged (only week N type [number]; no "no class")
    for invalid in (
        "## week 3 (Lunar New Year)\n",
        "## week 3\n",
        "## week 5 midterm\n",
        "## week 3 no class\n",
    ):
        ctx_invalid = make_ctx(invalid)
        msgs_fmt = session_heading_format(ctx_invalid)
        assert msgs_fmt and msgs_fmt[0].rule_id == "session_heading_format", (
            f"expected session_heading_format error for {invalid!r}"
        )
    assert not session_heading_format(
        make_ctx("## week 1 lecture\n## week 1 lecture 2\n")
    )

    txt = (
        "## week 1 lecture\n- datetime: 2023-01-02T10:00\n"
        "## week 2 lecture\n- datetime: 2023-01-01T09:00\n"
    )
    ctx = make_ctx(txt)
    msgs = session_datetime_order(ctx)
    assert msgs and "not after previous" in msgs[0].msg


def test_session_topic_rules():
    """Verify the new topic-related rules fire independently."""

    # missing-topic when a datetime is present and no status/unscheduled tag
    txt = "## week 1 lecture\n- datetime: 2023-01-01T10:00\n"
    ctx = make_ctx(txt)
    msgs = session_missing_topic(ctx)
    assert msgs and msgs[0].rule_id == "session_missing_topic"

    # unscheduled with topic should trigger its own rule
    txt2 = (
        "## week 1 lecture\n"
        "- datetime: 2023-01-01T10:00\n"
        "- status: unscheduled\n"
        "- topic: TBD\n"
    )
    ctx2 = make_ctx(txt2)
    msgs2 = session_unscheduled_with_topic(ctx2)
    assert msgs2 and msgs2[0].rule_id == "session_unscheduled_with_topic"

    # combinations should not leak between rules
    assert not session_missing_topic(ctx2)  # because status is unscheduled
    assert not session_unscheduled_with_topic(make_ctx("## w\n- datetime: 2023-01-01"))

    # no-class days omit topic; should not trigger session_missing_topic (heading is week N lecture etc.; status in metadata)
    for no_class_txt in (
        "## week 3 lecture\n- datetime: 2026-02-18T16:30:00+08:00/2026-02-18T17:50:00+08:00\n- status: no class\n- venue: LSK Room 1014\n",
        "## week 3 lecture\n- datetime: 2026-02-18T16:30:00+08:00/2026-02-18T17:50:00+08:00\n- status: public holiday: Lunar New Year\n- venue: LSK Room 1014\n",
    ):
        ctx_nc = make_ctx(no_class_txt)
        assert not session_missing_topic(ctx_nc), (
            "no-class / public holiday sessions may omit topic"
        )


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


def test_numeric_text_not_latex():
    """Lines with numbers/units or simple equations should warn when not in $...$."""

    # example from user request
    txt = (
        "numeric example with single source ::@:: 5 V into 50 Ω+75 Ω series "
        "with 25 Ω parallel branch gives I2=0.04 A, I3=0.20 A, I1=0.24 A.\n"
    )
    ctx = make_ctx(txt)
    msgs = numeric_text_not_latex(ctx)
    assert msgs, "plain-text numeric quantities should produce a warning"
    assert msgs[0].severity == Severity.WARNING
    assert "wrap quantities" in msgs[0].msg

    # if the line already contains dollars, the rule should be silent
    txt2 = R"The source is $5\,\mathrm{V}$ and I=0.1\,\mathrm{A}.\n"
    ctx2 = make_ctx(txt2)
    assert not numeric_text_not_latex(ctx2)

    # a line with numbers but no units/equations should not trigger
    txt3 = "Lecture 5 covers resistors and capacitors.\n"
    assert not numeric_text_not_latex(make_ctx(txt3))

    # suppression directives should work (reuse existing suppression tests)
    txt4 = (
        "<!-- check: ignore-line[numeric_text_not_latex]: example -->\n"
        "5 V is the supply.\n"
    )
    ctx4 = make_ctx(txt4)
    msgs4 = numeric_text_not_latex(ctx4)
    # rule itself will still return a message, but suppression is handled
    # by check_markdown_file; here we just ensure the pattern matches
    assert msgs4

    # and numeric expressions inside code fences should be ignored entirely
    txt5 = "```text\n5 V and 10 A should not trigger\n```\n"
    ctx5 = make_ctx(txt5)
    assert not numeric_text_not_latex(ctx5), "code fences must be skipped"


def test_qa_hierarchical_path_nested_labels():
    """Nested QA cards must include the full parent path on the left side.

    The left-hand gloss for an indented card should start with
    '<parent path> /' rather than omitting the immediate parent segment.
    """

    # Correct hierarchical paths: children start with full parent label + " /"
    good = (
        "- ELEC 1100\n"
        "  - ELEC 1100 / lab 1 preparation / breadboard and equipment\n"
        "    - ELEC 1100 / lab 1 preparation / breadboard and equipment / lab equipment overview ::@:: details\n"
        "    - ELEC 1100 / lab 1 preparation / breadboard and equipment / breadboard internal connections ::@:: details\n"
    )
    ctx_good = make_ctx(good)
    assert not qa_hierarchical_path(ctx_good)

    # Missing the immediate parent segment in the child gloss should be flagged
    bad = (
        "- ELEC 1100\n"
        "  - ELEC 1100 / lab 1 preparation / breadboard and equipment\n"
        "    - ELEC 1100 / lab 1 preparation / lab equipment overview ::@:: details\n"
    )
    ctx_bad = make_ctx(bad)
    msgs = qa_hierarchical_path(ctx_bad)
    assert msgs and msgs[0].rule_id == "qa_hierarchical_path"

    # Topic-note nested flashcards should follow the same full-parent-path rule
    good_topic = (
        "Flashcards for this section are as follows:\n\n"
        "- discrete distributions / Poisson approximation\n"
        "  - discrete distributions / Poisson approximation / statement ::@:: details\n"
        "  - discrete distributions / Poisson approximation / intuition ::@:: details\n"
    )
    assert not qa_hierarchical_path(make_ctx(good_topic, Path("/tmp/course/topic.md")))

    bad_topic = (
        "Flashcards for this section are as follows:\n\n"
        "- discrete distributions / Poisson approximation\n"
        "  - discrete distributions / intuition ::@:: details\n"
    )
    msgs_topic = qa_hierarchical_path(make_ctx(bad_topic, Path("/tmp/course/topic.md")))
    assert msgs_topic and msgs_topic[0].rule_id == "qa_hierarchical_path"


def test_qa_nested_indentation_two_spaces_per_level():
    """Nested flashcard bullets should indent by exactly two spaces per level."""

    good = (
        "Flashcards for this section are as follows:\n\n"
        "- discrete distributions / Poisson approximation\n"
        "  - discrete distributions / Poisson approximation / statement ::@:: details\n"
        "  - discrete distributions / Poisson approximation / intuition ::@:: details\n"
    )
    assert not qa_nested_indentation(make_ctx(good, Path("/tmp/course/topic.md")))

    bad_odd = (
        "Flashcards for this section are as follows:\n\n"
        "- discrete distributions / Poisson approximation\n"
        "   - discrete distributions / Poisson approximation / statement ::@:: details\n"
    )
    msgs_odd = qa_nested_indentation(make_ctx(bad_odd, Path("/tmp/course/topic.md")))
    assert msgs_odd and msgs_odd[0].rule_id == "qa_nested_indentation"

    bad_jump = (
        "Flashcards for this section are as follows:\n\n"
        "- discrete distributions / Poisson approximation\n"
        "    - discrete distributions / Poisson approximation / statement ::@:: details\n"
    )
    msgs_jump = qa_nested_indentation(make_ctx(bad_jump, Path("/tmp/course/topic.md")))
    assert msgs_jump and msgs_jump[0].rule_id == "qa_nested_indentation"


def test_topic_note_redundant_filename_prefix():
    """Topic-note flashcards should not repeat the filename or title."""

    good = (
        "Flashcards for this section are as follows:\n\n"
        "- definition ::@:: details\n"
        "- Poisson approximation\n"
        "  - Poisson approximation / statement ::@:: details\n"
    )
    assert not topic_note_redundant_filename_prefix(
        make_ctx(good, Path("/tmp/course/discrete distributions.md"))
    )

    bad_top = (
        "Flashcards for this section are as follows:\n\n"
        "- discrete distributions / definition ::@:: details\n"
    )
    msgs_top = topic_note_redundant_filename_prefix(
        make_ctx(bad_top, Path("/tmp/course/discrete distributions.md"))
    )
    assert msgs_top and msgs_top[0].rule_id == "topic_note_redundant_filename_prefix"

    bad_nested = (
        "Flashcards for this section are as follows:\n\n"
        "- Poisson approximation\n"
        "  - discrete distributions / Poisson approximation / statement ::@:: details\n"
    )
    msgs_nested = topic_note_redundant_filename_prefix(
        make_ctx(bad_nested, Path("/tmp/course/discrete distributions.md"))
    )
    assert (
        msgs_nested and msgs_nested[0].rule_id == "topic_note_redundant_filename_prefix"
    )

    bad_title_only = (
        "# Probability Measure\n\n"
        "Flashcards for this section are as follows:\n\n"
        "- Probability Measure ::@:: details\n"
    )
    msgs_title_only = topic_note_redundant_filename_prefix(
        make_ctx(bad_title_only, Path("/tmp/course/probability measure.md"))
    )
    assert (
        msgs_title_only
        and msgs_title_only[0].rule_id == "topic_note_redundant_filename_prefix"
    )

    bad_title_prefix = (
        "# Probability Measure\n\n"
        "Flashcards for this section are as follows:\n\n"
        "- Probability Measure / definition ::@:: details\n"
    )
    msgs_title_prefix = topic_note_redundant_filename_prefix(
        make_ctx(bad_title_prefix, Path("/tmp/course/probability measure.md"))
    )
    assert (
        msgs_title_prefix
        and msgs_title_prefix[0].rule_id == "topic_note_redundant_filename_prefix"
    )


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


def test_latex_spacing_ignore_code():
    """Math inside code fences should not trigger spacing rules."""

    txt = "```text\nBadexample$x=1$\n```\n"
    ctx = make_ctx(txt)
    assert not latex_spacing_before(ctx)
    assert not latex_spacing_after(ctx)


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


def test_latex_single_line_ignore_code():
    """Even malformed math inside code fences must be ignored."""
    txt = "```text\n$\nfoo\n$\n```\n"
    ctx = make_ctx(txt)
    assert not latex_single_line(ctx)


def test_block_latex_no_newline():
    """Block math delimited by $$ must not contain real newline chars."""
    txt = "$$a \\\n b$$\n"
    ctx = make_ctx(txt)
    msgs = latex_block_no_newline(ctx)
    assert msgs, "newline in block latex should be reported"

    txt2 = "$$a \\\\ b$$\n"  # uses \\\\ for a line break
    ctx = make_ctx(txt2)
    assert not latex_block_no_newline(ctx)


def test_no_soft_wrap_paragraph():
    """Only paragraph violations should be reported by paragraph rule."""
    txt = "First line\nsecond line\n"
    ctx = make_ctx(txt)
    msgs = no_soft_wrap_paragraph(ctx)
    assert msgs and "soft-wrapped" in msgs[0].msg

    # other paragraph allowances
    for good in [
        "First line\n\nsecond line\n",
        "Line one\\\nline two\n",
        "Line one  \nline two\n",
    ]:
        assert not no_soft_wrap_paragraph(make_ctx(good))

    # list-wrapping should not trigger paragraph rule
    txt = "- item part1\n  continuation\n"
    ctx = make_ctx(txt)
    assert not no_soft_wrap_paragraph(ctx)

    # only table rows are exempt (after stripping blockquote); blockquote prose still applies
    for good in [
        "> scenario line\n> \n> | | Dr | Cr |\n> |--|--:|--:|\n> | Cash | 50,000 | |\n",
        "| a | b |\n|--|--|\n| 1 | 2 |\n",
        ">> | a | b |\n>> |--|--|\n>> | 1 | 2 |\n",
        "> > | x |\n> > |--|\n",
    ]:
        assert not no_soft_wrap_paragraph(make_ctx(good)), (
            "table rows (with or without blockquote) must not be flagged"
        )

    # blockquote with two prose lines is still soft-wrap
    txt = "> first line\n> second line\n"
    ctx = make_ctx(txt)
    msgs = no_soft_wrap_paragraph(ctx)
    assert msgs and "soft-wrapped" in msgs[0].msg, (
        "blockquote prose lines must still be flagged as soft-wrapped"
    )

    # nested blockquote with two prose lines is still soft-wrap
    txt = ">> alpha\n>> beta\n"
    ctx = make_ctx(txt)
    msgs = no_soft_wrap_paragraph(ctx)
    assert msgs and "soft-wrapped" in msgs[0].msg


def test_no_soft_wrap_list():
    """Only list-item violations should be reported by list rule."""
    txt = "- item part1\n  continuation\n"
    ctx = make_ctx(txt)
    msgs = no_soft_wrap_list(ctx)
    assert msgs and "soft-wrapped" in msgs[0].msg

    # allowed list cases
    for good in [
        "- first\n- second\n",
        "- line1<br/>\nline2\n",
    ]:
        assert not no_soft_wrap_list(make_ctx(good))

    # paragraph soft wrap should not trigger list rule
    txt = "First line\nsecond line\n"
    ctx = make_ctx(txt)
    assert not no_soft_wrap_list(ctx)


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
async def test_suppression_numeric_text_rule(tmp_path: PathLike[str]):
    """Ensure suppressing numeric_text_not_latex works via check_markdown_file."""
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "<!-- check: ignore-next-line[numeric_text_not_latex]: because -->\n"
        "5 V supply is given.\n"
    )
    file = Path(tmp_path) / "numeric.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert not msgs, "numeric_text_not_latex warning should be suppressed"


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


@pytest.mark.anyio
async def test_suppression_duplicate_directives(tmp_path: PathLike[str]):
    """Two suppression comments of the same kind on one line should error.

    Authors should merge them into a single directive since the syntax
    already permits listing multiple rule names in a comma-separated list.
    """
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "Some useful text <!-- check: ignore-line[two_sided_calc_warning]: first --> "
        "<!-- check: ignore-line[qa_missing_separator]: second -->\n"
    )
    file = Path(tmp_path) / "dup.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    # Should produce a message with our new rule id
    assert any(m.rule_id == "suppression-multiple-commands" for m in msgs)
    assert any("merge" in m.msg for m in msgs)


@pytest.mark.anyio
async def test_suppression_redundant(tmp_path: PathLike[str]):
    """A suppression for a rule that never fires should be reported as error."""
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "<!-- check: ignore-line[unit_outside_math]: unnecessary -->\n"
        "Just some ordinary prose without any units or math\n"
    )
    file = Path(tmp_path) / "redundant.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert any(m.rule_id == "suppression-redundant" for m in msgs), msgs


@pytest.mark.anyio
async def test_file_level_suppression_hides_index_rules(tmp_path: PathLike[str]):
    """ignore-file should suppress all messages for the listed rules in a file.

    This is used for assignment-style index pages (e.g. labs/lab N/index.md)
    that do not follow the standard course index shell (# index + children).
    The redundancy check must consider the whole file: as long as at least one
    diagnostic for the rule exists anywhere, ignore-file is not redundant.
    """

    text = (
        "---\n"
        "aliases: [a]\n"
        "tags: [language/in/English, flashcard/active/special/academia/test/index]\n"
        "---\n"
        "<!-- check: ignore-file[index_heading_rule,index_children_rule]: assignment index without shell -->\n"
        "# some page\n"
        "## not-children\n"
    )
    file = Path(tmp_path) / "index.md"
    await file.write_text(text)

    # Without suppression, both index rules would fire on this path; with
    # ignore-file they should be fully removed from the result set.
    msgs = list(await check_markdown_file(file))
    assert not any(
        m.rule_id in {"index_heading_rule", "index_children_rule"} for m in msgs
    )
    # The suppression itself must not be marked redundant because those rules
    # would have produced diagnostics somewhere in the file.
    assert not any(m.rule_id == "suppression-redundant" for m in msgs)


@pytest.mark.anyio
async def test_file_level_suppression_redundant(tmp_path: PathLike[str]):
    """ignore-file should error when the rule never fires anywhere in the file."""

    text = (
        "---\n"
        "aliases: [a]\n"
        "tags: [language/in/English, flashcard/active/special/academia/test]\n"
        "---\n"
        "<!-- check: ignore-file[unit_outside_math]: unnecessary -->\n"
        "Plain text with no units after math symbols.\n"
    )
    file = Path(tmp_path) / "file_redundant.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert any(m.rule_id == "suppression-redundant" for m in msgs), msgs
