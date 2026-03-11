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
# ///
"""Generate SVG circuit diagrams for the ELEC 1100 lecture notes.

This module uses :mod:`schemdraw` to create a set of simple circuit
illustrations referenced throughout the course material.  The current
collection covers:

* a closed series loop (source plus three resistors);
* a parallel resistor network with a single source;
* a four‑branch KCL node;
* a KVL loop annotated with a mesh arrow;
* the two‑branch 5 V/50–75–25 worked‑example circuit; and
* a symmetric bridge network with two sources;
* basic component symbols (resistor, capacitor, diode, Zener, NPN/PNP);
* BJT equivalent circuits (NPN and PNP: diode plus dependent current source); and
* a few small application circuits used in ELEC 1100 (series diode + resistor,
  Zener clamp regulator, NPN low-side switch, and a 3‑pin regulator with
  bypass capacitors).

Application circuits use a consistent style: either built ground-up (e.g. diode–
resistor loop, Zener clamp) or with the main component placed first and branches
attached via ``.at()``; voltage sources use ``.reverse()`` where needed for polarity.

Outputs are written as SVG files into the ``attachments`` directory next
to the script so they can be committed to version control.  Running the
module without arguments generates diagrams in place; the optional
``outdir`` parameter exists only for testing.

The generator is intentionally minimal and deterministic.  There are no
unit tests by design; this comment documents that fact for future
maintainers.

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
from os import cpu_count, fspath

import matplotlib.pyplot as plt
import schemdraw.elements as elm
from anyio import Path
from asyncer import runnify
from schemdraw import Drawing

# cap worker count to avoid overloading the machine (matplotlib is process-heavy)
_MAX_POOL_WORKERS = min(4, cpu_count() or 1)


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


def generate_series_resistor(output: Path) -> None:
    """Draw a closed series circuit with a voltage source and three resistors.

    This version replaces an earlier open‑loop sketch.  A source is placed
    on the left, followed by two resistors along the top branch.  A third
    resistor on the right side completes the series chain back to the
    source.  No mesh arrow is included here; that appearance is handled by
    :func:`generate_kvl_loop`.
    """
    with drawing_context() as d:
        # left vertical source, top branch has two resistors, right branch
        # consists of a third resistor which closes the loop; bottom horizontal
        # wire returns to the source negative terminal.
        d += elm.SourceV().up().label("V")
        d += elm.Resistor().right().label("R1")
        d += elm.Resistor().down().label("R2")
        d += elm.Resistor().left().label("R3")  # back to source bottom
        d.save(fspath(output))


def generate_parallel_resistor(output: Path) -> None:
    """Draw a voltage source supplying two resistors connected in parallel.

    Earlier notes included just the pair of resistors; here the source and
    both the upper and lower rails are added to make the topology clear.  A
    horizontal return wire ties the bottoms of the two branches together
    and leads back to the source negative terminal.
    """
    with drawing_context() as d:
        # source on left, run right to the top junction node
        d += elm.SourceV().up().label("V")
        d += elm.Line().right(2)
        # first parallel branch: down through R1 and return toward the source
        d.push()
        d += elm.Resistor().down().label("R1")
        d += elm.Line().left(2)
        d.pop()
        # second branch from the same top node
        d += elm.Line().right(2)
        d += elm.Resistor().down().label("R2")
        # complete bottom rail back to source negative
        d += elm.Line().left(4)
        d.save(fspath(output))


def generate_kcl_node(output: Path) -> None:
    """Illustrate Kirchhoff's current law using a four‑branch junction node.

    A dot marks the junction; arrows depict two currents entering (I1 from
    the left, I2 from the right) and two leaving (I3 upward, I4 downward).
    The figure accompanies the discussion of the junction rule in the
    lecture notes.
    """
    with drawing_context() as d:
        d += elm.Dot()
        d.push()
        d.move(-2, 0)
        d += elm.Arrow().right(2).label("I1")
        d.pop()
        d.push()
        d.move(2, 0)
        d += elm.Arrow().left(2).label("I2")
        d.pop()
        d.push()
        d += elm.Arrow().up(2).label("I3")
        d.pop()
        d.push()
        d += elm.Arrow().down(2).label("I4")
        d.pop()
        d.save(fspath(output))


def generate_kvl_loop(output: Path) -> None:
    """Closed series loop containing a source and two resistors, with a mesh
    arrow to indicate the direction used when writing KVL equations.
    """
    with drawing_context() as d:
        d += elm.SourceV().up().label("V")
        d += elm.Resistor().right().label("R1")
        d += elm.Resistor().down().label("R2")
        d += elm.Line().left().label("R3")
        # add a mesh arrow to indicate current/voltage traversal direction
        d += elm.LoopArrow(direction="ccw").at((1.5, 1.5)).label("loop")
        d.save(fspath(output))


def generate_two_branch(output: Path) -> None:
    """Circuit showing a 5 V source supplying two parallel branches.  The left
    branch has two series resistors (R1 = 50 Ω, R2 = 75 Ω) while the right
    branch is a single 25 Ω resistor R3.  This configuration mirrors the
    sample problem discussed in lecture.
    """
    with drawing_context() as d:
        # source on the left, creating a top junction node
        d += elm.SourceV().up().label("5V")
        # move rightwards to start the left branch components
        d += elm.Line().right(2)
        d.push()
        d += elm.Resistor().right().label("R1\n50Ω")
        d += elm.Resistor().down().label("R2\n75Ω")
        # close bottom rail back to the source negative terminal
        d += elm.Line().left(5)
        # return to the top junction and draw downward branch R3
        d.pop()
        d += elm.Resistor().down().label("R3\n25Ω")
        d += elm.Ground()
        d.save(fspath(output))


def generate_bridge_two_sources(output: Path) -> None:
    """Bridge‑style circuit with two independent sources and a central resistor.

    A 6 V source with a 2 Ω series resistor forms the left loop; a 10 V
    source with a 2 Ω resistor forms the right loop (source drawn with
    ``.reverse()``).  The central 1 Ω resistor sits between the top and
    bottom rails and carries the sum of the two loop currents, giving
    rise to the $(I_1+I_2)$ term in the KVL equations discussed in class.
    """
    with drawing_context() as d:
        d += elm.Dot().label("X")  # centre node reference for analysis

        # left loop
        d += elm.Resistor().down().label("1Ω")
        d += elm.Ground()
        d += elm.Line().left()
        d += elm.SourceV().up().label("6V")
        d += elm.Resistor().right().label("2Ω")

        # right loop
        d += elm.SourceV().right().reverse().label("10V")
        d += elm.Resistor().down().label("2Ω")
        d += elm.Line().left()

        d.save(fspath(output))


def generate_symbol_resistor(output: Path) -> None:
    """Single resistor symbol with terminals."""
    with drawing_context() as d:
        d += elm.Resistor().right().label("R")
        d.save(fspath(output))


def generate_symbol_capacitor(output: Path) -> None:
    """Single capacitor symbol with terminals."""
    with drawing_context() as d:
        d += elm.Capacitor().right().label("C")
        d.save(fspath(output))


def generate_symbol_diode(output: Path) -> None:
    """Single diode symbol with anode and cathode dots and labels."""
    with drawing_context() as d:
        d += elm.Dot().label("anode")
        d += elm.Line().right(0.5)
        d += elm.Diode().right().label("diode")
        d += elm.Line().right(0.5)
        d += elm.Dot().label("cathode")
        d.save(fspath(output))


def generate_symbol_zener(output: Path) -> None:
    """Single Zener diode symbol."""
    with drawing_context() as d:
        d += elm.Zener().right().label("Zener")
        d.save(fspath(output))


def generate_symbol_voltage_source(output: Path) -> None:
    """Single DC voltage source/battery symbol."""
    with drawing_context() as d:
        d += elm.SourceV().right().label("$V$")
        d.save(fspath(output))


def generate_symbol_ground(output: Path) -> None:
    """Ground symbol."""
    with drawing_context() as d:
        d += elm.Ground()
        d.save(fspath(output))


def generate_symbol_npn(output: Path) -> None:
    """NPN BJT symbol (circle=True) with B/C/E terminals via .at() and short lines."""
    with drawing_context() as d:
        bjt = elm.BjtNpn(circle=True).label("NPN")
        d += bjt
        d += elm.Line().length(0.5).at(bjt.base).left().label("B")
        d += elm.Line().length(0.5).at(bjt.collector).up().label("C")
        d += elm.Line().length(0.5).at(bjt.emitter).down().label("E")
        d.save(fspath(output))


def generate_symbol_pnp(output: Path) -> None:
    """PNP BJT symbol (circle=True) with B/C/E terminals via .at() and short lines."""
    with drawing_context() as d:
        bjt = elm.BjtPnp(circle=True).label("PNP")
        d += bjt
        d += elm.Line().length(0.5).at(bjt.base).left().label("B")
        d += elm.Line().length(0.5).at(bjt.collector).down().label("C")
        d += elm.Line().length(0.5).at(bjt.emitter).up().label("E")
        d.save(fspath(output))


def generate_equivalent_npn(output: Path) -> None:
    """NPN BJT equivalent: C–E path with dependent current source β·I_B, B–E diode from emitter to base.

    Collector at top; controlled current source down; push() to hold the node below it;
    line down to emitter E. Pop to that node; add B–E diode left with .reverse() (anode at B,
    cathode at E); then base dot B.
    """
    with drawing_context() as d:
        d += elm.Dot().label("C")
        d += elm.SourceControlledI().down().label(r"$\beta I_B$")
        d.push()
        d += elm.Line().down()
        d += elm.Dot().label("E", loc="bottom")

        d.pop()
        d += elm.Diode().left().reverse().label("B–E")
        d += elm.Dot().label("B")

        d.save(fspath(output))


def generate_equivalent_pnp(output: Path) -> None:
    """PNP BJT equivalent: E–C path with dependent current source β·I_B, E–B diode from emitter to base.

    Emitter E at top; line down; push() to hold the node below it; controlled current source
    down to collector C. Pop to that node; add E–B diode left (anode at E, cathode at B);
    then base dot B.
    """
    with drawing_context() as d:
        d += elm.Dot().label("E")
        d += elm.Line().down()
        d.push()
        d += elm.SourceControlledI().down().label(r"$\beta I_B$")
        d += elm.Dot().label("C", loc="bottom")

        d.pop()
        d += elm.Diode().left().label("E–B")
        d += elm.Dot().label("B")

        d.save(fspath(output))


def generate_series_diode_resistor(output: Path) -> None:
    """Series source–resistor–diode loop (common intro analysis).

    Built ground-up: GND – V_S up – R right – diode down – line left to close.
    """
    with drawing_context() as d:
        d += elm.Ground()
        d += elm.SourceV().up().label("$V_S$")
        d += elm.Resistor().right().label("R")
        d += elm.Diode().down().label("$V_D$")
        d += elm.Line().left()
        d.save(fspath(output))


def generate_zener_clamp(output: Path) -> None:
    """Zener clamp regulator: V_in -> R_S -> node -> (Zener || R_L) -> GND.

    Built ground-up; Zener branch uses .reverse() for correct polarity.
    Push/pop for the two shunt branches from the node.
    """
    with drawing_context() as d:
        d += elm.Ground()
        d += elm.SourceV().up().label("$V_{in}$")
        d += elm.Resistor().right().label("$R_S$")
        d += elm.Dot().label("$V_{node}$")
        # Branch 1: Zener diode to ground (shunt clamp)
        d.push()
        d += elm.Zener().down().reverse().label("$V_Z$")
        d += elm.Line().left()  # return to voltage source
        d.pop()
        # Branch 2: load resistor to ground
        d.push()
        d += elm.Line().right(1.5)
        d += elm.Resistor().down().label("$R_L$")
        d += elm.Line().left(1.5)  # return
        d.pop()
        d.save(fspath(output))


def generate_npn_low_side_switch(output: Path) -> None:
    """NPN low-side switch: Vcc -> load -> collector; emitter to GND; base via R_B.

    Central component (BJT, circle=True) placed first; each branch attached with
    .at(q.collector), .at(q.emitter), .at(q.base). Sources use .reverse() so
    polarity is toward the transistor.
    """
    with drawing_context() as d:
        q = elm.BjtNpn(circle=True).label("Q")
        d += q

        # Vcc -> load -> collector
        d += elm.Resistor().at(q.collector).up().label("load")
        d += elm.SourceV().left().reverse().label(R"$V_{\mathrm{CC}}$")
        d += elm.Ground()

        # emitter -> GND
        d += elm.Ground().at(q.emitter)

        # Vin -> Rb -> base
        d += elm.Resistor().at(q.base).left().label("$R_B$")
        d += elm.SourceV().up().reverse().label(R"$V_{\mathrm{IN}}$")
        d += elm.Ground().left()

        d.save(fspath(output))


def generate_h_bridge(output: Path) -> None:
    """H-bridge with four transistors S1–S4 (PNP high-side, NPN low-side) and motor.

    Start with the motor (a horizontal Line left to right). Use the motor's
    start for the left rail (up: S1 PNP–Vcc, down: S4 NPN–GND) and the motor's
    end for the right rail (up: S2 PNP–Vcc, down: S3 NPN–GND). BJTs use circle=True.
    """
    with drawing_context() as d:
        # Motor: horizontal line from left to right
        motor = elm.Line().right(2).label("motor")
        d += motor

        # Left rail from motor.start: up (S1 PNP, Vcc) and down (S4 NPN, GND)
        d.push()
        d += elm.Line().at(motor.start).up().length(1)
        d += elm.BjtPnp(circle=True).anchor("collector").right().label("S1")
        d += elm.SourceV().up().reverse().label(R"$V_{\mathrm{cc}}$")
        d.pop()
        d += elm.Line().at(motor.start).down().length(1)
        bjt = elm.BjtNpn(circle=True).anchor("collector").right().label("S3")
        d += bjt
        d += elm.Ground().at(bjt.emitter)

        # Right rail from motor.end: up (S2 PNP, Vcc) and down (S3 NPN, GND)
        d.push()
        d += elm.Line().at(motor.end).up().length(1)
        d += elm.BjtPnp(circle=True).anchor("collector").right().reverse().label("S2")
        d += elm.SourceV().up().reverse().label(R"$V_{\mathrm{cc}}$")
        d.pop()
        d += elm.Line().at(motor.end).down().length(1)
        bjt = elm.BjtNpn(circle=True).anchor("collector").right().reverse().label("S4")
        d += bjt
        d += elm.Ground().at(bjt.emitter)

        d.save(fspath(output))


def generate_74hc14_pinout(output: Path) -> None:
    """74HC14 hex inverter IC pinout (14-pin DIP).

    Rectangular IC body; pin 1 top-left, pins 1–7 down left side, 8–14 up right
    side. VCC (14) and GND (7) highlighted; one inverter pair (1A, 1Y) shown
    for reference. Style: central box with Ic, size chosen for 14 pins.
    """
    with drawing_context() as d:
        ic = elm.Ic(
            size=(3, 6),
            pins=[
                elm.IcPin(name="7\nGND", side="L", anchorname="gnd"),
                elm.IcPin(name="6\n3Y", side="L", anchorname="p6"),
                elm.IcPin(name="5\n3A", side="L", anchorname="p5"),
                elm.IcPin(name="4\n2Y", side="L", anchorname="p4"),
                elm.IcPin(name="3\n2A", side="L", anchorname="p3"),
                elm.IcPin(name="2\n1Y", side="L", anchorname="p2"),
                elm.IcPin(name="1\n1A", side="L", anchorname="p1"),
                elm.IcPin(name="8\n4Y", side="R", anchorname="p8"),
                elm.IcPin(name="9\n4A", side="R", anchorname="p9"),
                elm.IcPin(name="10\n5Y", side="R", anchorname="p10"),
                elm.IcPin(name="11\n5A", side="R", anchorname="p11"),
                elm.IcPin(name="12\n6Y", side="R", anchorname="p12"),
                elm.IcPin(name="13\n6A", side="R", anchorname="p13"),
                elm.IcPin(name="14\nVCC", side="R", anchorname="vcc"),
            ],
        ).label("74HC14\nhex\ninverter")
        d += ic
        d.save(fspath(output))


def generate_l293_block(output: Path) -> None:
    """L293 dual H-bridge motor driver IC block (16-pin DIP).

    Key pins: 8 = VS (motor supply), 16 = VCC (logic); EN_12, IN_1, OUT_1,
    OUT_2, IN_2 for H-bridge 1; EN_34, IN_3, OUT_3, OUT_4, IN_4 for H-bridge 2.
    """
    with drawing_context() as d:
        ic = elm.Ic(
            size=(4, 7),
            pins=[
                elm.IcPin(name="8\nVS", side="L", anchorname="vs"),
                elm.IcPin(name="7\nIN_2", side="L", anchorname="in2"),
                elm.IcPin(name="6\nOUT_2", side="L", anchorname="out2"),
                elm.IcPin(name="5\nGND", side="L", anchorname="gnd2"),
                elm.IcPin(name="4\nGND", side="L", anchorname="gnd1"),
                elm.IcPin(name="3\nOUT_1", side="L", anchorname="out1"),
                elm.IcPin(name="2\nIN_1", side="L", anchorname="in1"),
                elm.IcPin(name="1\nEN_12", side="L", anchorname="en12"),
                elm.IcPin(name="9\nEN_34", side="R", anchorname="en34"),
                elm.IcPin(name="10\nIN_3", side="R", anchorname="in3"),
                elm.IcPin(name="11\nOUT_3", side="R", anchorname="out3"),
                elm.IcPin(name="12\nGND", side="R", anchorname="gnd3"),
                elm.IcPin(name="13\nGND", side="R", anchorname="gnd4"),
                elm.IcPin(name="14\nOUT_4", side="R", anchorname="out4"),
                elm.IcPin(name="15\nIN_4", side="R", anchorname="in4"),
                elm.IcPin(name="16\nVCC", side="R", anchorname="vcc"),
            ],
        ).label("L293\ndual\nH-bridge")
        d += ic
        d.save(fspath(output))


def generate_three_pin_regulator(output: Path) -> None:
    """3-pin regulator with input/output capacitors (e.g. 7805-style).

    Style follows generate_npn_low_side_switch: regulator (Ic with IN/OUT/GND
    pins, size=(3,2), label REG 5V) placed first; branches attached with
    .at(reg.v_in), .at(reg.v_out), .at(reg.gnd).  IN branch: line left –
    V_in node – C_in down – GND.  OUT branch: line right – V_out node –
    C_out down – GND.  GND pin – Ground().
    """
    with drawing_context() as d:
        reg = elm.Ic(
            size=(3, 2),
            pins=[
                elm.IcPin(name="IN", side="L", anchorname="v_in"),
                elm.IcPin(name="OUT", side="R", anchorname="v_out"),
                elm.IcPin(name="GND", side="B", anchorname="gnd"),
            ],
        ).label("REG\n5V")
        d += reg

        # IN: input rail – line left to node, then V_in up (reverse) to GND; C_in from node down to GND
        d += elm.Line().left(0.5).at(reg.v_in)
        d += elm.Dot().label(R"$V_{\mathrm{in}}$")
        d += elm.Capacitor().down().label(R"$C_{\mathrm{in}}$")
        d += elm.Ground()

        # OUT: output rail – line right, V_out node, C_out down to GND
        d += elm.Line().right(0.5).at(reg.v_out)
        d += elm.Dot().label(R"$V_{\mathrm{out}}$")
        d += elm.Capacitor().down().label(R"$C_{\mathrm{out}}$")
        d += elm.Ground()

        # GND pin
        d += elm.Ground().at(reg.gnd)

        d.save(fspath(output))


def _run_generator(args: tuple[Callable[[Path], None], Path]) -> None:
    """Run a single generator (func, path) for multiprocessing Pool."""
    func, path = args
    func(path)


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate ELEC1100 circuit diagrams (SVG)"
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
        (generate_series_resistor, outdir_path / "series.svg"),
        (generate_parallel_resistor, outdir_path / "parallel.svg"),
        (generate_kcl_node, outdir_path / "kcl.svg"),
        (generate_kvl_loop, outdir_path / "kvl.svg"),
        (generate_two_branch, outdir_path / "two_branch.svg"),
        (generate_bridge_two_sources, outdir_path / "bridge.svg"),
        (generate_symbol_resistor, outdir_path / "symbol_resistor.svg"),
        (generate_symbol_capacitor, outdir_path / "symbol_capacitor.svg"),
        (generate_symbol_diode, outdir_path / "symbol_diode.svg"),
        (generate_symbol_zener, outdir_path / "symbol_zener.svg"),
        (generate_symbol_voltage_source, outdir_path / "symbol_voltage_source.svg"),
        (generate_symbol_ground, outdir_path / "symbol_ground.svg"),
        (generate_symbol_npn, outdir_path / "symbol_npn.svg"),
        (generate_symbol_pnp, outdir_path / "symbol_pnp.svg"),
        (generate_equivalent_npn, outdir_path / "equivalent_npn.svg"),
        (generate_equivalent_pnp, outdir_path / "equivalent_pnp.svg"),
        (generate_series_diode_resistor, outdir_path / "series_diode_resistor.svg"),
        (generate_zener_clamp, outdir_path / "zener_clamp.svg"),
        (generate_npn_low_side_switch, outdir_path / "npn_low_side_switch.svg"),
        (generate_three_pin_regulator, outdir_path / "three_pin_regulator.svg"),
        (generate_h_bridge, outdir_path / "h_bridge.svg"),
        (generate_74hc14_pinout, outdir_path / "74hc14_pinout.svg"),
        (generate_l293_block, outdir_path / "l293_block.svg"),
    ]

    with Pool(processes=_MAX_POOL_WORKERS) as pool:
        pool.map(_run_generator, generators)


def __main__():
    """Entry point for running the script directly."""
    runnify(main, backend_options={"use_uvloop": True})()


if __name__ == "__main__":
    __main__()
