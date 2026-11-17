#!/usr/bin/env python
# /// script
# dependencies = [
#   "matplotlib>=3.9.0",
#   "schemdraw[matplotlib,svgmath]==0.22",
# ]
# requires-python = ">=3.13.0"
# ///
"""Generate the SVG drawing that defines the loading-effect hookup.

A drawing is part of a definition: the two dividers, the nodes A, B, C, and
the instrument drawn as an input resistance Rin across the measured branch
fix what "connecting the instrument to node B" means. Prose cannot state the
hookup without the picture, so the drawing is attached to the lab note and
this script is its single source. Wikimedia Commons carries no figure of this
lab-defined construction; it is redrawn here at the user's direction from the
definition the session material gives.

The output is written beside this script. Everything is placed by schemdraw:
the circuit is chained in drawing order, the bottom rail closes back to the
source's corner on named anchors, and the dashed instrument box is computed
around the input resistance by EncircleBox. Running the module without
without arguments generates the drawing in place; the optional ``outdir``
parameter exists only for testing. The saved file is forced to end with
exactly one newline.
"""

import argparse
from contextlib import contextmanager
from os import environ, fspath
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import schemdraw.elements as elm
from schemdraw import Drawing

# matplotlib stamps every SVG with the current time; pinning the epoch makes a
# regenerated file byte-identical to the committed one.
environ.setdefault("SOURCE_DATE_EPOCH", "0")
# Pin the SVG element-id salt so a regenerated file is byte-identical to the
# committed one (matplotlib salts element ids with a fresh uuid4 per process).
matplotlib.rcParams["svg.hashsalt"] = "information.academia-ingest"


@contextmanager
def drawing_context():
    """Yield a schemdraw Drawing and close its matplotlib figure on exit.

    Use: ``with drawing_context() as d: ... d.save(...)``
    """
    d = Drawing()
    try:
        yield d
    finally:
        backend_fig = getattr(d, "fig", None)
        if backend_fig is not None:
            mpl_fig = getattr(backend_fig, "fig", backend_fig)
            plt.close(mpl_fig)


def _finalize(path: Path) -> None:
    """Force the saved SVG to end with exactly one newline."""
    data = path.read_bytes().rstrip(b"\n") + b"\n"
    path.write_bytes(data)


def generate_loading_effect_circuit(output: Path) -> None:
    """Two dividers fed by one source, with the instrument drawn as Rin.

    The first divider R1-R2 carries node A, the second R3-R4 node B with R3
    above B and R4 below it, and the instrument connects at node B: its
    input resistance Rin appears between B and the bottom rail, inside a
    dashed box that marks it as the instrument rather than a circuit
    element. The bottom rail closes from Rin's foot back to the source's
    grounded corner, so no branch floats.
    """
    with drawing_context() as d:
        # loc="left" on a two-terminal element is element-local: schemdraw
        # rotates it with the element, and on a vertical element it lands at
        # the element's end. loc="top" is what sits on the screen-left of a
        # vertical element, so the value labels use it.
        source = elm.SourceV().up().label("$V_1$", loc="top")
        d += source
        d += elm.Dot().at(source.end).label("$C$", loc="top")
        rail = elm.Line().right()
        d += rail
        d += elm.Resistor().down().label("$R_1$", loc="top")
        d += elm.Dot().label("$A$", loc="left")
        d += elm.Resistor().down().label("$R_2$", loc="top")
        d += elm.Line().right()
        d += elm.Resistor().up().label("$R_4$", loc="top")
        bdot = elm.Dot().label("$B$", loc="left")
        d += bdot
        d += elm.Resistor().up().label("$R_3$", loc="top")
        d += elm.Line().tox(rail.end.x)
        wire = elm.Line().at(bdot.end).right()
        d += wire
        rin = elm.Resistor().at(wire.end).down().label("$R_{in}$", loc="top")
        d += rin
        d += elm.Line().left()
        drop = elm.Line().at(source.start).toy(rin.end.y)
        d += drop
        d += elm.Ground().at(drop.end)
        d += elm.Line().right()
        d += (
            # The box takes Rin's own label in: drawing it around the resistor
            # body alone leaves the box's left edge cutting through Rin.
            elm.EncircleBox(
                [rin],
                padx=0.4,
                pady=0.4,
                cornerradius=0,
                includelabels=True,
                ls="dashed",
            )
            .label("DMM or oscilloscope", loc="top")
        )
        d.save(fspath(output))
    _finalize(output)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate the ELEC 2400 lab 1(b) loading-effect drawing (SVG)"
        )
    )
    parser.add_argument(
        "outdir",
        nargs="?",
        help=(
            "output directory for generated SVGs; defaults to this script's "
            "attachments folder"
        ),
    )
    args = parser.parse_args(argv)

    outdir = Path(args.outdir) if args.outdir else Path(__file__).parent
    outdir.mkdir(parents=True, exist_ok=True)
    generate_loading_effect_circuit(outdir / "loading_effect_circuit.svg")
    return 0


def __main__() -> None:
    """Entry point for running the script directly."""
    raise SystemExit(main())


if __name__ == "__main__":
    __main__()
