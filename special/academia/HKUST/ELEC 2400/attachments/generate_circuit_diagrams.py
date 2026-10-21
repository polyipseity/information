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
  decides whether the power is written ``-VI`` or ``+VI``;
* the operational amplifier symbol, its circuit model inside the triangle, its
  differential-input transfer characteristic, and the negative-feedback loop;
* the practical voltage amplifier loading chain (source, amplifier, load);
* the unity-gain buffer amplifier;
* the inverting, non-inverting, summing, and difference amplifiers;
* the instrumentation amplifier with a differential output and its
  single-ended-output variant;
* the load-independent op-amp current source, the negative impedance
  converter, and the voltage-to-current converter built on it;
* the inverting amplifier with parallel feedback, the difference amplifier
  with its input mesh, the current-source design check in its failing and
  its improved form, and the two-op-amp circuit solved from an entry point;
* the parallel-plate capacitor, the capacitor and inductor symbols, the
  ideal transformer, and the AC source symbol;
* the phasor as a rotating vector, the complex plane with a number on it, the
  unit circle with the common exponentials, phasor addition, the impedance
  diagram, and the sinusoid with its RMS level.

Every circuit drawing is placed by schemdraw: elements are chained in the
drawing order, labels sit on the element they belong to, and leads attach to
named anchors, so a drawing stays correct when an element is added, removed,
or reordered. The exceptions name their own coordinates on purpose: the
transfer characteristic is a plot laid out from named level constants, the
feedback loop is a block diagram, and the two models whose components sit
inside a triangle or across dashed stage boxes (the op-amp circuit model and
the loading chain) place their parts against explicit points so the enclosing
shapes stay recognizable. A drawing that exists in two forms is two files
laid out beside each other by the Markdown that embeds them, because schemdraw
has no way to place a second figure without coordinates.

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
from math import cos, pi, sin
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
_ANNOT = "#c0392b"
_GREEN = "#1f6f1f"

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


def _op_amp_supplies(
    d: Drawing, op: elm.Opamp, *, flip: bool, label_side: str = "left"
) -> None:
    """Attach the supply leads of an operational amplifier.

    ``flip`` mirrors the default triangle: unflipped, ``vd`` sits on top and
    ``vs`` below; flipped, they exchange sides. The labels do not change: the
    upper lead is always ``V_dd`` and the lower one ``-V_ss``.

    ``label_side`` keeps both rail names on the left of their leads by
    default, and moves them to the right for the few figures whose left-hand
    side carries the wiring.
    """
    top_anchor, bottom_anchor = (op.vs, op.vd) if flip else (op.vd, op.vs)
    dx = -1.15 if label_side == "left" else 1.15
    d += elm.Line().at(top_anchor).up().length(0.9)
    d += elm.Label().at((top_anchor[0] + dx, top_anchor[1] + 1.05)).label("$V_{dd}$")
    d += elm.Line().at(bottom_anchor).down().length(0.9)
    d += (
        elm.Label()
        .at((bottom_anchor[0] + dx, bottom_anchor[1] - 1.05))
        .label("$-V_{ss}$")
    )


def generate_op_amp_symbol(output: Path) -> None:
    """Operational amplifier symbol with its two inputs and supply terminals.

    The course draws the non-inverting input (+) on top, so the triangle is
    flipped from schemdraw's default (which puts the inverting input there),
    and the gain ``A`` is written inside the triangle with the input names
    ``V+`` and ``V-`` beside their leads.
    """
    with drawing_context() as d:
        op = elm.Opamp().right().flip().anchor("center").label("$A$", loc="center")
        d += op
        d += elm.Line().at(op.in2).left().length(1.4).label("$V_+$", loc="top")
        d += elm.Line().at(op.in1).left().length(1.4).label("$V_-$", loc="bottom")
        d += elm.Line().at(op.out).right().length(1.4)
        _op_amp_supplies(d, op, flip=True)
        d.save(fspath(output))


def generate_op_amp_circuit_model(output: Path) -> None:
    """Circuit model of a practical op amp, drawn inside the triangle."""
    with drawing_context() as d:
        # The triangle is drawn from its corners so the model can sit inside it.
        top, bottom, tip = (0.0, 4.5), (0.0, -4.5), (14.0, 0.0)
        d += elm.Line().at(top).to(tip)
        d += elm.Line().at(tip).to(bottom)
        d += elm.Line().at(bottom).to(top)
        # input leads and the resistance between them; the course draws the
        # + input on top, names the inputs V+ and V-, and marks the input
        # voltage with + and - at the lead ends
        d += elm.Line().at((-2.2, 1.5)).to((0.0, 1.5)).label("$V_+$", loc="top")
        d += elm.Line().at((-2.2, -1.5)).to((0.0, -1.5)).label("$V_-$", loc="bottom")
        d += elm.Label().at((-2.3, 1.75)).label("$+$")
        d += elm.Label().at((-2.3, -1.95)).label("$-$")
        d += elm.Label().at((-1.55, 0.0)).label("$V_{in}$")
        d += elm.Line().at((0.0, 1.5)).to((1.5, 1.5))
        d += elm.Resistor().at((1.5, 1.5)).to((1.5, -1.5)).label("$R_i$", loc="left")
        d += elm.Line().at((1.5, -1.5)).to((0.0, -1.5))
        # controlled source, its ground, and the output resistance; the
        # diamond is drawn upward from its lower anchor, so it is placed from
        # the lead the ground hangs below rather than from the top lead
        source = elm.SourceControlledV().up().at((4.6, -0.9)).length(1.8)
        d += source
        d += elm.Label().at((6.5, 0.4)).label("$A(V_+ - V_-)$")
        d += elm.Line().at((4.6, -0.9)).to((4.6, -2.2))
        d += elm.Ground().at((4.6, -2.2))
        d += elm.Line().at((4.6, 0.9)).to((4.6, 1.7))
        d += elm.Line().at((4.6, 1.7)).to((6.0, 1.7))
        d += elm.Resistor().at((6.0, 1.7)).to((8.4, 1.7)).label("$R_o$", loc="bottom")
        d += elm.Line().at((8.4, 1.7)).to((12.2, 0.0))
        d += elm.Line().at((12.2, 0.0)).to((15.6, 0.0))
        d += elm.Label().at((15.25, 0.35)).label("$V_o$")
        # supply rails through the top and bottom edges
        d += elm.Line().at((7.0, 2.25)).to((7.0, 3.9)).label("$V_{dd}$", loc="top")
        d += (
            elm.Line().at((7.0, -2.25)).to((7.0, -3.9)).label("$-V_{ss}$", loc="bottom")
        )
        d.save(fspath(output))


def generate_op_amp_transfer_characteristic(output: Path) -> None:
    """Differential-input transfer characteristic of an operational amplifier.

    The input axis is labelled ``V+ - V-``, the differential voltage the
    course writes, the rails are marked ``V_dd`` and ``-V_ss`` where the
    output saturates (as the course plots it for the inverting amplifier),
    the knees sit a rail-gain below and above the origin, and the linear
    segment is annotated with its slope ``A``.
    """
    rail_high, rail_low = 2.4, -2.4
    knee = 0.6
    with drawing_context() as d:
        d += elm.Line().at((-6.0, 0.0)).to((6.0, 0.0))
        d += elm.Arrow().at((6.0, 0.0)).to((6.9, 0.0))
        d += elm.Label().at((8.35, 0.0)).label("$V_+ - V_-$")
        d += elm.Line().at((0.0, -3.0)).to((0.0, 3.3))
        d += elm.Arrow().at((0.0, 3.3)).to((0.0, 4.0))
        d += elm.Label().at((0.8, 4.05)).label("$V_o$")
        d += elm.Label().at((-0.5, 0.35)).label("$0$")
        # the characteristic itself is drawn in the course's curve colour
        d += elm.Line().at((-6.0, rail_low)).to((-knee, rail_low)).color(_RED)
        d += elm.Line().at((-knee, rail_low)).to((knee, rail_high)).color(_RED)
        d += elm.Line().at((knee, rail_high)).to((6.0, rail_high)).color(_RED)
        # knee ticks on the input axis, with the knee values below it
        d += elm.Line().at((knee, -0.12)).to((knee, 0.12))
        d += elm.Line().at((-knee, -0.12)).to((-knee, 0.12))
        d += elm.Label().at((0.95, -0.6)).label("$V_{dd}/A$")
        d += elm.Label().at((-0.95, -0.6)).label("$-V_{ss}/A$")
        d += elm.Label().at((-6.55, rail_high)).label("$V_{dd}$")
        d += elm.Label().at((-6.55, rail_low)).label("$-V_{ss}$")
        d += elm.Label().at((2.55, 0.95)).label("Slope $= A$")
        # the three regions named in one row below the plot, two lines each
        d += elm.Label().at((-3.5, -3.55)).label("Negative")
        d += elm.Label().at((-3.5, -3.97)).label("saturation region")
        d += elm.Label().at((0.0, -3.55)).label("Linear")
        d += elm.Label().at((0.0, -3.97)).label("region")
        d += elm.Label().at((3.5, -3.55)).label("Positive")
        d += elm.Label().at((3.5, -3.97)).label("saturation region")
        d.save(fspath(output))


def generate_feedback_loop(output: Path) -> None:
    """Block diagram of an amplifier under negative feedback.

    The course draws the closed loop as a summing junction feeding a forward
    gain block, with the output tapped and returned through a feedback gain
    block into the junction from below.
    """
    with drawing_context() as d:
        junction = (2.0, 0.0)
        # the gain blocks are plain four-line boxes: elm.Rect drops its path
        # when a Line follows it, and elm.RBox is an IEC box resistor whose
        # lead line runs through the block text
        for corner_a, corner_b in (
            ((3.2, 0.6), (6.4, 0.6)),
            ((6.4, 0.6), (6.4, -0.6)),
            ((6.4, -0.6), (3.2, -0.6)),
            ((3.2, -0.6), (3.2, 0.6)),
            ((3.2, -2.0), (6.4, -2.0)),
            ((6.4, -2.0), (6.4, -3.2)),
            ((6.4, -3.2), (3.2, -3.2)),
            ((3.2, -3.2), (3.2, -2.0)),
        ):
            d += elm.Line().at(corner_a).to(corner_b)
        d += elm.Label().at((4.8, 0.0)).label("Forward Gain")
        d += elm.Label().at((4.8, -2.6)).label("Feedback Gain")
        d += elm.Label().at((0.4, 0.0)).label("$V_{in}$")
        # the summing junction, drawn point by point: elm.Encircle measures
        # its arc from an element bbox that is not yet placed and yields NaN
        # geometry, so the circle and its label were silently dropped
        ring = _ellipse_around(junction, 0.55, 0.62)
        for start, end in zip(ring, ring[1:]):
            d += elm.Line().at(start).to(end)
        d += elm.Label().at(junction).label(r"$\Sigma$")
        d += elm.Arrow().at((0.9, 0.0)).to((junction[0] - 0.55, 0.0))
        d += elm.Arrow().at((junction[0] + 0.55, 0.0)).to((3.2, 0.0))
        d += elm.Arrow().at((6.4, 0.0)).to((8.4, 0.0))
        d += elm.Label().at((9.1, 0.0)).label("$V_{out}$")
        # the output tapped and returned through the feedback gain
        d += elm.Line().at((7.2, 0.0)).to((7.2, -2.6))
        d += elm.Arrow().at((7.2, -2.6)).to((6.4, -2.6))
        d += elm.Line().at((3.2, -2.6)).to((2.0, -2.6))
        d += elm.Arrow().at((2.0, -2.6)).to((junction[0], junction[1] - 0.62))
        d.save(fspath(output))


_AXIS_X0, _AXIS_X1 = -6.0, 6.0
_CHAR_RAIL, _CHAR_KNEE = 2.4, 0.6
_FEEDBACK_VIN = 0.8


def _block(d: Drawing, x0: float, y0: float, w: float, h: float, text: str) -> None:
    """An empty rectangle with centred text, for block diagrams.

    Explicit corner-to-corner lines rather than a rectangle element, so the
    size is in drawing units and nothing depends on the element's anchor.
    """
    d += elm.Line().at((x0, y0)).to((x0 + w, y0))
    d += elm.Line().at((x0 + w, y0)).to((x0 + w, y0 + h))
    d += elm.Line().at((x0 + w, y0 + h)).to((x0, y0 + h))
    d += elm.Line().at((x0, y0 + h)).to((x0, y0))
    d += elm.Label().at((x0 + w / 2, y0 + h / 2)).label(text)


def generate_oscillator_loop(output: Path) -> None:
    """The oscillator as three blocks in a ring: two integrators and an inverter."""

    with drawing_context() as d:
        box_w, box_h, y0 = 2.6, 1.5, -0.75
        xs = [0.0, 3.6, 7.2]
        _block(d, xs[0], y0, box_w, box_h, "integrator 1")
        _block(d, xs[1], y0, box_w, box_h, "integrator 2")
        _block(d, xs[2], y0, box_w, box_h, "inverting\namplifier")
        # signal arrows between the blocks, named after the voltages the note uses
        # no external input: the ring starts at the riser from the inverter
        for x_start, x_end, name in [
            (-1.0, xs[0], "$V_C$"),
            (xs[0] + box_w, xs[1], "$V_A$"),
            (xs[1] + box_w, xs[2], "$V_B$"),
        ]:
            d += elm.Arrow().at((x_start, 0.0)).to((x_end, 0.0))
            d += elm.Label().at(((x_start + x_end) / 2, 0.45)).label(name)
        # the inverter closes the ring: down, back along the bottom, up into the first block
        d += elm.Line().at((xs[2] + box_w, 0.0)).to((xs[2] + box_w + 1.0, 0.0))
        d += elm.Label().at((xs[2] + box_w + 0.55, 0.45)).label("$V_C$")
        d += elm.Line().at((xs[2] + box_w + 1.0, 0.0)).to((xs[2] + box_w + 1.0, -2.4))
        d += elm.Line().at((xs[2] + box_w + 1.0, -2.4)).to((-1.0, -2.4))
        d += elm.Arrow().at((-1.0, -2.4)).to((-1.0, -0.75))
        d += elm.Line().at((-1.0, -0.75)).to((-1.0, 0.0))
        d.save(fspath(output))


def generate_schmitt_hysteresis(output: Path) -> None:
    """Schmitt trigger transfer characteristic: the loop out and back again."""

    rail, thresh, span = 2.4, 1.6, 5.2
    with drawing_context() as d:
        d += elm.Line().at((-6.2, 0.0)).to((6.2, 0.0))
        d += elm.Arrow().at((6.2, 0.0)).to((7.0, 0.0))
        d += elm.Label().at((7.6, 0.0)).label("$V_{in}$")
        d += elm.Line().at((0.0, -3.2)).to((0.0, 3.4))
        d += elm.Arrow().at((0.0, 3.4)).to((0.0, 4.1))
        d += elm.Label().at((0.9, 4.15)).label("$V_o$")
        d += elm.Label().at((-0.55, 0.35)).label("$0$")
        d += elm.Label().at((-6.85, rail)).label("$V_{dd}$")
        d += elm.Label().at((-6.85, -rail)).label("$-V_{dd}$")
        # rising input: high until V_H, then the output trips down
        d += elm.Line().at((-span, rail)).to((thresh, rail)).color(_RED)
        d += elm.Arrow().at((-3.4, rail)).to((-2.0, rail)).color(_RED)
        d += elm.Line().at((thresh, rail)).to((thresh, -rail)).color(_RED)
        d += elm.Line().at((thresh, -rail)).to((span, -rail)).color(_RED)
        # falling input: low until V_L, then the output trips up
        d += elm.Line().at((span, -rail)).to((-thresh, -rail)).color(_RED)
        d += elm.Arrow().at((3.4, -rail)).to((2.0, -rail)).color(_RED)
        d += elm.Line().at((-thresh, -rail)).to((-thresh, rail)).color(_RED)
        d += elm.Line().at((-thresh, rail)).to((-span, rail)).color(_RED)
        # thresholds on the input axis, and the window between them
        d += elm.Line().at((thresh, -0.14)).to((thresh, 0.14))
        d += elm.Line().at((-thresh, -0.14)).to((-thresh, 0.14))
        d += elm.Label().at((thresh + 0.42, -0.45)).label("$V_H$")
        d += elm.Label().at((-thresh - 0.42, -0.45)).label("$V_L$")
        d += elm.Arrow().at((-thresh, -1.15)).to((thresh, -1.15))
        # clear of the vertical axis: the label sits under the right half of
        # the arrow, not across x = 0
        d += elm.Label().at((0.8, -1.95)).label("$\\Delta V_{hys}$")
        d.save(fspath(output))


def _characteristic_frame(d: Drawing) -> None:
    """Axes and the saturating characteristic, for the feedback-solution figures.

    Same geometry as ``generate_op_amp_transfer_characteristic``: rails at
    plus and minus 2.4, knees at plus and minus 0.6, input axis from -6 to 6.
    The steep middle is drawn far wider than a real amplifier's, so the
    crossings the two figures are about stay visible instead of collapsing
    onto the vertical axis.
    """
    d += elm.Line().at((_AXIS_X0, 0.0)).to((_AXIS_X1, 0.0))
    d += elm.Arrow().at((_AXIS_X1, 0.0)).to((_AXIS_X1 + 0.9, 0.0))
    d += elm.Label().at((_AXIS_X1 + 2.35, 0.0)).label("$V_+ - V_-$")
    d += elm.Line().at((0.0, -3.0)).to((0.0, 3.3))
    d += elm.Arrow().at((0.0, 3.3)).to((0.0, 4.0))
    d += elm.Label().at((0.8, 4.05)).label("$V_o$")
    d += elm.Label().at((-0.5, 0.35)).label("$0$")
    d += (
        elm.Line()
        .at((_AXIS_X0, -_CHAR_RAIL))
        .to((-_CHAR_KNEE, -_CHAR_RAIL))
        .color(_RED)
    )
    d += (
        elm.Line()
        .at((-_CHAR_KNEE, -_CHAR_RAIL))
        .to((_CHAR_KNEE, _CHAR_RAIL))
        .color(_RED)
    )
    d += elm.Line().at((_CHAR_KNEE, _CHAR_RAIL)).to((_AXIS_X1, _CHAR_RAIL)).color(_RED)
    d += elm.Label().at((_AXIS_X0 - 0.6, _CHAR_RAIL)).label("$V_{dd}$")
    d += elm.Label().at((_AXIS_X0 - 0.6, -_CHAR_RAIL)).label("$-V_{ss}$")


def generate_feedback_one_solution(output: Path) -> None:
    """Negative feedback: the downhill line meets the characteristic once."""

    with drawing_context() as d:
        _characteristic_frame(d)
        vin = _FEEDBACK_VIN
        # slope -1 through (V_in, 0), cut off where it leaves the canvas
        d += elm.Line().at((vin - 3.4, 3.4)).to((vin + 3.0, -3.0))
        d += (
            elm.Label()
            .at((-2.35, -3.7))
            .label("Negative feedback:  $V_o = V_{in} - (V_+ - V_-)$")
        )
        # the middle segment rises 2.4 over 0.6, so its slope is 4 on this
        # drawing and the crossing satisfies 4x = V_in - x
        x = vin / 5.0
        d += elm.Dot(radius=0.14).at((x, 4.0 * x))
        d += elm.Label().at((2.9, 1.45)).label("one solution")
        d += elm.Label().at((2.9, 1.02)).label("stable")
        d.save(fspath(output))


def generate_feedback_three_solutions(output: Path) -> None:
    """Positive feedback: the uphill line meets the characteristic three times."""

    with drawing_context() as d:
        _characteristic_frame(d)
        vin = _FEEDBACK_VIN
        # slope +1 through (V_in, 0), cut off where it leaves the canvas
        d += elm.Line().at((vin - _CHAR_RAIL, -_CHAR_RAIL)).to((vin + 2.65, 2.65))
        d += (
            elm.Label()
            .at((-2.35, -3.7))
            .label("Positive feedback:  $V_o = (V_+ - V_-) - V_{in}$")
        )
        # 4x = x - V_in puts the middle crossing left of the origin, and the
        # two rail crossings follow from 2.4 = x - V_in and -2.4 = x - V_in
        x = -vin / 3.0
        d += elm.Dot(open=True, radius=0.14).at((x, 4.0 * x))
        d += elm.Label().at((0.95, -1.95)).label("unstable")
        d += elm.Dot(radius=0.14).at((vin + _CHAR_RAIL, _CHAR_RAIL))
        d += elm.Dot(radius=0.14).at((vin - _CHAR_RAIL, -_CHAR_RAIL))
        d += elm.Label().at((1.6, 2.95)).label("stable")
        d += elm.Label().at((-3.0, -3.0)).label("stable")
        d.save(fspath(output))


def generate_amplifier_loading(output: Path) -> None:
    """Practical voltage amplifier loaded by a resistor, in three stages.

    Follows the course figure with one dashed box per stage (source,
    amplifier, load) over one continuous return wire, with no ground symbol.
    Inside the amplifier box the input port and the output port are two
    separate loops that share only that return wire: the source drives ``R_i``
    across the input terminals, and the dependent source ``A_v V_i`` drives its
    own loop through ``R_o`` and the load.  ``A_v V_i`` sits beside the diamond,
    ``V_i`` is marked inside the input loop, ``V_o`` to the right of the load
    loop, and each resistance beside the resistor that carries it.
    """
    with drawing_context() as d:
        source = elm.SourceV().up().at((0.0, -2.0)).length(2.0)
        d += source
        d += elm.Label().at((-0.85, -1.0)).label("$V_s$")
        d += elm.Resistor().at(source.end).to((2.0, 0.0)).label("$R_s$", loc="bottom")
        # the input port: its own loop, sharing only the return wire
        d += elm.Line().at((2.0, 0.0)).to((4.6, 0.0))
        d += elm.Resistor().at((4.6, 0.0)).to((4.6, -2.0))
        d += elm.Label().at((3.85, -1.0)).label("$R_i$")
        d += elm.Label().at((3.2, -0.45)).label("$+$")
        d += elm.Label().at((3.2, -1.0)).label("$V_i$")
        d += elm.Label().at((3.2, -1.55)).label("$-$")
        # the output port: the dependent source drives its own loop through
        # R_o and the load, meeting the input port only on the return wire
        amp = elm.SourceControlledV().up().at((5.6, -2.0)).length(2.0)
        d += amp
        d += elm.Label().at((6.75, -1.3)).label("$A_v V_i$")
        d += elm.Resistor().at((5.6, 0.0)).to((7.6, 0.0)).label("$R_o$", loc="bottom")
        d += elm.Line().at((7.6, 0.0)).to((9.2, 0.0))
        d += elm.Resistor().at((9.2, 0.0)).to((9.2, -2.0))
        d += elm.Label().at((9.68, -1.0)).label("$R_L$")
        d += elm.Label().at((10.8, -0.45)).label("$+$")
        d += elm.Label().at((10.8, -1.0)).label("$V_o$")
        d += elm.Label().at((10.8, -1.55)).label("$-$")
        # one continuous return wire, the only wire the two ports share
        d += elm.Line().at(source.start).to((9.2, -2.0))
        for corner1, corner2 in (
            ((-1.3, -2.4), (2.4, 0.4)),
            ((2.9, -2.4), (8.0, 0.4)),
            ((8.6, -2.4), (10.15, 0.4)),
        ):
            box = elm.Rect(corner1=corner1, corner2=corner2)
            d += box.at((0.0, 0.0)).linestyle("--")
        d += elm.Label().at((0.8, -3.0)).label("source")
        d += elm.Label().at((5.45, -3.0)).label("amplifier")
        d += elm.Label().at((9.2, -3.0)).label("load")
        d.save(fspath(output))


def generate_buffer_amplifier(output: Path) -> None:
    """Unity-gain buffer (voltage follower).

    Flipped from the default, the non-inverting input (+) sits on top, fed
    by ``V_in``; the output is wired back to the inverting input below it,
    as the course draws the circuit, with the gain ``A`` inside the
    triangle.
    """
    with drawing_context() as d:
        op = (
            elm.Opamp()
            .right()
            .flip()
            .at((0.0, 0.0))
            .anchor("center")
            .label("$A$", loc="center")
        )
        d += op
        d += elm.Line().at(op.in2).left().length(2.2).label("$V_{in}$", loc="bottom")
        node = (op.out[0] + 2.4, 0.0)
        d += elm.Line().at(op.out).to(node)
        d += elm.Dot().at(node)
        d += elm.Line().at(node).to((node[0], -1.9))
        d += elm.Line().at((node[0], -1.9)).to((op.in1[0] - 0.6, -1.9))
        d += elm.Line().at((op.in1[0] - 0.6, -1.9)).to((op.in1[0] - 0.6, op.in1[1]))
        d += elm.Line().at((op.in1[0] - 0.6, op.in1[1])).to(op.in1)
        d += elm.Label().at((node[0] + 1.0, 0.0)).label("$V_o$")
        d.save(fspath(output))


def generate_schmitt_trigger(output: Path) -> None:
    """Schmitt trigger: a comparator with the divider moved onto the + input.

    Follows the course figure: the non-inverting input sits on top and takes
    the tap of the ``R_1``/``R_2`` divider, which runs along a rail above the
    triangle from ground to the output node; ``V_in`` enters the inverting
    input below it.  The rail clears the ``V_dd`` supply lead, so no wire
    crosses another and each resistance sits above its own resistor.
    """
    with drawing_context() as d:
        op = (
            elm.Opamp()
            .right()
            .flip()
            .at((0.0, 0.0))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += op
        # supply names sit right above and below their own leads: the shared
        # helper would push them sideways into the tap wire of the divider
        d += elm.Line().at(op.vs).up().length(0.9)
        d += elm.Label().at((op.vs[0], op.vs[1] + 1.45)).label("$V_{dd}$")
        d += elm.Line().at(op.vd).down().length(0.9)
        d += elm.Label().at((op.vd[0], op.vd[1] - 1.45)).label("$-V_{ss}$")
        rail_y = op.vs[1] + 2.4
        tap_x = op.in2[0] - 0.9
        node = (op.out[0] + 2.4, 0.0)
        # the divider rail: ground, R_1, the tap on the + input, R_2, output
        ground_x = tap_x - 2.2
        d += elm.Line().at((ground_x, rail_y)).down().length(0.6)
        d += elm.Ground().at((ground_x, rail_y - 0.6))
        d += (
            elm.Resistor()
            .at((ground_x, rail_y))
            .to((tap_x, rail_y))
            .label("$R_1$", loc="top")
        )
        d += elm.Dot().at((tap_x, rail_y))
        d += (
            elm.Resistor()
            .at((tap_x, rail_y))
            .to((node[0], rail_y))
            .label("$R_2$", loc="top")
        )
        d += elm.Line().at((tap_x, rail_y)).to((tap_x, op.in2[1]))
        d += elm.Line().at((tap_x, op.in2[1])).to(op.in2)
        d += elm.Label().at((tap_x - 0.6, op.in2[1] + 0.5)).label("$V_+$")
        # the input enters the inverting terminal, marked with its own name
        d += elm.Line().at(op.in1).left().length(2.6)
        d += elm.Label().at((op.in1[0] - 2.55, op.in1[1] - 0.45)).label("$V_{in}$")
        d += elm.Label().at((op.in1[0] - 0.85, op.in1[1] + 0.42)).label("$V_-$")
        # the output node the feedback divider hangs from
        d += elm.Line().at(op.out).to(node)
        d += elm.Dot().at(node)
        d += elm.Line().at((node[0], rail_y)).to(node)
        d += elm.Label().at((node[0] + 1.0, 0.0)).label("$V_o$")
        d.save(fspath(output))


def generate_non_inverting_amplifier(output: Path) -> None:
    """Non-inverting amplifier with its feedback divider.

    Flipped from the default, the non-inverting input (+) sits on top and
    receives ``V_in``; the ``R2``/``R1`` divider tapped off the output feeds
    the inverting input below it, as the course draws the circuit.
    """
    with drawing_context() as d:
        op = (
            elm.Opamp()
            .right()
            .flip()
            .at((0.0, 0.0))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += op
        d += elm.Line().at(op.in2).left().length(2.4).label("$V_{in}$", loc="bottom")
        _op_amp_supplies(d, op, flip=True)
        node = (op.out[0] + 2.2, 0.0)
        d += elm.Line().at(op.out).to(node)
        d += elm.Dot().at(node)
        d += elm.Label().at((node[0] + 1.0, 0.0)).label("$V_{out}$")
        tap = (node[0], op.in2[1] - 1.7)
        d += elm.Resistor().at(node).to(tap).label("$R_2$", loc="right")
        d += elm.Dot().at(tap)
        d += elm.Label().at((tap[0] - 0.95, tap[1] + 0.55)).label("$V_-$")
        d += elm.Resistor().at(tap).to((tap[0], tap[1] - 1.7))
        d += elm.Label().at((tap[0] + 0.62, tap[1] - 1.30)).label("$R_1$")
        d += elm.Ground().at((tap[0], tap[1] - 1.7))
        # the divider tap reaches the inverting input from outside the
        # triangle, passing below the inverted supply lead on the way
        feed_x = op.in1[0] - 1.1
        feed_y = op.vd[1] - 1.8
        d += elm.Line().at(tap).to((op.out[0] + 0.4, tap[1]))
        d += elm.Line().at((op.out[0] + 0.4, tap[1])).to((op.out[0] + 0.4, feed_y))
        d += elm.Line().at((op.out[0] + 0.4, feed_y)).to((feed_x, feed_y))
        d += elm.Line().at((feed_x, feed_y)).to((feed_x, op.in1[1]))
        d += elm.Line().at((feed_x, op.in1[1])).to(op.in1)
        d.save(fspath(output))


def _capacitor_branch(
    d: Drawing, x0: float, x1: float, y: float, name: str, label_dy: float = 1.0
) -> elm.Line:
    """A capacitor sitting in a horizontal branch that runs from ``x0`` to ``x1``.

    Schemdraw's own capacitor element is avoided on purpose: the plates here
    sit at a fixed gap so the two figures that swap the capacitor and the
    resistor read at the same scale. Returns the lead the caller may hang a
    current arrow on.
    """
    xm = (x0 + x1) / 2
    lead = elm.Line().at((x0, y)).to((xm - 0.12, y))
    d += lead
    d += elm.Line().at((xm - 0.12, y - 0.45)).to((xm - 0.12, y + 0.45)).linewidth(3)
    d += elm.Line().at((xm + 0.12, y - 0.45)).to((xm + 0.12, y + 0.45)).linewidth(3)
    d += elm.Line().at((xm + 0.12, y)).to((x1, y))
    d += elm.Label().at((xm, y + label_dy)).label(name)
    return lead


def _inverting_skeleton(
    d: Drawing,
) -> tuple[elm.Opamp, elm.SourceV, tuple[float, float]]:
    """Draw the parts shared by the inverting amplifier and its two calculus stages.

    Returns the amplifier, the input source and the summing node, so each
    caller only has to fill in the input path and the feedback path.
    """
    op = (
        elm.Opamp()
        .right()
        .at((0.0, 0.0))
        .anchor("center")
        .label(r"$\infty$", loc="center")
    )
    d += op
    d += elm.Line().at(op.in2).left().length(1.1)
    d += elm.Line().at((op.in2[0] - 1.1, op.in2[1])).down().length(1.1)
    d += elm.Ground().at((op.in2[0] - 1.1, op.in2[1] - 1.1))
    _op_amp_supplies(d, op, flip=False, label_side="right")
    source = (
        elm.SourceV()
        .up()
        .at((-7.4, -2.2))
        .length(2.825)
        .label("$V_{in}$", loc="bottom")
    )
    d += source
    d += elm.Ground().at(source.start)
    return op, source, (-2.4, op.in1[1])


RAIL_Y = 3.3
"""Height of the feedback rail in the calculus stages.

Higher than the inverting amplifier's 2.7 because the capacitor sits on the
rail here, and its plates would otherwise crowd the ``V_dd`` supply label.
"""


def _feedback_rail(
    d: Drawing, op: elm.Opamp, node_a: tuple[float, float]
) -> tuple[float, float]:
    """Output node and the start of the feedback rail that clears the V_dd lead."""
    node = (op.out[0] + 2.6, 0.0)
    d += elm.Line().at(op.out).to(node)
    d += elm.Dot().at(node)
    d += elm.Label().at((node[0] + 1.0, 0.0)).label("$V_{out}$")
    d += elm.Line().at(node_a).to((node_a[0], RAIL_Y))
    return node


def generate_dac_converter(output: Path) -> None:
    """4-bit digital-to-analog converter, weighting stage and sign restore.

    Four bits close four switches into branches weighted ``2R``, ``4R``,
    ``8R`` and ``16R`` against the feedback ``R`` of an inverting summing
    amplifier, so the word becomes a sum.  A second inverting amplifier with
    equal ``R_a`` resistors follows it and cancels the minus sign, which is
    how the output leaves the converter.
    """
    with drawing_context() as d:
        op1 = (
            elm.Opamp()
            .right()
            .anchor("center")
            .at((7.4, 3.4))
            .label("$A$", loc="center")
        )
        op2 = (
            elm.Opamp()
            .right()
            .anchor("center")
            .at((16.6, 3.4))
            .label("$A$", loc="center")
        )
        d += op1
        d += op2
        sum_y = op1.in1[1]
        weights = ("$2R$", "$4R$", "$8R$", "$16R$")
        bits = ("$b_3$", "$b_2$", "$b_1$", "$b_0$")
        branch_y = [sum_y + 1.8, sum_y + 0.6, sum_y - 0.6, sum_y - 1.8]
        # the reference feeds all four switched branches
        d += elm.Line().at((0.0, branch_y[0])).to((0.0, branch_y[-1]))
        d += (
            elm.Label().at((-1.05, (branch_y[0] + branch_y[-1]) / 2)).label("$V_{ref}$")
        )
        for y, weight, bit in zip(branch_y, weights, bits):
            d += elm.Line().at((0.0, y)).to((0.55, y))
            d += elm.Switch().at((0.55, y)).to((1.55, y))
            d += elm.Label().at((3.85, y - 0.48)).label(bit)
            d += elm.Resistor().at((1.55, y)).to((3.3, y))
            d += elm.Label().at((2.42, y + 0.55)).label(weight)
            d += elm.Line().at((3.3, y)).to((4.3, y))
        # the four branches meet at the summing node of the first amplifier
        d += elm.Line().at((4.3, branch_y[0])).to((4.3, branch_y[-1]))
        for y in branch_y:
            d += elm.Dot().at((4.3, y))
        d += elm.Line().at((4.3, sum_y)).to(op1.in1)
        d += elm.Line().at(op1.in2).left().length(0.9)
        d += elm.Line().at((op1.in2[0] - 0.9, op1.in2[1])).down().length(0.9)
        d += elm.Ground().at((op1.in2[0] - 0.9, op1.in2[1] - 0.9))
        # feedback R of the weighting stage, clear of the triangle
        node1 = (op1.out[0] + 2.2, sum_y)
        d += elm.Line().at(op1.out).to(node1)
        d += elm.Dot().at(node1)
        fb1_y = sum_y + 2.9
        d += elm.Line().at((4.3, sum_y)).to((4.3, fb1_y))
        d += (
            elm.Resistor()
            .at((4.3, fb1_y))
            .to((node1[0], fb1_y))
            .label("$R$", loc="top")
        )
        d += elm.Line().at((node1[0], fb1_y)).to(node1)
        # the inverting stage: R_a in, R_a back, so the sign returns to plus
        ra_x0 = node1[0] + 1.0
        ra_x1 = op2.in1[0] - 2.2
        d += elm.Line().at(node1).to((ra_x0, sum_y))
        d += elm.Resistor().at((ra_x0, sum_y)).to((ra_x1, sum_y))
        d += elm.Label().at(((ra_x0 + ra_x1) / 2, sum_y + 0.62)).label("$R_a$")
        tap2 = (ra_x1 + 1.0, sum_y)
        d += elm.Line().at((ra_x1, sum_y)).to(tap2)
        d += elm.Dot().at(tap2)
        d += elm.Line().at(tap2).to(op2.in1)
        d += elm.Line().at(op2.in2).left().length(0.9)
        d += elm.Line().at((op2.in2[0] - 0.9, op2.in2[1])).down().length(0.9)
        d += elm.Ground().at((op2.in2[0] - 0.9, op2.in2[1] - 0.9))
        node2 = (op2.out[0] + 2.2, sum_y)
        d += elm.Line().at(op2.out).to(node2)
        d += elm.Dot().at(node2)
        fb2_y = sum_y + 2.2
        d += elm.Line().at(tap2).to((tap2[0], fb2_y))
        d += (
            elm.Resistor()
            .at((tap2[0], fb2_y))
            .to((node2[0], fb2_y))
            .label("$R_a$", loc="top")
        )
        d += elm.Line().at((node2[0], fb2_y)).to(node2)
        d += elm.Label().at((node2[0] + 1.05, sum_y)).label("$V_o$")
        d.save(fspath(output))


def generate_flash_adc(output: Path) -> None:
    """2-bit flash analog-to-digital converter, chain and encoder.

    A chain of four equal ``R`` divides ``V_ref`` into the three references;
    each comparator takes ``V_in`` on its plus input and one reference on its
    minus input, and the three outputs ``A``, ``B`` and ``C`` enter a binary
    encoder that prints the two-bit word.  The ``V_in`` bus crosses the
    reference leads without a dot: the two nets do not meet.  The comparators
    are drawn wider than the usual symbol so their ``+``, ``-`` and ``CMP``
    marks fit inside and beside them at full size.
    """
    with drawing_context() as d:
        top_y, step = 7.2, 2.1
        d += elm.Label().at((0.0, top_y + 0.55)).label("$V_{ref}$")
        # four equal R down to ground, with the three taps between them
        ys = [top_y - step * i for i in range(5)]
        for y0, y1 in zip(ys, ys[1:]):
            d += elm.Resistor().at((0.0, y0)).to((0.0, y1))
            d += elm.Label().at((-0.78, (y0 + y1) / 2)).label("$R$")
        d += elm.Ground().at((0.0, ys[-1]))
        # the three references, written beside their taps
        for y, text in zip(ys[1:4], ("$3V_{ref}/4$", "$V_{ref}/2$", "$V_{ref}/4$")):
            d += elm.Label().at((-1.55, y)).label(text)
            d += elm.Dot().at((0.0, y))
        # the input bus, crossing the reference leads without joining them
        bus_x = 2.2
        plus_y = [y + 0.6 for y in ys[1:4]]
        d += elm.Line().at((bus_x, top_y - 0.3)).to((bus_x, plus_y[-1]))
        d += elm.Label().at((bus_x, top_y + 0.55)).label("$V_{in}$")
        for y_plus in plus_y[:-1]:
            d += elm.Dot().at((bus_x, y_plus))
        # three comparators: plus from the input bus, minus from the chain
        tip_x, half = 6.3, 0.9
        centres = [y + 0.3 for y in ys[1:4]]
        for y_ref, y_plus, centre, name in zip(
            ys[1:4], plus_y, centres, ("$A$", "$B$", "$C$")
        ):
            d += elm.Line().at((bus_x, y_plus)).to((3.7, y_plus))
            d += elm.Line().at((0.0, y_ref)).to((3.7, y_ref))
            d += elm.Line().at((3.7, centre + half)).to((3.7, centre - half))
            d += elm.Line().at((3.7, centre + half)).to((tip_x, centre))
            d += elm.Line().at((3.7, centre - half)).to((tip_x, centre))
            # the mathtext ink sits above and right of a label anchor, so
            # each mark is offset back onto the lead it names
            d += (
                elm.Label()
                .at((4.229, y_plus - 0.128))
                .label("$+$", halign="center", valign="center")
            )
            d += (
                elm.Label()
                .at((4.229, y_ref - 0.181))
                .label("$-$", halign="center", valign="center")
            )
            d += elm.Label().at((6.95, centre - 0.45)).label("CMP")
            d += elm.Label().at((6.95, centre + 0.4)).label(name)
        # the encoder, drawn as one block that prints the reduced logic
        # explicit corner-to-corner lines: elm.Rect inherits the previous
        # element's angle and would arrive rotated
        left, right = 8.2, 13.4
        top, bottom = centres[0] + 1.0, centres[-1] - 1.3
        for corner_a, corner_b in (
            ((left, bottom), (right, bottom)),
            ((right, bottom), (right, top)),
            ((right, top), (left, top)),
            ((left, top), (left, bottom)),
        ):
            d += elm.Line().at(corner_a).to(corner_b).linestyle("--")
        d += elm.Label().at(((left + right) / 2, bottom + 0.75)).label("binary encoder")
        out1, out2 = (centres[0] + centres[1]) / 2, (centres[1] + centres[2]) / 2
        d += elm.Label().at(((left + right) / 2, out1)).label("$b_1 = B$")
        d += elm.Label().at(((left + right) / 2, out2)).label("$b_0 = (A+\\bar{B})C$")
        for centre in centres:
            d += elm.Line().at((tip_x, centre)).to((left, centre))
        for y, name in ((out1, "$b_1$"), (out2, "$b_0$")):
            d += elm.Line().at((right, y)).to((right + 1.6, y))
            d += elm.Label().at((right + 2.15, y)).label(name)
        d.save(fspath(output))


def generate_integrator(output: Path) -> None:
    """Inverting integrator: resistor in the input path, capacitor feeding back."""

    with drawing_context() as d:
        op, source, node_a = _inverting_skeleton(d)
        r1 = elm.Resistor().at(source.end).to(node_a)
        d += (
            elm.Label()
            .at(((source.end[0] + node_a[0]) / 2, node_a[1] + 1.35))
            .label("$R$")
        )
        d += r1
        d += elm.CurrentLabel(top=True).at(r1).label("$I$")
        d += elm.Dot().at(node_a)
        d += elm.Label().at((node_a[0] - 0.55, node_a[1] + 0.7)).label("$V_-$")
        d += elm.Line().at(node_a).to(op.in1)
        node = _feedback_rail(d, op, node_a)
        lead = _capacitor_branch(d, node_a[0], node[0], RAIL_Y, "$C_1$")
        d += elm.CurrentLabel(top=True).at(lead.end).label("$I$")
        d += elm.Line().at((node[0], RAIL_Y)).to(node)
        d += elm.Dot().at((node_a[0], RAIL_Y))
        d += elm.Dot().at((node[0], RAIL_Y))
        # reset switch: a rail of its own above the capacitor, in parallel with
        # it, so closing the blade shorts C_1 and returns V_o to zero
        sw_y = RAIL_Y + 1.9
        mid = (node_a[0] + node[0]) / 2
        d += elm.Line().at((node_a[0], RAIL_Y)).to((node_a[0], sw_y))
        d += elm.Line().at((node[0], RAIL_Y)).to((node[0], sw_y))
        d += elm.Line().at((node_a[0], sw_y)).to((mid - 0.95, sw_y))
        d += elm.Switch().at((mid - 0.95, sw_y)).to((mid + 0.95, sw_y))
        d += elm.Line().at((mid + 0.95, sw_y)).to((node[0], sw_y))
        d += elm.Label().at((mid, sw_y + 1.15)).label("reset")
        d += (
            elm.Label().at((node_a[0] - 1.6, node_a[1] - 1.95)).label("virtual\nground")
        )
        d.save(fspath(output))


def generate_differentiator(output: Path) -> None:
    """Inverting differentiator: capacitor in the input path, resistor feeding back."""

    with drawing_context() as d:
        op, source, node_a = _inverting_skeleton(d)
        lead = _capacitor_branch(d, source.end[0], node_a[0], node_a[1], "$C_1$", 1.35)
        d += elm.CurrentLabel(top=True).at(lead.end).label("$I$")
        d += elm.Dot().at(node_a)
        d += elm.Label().at((node_a[0] - 0.55, node_a[1] + 0.7)).label("$V_-$")
        d += elm.Line().at(node_a).to(op.in1)
        node = _feedback_rail(d, op, node_a)
        r = elm.Resistor().at((node_a[0], RAIL_Y)).to((node[0], RAIL_Y))
        d += r
        d += elm.Label().at(((node_a[0] + node[0]) / 2, RAIL_Y + 1.35)).label("$R$")
        d += elm.CurrentLabel(top=True).at(r).label("$I$")
        d += elm.Line().at((node[0], RAIL_Y)).to(node)
        d += (
            elm.Label().at((node_a[0] - 1.6, node_a[1] - 1.95)).label("virtual\nground")
        )
        d.save(fspath(output))


def generate_inverting_amplifier(output: Path) -> None:
    """Inverting amplifier with the inverting input at virtual ground.

    The default triangle already has the inverting input (-) on top, as the
    course draws this circuit: ``R1`` carries ``V_in`` to that input, ``R2``
    returns from the output to the same node, and the non-inverting input
    below is grounded.
    """
    with drawing_context() as d:
        op = (
            elm.Opamp()
            .right()
            .at((0.0, 0.0))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += op
        d += elm.Line().at(op.in2).left().length(1.1)
        d += elm.Line().at((op.in2[0] - 1.1, op.in2[1])).down().length(1.1)
        d += elm.Ground().at((op.in2[0] - 1.1, op.in2[1] - 1.1))
        _op_amp_supplies(d, op, flip=False, label_side="right")
        source = (
            elm.SourceV()
            .up()
            .at((-7.4, -2.2))
            .length(2.825)
            .label("$V_{in}$", loc="bottom")
        )
        d += source
        d += elm.Ground().at(source.start)
        node_a = (-2.4, op.in1[1])
        r1 = elm.Resistor().at(source.end).to(node_a)
        # the name sits directly above the current arrow that schemdraw
        # draws over the body, so the two read as one label on R_1
        d += (
            elm.Label()
            .at(((source.end[0] + node_a[0]) / 2, node_a[1] + 1.35))
            .label("$R_1$")
        )
        d += r1
        d += elm.CurrentLabel(top=True).at(r1).label("$I$")
        d += elm.Dot().at(node_a)
        d += elm.Label().at((node_a[0] - 0.55, node_a[1] + 0.7)).label("$V_-$")
        d += elm.Line().at(node_a).to(op.in1)
        node = (op.out[0] + 2.6, 0.0)
        d += elm.Line().at(op.out).to(node)
        d += elm.Dot().at(node)
        d += elm.Label().at((node[0] + 1.0, 0.0)).label("$V_{out}$")
        # the return path clears the V_dd supply stub, which rises to 1.74
        # and whose label sits at 1.89
        d += elm.Line().at(node_a).to((node_a[0], 2.7))
        r2 = elm.Resistor().at((node_a[0], 2.7)).to((node[0], 2.7))
        d += r2
        d += elm.Label().at(((node_a[0] + node[0]) / 2, 3.35 + 0.7)).label("$R_2$")
        d += elm.CurrentLabel(top=True).at(r2).label("$I$")
        d += elm.Line().at((node[0], 2.7)).to(node)
        # the name hangs left of the summing node on two lines, so it stays
        # close to the node while ending well clear of it, and clear of the
        # wire that carries the non-inverting input down to ground
        d += elm.Label().at((node_a[0] - 2.0, node_a[1] - 1.1)).label("virtual\nground")
        d.save(fspath(output))


def generate_summing_amplifier(output: Path) -> None:
    """Two-input summing amplifier.

    The default triangle already has the inverting input (-) on top, as the
    course draws this circuit: both sources reach that input through their
    resistors, ``Rf`` returns from the output to the same node, and the
    non-inverting input below is grounded.
    """
    with drawing_context() as d:
        op = (
            elm.Opamp()
            .right()
            .at((0.0, 0.0))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += op
        d += elm.Line().at(op.in2).left().length(1.1)
        d += elm.Line().at((op.in2[0] - 1.1, op.in2[1])).down().length(1.1)
        d += elm.Ground().at((op.in2[0] - 1.1, op.in2[1] - 1.1))
        source_1 = (
            elm.SourceV()
            .up()
            .at((-8.4, -2.2))
            .length(2.825)
            .label("$V_{s1}$", loc="bottom")
        )
        d += source_1
        d += elm.Ground().at(source_1.start)
        node_a = (-2.6, op.in1[1])
        d += elm.Resistor().at(source_1.end).to(node_a).label("$R_1$", loc="top")
        source_2 = (
            elm.SourceV()
            .up()
            .at((-9.8, 1.2))
            .length(1.3)
            .label("$V_{s2}$", loc="bottom")
        )
        d += source_2
        d += elm.Ground().at(source_2.start)
        d += (
            elm.Resistor()
            .at(source_2.end)
            .to((-4.2, source_2.end[1]))
            .label("$R_2$", loc="top")
        )
        d += elm.Line().at((-4.2, source_2.end[1])).to((-4.2, node_a[1]))
        d += elm.Line().at((-4.2, node_a[1])).to(node_a)
        d += elm.Dot().at(node_a)
        d += elm.Line().at(node_a).to(op.in1)
        node = (op.out[0] + 2.6, 0.0)
        d += elm.Line().at(op.out).to(node)
        d += elm.Dot().at(node)
        d += elm.Label().at((node[0] + 1.0, 0.0)).label("$V_{out}$")
        d += elm.Line().at(node_a).to((node_a[0], 1.9))
        d += elm.Resistor().at((node_a[0], 1.9)).to((node[0], 1.9))
        d += elm.Label().at(((node_a[0] + node[0]) / 2, 2.55)).label("$R_f$")
        d += elm.Line().at((node[0], 1.9)).to(node)
        d.save(fspath(output))


def generate_difference_amplifier(output: Path) -> None:
    """Difference amplifier with its four-resistor network.

    The default triangle already has the inverting input (-) on top, as the
    course draws this circuit: ``V1`` reaches it through ``R1`` with ``R2``
    returning from the output, and ``V2`` feeds the non-inverting input
    below through its own ``R1``/``R2`` divider.
    """
    with drawing_context() as d:
        op = (
            elm.Opamp()
            .right()
            .at((0.6, 0.0))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += op
        source_1 = (
            elm.SourceV().up().at((-8.6, -3.1)).length(4.0).label("$V_1$", loc="bottom")
        )
        d += source_1
        d += elm.Ground().at(source_1.start)
        node_a = (-3.4, 1.2)
        d += elm.Resistor().at(source_1.end).to((-3.4, 0.9)).label("$R_1$", loc="top")
        d += elm.Line().at((-3.4, 0.9)).to(node_a)
        d += elm.Dot().at(node_a)
        d += elm.Line().at(node_a).to((-1.4, 1.2))
        d += elm.Line().at((-1.4, 1.2)).to((-1.4, op.in1[1]))
        d += elm.Line().at((-1.4, op.in1[1])).to(op.in1)
        source_2 = (
            elm.SourceV().up().at((-6.8, -3.1)).length(2.0).label("$V_2$", loc="bottom")
        )
        d += source_2
        d += elm.Ground().at(source_2.start)
        node_b = (-3.4, -1.2)
        d += elm.Resistor().at(source_2.end).to((-3.4, -1.1)).label("$R_1$", loc="top")
        d += elm.Line().at((-3.4, -1.1)).to(node_b)
        d += elm.Dot().at(node_b)
        d += elm.Line().at(node_b).to((-1.4, -1.2))
        d += elm.Line().at((-1.4, -1.2)).to((-1.4, op.in2[1]))
        d += elm.Line().at((-1.4, op.in2[1])).to(op.in2)
        d += elm.Resistor().at(node_b).to((-3.4, -2.6))
        d += elm.Label().at((-2.8, -1.9)).label("$R_2$")
        d += elm.Ground().at((-3.4, -2.6))
        node = (op.out[0] + 2.6, 0.0)
        d += elm.Line().at(op.out).to(node)
        d += elm.Dot().at(node)
        d += elm.Label().at((node[0] + 1.0, 0.0)).label("$V_{out}$")
        d += elm.Line().at(node_a).to((node_a[0], 2.4))
        d += elm.Resistor().at((node_a[0], 2.4)).to((node[0], 2.4))
        d += elm.Label().at(((node_a[0] + node[0]) / 2, 2.85)).label("$R_2$")
        d += elm.Line().at((node[0], 2.4)).to(node)
        d.save(fspath(output))


def generate_instrumentation_amplifier(output: Path) -> None:
    """Two-op-amp instrumentation amplifier with a differential output.

    A string of ``R1``, ``R``, ``R1`` hangs between the two op-amp outputs;
    each inverting input taps the string, so the gain resistor ``R`` carries
    the whole input difference and the output is read between the two
    outputs.
    """
    with drawing_context() as d:
        top = (
            elm.Opamp()
            .right()
            .flip()
            .at((0.0, 4.0))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += top
        bottom = (
            elm.Opamp()
            .right()
            .at((0.0, -4.0))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += bottom
        # each signal enters the non-inverting input (+): flipped from the
        # default, the top triangle has + on top, and the bottom one keeps
        # + below, as the course draws them
        d += elm.Line().at(top.in2).left().length(2.2)
        d += elm.Label().at((top.in2[0] - 2.2, top.in2[1] - 0.6)).label("$V_2$")
        d += elm.Line().at(bottom.in2).left().length(2.2)
        d += elm.Label().at((bottom.in2[0] - 3.4, bottom.in2[1] - 0.6)).label("$V_1$")
        # the resistor string between the two outputs
        out_top = (top.out[0] + 1.6, top.out[1])
        out_bottom = (bottom.out[0] + 1.6, bottom.out[1])
        d += elm.Line().at(top.out).to(out_top)
        d += elm.Dot().at(out_top)
        d += elm.Label().at((out_top[0] + 0.9, out_top[1] + 0.5)).label("$+$")
        d += elm.Line().at(bottom.out).to(out_bottom)
        d += elm.Dot().at(out_bottom)
        d += elm.Label().at((out_bottom[0] + 0.9, out_bottom[1] - 0.5)).label("$-$")
        d += (
            elm.Label()
            .at((out_top[0] + 2.4, (out_top[1] + out_bottom[1]) / 2))
            .label("$V_o$")
        )
        r1_top_end = (out_top[0], out_top[1] - 1.5)
        d += elm.Resistor().at(out_top).to(r1_top_end)
        d += elm.Label().at((out_top[0] + 0.55, out_top[1] - 0.75)).label("$R_1$")
        d += elm.Dot().at(r1_top_end)
        d += elm.Label().at((r1_top_end[0] - 0.95, r1_top_end[1] - 0.35)).label("$V_2$")
        # each inverting input taps the string through an elbow wire
        top_jog = (top.in1[0] - 1.0, r1_top_end[1])
        d += elm.Line().at(r1_top_end).to(top_jog)
        d += elm.Line().at(top_jog).to((top_jog[0], top.in1[1]))
        d += elm.Line().at((top_jog[0], top.in1[1])).to(top.in1)
        gain_start = r1_top_end
        gain_end = (out_bottom[0], out_bottom[1] + 1.5)
        gain_res = elm.Resistor().at(gain_start).to(gain_end)
        d += (
            elm.Label()
            .at((gain_end[0] + 0.45, (r1_top_end[1] + gain_end[1]) / 2))
            .label("$R$")
        )
        d += gain_res
        d += elm.CurrentLabel(top=False).at(gain_res).label("$I$")
        d += elm.Dot().at(gain_end)
        d += elm.Label().at((gain_end[0] - 1.2, gain_end[1] + 0.35)).label("$V_1$")
        bottom_jog = (bottom.in1[0] - 1.0, gain_end[1])
        d += elm.Line().at(gain_end).to(bottom_jog)
        d += elm.Line().at(bottom_jog).to((bottom_jog[0], bottom.in1[1]))
        d += elm.Line().at((bottom_jog[0], bottom.in1[1])).to(bottom.in1)
        d += elm.Resistor().at(gain_end).to(out_bottom)
        d += (
            elm.Label()
            .at((gain_end[0] + 0.45, (gain_end[1] + out_bottom[1]) / 2))
            .label("$R_1$")
        )
        d.save(fspath(output))


def generate_instrumentation_amplifier_single_ended(output: Path) -> None:
    """Instrumentation amplifier reshaped for a ground-referenced output.

    The course's single-ended version: the string becomes ``R2``, ``R1``,
    ``R1``, ``R2`` running from the top output down to ground, ``RG`` hangs
    to the right from the ``V2`` tap to the bottom output, and the lower
    ``R2`` returns that output node to ground. Each op-amp terminal reaches
    the string through its own corridor, so no wire crosses another.
    """
    with drawing_context() as d:
        top = (
            elm.Opamp()
            .right()
            .flip()
            .at((0.0, 4.6))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += top
        bottom = (
            elm.Opamp()
            .right()
            .at((0.0, -3.6))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += bottom
        # the two inputs, at the non-inverting terminals as before
        d += elm.Line().at(top.in2).left().length(2.4)
        d += elm.Label().at((top.in2[0] - 2.6, top.in2[1] - 0.7)).label("$V_2$")
        d += elm.Line().at(bottom.in2).left().length(2.4)
        d += elm.Label().at((bottom.in2[0] - 2.6, bottom.in2[1] - 0.7)).label("$V_1$")

        xs = top.out[0] + 3.0
        node_vo = (xs, top.out[1])
        tap_v2 = (xs, node_vo[1] - 1.9)
        tap_v1 = (xs, tap_v2[1] - 2.3)
        node_c = (xs, tap_v1[1] - 2.3)

        # top output out to the Vo node, then R2 down to the V2 tap
        d += elm.Line().at(top.out).to(node_vo)
        d += elm.Dot().at(node_vo)
        d += elm.Label().at((xs + 0.9, node_vo[1] + 0.55)).label("$V_o$")
        d += elm.Resistor().at(node_vo).to(tap_v2)
        d += elm.Label().at((xs + 0.6, (node_vo[1] + tap_v2[1]) / 2)).label("$R_2$")
        d += elm.Dot().at(tap_v2)
        d += elm.Label().at((xs - 0.95, tap_v2[1] + 0.45)).label("$V_2$")

        # R1 from the V2 tap to the V1 tap, R1 on to the bottom output node
        res_ia = elm.Resistor().at(tap_v2).to(tap_v1)
        d += elm.Label().at((xs + 0.6, (tap_v2[1] + tap_v1[1]) / 2)).label("$R_1$")
        arrow_a_top = (xs - 0.5, tap_v2[1] - 0.25)
        arrow_a_tip = (xs - 0.5, tap_v2[1] - 1.05)
        d += elm.Arrow().at(arrow_a_top).to(arrow_a_tip)
        d += elm.Label().at((xs - 1.15, (tap_v2[1] + tap_v1[1]) / 2)).label("$I_a$")
        d += res_ia
        d += elm.Dot().at(tap_v1)
        d += elm.Label().at((xs - 0.95, tap_v1[1] + 0.45)).label("$V_1$")
        res_ib = elm.Resistor().at(tap_v1).to(node_c)
        d += elm.Label().at((xs + 0.6, (tap_v1[1] + node_c[1]) / 2)).label("$R_1$")
        arrow_b_top = (xs - 0.5, tap_v1[1] - 0.25)
        arrow_b_tip = (xs - 0.5, tap_v1[1] - 1.05)
        d += elm.Arrow().at(arrow_b_top).to(arrow_b_tip)
        d += elm.Label().at((xs - 1.15, (tap_v1[1] + node_c[1]) / 2)).label("$I_b$")
        d += res_ib
        d += elm.Dot().at(node_c)

        # lower R2 and its ground, straight down from the bottom output node
        foot = (xs, node_c[1] - 1.9)
        d += elm.Resistor().at(node_c).to(foot)
        d += elm.Label().at((xs + 0.6, (node_c[1] + foot[1]) / 2)).label("$R_2$")
        d += elm.Ground().at(foot)

        # top inverting input: out to the left of the op-amp, then up and in
        x_top_lane = top.in1[0] - 1.2
        d += elm.Line().at(tap_v2).to((x_top_lane, tap_v2[1]))
        d += elm.Line().at((x_top_lane, tap_v2[1])).to((x_top_lane, top.in1[1]))
        d += elm.Line().at((x_top_lane, top.in1[1])).to(top.in1)

        # bottom inverting input: its own lane, clear of the output wire
        x_bot_lane = bottom.in1[0] - 1.5
        d += elm.Line().at(tap_v1).to((x_bot_lane, tap_v1[1]))
        d += elm.Line().at((x_bot_lane, tap_v1[1])).to((x_bot_lane, bottom.in1[1]))
        d += elm.Line().at((x_bot_lane, bottom.in1[1])).to(bottom.in1)

        # bottom output: left at the node's height, then down into the output
        d += elm.Line().at(node_c).to((bottom.out[0], node_c[1]))
        d += elm.Line().at((bottom.out[0], node_c[1])).to(bottom.out)

        # RG on the far right, from the V2 tap to the bottom output node
        rg_x = xs + 2.4
        d += elm.Line().at(tap_v2).to((rg_x, tap_v2[1]))
        d += (
            elm.Resistor()
            .at((rg_x, tap_v2[1]))
            .to((rg_x, node_c[1]))
            .label("$R_G$", loc="right")
        )
        d += elm.Line().at((rg_x, node_c[1])).to(node_c)
        d.save(fspath(output))


def generate_negative_impedance_converter(output: Path) -> None:
    """Op-amp negative impedance converter seen from its input port.

    ``R`` bridges the input node to the output, and the inverting input taps
    the ``R2``/``R1`` divider hung from the output, so the resistance looking
    into the input is a scaled negative copy of ``R1``. That input resistance
    ``R_i`` is drawn as the element the source drives through on the way to
    the input node, and ``I_i`` is the current of the branch reaching it.
    """
    with drawing_context() as d:
        node_p = (-6.4, -0.575)
        source = elm.SourceV().up().at((-6.4, -4.575)).length(1.7)
        d += elm.Label().at((-7.5, -3.725)).label("$V_s$")
        d += source
        d += elm.Ground().at(source.start)
        # the converter presents R_i at its input, so the source drives it
        # through R_i; I_i is the current of that branch into the node
        d += elm.Resistor().at(source.end).to((-6.4, -1.375))
        d += elm.Label().at((-7.15, -2.125)).label("$R_i$")
        i_lead = elm.Line().at((-6.4, -1.375)).to(node_p)
        d += i_lead
        d += elm.CurrentLabel(length=0.9, ofst=0.45).at(i_lead).label("$I_i$")
        d += elm.Dot().at(node_p)
        op = elm.Opamp().right().flip().at((-1.2, -1.2)).anchor("center")
        d += op
        # flipped from the default, the non-inverting input (+) sits on top
        # and takes the node along its own row, while the inverting input
        # below taps the divider; the other wiring would feed back with the
        # wrong sign
        d += elm.Line().at(node_p).to(op.in2)
        # R bridges the node to the output over the top of the triangle, one
        # row below whose corner the triangle's upper corner now sits
        d += elm.Line().at(node_p).to((-6.4, 0.9))
        d += elm.Line().at((-6.4, 0.9)).to((-5.2, 0.9))
        d += elm.Resistor().at((-5.2, 0.9)).to((-3.5, 0.9)).label("$R$", loc="top")
        out_node = (op.out[0] + 2.0, 0.9)
        d += elm.Line().at((-3.5, 0.9)).to(out_node)
        d += elm.Line().at(op.out).to((op.out[0], 0.9))
        d += elm.Dot().at((op.out[0], 0.9))
        d += elm.Dot().at(out_node)
        d += elm.Label().at((out_node[0] + 0.8, out_node[1] + 0.4)).label("$V$")
        d += elm.Resistor().at(out_node).to((out_node[0], -2.0))
        d += elm.Label().at((out_node[0] + 0.55, -0.55)).label("$R_2$")
        tap = (out_node[0], -2.0)
        d += elm.Dot().at(tap)
        d += elm.Resistor().at(tap).to((tap[0], -4.0))
        d += elm.Label().at((tap[0] + 0.55, -3.0)).label("$R_1$")
        d += elm.Ground().at((tap[0], -4.0))
        # the divider taps the inverting input from below: the lane clears
        # the triangle's lower corner by half a unit and rises outside it
        d += elm.Line().at(tap).to((op.out[0], tap[1]))
        d += elm.Line().at((op.out[0], tap[1])).to((op.out[0], tap[1] - 0.95))
        d += (
            elm.Line()
            .at((op.out[0], tap[1] - 0.95))
            .to((op.in1[0] - 1.05, tap[1] - 0.95))
        )
        d += (
            elm.Line()
            .at((op.in1[0] - 1.05, tap[1] - 0.95))
            .to((op.in1[0] - 1.05, op.in1[1]))
        )
        d += elm.Line().at((op.in1[0] - 1.05, op.in1[1])).to(op.in1)
        d.save(fspath(output))


def generate_voltage_to_current_converter(output: Path) -> None:
    """Voltage-to-current converter: a negative impedance converter load-cancelled source.

    The ``R``/op-amp subtree presents ``-R`` at the node ``V1``, cancelling
    the ``R`` that feeds it from ``V_s``, so the load current ``I_L`` is set
    by ``V_s`` and ``R`` alone. The load sits between that node and ground.
    """
    with drawing_context() as d:
        source = (
            elm.SourceV().up().at((-6.4, -2.4)).length(2.4).label("$V_s$", loc="bottom")
        )
        d += source
        d += elm.Ground().at(source.start)
        node_v1 = (-2.2, 0.0)
        d += elm.Resistor().at(source.end).to(node_v1).label("$R$", loc="top")
        d += elm.Dot().at(node_v1)
        d += elm.Label().at((-2.2, 0.55)).label("$V_1$")
        load = elm.RBox(size=(1.2, 1.8)).down().length(1.8).at((-3.6, -1.5))
        d += load
        d += (
            elm.Label()
            .at((load.start[0] - 1.45, (load.start[1] + load.end[1]) / 2))
            .label("$R_L$")
        )
        d += elm.Line().at(load.end).to((load.end[0], -4.2))
        d += elm.Ground().at((load.end[0], -4.2))
        d += elm.CurrentLabel(top=False).at(load).label("$I_L$")
        d += elm.Line().at(node_v1).to((node_v1[0], load.start[1]))
        d += elm.Dot().at((node_v1[0], load.start[1]))
        d += elm.Line().at((node_v1[0], load.start[1])).to(load.start)
        # the converter subtree: R from the node to the output, divider back
        out_node = (2.6, 0.0)
        d += elm.Resistor().at(node_v1).to(out_node).label("$R$", loc="top")
        d += elm.Dot().at(out_node)
        # the output node is the one the analysis puts at twice V1, so the
        # value is written on the node rather than floating beside the wire
        d += (
            elm.Label()
            .at((out_node[0] + 1.25, out_node[1] + 0.32))
            .label("$V_o = 2V_1$")
        )
        op = elm.Opamp().right().flip().at((0.2, -2.6)).anchor("center")
        d += op
        out_trunk = elm.Line().at(op.out).to((out_node[0], op.out[1]))
        d += out_trunk
        d += elm.Line().at(out_trunk.end).to(out_node)
        # flipped: the non-inverting input (+) on top is held at V1 by the
        # node, whose column drops to the + input's row before the lead runs
        # horizontally into the anchor; the inverting input below taps the
        # R1/R1 divider
        d += elm.Line().at(node_v1).to((node_v1[0], op.in2[1]))
        d += elm.Line().at((node_v1[0], op.in2[1])).to(op.in2)
        tap = (out_node[0], -4.85)
        r_div_upper = elm.Resistor().at((out_node[0], op.out[1] - 0.9)).to(tap)
        d += r_div_upper
        d += elm.Line().at(r_div_upper.start).to(out_trunk.end)
        d += (
            elm.Label()
            .at((out_node[0] + 0.65, (op.out[1] - 0.9 + tap[1]) / 2))
            .label("$R_1$")
        )
        d += elm.Dot().at(tap)
        # the inverting-input lead leaves the tap itself, so the upper and
        # lower R1 read as one chain and the dot marks the only branch the
        # divider feeds; the lane drops below the triangle body and enters
        # the input from outside it
        d += elm.Line().at(tap).to((-1.2, tap[1]))
        d += elm.Line().at((-1.2, tap[1])).to((-1.2, op.in1[1]))
        d += elm.Line().at((-1.2, op.in1[1])).to(op.in1)
        d += elm.Resistor().at(tap).to((tap[0], -6.2))
        d += elm.Label().at((tap[0] + 0.65, (tap[1] - 6.2) / 2)).label("$R_1$")
        d += elm.Ground().at((tap[0], -6.2))
        d.save(fspath(output))


def generate_op_amp_current_source(output: Path) -> None:
    """Load-independent op-amp current source with a floating load.

    ``R3`` sets the current into the virtual ground at the inverting input,
    ``R2`` carries it on to the node ``V1``, and ``R1`` returns it to ground;
    the load ``R_L`` sits between the op-amp output and that node, so the
    current it carries does not depend on its resistance.
    """
    with drawing_context() as d:
        source = (
            elm.SourceV().up().at((-8.0, -2.6)).length(2.6).label("$V_s$", loc="bottom")
        )
        d += source
        d += elm.Ground().at(source.start)
        node_p = (-8.0, 0.0)
        d += elm.Line().at(source.end).to(node_p)
        d += elm.Dot().at(node_p)
        op = elm.Opamp().right().at((-1.6, -2.0)).anchor("center")
        d += op
        # the inverting input taps the R3/R2 node from above and the
        # non-inverting input is grounded below, as the course draws it
        d += elm.Line().at(op.in2).left().length(1.0)
        d += elm.Line().at((op.in2[0] - 1.0, op.in2[1])).down().length(1.0)
        d += elm.Ground().at((op.in2[0] - 1.0, op.in2[1] - 1.0))
        d += (
            elm.Resistor()
            .at(node_p)
            .to((node_p[0] + 2.0, 0.0))
            .label("$R_3$", loc="top")
        )
        node_q = (node_p[0] + 2.0, 0.0)
        d += elm.Dot().at(node_q)
        d += elm.Line().at(node_q).to((node_q[0], op.in1[1]))
        d += elm.Line().at((node_q[0], op.in1[1])).to(op.in1)
        node_v1 = (4.6, 0.0)
        d += elm.Resistor().at(node_q).to(node_v1).label("$R_2$", loc="top")
        d += elm.Dot().at(node_v1)
        d += elm.Label().at((node_v1[0] + 0.9, node_v1[1] + 0.35)).label("$V_1$")
        load = elm.RBox(size=(1.6, 1.0)).at((1.2, -2.0)).label("$R_L$", loc="top")
        d += load
        d += elm.Line().at(op.out).to(load.start)
        d += elm.Line().at(load.end).to((load.end[0], -3.7))
        d += elm.Line().at((load.end[0], -3.7)).to((5.9, -3.7))
        d += elm.Line().at((5.9, -3.7)).to((5.9, 0.0))
        d += elm.Line().at((5.9, 0.0)).to(node_v1)
        d += elm.Arrow().at((2.0, -2.85)).to((0.6, -2.85))
        d += elm.Label().at((2.35, -2.85)).label("$I_L$")
        d += (
            elm.Resistor()
            .at(node_v1)
            .to((node_v1[0], -2.6))
            .label("$R_1$", loc="right")
        )
        d += elm.Ground().at((node_v1[0], -2.6))
        d.save(fspath(output))


def _circle_points(radius: float) -> list[tuple[float, float]]:
    """Points around a circle centred on the origin."""
    return [
        (radius * cos(a * pi / 60), radius * sin(a * pi / 60)) for a in range(0, 120)
    ]


def _ellipse_around(
    center: tuple[float, float], rx: float, ry: float
) -> list[tuple[float, float]]:
    """Points around an ellipse centred on ``center``, six degrees apart."""
    return [
        (center[0] + rx * cos(a * pi / 30), center[1] + ry * sin(a * pi / 30))
        for a in range(61)
    ]


def _poly(
    d: Drawing,
    points: list[tuple[float, float]],
    *,
    color: str | None = None,
    linestyle: str | None = None,
) -> None:
    """Add a polyline drawn as chained straight segments."""
    for start, end in zip(points, points[1:]):
        segment = elm.Line().at(start).to(end)
        if color is not None:
            segment = segment.color(color)
        if linestyle is not None:
            segment = segment.linestyle(linestyle)
        d += segment


def generate_inverting_parallel_feedback(output: Path) -> None:
    """Inverting amplifier whose feedback path is a 6 kOhm || 3 kOhm pair."""

    with drawing_context() as d:
        op = (
            elm.Opamp()
            .right()
            .at((0.0, 0.0))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += op
        d += elm.Line().at(op.in2).left().length(1.1)
        d += elm.Line().at((op.in2[0] - 1.1, op.in2[1])).down().length(1.1)
        d += elm.Ground().at((op.in2[0] - 1.1, op.in2[1] - 1.1))
        source = (
            elm.SourceV()
            .up()
            .at((-7.4, -2.2))
            .length(2.825)
            .label("$V_s$", loc="bottom")
        )
        d += source
        d += elm.Ground().at(source.start)
        node_a = (-2.4, op.in1[1])
        d += (
            elm.Resistor()
            .at(source.end)
            .to(node_a)
            .label(r"$1\,\mathrm{k}\Omega$", loc="top")
        )
        d += elm.Dot().at(node_a)
        d += elm.Line().at(node_a).to(op.in1)
        node = (op.out[0] + 2.6, 0.0)
        d += elm.Line().at(op.out).to(node)
        d += elm.Dot().at(node)
        d += elm.Label().at((node[0] + 1.2, 0.0)).label("$V_o$")
        # one trunk rises from the inverting node and one descends from the
        # output node; the two feedback resistors tap them side by side
        d += elm.Line().at(node_a).to((node_a[0], 4.4))
        d += elm.Dot().at((node_a[0], 2.6))
        d += (
            elm.Resistor()
            .at((node_a[0], 2.6))
            .to((node[0], 2.6))
            .label(r"$6\,\mathrm{k}\Omega$", loc="top")
        )
        d += elm.Line().at((node[0], 4.4)).to((node[0], 2.6))
        d += elm.Dot().at((node[0], 2.6))
        d += elm.Line().at((node[0], 2.6)).to(node)
        d += (
            elm.Resistor()
            .at((node_a[0], 4.4))
            .to((node[0], 4.4))
            .label(r"$3\,\mathrm{k}\Omega$", loc="top")
        )
        d.save(fspath(output))


def generate_difference_amplifier_iin_mesh(output: Path) -> None:
    """Difference amplifier with the input mesh I_in = (V2 - V1) / (2 R1).

    The course draws the same four-resistor circuit with a mesh arrow through
    the two matched input resistors: no current enters the op-amp inputs, so
    the pair behaves as 2 R1 in series across the source difference.
    """

    with drawing_context() as d:
        op = (
            elm.Opamp()
            .right()
            .at((0.6, 0.0))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += op
        source_1 = (
            elm.SourceV().up().at((-8.6, -3.1)).length(4.0).label("$V_1$", loc="bottom")
        )
        d += source_1
        d += elm.Ground().at(source_1.start)
        node_a = (-3.4, 1.2)
        d += elm.Resistor().at(source_1.end).to((-3.4, 0.9)).label("$R_1$", loc="top")
        d += elm.Line().at((-3.4, 0.9)).to(node_a)
        d += elm.Dot().at(node_a)
        d += elm.Line().at(node_a).to((-1.4, 1.2))
        d += elm.Line().at((-1.4, 1.2)).to((-1.4, op.in1[1]))
        d += elm.Line().at((-1.4, op.in1[1])).to(op.in1)
        source_2 = (
            elm.SourceV().up().at((-6.8, -3.1)).length(2.0).label("$V_2$", loc="bottom")
        )
        d += source_2
        d += elm.Ground().at(source_2.start)
        node_b = (-3.4, -1.2)
        d += elm.Resistor().at(source_2.end).to((-3.4, -1.1)).label("$R_1$", loc="top")
        d += elm.Line().at((-3.4, -1.1)).to(node_b)
        d += elm.Dot().at(node_b)
        d += elm.Line().at(node_b).to((-1.4, -1.2))
        d += elm.Line().at((-1.4, -1.2)).to((-1.4, op.in2[1]))
        d += elm.Line().at((-1.4, op.in2[1])).to(op.in2)
        d += elm.Resistor().at(node_b).to((-3.4, -2.6))
        d += elm.Label().at((-2.8, -1.9)).label("$R_2$")
        d += elm.Ground().at((-3.4, -2.6))
        node = (op.out[0] + 2.6, 0.0)
        d += elm.Line().at(op.out).to(node)
        d += elm.Dot().at(node)
        d += elm.Label().at((node[0] + 1.0, 0.0)).label("$V_{out}$")
        d += elm.Line().at(node_a).to((node_a[0], 2.4))
        d += elm.Resistor().at((node_a[0], 2.4)).to((node[0], 2.4))
        d += elm.Label().at(((node_a[0] + node[0]) / 2, 2.85)).label("$R_2$")
        d += elm.Line().at((node[0], 2.4)).to(node)
        # the mesh: one loop arrow inside the input loop, as the course
        # draws it, instead of a dashed box that only outlined the region
        # without saying what circulated in it
        d += (
            elm.LoopArrow(direction="ccw", width=1.0, height=1.0)
            .at((-6.0, -0.1))
            .label("$I_{in}$")
            .color(_ANNOT)
        )
        d += elm.Label().at((-5.0, -4.15)).label(r"$I_{in}=\frac{V_2-V_1}{2R_1}$")
        d.save(fspath(output))


def _generate_current_source_design(
    output: Path,
    *,
    feedback: str,
    shunt: str,
    output_voltage: str,
    node_voltage: str,
    caption: str,
    annotate: bool,
) -> None:
    """Op-amp current source with concrete values, as the course checks it."""

    with drawing_context() as d:
        source = (
            elm.SourceV().up().at((-7.6, -2.0)).length(2.0).label("2 V", loc="bottom")
        )
        d += source
        d += elm.Ground().at(source.start)
        node_p = (-7.6, 0.0)
        d += elm.Line().at(source.end).to(node_p)
        d += (
            elm.Resistor()
            .at(node_p)
            .to((-4.6, 0.0))
            .label(r"$100\,\mathrm{k}\Omega$", loc="top")
        )
        node_a = (-4.6, 0.0)
        d += elm.Dot().at(node_a)
        op = (
            elm.Opamp()
            .right()
            .at((-3.0, -1.7))
            .anchor("center")
            .label(r"$\infty$", loc="center")
        )
        d += op
        d += elm.Line().at(node_a).to((op.in1[0], node_a[1]))
        d += elm.Line().at((op.in1[0], node_a[1])).to(op.in1)
        d += elm.Line().at(op.in2).left().length(0.9)
        d += elm.Line().at((op.in2[0] - 0.9, op.in2[1])).down().length(0.9)
        d += elm.Ground().at((op.in2[0] - 0.9, op.in2[1] - 0.9))
        # supply rails, attached to the op-amp body
        d += elm.Line().at((-3.0, -1.0)).to((-3.0, 0.9))
        d += elm.Label().at((-2.75, 1.25)).label("15 V")
        d += elm.Line().at((-3.0, -2.4)).to((-3.0, -3.3))
        d += elm.Label().at((-3.0, -3.65)).label("-15 V")
        # feedback over the top to the load node
        d += elm.Line().at(node_a).to((-4.6, 1.6))
        d += elm.Line().at((-4.6, 1.6)).to((-0.6, 1.6))
        d += elm.Resistor().at((-0.6, 1.6)).to((4.4, 1.6)).label(feedback, loc="top")
        d += elm.Line().at((4.4, 1.6)).to((4.4, 0.0))
        node_v1 = (4.4, 0.0)
        d += elm.Dot().at(node_v1)
        # the load between the op-amp output and that node
        # the load box is four lines, not elm.Rect: schemdraw 0.23 drops a
        # Rect's path when a Line is added after it in the same drawing
        for corner_a, corner_b in (
            ((0.8, -1.25), (0.8, -2.15)),
            ((0.8, -2.15), (3.4, -2.15)),
            ((3.4, -2.15), (3.4, -1.25)),
            ((3.4, -1.25), (0.8, -1.25)),
        ):
            d += elm.Line().at(corner_a).to(corner_b)
        d += elm.Label().at((2.1, -2.5)).label(r"$1\,\mathrm{k}\Omega$")
        d += elm.Line().at(op.out).to((0.8, -1.7))
        # the load's far terminal leaves the edge midpoint and steps out
        # before rising, instead of springing off the box corner
        d += elm.Line().at((3.4, -1.7)).to((4.0, -1.7))
        d += elm.Line().at((4.0, -1.7)).to((4.0, 0.0))
        d += elm.Line().at((4.0, 0.0)).to(node_v1)
        # the shunt resistor back to ground
        d += elm.Resistor().at(node_v1).to((4.4, -3.0))
        d += elm.Label().at((5.35, -1.5)).label(shunt)
        d += elm.Ground().at((4.4, -3.0))
        if annotate:
            # the voltages and currents the course writes on the figure
            d += (
                elm.Label()
                .at((-6.1, -0.42))
                .label(r"$20\,\mu\mathrm{A}$")
                .color(_GREEN)
            )
            d += elm.Label().at((-2.05, -3.15)).label("0 V").color(_GREEN)
            d += elm.Label().at((0.1, -1.0)).label(output_voltage).color(_ANNOT)
            d += elm.Label().at((3.1, 0.62)).label(node_voltage).color(_ANNOT)
            d += elm.Label().at((2.75, -0.75)).label(r"$2\,\mathrm{mA}$").color(_GREEN)
            d += (
                elm.Label()
                .at((-2.55, 2.12))
                .label(r"$20\,\mu\mathrm{A}$")
                .color(_GREEN)
            )
        d += elm.Label().at((0.5, -4.1)).label(caption)
        d.save(fspath(output))


def generate_current_source_design_check(output: Path) -> None:
    """The current-source values whose node voltages break the rails."""

    _generate_current_source_design(
        output,
        feedback=r"$1\,\mathrm{M}\Omega$",
        shunt=r"$10\,\mathrm{k}\Omega$",
        output_voltage="-22 V",
        node_voltage="-20 V",
        caption="design does not work",
        annotate=True,
    )


def generate_current_source_design_improved(output: Path) -> None:
    """The same current source with values that stay inside the rails."""

    _generate_current_source_design(
        output,
        feedback=r"$500\,\mathrm{k}\Omega$",
        shunt=r"$5\,\mathrm{k}\Omega$",
        output_voltage="-12 V",
        node_voltage="-10 V",
        caption="design OK; R_L max 2.5 kOhm",
        annotate=True,
    )


def generate_entry_point_annotated(output: Path) -> None:
    """Two-op-amp circuit solved from an entry point, with every value marked.

    All four op-amp inputs sit at 5 V and draw no current, so the analysis
    starts at the 1 kOhm resistor under the 5 V source and walks the rest of
    the circuit from there. Every wire runs horizontally or vertically, and
    every annotation sits beside the branch it describes.
    """

    with drawing_context() as d:
        y_top = 0.0
        y_rail = -3.5
        x_src = -10.0
        x_vres = -8.0
        x1f = -1.5
        y1o = -0.625
        x_out = 3.0
        y_w = -6.25
        y_gnd = -9.0
        x2f = -2.5
        y2o = -5.625
        node_x = (x_vres, y_rail)
        # node Y taps the rail left of the first op-amp, so the wire into its
        # - input runs up and then across, never along the triangle's edge
        node_y = (x1f - 0.5, y_rail)
        node_z = (x_out, y_rail)
        node_w = (x_out, y_w)

        # the 5 V source, and the wire carrying I_s to the first op-amp's +
        d += elm.SourceV().up().at((x_src, y_rail)).length(y_top - y_rail)
        d += elm.Ground().at((x_src, y_rail))
        d += elm.Label().at((x_src + 0.2, -5.1)).label(r"$*$ entry point")
        d += elm.Label().at((x_src - 1.2, -1.75)).label("5 V")
        d += elm.Line().at((x_src, y_top)).to((x1f, y_top))
        d += elm.Arrow().at((x_src + 1.1, y_top)).to((x_src + 1.9, y_top))
        d += elm.Label().at((x_src + 1.5, y_top + 0.45)).label("$I_s$")

        # the 1 kOhm under the source, the entry point, down to the 0 V node
        d += elm.Dot().at((x_vres, y_top))
        d += elm.Resistor().at((x_vres, y_top)).to(node_x)
        d += elm.Arrow().at((x_vres, y_top - 0.35)).to((x_vres, y_top - 1.15))
        d += elm.Label().at((x_vres + 0.75, y_top - 0.75)).label("5 mA*").color(_GREEN)
        d += elm.Label().at((x_vres + 0.75, -1.9)).label(r"$1\,\mathrm{k}\Omega$")
        d += elm.Dot().at(node_x)
        d += (
            elm.Label()
            .at((node_x[0] - 1.0, node_x[1] + 0.45))
            .label("0 V")
            .color(_GREEN)
        )
        # the second op-amp's output sinks the 10 mA arriving at the 0 V node
        d += elm.Arrow().at((x_vres, y_rail - 0.4)).to((x_vres, y_rail - 1.2))
        d += (
            elm.Label()
            .at((node_x[0] - 1.0, node_x[1] - 0.85))
            .label("10 mA")
            .color(_GREEN)
        )

        # the rail: two 1 kOhm in series, 5 mA each, tapped at node Y
        d += elm.Line().at(node_x).to((-6.5, y_rail))
        d += elm.Resistor().at((-6.5, y_rail)).to((-4.5, y_rail))
        d += elm.Label().at((-5.5, y_rail - 0.7)).label(r"$1\,\mathrm{k}\Omega$")
        d += elm.Arrow().at((-5.15, y_rail + 0.7)).to((-5.85, y_rail + 0.7))
        d += elm.Label().at((-5.5, y_rail + 1.15)).label("5 mA").color(_GREEN)
        d += elm.Line().at((-4.5, y_rail)).to((-1.3, y_rail))
        d += elm.Resistor().at((-1.3, y_rail)).to((0.7, y_rail))
        d += elm.Label().at((-0.3, y_rail - 0.7)).label(r"$1\,\mathrm{k}\Omega$")
        d += elm.Arrow().at((0.05, y_rail + 0.7)).to((-0.65, y_rail + 0.7))
        d += elm.Label().at((-0.3, y_rail + 1.15)).label("5 mA").color(_GREEN)
        d += elm.Line().at((0.7, y_rail)).to(node_z)
        d += elm.Dot().at(node_y)
        d += elm.Dot().at(node_z)

        # the first op-amp: + fed from the source wire, - from node Y
        top = elm.Opamp().flip().at((x1f, y1o)).label(r"$\infty$", loc="center")
        d += top
        d += elm.Line().at(node_y).to((node_y[0], top.in1[1]))
        d += elm.Line().at((node_y[0], top.in1[1])).to(top.in1)
        d += elm.Line().at(top.out).to((x_out, top.out[1]))
        d += elm.Line().at((x_out, top.out[1])).to(node_z)
        d += elm.Label().at((-2.4, y_top + 0.45)).label("5 V").color(_GREEN)
        d += elm.Label().at((-2.4, y_top - 0.45)).label("0 A").color(_ANNOT)
        d += elm.Label().at((-2.6, -1.7)).label("5 V").color(_GREEN)
        d += elm.Label().at((-2.6, -2.6)).label("0 A").color(_ANNOT)
        d += elm.Label().at((x_out + 0.55, top.out[1] - 0.075)).label("$V_o$")

        # the second op-amp: apex left, - from node Y, + from node W,
        # output back up to the 0 V node
        bottom = (
            elm.Opamp().left().flip().at((x2f, y2o)).label(r"$\infty$", loc="center")
        )
        d += bottom
        d += elm.Line().at(node_y).to((node_y[0], bottom.in1[1]))
        d += elm.Line().at((node_y[0], bottom.in1[1])).to(bottom.in1)
        d += elm.Label().at((-1.4, bottom.in1[1] + 0.4)).label("0 A").color(_ANNOT)
        d += elm.Label().at((-1.4, bottom.in1[1] - 0.4)).label("5 V").color(_GREEN)
        d += elm.Line().at(node_w).to(bottom.in2)
        d += elm.Label().at((0.6, bottom.in2[1] - 0.45)).label("5 V").color(_GREEN)
        d += elm.Label().at((0.6, bottom.in2[1] - 1.0)).label("0 A").color(_ANNOT)
        d += elm.Line().at(bottom.out).to((x_vres, bottom.out[1]))
        d += elm.Line().at((x_vres, bottom.out[1])).to(node_x)

        # the output column: node Z down to node W, and on to ground
        d += elm.Resistor().at(node_z).to(node_w)
        d += elm.Arrow().at((x_out, y_rail - 0.2)).to((x_out, y_rail - 0.8))
        d += elm.Label().at((x_out + 0.9, y_rail - 0.5)).label("10 V").color(_GREEN)
        d += elm.Label().at((x_out + 0.9, y_rail - 1.1)).label("10 mA").color(_GREEN)
        d += elm.Label().at((x_out - 0.9, y_rail - 1.4)).label(r"$1\,\mathrm{k}\Omega$")
        d += elm.Resistor().at(node_w).to((x_out, y_gnd))
        d += elm.Dot().at(node_w)
        d += elm.Label().at((x_out + 0.9, y_w + 0.4)).label("5 V").color(_GREEN)
        d += elm.Arrow().at((x_out, y_gnd + 0.65)).to((x_out, y_gnd + 0.1))
        d += elm.Label().at((x_out + 0.9, y_gnd + 0.4)).label(r"$1\,\mathrm{k}\Omega$")
        d += elm.Label().at((x_out + 0.9, y_gnd - 0.5)).label("5 mA").color(_GREEN)
        d += elm.Ground().at((x_out, y_gnd))
        d.save(fspath(output))


def generate_plate_capacitor_geometry(output: Path) -> None:
    """Parallel-plate capacitor: two plates, the dielectric, the field, the
    voltage."""

    with drawing_context() as d:
        # the dielectric slab first so the plates and charges draw over it
        plate_box = elm.Rect(corner1=(0.05, 0.9), corner2=(2.55, -0.9))
        d += plate_box.at((0.0, 0.0)).fill("#e6e6e6").linestyle("--")
        d += elm.Line().at((0.0, 1.0)).to((2.6, 1.0)).linewidth(3)
        d += elm.Line().at((0.0, -1.0)).to((2.6, -1.0)).linewidth(3)
        # the field arrows inside the dielectric
        for x in (0.7, 1.3, 1.9):
            d += elm.Arrow().at((x, 0.6)).to((x, -0.6)).color(_ANNOT)
        d += elm.Label().at((0.2, 0.0)).label("$E$").color(_ANNOT)
        # the bound charge rows on the inner faces
        for x in (0.45, 0.9, 1.35, 1.8, 2.2):
            d += elm.Label().at((x, 1.42)).label("+")
            d += elm.Label().at((x, -1.42)).label("-")
        # the source from the lower plate back to the upper plate, with
        # its terminals on the two lead rows so every lead is straight
        source = elm.SourceV().up().at((-3.6, -1.5)).length(3.0)
        d += source
        d += elm.Label().at((-5.0, 0.0)).label("$V$")
        d += elm.Ground().at(source.start)
        d += elm.Line().at(source.start).to((0.0, -1.5))
        d += elm.Line().at((0.0, -1.5)).to((0.0, -1.0))
        d += elm.Line().at(source.end).to((0.0, 1.5))
        d += elm.Line().at((0.0, 1.5)).to((0.0, 1.0))
        d += elm.Label().at((1.3, -2.05)).label("Dielectric")
        d += elm.Label().at((1.3, 2.05)).label("Metal plates")
        d += elm.Label().at((4.5, 1.0)).label(r"$+Q$")
        d += elm.Label().at((4.5, -1.0)).label(r"$-Q$")
        d += elm.Line().at((2.75, 1.0)).to((4.0, 1.0))
        d += elm.Line().at((2.75, -1.0)).to((4.0, -1.0))
        d.save(fspath(output))


def generate_symbol_capacitor(output: Path) -> None:
    """Capacitor symbol: two parallel plates across the branch."""

    with drawing_context() as d:
        d += elm.Line().at((0.0, 2.2)).to((0.0, 0.25))
        d += elm.Line().at((-0.9, 0.25)).to((0.9, 0.25)).linewidth(3)
        d += elm.Line().at((-0.9, -0.25)).to((0.9, -0.25)).linewidth(3)
        d += elm.Line().at((0.0, -0.25)).to((0.0, -2.2))
        d += elm.Arrow().at((0.85, 1.9)).to((0.85, 1.1))
        d += elm.Label().at((1.35, 1.5)).label(r"$i_C(t)$")
        d += elm.Label().at((1.5, 0.55)).label("+")
        d += elm.Label().at((1.5, -0.55)).label("-")
        d += elm.Label().at((1.9, 0.0)).label(r"$v_C(t)$")
        d += elm.Label().at((-1.4, 0.0)).label("$C$")
        d.save(fspath(output))


def generate_symbol_inductor(output: Path) -> None:
    """Inductor symbol: a coil in the branch."""

    with drawing_context() as d:
        d += elm.Line().at((0.0, 2.2)).to((0.0, 0.9))
        d += elm.Inductor(segments=4).down().at((0.0, 0.9)).length(1.8)
        d += elm.Label().at((-1.3, 0.0)).label("$L$")
        d += elm.Line().at((0.0, -0.9)).to((0.0, -2.2))
        d += (
            elm.Arrow()
            .at((0.75, 1.9))
            .to((0.75, 1.1))
            .label(r"$i_\ell(t)$", loc="right")
        )
        d += elm.Label().at((1.45, 0.6)).label("+")
        d += elm.Label().at((1.45, -0.6)).label("-")
        d += elm.Label().at((1.85, 0.0)).label(r"$v_\ell(t)$")
        d.save(fspath(output))


def generate_transformer_ideal(output: Path) -> None:
    """Ideal transformer: two dotted coils on one core, source and load."""

    with drawing_context() as d:
        source = elm.SourceSin().up().at((-6.0, -1.6)).length(3.2)
        d += source
        d += elm.Ground().at(source.start)
        d += elm.Line().at(source.end).to((-2.6, 1.6))
        d += elm.Arrow().at((-5.2, 2.1)).to((-4.0, 2.1)).label(r"$I_p$", loc="right")
        d += elm.Label().at((-4.4, 0.6)).label("+")
        d += elm.Label().at((-4.4, -0.6)).label("-")
        d += elm.Label().at((-5.0, 0.0)).label("$V_p$")
        d += elm.Inductor(segments=5).down().at((-2.6, 1.6)).length(3.2)
        # the dot of each winding marks the same end on the side clear of
        # its own turns, so it reads as that winding's dotted terminal
        d += elm.Dot().at((-2.95, 1.25))
        d += elm.Line().at((-2.6, -1.6)).to(source.start)
        # the shared core
        d += elm.Line().at((-1.8, 1.9)).to((-1.8, -1.9))
        d += elm.Line().at((-1.4, 1.9)).to((-1.4, -1.9))
        d += elm.Inductor(segments=5).down().at((-1.0, 1.6)).length(3.2)
        d += elm.Dot().at((-0.65, 1.25))
        d += elm.Line().at((-1.0, -1.6)).to((1.8, -1.6))
        d += elm.Line().at((-1.0, 1.6)).to((1.8, 1.6))
        d += elm.Arrow().at((0.0, 2.1)).to((0.9, 2.1)).label(r"$I_s$", loc="right")
        d += elm.Label().at((0.4, 0.6)).label("+")
        d += elm.Label().at((0.4, -0.6)).label("-")
        d += elm.Label().at((-0.1, 0.0)).label("$V_s$")
        d += (
            elm.Resistor().down().at((1.8, 1.6)).length(3.2).label("$Z_L$", loc="right")
        )
        d += elm.Label().at((-1.8, 2.9)).label(r"$N_p:N_s$")
        d.save(fspath(output))


def generate_symbol_source_ac(output: Path) -> None:
    """AC source symbol: a circle carrying one cycle of a sinusoid."""

    with drawing_context() as d:
        source = elm.SourceSin().up().at((0.0, -0.8)).length(1.6)
        d += source
        d += elm.Label().at((1.35, 0.55)).label("+")
        d += elm.Label().at((1.35, -0.55)).label("-")
        d += elm.Label().at((1.75, 0.0)).label(r"$v_s(t)$")
        d.save(fspath(output))


def generate_phasor_rotating_vector(output: Path) -> None:
    """A phasor on the complex plane: rotating vector and projection."""

    with drawing_context() as d:
        d += elm.Line().at((-3.2, 0.0)).to((3.6, 0.0))
        d += elm.Arrow().at((3.6, 0.0)).to((4.3, 0.0))
        d += elm.Label().at((4.8, 0.0)).label(r"$\mathrm{Re}$")
        d += elm.Line().at((0.0, -2.8)).to((0.0, 2.8))
        d += elm.Arrow().at((0.0, 2.8)).to((0.0, 3.5))
        d += elm.Label().at((0.6, 3.5)).label(r"$\mathrm{Im}$")
        _poly(d, _circle_points(2.0), linestyle="--", color="#999999")
        tip = (2.0 * cos(pi / 3), 2.0 * sin(pi / 3))
        d += elm.Arrow().at((0.0, 0.0)).to(tip).label(r"$\vec{z}$", loc="right")
        # the angle from the real axis
        arc = [
            (0.7 * cos(a * pi / 180), 0.7 * sin(a * pi / 180)) for a in range(8, 61, 4)
        ]
        _poly(d, arc)
        d += elm.Label().at((0.35, 1.2)).label(r"$\theta$")
        # projection of the tip on both axes
        d += elm.Line().at(tip).to((tip[0], 0.0)).linestyle("--")
        d += elm.Line().at(tip).to((0.0, tip[1])).linestyle("--")
        d += elm.Dot().at((tip[0], 0.0))
        d += elm.Dot().at((0.0, tip[1]))
        d += elm.Label().at((tip[0], -0.4)).label("$x$")
        d += elm.Label().at((-0.35, tip[1] - 0.10)).label("$y$")
        d += elm.Label().at((2.6, 2.5)).label(r"$\omega$")
        d.save(fspath(output))


def generate_complex_plane(output: Path) -> None:
    """Complex number on the plane: rectangular components and polar form."""

    with drawing_context() as d:
        d += elm.Line().at((-1.0, 0.0)).to((4.2, 0.0))
        d += elm.Arrow().at((4.2, 0.0)).to((4.9, 0.0))
        d += elm.Label().at((5.4, 0.0)).label(r"$\mathrm{Re}$")
        d += elm.Line().at((0.0, -0.8)).to((0.0, 3.2))
        d += elm.Arrow().at((0.0, 3.2)).to((0.0, 3.9))
        d += elm.Label().at((0.6, 3.9)).label(r"$\mathrm{Im}$")
        z = (2.8, 1.9)
        d += elm.Arrow().at((0.0, 0.0)).to(z).label(r"$z = a + j b$", loc="right")
        d += elm.Line().at(z).to((z[0], 0.0)).linestyle("--")
        d += elm.Line().at(z).to((0.0, z[1])).linestyle("--")
        d += elm.Dot().at(z)
        d += elm.Dot().at((z[0], 0.0))
        d += elm.Dot().at((0.0, z[1]))
        d += elm.Label().at((z[0] / 2, -0.38)).label("$a$")
        d += elm.Label().at((-0.5, z[1] / 2)).label(r"$j b$")
        arc = [
            (0.85 * cos(a * pi / 180), 0.85 * sin(a * pi / 180))
            for a in range(8, 35, 4)
        ]
        _poly(d, arc)
        d += elm.Label().at((1.15, 0.3)).label(r"$\theta$")
        d += elm.Label().at((1.15, 1.5)).label(r"$r = |z|$")
        d.save(fspath(output))


def generate_unit_circle_common_values(output: Path) -> None:
    """The unit circle with the exponentials the course uses by heart."""

    with drawing_context() as d:
        _poly(d, _circle_points(2.0))
        d += elm.Line().at((-2.6, 0.0)).to((2.9, 0.0))
        d += elm.Line().at((0.0, -2.6)).to((0.0, 2.9))
        rays = (
            (0, "1", r"$0$", (2.5, -0.35), (1.35, -0.35)),
            (
                30,
                r"$\frac{\sqrt{3}}{2}+j\frac{1}{2}$",
                r"$\frac{\pi}{6}$",
                (3.0, 1.15),
                (1.5, 0.40),
            ),
            (
                45,
                r"$\frac{\sqrt{2}}{2}+j\frac{\sqrt{2}}{2}$",
                r"$\frac{\pi}{4}$",
                (1.95, 2.05),
                (0.75, 1.15),
            ),
            (90, r"$j$", r"$\frac{\pi}{2}$", (0.5, 2.35), (-0.75, 1.35)),
            (180, r"$-1$", r"$\pi$", (-2.35, 0.5), (-1.35, 0.6)),
            (270, r"$-j$", r"$\frac{3\pi}{2}$", (0.55, -2.35), (0.35, -1.5)),
        )
        for angle, value, tick, at_value, at_tick in rays:
            theta = angle * pi / 180
            tip = (2.0 * cos(theta), 2.0 * sin(theta))
            d += elm.Line().at((0.0, 0.0)).to(tip).color(_GREEN)
            d += elm.Dot().at(tip)
            d += elm.Label().at(at_value).label(value)
            d += elm.Label().at(at_tick).label(tick)
        d += elm.Label().at((0.0, 3.62)).label(r"$e^{j\theta}$ on the unit circle")
        d.save(fspath(output))


def generate_phasor_diagram_addition(output: Path) -> None:
    """Phasor addition: two vectors placed head to tail, the sum drawn from
    the origin."""

    with drawing_context() as d:
        d += elm.Line().at((-1.0, 0.0)).to((5.6, 0.0))
        d += elm.Arrow().at((5.6, 0.0)).to((6.3, 0.0))
        d += elm.Label().at((6.8, 0.0)).label(r"$\mathrm{Re}$")
        d += elm.Line().at((0.0, -0.8)).to((0.0, 3.4))
        d += elm.Arrow().at((0.0, 3.4)).to((0.0, 4.1))
        d += elm.Label().at((0.6, 4.1)).label(r"$\mathrm{Im}$")
        a_tip = (2.4, 1.0)
        c_tip = (4.4, 2.6)
        d += elm.Arrow().at((0.0, 0.0)).to(a_tip)
        # each name sits just off its own arrow, on the side of that arrow
        # that the other two arrows leave free
        d += elm.Label().at((2.1, 0.44)).label(r"$\vec{A}$")
        d += elm.Arrow().at(a_tip).to(c_tip)
        d += elm.Label().at((3.55, 1.15)).label(r"$\vec{B}$")
        d += elm.Arrow().at((0.0, 0.0)).to(c_tip).color(_ANNOT)
        d += elm.Label().at((2.3, 2.2)).label(r"$\vec{C}=\vec{A}+\vec{B}$")
        d += elm.Dot().at(a_tip)
        d += elm.Dot().at(c_tip)
        d.save(fspath(output))


def generate_impedance_diagram(output: Path) -> None:
    """Impedance diagram: resistance on the real axis, inductive reactance
    up, the resultant impedance."""

    with drawing_context() as d:
        d += elm.Line().at((-0.6, 0.0)).to((4.0, 0.0))
        d += elm.Arrow().at((4.0, 0.0)).to((4.7, 0.0))
        d += elm.Label().at((5.2, 0.0)).label(r"$\mathrm{Re}$")
        d += elm.Line().at((0.0, -1.4)).to((0.0, 3.4))
        d += elm.Arrow().at((0.0, 3.4)).to((0.0, 4.1))
        d += elm.Label().at((0.6, 4.1)).label(r"$\mathrm{Im}$")
        d += elm.Arrow().at((0.0, 0.0)).to((2.8, 0.0)).label("$R$", loc="bottom")
        d += elm.Arrow().at((2.8, 0.0)).to((2.8, 2.2))
        d += elm.Label().at((3.2, 2.2)).label(r"$jX_L$")
        d += elm.Arrow().at((0.0, 0.0)).to((2.8, 2.2)).color(_ANNOT)
        d += elm.Label().at((1.0, 1.65)).label("$Z$").color(_ANNOT)
        arc = [
            (0.9 * cos(a * pi / 180), 0.9 * sin(a * pi / 180)) for a in range(8, 39, 4)
        ]
        _poly(d, arc)
        d += elm.Label().at((1.55, 0.45)).label(r"$\theta$")
        d += elm.Label().at((3.6, -1.1)).label(r"$Z = R + jX_L$")
        d.save(fspath(output))


def generate_admittance_diagram(output: Path) -> None:
    """Admittance diagram: conductance on the real axis, the susceptance of an
    inductor below it, the resultant admittance."""

    with drawing_context() as d:
        d += elm.Line().at((-0.6, 0.0)).to((4.0, 0.0))
        d += elm.Arrow().at((4.0, 0.0)).to((4.7, 0.0))
        d += elm.Label().at((5.2, 0.0)).label(r"$\mathrm{Re}$")
        d += elm.Line().at((0.0, -3.4)).to((0.0, 1.4))
        d += elm.Arrow().at((0.0, 1.4)).to((0.0, 2.1))
        d += elm.Label().at((0.6, 2.1)).label(r"$\mathrm{Im}$")
        d += elm.Arrow().at((0.0, 0.0)).to((2.8, 0.0)).label("$G$", loc="top")
        d += elm.Arrow().at((2.8, 0.0)).to((2.8, -2.2))
        d += elm.Label().at((3.25, -2.2)).label(r"$jB$")
        d += elm.Arrow().at((0.0, 0.0)).to((2.8, -2.2)).color(_ANNOT)
        d += elm.Label().at((1.35, -1.5)).label("$Y$").color(_ANNOT)
        arc = [
            (0.9 * cos(a * pi / 180), 0.9 * sin(a * pi / 180))
            for a in range(-38, -7, 4)
        ]
        _poly(d, arc)
        d += elm.Label().at((1.55, -0.5)).label(r"$-\theta$")
        d += elm.Label().at((3.6, 1.2)).label(r"$Y = G + jB$")
        d.save(fspath(output))


def generate_rms_waveform(output: Path) -> None:
    """A sinusoid with its peak, its RMS level, and its period marked."""

    with drawing_context() as d:
        period = 6.0
        amplitude = 1.4
        d += elm.Line().at((-0.8, 0.0)).to((13.0, 0.0))
        d += elm.Arrow().at((13.0, 0.0)).to((13.8, 0.0))
        d += elm.Label().at((14.4, 0.0)).label("$t$")
        d += elm.Line().at((0.0, -2.4)).to((0.0, 2.4))
        d += elm.Arrow().at((0.0, 2.4)).to((0.0, 3.0))
        d += elm.Label().at((0.6, 3.0)).label("$v(t)$")
        # two periods across the marked span, so the T bracket is one
        curve = [
            (2 * period * t / 500, amplitude * sin(2 * pi * 2 * t / 500))
            for t in range(0, 501)
        ]
        _poly(d, curve, color=_ANNOT)
        d += elm.Line().at((0.0, amplitude)).to((12.0, amplitude)).linestyle("--")
        d += elm.Label().at((12.6, amplitude)).label("$V_p$")
        d += elm.Line().at((0.0, -amplitude)).to((12.0, -amplitude)).linestyle("--")
        d += elm.Label().at((12.6, -amplitude)).label(r"$-V_p$")
        rms = amplitude / 2**0.5
        d += elm.Line().at((0.0, rms)).to((12.0, rms)).linestyle(":")
        d += elm.Label().at((4.0, 0.44)).label(r"$V_{rms}=\frac{V_p}{\sqrt{2}}$")
        d += elm.Line().at((0.0, -2.1)).to((period, -2.1))
        d += elm.Label().at((period / 2, -2.55)).label("$T$")
        d += elm.Dot().at((0.0, 0.0))
        d += elm.Dot().at((period, 0.0))
        d.save(fspath(output))


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
        (generate_op_amp_symbol, outdir_path / "op_amp_symbol.svg"),
        (generate_op_amp_circuit_model, outdir_path / "op_amp_circuit_model.svg"),
        (
            generate_op_amp_transfer_characteristic,
            outdir_path / "op_amp_transfer_characteristic.svg",
        ),
        (generate_feedback_loop, outdir_path / "feedback_loop.svg"),
        (generate_oscillator_loop, outdir_path / "oscillator_loop.svg"),
        (generate_schmitt_hysteresis, outdir_path / "schmitt_hysteresis.svg"),
        (
            generate_feedback_one_solution,
            outdir_path / "feedback_one_solution.svg",
        ),
        (
            generate_feedback_three_solutions,
            outdir_path / "feedback_three_solutions.svg",
        ),
        (generate_amplifier_loading, outdir_path / "amplifier_loading.svg"),
        (generate_buffer_amplifier, outdir_path / "buffer_amplifier.svg"),
        (
            generate_non_inverting_amplifier,
            outdir_path / "non_inverting_amplifier.svg",
        ),
        (generate_schmitt_trigger, outdir_path / "schmitt_trigger.svg"),
        (generate_inverting_amplifier, outdir_path / "inverting_amplifier.svg"),
        (generate_summing_amplifier, outdir_path / "summing_amplifier.svg"),
        (generate_dac_converter, outdir_path / "dac_converter.svg"),
        (generate_flash_adc, outdir_path / "flash_adc.svg"),
        (generate_difference_amplifier, outdir_path / "difference_amplifier.svg"),
        (
            generate_instrumentation_amplifier,
            outdir_path / "instrumentation_amplifier.svg",
        ),
        (
            generate_instrumentation_amplifier_single_ended,
            outdir_path / "instrumentation_amplifier_single_ended.svg",
        ),
        (
            generate_negative_impedance_converter,
            outdir_path / "negative_impedance_converter.svg",
        ),
        (
            generate_voltage_to_current_converter,
            outdir_path / "voltage_to_current_converter.svg",
        ),
        (
            generate_op_amp_current_source,
            outdir_path / "op_amp_current_source.svg",
        ),
        (
            generate_inverting_parallel_feedback,
            outdir_path / "inverting_parallel_feedback.svg",
        ),
        (generate_integrator, outdir_path / "integrator.svg"),
        (generate_differentiator, outdir_path / "differentiator.svg"),
        (
            generate_difference_amplifier_iin_mesh,
            outdir_path / "difference_amplifier_iin_mesh.svg",
        ),
        (
            generate_current_source_design_check,
            outdir_path / "current_source_design_check.svg",
        ),
        (
            generate_current_source_design_improved,
            outdir_path / "current_source_design_improved.svg",
        ),
        (
            generate_entry_point_annotated,
            outdir_path / "entry_point_annotated.svg",
        ),
        (
            generate_plate_capacitor_geometry,
            outdir_path / "plate_capacitor_geometry.svg",
        ),
        (generate_symbol_capacitor, outdir_path / "symbol_capacitor.svg"),
        (generate_symbol_inductor, outdir_path / "symbol_inductor.svg"),
        (generate_transformer_ideal, outdir_path / "transformer_ideal.svg"),
        (generate_symbol_source_ac, outdir_path / "symbol_source_ac.svg"),
        (
            generate_phasor_rotating_vector,
            outdir_path / "phasor_rotating_vector.svg",
        ),
        (generate_complex_plane, outdir_path / "complex_plane.svg"),
        (
            generate_unit_circle_common_values,
            outdir_path / "unit_circle_common_values.svg",
        ),
        (
            generate_phasor_diagram_addition,
            outdir_path / "phasor_diagram_addition.svg",
        ),
        (generate_impedance_diagram, outdir_path / "impedance_diagram.svg"),
        (generate_rms_waveform, outdir_path / "rms_waveform.svg"),
        (generate_admittance_diagram, outdir_path / "admittance_diagram.svg"),
    ]

    with Pool(processes=_MAX_POOL_WORKERS) as pool:
        pool.map(_run_generator, generators)


def __main__():
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
