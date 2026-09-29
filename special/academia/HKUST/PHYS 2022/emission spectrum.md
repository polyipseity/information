---
aliases:
  - emission line
  - emission spectrum
  - line spectrum
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/emission_spectrum
  - language/in/English
---

# emission spectrum

An _emission spectrum_ is the set of wavelengths a substance gives off as its own light once it is excited, as distinct from light reflected from it. Burning a substance in a flame excites its atoms, and the light that comes back out is their own. A lithium salt burns crimson, a barium salt yellow-green, and neither colour changes with the temperature of the flame or with what else is dissolved in it. The colour belongs to the element. An excited gas gives a line spectrum. A hot solid or a hollow cavity gives a smooth continuous spectrum instead, with a single peak whose position its temperature sets.

The lines sit at fixed wavelengths, so measuring them gives the composition of whatever produced them.

---

Flashcards for this section are as follows:

- overview: what an emission spectrum is ::@:: The set of wavelengths a substance emits as its own light when it is excited, not light reflected from it.
- why the colour of a burning substance is a property of the element ::@:: Burning excites its atoms, and the light they give off is fixed by the element: a lithium salt burns crimson, a barium salt yellow-green, and neither colour changes with the temperature of the flame or with what else is dissolved in it.
- what a line spectrum reveals about a substance of unknown composition ::@:: What it is made of, because the lines sit at the wavelengths of the elements present.
- how the spectrum of an excited gas differs from that of a hot solid ::@:: An excited gas gives separated lines, while a hot solid or cavity gives a smooth continuous spectrum with a single peak whose position its temperature sets.

## flame colours and the spectrometer

From the middle of the 18th century, chemists noticed that materials burnt in a flame gave it a colour of their own. A colour that could not be separated into its parts said only that a substance was there, not which one. Gustav Kirchhoff (1824-1887) and Robert Bunsen (1811-1899) made the colour quantitative by analysing it in a spectrometer instead of looking at it.

The flame test is their method, still a laboratory routine. A wire is dipped into a salt and held in the flame. The colour is read against five standard examples: lithium crimson, potassium a pale lilac, iron orange, barium yellow-green, strontium crimson. Lithium and strontium both burn crimson, too alike for the naked eye to tell apart; the spectrometer separates them.

A spectrometer turns a colour into a list. Light from the flame is collimated into a narrow beam and sent through a grating. The grating spreads it by wavelength onto a screen or a detector, where each wavelength can be measured. What the instrument measures is a position, and turning a position into a wavelength takes the grating equation.

---

Flashcards for this section are as follows:

- overview: what a material does to a flame colour ::@:: From the middle of the 18th century, chemists found that each material burnt in a flame gave it a colour of its own.
- Kirchhoff and Bunsen, and what they did with those colours ::@:: Gustav Kirchhoff (1824-1887) and Robert Bunsen (1811-1899) made the colours quantitative by analysing them in a spectrometer instead of looking at them.
- what a flame colour showed before it could be separated into its parts ::@:: Only that a substance was there, not which one.
- the five elements the standard flame test names ::@:: Lithium, potassium, iron, barium, and strontium.
- the flame colour of potassium ::@:: A pale lilac.
- the flame colour of barium ::@:: Yellow-green.
- the flame colours of lithium and strontium ::@:: Both crimson, which is why the naked eye alone cannot tell the two apart.
- the flame colour of iron ::@:: Orange.
- what the spectrometer does to the light from a flame ::@:: It collimates the light into a beam, spreads it by wavelength, and turns a colour into a set of measured positions, each of which converts to a wavelength.

## how a grating separates the lines

A diffraction grating is a flat surface ruled with thousands of parallel lines per centimetre. The spacing between neighbouring rulings, $d$, characterises it. Collimated light from a flame falls on the grating, and each wavelength leaves at its own angle $\theta$, set by $d\sin\theta = n\lambda$ with $n$ an integer.

For a fixed order $n$ and a fixed spacing $d$, $\sin\theta$ is proportional to $\lambda$. Long wavelengths leave at large angles and short ones at small angles. The beam fans out into a spectrum laid out in order of wavelength. An element is identified by the set of wavelengths it emits.

Four emission spectra recorded on the same instrument differ in the number of lines they show. Hydrogen shows four across the visible band, the fewest of the four. Helium and oxygen show more. Iron shows so many lines that they crowd into a dense band reading as a single grey stripe from a distance. Line count follows the number of electronic transitions the atom can make, and iron has far more of them than hydrogen. Every one of those transitions can emit; iron's spectrum comes close to continuity without ever reaching it.

---

Flashcards for this section are as follows:

- overview: how a grating of ruling spacing $d$ separates light of wavelength $\lambda$ into angles $\theta$ ::@:: Collimated light falls on a grating ruled with thousands of lines per centimetre, and each wavelength leaves at its own angle through $d\sin\theta = n\lambda$, $n$ an integer.
- the grating equation: what $d$, $n$, and $\theta$ are ::@:: $d\sin\theta = n\lambda$, where $d$ is the distance between neighbouring rulings and $n$ is an integer.
- the number of rulings a grating carries per centimetre ::@:: Thousands, and their spacing $d$ sets the angle at which each wavelength leaves. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- how the diffraction angle changes as the wavelength grows ::@:: Since $d\sin\theta = n\lambda$ at fixed $d$ and $n$, a longer wavelength leaves at a larger angle, so the colours spread out in order of wavelength. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the emission spectrum with the fewest lines of the four compared ::@:: Hydrogen, with four lines across the visible.
- the emission spectrum with the most lines of the four compared ::@:: Iron, whose lines are dense enough to read as a band.
- why iron has so many lines where hydrogen has four ::@:: Iron has far more electronic transitions available to it, and each can emit, so its spectrum approaches continuity without reaching it.
- what a line spectrum identifies an element by ::@:: The set of wavelengths it emits, not the colour a person sees in a flame.

## why the lines are discrete

The classical account of a glowing gas was that charged atoms and molecules are in motion and that an accelerating charge radiates a wave. A continuum of frequencies of motion would radiate a continuum of frequencies of light. A classical gas ought to glow with a smooth spread of colour, the way a hot filament does. The spectra show the opposite: separated lines with nothing at all in the gaps. Hydrogen is the clearest case, since its four visible lines are the ones the [Balmer series](Balmer%20series.md) writes a formula for.

The discrete-level picture accounts for those empty gaps; the level diagram below shows the same thing in symbols. An electron bound to a nucleus can only sit at certain allowed energies; between them it has none. A drop from $E_1$ to $E_0$ releases $E_1 - E_0$ as a single photon. That photon has energy $hf$, so $E_1 - E_0 = hf$ at its frequency $f$. Each difference between two allowed levels gives one wavelength. Fixing the lower level and letting the upper one run up the ladder gives a series of lines. The levels crowd together as they rise, so the differences between neighbours shrink and the series converges on a short-wavelength limit. The gaps between the lines are the light no allowed transition can produce.

![hydrogen energy levels: a ladder of horizontal levels from n=1 upward, with the Lyman, Balmer and Paschen series marked and series-limit arrows labelled 3.4, 1.9 and 1.1 micrometres, beside the visible spectrum band and a black-body curve](attachments/Hydrogen%20energy%20levels.svg)

Each element has its own allowed levels, so each has its own set of differences and its own set of emission wavelengths. Two elements emit the same line only when a difference between two of their levels coincides, an accident rather than a rule. The photon leaves on a transition between two states. Calling that a wave radiating off a vibrating atom is the assumption a classical gas has to give up.

---

Flashcards for this section are as follows:

- overview: why an excited gas emits separated lines rather than a continuous spread ::@:: Its electron can only occupy certain allowed energies, and each drop between two of them emits one photon carrying the difference, so only particular wavelengths can come out.
- the energy of the photon emitted in a drop from $E_1$ to $E_0$ ::@:: $E_1 - E_0 = hf$, the gap between the two levels.
- what the dark gaps between the lines of a line spectrum represent ::@:: Wavelengths that no allowed transition of the atom can produce.
- what the classical account of a glowing gas predicts, and where it fails ::@:: That accelerating charges radiate a continuous spread of frequencies, giving a smooth colour, which contradicts the separated lines and dark gaps that are observed; a photon leaves on a transition between two states rather than as a wave radiating off a vibrating atom.
- why two elements emit different lines ::@:: Their allowed energy levels differ, so the set of differences between levels, and with it the set of photon wavelengths, differs too.
- when can two elements emit a line at the same wavelength ::@:: When a difference between two allowed levels of one coincides with a difference between two of the other, an accident rather than a rule.
- the clearest case of separated lines, and the reason ::@:: Hydrogen, whose four visible lines are the ones the Balmer series writes a formula for.
- ![hydrogen energy levels: a ladder of horizontal levels from n=1 upward, with the Lyman, Balmer and Paschen series marked and series-limit arrows labelled 3.4, 1.9 and 1.1 micrometres, beside the visible spectrum band and a black-body curve](attachments/Hydrogen%20energy%20levels.svg) ::@:: A ladder of horizontal energy levels for hydrogen starting at $n=1$ near the nucleus and climbing, the Lyman, Balmer and Paschen series picked out on the left with arrows dropping to $n=1$, $n=2$ and $n=3$, series limits marked at $3.4$, $1.9$ and $1.1\ \mu\text{m}$, and the visible band with a black-body curve on the right. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the level diagram: why a series of lines ends at a short-wavelength limit ::@:: The levels crowd together as they climb, so the energy differences between neighbours shrink, and the wavelengths they produce approach a limit from above.

## lines as a fingerprint

A line spectrum identifies what a source is made of, even a source too remote to sample. Find the wavelengths at which it emits, match them against the spectra of the known elements, read off the composition. Before the spectroscope, the case for atoms rested on indirect behaviour: diffusion, the way a gas expands, the way a solid dissolves. A rival account could explain all of that. Spectroscopy put numbers on both sides of the dispute. The opponents of atomism, who held the atoms to be a bookkeeping fiction, had to account for a set of lines at fixed wavelengths rather than a colour; see [history of atomic theory](history%20of%20atomic%20theory.md).

A galaxy lying behind the cluster SMACS 0723 was measured the same way, at a far greater distance. Its light left it 13.1 billion years ago. A microshutter array spectrometer took that spectrum over roughly $3.3$ to $4.9\ \mu\text{m}$ and resolved the emission into individual lines, identified as oxygen, hydrogen, and neon.

A spectrum records only what the detector responded to. This detector is blind across a gap at about $4.3\ \mu\text{m}$, and any line falling inside it would be invisible. A feature missing from a measured spectrum is a fact about the instrument, not the source.

---

Flashcards for this section are as follows:

- overview: what a line spectrum lets a spectroscopist do ::@:: Identify the composition of a source that is too remote to be sampled.
- the evidence for atoms before the spectroscope ::@:: Indirect behaviour such as diffusion, the way a gas expands, and the way a solid dissolves.
- the galaxy whose spectrum was taken behind SMACS 0723, and how old its light is ::@:: The galaxy behind the cluster, whose light left it 13.1 billion years ago.
- the instrument that took that spectrum over roughly $3.3$ to $4.9\ \mu\text{m}$ ::@:: A microshutter array spectrometer.
- the elements identified in the lines of that spectrum ::@:: Oxygen, hydrogen, and neon.
- the detector gap in that spectrum, and where it sits ::@:: Near $4.3\ \mu\text{m}$, a range over which the detector records nothing. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the absence of a line in a measured spectrum has to be read carefully ::@:: A line falling inside a detector gap would be invisible, so absence shows only what the instrument could see.
- why a line spectrum carried more weight than the earlier indirect evidence for atoms ::@:: Its lines are fixed to particular wavelengths, so the case rested on measurements rather than on behaviour a rival account could also explain.
