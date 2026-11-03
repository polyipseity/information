#!/usr/bin/env python
"""Draw the course's definitional figures that no free image covers.

Searched Wikimedia Commons first, and these came up empty, so they are drawn
here: "moral compass spectrum" returns compass roses and a patent drawing,
and "五常" returns the place in Wuhan.

The moral compass spectrum reproduces the course's own drawing: five terms in
a row, each slightly tilted, over a bar reading "Power and Culture", with the
definition that separates each term from its neighbours. Every position is
computed from one row of constants, so widening a label or changing a term
cannot push a box into its neighbour.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent

FONT = "DejaVu Sans, Helvetica, Arial, sans-serif"

TERMS: tuple[tuple[str, str, float], ...] = (
    ("Justice", "administering of deserved punishment or reward", -12.0),
    (
        "Laws",
        "a rule of conduct or action recognized as enforced by a controlling authority",
        -6.0,
    ),
    ("Rules", "accepted procedure, custom, or habit", 0.0),
    ("Ethics", "principles of conduct governing an individual or a group", 6.0),
    ("Morals", "conforming to a standard of right behavior", 12.0),
)

CANVAS_W = 1060
CANVAS_H = 560
ROW_Y = 330.0
BOX_W = 150.0
BOX_H = 96.0
GAP = 24.0
LABEL_SIZE = 22
CARD_SIZE = 14
CARD_PAD = 12.0
CARD_WRAP = 30
CARD_Y = (168.0, 62.0, 168.0, 62.0, 168.0)
ARCH_Y = 470.0
ARCH_H = 46.0


def wrap(text: str, limit: int) -> list[str]:
    """Break *text* into lines no longer than *limit* characters."""
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if len(candidate) <= limit:
            current = candidate
            continue
        lines.append(current)
        current = word
    lines.append(current)
    return lines


def row_left(index: int) -> float:
    """Return the left edge of box *index* in a row centred on the canvas."""
    width = len(TERMS) * BOX_W + (len(TERMS) - 1) * GAP
    return (CANVAS_W - width) / 2 + index * (BOX_W + GAP)


def term_box(index: int, term: str, tilt: float) -> list[str]:
    left = row_left(index)
    cx = left + BOX_W / 2
    base = ROW_Y + BOX_H / 2
    return [
        f'  <g transform="translate({cx:.1f} {base:.1f}) rotate({tilt:.1f})">',
        f'    <rect x="{-BOX_W / 2:.1f}" y="{-BOX_H / 2:.1f}" width="{BOX_W:.1f}"'
        f' height="{BOX_H:.1f}" rx="10" fill="#1f6fb2"/>',
        f'    <text x="0" y="{LABEL_SIZE / 3:.1f}" text-anchor="middle"'
        f' font-family="{FONT}" font-size="{LABEL_SIZE}" fill="#ffffff">{term}</text>',
        "  </g>",
    ]


def definition_card(index: int, text: str) -> list[str]:
    lines = wrap(text, CARD_WRAP)
    width = max(len(line) for line in lines) * CARD_SIZE * 0.56 + 2 * CARD_PAD
    height = len(lines) * (CARD_SIZE * 1.45) + 2 * CARD_PAD
    cx = row_left(index) + BOX_W / 2
    top = CARD_Y[index]
    out = [
        f'  <line x1="{cx:.1f}" y1="{top + height:.1f}" x2="{cx:.1f}"'
        f' y2="{ROW_Y + BOX_H / 2:.1f}" stroke="#4a4a4a" stroke-width="1.5"/>',
        f'  <rect x="{cx - width / 2:.1f}" y="{top:.1f}" width="{width:.1f}"'
        f' height="{height:.1f}" rx="10" fill="#ffffff" stroke="#4a4a4a" stroke-width="2"/>',
    ]
    for row, line in enumerate(lines):
        ty = top + CARD_PAD + CARD_SIZE + row * CARD_SIZE * 1.45
        out.append(
            f'  <text x="{cx:.1f}" y="{ty:.1f}" text-anchor="middle"'
            f' font-family="{FONT}" font-size="{CARD_SIZE}" fill="#1a1a1a">{line}</text>'
        )
    return out


def moral_compass_spectrum() -> str:
    body: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}"'
        f' viewBox="0 0 {CANVAS_W} {CANVAS_H}">',
        f'  <rect width="{CANVAS_W}" height="{CANVAS_H}" fill="#ffffff"/>',
    ]
    for index, (_, definition, _) in enumerate(TERMS):
        body.extend(definition_card(index, definition))
    for index, (term, _, tilt) in enumerate(TERMS):
        body.extend(term_box(index, term, tilt))
    arch_w = CANVAS_W - 240
    body.extend(
        [
            f'  <rect x="120" y="{ARCH_Y}" width="{arch_w}" height="{ARCH_H}" rx="4"'
            ' fill="#1f6fb2"/>',
            f'  <text x="{CANVAS_W / 2}" y="{ARCH_Y + ARCH_H / 2 + 7}" text-anchor="middle"'
            f' font-family="{FONT}" font-size="20" fill="#ffffff">Power and Culture</text>',
            "</svg>",
        ]
    )
    return "\n".join(body) + "\n"


def virtue_mean() -> str:
    """Draw Aristotle's doctrine of the mean: one virtue between two vices."""
    width = 900
    height = 350
    band_y = 110.0
    band_h = 96.0
    band_w = 240.0
    labels = (
        ("Vice of deficiency", "Cowardice", "#b4453f"),
        ("Virtue, the mean", "Courage", "#1f6fb2"),
        ("Vice of excess", "Recklessness", "#b4453f"),
    )
    left = (width - 3 * band_w) / 2
    body: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"'
        f' viewBox="0 0 {width} {height}">',
        f'  <rect width="{width}" height="{height}" fill="#ffffff"/>',
    ]
    for index, (zone, example, colour) in enumerate(labels):
        x = left + index * band_w
        body.extend(
            [
                f'  <rect x="{x:.1f}" y="{band_y}" width="{band_w}" height="{band_h}"'
                f' fill="{colour}"/>',
                f'  <text x="{x + band_w / 2:.1f}" y="{band_y + 38:.1f}" text-anchor="middle"'
                f' font-family="{FONT}" font-size="19" fill="#ffffff">{zone}</text>',
                f'  <text x="{x + band_w / 2:.1f}" y="{band_y + 72:.1f}" text-anchor="middle"'
                f' font-family="{FONT}" font-size="24" fill="#ffffff">{example}</text>',
                f'  <text x="{x + band_w / 2:.1f}" y="{band_y - 24:.1f}" text-anchor="middle"'
                f' font-family="{FONT}" font-size="16" fill="#1a1a1a">{"too little" if index == 0 else ("too much" if index == 2 else "the balance")}</text>',
            ]
        )
    body.extend(
        [
            f'  <text x="{width / 2}" y="{band_y + band_h + 56}" text-anchor="middle"'
            f' font-family="{FONT}" font-size="17" fill="#1a1a1a">'
            "Facing danger for the right reason and in the right circumstances sits between failing to face it and ignoring it.</text>",
            "</svg>",
        ]
    )
    return "\n".join(body) + "\n"


def dissonance_routes() -> str:
    """Draw the three routes out of cognitive dissonance."""
    width = 1000
    height = 420
    source_x = 60.0
    source_y = 150.0
    source_w = 250.0
    source_h = 110.0
    target_x = 470.0
    target_w = 470.0
    target_h = 80.0
    targets = (
        "reduce the importance of the conflicting cognitions",
        "add consonant cognitions",
        "change a discrepant cognition",
    )
    step = 110.0
    top = 40.0
    body: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"'
        f' viewBox="0 0 {width} {height}">',
        f'  <rect width="{width}" height="{height}" fill="#ffffff"/>',
        f'  <rect x="{source_x}" y="{source_y}" width="{source_w}" height="{source_h}"'
        ' rx="10" fill="#b4453f"/>',
        f'  <text x="{source_x + source_w / 2}" y="{source_y + 46}" text-anchor="middle"'
        f' font-family="{FONT}" font-size="20" fill="#ffffff">Dissonance</text>',
        f'  <text x="{source_x + source_w / 2}" y="{source_y + 78}" text-anchor="middle"'
        f' font-family="{FONT}" font-size="15" fill="#ffffff">two cognitions that conflict</text>',
    ]
    for index, target in enumerate(targets):
        y = top + index * step
        centre = y + target_h / 2
        body.extend(
            [
                f'  <line x1="{source_x + source_w}" y1="{source_y + source_h / 2}"'
                f' x2="{target_x}" y2="{centre}" stroke="#4a4a4a" stroke-width="2"/>',
                f'  <rect x="{target_x}" y="{y}" width="{target_w}" height="{target_h}"'
                ' rx="10" fill="none" stroke="#1f6fb2" stroke-width="2"/>',
                f'  <text x="{target_x + 20}" y="{centre + 7}" font-family="{FONT}"'
                f' font-size="17" fill="#1a1a1a">{index + 1}. {target}</text>',
            ]
        )
    body.append("</svg>")
    return "\n".join(body) + "\n"


def hierarchy_of_goods() -> str:
    """Draw Aristotle's ranking of goods, highest at the top.

    Commons has no figure for this ranking. Bands rather than a pyramid, because
    a pyramid's apex is too narrow to hold a label, and Maslow's pyramid already
    shows the comparison elsewhere in the note.
    """
    width = 900
    height = 470
    bands = (
        ("Goods of the soul", "intellectual and moral", "#1f6fb2", "#ffffff"),
        ("Goods of the body", "health", "#5b9ecb", "#ffffff"),
        ("External goods", "wealth, friends, political standing", "#a8c8de", "#1a1a1a"),
    )
    centre = width / 2
    band_w = 640.0
    band_h = 84.0
    gap = 10.0
    first_top = 170.0
    body: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"'
        f' viewBox="0 0 {width} {height}">',
        f'  <rect width="{width}" height="{height}" fill="#ffffff"/>',
        f'  <text x="{centre}" y="46" text-anchor="middle" font-family="{FONT}"'
        ' font-size="24" fill="#1a1a1a">Eudaimonia, the final, complete, and self-sufficient end</text>',
        f'  <text x="{centre}" y="76" text-anchor="middle" font-family="{FONT}"'
        ' font-size="16" fill="#4a4a4a">every other good is ranked by how well it serves that end</text>',
        f'  <line x1="{centre}" y1="96" x2="{centre}" y2="{first_top - 14}" stroke="#1a1a1a"'
        ' stroke-width="2"/>',
        f'  <polygon points="{centre},{first_top - 4} {centre - 9},{first_top - 16}'
        f' {centre + 9},{first_top - 16}" fill="#1a1a1a"/>',
    ]
    for index, (label, sublabel, fill_colour, text_colour) in enumerate(bands):
        top = first_top + index * (band_h + gap)
        body.append(
            f'  <rect x="{centre - band_w / 2:.1f}" y="{top:.1f}" width="{band_w:.1f}"'
            f' height="{band_h:.1f}" rx="8" fill="{fill_colour}"/>'
        )
        body.append(
            f'  <text x="{centre}" y="{top + 42:.1f}" text-anchor="middle"'
            f' font-family="{FONT}" font-size="22" fill="{text_colour}">{label}</text>'
        )
        body.append(
            f'  <text x="{centre}" y="{top + 66:.1f}" text-anchor="middle"'
            f' font-family="{FONT}" font-size="15" fill="{text_colour}">{sublabel}</text>'
        )
    body.append("</svg>")
    return "\n".join(body) + "\n"


def main() -> None:
    figures = {
        "moral_compass_spectrum.svg": moral_compass_spectrum(),
        "virtue_mean.svg": virtue_mean(),
        "dissonance_routes.svg": dissonance_routes(),
        "hierarchy_of_goods.svg": hierarchy_of_goods(),
    }
    for name, content in figures.items():
        target = HERE / name
        target.write_text(content, encoding="utf-8")
        print(target)


if __name__ == "__main__":
    main()
