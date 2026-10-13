"""Test the trailing-newline guarantee in the SOSC 1960 figure generator."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

GENERATOR = (
    Path(__file__).parents[6]
    / "special/academia/HKUST/SOSC 1960/attachments/generate_figures.py"
)


def _load() -> ModuleType:
    """Import the generator by path; it is a script, not an importable package."""
    spec = importlib.util.spec_from_file_location("sosc1960_figures", GENERATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {GENERATOR}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_generator_is_where_the_tree_expects_it() -> None:
    """Guard the path arithmetic in ``_load``, which is easy to get wrong."""
    assert GENERATOR.is_file(), f"expected the generator at {GENERATOR}"
    assert _load().__file__ == str(GENERATOR)


def test_normalise_adds_the_missing_newline() -> None:
    """A drawing with no trailing newline gets exactly one."""
    normalise = _load()._normalise_trailing_newline

    assert normalise("<svg/>") == "<svg/>\n"


def test_normalise_leaves_one_newline_alone() -> None:
    """A drawing that is already correct is returned unchanged."""
    normalise = _load()._normalise_trailing_newline

    assert normalise("<svg/>\n") == "<svg/>\n"


def test_normalise_collapses_several_newlines() -> None:
    """A blank tail of any length comes down to one newline."""
    normalise = _load()._normalise_trailing_newline

    assert normalise("<svg/>\n\n") == "<svg/>\n"
    assert normalise("<svg/>\n\n\n\n") == "<svg/>\n"
    assert normalise("<svg/>\r\n\r\n") == "<svg/>\n"


def test_normalise_drops_whitespace_after_the_last_newline() -> None:
    """Whitespace sitting on the lines after the last newline goes with them."""
    normalise = _load()._normalise_trailing_newline

    assert normalise("<svg/>\n  \n\t\n") == "<svg/>\n"


def test_normalise_leaves_the_body_alone() -> None:
    """Only the tail is rewritten, so newlines inside the drawing survive."""
    normalise = _load()._normalise_trailing_newline

    svg = "<svg>\n  <rect/>\n  <rect/>\n</svg>\n\n\n"
    assert normalise(svg) == "<svg>\n  <rect/>\n  <rect/>\n</svg>\n"


def test_main_normalises_what_it_writes(tmp_path: Path) -> None:
    """Every figure written through ``main`` ends in exactly one newline.

    The generator is pointed at a temp directory so the committed figures are
    left alone.
    """
    module = _load()

    module.main(["--outdir", str(tmp_path)])

    written = sorted(tmp_path.glob("*.svg"))
    assert written, "main() wrote no figures"
    for path in written:
        data = path.read_bytes()
        assert data.endswith(b"</svg>\n"), path
        assert not data.endswith(b"</svg>\n\n"), path
