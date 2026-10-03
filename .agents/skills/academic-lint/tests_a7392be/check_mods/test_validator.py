"""Tests for validator module behaviour related to registries."""

import sys
from collections.abc import Sequence
from os import PathLike

import main
import pytest
from anyio import Path
from main_mods import validator
from main_mods.models import ValidationMessage
from main_mods.registry import RuleRegistry
from main_mods.rules import RULE_REGISTRY as RULES_REGISTRY
from main_mods.validator import RULE_REGISTRY as VALIDATOR_REGISTRY
from main_mods.validator import check_markdown_file, walk_and_check

"""Public symbols exported by this module (none)."""
__all__ = ()


def test_validator_registry_contains_rules():
    """The registry built by the validator should include rules from rules.py."""
    ids = [rid for rid, _ in VALIDATOR_REGISTRY.items()]
    assert "metadata_aliases_present" in ids
    # ensure registry is a separate object from the rules module's own
    assert VALIDATOR_REGISTRY is not RULES_REGISTRY


async def make_temp_markdown(tmp_path: PathLike[str], content: str) -> Path:
    """Helper to write a markdown file and return its Path object.

    The returned object is an :class:`anyio.Path` so callers can use
    asynchronous file operations in tests.
    """

    path = Path(tmp_path) / "file.md"
    # create any necessary parent directories
    await path.parent.mkdir(parents=True, exist_ok=True)
    await path.write_text(content)

    return path


@pytest.mark.anyio
async def test_check_markdown_file_missing_frontmatter(tmp_path: PathLike[str]):
    """Validator should report missing frontmatter correctly."""
    p = await make_temp_markdown(tmp_path, "no frontmatter here")
    msgs = await check_markdown_file(p)
    assert any(
        m.rule_id == "missing_yaml_frontmatter"
        and m.msg.startswith("missing YAML frontmatter")
        for m in msgs
    ), f"expected missing frontmatter error, got {[str(m) for m in msgs]}"


@pytest.mark.anyio
async def test_validator_detects_mismatched_rule_id(tmp_path: PathLike[str]):
    """Main should fail if a rule id does not equal the function name."""
    # create a minimal file to run against (path itself isn't used later)
    _path = await make_temp_markdown(tmp_path, "---\naliases: []\ntags: []\n---\n")

    # temporarily inject a badly named rule into the registry
    def bogus(ctx):
        """Fake rule used to trigger mismatched id detection."""
        return []

    VALIDATOR_REGISTRY.register(id="not_matching_name")(bogus)
    try:
        with pytest.raises(SystemExit) as exc_info:
            await validator.main([str(tmp_path)])
        assert exc_info.value.code == 3
    finally:
        VALIDATOR_REGISTRY._rules.pop("not_matching_name", None)


@pytest.mark.anyio
async def test_check_markdown_file_and_rule_exception(
    tmp_path: PathLike[str], monkeypatch
):
    """A rule that raises should be reported as an exception message."""
    # create a simple file with minimal valid frontmatter
    p = await make_temp_markdown(tmp_path, "---\naliases: []\ntags: []\n---\n")

    # temporarily add a rule that raises
    def bad_rule(ctx):
        """Fake rule used to trigger an exception path."""
        raise RuntimeError("boom")

    VALIDATOR_REGISTRY.register(id="bad")(bad_rule)
    try:
        msgs = await check_markdown_file(p)
        assert any("exception in rule bad_rule" in m.msg for m in msgs)
    finally:
        # remove the bad rule so other tests are unaffected
        VALIDATOR_REGISTRY._rules.pop("bad", None)


@pytest.mark.anyio
async def test_walk_and_check_and_main_json(
    tmp_path: PathLike[str], capsys: pytest.CaptureFixture[str]
):
    """walk_and_check should find errors and main() should output JSON."""
    # create two files: one valid, one with missing aliases
    _good = await make_temp_markdown(
        tmp_path,
        # use a tag matching the flashcard/active/special/academia prefix
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n",
    )
    bad = await make_temp_markdown(Path(tmp_path) / "sub", "---\ntags: []\n---\n")
    # run walk_and_check on directory
    res = await walk_and_check([Path(tmp_path)])
    # should record errors for bad file
    assert any(p == bad for p, _ in res.errors())

    # also verify that a single-file root is handled correctly
    res2 = await walk_and_check([bad])
    assert any(p == bad for p, _ in res2.errors())
    # and good file alone yields no errors
    res3 = await walk_and_check([_good])
    assert not res3.errors()

    # test main output with --json (directory path remains supported)
    with pytest.raises(SystemExit) as exc_info:
        await validator.main([str(tmp_path), "--json"])
    assert exc_info.value.code == 2
    out = capsys.readouterr().out
    # output should now use a single 'issues' key containing messages
    assert "issues" in out
    assert "missing" in out
    # ensure severity properties appear
    assert '"severity": "warning"' in out or '"severity": "error"' in out


@pytest.mark.anyio
async def test_main_prints_errors_and_warnings_together(
    tmp_path: PathLike[str], capsys: pytest.CaptureFixture[str]
):
    """Non-json output should include both errors and warnings with prefixes."""
    # create one file that triggers a warning (uppercase header)
    _file_warn = await make_temp_markdown(
        tmp_path,
        """---
aliases: [a]
tags: [language/in/English, flashcard/active/special/academia/test]
---
## BadHeader
""",
    )
    # create one file that triggers an error
    _file_err = await make_temp_markdown(
        Path(tmp_path) / "err.md", "---\ntags: []\n---\n"
    )
    with pytest.raises(SystemExit) as exc_info:
        await validator.main([str(tmp_path)])
    assert exc_info.value.code == 2
    out = capsys.readouterr().out.lower()
    assert "warning" in out
    assert "error" in out
    # the colored prefix should show the rule id with severity
    assert "[warning/" in out or "[error/" in out


@pytest.mark.anyio
async def test_max_per_rule_limit(
    tmp_path: PathLike[str], capsys: pytest.CaptureFixture[str], monkeypatch
):
    """CLI should limit displayed occurrences per rule using --max-per-rule.

    To avoid incidental noise from unrelated rules (e.g. flashcard tag
    checks) we temporarily replace ``validator.RULE_REGISTRY`` with a
    lightweight registry containing only the ``metadata_aliases_present``
    rule.  This ensures each bad file contributes exactly one issue.
    """
    # build a minimal registry with just the alias rule
    alias_func = RULES_REGISTRY._rules.get("metadata_aliases_present")
    assert alias_func is not None, "alias rule must exist"

    newreg = RuleRegistry()
    newreg.register(id="metadata_aliases_present")(alias_func)
    monkeypatch.setattr(validator, "RULE_REGISTRY", newreg)

    # create six files that all trigger the same error (missing aliases)
    for i in range(6):
        fpath = Path(tmp_path) / f"bad{i}.md"
        await Path(fpath).write_text("""---\ntags: []\n---\n""")

    # run without specifying limit (default 5)
    with pytest.raises(SystemExit) as exc_info:
        await validator.main([str(tmp_path)])
    assert exc_info.value.code == 2
    out = capsys.readouterr().out
    # the summary should report 6 problems in total
    assert "6 problem(s) found" in out
    # check that the output mentioned '5 of 6 occurrence(s)' and omission note
    assert "5/6 occurrence(s)" in out
    assert "more occurrence(s) not shown" in out

    # now run with an explicit limit of 0 (unlimited)
    with pytest.raises(SystemExit) as exc_info2:
        await validator.main([str(tmp_path), "--max-per-rule", "0"])
    assert exc_info2.value.code == 2
    out2 = capsys.readouterr().out
    # should list all 6 occurrences and not mention truncation
    assert "6 occurrence(s)" in out2
    assert "not shown" not in out2


@pytest.mark.anyio
async def test_check_entrypoint(
    tmp_path: PathLike[str], monkeypatch: pytest.MonkeyPatch
):
    """The `check` CLI wrapper should mirror validator.main behavior."""
    # ensure the thin wrapper around validator.main behaves identically

    _path = await make_temp_markdown(tmp_path, "---\naliases: []\ntags: []\n---\n")

    previous_argv = sys.argv[:]  # keep original list contents
    try:
        sys.argv[:] = ["main", str(tmp_path)]
        with pytest.raises(SystemExit) as exc_info:
            await main.main()
        assert exc_info.value.code == 2

        # verify that passing a markdown file directly also works
        sys.argv[:] = ["main", str(_path)]
        with pytest.raises(SystemExit) as exc_info2:
            await main.main()
        assert exc_info2.value.code == 2
    finally:
        sys.argv[:] = previous_argv


@pytest.mark.anyio
async def test_walk_and_check_single_file(tmp_path: PathLike[str]):
    """Providing a markdown file path should exercise only that file."""
    bad = await make_temp_markdown(tmp_path, "---\ntags: []\n---\n")
    # directory root would find bad but test single file explicitly
    res = await walk_and_check([bad])
    assert any(p == bad for p, _ in res.errors())


@pytest.mark.anyio
async def test_suppression_on_heading_ignore_line(tmp_path: PathLike[str]):
    """ignore-line on a heading line should trigger suppression-on-heading warning."""
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "## Some heading <!-- check: ignore-line[unit_outside_math]: because -->\n"
    )
    file = Path(tmp_path) / "heading_line.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert any(
        m.rule_id == "suppression-on-heading" and m.severity.name == "WARNING"
        for m in msgs
    ), f"expected suppression-on-heading warning, got {[m.rule_id for m in msgs]}"
    # the suppression should still work for the actual rule
    assert not any(m.rule_id == "unit_outside_math" for m in msgs)


@pytest.mark.anyio
async def test_suppression_not_on_heading(tmp_path: PathLike[str]):
    """Suppression on a normal (non-heading) line should NOT trigger suppression-on-heading."""
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "Some ordinary text <!-- check: ignore-line[unit_outside_math]: because -->\n"
        "More text $I=5$ A\n"
    )
    file = Path(tmp_path) / "non_heading.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert not any(m.rule_id == "suppression-on-heading" for m in msgs), msgs


@pytest.mark.anyio
async def test_suppression_not_on_heading_next_line(tmp_path: PathLike[str]):
    """ignore-next-line on a normal line before a heading should NOT trigger suppression-on-heading."""
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "<!-- check: ignore-next-line[unit_outside_math]: because -->\n"
        "## Some heading\n"
    )
    file = Path(tmp_path) / "heading_next.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert not any(m.rule_id == "suppression-on-heading" for m in msgs), msgs
    # the suppression itself should be flagged as redundant (no unit_outside_math error exists)
    assert any(m.rule_id == "suppression-redundant" for m in msgs), msgs


@pytest.mark.anyio
async def test_suppression_not_on_heading_file_level(tmp_path: PathLike[str]):
    """ignore-file on a normal line before a heading should NOT trigger suppression-on-heading."""
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "<!-- check: ignore-file[unit_outside_math]: because -->\n"
        "## Some heading\n"
    )
    file = Path(tmp_path) / "heading_file.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert not any(m.rule_id == "suppression-on-heading" for m in msgs), msgs


@pytest.mark.anyio
async def test_suppression_on_heading_with_other_errors(tmp_path: PathLike[str]):
    """Heading line suppression should appear alongside other validation errors.

    The ``suppression-on-heading`` warning does not prevent other rules from
    firing; ``header_style`` and ``header_flashcard_presence`` should still
    trigger as usual.
    """
    text = (
        "---\naliases: [a]\ntags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        "## Overview <!-- check: ignore-line[unit_outside_math]: spacing accepted -->\n"
    )
    file = Path(tmp_path) / "heading_mixed.md"
    await file.write_text(text)

    msgs = list(await check_markdown_file(file))
    assert any(m.rule_id == "suppression-on-heading" for m in msgs), msgs
    # other rules still fire (unit_outside_math never fires here, so suppression is redundant)
    assert any(m.rule_id == "suppression-redundant" for m in msgs), msgs


# suppression regions and code fences ------------------------------------------


async def _write(tmp_path: PathLike[str], name: str, body: str) -> Path:
    """Write *body* under the frontmatter the other suppression tests use."""
    file = Path(tmp_path) / name
    await file.write_text(
        "---\naliases: [a]\n"
        "tags: [language/in/English, flashcard/active/special/academia/test]\n---\n"
        + body
    )
    return file


def _rule_ids(msgs: Sequence[ValidationMessage]) -> set[str]:
    """Return the rule IDs present in *msgs*."""
    return {m.rule_id for m in msgs}


@pytest.mark.anyio
async def test_suppression_inside_code_block_is_reported_and_not_honoured(
    tmp_path: PathLike[str],
):
    """A directive in a fence silences nothing, because nothing there is checked."""
    file = await _write(
        tmp_path,
        "in_fence.md",
        "```text\n"
        "<!-- check: ignore-line[unit_outside_math]: pasted from a shell transcript -->\n"
        "```\n"
        "More $I=5$ A\n",
    )

    msgs = list(await check_markdown_file(file))
    warned = [m for m in msgs if m.rule_id == "suppression-in-code-block"]
    assert len(warned) == 1, [m.rule_id for m in msgs]
    assert warned[0].severity.name == "WARNING"
    # The rule it claimed to cover still fires, which is the whole point.
    assert "unit_outside_math" in _rule_ids(msgs)


@pytest.mark.anyio
async def test_ignore_file_inside_code_block_is_not_honoured(
    tmp_path: PathLike[str],
):
    """An ignore-file buried in a fence must not silence the rest of the file."""
    file = await _write(
        tmp_path,
        "file_in_fence.md",
        "```text\n"
        "<!-- check: ignore-file[unit_outside_math]: pasted from a shell transcript -->\n"
        "```\n"
        "More $I=5$ A\n",
    )

    msgs = list(await check_markdown_file(file))
    assert "suppression-in-code-block" in _rule_ids(msgs)
    assert "unit_outside_math" in _rule_ids(msgs)


@pytest.mark.anyio
async def test_balanced_pair_suppresses_across_the_region(tmp_path: PathLike[str]):
    """A matching begin and end silence the lines between them."""
    file = await _write(
        tmp_path,
        "balanced.md",
        "<!-- check: ignore-begin[unit_outside_math]: log pasted verbatim -->\n"
        "More $I=5$ A\n"
        "<!-- check: ignore-end[unit_outside_math]: end of log -->\n",
    )

    msgs = list(await check_markdown_file(file))
    assert "unit_outside_math" not in _rule_ids(msgs)
    assert "suppression-pair-mismatch" not in _rule_ids(msgs)
    assert "suppression-redundant" not in _rule_ids(msgs)


@pytest.mark.anyio
async def test_ignore_end_without_a_begin_is_reported(tmp_path: PathLike[str]):
    """Closing a region that was never opened is a mismatch."""
    file = await _write(
        tmp_path,
        "unmatched_close.md",
        "<!-- check: ignore-end[unit_outside_math]: stray closer -->\n",
    )

    msgs = list(await check_markdown_file(file))
    bad = [m for m in msgs if m.rule_id == "suppression-pair-mismatch"]
    assert len(bad) == 1, [m.rule_id for m in msgs]
    assert bad[0].line == 5


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("closer", "label"),
    [
        ("<!-- check: ignore-end[no_smart_single_quotes]: dropped one -->", "subset"),
        (
            "<!-- check: ignore-end[unit_outside_math, no_smart_single_quotes]: added one -->",
            "superset",
        ),
    ],
)
async def test_ignore_end_must_name_the_opener_rules(
    tmp_path: PathLike[str], closer: str, label: str
):
    """A closer naming a different set of rules is an error either way round.

    Union and intersection are both refused. Each would silence a rule the
    author never agreed to at that end, and neither would say so.
    """
    file = await _write(
        tmp_path,
        f"mismatch_{label}.md",
        "<!-- check: ignore-begin[unit_outside_math]: log pasted verbatim -->\n"
        "More $I=5$ A\n"
        f"{closer}\n",
    )

    msgs = list(await check_markdown_file(file))
    bad = [m for m in msgs if m.rule_id == "suppression-pair-mismatch"]
    assert len(bad) == 1, [m.rule_id for m in msgs]
    assert bad[0].line == 7
    # Nothing is suppressed when the two ends disagree.
    assert "unit_outside_math" in _rule_ids(msgs)


@pytest.mark.anyio
async def test_unclosed_begin_is_reported_on_the_opener_line(
    tmp_path: PathLike[str],
):
    """An opener with no closer is reported where the author has to edit."""
    file = await _write(
        tmp_path,
        "unclosed.md",
        "<!-- check: ignore-begin[unit_outside_math]: log pasted verbatim -->\n"
        "More $I=5$ A\n",
    )

    msgs = list(await check_markdown_file(file))
    bad = [m for m in msgs if m.rule_id == "suppression-pair-mismatch"]
    assert len(bad) == 1, [m.rule_id for m in msgs]
    assert bad[0].line == 5
    assert "never closed" in bad[0].msg


@pytest.mark.anyio
async def test_nested_begin_reports_nested_and_not_mismatch(
    tmp_path: PathLike[str],
):
    """A second opener is a nesting error under its own rule ID.

    It gets its own ID because the repair differs: amend a rule list, or
    delete a directive.
    """
    file = await _write(
        tmp_path,
        "nested.md",
        "<!-- check: ignore-begin[unit_outside_math]: log pasted verbatim -->\n"
        "<!-- check: ignore-begin[unit_outside_math]: second attempt -->\n"
        "More $I=5$ A\n"
        "<!-- check: ignore-end[unit_outside_math]: end of log -->\n",
    )

    msgs = list(await check_markdown_file(file))
    nested = [m for m in msgs if m.rule_id == "suppression-region-nested"]
    assert len(nested) == 1, [m.rule_id for m in msgs]
    assert nested[0].line == 6
    assert "5" in nested[0].msg, "the message should name the line it collided with"
    assert "suppression-pair-mismatch" not in _rule_ids(msgs)


@pytest.mark.anyio
async def test_nested_begin_leaves_the_outer_region_working(
    tmp_path: PathLike[str],
):
    """The outer region survives a nested opener, so no pair error follows it.

    Had the nested opener been registered, the outer region would have been
    hidden and the closer would have had nothing to close, reporting one
    mistake as two.
    """
    file = await _write(
        tmp_path,
        "nested_outer.md",
        "<!-- check: ignore-begin[unit_outside_math]: log pasted verbatim -->\n"
        "<!-- check: ignore-begin[unit_outside_math]: second attempt -->\n"
        "More $I=5$ A\n"
        "<!-- check: ignore-end[unit_outside_math]: end of log -->\n",
    )

    msgs = list(await check_markdown_file(file))
    assert "suppression-region-nested" in _rule_ids(msgs)
    assert "suppression-pair-mismatch" not in _rule_ids(msgs)
    assert "unit_outside_math" not in _rule_ids(msgs)


@pytest.mark.anyio
async def test_region_silences_only_the_rules_its_opener_named(
    tmp_path: PathLike[str],
):
    """A rule the opener never named is left alone inside the region."""
    file = await _write(
        tmp_path,
        "wrong_rule.md",
        "<!-- check: ignore-begin[unit_outside_math]: log pasted verbatim -->\n"
        "It\u2019s a variable.\n"
        "<!-- check: ignore-end[unit_outside_math]: end of log -->\n",
    )

    msgs = list(await check_markdown_file(file))
    assert "no_smart_single_quotes" in _rule_ids(msgs)


@pytest.mark.anyio
async def test_a_region_does_not_spare_a_stale_single_line_of_the_same_rule(
    tmp_path: PathLike[str],
):
    """A stale one-liner is judged even when a region elsewhere covers its rule.

    Skipping by rule ID rather than by covered line would hide this one, and
    the hidden case is exactly the one a region introduces.
    """
    file = await _write(
        tmp_path,
        "region_and_stale_line.md",
        "<!-- check: ignore-line[no_smart_single_quotes]: stale, covers nothing -->\n"
        "Nothing curly below this line.\n"
        "\n"
        "<!-- check: ignore-begin[no_smart_single_quotes]: covers the log below -->\n"
        "It\u2019s a variable.\n"
        "<!-- check: ignore-end[no_smart_single_quotes]: covers the log above -->\n",
    )

    msgs = list(await check_markdown_file(file))
    redundant = [m for m in msgs if m.rule_id == "suppression-redundant"]
    assert len(redundant) == 1, [(m.line, m.msg) for m in redundant]
    # The report belongs to the stale one-liner, not to the working region.
    assert redundant[0].msg.startswith("suppression for rule")
    assert "region" not in redundant[0].msg


@pytest.mark.anyio
async def test_a_working_region_is_judged_once_across_its_span(
    tmp_path: PathLike[str],
):
    """A region that silences something raises no redundancy report."""
    file = await _write(
        tmp_path,
        "working_region.md",
        "<!-- check: ignore-begin[no_smart_single_quotes]: covers the log below -->\n"
        "It\u2019s a variable.\n"
        "<!-- check: ignore-end[no_smart_single_quotes]: covers the log above -->\n",
    )

    msgs = list(await check_markdown_file(file))
    assert "suppression-redundant" not in _rule_ids(msgs)


@pytest.mark.anyio
async def test_region_opener_may_sit_on_a_heading(tmp_path: PathLike[str]):
    """A region covering a heading is what the pair is for, so no warning."""
    file = await _write(
        tmp_path,
        "region_on_heading.md",
        "<!-- check: ignore-begin[unit_outside_math]: heading and its table -->\n"
        "## overview\n"
        "<!-- check: ignore-end[unit_outside_math]: end of table -->\n",
    )

    msgs = list(await check_markdown_file(file))
    assert "suppression-on-heading" not in _rule_ids(msgs)


@pytest.mark.anyio
async def test_region_requires_a_rationale(tmp_path: PathLike[str]):
    """Both ends of a region are held to the same bar as a line directive."""
    file = await _write(
        tmp_path,
        "region_no_reason.md",
        "<!-- check: ignore-begin[unit_outside_math]: -->\n"
        "More $I=5$ A\n"
        "<!-- check: ignore-end[unit_outside_math]: -->\n",
    )

    msgs = list(await check_markdown_file(file))
    assert sum(1 for m in msgs if m.rule_id == "suppression-missing-rationale") == 2
