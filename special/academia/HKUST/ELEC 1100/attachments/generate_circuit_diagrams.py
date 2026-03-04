#!/usr/bin/env python
# /// script
# dependencies = [
#   "schemdraw[matplotlib,svgmath]>=0.22",
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
* a symmetric bridge network with two sources.

Outputs are written as SVG files into the ``attachments`` directory next
to the script so they can be committed to version control.  Running the
module without arguments generates diagrams in place; the optional
``outdir`` parameter exists only for testing.

The generator is intentionally minimal and deterministic.  There are no
unit tests by design; this comment documents that fact for future
maintainers.
"""

import argparse
from asyncio import run
from os import fspath

import schemdraw
import schemdraw.elements as elm
from anyio import Path


def generate_series_resistor(output: Path) -> None:
    """Draw a closed series circuit with a voltage source and three resistors.

    This version replaces an earlier open‑loop sketch.  A source is placed
    on the left, followed by two resistors along the top branch.  A third
    resistor on the right side completes the series chain back to the
    source.  No mesh arrow is included here; that appearance is handled by
    :func:`generate_kvl_loop`.
    """

    d = schemdraw.Drawing()
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

    d = schemdraw.Drawing()
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

    d = schemdraw.Drawing()
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

    d = schemdraw.Drawing()
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

    d = schemdraw.Drawing()
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
    """Bridge‑style circuit containing two independent sources and a central
    resistor.

    A 6 V source with a 2 Ω series resistor forms the left loop; a 10 V
    source with a 2 Ω resistor forms the right loop.  The central 1 Ω
    resistor sits between the top and bottom rails and carries the sum of
    the two loop currents, giving rise to the $(I_1+I_2)$ term in the
    KVL equations discussed in class.
    """

    d = schemdraw.Drawing()
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

    # always generate the full set of diagrams
    generate_series_resistor(outdir / "series.svg")
    generate_parallel_resistor(outdir / "parallel.svg")
    generate_kcl_node(outdir / "kcl.svg")
    generate_kvl_loop(outdir / "kvl.svg")
    generate_two_branch(outdir / "two_branch.svg")
    generate_bridge_two_sources(outdir / "bridge.svg")


if __name__ == "__main__":
    run(main())
