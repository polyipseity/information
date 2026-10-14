---
aliases:
  - SPM
  - atomic force microscope
  - scanning probe microscopes
  - scanning probe microscopy
  - scanning tunnelling microscope
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/scanning_probe_microscopes
  - language/in/English
---

# scanning probe microscopes

A scanning probe microscope drags a sharp tip across a surface, an atom's diameter away from it, and turns what the tip feels at each point into a contour map of the surface atom by atom. The family shares that arrangement: one sharp tip, scanned over the surface, with a feedback loop holding the tip–sample interaction fixed while the scan runs. The members differ in what they feel. A scanning tunnelling microscope feels a tunnelling current across the gap and needs a conducting sample. An atomic force microscope feels the force on a soft cantilever and works on any surface. The STM came first, built by Binnig and Rohrer in the early 1980s (Nobel Prize 1986), and the AFM followed in 1985.

---

Flashcards for this section are as follows:

- overview: how a scanning probe microscope builds its image ::@:: A sharp tip is scanned across the surface an atom's diameter away while feedback holds the tip–sample interaction fixed, and the tip's height at each point draws a contour map of the surface atom by atom.
- what a scanning tunnelling microscope (STM) and an atomic force microscope (AFM) each feels at the tip ::@:: An STM feels the tunnelling current across the tip–surface gap, so it needs a conducting sample; an AFM feels the force on a soft cantilever, so it works on any surface.

## scanning tunnelling microscope

The scanning tunnelling microscope turns the exponential into a ruler. A sharp metallic tip hovers within $d < 1$ nm of a conducting surface, and a bias voltage drives a tunnelling current across the vacuum gap $d$. The current depends on the local electron density at the Fermi level. The gap itself acts as the barrier, with its height near the work function $\phi$ of the tip, because the bias shares that energy scale.

The standard operating mode holds the current steady rather than the tip. A feedback loop compares the tunnelling current with its set value and moves the tip up or down to restore it as the scan runs, so the recorded tip height traces the surface contours. The currents are small, down to a few picoamperes. A gap change of only 0.4 nm moves the current by a factor of $10^4$.

For a wide gap the [transmission probability](quantum%20tunnelling.md#transmission%20probability) through the barrier is $T_{\mathrm{gap}} \approx e^{-2\kappa d}$, with $\kappa = \sqrt{2m\phi}/\hbar$ the rectangular-barrier decay constant with $V_0$ replaced by $\phi$. The current is the incident electron flux times the transmission, so the flux carries the bias voltage and the tunnelling factor is $T_{\mathrm{gap}}$. The chain gives $I \propto V e^{-2\kappa d}$.

The sensitivity follows from that exponential. A fractional gap change $dd$ moves the current by $dI/I = -2\kappa\, dd$. With $\phi \approx 5$ eV the decay constant is $\kappa \approx 1.15\ \mathrm{\AA}^{-1}$, so $2\kappa \approx 2.3\ \mathrm{\AA}^{-1}$. Each extra ångström of gap therefore multiplies $I$ by $e^{-2.3} \approx 0.1$, nearly an order of magnitude per ångström.

Because $I$ falls by nearly an order of magnitude for each ångström of extra gap, the current tracks the tip–surface distance with sub-ångström precision, and scanning the tip across the surface maps the surface atom by atom, corrugations of order 0.3 nm on gold, magnified to a visible image. The microscope measures distance through tunnelling probability itself.

---

Flashcards for this section are as follows:

- what carries the distance information in a scanning tunnelling microscope (STM) current $I \propto V e^{-2d\sqrt{2m\phi}/\hbar}$ ::@:: The tunnelling dependence $I \propto V\,e^{-2d\sqrt{2m\phi}/\hbar}$ on the tip–surface gap $d$.
- how the scanning tunnelling microscope (STM) current $I \propto V e^{-2\kappa d}$ follows from the gap transmission ::@:: The wide-gap transmission is $T_{\mathrm{gap}} \approx e^{-2\kappa d}$ with $\kappa = \sqrt{2m\phi}/\hbar$, and the current is incident flux times transmission, with the flux carrying the bias $V$.
- the sensitivity of a scanning tunnelling microscope (STM) current to a gap change $dd$ ::@:: $dI/I = -2\kappa\, dd$; with $\phi \approx 5$ eV, $\kappa \approx 1.15\ \mathrm{\AA}^{-1}$, so each extra ångström multiplies $I$ by $e^{-2.3} \approx 0.1$.
- the sensitivity of a scanning tunnelling microscope (STM) to gap width ::@:: Nearly one order of magnitude of current per ångström of extra separation, enough for atomic resolution.
- what holds a scanning tunnelling microscope (STM) tip at constant current while it scans ::@:: A feedback loop moves the tip up or down until the current returns to its set value, and the tip's height at each point traces the surface contours.

## atomic force microscope

An atomic force microscope reads force instead of current. A sharp tip rides on the end of a soft cantilever, and the interatomic forces between tip and sample bend the cantilever as the tip passes over each atom. A laser reflects off the back of the cantilever onto a position-sensitive detector, and the feedback signal from that detector moves the sample up and down until the deflection, and so the force, sits at its set value. The recorded motion of the sample is the topography.

The arrangement is that of a record-player stylus crossing a groove, about a million times more sensitive. Cantilevers are microfabricated from silicon with spring constants as small as 0.1 N/m, against about 1 N/m for a 4 mm by 1 mm piece of household aluminium foil. They run roughly 100 μm across and 1 μm thick. The tapered tip may end 50 nm across, and the tracking forces reach down to $10^{-9}$ N. The feedback holds the deflection small enough that the tip never damages or distorts the sample atoms.

Because it senses force rather than current, the AFM needs no conducting surface, no special sample preparation, and no expensive vacuum. That opens ceramics, polymers, optical surfaces, and biological specimens from DNA to leaf sections. The sensitivity has a price: air currents and even voices move the cantilever, so the instrument needs special vibrational insulation.

---

Flashcards for this section are as follows:

- overview: how an atomic force microscope turns tip–sample force into a topographic map ::@:: The interatomic forces bend a soft cantilever carrying the tip, a laser reflected onto a position detector reads the deflection, feedback moves the sample until the deflection is fixed, and the recorded sample motion is the topography.
- the spring constant of a microfabricated atomic force microscope (AFM) cantilever, set against household aluminium foil ::@:: Silicon cantilevers reach 0.1 N/m, while a 4 mm by 1 mm piece of household aluminium foil is about 1 N/m.
- the tracking force and tip end-size of an atomic force microscope (AFM) ::@:: Tracking forces reach down to $10^{-9}$ N, and the tapered tip may end only 50 nm across. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what an atomic force microscope (AFM) needs that a scanning tunnelling microscope (STM) does not, and the surfaces that follow from it ::@:: No conducting surface, no special sample preparation, and no expensive vacuum; ceramics, polymers, optical surfaces, and biological specimens can all be imaged.
- why an atomic force microscope (AFM) needs special vibrational insulation ::@:: Air currents and even human voices move the sensitive cantilever, so the instrument must be isolated from vibration.
