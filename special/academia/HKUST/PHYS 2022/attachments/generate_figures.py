#!/usr/bin/env python
"""Generate the SVG figures kept in this attachments directory.

Run from the repository root (or any cwd; paths are resolved relative to this
file):

    python3 "special/academia/HKUST/PHYS 2022/attachments/generate_figures.py"

The checked-in SVGs are the source of truth: this script embeds their exact
contents, so running it reproduces every figure byte for byte and can be used
to restore a lost or edited file.

Wikimedia Commons was searched for a freely licensed drawing of the
Davisson-Germer grating geometry before `grating_scattering_geometry.svg` was
generated: `File:Davisson-Germer experiment.svg` carries the apparatus rather
than the lattice-plane construction, `File:Ewald construction for electron
diffraction on a two-dimensional lattice, top view.svg` is an Ewald
construction, and `File:Bragg diffraction 2.svg` is described as Bragg
diffraction from a cubic crystal lattice, so none of them fixes phi, theta,
alpha, d, and D in one geometry.

Wikimedia Commons was searched before `box_state_wave_functions.svg` and
`box_state_probability_densities.svg` were generated. `File:Particle in a 1D
box Probability Densities.svg` draws both forms on one panel per level, so a
card cannot show one form without showing the other; `File:1D Wavefunctions
with Energies.svg` and `File:1D Probability Density with Energies.svg` run
their E/E1 axis through the curves they label; `File:Infinite well2.svg`
clips its n = 1 level at the frame and carries no densities. None splits the
two forms into separate pictures of the first three levels.

Wikimedia Commons was searched before `geiger_marsden_apparatus.svg` was
generated. A `Geiger Marsden apparatus scattering` search over the file
namespace returned `File:Geiger-Marsden apparatus CGI mock-up.png` (CC BY 3.0)
and `File:Geiger-Marsden apparatus 2 CGI mock-up.jpg` (CC BY 4.0), both
unlabelled computer-generated mock-ups of the cylinder and the foil disc that
mark no source, slit, foil, screen, microscope or scattering angle, plus
radioactivity book scans, so no Commons file fixes the setup the note describes.

Wikimedia Commons was searched before `franck_hertz_tube.svg` was generated.
`File:Hg-Vakuum tube used for Franck-Hertz experiment.svg` labels its parts
U_H, C, A, S, Hg, I_A, U_1, U_2 (read from the file's own text) and
`File:Experiencia Franck Hertz.svg` writes them in Portuguese (Vapor de
mercúrio, Grade, Placa coletora), so neither spells the parts out in
English. `File:Aparell Franck-Hertz.png` does spell them out, in Catalan
(Filament, Catode, Reixeta, Ànode); it was later downloaded into this
directory and embedded in the note, and this generated figure is kept as
an alternative rendering.
"""

import math
from pathlib import Path

HERE = Path(__file__).resolve().parent

_LEVELS = (1, 2, 3)
_PANEL_X = (0, 260, 520)
_WALL_OFFSET = 72
_BOX_WIDTH = 156
_WALL_TOP = 34
_AXIS_Y = 186
_ZERO_PSI = 100
_AMPLITUDE = 56
_ZERO_DENSITY = 156
_DENSITY_HEIGHT = 56
_SAMPLES = (
    120  # divisible by 6, so every node and peak of n = 1, 2, 3 is sampled exactly
)


def _box_curve(left: int, n: int, base: int, scale: int, squared: bool) -> str:
    """Return polyline points for one level across one panel of the box."""
    points = []
    for k in range(_SAMPLES + 1):
        sine = math.sin(n * math.pi * k / _SAMPLES)
        value = sine * sine if squared else sine
        x = left + _BOX_WIDTH * k / _SAMPLES
        points.append(f"{x:.1f},{base - scale * value:.1f}")
    return " ".join(points)


def rutherford_scattering_geometry_svg() -> str:
    """Return the rutherford_scattering_geometry.svg figure content."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 400" font-family="Georgia, 'Times New Roman', serif" font-size="16">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#000"/>
    </marker>
  </defs>

  <!-- trajectory: hyperbolic path bending away from the scatterer -->
  <path d="M 40 250 L 195 245 L 276 241 L 320 238 L 349 234 L 391 223 L 430 204 L 491 164 L 555 114 L 601 75"
        fill="none" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>
  <path d="M 85 244 L 105 249 L 85 254 Z" fill="#000"/>

  <!-- incoming-direction reference (dashed) and scatterer level (solid) -->
  <line x1="40" y1="250" x2="630" y2="250" stroke="#000" stroke-width="1" stroke-dasharray="7,5"/>
  <line x1="240" y1="330" x2="630" y2="330" stroke="#000" stroke-width="1"/>

  <!-- impact parameter b -->
  <line x1="270" y1="250" x2="270" y2="330" stroke="#000" stroke-width="1" marker-start="url(#arr)" marker-end="url(#arr)"/>
  <text x="256" y="295" text-anchor="end" font-style="italic">b</text>

  <!-- scatterer -->
  <circle cx="430" cy="330" r="7" fill="#000"/>
  <text x="398" y="358"><tspan font-style="italic">Z</tspan><tspan font-size="11" dy="3">2</tspan><tspan dy="-3" font-style="italic">e</tspan></text>
  <text x="395" y="376" font-size="13">scatterer</text>

  <!-- radius r from scatterer to a point on the trajectory -->
  <line x1="430" y1="330" x2="349" y2="234" stroke="#000" stroke-width="1"/>
  <text x="378" y="290" text-anchor="end" font-style="italic">r</text>

  <!-- scattering angle theta between the incoming direction and the outgoing asymptote -->
  <path d="M 435 250 A 34 34 0 0 0 427 228" fill="none" stroke="#000" stroke-width="1"/>
  <text x="417" y="247" text-anchor="middle" font-style="italic">θ</text>

  <!-- incident particle labels -->
  <text x="36" y="232"><tspan font-style="italic">Z</tspan><tspan font-size="11" dy="3">1</tspan><tspan dy="-3">, </tspan><tspan font-style="italic">v</tspan><tspan font-size="11" dy="3">0</tspan></text>
</svg>
"""


def bragg_reflection_geometry_svg() -> str:
    """Return the bragg_reflection_geometry.svg figure content."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 320" font-family="Georgia, 'Times New Roman', serif" font-size="15">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#000"/>
    </marker>
  </defs>

  <!-- two rows of atoms, spacing d -->
  <g fill="#000">
    <circle cx="140" cy="150" r="5"/><circle cx="200" cy="150" r="5"/><circle cx="260" cy="150" r="5"/>
    <circle cx="320" cy="150" r="5"/><circle cx="380" cy="150" r="5"/><circle cx="440" cy="150" r="5"/>
    <circle cx="500" cy="150" r="5"/>
    <circle cx="140" cy="230" r="5"/><circle cx="200" cy="230" r="5"/><circle cx="260" cy="230" r="5"/>
    <circle cx="320" cy="230" r="5"/><circle cx="380" cy="230" r="5"/><circle cx="440" cy="230" r="5"/>
    <circle cx="500" cy="230" r="5"/>
  </g>

  <!-- incident and reflected rays: upper ray strikes a, lower ray strikes b -->
  <line x1="140" y1="80" x2="313.9" y2="147.8" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>
  <line x1="320" y1="150" x2="486" y2="85" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>
  <line x1="140" y1="160" x2="313.9" y2="227.8" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>
  <line x1="320" y1="230" x2="486" y2="165" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>

  <!-- dashed plane through a, and perpendiculars from a onto the lower ray -->
  <line x1="250" y1="150" x2="560" y2="150" stroke="#000" stroke-width="1" stroke-dasharray="7,5"/>
  <line x1="320" y1="150" x2="293" y2="220" stroke="#000" stroke-width="1" stroke-dasharray="5,4"/>
  <line x1="320" y1="150" x2="347" y2="220" stroke="#000" stroke-width="1" stroke-dasharray="5,4"/>

  <!-- plane spacing d -->
  <line x1="200" y1="150" x2="200" y2="230" stroke="#000" stroke-width="1" marker-start="url(#arr)" marker-end="url(#arr)"/>
  <text x="186" y="195" text-anchor="end" font-style="italic">d</text>

  <!-- glancing angles at a -->
  <path d="M 298 150 A 22 22 0 0 1 299.5 142" fill="none" stroke="#000" stroke-width="1"/>
  <path d="M 342 150 A 22 22 0 0 0 340.5 142" fill="none" stroke="#000" stroke-width="1"/>
  <text x="287" y="148" text-anchor="end" font-style="italic" font-size="13" stroke="#FFF" stroke-width="3.5" paint-order="stroke">θ</text>
  <text x="356" y="149" font-style="italic" font-size="13" stroke="#FFF" stroke-width="3.5" paint-order="stroke">θ</text>

  <!-- atom labels -->
  <text x="324" y="138" font-style="italic" stroke="#FFF" stroke-width="3.5" paint-order="stroke">a</text>
  <text x="286" y="228" text-anchor="end" font-style="italic" stroke="#FFF" stroke-width="3.5" paint-order="stroke">b</text>

  <!-- path-difference segments on the lower ray -->
  <text x="291" y="214" text-anchor="end" stroke="#FFF" stroke-width="3.5" paint-order="stroke"><tspan font-style="italic">d</tspan> sin <tspan font-style="italic">θ</tspan></text>
  <text x="349" y="214" stroke="#FFF" stroke-width="3.5" paint-order="stroke"><tspan font-style="italic">d</tspan> sin <tspan font-style="italic">θ</tspan></text>
  <path d="M 293 252 Q 320 266 347 252" fill="none" stroke="#000" stroke-width="1"/>
  <text x="320" y="292" text-anchor="middle"><tspan font-size="16" font-style="italic">2</tspan><tspan font-style="italic">d</tspan> sin <tspan font-style="italic">θ</tspan></text>

  <!-- beam labels -->
  <text x="133" y="66" text-anchor="end" font-size="13">incident beam</text>
  <text x="505" y="58" font-size="13">reflected beam</text>
</svg>
"""


def bragg_transmission_geometry_svg() -> str:
    """Return the bragg_transmission_geometry.svg figure content."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" font-family="Georgia, 'Times New Roman', serif" font-size="15">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#000"/>
    </marker>
  </defs>

  <!-- (a) side view -->
  <text x="40" y="44" font-size="14">(a) side view</text>

  <!-- beam axis (dashed) -->
  <line x1="40" y1="170" x2="345" y2="170" stroke="#000" stroke-width="1" stroke-dasharray="7,5"/>

  <!-- incident beam -->
  <line x1="42" y1="170" x2="168" y2="170" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>
  <text x="42" y="156" font-size="13">incident beam</text>

  <!-- sample slab -->
  <rect x="170" y="135" width="8" height="70" fill="#000"/>
  <text x="174" y="126" text-anchor="middle" font-size="13" stroke="#FFF" stroke-width="3.5" paint-order="stroke">sample</text>

  <!-- direct beam to the plate -->
  <line x1="178" y1="170" x2="344" y2="170" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>
  <text x="262" y="187" text-anchor="middle" font-size="13" stroke="#FFF" stroke-width="3.5" paint-order="stroke">direct beam</text>

  <!-- diffracted cone, edge-on: two rays at 2θ around the axis -->
  <line x1="178" y1="170" x2="346" y2="127" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>
  <line x1="178" y1="170" x2="346" y2="213" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>
  <text x="206" y="110" font-size="13" stroke="#FFF" stroke-width="3.5" paint-order="stroke">diffracted rays</text>

  <!-- 2θ mark between axis and upper ray -->
  <path d="M 212 170 A 34 34 0 0 0 220.7 161.4" fill="none" stroke="#000" stroke-width="1"/>
  <text x="222" y="159" font-size="13" font-style="italic" stroke="#FFF" stroke-width="3.5" paint-order="stroke">2θ</text>

  <!-- detector plate, edge-on, with the ring intersections marked -->
  <line x1="350" y1="100" x2="350" y2="240" stroke="#000" stroke-width="3"/>
  <circle cx="350" cy="127" r="3.5" fill="#000"/>
  <circle cx="350" cy="213" r="3.5" fill="#000"/>
  <text x="358" y="118" font-size="13" stroke="#FFF" stroke-width="3.5" paint-order="stroke">ring, edge-on</text>
  <text x="350" y="258" text-anchor="middle" font-size="13" stroke="#FFF" stroke-width="3.5" paint-order="stroke">detector plate</text>

  <!-- (b) detector face -->
  <text x="490" y="44" font-size="14">(b) detector face</text>

  <!-- plate outline -->
  <rect x="490" y="90" width="160" height="160" fill="none" stroke="#000" stroke-width="3"/>

  <!-- rings and the direct-beam spot -->
  <circle cx="570" cy="170" r="38" fill="none" stroke="#000" stroke-width="1.5"/>
  <circle cx="570" cy="170" r="62" fill="none" stroke="#000" stroke-width="1.5"/>
  <circle cx="570" cy="170" r="4" fill="#000"/>
  <text x="570" y="200" text-anchor="middle" font-size="13" stroke="#FFF" stroke-width="3.5" paint-order="stroke">direct beam</text>

  <!-- ring labels with leaders -->
  <line x1="597" y1="143" x2="618" y2="122" stroke="#000" stroke-width="1"/>
  <text x="622" y="120" font-size="13" stroke="#FFF" stroke-width="3.5" paint-order="stroke">ring (200)</text>
  <line x1="614" y1="126" x2="638" y2="104" stroke="#000" stroke-width="1"/>
  <text x="642" y="102" font-size="13" stroke="#FFF" stroke-width="3.5" paint-order="stroke">ring (400)</text>
</svg>
"""


def grating_scattering_geometry_svg() -> str:
    """Return the grating_scattering_geometry.svg figure content."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 500" font-family="Georgia, 'Times New Roman', serif" font-size="15">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#000"/>
    </marker>
  </defs>

  <!-- lattice planes, slope 1/2 through real atoms: d = D sin alpha exactly (alpha = arctan 1/2) -->
  <g stroke="#000" stroke-width="1" stroke-dasharray="7,5">
    <line x1="170" y1="30" x2="700" y2="295"/>
    <line x1="110" y1="60" x2="700" y2="355"/>
    <line x1="130" y1="130" x2="700" y2="415"/>
    <line x1="40" y1="145" x2="610" y2="430"/>
    <line x1="40" y1="205" x2="490" y2="430"/>
  </g>

  <!-- atoms: columns D = 120 apart, rows 60 apart -->
  <g fill="#000">
    <circle cx="70" cy="160" r="6"/><circle cx="190" cy="160" r="6"/><circle cx="310" cy="160" r="6"/><circle cx="430" cy="160" r="6"/><circle cx="550" cy="160" r="6"/><circle cx="670" cy="160" r="6"/>
    <circle cx="70" cy="220" r="6"/><circle cx="190" cy="220" r="6"/><circle cx="310" cy="220" r="6"/><circle cx="430" cy="220" r="6"/><circle cx="550" cy="220" r="6"/><circle cx="670" cy="220" r="6"/>
    <circle cx="70" cy="280" r="6"/><circle cx="190" cy="280" r="6"/><circle cx="310" cy="280" r="6"/><circle cx="430" cy="280" r="6"/><circle cx="550" cy="280" r="6"/><circle cx="670" cy="280" r="6"/>
    <circle cx="70" cy="340" r="6"/><circle cx="190" cy="340" r="6"/><circle cx="310" cy="340" r="6"/><circle cx="430" cy="340" r="6"/><circle cx="550" cy="340" r="6"/><circle cx="670" cy="340" r="6"/>
    <circle cx="70" cy="400" r="6"/><circle cx="190" cy="400" r="6"/><circle cx="310" cy="400" r="6"/><circle cx="430" cy="400" r="6"/><circle cx="550" cy="400" r="6"/><circle cx="670" cy="400" r="6"/>
  </g>

  <!-- row spacing D between two atoms of one row, and the perpendicular d from the second atom down to the first atom's plane -->
  <g stroke="#000" stroke-width="1.5">
    <line x1="430" y1="340" x2="550" y2="340"/>
    <line x1="550" y1="340" x2="526" y2="388"/>
  </g>
  <path d="M 534 392 L 526 388 L 530 380 L 538 384 Z" fill="none" stroke="#000" stroke-width="1"/>
  <line x1="430" y1="420" x2="430" y2="460" stroke="#000" stroke-width="1"/>
  <line x1="550" y1="420" x2="550" y2="460" stroke="#000" stroke-width="1"/>
  <line x1="430" y1="440" x2="550" y2="440" stroke="#000" stroke-width="1" marker-start="url(#arr)" marker-end="url(#arr)"/>
  <text x="490" y="468" text-anchor="middle" font-style="italic">D</text>
  <text x="550" y="370" text-anchor="middle" font-style="italic" stroke="#FFF" stroke-width="3.5" paint-order="stroke">d</text>
  <path d="M 466 340 A 36 36 0 0 1 462.2 356.1" fill="none" stroke="#000" stroke-width="1"/>
  <text x="481" y="356" text-anchor="middle" font-style="italic" stroke="#FFF" stroke-width="3.5" paint-order="stroke">α</text>

  <!-- plane normal from the scattering atom, bisecting the beams -->
  <line x1="310" y1="160" x2="368" y2="44" stroke="#000" stroke-width="1"/>

  <!-- incident beam striking the atom at (310,160), scattered beam along the exact reflection direction -->
  <line x1="310" y1="56" x2="310" y2="154" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>
  <line x1="310" y1="160" x2="462" y2="46" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>

  <!-- angles at the scattering atom: phi = 53.13 deg between the beams, alpha on each side of the normal, theta = 63.43 deg from beam to plane -->
  <path d="M 310 60 A 100 100 0 0 1 390 100" fill="none" stroke="#000" stroke-width="1"/>
  <path d="M 310 98 A 62 62 0 0 1 337.7 104.6" fill="none" stroke="#000" stroke-width="1"/>
  <path d="M 337.7 104.6 A 62 62 0 0 1 359.6 122.8" fill="none" stroke="#000" stroke-width="1"/>
  <path d="M 310 72 A 88 88 0 0 0 231.3 120.7" fill="none" stroke="#000" stroke-width="1"/>

  <!-- forward continuation of the incident beam (dashed), and 2 theta = 126.87 deg measured from that continuation to the scattered beam: the two arcs share the scattered beam and the straight incident line, so phi + 2 theta = 180 deg reads off the drawing -->
  <line x1="310" y1="166" x2="310" y2="300" stroke="#000" stroke-width="1" stroke-dasharray="7,5"/>
  <path d="M 310 260 A 100 100 0 0 0 390 100" fill="none" stroke="#000" stroke-width="1"/>

  <!-- labels -->
  <text x="330" y="52" text-anchor="middle" font-style="italic" stroke="#FFF" stroke-width="3.5" paint-order="stroke">φ</text>
  <text x="393" y="243" text-anchor="middle" font-style="italic" stroke="#FFF" stroke-width="3.5" paint-order="stroke">2θ</text>
  <text x="328" y="86" text-anchor="middle" font-style="italic" stroke="#FFF" stroke-width="3.5" paint-order="stroke">α</text>
  <text x="361" y="102" text-anchor="middle" font-style="italic" stroke="#FFF" stroke-width="3.5" paint-order="stroke">α</text>
  <text x="272" y="102" text-anchor="middle" font-style="italic" stroke="#FFF" stroke-width="3.5" paint-order="stroke">θ</text>
  <text x="300" y="64" text-anchor="end" font-size="14" stroke="#FFF" stroke-width="3.5" paint-order="stroke">Incident beam</text>
  <text x="472" y="50" font-size="14">Scattered beam</text>
</svg>
"""


def box_state_wave_functions_svg() -> str:
    """Return the box_state_wave_functions.svg figure content."""
    panels = []
    for i, n in enumerate(_LEVELS):
        left = _PANEL_X[i] + _WALL_OFFSET
        nodes = "".join(
            f'\n  <circle cx="{left + _BOX_WIDTH * k / n}" cy="{_ZERO_PSI}" r="3.5" fill="#000"/>'
            for k in range(1, n)
        )
        panels.append(
            f"""
  <!-- psi {n}: zero line at y = {_ZERO_PSI}, {n - 1} interior node(s) marked -->
  <line x1="{left}" y1="{_WALL_TOP}" x2="{left}" y2="{_AXIS_Y}" stroke="#000" stroke-width="2"/>
  <line x1="{left + _BOX_WIDTH}" y1="{_WALL_TOP}" x2="{left + _BOX_WIDTH}" y2="{_AXIS_Y}" stroke="#000" stroke-width="2"/>
  <line x1="{left}" y1="{_ZERO_PSI}" x2="{left + _BOX_WIDTH}" y2="{_ZERO_PSI}" stroke="#000" stroke-width="1" stroke-dasharray="7,5"/>{nodes}
  <polyline points="{_box_curve(left, n, _ZERO_PSI, _AMPLITUDE, squared=False)}" fill="none" stroke="#000" stroke-width="2"/>
  <text x="{left - 10}" y="{_ZERO_PSI + 5}" text-anchor="end"><tspan font-style="italic">ψ</tspan><tspan font-size="11" dy="3">{n}</tspan></text>
  <line x1="{left}" y1="{_AXIS_Y}" x2="{left + _BOX_WIDTH}" y2="{_AXIS_Y}" stroke="#000" stroke-width="1" marker-end="url(#arr)"/>
  <text x="{left}" y="{_AXIS_Y + 20}" text-anchor="middle">0</text>
  <text x="{left + _BOX_WIDTH}" y="{_AXIS_Y + 20}" text-anchor="middle" font-style="italic">L</text>
  <text x="{left + _BOX_WIDTH // 2}" y="{_AXIS_Y + 20}" text-anchor="middle" font-style="italic">x</text>"""
        )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 24 780 196" font-family="Georgia, 'Times New Roman', serif" font-size="15">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#000"/>
    </marker>
  </defs>{"".join(panels)}
</svg>
"""


def box_state_probability_densities_svg() -> str:
    """Return the box_state_probability_densities.svg figure content."""
    panels = []
    for i, n in enumerate(_LEVELS):
        left = _PANEL_X[i] + _WALL_OFFSET
        panels.append(
            f"""
  <!-- psi {n} squared: baseline at y = {_ZERO_DENSITY}, {n} humps -->
  <line x1="{left}" y1="{_WALL_TOP}" x2="{left}" y2="{_AXIS_Y}" stroke="#000" stroke-width="2"/>
  <line x1="{left + _BOX_WIDTH}" y1="{_WALL_TOP}" x2="{left + _BOX_WIDTH}" y2="{_AXIS_Y}" stroke="#000" stroke-width="2"/>
  <line x1="{left}" y1="{_ZERO_DENSITY}" x2="{left + _BOX_WIDTH}" y2="{_ZERO_DENSITY}" stroke="#000" stroke-width="1" stroke-dasharray="7,5"/>
  <polyline points="{_box_curve(left, n, _ZERO_DENSITY, _DENSITY_HEIGHT, squared=True)}" fill="none" stroke="#000" stroke-width="2"/>
  <text x="{left - 10}" y="{_ZERO_DENSITY + 5}" text-anchor="end"><tspan>|</tspan><tspan font-style="italic">ψ</tspan><tspan font-size="11" dy="3">{n}</tspan><tspan dy="-3">|²</tspan></text>
  <line x1="{left}" y1="{_AXIS_Y}" x2="{left + _BOX_WIDTH}" y2="{_AXIS_Y}" stroke="#000" stroke-width="1" marker-end="url(#arr)"/>
  <text x="{left}" y="{_AXIS_Y + 20}" text-anchor="middle">0</text>
  <text x="{left + _BOX_WIDTH}" y="{_AXIS_Y + 20}" text-anchor="middle" font-style="italic">L</text>
  <text x="{left + _BOX_WIDTH // 2}" y="{_AXIS_Y + 20}" text-anchor="middle" font-style="italic">x</text>"""
        )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 24 780 196" font-family="Georgia, 'Times New Roman', serif" font-size="15">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#000"/>
    </marker>
  </defs>{"".join(panels)}
</svg>
"""


def franck_hertz_tube_svg() -> str:
    """Return the franck_hertz_tube.svg figure content."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 90 840 440" font-family="Georgia, 'Times New Roman', serif" font-size="15">
  <defs>
    <marker id="arrb" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#00ADEF"/>
    </marker>
  </defs>

  <!-- filament power supply: positive plate on top, negative below -->
  <text x="20" y="110">Filament</text>
  <text x="20" y="130">power</text>
  <text x="20" y="150">supply</text>
  <text x="66" y="180" text-anchor="middle">+</text>
  <line x1="36" y1="190" x2="96" y2="190" stroke="#00ADEF" stroke-width="2"/>
  <line x1="48" y1="210" x2="84" y2="210" stroke="#00ADEF" stroke-width="3"/>
  <text x="66" y="234" text-anchor="middle">−</text>

  <!-- tube: filament, mercury vapor, grid, collector -->
  <rect x="220" y="150" width="440" height="100" rx="50" ry="50" fill="#E6E6E6" stroke="#000" stroke-width="1.5"/>

  <!-- filament leads and the return that drops to the circuit -->
  <line x1="96" y1="190" x2="271" y2="190" stroke="#000" stroke-width="1.5"/>
  <line x1="84" y1="210" x2="271" y2="210" stroke="#000" stroke-width="1.5"/>
  <circle cx="170" cy="210" r="3.5" fill="#000"/>
  <line x1="170" y1="210" x2="170" y2="430" stroke="#000" stroke-width="1.5"/>
  <circle cx="275" cy="200" r="11" fill="#FFF" stroke="#000" stroke-width="1.5"/>
  <circle cx="297" cy="200" r="11" fill="#FFF" stroke="#000" stroke-width="1.5"/>
  <text x="286" y="240" text-anchor="middle">Filament</text>

  <!-- electrons crossing the mercury vapor -->
  <line x1="330" y1="182" x2="392" y2="182" stroke="#00ADEF" stroke-width="2.5" marker-end="url(#arrb)"/>
  <line x1="330" y1="200" x2="392" y2="200" stroke="#00ADEF" stroke-width="2.5" marker-end="url(#arrb)"/>
  <line x1="330" y1="218" x2="392" y2="218" stroke="#00ADEF" stroke-width="2.5" marker-end="url(#arrb)"/>
  <text x="404" y="207"><tspan font-style="italic">e</tspan><tspan font-size="11" dy="-6">−</tspan></text>
  <text x="430" y="170" text-anchor="middle">Hg vapor</text>

  <!-- grid, its lead down to the accelerating supply -->
  <line x1="530" y1="160" x2="530" y2="240" stroke="#000" stroke-width="1.5" stroke-dasharray="7,5"/>
  <text x="520" y="236" text-anchor="end">Grid</text>
  <line x1="530" y1="240" x2="530" y2="430" stroke="#000" stroke-width="1.5"/>
  <circle cx="530" cy="350" r="3.5" fill="#000"/>
  <circle cx="530" cy="430" r="3.5" fill="#000"/>

  <!-- collector and its wire out to the electrometer -->
  <line x1="575" y1="175" x2="575" y2="225" stroke="#000" stroke-width="6"/>
  <text x="614" y="116">Collector</text>
  <line x1="622" y1="126" x2="580" y2="172" stroke="#000" stroke-width="1"/>
  <line x1="578" y1="200" x2="700" y2="200" stroke="#000" stroke-width="1.5"/>
  <line x1="700" y1="200" x2="700" y2="300" stroke="#000" stroke-width="1.5"/>
  <circle cx="700" cy="318" r="18" fill="#FFF" stroke="#000" stroke-width="1.5"/>
  <text x="700" y="324" text-anchor="middle" font-size="17">A</text>
  <text x="726" y="324">Electrometer</text>

  <!-- 1.5 V retarding bias, negative side toward the collector -->
  <line x1="700" y1="336" x2="700" y2="352" stroke="#000" stroke-width="1.5"/>
  <line x1="688" y1="352" x2="712" y2="352" stroke="#00ADEF" stroke-width="3"/>
  <line x1="680" y1="364" x2="720" y2="364" stroke="#00ADEF" stroke-width="1.5"/>
  <line x1="700" y1="364" x2="700" y2="430" stroke="#000" stroke-width="1.5"/>
  <text x="730" y="356">−</text>
  <text x="730" y="376">+</text>
  <text x="752" y="368">1.5 V</text>

  <!-- voltmeter across filament and grid -->
  <line x1="170" y1="350" x2="332" y2="350" stroke="#000" stroke-width="1.5"/>
  <line x1="368" y1="350" x2="530" y2="350" stroke="#000" stroke-width="1.5"/>
  <circle cx="170" cy="350" r="3.5" fill="#000"/>
  <circle cx="350" cy="350" r="18" fill="#FFF" stroke="#000" stroke-width="1.5"/>
  <text x="350" y="356" text-anchor="middle" font-size="17">V</text>
  <text x="350" y="396" text-anchor="middle">Voltmeter</text>

  <!-- 0-45 V accelerating supply between filament and grid -->
  <line x1="170" y1="430" x2="420" y2="430" stroke="#000" stroke-width="1.5"/>
  <line x1="432" y1="430" x2="700" y2="430" stroke="#000" stroke-width="1.5"/>
  <line x1="420" y1="418" x2="420" y2="442" stroke="#00ADEF" stroke-width="3"/>
  <line x1="432" y1="410" x2="432" y2="450" stroke="#00ADEF" stroke-width="1.5"/>
  <text x="406" y="436" text-anchor="end">−</text>
  <text x="446" y="436">+</text>
  <text x="426" y="478" text-anchor="middle">0 – 45 V</text>
  <text x="426" y="502" text-anchor="middle">Accelerating power supply</text>
</svg>
"""


def geiger_marsden_apparatus_svg() -> str:
    """Return the geiger_marsden_apparatus.svg figure content."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 460" font-family="Georgia, 'Times New Roman', serif" font-size="15">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="#000"/>
    </marker>
  </defs>

  <!-- evacuated chamber: the source, the foil and the detector all sit inside it -->
  <rect x="30" y="40" width="640" height="380" rx="30" ry="30" fill="none" stroke="#000" stroke-width="1.5" stroke-dasharray="9,6"/>
  <text x="48" y="404" font-size="14">evacuated chamber</text>

  <!-- alpha source: body with a conical nose pointing at the slit -->
  <rect x="70" y="126" width="80" height="48" rx="8" ry="8" fill="#E6E6E6" stroke="#000" stroke-width="1.5"/>
  <path d="M 150 136 L 190 150 L 150 164 Z" fill="#E6E6E6" stroke="#000" stroke-width="1.5"/>
  <text x="70" y="112" font-size="14">α-particle source</text>

  <!-- lead plate in two pieces, the gap between them is the slit the beam passes -->
  <g fill="#666" stroke="#000" stroke-width="1">
    <rect x="255" y="55" width="30" height="85"/>
    <rect x="255" y="160" width="30" height="100"/>
  </g>
  <text x="295" y="90" font-size="14">lead plate</text>

  <!-- incident beam: from the source, through the slit, onto the foil -->
  <line x1="192" y1="150" x2="464" y2="150" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>

  <!-- gold foil -->
  <line x1="470" y1="85" x2="470" y2="340" stroke="#000" stroke-width="2"/>
  <text x="480" y="100" font-size="14">gold foil</text>

  <!-- direction the beam would take with no scattering -->
  <line x1="476" y1="150" x2="640" y2="150" stroke="#000" stroke-width="1" stroke-dasharray="7,5"/>

  <!-- scattered beam, back on the side the beam came from -->
  <line x1="470" y1="150" x2="441.6" y2="272.8" stroke="#000" stroke-width="2" marker-end="url(#arr)"/>

  <!-- scattering angle theta between the unscattered direction and the scattered beam -->
  <path d="M 530 150 A 60 60 0 0 1 456.5 208.5" fill="none" stroke="#000" stroke-width="1"/>
  <text x="517" y="214" text-anchor="middle" font-style="italic">θ</text>

  <!-- the arm swings the screen and microscope around the foil -->
  <path d="M 453.3 309.6 A 160 160 0 0 0 561.8 281" fill="none" stroke="#000" stroke-width="1" stroke-dasharray="7,5" marker-end="url(#arr)"/>
  <text x="533" y="336" text-anchor="middle" font-size="14">swinging arm</text>

  <!-- scintillating screen across the scattered beam -->
  <line x1="416.6" y1="272.6" x2="463.4" y2="283.4" stroke="#000" stroke-width="3"/>
  <text x="410" y="285" text-anchor="end" font-size="14">screen</text>

  <!-- microscope behind the screen, pointed at it -->
  <polygon points="446.8,290.3 432.4,379.4 403.2,372.6 429.2,286.3" fill="#E6E6E6" stroke="#000" stroke-width="1.5"/>
  <text x="395" y="345" text-anchor="end" font-size="14">microscope</text>
</svg>
"""


def main() -> None:
    """Write every figure this script knows into HERE."""
    figures = {
        "rutherford_scattering_geometry.svg": rutherford_scattering_geometry_svg(),
        "geiger_marsden_apparatus.svg": geiger_marsden_apparatus_svg(),
        "bragg_reflection_geometry.svg": bragg_reflection_geometry_svg(),
        "bragg_transmission_geometry.svg": bragg_transmission_geometry_svg(),
        "grating_scattering_geometry.svg": grating_scattering_geometry_svg(),
        "box_state_wave_functions.svg": box_state_wave_functions_svg(),
        "box_state_probability_densities.svg": box_state_probability_densities_svg(),
        "franck_hertz_tube.svg": franck_hertz_tube_svg(),
    }
    for name, content in figures.items():
        path = HERE / name
        path.write_text(content, encoding="utf-8")
        print(f"wrote {path.name} ({len(content)} bytes)")


if __name__ == "__main__":
    main()
