#!/usr/bin/env python
# /// script
# dependencies = [
#   "matplotlib>=3.11.0",
# ]
# requires-python = ">=3.13.0"
# ///
"""Generate the drawings for the COMP 3511 notes.

Three drawings are produced, and each one is the definition of what its note
states in prose.

``process_states.svg`` is the five-state process model: the five states and the
six transitions that connect them. A state and the event that moves a process
out of it are one fact, so the drawing carries the event labels rather than
leaving the prose to name them. The note cards it both ways, and the labels are
what the recall card asks for.

``mlfq_structure.svg`` is the three-queue multilevel feedback queue of the
course's worked example: a new job entering the highest-priority queue, the
quantum each queue grants before demoting a job, and the run-to-completion
queue at the bottom. The quanta are the parameters of the algorithm, so they
sit in the drawing.

``resource_allocation_graph.svg`` is a resource-allocation graph: processes as
circles, resource types as rectangles with one dot per instance, and the two
kinds of edge that make the graph a statement about who holds what and who
waits for what. The convention is what the note defines, so a reader has to be
able to draw it from the card, not only to read it.

Output is written beside this script so that it can be committed. Run it with
``uv run <path to this file>``.
"""

from __future__ import annotations

import math
import sys
import tempfile
from pathlib import Path

import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.patches import (
    Circle,
    Ellipse,
    FancyArrowPatch,
    FancyBboxPatch,
    Rectangle,
)

# Reproducible SVG output. matplotlib salts the element ids it generates with a
# fresh uuid4 per process, so redrawing an unchanged figure still produces a
# diff; pinning the salt makes a regenerated file byte-identical to the
# committed one. The date is dropped outright via ``metadata`` below.
matplotlib.rcParams["svg.hashsalt"] = "information.academia-ingest"

OUTPUT_DIR = Path(__file__).resolve().parent

STATE_FILL = "#cfe3ef"
RESOURCE_FILL = "#e6e6e6"
MARK_COLOUR = "#37474f"
LABEL_SIZE = 10

STATE_SIZE = (10.1, 3.7)
STATE_W = 1.70
STATE_H = 0.84
NEW = (1.00, 3.10)
READY = (3.25, 2.05)
RUNNING = (6.55, 2.05)
TERMINATED = (9.05, 3.10)
WAITING = (4.80, 0.65)

MLFQ_SIZE = (9.5, 4.3)
MLFQ_LEFT = 1.55
MLFQ_RIGHT = 6.55
MLFQ_BOX_H = 0.80
MLFQ_BOX_W = 5.00
MLFQ_ROWS = (3.50, 2.10, 0.70)

RAG_SIZE = (9.0, 4.6)
RAG_NODE_R = 0.42
RAG_RES_W = 1.05
RAG_RES_H = 0.80


def _arrow(
    ax,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    connectionstyle: str = "arc3,rad=0",
    colour: str = MARK_COLOUR,
) -> None:
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            connectionstyle=connectionstyle,
            arrowstyle="-|>",
            linewidth=1.1,
            color=colour,
            mutation_scale=13,
            shrinkA=0,
            shrinkB=0,
        )
    )


def _beside(
    ax,
    start: tuple[float, float],
    end: tuple[float, float],
    text: str,
    *,
    t: float = 0.5,
    distance: float = 0.16,
    side: float = 1.0,
    ha: str = "center",
    va: str = "bottom",
    fontsize: float = LABEL_SIZE - 1,
) -> None:
    """Place ``text`` beside a segment so that no arrow runs through it.

    The label sits ``distance`` to the left of the segment at fraction ``t``
    when ``side`` is positive, and to the right when it is negative. Text is
    anchored away from that point, so the box never straddles the line.
    """
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = math.hypot(dx, dy)
    x = start[0] + dx * t - dy / length * distance * side
    y = start[1] + dy * t + dx / length * distance * side
    ax.text(
        x,
        y,
        text,
        ha=ha,
        va=va,
        fontsize=fontsize,
        color=MARK_COLOUR,
    )


def _edge(centre, w, h, toward: tuple[float, float]) -> tuple[float, float]:
    """Return the point where the ray from ``centre`` to ``toward`` leaves the ellipse."""
    dx = toward[0] - centre[0]
    dy = toward[1] - centre[1]
    scale = 1.0 / (((dx / (w / 2)) ** 2 + (dy / (h / 2)) ** 2) ** 0.5)
    return (centre[0] + dx * scale, centre[1] + dy * scale)


def _ellipse(ax, centre: tuple[float, float], w: float, h: float) -> None:
    ax.add_patch(
        Ellipse(
            centre,
            w,
            h,
            facecolor=STATE_FILL,
            edgecolor=MARK_COLOUR,
            linewidth=1.1,
        )
    )


def draw_process_states(ax) -> None:
    """Draw the five states and the six transitions between them."""
    ax.set_xlim(0, STATE_SIZE[0])
    ax.set_ylim(0.05, 3.75)
    ax.axis("off")

    states = (
        (NEW, "new"),
        (READY, "ready"),
        (RUNNING, "running"),
        (TERMINATED, "terminated"),
        (WAITING, "waiting"),
    )
    for centre, _ in states:
        _ellipse(ax, centre, STATE_W, STATE_H)
    for centre, label in states:
        ax.text(
            centre[0],
            centre[1],
            label,
            ha="center",
            va="center",
            fontsize=LABEL_SIZE,
            color=MARK_COLOUR,
        )

    admitted = (
        _edge(NEW, STATE_W, STATE_H, (3.00, 2.35)),
        _edge(READY, STATE_W, STATE_H, (1.00, 3.10)),
    )
    _arrow(ax, *admitted)
    _beside(ax, *admitted, "admitted", t=0.55, distance=0.15)

    dispatch = (
        (READY[0] + STATE_W / 2, READY[1]),
        (RUNNING[0] - STATE_W / 2, RUNNING[1]),
    )
    _arrow(ax, *dispatch)
    _beside(ax, *dispatch, "scheduler dispatch", distance=0.14)

    interrupt = (
        (RUNNING[0] - 0.42, RUNNING[1] + STATE_H / 2),
        (READY[0] + 0.42, READY[1] + STATE_H / 2),
    )
    _arrow(ax, *interrupt, connectionstyle="arc3,rad=0.95")
    _beside(ax, *interrupt, "interrupt", distance=0.34, side=-1.0)

    wait = (
        _edge(RUNNING, STATE_W, STATE_H, (5.60, 0.85)),
        _edge(WAITING, STATE_W, STATE_H, (6.20, 2.20)),
    )
    _arrow(ax, *wait)
    _beside(ax, *wait, "I/O or event wait", t=0.5, ha="left", va="center")

    completion = (
        _edge(WAITING, STATE_W, STATE_H, (3.10, 2.00)),
        _edge(READY, STATE_W, STATE_H, (4.90, 0.60)),
    )
    _arrow(ax, *completion)
    _beside(
        ax,
        *completion,
        "I/O or event completion",
        t=0.45,
        ha="right",
        va="center",
    )

    exit_arrow = (
        _edge(RUNNING, STATE_W, STATE_H, (9.20, 3.20)),
        _edge(TERMINATED, STATE_W, STATE_H, (6.50, 1.90)),
    )
    _arrow(ax, *exit_arrow)
    _beside(ax, *exit_arrow, "exit", t=0.45, distance=0.15)


def draw_mlfq(ax) -> None:
    """Draw three priority queues, their quanta and the two demotions."""
    ax.set_xlim(0, MLFQ_SIZE[0])
    ax.set_ylim(0.30, 4.60)
    ax.axis("off")

    queues = (
        ("queue 0: round robin, quantum 4", MLFQ_ROWS[0]),
        ("queue 1: round robin, quantum 8", MLFQ_ROWS[1]),
        ("queue 2: first-come first-served", MLFQ_ROWS[2]),
    )
    for label, y in queues:
        ax.add_patch(
            FancyBboxPatch(
                (MLFQ_LEFT, y),
                MLFQ_BOX_W,
                MLFQ_BOX_H,
                boxstyle="round,pad=0.02,rounding_size=0.04",
                facecolor=STATE_FILL,
                edgecolor=MARK_COLOUR,
                linewidth=1.1,
            )
        )
        ax.text(
            MLFQ_LEFT + MLFQ_BOX_W / 2,
            y + MLFQ_BOX_H / 2,
            label,
            ha="center",
            va="center",
            fontsize=LABEL_SIZE,
            color=MARK_COLOUR,
        )

    box_right = MLFQ_LEFT + MLFQ_BOX_W
    mids = [y + MLFQ_BOX_H / 2 for _, y in queues]

    _arrow(ax, (MLFQ_LEFT - 1.20, mids[0]), (MLFQ_LEFT - 0.02, mids[0]))
    _beside(
        ax,
        (MLFQ_LEFT - 1.20, mids[0]),
        (MLFQ_LEFT - 0.02, mids[0]),
        "new job",
        t=0.0,
        distance=0.14,
        ha="left",
    )

    for upper, lower in ((MLFQ_ROWS[0], MLFQ_ROWS[1]), (MLFQ_ROWS[1], MLFQ_ROWS[2])):
        start = (MLFQ_LEFT - 0.32, upper)
        end = (MLFQ_LEFT - 0.32, lower + MLFQ_BOX_H)
        _arrow(ax, start, end)
        _beside(
            ax,
            start,
            end,
            "quantum\nexpires",
            distance=0.16,
            side=-1.0,
            ha="right",
            va="center",
            fontsize=LABEL_SIZE - 2,
        )

    spine = box_right + 0.55
    for mid in mids:
        ax.plot([box_right, spine], [mid, mid], color=MARK_COLOUR, linewidth=1.1)
    ax.plot([spine, spine], [mids[-1], mids[0]], color=MARK_COLOUR, linewidth=1.1)
    _arrow(ax, (spine, mids[0]), (spine + 0.55, mids[0]))
    ax.text(
        spine + 0.68,
        mids[0],
        "process completes",
        ha="left",
        va="center",
        fontsize=LABEL_SIZE - 1,
        color=MARK_COLOUR,
    )


def draw_resource_allocation_graph(ax) -> None:
    """Draw processes, resource types with instances, and the two edge kinds."""
    ax.set_xlim(0, RAG_SIZE[0])
    ax.set_ylim(0.20, 4.60)
    ax.axis("off")

    tasks = {"T1": (1.05, 2.50), "T2": (4.25, 2.50), "T3": (7.45, 2.50)}
    resources = {
        "R1": (2.65, 3.95),
        "R2": (2.65, 1.05),
        "R3": (5.90, 3.95),
        "R4": (7.45, 1.05),
    }
    instances = {"R1": 1, "R2": 2, "R3": 1, "R4": 3}

    for name, centre in tasks.items():
        ax.add_patch(
            Circle(
                centre,
                RAG_NODE_R,
                facecolor=STATE_FILL,
                edgecolor=MARK_COLOUR,
                linewidth=1.1,
            )
        )
        ax.text(
            centre[0],
            centre[1],
            name,
            ha="center",
            va="center",
            fontsize=LABEL_SIZE,
            color=MARK_COLOUR,
        )

    for name, centre in resources.items():
        ax.add_patch(
            Rectangle(
                (centre[0] - RAG_RES_W / 2, centre[1] - RAG_RES_H / 2),
                RAG_RES_W,
                RAG_RES_H,
                facecolor=RESOURCE_FILL,
                edgecolor=MARK_COLOUR,
                linewidth=1.1,
            )
        )
        count = instances[name]
        spacing = RAG_RES_W / (count + 1)
        for k in range(count):
            ax.add_patch(
                Circle(
                    (centre[0] - RAG_RES_W / 2 + spacing * (k + 1), centre[1]),
                    0.05,
                    facecolor=MARK_COLOUR,
                    edgecolor=MARK_COLOUR,
                )
            )
        ax.text(
            centre[0] - RAG_RES_W / 2 - 0.12,
            centre[1],
            name,
            ha="right",
            va="center",
            fontsize=LABEL_SIZE,
            color=MARK_COLOUR,
        )

    def task_box(task: str, resource: str) -> tuple[float, float]:
        """Return the point on the task circle facing the resource box."""
        return _edge(tasks[task], RAG_NODE_R * 2, RAG_NODE_R * 2, resources[resource])

    def box_task(task: str, resource: str) -> tuple[float, float]:
        """Return the point on the resource box facing the task circle."""
        centre = resources[resource]
        return _edge(centre, RAG_RES_W, RAG_RES_H, tasks[task])

    for task, resource, t in (
        ("T1", "R1", 0.55),
        ("T2", "R3", 0.62),
    ):
        start = task_box(task, resource)
        end = box_task(task, resource)
        _arrow(ax, start, end)
        _beside(
            ax,
            start,
            end,
            "request",
            t=t,
            distance=0.12,
            ha="right",
            va="bottom",
            fontsize=LABEL_SIZE - 2,
        )

    for task, resource, t, align, valign in (
        ("T2", "R1", 0.45, "left", "bottom"),
        ("T1", "R2", 0.50, "right", "top"),
        ("T2", "R2", 0.45, "right", "bottom"),
        ("T3", "R3", 0.45, "left", "bottom"),
    ):
        start = box_task(task, resource)
        end = task_box(task, resource)
        _arrow(ax, start, end)
        _beside(
            ax,
            start,
            end,
            "assignment",
            t=t,
            distance=0.12,
            ha=align,
            va=valign,
            fontsize=LABEL_SIZE - 2,
        )


def render(name: str, size: tuple[float, float], draw, *, preview: bool) -> None:
    """Draw one figure into ``name``, and into a PNG outside the repo on request."""
    fig = Figure(figsize=size, dpi=150)
    canvas = FigureCanvasAgg(fig)
    ax = fig.add_axes((0.0, 0.0, 1.0, 1.0))
    draw(ax)
    fig.savefig(OUTPUT_DIR / name, format="svg", metadata={"Date": None})
    if preview:
        fig.savefig(
            Path(tempfile.gettempdir()) / (name.removesuffix(".svg") + ".png"),
            format="png",
        )
    canvas.draw()


def main() -> None:
    """Write the three drawings beside this script."""
    preview = "preview" in sys.argv[1:]
    render("process_states.svg", STATE_SIZE, draw_process_states, preview=preview)
    render("mlfq_structure.svg", MLFQ_SIZE, draw_mlfq, preview=preview)
    render(
        "resource_allocation_graph.svg",
        RAG_SIZE,
        draw_resource_allocation_graph,
        preview=preview,
    )


def __main__() -> None:
    """Entry point for running the script directly."""
    main()


if __name__ == "__main__":
    __main__()
