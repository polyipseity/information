#!/usr/bin/env python
# /// script
# dependencies = [
#   "anyio>=3.6.0",
#   "asyncer>=0.0.17",
#   "matplotlib>=3.9.0",
#   "schemdraw[matplotlib,svgmath]>=0.22",
#   "uvloop>=0.22.0; platform_system != 'Windows'",
#   "winloop>=0.5.0; platform_system == 'Windows'",
# ]
# requires-python = ">=3.13.0"
# ///
"""Generate the SVG circuit drawings for the ELEC 2400 notes.

A drawing is part of a definition: recognising a source, a resistor, or a
ground on a diagram, and knowing which way a reference direction runs, means
knowing what the drawing looks like. The notes therefore embed the drawings
beside the prose that defines them, and this script is their single source.

The collection covers the drawings introduced by the tutorials and lectures:

* the resistor symbol (a zigzag line labelled ``R``);
* the ground symbol (stacked strokes at a reference node);
* the voltmeter with its red positive and black negative probe;
* the three drawings used for one and the same ideal voltage source, each in
  its own file (battery, circle, rectangle) with its value label;
* the reference direction of a current through a resistor, drawn both with and
  against the resistor voltage marks;
* the marks alone, with no value written; and
* the power reference of an element, drawn with the current arrow leaving and
  with the current arrow entering the terminal marked ``+``, which is what
  decides whether the power is written ``-VI`` or ``+VI``.

Every drawing is placed by schemdraw: elements are chained in the drawing
order, labels sit on the element they belong to, and leads attach to named
anchors. No file carries a hand-picked coordinate, so a drawing stays correct
when an element is added, removed, or reordered. A drawing that exists in two
forms is two files laid out beside each other by the Markdown that embeds
them, because schemdraw has no way to place a second figure without
coordinates.

Outputs are written as SVG files into the ``attachments`` directory next to the
script so they can be committed to version control. Running the module without
arguments generates the diagrams in place; the optional ``outdir`` parameter
exists only for testing.

The generator is intentionally minimal and deterministic. There are no unit
tests by design; this comment documents that fact for future maintainers.

Each diagram is built inside a :func:`drawing_context` context manager so the
matplotlib figure is closed after saving, avoiding a RuntimeWarning when
generating many figures in one run. Diagrams are generated concurrently via
:mod:`multiprocessing` so each runs in its own process (matplotlib is not
thread-safe).
"""

import argparse
from collections.abc import Callable
from contextlib import contextmanager
from multiprocessing import Pool
from os import cpu_count, environ, fspath

import matplotlib
import matplotlib.pyplot as plt
import schemdraw.elements as elm
from anyio import Path
from asyncer import runnify
from schemdraw import Drawing

# Reproducible SVG output. matplotlib salts the element ids it generates with a
# fresh uuid4 per process and stamps every file with the current time, so
# redrawing an unchanged diagram still produces a diff. Pinning the salt and the
# timestamp makes a regenerated file byte-identical to the committed one.
#
# Both settings sit at module level, not inside main(): diagrams are drawn in
# multiprocessing Pool workers, which re-import this module under macOS spawn.
#
# schemdraw's Drawing.save() takes no ``metadata=`` argument, so the date cannot
# be dropped the way the plain-matplotlib generators drop it; it is pinned
# instead, leaving these files with a SOURCE_DATE_EPOCH stamp they would not
# otherwise carry. Changing the salt rewrites every SVG this script produces.
environ.setdefault("SOURCE_DATE_EPOCH", "0")
matplotlib.rcParams["svg.hashsalt"] = "information.academia-ingest"

# cap worker count to avoid overloading the machine (matplotlib is process-heavy)
_MAX_POOL_WORKERS = min(4, cpu_count() or 1)

# the course draws current reference arrows in red and marks the voltmeter's
# positive probe red, so the same colour carries the same meaning in the SVGs
_RED = "#e00000"

# the three source drawings sit side by side in a note, so they are kept to one
# height and read as a set; a longer element only stretches the leads
_SOURCE_LENGTH = 2


@contextmanager
def drawing_context():
    """Yield a schemdraw Drawing and close its matplotlib figure on exit.

    Avoids RuntimeWarning about too many figures when generating many diagrams.
    Use: ``with drawing_context() as d: ... d.save(...)``
    """
    d = Drawing()
    try:
        yield d
    finally:
        backend_fig = getattr(d, "fig", None)
        if backend_fig is not None:
            # schemdraw mpl backend wraps matplotlib Figure as backend_fig.fig
            mpl_fig = getattr(backend_fig, "fig", backend_fig)
            plt.close(mpl_fig)


def generate_symbol_resistor(output: Path) -> None:
    """Resistor symbol: the zigzag line the course draws, labelled ``R``."""
    with drawing_context() as d:
        d += elm.Resistor().right().label("$R$")
        d.save(fspath(output))


def generate_symbol_ground(output: Path) -> None:
    """Ground symbol: the reference node drawn as stacked horizontal strokes."""
    with drawing_context() as d:
        d += elm.Ground()
        d.save(fspath(output))


def generate_symbol_voltmeter(output: Path) -> None:
    """Voltmeter drawn as the course draws it: a box with a red `+` and a black `-` terminal.

    The red terminal reaches the node marked ``A`` and the black terminal the
    node marked ``B``, so the drawing carries both the shape of the meter and
    the colour rule for its terminals.
    """
    with drawing_context() as d:
        meter = elm.Ic(
            size=(2.5, 2),
            pins=[
                elm.IcPin(name="$+$", side="B", anchorname="plus"),
                elm.IcPin(name="$-$", side="B", anchorname="minus"),
            ],
        ).label("Voltmeter")
        d += meter
        d += elm.Dot(color=_RED).at(meter.plus).label("$A$", loc="bottom")
        d += elm.Dot().at(meter.minus).label("$B$", loc="bottom")
        d.save(fspath(output))


def generate_symbol_source_battery(output: Path) -> None:
    """A source drawn as a battery: two parallel lines, the longer one positive.

    Drawn downwards so the long line sits on top, and kept shorter than the
    default element so the two lines stay the subject of the drawing, as the
    course draws it.
    """
    with drawing_context() as d:
        d += elm.BatteryCell().down().length(_SOURCE_LENGTH).label("$5\\text{ V}$")
        d.save(fspath(output))


def generate_symbol_source_circle(output: Path) -> None:
    """A source drawn as a circle holding ``+`` and ``-``.

    Drawn upwards so the plus mark sits on top, with the value beside the
    circle, as the course draws it.
    """
    with drawing_context() as d:
        d += (
            elm.SourceV()
            .up()
            .length(_SOURCE_LENGTH)
            .label("$12\\text{ V}$", loc="bottom")
        )
        d.save(fspath(output))


def generate_symbol_source_rectangle(output: Path) -> None:
    """A source drawn as a rectangle holding the same two marks."""
    with drawing_context() as d:
        box = elm.Ic(
            size=(1.5, 1.5),
            pins=[
                elm.IcPin(name="$+$", side="T", anchorname="plus"),
                elm.IcPin(name="$-$", side="B", anchorname="minus"),
            ],
        ).label("$10\\text{ V}$", loc="right")
        d += box
        d.save(fspath(output))


def _generate_reference_direction(output: Path, label: str, reverse: bool) -> None:
    """One reference-direction drawing: marks above the resistor, arrow below it."""
    with drawing_context() as d:
        resistor = elm.Resistor().right().label(["$+$", "$V_1$", "$-$"], loc="top")
        d += resistor
        d += elm.CurrentLabel(top=False, reverse=reverse).at(resistor).label(label)
        d.save(fspath(output))


def generate_reference_direction_with(output: Path) -> None:
    """Current arrow drawn from the plus mark to the minus mark of the voltage."""
    _generate_reference_direction(output, "$I_1 = 2\\text{ A}$", False)


def generate_reference_direction_against(output: Path) -> None:
    """Current arrow drawn from the minus mark to the plus mark of the voltage."""
    _generate_reference_direction(output, "$I_2 = -2\\text{ A}$", True)


def generate_reference_marks(output: Path) -> None:
    """Reference marks alone: an element marked ``+`` and ``-`` with no value written.

    The marks fix only which terminal counts as positive, so the drawing
    carries no number and no current arrow. Drawn upwards so the plus mark sits
    at the top, with the upper node named ``A`` and the lower one ``B``, as the
    course draws it.
    """
    with drawing_context() as d:
        source = elm.SourceV().up()
        d += source
        d += elm.Dot().at(source.start).label("$B$", loc="right")
        d += elm.Dot().at(source.end).label("$A$", loc="right")
        d.save(fspath(output))


#: The current arrow runs along the upper lead, so the lead is drawn long enough
#: that the arrowhead and its label clear the ``+`` mark and the terminal dot,
#: and no longer than that: at 2.1 the arrowhead already crowds the dot, and at
#: 1.9 it touches it.
_POWER_LEAD_LENGTH = 2.3


def _generate_power_reference(output: Path, reverse: bool) -> None:
    """One power-reference drawing: where the current arrow sits against the ``+`` mark.

    The element is drawn upwards so its ``+`` mark sits at the top, and the
    current arrow is hung on the upper lead, next to that mark. With
    ``reverse=False`` the arrow runs from the ``+`` mark away from the element,
    so the current leaves the positive terminal; with ``reverse=True`` it runs
    back towards the mark, so the current enters the positive terminal. The two
    files differ only in that one direction, which is the whole of the
    convention they state.
    """
    with drawing_context() as d:
        d += elm.SourceV().up().label("$V_1$", loc="left")
        d += elm.Line().up().length(_POWER_LEAD_LENGTH)
        lead = d.elements[-1]
        d += elm.CurrentLabel(reverse=reverse).at(lead).label("$I_1$")
        d += elm.Dot().at(lead.end)
        d.save(fspath(output))


def generate_power_reference_current_out_of_plus(output: Path) -> None:
    """Current arrow leaving the terminal marked ``+``, so the power is ``-VI``."""
    _generate_power_reference(output, reverse=False)


def generate_power_reference_current_into_plus(output: Path) -> None:
    """Current arrow entering the terminal marked ``+``, so the power is ``+VI``."""
    _generate_power_reference(output, reverse=True)


def _run_generator(args: tuple[Callable[[Path], None], Path]) -> None:
    """Run a single generator (func, path) for multiprocessing Pool."""
    func, path = args
    func(path)


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate ELEC 2400 circuit diagrams (SVG)"
    )
    parser.add_argument(
        "outdir",
        nargs="?",
        help="output directory for generated SVGs; defaults to this script's attachments folder",
    )
    args = parser.parse_args()

    if args.outdir:
        outdir = Path(args.outdir)
    else:
        # default to the directory where the script resides (attachments)
        outdir = Path(__file__).parent
    await outdir.mkdir(parents=True, exist_ok=True)

    # Path paths for pickling in worker processes
    outdir_path = Path(fspath(outdir))
    generators: list[tuple[Callable[[Path], None], Path]] = [
        (generate_symbol_resistor, outdir_path / "symbol_resistor.svg"),
        (generate_symbol_ground, outdir_path / "symbol_ground.svg"),
        (generate_symbol_voltmeter, outdir_path / "symbol_voltmeter.svg"),
        (generate_symbol_source_battery, outdir_path / "symbol_source_battery.svg"),
        (generate_symbol_source_circle, outdir_path / "symbol_source_circle.svg"),
        (
            generate_symbol_source_rectangle,
            outdir_path / "symbol_source_rectangle.svg",
        ),
        (
            generate_reference_direction_with,
            outdir_path / "reference_direction_with.svg",
        ),
        (
            generate_reference_direction_against,
            outdir_path / "reference_direction_against.svg",
        ),
        (generate_reference_marks, outdir_path / "reference_marks.svg"),
        (
            generate_power_reference_current_out_of_plus,
            outdir_path / "power_reference_current_out_of_plus.svg",
        ),
        (
            generate_power_reference_current_into_plus,
            outdir_path / "power_reference_current_into_plus.svg",
        ),
    ]

    with Pool(processes=_MAX_POOL_WORKERS) as pool:
        pool.map(_run_generator, generators)


def __main__():
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
