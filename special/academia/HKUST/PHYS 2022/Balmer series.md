---
aliases:
  - Balmer lines
  - Balmer series
  - hydrogen line spectrum
  - spectral series
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Balmer_series
  - language/in/English
---

# Balmer series

Hydrogen's lines do not fall at random. Four of them lie in the visible. Past those four the series crowds towards a limit in the ultraviolet. The pattern is regular enough to be written down as a formula.

The _Balmer series_ is that formula together with the lines it produces. Johann Balmer published the fit in 1885.

Hydrogen showed the pattern first. Its atom holds a single electron, which leaves few possible transitions and few, well separated lines. Every other element has more lines, crowded and interleaved, and the regularity is lost among them.

A spectral series is the set of lines produced by all the transitions that end on one and the same level. The end level fixes where the series falls, because the energy drop onto that level sets the photon energy. The Lyman series ends on the ground state and lies entirely in the ultraviolet; the Paschen series ends on the third level and lies in the infrared. The Balmer series ends on the second level, in the visible.

---

Flashcards for this section are as follows:

- overview: what the Balmer series is ::@:: A relation fitted to the measured wavelengths of the visible hydrogen lines, together with the lines it produces.
- who found the Balmer formula, and when ::@:: Johann Balmer, in 1885.
- how many hydrogen lines lie in the visible, and what happens past them ::@:: Four of them, and the series then crowds towards a limit in the ultraviolet.
- what a spectral series is ::@:: The set of lines produced by all the transitions that end on one and the same energy level.
- why hydrogen showed the pattern before any other element did ::@:: Hydrogen has a single electron, so it has few possible transitions; its lines are few and well separated. Other elements have more lines, crowded and interleaved.
- where the Lyman, Balmer, and Paschen series fall, which level each ends on, and why ::@:: Lyman ends on the ground state in the ultraviolet, Balmer on the second level in the visible, Paschen on the third in the infrared, because the end level fixes the energy drop onto that level, and the drop fixes the photon energy.

## the Balmer formula

Balmer's relation gives the wavelength of a line in terms of a single integer $k$: $\lambda = 364.56\,\dfrac{k^2}{k^2 - 4}\ \text{nm}$, where $k = 3, 4, 5, \ldots$ and $k > 2$. The restriction $k > 2$ is not a convenience. At $k = 2$ the denominator $k^2 - 4$ vanishes and the expression has no value.

Each $k$ is a whole number, so the formula returns one fixed wavelength per line and no line can be shifted. With $k = 3$, $\lambda = 364.56 \times \dfrac{9}{9 - 4} = 364.56 \times \dfrac{9}{5} = 656.3\ \text{nm}$, the red line. With $k = 4$, $\lambda = 364.56 \times \dfrac{16}{16 - 4} = 364.56 \times \dfrac{4}{3} = 486.1\ \text{nm}$, the blue-green line.

As $k$ grows the two terms $k^2$ and $k^2 - 4$ come closer together, the ratio $k^2/(k^2 - 4)$ falls towards 1, and the wavelengths shorten towards $364.56\ \text{nm}$. That value is the series limit. The ratio stays above 1 for every $k$ the formula admits, so no line falls below the series limit.

---

Flashcards for this section are as follows:

- overview: the Balmer formula, in terms of the integer $k$ ::@:: $\lambda = 364.56\,\dfrac{k^2}{k^2 - 4}\ \text{nm}$, with $k = 3, 4, 5, \ldots$ and $k > 2$.
- the Balmer formula with $k = 3$: the wavelength produced ::@:: $\lambda = 364.56 \times \dfrac{9}{5} = 656.3\ \text{nm}$, the red line.
- the Balmer formula with $k = 4$: the wavelength produced ::@:: $\lambda = 364.56 \times \dfrac{4}{3} = 486.1\ \text{nm}$, the blue-green line.
- the restriction on $k$ in the Balmer formula, and why it is there ::@:: $k > 2$, because at $k = 2$ the denominator $k^2 - 4$ vanishes and the expression has no value.
- the constant in $\lambda = 364.56\,\dfrac{k^2}{k^2 - 4}\ \text{nm}$: its value, its units, and what the series approaches ::@:: $364.56$ in nanometres, the series limit.
- why the wavelengths in the series shorten as $k$ grows ::@:: Because $k^2$ and $k^2 - 4$ come closer together, the ratio $k^2/(k^2 - 4)$ falls towards 1, and the wavelength approaches $364.56\ \text{nm}$ from above.
- why no Balmer line lies below the series limit at $364.56\ \text{nm}$ ::@:: The ratio $k^2/(k^2 - 4)$ stays above 1 for every $k$ the formula admits, so the wavelength never drops below $364.56\ \text{nm}$.
- can the position of a Balmer line be moved once the formula is fixed ::@:: No, because each $k$ is a whole number and the formula returns one fixed wavelength per line. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## where the lines fall

Taking $k$ in turn gives the lines in order of decreasing wavelength. $k = 3$ gives $656.3\ \text{nm}$ in the red and $k = 4$ gives $486.1\ \text{nm}$ in the blue-green. $k = 5$ and $k = 6$ give $434.0\ \text{nm}$ and $410.2\ \text{nm}$ in the violet, and those four are the ones the eye sees. $k = 7$ gives $397.0\ \text{nm}$ as the series runs into the ultraviolet. The lines carry on towards the limit, with $365.0\ \text{nm}$ among them. Past the visible the lines are measured on a plate or a detector.

The spacing collapses as $k$ grows. From $k = 3$ to $k = 4$ the wavelengths differ by $170\ \text{nm}$. Once $k$ is large the neighbouring lines sit a nanometre or two apart, packed against the limit at $364.56\ \text{nm}$. Since $k$ runs over the integers without end, infinitely many lines crowd above $364.56\ \text{nm}$, which is where the hydrogen spectrum shows its edge.

---

Flashcards for this section are as follows:

- overview: the wavelengths of the four visible Balmer lines, from about $400$ to $700\ \text{nm}$ ::@:: $656.3\ \text{nm}$ in the red, $486.1\ \text{nm}$ in the blue-green, and $434.0\ \text{nm}$ and $410.2\ \text{nm}$ in the violet.
- the Balmer lines for $k = 7$ and beyond, which run towards the ultraviolet ::@:: $397.0\ \text{nm}$ at $k = 7$, then a run of lines in the ultraviolet, with $365.0\ \text{nm}$ among those close to the limit.
- the Balmer lines the eye does not see: how they are measured ::@:: On a plate or a detector.
- the wavelength of the series limit ::@:: $364.56\ \text{nm}$, the shortest wavelength the Balmer series can produce. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- how the spacing between neighbouring Balmer lines changes as $k$ grows, starting from the $k = 3$ to $k = 4$ gap ::@:: It collapses, from $170\ \text{nm}$ between those two lines down to a nanometre or two once $k$ is large.
- why infinitely many lines can lie above the series limit at $364.56\ \text{nm}$ ::@:: $k$ runs over the integers without end, and the lines keep shortening towards the limit without crossing it.
- what the edge in a hydrogen spectrum marks ::@:: The wavelength at which the Balmer lines stop, $364.56\ \text{nm}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## why the formula is a puzzle

Nothing in the physics of the time picked out $656.3\ \text{nm}$. Classical theory puts the electron in orbit, and an orbit radiates a continuous spread of frequencies, so it predicts a smear where the measurement finds four separated lines. Discrete levels account for the separation: the available energies are discrete, and the wavelengths are fixed by the differences between them. What discrete levels do not explain is why the values come out at exactly those numbers. The levels themselves are drawn in [emission spectrum](emission%20spectrum.md).

Any four wavelengths can be fitted. This one carries a single constant and no free parameter. The constant $364.56\ \text{nm}$ was fixed by the lines already seen, and the ultraviolet lines it then predicted were found afterwards, at the wavelengths it gave.

The quantum argument from 1895 onwards is about failures of this sort, set out in [modern physics](modern%20physics.md). The Balmer formula is evidence that atoms are real, as [history of atomic theory](history%20of%20atomic%20theory.md) sets out. Continuous matter cannot produce a formula with no free parameter that predicts lines nobody had measured.

---

Flashcards for this section are as follows:

- overview: what made the Balmer formula puzzling ::@:: Nothing in classical physics required hydrogen to emit at those particular wavelengths, and its picture of an orbiting charge predicts a continuous smear rather than separated lines.
- what classical theory predicts for a radiating atomic electron ::@:: A continuous spread of frequencies, since an accelerating charge radiates and an orbit has a continuum of frequencies in it.
- how the discrete energy levels account for the lines being separated ::@:: The available energies are discrete, so the differences between them are discrete, and the photon wavelengths are fixed by those differences.
- what the discrete-level picture leaves unexplained about the Balmer formula ::@:: That the wavelengths come out at exactly the measured values, even though it accounts for the lines existing at all.
- what made the Balmer formula more than a fit, and what it showed about atoms ::@:: It carries one constant and no free parameter, so it predicted lines that had not been measured, and those lines were found afterwards. Continuous matter cannot do that.
- the value of the single constant in the Balmer formula $\lambda = 364.56\,\dfrac{k^2}{k^2 - 4}\ \text{nm}$ ::@:: $364.56\ \text{nm}$, fixed by the lines that had already been measured.
