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

The figures added when the brain unit came through record the same kind of
empty search:

- ``brain_division_naming.svg`` — the nesting of the five embryological
  subdivisions against forebrain, midbrain, and hindbrain, with the brain
  stem crossing the hindbrain group through the pons. Searching Commons for
  "forebrain midbrain hindbrain subdivisions" returns
  ``File:EmbryonicBrain-pl.svg`` and ``File:EmbryonicBrain.svg``, which draw
  embryonic vesicles and stop before the adult structures the note needs,
  plus scanned journal volumes. Nothing shows the two schemes overlapping.
- ``split_brain_test_setup.svg`` — the construction the split-brain method
  rests on: a fixation point, the hemifield each retinal half reaches, and
  the cut corpus callosum. Searching for "split-brain patient test" returns
  a paper on moral judgement and historical surgery PDFs. The only diagram
  of the setup found belongs to the lecture slides, which are course
  material and cannot be reused as a figure.
- ``split_brain_word_display.svg``: two words, one to each visual field, and
  the two responses they allow, the left hand pointing out HAT and the word
  BAND spoken aloud. Searching Commons for "split brain", "split brain
  experiment", "split brain patient diagram", "split brain hat band",
  "corpus callosum severed experiment", "hemispheres word hat band", and
  "word flashed visual field patient" returns scanned journal volumes and
  unrelated papers, and nothing drawn from this experiment. The one title
  that matches the name, ``File:Split-Brain Beispiel.svg`` (CC BY-SA 4.0,
  Tourar), is a computer-cluster diagram: two groups of nodes around a
  failed node and two schedulers, not a brain, so it is not a match.
  ``SplitBrainExperiments.jpg``, archived here, draws the patient at the
  table and leaves the two words out.

A figure added with the artificial intelligence unit, and the four searches behind
it: ``face_trait_space.svg`` places one schematic face three times in the space
the two primary trait dimensions span, trustworthiness across and dominance up,
so that a single trait moves between neighbouring placements. It is generated
because no drawing of that space exists on Commons. The searches for "Oosterhof
Todorov face", "face trait dimensions", "trustworthiness dominance face", and
"social perception face space" return papers on attractiveness, age estimation
and body perception, plus scanned books, and none of them draws the axes.

``autonomic_nervous_system.svg`` carries the stress unit's paired organ effects.
Searching Commons for "autonomic nervous system sympathetic parasympathetic"
returns diagrams of the same subject, among them ``File:Parasympathetic and
sympathetic.png`` and the German ``File:Das vegetative Nervensystem.png``. The
note needs one thing from them, the five pairs of opposing effects stated as
labels, so the figure here states exactly those pairs and nothing else: each
organ in a box, the sympathetic effect on its left, the parasympathetic effect
on its right.

The figure for the disciplines closes a search that found only substitutes:

- ``cognitive_science_hexagon.svg`` — the six disciplines at a hexagon's
  corners, the five hybrid fields inside it, and a ring on psychology and on
  artificial intelligence. Searching Commons for "cognitive science hexagon"
  returns ``File:Cognitive Science Hexagon.svg`` and its translations, which
  draw a picture at each corner beside its name and leave the interior empty, so
  none of them carries the hybrid fields or the two rings this note needs.

One figure closes a search that found only partly labelled substitutes:

- ``eye_section.svg`` — a horizontal section of the eye with every part the note
  names labelled, and two rays crossing at the lens to show the inverted image.
  Searching Commons for "human eye cross section labelled", "eye anatomy diagram",
  and "eye cross section cornea lens retina" returns
  ``File:Schematic diagram of the human eye en.svg`` (archived here) and its
  multilingual siblings, whose left-hand labels are clipped
  ("Suspensory ligaments of lens", "Ciliary body") and whose cornea, pupil,
  aqueous humour and iris are unnamed; ``File:Eye-diagram.svg``, which numbers
  thirty parts with no names; ``File:Three Internal chambers of the Eye.svg``,
  which names only the vitreous chamber; and ``File:Simple diagram of human eye
  multilingual.svg``, which numbers every part and names none. None of them
  labels the parts the note's cards ask about, so the figure is generated.

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
PROTECT = "#1a7f5a"  # the arrow that marks a protective direction
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


# --- brain vocabulary (from the former generate_brain_figures)

LEFT_HEMI = "#1f3864"  # fibres that run to the left hemisphere
RIGHT_HEMI = "#c2410c"  # fibres that run to the right hemisphere


def _b_text(
    x: float,
    y: float,
    body: str,
    size: float = 16,
    anchor: str = "middle",
    fill: str = LABEL,
    style: str = "normal",
    weight: str = "normal",
) -> str:
    return (
        f"<text x='{x:g}' y='{y:g}' {FONT} font-size='{size}' font-style='{style}' "
        f"font-weight='{weight}' text-anchor='{anchor}' fill='{fill}'>{body}</text>"
    )


def _b_head(width: int, height: int) -> list[str]:
    return [
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {width} {height}' "
        f"width='{width}' height='{height}'>",
        f"<rect width='{width}' height='{height}' fill='#ffffff'/>",
    ]


def _b_bracket(x: float, y1: float, y2: float, towards: float) -> str:
    """A span marker: a vertical rule at ``x`` with ticks pointing at ``towards``."""
    return (
        f"<path d='M {towards:g} {y1:g} L {x:g} {y1:g} L {x:g} {y2:g} "
        f"L {towards:g} {y2:g}' fill='none' stroke='{MUTED}' stroke-width='1.8'/>"
    )


def _b_affix_text(
    x: float,
    y: float,
    prefix: str,
    rest: str,
    size: int = 12,
    anchor: str = "middle",
    fill: str = MUTED,
) -> str:
    """A word whose ``prefix`` is set apart from ``rest``, for names that differ
    only in that prefix and share the rest."""
    return (
        f"<text x='{x:g}' y='{y:g}' {FONT} font-size='{size}' "
        f"text-anchor='{anchor}' fill='{fill}'>"
        f"<tspan font-weight='bold' fill='{INK}'>{prefix}</tspan>"
        f"<tspan font-style='italic'>{rest}</tspan></text>"
    )


# --- one brain, three naming schemes --------------------------------------


def division_naming() -> str:
    """The overlap that makes brain nomenclature hard: the same structures named by
    development, by anatomy, and by function, with the brain stem cutting across
    the hindbrain group through the pons."""
    width, height = 1040, 430
    parts = _b_head(width, height)

    parts.append(
        _b_text(
            width / 2,
            26,
            "Mammalian brain divisions, named three ways",
            17,
            weight="bold",
        )
    )

    mid_x, mid_w = 250.0, 330.0
    parts.append(
        _b_text(
            mid_x + (mid_w + 358) / 2,
            56,
            "structure, with its embryological name below",
            13,
            fill=MUTED,
        )
    )
    parts.append(_b_text(850, 56, "functional division", 13, fill=MUTED))

    # Each embryological name is the same ``-encephalon`` tail under a prefix
    # that names the structure, so the prefix is what carries the difference.
    rows = (
        ("Cerebral hemispheres", "tel", "encephalon", 74.0, 52.0),
        ("Thalamus and hypothalamus", "di", "encephalon", 140.0, 46.0),
        ("Midbrain", "mesen", "encephalon", 200.0, 46.0),
        ("Pons", "meten", "encephalon", 260.0, 46.0),
        ("Medulla", "myelen", "encephalon", 320.0, 46.0),
    )
    extents: dict[str, tuple[float, float]] = {}
    for name, prefix, rest, top, box_h in rows:
        parts.append(
            f"<rect x='{mid_x:g}' y='{top:g}' width='{mid_w:g}' height='{box_h:g}' "
            f"rx='4' fill='{STAGE}' stroke='{INK}' stroke-width='2'/>"
        )
        centre = top + box_h / 2
        extents[name] = (top, top + box_h)
        parts.append(_b_text(mid_x + mid_w / 2, centre - 4, name, 15, weight="bold"))
        parts.append(_b_affix_text(mid_x + mid_w / 2, centre + 15, prefix, rest))

    # The cerebellum shares the pons' row.  Putting the two side by side is what
    # makes both the hindbrain group and the brain-stem group contiguous.
    cel_x, cel_w, cel_y, cel_h = 608.0, 172.0, 260.0, 46.0
    parts.append(
        f"<rect x='{cel_x:g}' y='{cel_y:g}' width='{cel_w:g}' height='{cel_h:g}' "
        f"rx='4' fill='{STAGE}' stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(
        _b_text(cel_x + cel_w / 2, cel_y + 19, "Cerebellum", 15, weight="bold")
    )
    parts.append(_b_affix_text(cel_x + cel_w / 2, cel_y + 37, "meten", "encephalon"))

    # The two structures the cerebellum shares its embryological name with sit
    # in the column, so the offset box needs a tie back to the pons' row.  Drawn
    # before the brain-stem outline, which then runs across it.
    parts.append(
        f"<line x1='{mid_x + mid_w:g}' y1='{cel_y + cel_h / 2:g}' "
        f"x2='{cel_x:g}' y2='{cel_y + cel_h / 2:g}' stroke='{MUTED}' "
        "stroke-width='1.6'/>"
    )

    # Brain stem.  One definition spans the diencephalon as well, so the outline
    # reaches up to the thalamus and hypothalamus and so crosses both of the
    # other schemes, while still stopping short of the cerebellum beside the pons.
    stem_x = mid_x - 14.0
    stem_top = extents["Thalamus and hypothalamus"][0] - 8.0
    stem_bottom = extents["Medulla"][1] + 8.0
    parts.append(
        f"<rect x='{stem_x:g}' y='{stem_top:g}' width='{mid_w + 28:g}' "
        f"height='{stem_bottom - stem_top:g}' rx='10' fill='none' stroke='{MARK}' "
        f"stroke-width='2' stroke-dasharray='7 5'/>"
    )
    parts.append(
        _b_text(
            stem_x - 10,
            (stem_top + stem_bottom) / 2 + 5,
            "brain stem",
            13,
            anchor="end",
            fill=MARK,
            style="italic",
        )
    )

    # Functional divisions on the right: forebrain, midbrain, hindbrain.  A
    # bracket spans its boxes end to end, so a single-box division still draws a
    # bracket the height of that box rather than a flat tick.
    br_x = 836.0
    spans = (
        (
            "Forebrain",
            extents["Cerebral hemispheres"][0],
            extents["Thalamus and hypothalamus"][1],
        ),
        ("Midbrain", extents["Midbrain"][0], extents["Midbrain"][1]),
        ("Hindbrain", extents["Pons"][0], extents["Medulla"][1]),
    )
    for label, y1, y2 in spans:
        parts.append(_b_bracket(br_x, y1, y2, br_x + 14))
        parts.append(
            _b_text(
                br_x + 22, (y1 + y2) / 2 + 5, label, 15, anchor="start", weight="bold"
            )
        )

    parts.append(
        _b_text(
            width / 2,
            412,
            "the brain stem takes the thalamus and hypothalamus from the forebrain and the pons from the hindbrain",
            13,
            fill=MARK,
            style="italic",
        )
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


# --- the split-brain testing setup ----------------------------------------


def split_brain_setup() -> str:
    """The construction the method rests on: fibres from the nasal retina cross at
    the chiasm, so a hemifield reaches the opposite hemisphere, and a cut corpus
    callosum keeps it there."""
    width, height = 1000, 560
    parts = _b_head(width, height)

    # The screen.  A fixation point is what makes one hemifield reachable alone.
    parts.append(
        f"<rect x='250' y='40' width='500' height='72' rx='4' fill='{OUTCOME}' "
        f"stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(
        f"<line x1='500' y1='62' x2='500' y2='92' stroke='{INK}' stroke-width='2.4'/>"
    )
    parts.append(
        f"<line x1='485' y1='77' x2='515' y2='77' stroke='{INK}' stroke-width='2.4'/>"
    )
    parts.append(
        f"<rect x='292' y='62' width='96' height='30' rx='3' fill='{RIGHT_HEMI}' fill-opacity='0.18' "
        f"stroke='{RIGHT_HEMI}' stroke-width='2'/>"
    )
    parts.append(_b_text(340, 82, "stimulus", 13, fill=RIGHT_HEMI))
    parts.append(
        _b_text(
            524, 81, "fixation point", 12, anchor="start", fill=MUTED, style="italic"
        )
    )
    parts.append(_b_text(236, 128, "left visual field", 12, anchor="start"))
    parts.append(_b_text(746, 128, "right visual field", 12, anchor="end"))

    # Each eye, split into a temporal and a nasal half.  The temporal side is
    # the outer one, so it points away from the midline in both eyes.
    for cx, temporal_x, nasal_x in ((400.0, 344.0, 452.0), (600.0, 656.0, 548.0)):
        parts.append(
            f"<circle cx='{cx:g}' cy='200' r='28' fill='{STAGE}' stroke='{INK}' stroke-width='2'/>"
        )
        parts.append(
            f"<line x1='{cx:g}' y1='172' x2='{cx:g}' y2='228' stroke='{INK}' stroke-width='1.6'/>"
        )
        parts.append(_b_text(temporal_x, 205, "temporal", 11, fill=MUTED))
        parts.append(_b_text(nasal_x, 205, "nasal", 11, fill=MUTED))
        parts.append(_b_text(cx, 252, "left eye" if cx < 500 else "right eye", 14))

    # Light from the left visual field lands on the right-hand half of each
    # retina: the nasal half of the left eye and the temporal half of the right.
    # Those are the two halves that reach the right hemisphere below.
    parts.append(
        "<defs><marker id='light' viewBox='0 0 10 10' refX='9' refY='5' "
        "markerWidth='4' markerHeight='4' orient='auto-start-reverse'>"
        f"<path d='M 0 0 L 10 5 L 0 10 z' fill='{MUTED}'/></marker></defs>"
    )
    for d in ("M 352 116 L 427 193", "M 352 116 L 627 193"):
        parts.append(
            f"<path d='{d}' fill='none' stroke='{MUTED}' stroke-width='1.5' "
            "stroke-dasharray='5 4' marker-end='url(#light)'/>"
        )

    # Which fibre colour is which.  Without this the two routes read alike.
    parts.append(
        f"<line x1='18' y1='150' x2='52' y2='150' stroke='{RIGHT_HEMI}' stroke-width='3'/>"
    )
    parts.append(
        _b_text(60, 154, "nasal fibres: cross at the chiasm", 12, anchor="start")
    )
    parts.append(
        f"<line x1='18' y1='182' x2='52' y2='182' stroke='{LEFT_HEMI}' stroke-width='3'/>"
    )
    parts.append(
        _b_text(60, 186, "temporal fibres: stay on their own side", 12, anchor="start")
    )

    # The chiasm: where the nasal fibres cross.
    parts.append(
        f"<circle cx='500' cy='300' r='9' fill='#ffffff' stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(_b_text(500, 328, "optic chiasm", 13, fill=MUTED, style="italic"))

    # Four fibres.  Each eye's nasal half crosses at the chiasm; its temporal
    # half stays on its own side.  All four start on their own circle's edge.
    fibres = (
        ("M 380 220 C 330 268 250 300 232 380", LEFT_HEMI),
        ("M 420 220 C 470 262 500 282 500 300 C 560 322 760 342 768 380", RIGHT_HEMI),
        ("M 580 220 C 530 262 500 282 500 300 C 440 322 240 342 232 380", LEFT_HEMI),
        ("M 620 220 C 670 268 750 300 768 380", RIGHT_HEMI),
    )
    for d, colour in fibres:
        parts.append(
            f"<path d='{d}' fill='none' stroke='{colour}' stroke-width='2.6'/>"
        )

    # The two hemispheres, and the cut between them.
    for x, body, sub in (
        (140.0, "left hemisphere", "speaks; controls the right hand"),
        (620.0, "right hemisphere", "does not speak; controls the left hand"),
    ):
        parts.append(
            f"<rect x='{x:g}' y='380' width='240' height='62' rx='4' fill='{OUTCOME}' "
            f"stroke='{INK}' stroke-width='2'/>"
        )
        parts.append(_b_text(x + 120, 404, body, 15, weight="bold"))
        parts.append(_b_text(x + 120, 425, sub, 12, fill=MUTED))

    parts.append(
        f"<line x1='380' y1='411' x2='446' y2='411' stroke='{INK}' stroke-width='6' stroke-linecap='round'/>"
    )
    parts.append(
        f"<line x1='554' y1='411' x2='620' y2='411' stroke='{INK}' stroke-width='6' stroke-linecap='round'/>"
    )
    parts.append(
        f"<line x1='470' y1='393' x2='530' y2='429' stroke='{RIGHT_HEMI}' stroke-width='3'/>"
    )
    parts.append(
        f"<line x1='530' y1='393' x2='470' y2='429' stroke='{RIGHT_HEMI}' stroke-width='3'/>"
    )
    parts.append(
        _b_text(500, 462, "corpus callosum, cut", 13, fill=MARK, style="italic")
    )

    parts.append(
        _b_text(
            width / 2,
            510,
            "the nasal half of each eye crosses at the chiasm, the temporal half does not,",
            14,
            fill=INK,
        )
    )
    parts.append(
        _b_text(
            width / 2,
            534,
            "so the stimulus reaches only the right hemisphere and stays there",
            14,
            fill=INK,
        )
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


# --- one word to each visual field ----------------------------------------


def split_brain_word_display() -> str:
    """Two words, one to each field, and the two responses they allow: the left
    hand points out HAT, which only the silent right hemisphere saw, and speech
    names BAND, which only the left hemisphere saw, because the cut corpus
    callosum stops either word crossing the midline."""
    width, height = 1000, 620
    parts = _b_head(width, height)

    # The field labels sit above the screen, so nothing crowds the space the two
    # leads and the arm's own lead run through.
    parts.append(_b_text(196, 32, "left visual field", 12, anchor="start"))
    parts.append(_b_text(804, 32, "right visual field", 12, anchor="end"))
    parts.append(
        f"<rect x='190' y='44' width='620' height='72' rx='4' fill='{OUTCOME}' "
        f"stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(_b_text(300, 88, "HAT", 28, fill=INK, weight="bold"))
    parts.append(_b_text(700, 88, "BAND", 28, fill=INK, weight="bold"))
    parts.append(
        f"<line x1='500' y1='64' x2='500' y2='96' stroke='{INK}' stroke-width='2.4'/>"
        f"<line x1='480' y1='80' x2='520' y2='80' stroke='{INK}' stroke-width='2.4'/>"
    )

    # The spoken response, in a bubble whose tail reaches the head from behind.
    # The tail is drawn before the head, which closes it off.
    parts.append(
        f"<path d='M 722 206 L 688 284 L 722 246 Z' fill='#ffffff' "
        f"stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(
        f"<rect x='720' y='170' width='255' height='80' rx='14' fill='#ffffff' "
        f"stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(_b_text(847, 222, "BAND", 26, fill=INK, weight="bold"))
    parts.append(_b_text(847, 276, "spoken aloud", 13, fill=MUTED))

    # The patient, seen from above and facing the screen: a torso, the left arm
    # raised, and the head around the brain.  The arm is an outlined tube, so the
    # hand reads as its end rather than as a separate mark.
    parts.append(
        f"<line x1='368' y1='492' x2='205' y2='355' stroke='{INK}' "
        "stroke-width='24' stroke-linecap='round'/>"
    )
    parts.append(
        "<line x1='368' y1='492' x2='205' y2='355' stroke='#ffffff' "
        "stroke-width='19' stroke-linecap='round'/>"
    )
    parts.append(
        f"<rect x='320' y='468' width='360' height='62' rx='26' fill='#ffffff' "
        f"stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(_b_text(500, 506, "patient, from above", 12, fill=MUTED))
    parts.append(
        f"<circle cx='205' cy='355' r='14' fill='#ffffff' stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(
        f"<ellipse cx='500' cy='300' rx='190' ry='168' fill='#ffffff' "
        f"stroke='{INK}' stroke-width='2'/>"
    )

    # The brain from above: two hemispheres meeting at the midline, with the
    # callosum running along it and cut through, marked the way the setup figure
    # marks it.
    for cx, body, note in (
        (416, "left hemisphere", "speaks"),
        (584, "right hemisphere", "does not speak"),
    ):
        parts.append(
            f"<ellipse cx='{cx}' cy='300' rx='84' ry='128' fill='{OUTCOME}' "
            f"stroke='{INK}' stroke-width='2'/>"
        )
        parts.append(_b_text(cx, 296, body, 13, weight="bold"))
        parts.append(_b_text(cx, 318, note, 12, fill=MUTED))
    parts.append(
        f"<line x1='500' y1='232' x2='500' y2='284' stroke='{INK}' "
        "stroke-width='12' stroke-linecap='round'/>"
        f"<line x1='500' y1='316' x2='500' y2='368' stroke='{INK}' "
        "stroke-width='12' stroke-linecap='round'/>"
    )
    parts.append(
        f"<line x1='487' y1='286' x2='513' y2='314' stroke='{RIGHT_HEMI}' stroke-width='3.5'/>"
        f"<line x1='513' y1='286' x2='487' y2='314' stroke='{RIGHT_HEMI}' stroke-width='3.5'/>"
    )
    parts.append(
        _b_text(500, 450, "corpus callosum, cut", 12, fill=MARK, style="italic")
    )

    # Each word crosses to the hemisphere opposite the field that showed it, the
    # crossing being the point the two responses turn on.
    parts.append(
        "<defs><marker id='field' viewBox='0 0 10 10' refX='9' refY='5' "
        "markerWidth='4' markerHeight='4' orient='auto-start-reverse'>"
        f"<path d='M 0 0 L 10 5 L 0 10 z' fill='{MUTED}'/></marker></defs>"
    )
    for d in ("M 320 120 L 556 180", "M 680 120 L 444 180"):
        parts.append(
            f"<path d='{d}' fill='none' stroke='{MUTED}' stroke-width='1.6' "
            "stroke-dasharray='6 5' marker-end='url(#field)'/>"
        )

    # The manual response: the raised hand's lead stops just under the word the
    # eye of that field saw.
    parts.append(_b_text(178, 350, "left hand", 14, anchor="end", weight="bold"))
    parts.append(_b_text(178, 370, "points to HAT", 12, anchor="end", fill=MUTED))
    parts.append(
        f"<path d='M 205 339 L 285 128' fill='none' stroke='{MUTED}' stroke-width='1.6' "
        "stroke-dasharray='6 5' marker-end='url(#field)'/>"
    )

    parts.append(
        _b_text(
            width / 2,
            570,
            "the left field reaches the right hemisphere, which cannot speak but moves the left hand,",
            14,
            fill=INK,
        )
    )
    parts.append(
        _b_text(
            width / 2,
            594,
            "and the right field reaches the left hemisphere, which speaks",
            14,
            fill=INK,
        )
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def face_trait_space() -> str:
    """The space a first impression of a face is read in: trustworthiness across,
    dominance up, and one face placed three times so that only one of the two
    traits moves between neighbouring placements."""

    def face(cx: float, cy: float, brow: int, mouth: int) -> str:
        """A schematic head at ``(cx, cy)``. ``brow`` lowers the inner eyebrow ends
        by that many pixels, which is what makes a face read as dominant, and
        ``mouth`` curves the mouth upward."""
        return "".join(
            [
                f"<circle cx='{cx:g}' cy='{cy:g}' r='34' fill='#ffffff'/>",
                f"<circle cx='{cx:g}' cy='{cy:g}' r='29' fill='{OUTCOME}' "
                f"stroke='{INK}' stroke-width='1.8'/>",
                f"<circle cx='{cx - 10:g}' cy='{cy - 4:g}' r='2.8' fill='{INK}'/>",
                f"<circle cx='{cx + 10:g}' cy='{cy - 4:g}' r='2.8' fill='{INK}'/>",
                f"<line x1='{cx - 16:g}' y1='{cy - 16:g}' x2='{cx - 5:g}' "
                f"y2='{cy - 15 + brow:g}' stroke='{INK}' stroke-width='2'/>",
                f"<line x1='{cx + 5:g}' y1='{cy - 15 + brow:g}' x2='{cx + 16:g}' "
                f"y2='{cy - 16:g}' stroke='{INK}' stroke-width='2'/>",
                f"<path d='M {cx - 11:g} {cy + 11:g} Q {cx:g} {cy + 11 + mouth:g} "
                f"{cx + 11:g} {cy + 11:g}' fill='none' stroke='{INK}' "
                f"stroke-width='2' stroke-linecap='round'/>",
            ]
        )

    width, height = 780, 540
    parts = _b_head(width, height)
    parts.append(
        _b_text(
            width / 2,
            32,
            "Two trait dimensions of a first impression",
            17,
            weight="bold",
        )
    )

    origin_x, origin_y = 360.0, 300.0

    # The two axes. Drawn first and thin, so the three heads and their white
    # haloes sit on top of them rather than beside them.
    parts.append(
        f"<line x1='110' y1='{origin_y:g}' x2='680' y2='{origin_y:g}' "
        f"stroke='{MUTED}' stroke-width='1.4'/>"
        f"<line x1='{origin_x:g}' y1='470' x2='{origin_x:g}' y2='100' "
        f"stroke='{MUTED}' stroke-width='1.4'/>"
    )
    parts.append(
        f"<path d='M 680 {origin_y:g} l -12 -5 l 0 10 Z' fill='{MUTED}'/>"
        f"<path d='M {origin_x:g} 100 l -5 12 l 10 0 Z' fill='{MUTED}'/>"
    )
    parts.append(_b_text(112, origin_y - 12, "untrustworthy", 12, anchor="start"))
    parts.append(_b_text(676, origin_y - 12, "trustworthy", 12, anchor="end"))
    parts.append(_b_text(origin_x + 12, 106, "dominant", 12, anchor="start"))
    parts.append(_b_text(origin_x + 12, 462, "submissive", 12, anchor="start"))

    # Three placements of one head: the middle one, one raised on dominance,
    # one moved toward trustworthy. The brows and the mouth are the only
    # difference, and the second raised brow pair is what dominance looks like.
    parts.append(face(origin_x, origin_y, 0, 1))
    parts.append(face(origin_x, 176.0, 4, 1))
    parts.append(face(548.0, origin_y, 0, 7))
    parts.append(
        _b_text(
            origin_x + 62,
            240,
            "more dominant",
            12,
            anchor="start",
            fill=INK,
            weight="bold",
        )
    )
    parts.append(
        _b_text(548, origin_y + 60, "more trustworthy", 12, fill=INK, weight="bold")
    )

    # The two moves, each drawn from the middle head toward one neighbour.
    parts.append(
        f"<path d='M {origin_x:g} 254 L {origin_x:g} 218' fill='none' "
        f"stroke='{MARK}' stroke-width='2' stroke-dasharray='5 4'/>"
        f"<path d='M {origin_x:g} 218 l -5 9 l 10 0 Z' fill='{MARK}'/>"
        f"<path d='M 418 {origin_y:g} L 506 {origin_y:g}' fill='none' "
        f"stroke='{MARK}' stroke-width='2' stroke-dasharray='5 4'/>"
        f"<path d='M 506 {origin_y:g} l -9 -5 l 0 10 Z' fill='{MARK}'/>"
    )
    parts.append(
        _b_text(
            width / 2,
            500,
            "One trait moves at each step, and the identity stays fixed.",
            12.5,
        )
    )

    parts.append("</svg>")
    return "".join(parts)


def _autonomic_lines(
    x: float,
    centre: float,
    lines: tuple[str, ...],
    anchor: str,
    weight: str = "normal",
    fill: str = LABEL,
    size: int = 14,
) -> list[str]:
    """Stack one to three label lines around ``centre`` and return the text elements."""
    step = size + 3
    first = centre - (len(lines) - 1) * step / 2 + 5
    return [
        _i_text(x, first + index * step, line, size, anchor, weight=weight, fill=fill)
        for index, line in enumerate(lines)
    ]


def autonomic_pairs() -> str:
    """Each organ of the body between the two branches, with each branch's effect and its reason.

    No arrows join a branch to an organ. Both branches reach every organ, and the
    only thing an arrowhead could add is a direction that differs between the two
    columns for no reason: the effects are written on the side of the branch that
    has them. Each effect carries the purpose it serves, set under it in the
    muted colour, so the figure answers why as well as what.
    """
    organs_x, organ_w = 365.0, 170.0
    parts = [
        _i_text(170, 40, "sympathetic branch", 18, fill=INK, weight="bold"),
        _i_text(170, 62, "prepares the body for action", 13, fill=MUTED),
        _i_text(730, 40, "parasympathetic branch", 18, fill=INK, weight="bold"),
        _i_text(730, 62, "restores and holds equilibrium at rest", 13, fill=MUTED),
        _i_text(450, 74, "organ", 15, fill=MUTED),
    ]
    rows = (
        (
            ("eyes",),
            (("Dilates pupil",), "more light to see by"),
            (("Contracts pupil",), "less light, finer detail"),
        ),
        (
            ("lungs",),
            (("Relaxes bronchi",), "more air per breath"),
            (("Constricts bronchi",), "resting air flow"),
        ),
        (
            ("heart",),
            (("Accelerates and", "strengthens heartbeat"), "blood to the muscles"),
            (("Slows heartbeat",), "energy saved"),
        ),
        (
            ("stomach and", "intestines"),
            (("Inhibits activity",), "blood sent elsewhere"),
            (("Stimulates activity",), "food digested"),
        ),
        (
            ("blood vessels of", "the internal organs"),
            (("Contracts vessels",), "blood pushed to muscle"),
            (("Dilates vessels",), "organs run normally"),
        ),
    )
    for index, (organ, sympathetic, parasympathetic) in enumerate(rows):
        centre = 152 + index * 96
        parts.append(_i_box(organs_x, centre - 23, organ_w, 46, "#ffffff", rx=6))
        parts += _autonomic_lines(
            organs_x + organ_w / 2, centre, organ, "middle", "bold"
        )
        for side, (effect, reason) in enumerate((sympathetic, parasympathetic)):
            anchor = "end" if side == 0 else "start"
            x = 348 if side == 0 else 552
            parts += _autonomic_lines(x, centre - 9, effect, anchor)
            parts += _autonomic_lines(
                x, centre + 22, (reason,), anchor, fill=MUTED, size=12
            )
    parts.append(
        _i_text(
            450,
            606,
            "each branch acts on the same organs, in opposite directions",
            15,
            fill=MARK,
            style="italic",
        )
    )
    return _c_canvas(900, 630, "".join(parts))


def _s_box(x: float, y: float, w: float, h: float, label: str) -> list[str]:
    """One named box of the stress chain, its label centred inside it."""
    return [
        _i_box(x, y, w, h, OUTCOME),
        _i_text(x + w / 2, y + h / 2 + 6, label, 17, fill=LABEL, weight="bold"),
    ]


def _s_marker(x: float, y1: float, y2: float, fill: str) -> str:
    """A heavy arrow beside a box, pointing up for protection or down for risk."""
    return _i_arrow(x, y1, x, y2, fill=fill, width=7, head=20)


def stress_chain() -> str:
    """Positive affect into stress, then the behavioural and the activation route into disease."""
    protect, risk = PROTECT, MARK
    parts: list[str] = []
    parts += _s_box(190, 50, 230, 70, "positive affect")
    parts += _s_box(190, 175, 230, 70, "stress")
    parts += _s_box(60, 305, 250, 70, "healthy behaviour")
    parts += _s_box(340, 305, 250, 70, "psychological activation")
    parts += _s_box(205, 440, 200, 70, "disease")
    parts.append(_i_arrow(305, 124, 305, 175, fill=INK, width=2.5, head=13))
    parts.append(_i_arrow(255, 245, 200, 305, fill=INK, width=2.5, head=13))
    parts.append(_i_arrow(355, 245, 430, 305, fill=INK, width=2.5, head=13))
    parts.append(_i_arrow(225, 375, 270, 440, fill=INK, width=2.5, head=13))
    parts.append(_i_arrow(430, 375, 340, 440, fill=INK, width=2.5, head=13))
    parts.append(_s_marker(125, 122, 52, protect))
    parts.append(_s_marker(490, 173, 243, risk))
    parts.append(_s_marker(28, 377, 307, protect))
    parts.append(_s_marker(622, 303, 373, risk))
    parts.append(_s_marker(452, 438, 508, risk))
    parts.append(_i_text(240, 552, "upward arrow: protection", 14, fill=protect))
    parts.append(_i_text(520, 552, "downward arrow: risk", 14, fill=risk))
    return _c_canvas(700, 580, "".join(parts))


# Helvetica advance widths, in units of 1000 em, for the lowercase letters and
# the space. A ring is sized and centred from its own label's measured width,
# because a count of characters puts the ring off by most of a letter.
_HELVETICA_ADVANCE = {
    " ": 278,
    "a": 556,
    "b": 556,
    "c": 500,
    "d": 556,
    "e": 556,
    "f": 278,
    "g": 556,
    "h": 556,
    "i": 222,
    "j": 222,
    "k": 500,
    "l": 222,
    "m": 833,
    "n": 556,
    "o": 556,
    "p": 556,
    "q": 556,
    "r": 333,
    "s": 500,
    "t": 278,
    "u": 556,
    "v": 500,
    "w": 722,
    "x": 500,
    "y": 500,
    "z": 500,
}


def _helvetica_width(text: str, size: float) -> float:
    """The width ``text`` takes at ``size``, from Helvetica's advance widths."""
    return sum(_HELVETICA_ADVANCE[char] for char in text) * size / 1000


def cognitive_science_hexagon() -> str:
    """The six disciplines at a hexagon's corners, joined by the chords their hybrids sit on.

    Every corner is joined to two others by an interior chord, and each hybrid is
    written along the chord joining the two disciplines that form it, so the
    drawing shows which pair of fields produces which subject instead of stating
    the relations only in the prose.
    """
    cx, cy, r = 430.0, 350.0, 230.0
    corners = (
        ("philosophy", -90.0),
        ("linguistics", -30.0),
        ("anthropology", 30.0),
        ("neuroscience", 90.0),
        ("artificial intelligence", 150.0),
        ("psychology", 210.0),
    )
    at = {
        name: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
        for name, a in corners
    }
    size = 17
    parts: list[str] = []
    ring = "".join(f"{x:g},{y:g} " for x, y in at.values()).strip()
    parts.append(
        f"<polygon points='{ring}' fill='#fbfcf0' stroke='#9fc3a8' stroke-width='2.4'/>"
    )
    # Each hybrid lies on the chord between the two disciplines that form it,
    # set a little off the line so the two that cross at the centre stay apart.
    links = (
        ("psycholinguistics", "psychology", "linguistics", 0.50, -7.0),
        ("cognitive psychology", "psychology", "artificial intelligence", 0.50, 8.0),
        (
            "computational linguistics",
            "linguistics",
            "artificial intelligence",
            0.68,
            9.0,
        ),
        ("cognitive neuroscience", "neuroscience", "psychology", 0.26, -9.0),
        (
            "computational neuroscience",
            "artificial intelligence",
            "neuroscience",
            0.50,
            9.0,
        ),
    )
    for label, first, second, along, off in links:
        (x1, y1), (x2, y2) = at[first], at[second]
        parts.append(
            f"<line x1='{x1:g}' y1='{y1:g}' x2='{x2:g}' y2='{y2:g}' "
            f"stroke='#9fc3a8' stroke-width='1.6'/>"
        )
        mx, my = x1 + (x2 - x1) * along, y1 + (y2 - y1) * along
        length = math.hypot(x2 - x1, y2 - y1)
        mx += -(y2 - y1) / length * off
        my += (x2 - x1) / length * off
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        if angle > 90 or angle <= -90:
            angle += 180
        parts.append(
            f"<g transform='translate({mx:g},{my:g}) rotate({angle:g})'>"
            + _i_text(0, 5, label, 15, fill=MUTED)
            + "</g>"
        )
    # The six disciplines are written outside their own corner, the two side
    # ones pushed clear of the edges they sit on.
    outside = (
        ("philosophy", 0.0, -20.0, "middle"),
        ("linguistics", 16.0, 6.0, "start"),
        ("anthropology", 16.0, 6.0, "start"),
        ("neuroscience", 0.0, 30.0, "middle"),
        ("artificial intelligence", -16.0, 6.0, "end"),
        ("psychology", -16.0, 6.0, "end"),
    )
    for name, dx, dy, anchor in outside:
        x, y = at[name]
        if " " in name:
            first, second = name.split(" ", 1)
            parts.append(
                _i_text(x + dx, y + dy - 9, first, size, anchor=anchor, fill=INK)
            )
            parts.append(
                _i_text(x + dx, y + dy + 11, second, size, anchor=anchor, fill=INK)
            )
        else:
            parts.append(_i_text(x + dx, y + dy, name, size, anchor=anchor, fill=INK))
    return _c_canvas(790, 645, "".join(parts))


def _e_text(
    x: float, y: float, body: str, size: int = 15, anchor: str = "start"
) -> str:
    """One label of the eye section, in the shared label colour."""
    return _i_text(x, y, body, size, anchor=anchor, fill=LABEL)


def _e_lead(x1: float, y1: float, x2: float, y2: float) -> str:
    """A leader from a label to the part it names, ending in a dot on that part."""
    return (
        f"<line x1='{x1:g}' y1='{y1:g}' x2='{x2:g}' y2='{y2:g}' stroke='{MUTED}' stroke-width='1.2'/>"
        f"<circle cx='{x2:g}' cy='{y2:g}' r='3' fill='{MUTED}'/>"
    )


def eye_section() -> str:
    """A horizontal section of the right eye, light entering from the left.

    The parts are drawn in the order light meets them, so the drawing carries
    the sequence the prose states. Two rays leave one point above the axis,
    bend at the lens, and meet again below the axis on the retina, which is
    what makes the image inverted.
    """
    cx, cy, r = 420.0, 330.0, 170.0
    parts: list[str] = []
    parts.append(
        f"<circle cx='{cx:g}' cy='{cy:g}' r='{r:g}' fill='#fbe6cf' stroke='{INK}' stroke-width='2'/>"
    )
    parts.append(
        "<path d='M 499,193 A 158,158 0 0 1 499,467' fill='none' stroke='#d97706' stroke-width='9'/>"
    )
    parts.append(
        "<path d='M 311,200 C 175,240 175,420 311,460' fill='none' stroke='#a8c8e8' stroke-width='16'/>"
    )
    for y in (200.0, 344.0):
        parts.append(
            f"<rect x='318' y='{y:g}' width='38' height='86' fill='#8b5a2b' stroke='{INK}' stroke-width='1.4'/>"
        )
    parts.append(
        f"<ellipse cx='390' cy='330' rx='34' ry='74' fill='#cfe3f5' stroke='{INK}' stroke-width='1.8'/>"
    )
    parts.append(
        "<polygon points='536,449 556,410 716,486 690,528' fill='#f6e3b0' stroke='#1f3864' stroke-width='1.4'/>"
    )
    parts.append(
        f"<ellipse cx='550' cy='416' rx='13' ry='21' transform='rotate(34 550 416)' fill='#c8c8c8' stroke='{INK}' stroke-width='1.2'/>"
    )
    parts.append(f"<circle cx='572' cy='330' r='6' fill='{MARK}'/>")
    for path in (
        "M 30,250 L 390,314 L 580,373",
        "M 30,318 L 390,338 L 580,373",
    ):
        parts.append(
            f"<path d='{path}' fill='none' stroke='{MARK}' stroke-width='1.6'/>"
        )
    parts.append(_e_text(18, 150, "cornea"))
    parts.append(_e_lead(100, 155, 246, 268))
    parts.append(_e_text(300, 118, "pupil", anchor="middle"))
    parts.append(_e_lead(312, 128, 337, 302))
    parts.append(_e_text(505, 150, "iris"))
    parts.append(_e_lead(500, 158, 356, 218))
    parts.append(_e_text(18, 560, "aqueous humour"))
    parts.append(_e_lead(160, 552, 287, 404))
    parts.append(_e_text(438, 96, "lens", anchor="middle"))
    parts.append(_e_lead(438, 106, 396, 258))
    parts.append(_e_text(400, 470, "vitreous humour", anchor="middle"))
    parts.append(_e_text(700, 230, "retina"))
    parts.append(_e_lead(690, 236, 559, 256))
    parts.append(_e_text(700, 310, "fovea"))
    parts.append(_e_lead(690, 316, 572, 330))
    parts.append(_e_text(700, 390, "blind spot"))
    parts.append(_e_lead(690, 396, 553, 412))
    parts.append(_e_text(620, 615, "optic nerve", anchor="middle"))
    parts.append(_e_lead(640, 600, 668, 512))
    return _c_canvas(790, 640, "".join(parts))


FIGURES = {
    "eye_section.svg": eye_section,
    "autonomic_nervous_system.svg": autonomic_pairs,
    "stress_to_disease.svg": stress_chain,
    "classical_conditioning_extinction.svg": extinction_sequence,
    "classical_conditioning_blocking.svg": blocking_phases,
    "conditioning_relations.svg": relations,
    "observational_learning_stages.svg": stages,
    "correlation_causal_directions.svg": causal_directions,
    "brain_division_naming.svg": division_naming,
    "split_brain_test_setup.svg": split_brain_setup,
    "split_brain_word_display.svg": split_brain_word_display,
    "face_trait_space.svg": face_trait_space,
    "cognitive_science_hexagon.svg": cognitive_science_hexagon,
}


def _normalise_trailing_newline(svg: str) -> str:
    """Return ``svg`` ending in exactly one newline, whatever it ended in before."""
    text = svg.rstrip() + "\n"
    # A tripwire, not a check. The strip above cannot fail; this is here so a
    # later edit to that line cannot bring back the defect this prevents.
    assert text.endswith("\n") and not text.endswith("\n\n"), repr(text[-20:])
    return text


def main(argv: Sequence[str] | None = None) -> None:
    """Write every figure beside this script, or into the directory named by ``--outdir``."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outdir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args(argv)
    outdir: Path = args.outdir
    outdir.mkdir(parents=True, exist_ok=True)
    for name, build in FIGURES.items():
        (outdir / name).write_text(
            _normalise_trailing_newline(build()), encoding="utf-8"
        )
        print(f"wrote {fspath(outdir / name)}")


def __main__() -> None:
    """Regenerate the figures in place."""
    main()


if __name__ == "__main__":
    __main__()
