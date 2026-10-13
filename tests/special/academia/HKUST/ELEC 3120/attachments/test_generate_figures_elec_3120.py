"""Test the trailing-newline guarantee in the ELEC 3120 figure generator."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

GENERATOR = (
    Path(__file__).parents[6]
    / "special/academia/HKUST/ELEC 3120/attachments/generate_figures.py"
)


def _load() -> ModuleType:
    """Import the generator by path; it is a script, not an importable package."""
    spec = importlib.util.spec_from_file_location("elec3120_figures", GENERATOR)
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


def test_write_svg_fixes_a_file_savefig_left_dirty(tmp_path: Path) -> None:
    """The post-savefig pass rewrites a file the way matplotlib left it."""
    module = _load()
    target = tmp_path / "figure.svg"
    target.write_text("<svg>\n  <rect/>\n</svg>\n\n\n", encoding="utf-8")

    module._write_svg(target)

    data = target.read_bytes()
    assert data == b"<svg>\n  <rect/>\n</svg>\n"
    assert data.endswith(b"</svg>\n")
    assert not data.endswith(b"</svg>\n\n")


def test_write_svg_leaves_a_clean_file_alone(tmp_path: Path) -> None:
    """A file that already ends correctly comes back byte-identical."""
    module = _load()
    target = tmp_path / "figure.svg"
    original = b"<svg>\n  <rect/>\n</svg>\n"
    target.write_bytes(original)

    module._write_svg(target)

    assert target.read_bytes() == original


def test_write_svg_never_touches_the_committed_figures(tmp_path: Path) -> None:
    """The helper is given its path, so it only ever rewrites the file it is handed.

    matplotlib writes beside this script, so a mistake here would rewrite a
    committed figure. Checking the committed files still end correctly guards
    that without drawing anything.
    """
    module = _load()
    before = {path.name: path.read_bytes() for path in GENERATOR.parent.glob("*.svg")}
    assert before, "expected the committed ELEC 3120 figures to be present"

    target = tmp_path / "figure.svg"
    target.write_text("<svg/>\n\n", encoding="utf-8")
    module._write_svg(target)

    after = {path.name: path.read_bytes() for path in GENERATOR.parent.glob("*.svg")}
    assert after == before
    for data in after.values():
        assert data.endswith(b"\n") and not data.endswith(b"\n\n")
