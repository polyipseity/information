# /// script
# requires-python = ">=3.13.0"
# ///
"""Generate the definitional drawing for unlisted trading privileges.

The drawing shows how a single-listed stock reaches trading venues other than
its listing exchange: one box for the stock, a bus of three drops, and the
listing exchange separated from the two unlisted trading privilege venues.

Wikimedia Commons was searched before generating (see the module docstring in
the note's commit history): "unlisted trading privileges" returned no
filetype:bitmap hits, and the hits for "national market system securities
information processor" and "Regulation NMS" were unrelated (a photograph
titled File:HARVEST-tape.jpg, and National Monument System entries in
Washington, Michigan, Minnesota, and Norfolk). No freely licensed figure shows
this structure, so the drawing is generated.

Run from the attachments directory:

    uv run python generate_figures.py

Deterministic: fixed coordinates, no randomness, no timestamps.
"""

from pathlib import Path

BLUE_FILL = "#d6e4f7"
BLUE_EDGE = "#1f4e9c"
RED_FILL = "#f6d6d6"
RED_EDGE = "#a11f1f"
TEXT = "#1a1a1a"
FONT = "DejaVu Sans, Helvetica, Arial, sans-serif"

BOX_W = 260
BOX_H = 90
DROPS = (
    # (x, label, subtitle, edge, fill)
    (40, "NYSE", "can trade AAPL", BLUE_EDGE, BLUE_FILL),
    (390, "NASDAQ", "can trade AAPL", RED_EDGE, RED_FILL),
    (740, "IEX", "can trade AAPL", RED_EDGE, RED_FILL),
)
BUS_Y = 150


def box(x: float, y: float, w: float, h: float, edge: str, fill: str) -> str:
    return (
        f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
        f'fill="{fill}" stroke="{edge}" stroke-width="3"/>\n'
    )


def label(x: float, y: float, text: str, size: int, weight: str = "normal") -> str:
    return (
        f'  <text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" fill="{TEXT}" text-anchor="middle">{text}</text>\n'
    )


def arrow(x: float, y1: float, y2: float) -> str:
    head = 9
    return (
        f'  <line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - head}" '
        f'stroke="#555555" stroke-width="3" marker-end="url(#head)"/>\n'
    )


def build() -> str:
    out = [
        '<?xml version="1.0" encoding="UTF-8"?>\n',
        '<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="420" '
        'viewBox="0 0 1120 420" role="img" '
        'aria-label="A stock single-listed on the New York Stock Exchange trading '
        "on the New York Stock Exchange, on Nasdaq through unlisted trading "
        'privileges, and on the IEX through unlisted trading privileges">\n',
        "  <defs>\n",
        '    <marker id="head" markerWidth="10" markerHeight="8" refX="9" refY="4" '
        'orient="auto">\n',
        '      <path d="M0,0 L10,4 L0,8 z" fill="#555555"/>\n',
        "    </marker>\n",
        "  </defs>\n",
    ]

    # The listed stock, alone at the top.
    out.append(box(40, 20, 300, 80, BLUE_EDGE, BLUE_FILL))
    out.append(label(190, 55, "AAPL", 24, "bold"))
    out.append(label(190, 82, "single-listed on NYSE", 17))

    # A bus splitting the listing into the venues that may trade it.
    first = DROPS[0][0] + BOX_W / 2
    last = DROPS[-1][0] + BOX_W / 2
    out.append(
        f'  <line x1="190" y1="100" x2="190" y2="{BUS_Y}" '
        'stroke="#555555" stroke-width="3"/>\n'
    )
    out.append(
        f'  <line x1="{first}" y1="{BUS_Y}" x2="{last}" y2="{BUS_Y}" '
        'stroke="#555555" stroke-width="3"/>\n'
    )

    names = ("listed exchange", "UTP", "UTP")
    for (x, name, sub, edge, fill), note in zip(DROPS, names):
        centre = x + BOX_W / 2
        out.append(arrow(centre, BUS_Y, 250))
        out.append(
            f'  <text x="{centre + 14}" y="196" font-family="{FONT}" '
            f'font-size="18" fill="{TEXT}">{note}</text>\n'
        )
        out.append(box(x, 250, BOX_W, BOX_H, edge, fill))
        out.append(label(centre, 288, name, 22, "bold"))
        out.append(label(centre, 316, sub, 16))

    # The bracket that names the two groups the split produces.
    out.append(
        '  <path d="M1090,20 L1090,340" stroke="#6a8f3a" stroke-width="3" fill="none" '
        'transform="translate(0,0)"/>\n'
    )
    out.append(
        '  <path d="M1074,20 q16,10 0,20 M1074,160 q16,10 0,20 M1074,320 q16,10 0,20" '
        'stroke="#6a8f3a" stroke-width="3" fill="none"/>\n'
    )
    out.append(
        f'  <text x="1102" y="180" font-family="{FONT}" font-size="18" fill="{TEXT}" '
        'text-anchor="middle" transform="rotate(90 1102 180)">'
        "listing exchange and trading exchanges</text>\n"
    )

    out.append("</svg>\n")
    return "".join(out)


def main() -> None:
    target = Path(__file__).with_name("utp_listing_and_trading.svg")
    target.write_text(build(), encoding="utf-8")
    print(f"wrote {target}")


if __name__ == "__main__":
    main()
