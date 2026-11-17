#!/usr/bin/env python
# /// script
# dependencies = [
#   "matplotlib>=3.9.0",
#   "numpy>=1.26",
#   "schemdraw[matplotlib,svgmath]==0.22",
# ]
# requires-python = ">=3.13.0"
# ///
"""Generate the SVG drawings that define the phase-measurement setup.

A drawing is part of a definition: the series RC hookup fixes where the two
oscilloscope channels connect, and the Lissajous ellipse fixes which two
distances the relation sin(theta) = a/b is read from. Prose cannot state
either without the picture, so the drawings are attached to the lab note and
this script is their single source. Wikimedia Commons carries no figure of
these two lab-defined constructions; they are redrawn here at the user's
direction from the definitions the session material gives.

Outputs are written beside this script. The circuit is placed by schemdraw;
the ellipse is placed by matplotlib. Running the module without arguments
generates the drawings in place; the optional ``outdir`` parameter exists only
for testing. Every saved file is forced to end with exactly one newline.
"""

import argparse
from contextlib import contextmanager
from os import environ, fspath
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
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


def generate_phase_measurement_circuit(output: Path) -> None:
    """Series RC hookup: source, capacitor, node A, resistor, ground.

    Node B is the wire between the source and the capacitor, node A the wire
    between the capacitor and the resistor, so the drawing fixes where each
    oscilloscope channel connects and which element sits between the nodes.
    """
    with drawing_context() as d:
        source = elm.SourceSin().up().label("$V_1(t)$", loc="top")
        d += source
        rail = elm.Line().right().at(source.end)
        d += rail
        # Node B is the wire from the source to the capacitor; a labelled dot
        # at the corner marks it, as in the definition the material gives.
        d += elm.Dot().label("$B$", loc="top")
        # loc="left" on a two-terminal element is element-local: schemdraw
        # rotates it with the element, and on a vertical element it lands at
        # the element's end. loc="top" is what sits on the screen-left of a
        # vertical element, so the value labels use it.
        d += elm.Capacitor().down().label("$C$", loc="top")
        d += elm.Dot().label("$A$", loc="right")
        d += elm.Resistor().down().label("$R$", loc="top")
        bottom = elm.Line().left()
        d += bottom
        # The bottom lead and the left branch meet at the bottom-left node,
        # which a dot marks as the junction it is; the ground hangs on its
        # own short lead off that node, so the symbol ends a wire instead of
        # sitting in the middle of one.
        d += elm.Dot().at(bottom.end)
        ground_lead = elm.Line().at(bottom.end).down().length(0.5)
        d += ground_lead
        d += elm.Ground().at(ground_lead.end)
        d += elm.Line().at(bottom.end).toy(source.start.y)
        d.save(fspath(output))
    _finalize(output)


def generate_lissajous_phase_ellipse(output: Path) -> None:
    """Lissajous ellipse: a the intercept on the vertical axis, b the extent.

    The channel-A voltage sets the horizontal coordinate and the channel-B
    voltage the vertical one, so a phase difference traces an ellipse. The
    height a is where the ellipse crosses the vertical axis and the height b
    its greatest distance above the horizontal axis, giving sin(theta) = a/b.
    """
    # ellipse tilted at 45 degrees with semi-axes a0 (major) and b0 (minor):
    # its vertical intercept sits at 2*a0*b0/hypot(a0, b0) and its greatest
    # height at hypot(a0, b0), both in the rotated frame, and the 2**0.5
    # that turns that frame into x and y shrinks each by the same factor
    a0, b0 = 1.25, 0.4
    span = float(np.hypot(a0, b0))
    a_height = 2 * a0 * b0 / (span * 2**0.5)
    b_height = span / 2**0.5

    t = np.linspace(0, 2 * np.pi, 400)
    x = (a0 * np.cos(t) - b0 * np.sin(t)) / 2**0.5
    y = (a0 * np.cos(t) + b0 * np.sin(t)) / 2**0.5

    fig, ax = plt.subplots(figsize=(3.2, 2.6))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.plot(x, y, color="black", lw=1.4)
    ax.plot([-1.6, 1.6], [0, 0], color="black", lw=1.2)
    ax.plot([0, 0], [-1.45, 1.45], color="black", lw=1.2)

    # a: horizontal guide at the ellipse's crossing of the vertical axis,
    # with the measuring arrow beside the axis
    ax.plot([-0.9, 0], [a_height, a_height], color="black", lw=0.8)
    ax.annotate(
        "",
        xy=(-0.7, 0),
        xytext=(-0.7, a_height),
        arrowprops=dict(arrowstyle="<->", color="black", lw=1.1),
    )
    ax.text(-0.85, a_height / 2, "$a$", ha="right", va="center", fontsize=13)

    # b: horizontal guide at the ellipse's greatest height, with the arrow
    # outside the ellipse
    ax.plot([0, 1.35], [b_height, b_height], color="black", lw=0.8)
    ax.annotate(
        "",
        xy=(1.3, 0),
        xytext=(1.3, b_height),
        arrowprops=dict(arrowstyle="<->", color="black", lw=1.1),
    )
    ax.text(1.45, b_height / 2, "$b$", ha="left", va="center", fontsize=13)

    ax.set_xlim(-1.7, 1.75)
    ax.set_ylim(-1.5, 1.5)
    fig.savefig(fspath(output), transparent=False, bbox_inches="tight")
    plt.close(fig)
    _finalize(output)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate the ELEC 2400 lab 1(a) phase-measurement drawings (SVG)"
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
    generate_phase_measurement_circuit(outdir / "phase_measurement_circuit.svg")
    generate_lissajous_phase_ellipse(outdir / "lissajous_phase_ellipse.svg")
    return 0


def __main__() -> None:
    """Entry point for running the script directly."""
    raise SystemExit(main())


if __name__ == "__main__":
    __main__()
