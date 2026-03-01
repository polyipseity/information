"""Tests for validator module behaviour related to registries."""

from os import PathLike

import check
import pytest
from anyio import Path
from check_mods import validator
from check_mods.registry import RuleRegistry
from check_mods.rules import RULE_REGISTRY as RULES_REGISTRY
from check_mods.validator import RULE_REGISTRY as VALIDATOR_REGISTRY
from check_mods.validator import check_markdown_file, walk_and_check

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


@pytest.mark.asyncio
async def test_check_markdown_file_missing_frontmatter(tmp_path: PathLike[str]):
    """Validator should report missing frontmatter correctly."""
    p = await make_temp_markdown(tmp_path, "no frontmatter here")
    msgs = await check_markdown_file(p)
    assert msgs and msgs[0].msg.startswith("missing YAML frontmatter")


@pytest.mark.asyncio
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
        rc = await validator.main([str(tmp_path)])
        assert rc == 3
    finally:
        VALIDATOR_REGISTRY._rules.pop("not_matching_name", None)


@pytest.mark.asyncio
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


@pytest.mark.asyncio
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
    bad = await make_temp_markdown(tmp_path / "sub", "---\ntags: []\n---\n")
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
    rc = await validator.main([str(tmp_path), "--json"])
    assert rc == 2
    out = capsys.readouterr().out
    # output should now use a single 'issues' key containing messages
    assert "issues" in out
    assert "missing" in out
    # ensure severity properties appear
    assert '"severity": "warning"' in out or '"severity": "error"' in out


@pytest.mark.asyncio
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
    _file_err = await make_temp_markdown(tmp_path / "err.md", "---\ntags: []\n---\n")
    rc = await validator.main([str(tmp_path)])
    assert rc == 2
    out = capsys.readouterr().out.lower()
    assert "warning" in out
    assert "error" in out
    # the colored prefix should show the rule id with severity
    assert "[warning/" in out or "[error/" in out


@pytest.mark.asyncio
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
        fpath = tmp_path / f"bad{i}.md"
        await Path(fpath).write_text("""---\ntags: []\n---\n""")

    # run without specifying limit (default 5)
    rc = await validator.main([str(tmp_path)])
    assert rc == 2
    out = capsys.readouterr().out
    # the summary should report 6 problems in total
    assert "6 problem(s) found" in out
    # check that the output mentioned '5 of 6 occurrence(s)' and omission note
    assert "5/6 occurrence(s)" in out
    assert "more occurrence(s) not shown" in out

    # now run with an explicit limit of 0 (unlimited)
    rc2 = await validator.main([str(tmp_path), "--max-per-rule", "0"])
    assert rc2 == 2
    out2 = capsys.readouterr().out
    # should list all 6 occurrences and not mention truncation
    assert "6 occurrence(s)" in out2
    assert "not shown" not in out2


@pytest.mark.asyncio
async def test_check_entrypoint(tmp_path: PathLike[str]):
    """The `check` CLI wrapper should mirror validator.main behavior."""
    # ensure the thin wrapper around validator.main behaves identically

    _path = await make_temp_markdown(tmp_path, "---\naliases: []\ntags: []\n---\n")
    rc = await check.main([str(tmp_path)])
    assert rc == 2

    # verify that passing a markdown file directly also works
    rc2 = await check.main([str(_path)])
    assert rc2 == 2


@pytest.mark.asyncio
async def test_walk_and_check_single_file(tmp_path: PathLike[str]):
    """Providing a markdown file path should exercise only that file."""
    bad = await make_temp_markdown(tmp_path, "---\ntags: []\n---\n")
    # directory root would find bad but test single file explicitly
    res = await walk_and_check([bad])
    assert any(p == bad for p, _ in res.errors())
