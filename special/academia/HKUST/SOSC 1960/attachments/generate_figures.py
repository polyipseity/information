#!/usr/bin/env python
# /// script
# requires-python = ">=3.13.0"
# ///
"""Generate the SVG figures defined by the SOSC 1960 notes.

The course takes its figures from Wikimedia Commons wherever a suitable
freely-licensed image exists, downloaded with pyarchivist; see
``index.md`` for the five archived here under that rule. This script
generates only the figures for which no suitable image was found.

Those figures state something prose alone cannot. The three-row sequence
that reverses conditioning, the three-panel arrangement of a blocking
experiment whose whole point is which cue is present in which phase, the
four stages of learning from a model where the order is the entire claim,
the three causal structures one correlation is compatible with, and the
three relations around a behaviour. They are written as SVG text rather
than drawn through a plotting library, because every coordinate carries
meaning: the order of the rows is the order of the trials, and the order
of the panels is the order of the phases.

The four searches that found no dedicated single-purpose diagram. A search
coming up empty is not the same as a subject being absent: for two of
these, ``File:Classical Conditioning.svg`` (archived here) does carry a
row for the procedure, but as one panel of a seven-panel chart, which is a
worse figure for a note about that procedure than a purpose-built
diagram. So they are generated, and the near-match is recorded rather than
used:

- ``classical_conditioning_blocking.svg`` — the Kamin blocking procedure.
  Searching Commons for "Kamin blocking" and "blocking effect psychology"
  returns power-station cooling towers and unrelated scanned books. The
  only diagram of the procedure found is the BLOCKING row of the
  seven-panel chart.
- ``classical_conditioning_extinction.svg`` — extinction across rows. The
  search for "conditioned response extinction curve" returns optics papers
  on light extinction and combustion extinction. As with blocking, the
  only diagram of the procedure found is one row of that same chart.
- ``observational_learning_stages.svg`` — Bandura's four stages. The search
  for "four stages observational learning" returns Bacon's *Advancement of
  Learning* and a maze-learning rat study. Nothing usable, and nothing
  showing the four stages in order.
- ``correlation_causal_directions.svg`` — the three causal structures one
  correlation is compatible with. The searches for "causal diagram
  confound" and "correlation causation diagram psychology" return causal
  graphs drawn in the finance literature, each showing a single confounder
  rather than the three structures side by side.

A fifth figure, ``conditioning_relations.svg``, keeps a partial Commons
alternative deliberately unused: ``File:Classical vs operant conditioning.svg``
(CC BY-SA 4.0, Perey) is close, but it does not draw the occasion-setting
arrow that ``operant conditioning.md`` asks a reader to find in the figure.
The course's rule is that prose is not bent to fit a substitute image, so
the figure is generated instead.

The helpers are namespaced by their source script (``_c_``, ``_i_``, ``_r_``)
rather than unified, because the three sets differ in ways that are visible
in the output: the conditioning ``_text`` defaults to size 16 and emits no
``font-weight`` or ``font-style`` attribute, the instrumental ``_text``
defaults to size 16 and always emits them, and the research-design ``_text``
defaults to size 17 and emits neither. Unifying them would change a figure
that is not meant to change. The constants they share are declared once,
because their values already agree across all three sets.

Outputs are written next to this script so they can be committed to version
control. Running the module without arguments regenerates the figures in
place; the optional ``outdir`` parameter exists only for testing.

There are no unit tests by design; this comment documents that fact for
future maintainers.
"""

import argparse
import math
from collections.abc import Sequence
from os import fspath
from pathlib import Path

# --- shared drawing vocabulary ---------------------------------------------
# These values already agreed across the three source scripts.

INK = "#1f3864"
LABEL = "#1a1a1a"
MUTED = "#5a5a5a"
STAGE = "#fbd3a6"  # something the organism receives
OUTCOME = "#e8eef7"  # what the organism does
ABSENT = "#f2f2f2"  # a stimulus withdrawn, marked with a minus sign
MARK = "#c2410c"  # the arrow or label that names the relation
NODE_FILL = STAGE  # a filled box in a causal diagram
FONT = "font-family='Helvetica, Arial, sans-serif'"


# --- conditioning vocabulary (from the former generate_conditioning_figures)


def _c_text(
    x: float,
    y: float,
    body: str,
    size: int = 16,
    anchor: str = "middle",
    fill: str = LABEL,
) -> str:
    return (
        f"<text x='{x:g}' y='{y:g}' {FONT} font-size='{size}' "
        f"text-anchor='{anchor}' fill='{fill}'>{body}</text>"
    )


def _c_box(x: float, y: float, w: float, h: float, fill: str) -> str:
    return f"<rect x='{x:g}' y='{y:g}' width='{w:g}' height='{h:g}' rx='4' fill='{fill}' stroke='{INK}' stroke-width='2'/>"


def _c_arrow(x1: float, y: float, x2: float, fill: str = INK) -> str:
    return (
        f"<line x1='{x1:g}' y1='{y:g}' x2='{x2 - 10:g}' y2='{y:g}' stroke='{fill}' stroke-width='2.2'/>"
        f"<path d='M {x2:g} {y:g} L {x2 - 11:g} {y + 5.5:g} L {x2 - 11:g} {y - 5.5:g} Z' fill='{fill}'/>"
    )


def _c_canvas(w: float, h: float, body: str) -> str:
    return (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w:g} {h:g}' "
        f"width='{w:g}' height='{h:g}'>\n<rect width='{w:g}' height='{h:g}' fill='#ffffff'/>\n{body}\n</svg>\n"
    )


def _c_v_arrow(x: float, y1: float, y2: float, fill: str = INK) -> str:
    return (
        f"<line x1='{x:g}' y1='{y1:g}' x2='{x:g}' y2='{y2 - 8:g}' stroke='{fill}' stroke-width='2.2'/>"
        f"<path d='M {x:g} {y2:g} L {x - 5.5:g} {y2 - 11:g} L {x + 5.5:g} {y2 - 11:g} Z' fill='{fill}'/>"
    )


# --- instrumental-learning vocabulary (former generate_instrumental_learning_figures)


def _i_text(
    x: float,
    y: float,
    body: str,
    size: int = 16,
    anchor: str = "middle",
    fill: str = LABEL,
    weight: str = "normal",
    style: str = "normal",
) -> str:
    return (
        f"<text x='{x:g}' y='{y:g}' {FONT} font-size='{size}' font-weight='{weight}' "
        f"font-style='{style}' text-anchor='{anchor}' fill='{fill}'>{body}</text>"
    )


def _i_box(
    x: float, y: float, w: float, h: float, fill: str, rx: float = 8, stroke: str = INK
) -> str:
    return f"<rect x='{x:g}' y='{y:g}' width='{w:g}' height='{h:g}' rx='{rx:g}' fill='{fill}' stroke='{stroke}' stroke-width='2'/>"


def _i_arrow(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    fill: str = MARK,
    width: float = 3,
    head: int = 11,
    dash: str = "",
) -> str:
    """A straight arrow from (x1, y1) to (x2, y2) with a solid head on the far end."""
    angle = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(angle), y2 - head * math.sin(angle)
    left = (bx - head * 0.45 * math.sin(angle), by + head * 0.45 * math.cos(angle))
    right = (bx + head * 0.45 * math.sin(angle), by - head * 0.45 * math.cos(angle))
    dashes = f" stroke-dasharray='{dash}'" if dash else ""
    return (
        f"<line x1='{x1:g}' y1='{y1:g}' x2='{bx:g}' y2='{by:g}' stroke='{fill}' stroke-width='{width}'{dashes}/>"
        f"<polygon points='{x2:g},{y2:g} {left[0]:g},{left[1]:g} {right[0]:g},{right[1]:g}' fill='{fill}'/>"
    )


def _i_svg(width: float, height: float, body: str) -> str:
    return (
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{width:g}' height='{height:g}' "
        f"viewBox='0 0 {width:g} {height:g}' role='img'>\n{body}\n</svg>\n"
    )


# --- research-design vocabulary (former generate_research_design_figures)


def _r_text(
    x: float, y: float, body: str, size: int = 17, anchor: str = "middle"
) -> str:
    return (
        f"<text x='{x:g}' y='{y:g}' {FONT} font-size='{size}' "
        f"text-anchor='{anchor}' fill='{LABEL}'>{body}</text>"
    )


def _r_arrow(
    x1: float, y1: float, x2: float, y2: float, width: float = 2.2
) -> list[str]:
    """A straight shaft from (x1, y1) to (x2, y2) with a head at the tip."""
    dx, dy = x2 - x1, y2 - y1
    length = (dx * dx + dy * dy) ** 0.5
    ux, uy = dx / length, dy / length
    # Stop the shaft where the head begins, so the two never overlap.
    head = 11.0
    return [
        f"<line x1='{x1 + ux * 2:g}' y1='{y1 + uy * 2:g}' "
        f"x2='{x2 - ux * head:g}' y2='{y2 - uy * head:g}' "
        f"stroke='{INK}' stroke-width='{width:g}'/>",
        f"<path d='M {x2:g} {y2:g} L {x2 - ux * head - uy * head * 0.55:g} "
        f"{y2 - uy * head + ux * head * 0.55:g} "
        f"L {x2 - ux * head + uy * head * 0.55:g} "
        f"{y2 - uy * head - ux * head * 0.55:g} Z' fill='{INK}'/>",
    ]


def _r_box(x: float, y: float, w: float, h: float, body: str) -> list[str]:
    return [
        f"<rect x='{x:g}' y='{y:g}' width='{w:g}' height='{h:g}' rx='4' "
        f"fill='{NODE_FILL}' stroke='{INK}' stroke-width='2'/>",
        _r_text(x + w / 2, y + h / 2 + 6, body),
    ]


def _r_head(width: int, height: int) -> list[str]:
    return [
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {width} {height}' "
        f"width='{width}' height='{height}'>",
        f"<rect width='{width}' height='{height}' fill='#ffffff'/>",
    ]


# --- extinction: bell without meat -----------------------------------------


def extinction_sequence() -> str:
    """The three rows in which a conditioned response dies: the bell, alone, and no meat.

    Every row is a bell-alone trial. Showing meat in the first row would be a
    conditioning trial, not an extinction one, and would contradict the label.
    The response box fades down the rows so the decline is the picture.
    """
    w, row_h, top = 830, 88, 62
    h = top + row_h * 3 + 18
    parts = [
        _c_text(20, 30, "Extinction of a conditioned response", 18, "start"),
        _c_text(20, 48, "The bell alone, with the meat withheld", 14, "start", MUTED),
    ]
    rows = (
        (
            "1",
            "the bell, at the start of extinction",
            STAGE,
            OUTCOME,
            "salivating (CR)",
        ),
        (
            "2",
            "the same bell, trial after trial",
            STAGE,
            ABSENT,
            "salivating, but fading",
        ),
        ("3", "the same bell, later still", STAGE, ABSENT, "nothing"),
    )
    for i, (num, stage, food_fill, response_fill, response) in enumerate(rows):
        y = top + i * row_h
        parts.append(_c_text(20, y + 34, num, 17, "start"))
        parts.append(_c_text(48, y + 32, stage, 15, "start"))
        parts.append(_c_arrow(360, y + 26, 410, MARK))
        parts.append(_c_box(412, y, 150, 52, food_fill))
        parts.append(_c_text(487, y + 32, "no meat", 15))
        parts.append(_c_arrow(574, y + 26, 624))
        parts.append(_c_box(626, y, 190, 52, response_fill))
        parts.append(_c_text(721, y + 32, response, 15))
    return _c_canvas(w, h, "\n".join(parts))


# --- blocking: a prior cue predicts, so the second cue is never learned -----


def blocking_phases() -> str:
    """Three panels: a prior cue predicts the outcome, and the second cue is never paired with it.

    The test panel carries both cues. Showing only the light would leave the reader
    unable to tell a failed association from a dead animal, and the point of Kamin's
    demonstration is the contrast: the tone still works, the light never learned.
    """
    w, panel_w, gap, top, box_h, box_gap = 940, 292, 20, 56, 40, 22
    panel_h = 330
    h = top + panel_h + 74
    parts = [_c_text(20, 30, "The three phases of a blocking experiment", 18, "start")]

    def column(
        x: float, y: float, width: float, label: str, fill: str, size: int = 15
    ) -> list[str]:
        """A single labelled box."""
        return [
            _c_box(x, y, width, box_h, fill),
            _c_text(x + width / 2, y + 25, label, size),
        ]

    # Phase 1: the tone alone comes to predict the food.
    x = 20
    parts.append(
        f"<rect x='{x:g}' y='{top:g}' width='{panel_w:g}' height='{panel_h:g}' rx='10' fill='#ffffff' stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(_c_text(x + panel_w / 2, top + 28, "phase 1", 17))
    bx, bw = x + 22, panel_w - 44
    for j, (label, fill) in enumerate(
        (("tone", STAGE), ("food", STAGE), ("response", OUTCOME))
    ):
        by = top + 46 + j * (box_h + box_gap)
        parts += column(bx, by, bw, label, fill)
        if j:
            parts.append(
                _c_v_arrow(
                    bx + bw / 2, by - box_gap, by, MARK if label == "food" else INK
                )
            )

    # Phase 2: the same pairing continues, with the light inserted just before the tone.
    # The light's arrow is grey, because the light merely precedes the tone rather than
    # predicting the food; orange marks a cue that predicts the food.
    x = 20 + panel_w + gap
    parts.append(
        f"<rect x='{x:g}' y='{top:g}' width='{panel_w:g}' height='{panel_h:g}' rx='10' fill='#ffffff' stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(_c_text(x + panel_w / 2, top + 28, "phase 2", 17))
    bx, bw = x + 22, panel_w - 44
    for j, (label, fill) in enumerate(
        (("light", ABSENT), ("tone", STAGE), ("food", STAGE), ("response", OUTCOME))
    ):
        by = top + 46 + j * (box_h + box_gap)
        parts += column(bx, by, bw, label, fill)
        if j:
            parts.append(
                _c_v_arrow(
                    bx + bw / 2, by - box_gap, by, {1: MUTED, 2: MARK}.get(j, INK)
                )
            )
    parts.append(
        _c_text(
            bx + bw / 2, top + 296, "the light comes before the tone,", 13, fill=MUTED
        )
    )
    parts.append(
        _c_text(
            bx + bw / 2,
            top + 314,
            "and is never followed by the food on its own",
            13,
            fill=MUTED,
        )
    )

    # The test: both cues presented alone, side by side, so the contrast is the picture.
    x = 20 + 2 * (panel_w + gap)
    parts.append(
        f"<rect x='{x:g}' y='{top:g}' width='{panel_w:g}' height='{panel_h:g}' rx='10' fill='#ffffff' stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(_c_text(x + panel_w / 2, top + 28, "test", 17))
    bx, bw = x + 22, panel_w - 44
    half = (bw - 12) / 2
    cue_bottom = top + 46 + box_h
    outcome_top = cue_bottom + box_gap + 34
    for k, (cue, cue_fill, outcome) in enumerate(
        (("light", ABSENT, "no response"), ("tone", STAGE, "response"))
    ):
        cx = bx + k * (half + 12)
        parts += column(cx, top + 46, half, cue, cue_fill)
        parts.append(_c_v_arrow(cx + half / 2, cue_bottom, outcome_top))
        parts += column(
            cx, outcome_top, half, outcome, OUTCOME if cue == "tone" else ABSENT, 14
        )
    parts.append(
        _c_text(
            x + panel_w / 2,
            outcome_top + box_h + 22,
            "the tone still works; the light never learned",
            13,
            fill=MARK,
        )
    )

    parts.append(
        _c_text(
            20,
            top + panel_h + 28,
            "The light is presented in phase 2 while the tone already predicts the food, so the light predicts",
            15,
            "start",
        )
    )
    parts.append(
        _c_text(
            20,
            top + panel_h + 48,
            "nothing, and the test finds no association to it, even though the tone is tested in the same phase and still works.",
            15,
            "start",
        )
    )
    return _c_canvas(w, h, "\n".join(parts))


# --- the three relations around a behaviour --------------------------------


def relations() -> str:
    """Stimulus control and occasion setting between the terms, and the habit as the response's own route to the outcome."""
    parts = [
        _i_text(120, 90, "S", 46, fill=INK, weight="bold"),
        _i_text(680, 90, "O", 46, fill=INK, weight="bold"),
        _i_text(400, 380, "R", 46, fill=INK, weight="bold"),
        _i_text(120, 122, "stimulus", 14, fill=MUTED),
        _i_text(680, 122, "outcome", 14, fill=MUTED),
        _i_text(400, 412, "response", 14, fill=MUTED),
    ]
    parts.append(_i_arrow(165, 82, 655, 82, fill=INK))
    parts.append(
        _i_text(400, 60, "classical conditioning", 16, fill=INK, style="italic")
    )
    # The source's occasion-setting arrow is the short one: it leaves the stimulus and
    # stops short of the response. Both stimulus-to-response routes necessarily run
    # the same corridor between S and R, so they are told apart by line style rather
    # than by position: stimulus control is solid and reaches R, occasion setting is
    # dashed, offset to one side, and stops short.
    parts.append(_i_arrow(150, 130, 378, 345, fill=MARK))
    parts.append(_i_arrow(185, 105, 320, 245, fill=INK, width=2.4, dash="9 7"))
    parts.append(_i_text(400, 222, "occasion setting", 16, fill=INK, style="italic"))
    parts.append(_i_arrow(448, 348, 660, 110, fill=INK))
    parts.append(_i_text(665, 268, "instrumental", 16, fill=INK, style="italic"))
    parts.append(_i_text(665, 286, "conditioning", 16, fill=INK, style="italic"))
    parts.append(_i_arrow(140, 120, 375, 342, fill=MARK, width=0))
    parts.append(_i_text(178, 250, "stimulus control", 16, fill=MARK))
    parts.append(
        _i_text(178, 268, "(a habit needs no cue)", 14, fill=MARK, style="italic")
    )
    return _i_svg(800, 440, "".join(parts))


# --- the four stages of learning from a model ------------------------------


def stages() -> str:
    """The order of the four stages, which is the whole claim: each one can fail on its own."""
    names = (
        ("Attention", ("the learner", "watches the model")),
        ("Retention", ("the behaviour is", "kept in memory")),
        ("Initiation", ("the learner", "performs it")),
        ("Motivation", ("the learner", "repeats it")),
    )
    parts = []
    for i, (name, gloss) in enumerate(names):
        x = 30.0 + i * 205
        parts.append(_i_box(x, 90, 170, 130, STAGE if i % 2 == 0 else OUTCOME))
        parts.append(_i_text(x + 85, 128, str(i + 1), 20, fill=MUTED))
        parts.append(_i_text(x + 85, 160, name, 20, fill=INK, weight="bold"))
        parts.append(_i_text(x + 85, 186, gloss[0], 13, fill=MUTED))
        parts.append(_i_text(x + 85, 204, gloss[1], 13, fill=MUTED))
        if i < 3:
            parts.append(_i_arrow(x + 172, 155, x + 201, 155))
    parts.append(
        _i_text(
            430, 70, "each stage can fail on its own", 15, fill=MARK, style="italic"
        )
    )
    return _i_svg(870, 250, "".join(parts))


# --- the three causal structures a correlation is compatible with ----------


def causal_directions() -> str:
    width, height = 800, 366
    box_w, box_h = 190, 46
    left_x, right_x = 250, 566
    parts = _r_head(width, height)

    # One row per structure, top to bottom: A causes B, B causes A, and a
    # third variable causing both.  The two boxes of the third row are
    # stacked so the pair of arrows reads as one common cause.  Each row is
    # named, so the figure carries its own claim rather than relying on the
    # prose to say which arrow means what.
    rows = (
        ("the first causes the second", "Facebook", "Depression", 34),
        ("the second causes the first", "Depression", "Facebook", 150),
        ("a third variable causes both", "No friends", None, 262),
    )
    for label, left_body, right_body, top in rows:
        centre = top + box_h / 2
        parts.append(_r_text(30, centre + 6, label, 16, "start"))
        if right_body is not None:
            parts += _r_box(left_x, top, box_w, box_h, left_body)
            parts += _r_box(right_x, top, box_w, box_h, right_body)
            parts += _r_arrow(left_x + box_w + 8, centre, right_x - 8, centre)
            continue
        # The common-cause row: the cause sits level with two stacked outcomes.
        for index, target in enumerate(("Facebook", "Depression")):
            parts += _r_box(right_x, top - 30 + index * 60, box_w, box_h, target)
        parts += _r_box(left_x, top, box_w, box_h, left_body)
        parts += _r_arrow(left_x + box_w + 8, centre, right_x - 8, top - 30 + box_h / 2)
        parts += _r_arrow(left_x + box_w + 8, centre, right_x - 8, top + 30 + box_h / 2)

    parts.append("</svg>")
    return "\n".join(parts) + "\n"


FIGURES = {
    "classical_conditioning_extinction.svg": extinction_sequence,
    "classical_conditioning_blocking.svg": blocking_phases,
    "conditioning_relations.svg": relations,
    "observational_learning_stages.svg": stages,
    "correlation_causal_directions.svg": causal_directions,
}


def main(argv: Sequence[str] | None = None) -> None:
    """Write every figure beside this script, or into the directory named by ``--outdir``."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outdir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args(argv)
    outdir: Path = args.outdir
    outdir.mkdir(parents=True, exist_ok=True)
    for name, build in FIGURES.items():
        (outdir / name).write_text(build(), encoding="utf-8")
        print(f"wrote {fspath(outdir / name)}")


def __main__() -> None:
    """Regenerate the figures in place."""
    main()


if __name__ == "__main__":
    __main__()
