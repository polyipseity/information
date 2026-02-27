"""Unit tests for data models in academic-notes.

Covers Frontmatter defaults, Severity enum, and ValidationResult helpers.
"""

from anyio import Path
from check_mods.models import (
    Frontmatter,
    Severity,
    ValidationMessage,
    ValidationResult,
)

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
