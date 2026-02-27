"""Unit tests for data models in academic-notes.

Covers Frontmatter defaults, Severity enum, and ValidationResult helpers.
"""

from anyio import Path
from check_mods.models import (
    Frontmatter,
    PreviewEntry,
    Severity,
    StrList,
    ValidationMessage,
    ValidationResult,
)
from pydantic_yaml import parse_yaml_raw_as

__all__ = ()


def test_frontmatter_defaults():
    """Frontmatter model should default to empty lists for aliases/tags."""

    fm = Frontmatter()
    assert fm.aliases == []
    assert fm.tags == []


def test_validation_result():
    """ValidationResult should separate errors from warnings correctly."""

    vr = ValidationResult()
    msg = ValidationMessage("oops")
    vr.add(Path("/tmp/file.md"), msg)
    assert vr.errors() == [(Path("/tmp/file.md"), msg)]
    assert vr.warnings() == []
    msg2 = ValidationMessage("warn", severity=Severity.WARNING)
    vr.add(Path("/tmp/f2.md"), msg2)
    assert len(vr.messages) == 2
    assert vr.warnings() == [(Path("/tmp/f2.md"), msg2)]


def test_strlist_coercions():
    """StrList should cooperate with pydantic parsing, coercing various inputs."""

    # YAML null -> None should now coerce to empty list
    assert parse_yaml_raw_as(StrList, "null") == []
    assert parse_yaml_raw_as(StrList, "[]") == []
    assert parse_yaml_raw_as(StrList, "[1, 2]") == ["1", "2"]
    assert parse_yaml_raw_as(StrList, "'abc'") == ["abc"]
    # scalar value
    assert parse_yaml_raw_as(StrList, "42") == ["42"]


def test_preview_entry_to_dict():
    """PreviewEntry.to_dict() should include only present fields."""

    e = PreviewEntry(Path("/tmp/foo.md"), "excerpt")
    d = e.to_dict()
    # path formatting may use either backslashes (Windows) or forward slashes;
    # just ensure the basename is correct and excerpt is present
    assert d["path"].endswith("/foo.md") or d["path"].endswith("\\foo.md")
    assert d["excerpt"] == "excerpt"
    e.caret = "^^"
    e.line = 3
    e.col = 5
    d = e.to_dict()
    assert d["caret"] == "^^"
    assert d["line"] == 3
    assert d["col"] == 5
