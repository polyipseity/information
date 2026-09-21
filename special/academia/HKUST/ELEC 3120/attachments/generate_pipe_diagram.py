#!/usr/bin/env python
# /// script
# dependencies = [
#   "matplotlib>=3.11.0",
# ]
# requires-python = ">=3.13.0"
# ///
"""Generate the pipe-model drawing for the ELEC 3120 notes.

The pipe model is a convention rather than an illustration: a link is drawn as
a pipe, the width of which is its bandwidth and the length of which is its
propagation delay. Everything later in the course leans on it, because it is
what makes a link quotable as two numbers, such as ``1 Gbps x 10 ms``, and it
explains why one link can be wide and short while another is narrow and long.
The note that defines bandwidth and delay therefore shows the drawing.

The pipe is one parametric shape with a dark mouth at the near end and a
rounded far end, and its two extent markers are derived from that shape: a
vertical one across the mouth, and a horizontal one under the body. Nothing is
nudged into place by hand, and no text is drawn, because the drawing stands on
the prompt side of a recognition card and must not print the answer.

The source drawing marks the two extents with curly braces; drafting arrows
with extension lines are the same statement in the notation the surrounding
notes use, and they stay legible at the size the note renders them.

Output is written beside this script as ``link_pipe_model.svg`` so that it can
be committed. Run it with ``uv run <path to this file>``.
"""

from __future__ import annotations

from pathlib import Path

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.patches import Ellipse, FancyArrowPatch, Rectangle

PIPE_LENGTH = 4.0
PIPE_DIAMETER = 1.2
MOUTH_HALF_WIDTH = 0.20
DIMENSION_GAP = 0.45

BODY_COLOUR = "#b39ddb"
MOUTH_COLOUR = "#6a1b9a"
MARK_COLOUR = "#37474f"

FIGURE_SIZE = (6.0, 1.9)
OUTPUT_NAME = "link_pipe_model.svg"


def draw_pipe(axes) -> None:
    """Draw the cylinder: a body with a rounded far end and a dark mouth."""
    near_edge = MOUTH_HALF_WIDTH
    far_edge = MOUTH_HALF_WIDTH + PIPE_LENGTH
    axes.add_patch(
        Rectangle(
            (near_edge, -PIPE_DIAMETER / 2),
            PIPE_LENGTH,
            PIPE_DIAMETER,
            facecolor=BODY_COLOUR,
            edgecolor="none",
        )
    )
    for center in (near_edge, far_edge):
        axes.add_patch(
            Ellipse(
                (center, 0.0),
                2 * MOUTH_HALF_WIDTH,
                PIPE_DIAMETER,
                facecolor=BODY_COLOUR,
                edgecolor="none",
            )
        )
    axes.add_patch(
        Ellipse(
            (near_edge, 0.0),
            2 * MOUTH_HALF_WIDTH,
            PIPE_DIAMETER,
            facecolor=MOUTH_COLOUR,
            edgecolor="none",
        )
    )


def draw_extent(
    axes,
    start: tuple[float, float],
    end: tuple[float, float],
    *extensions: tuple[tuple[float, float], tuple[float, float]],
) -> None:
    """Mark one extent of the pipe with a double arrow and extension lines."""
    axes.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="<->",
            mutation_scale=9,
            color=MARK_COLOUR,
            linewidth=1.2,
            shrinkA=0,
            shrinkB=0,
        )
    )
    for extension_start, extension_end in extensions:
        axes.plot(
            [extension_start[0], extension_end[0]],
            [extension_start[1], extension_end[1]],
            color=MARK_COLOUR,
            linewidth=0.7,
        )


def draw_extents(axes) -> None:
    """Mark the pipe's width at the mouth and its length along the body."""
    width_x = -DIMENSION_GAP / 2
    axes.add_patch(
        FancyArrowPatch(
            (width_x, -PIPE_DIAMETER / 2),
            (width_x, PIPE_DIAMETER / 2),
            arrowstyle="<->",
            mutation_scale=9,
            color=MARK_COLOUR,
            linewidth=1.2,
            shrinkA=0,
            shrinkB=0,
        )
    )
    for y in (-PIPE_DIAMETER / 2, PIPE_DIAMETER / 2):
        axes.plot([width_x, MOUTH_HALF_WIDTH], [y, y], color=MARK_COLOUR, linewidth=0.7)

    body_start = MOUTH_HALF_WIDTH
    body_end = MOUTH_HALF_WIDTH + PIPE_LENGTH
    length_y = -(PIPE_DIAMETER / 2 + DIMENSION_GAP)
    axes.add_patch(
        FancyArrowPatch(
            (body_start, length_y),
            (body_end, length_y),
            arrowstyle="<->",
            mutation_scale=9,
            color=MARK_COLOUR,
            linewidth=1.2,
            shrinkA=0,
            shrinkB=0,
        )
    )
    for x in (body_start, body_end):
        axes.plot(
            [x, x],
            [-PIPE_DIAMETER / 2, length_y],
            color=MARK_COLOUR,
            linewidth=0.7,
        )


def build_figure() -> Figure:
    """Return the finished pipe drawing."""
    figure = Figure(figsize=FIGURE_SIZE, layout="tight")
    FigureCanvasAgg(figure)
    axes = figure.add_subplot()
    axes.set_axis_off()
    axes.set_aspect("equal")
    draw_pipe(axes)
    draw_extents(axes)
    return figure


def main(argv: list[str] | None = None) -> None:
    """Write the pipe drawing beside this script."""
    del argv
    output = Path(__file__).with_name(OUTPUT_NAME)
    build_figure().savefig(output, format="svg", transparent=True)
    print(output)


def __main__() -> None:
    """Run the generator."""
    main()


if __name__ == "__main__":
    __main__()
