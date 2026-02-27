"""Tests for validator module behaviour related to registries."""

from os import PathLike

import check
import pytest
from anyio import Path
from check_mods import validator
from check_mods.rules import RULE_REGISTRY as rules_registry
from check_mods.validator import RULE_REGISTRY as validator_registry
from check_mods.validator import check_markdown_file, walk_and_check

__all__ = ()


def test_validator_registry_contains_rules():
    """The registry built by the validator should include rules from rules.py."""
    ids = [rid for rid, _ in validator_registry.items()]
    assert "metadata_aliases_present" in ids
    # ensure registry is a separate object from the rules module's own
    assert validator_registry is not rules_registry


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

    validator_registry.register(id="bad")(bad_rule)
    try:
        msgs = await check_markdown_file(p)
        assert any("exception in rule bad_rule" in m.msg for m in msgs)
    finally:
        # remove the bad rule so other tests are unaffected
        validator_registry._rules.pop("bad", None)


@pytest.mark.asyncio
async def test_walk_and_check_and_main_json(tmp_path: PathLike[str], capsys):
    """walk_and_check should find errors and main() should output JSON."""
    # create two files: one valid, one with missing aliases
    _good = await make_temp_markdown(
        tmp_path, "---\naliases: [a]\ntags: [language/in/English]\n---\n"
    )
    bad = await make_temp_markdown(tmp_path / "sub", "---\ntags: []\n---\n")
    # run walk_and_check on directory
    res = await walk_and_check([Path(tmp_path)])
    # should record errors for bad file
    assert any(p == bad for p, _ in res.errors())

    # test main output with --json
    rc = await validator.main([str(tmp_path), "--json"])
    assert rc == 2
    out = capsys.readouterr().out
    assert "errors" in out and "missing" in out


@pytest.mark.asyncio
async def test_check_entrypoint(tmp_path: PathLike[str]):
    """The `check` CLI wrapper should mirror validator.main behavior."""
    # ensure the thin wrapper around validator.main behaves identically

    _path = await make_temp_markdown(tmp_path, "---\naliases: []\ntags: []\n---\n")
    rc = await check.main([str(tmp_path)])
    assert rc == 2
