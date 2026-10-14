---
aliases:
  - NMR
  - magnetic resonance
  - nuclear magnetic resonance
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/nuclear_magnetic_resonance
  - language/in/English
---

# nuclear magnetic resonance

Nuclear magnetic resonance is the absorption of a radiowave by nuclei placed in a magnetic field, at the one frequency the field's level spacing allows. The measurement ties a frequency to a field, and the constant of proportionality is the nucleus's own magnetic moment. Magnetic resonance imaging is the same absorption read inside a body, with position hidden in the frequency.

---

Flashcards for this section are as follows:

- what a nucleus absorbs in nuclear magnetic resonance, and what fixes the absorbing frequency ::@:: A radiowave quantum, at the frequency matching the spacing of the nucleus's field-split spin levels.
- the constant that a measured frequency-against-field line fixes ::@:: The nucleus's own magnetic moment.

## spin levels in a field

A nucleus of spin $I$ carries a magnetic moment proportional to that spin, $\mu = g_N\mu_N m_I$ along the field with $m_I$ the spin projection. The constant of proportionality is the nuclear g-factor $g_N$: a dimensionless number measuring the magnetism the nucleus builds per unit of spin, absorbing every detail of how its charge moves inside. An external field $B$ turns the orientations into separate levels. Neighbouring levels sit $\Delta E = g_N \mu_N B$ apart, with $\mu_N = e\hbar/2m_p$ the nuclear magneton, so the spacing grows in step with the field. A nucleus of spin zero has no moment to orient and no levels to split: it stays silent in any field.

---

Flashcards for this section are as follows:

- the spacing $\Delta E$ between neighbouring spin levels of a nucleus in an external field $B$ ::@:: $\Delta E = g_N \mu_N B$, with $g_N$ the nuclear g-factor and $\mu_N = e\hbar/2m_p$ the nuclear magneton.
- the proportionality $\mu = g_N\mu_N m_I$ between a nucleus's spin and its magnetic moment ::@:: The moment grows with the spin projection $m_I$, at the rate $g_N\mu_N$ per unit of spin.
- what the nuclear g-factor $g_N$ absorbs ::@:: Every detail of how the nucleus's charge moves inside: magnetism per unit of spin is one measured number, which is why $g_N$ differs between nuclei.
- how the level spacing of a nucleus behaves as the external field $B$ grows ::@:: It grows in step with the field, $\Delta E = g_N \mu_N B$ linear in $B$.
- what a spin-zero nucleus does in an external magnetic field ::@:: Nothing: with no moment to orient it has no split levels and absorbs at no frequency.

## the resonance condition

A radiowave quantum $hf$ meets the level spacing exactly when $hf = g_N \mu_N B$, and the nucleus absorbs. Sweeping the frequency therefore finds the absorbing field at $B = hf/(g_N \mu_N)$: frequency and resonant field rise together, and five frequency-field pairs fall on a straight line through the origin, $f = (g_N \mu_N/h) B$. The slope $g_N \mu_N / h$ is fixed by the nucleus alone, which is what makes the line a measurement rather than a calibration.

---

Flashcards for this section are as follows:

- the condition a radiowave quantum $hf$ meets for a nucleus of g-factor $g_N$ to absorb in a field $B$ ::@:: $hf = g_N \mu_N B$, the quantum matching the level spacing $\Delta E = g_N \mu_N B$.
- the absorbing field $B$ in terms of the radiowave frequency $f$ for a nucleus of g-factor $g_N$ ::@:: $B = hf/(g_N \mu_N)$: frequency and resonant field rise together.
- the shape of a frequency-against-resonant-field plot, and what its slope carries ::@:: A straight line through the origin, $f = (g_N \mu_N/h) B$; the slope is $g_N \mu_N / h$, the nucleus's own constant. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## moments in magnetons

Nuclear moments are counted in nuclear magnetons, not Bohr magnetons, because the carrier sits in the nucleus: $\mu_N = (m_e/m_p)\mu_B \approx \mu_B/1836$, the proton's mass replacing the electron's. Hydrogen's nucleus is a single proton and its moment is $\mu_p \approx 2.79\,\mu_N$, about $1.5 \times 10^{-3}\,\mu_B$: the proton's g-factor is $g_p \approx 5.58$, and with spin one-half the moment takes half of it, $g_p\mu_N/2$. The size of $g_p$ is the interpretation: a structureless charged spin-half particle carries $g \approx 2$ and one magneton, the electron being exactly such a particle, while the proton's $5.58$ counts the motion of charge inside it. The electron cloud contributes nothing to the resonance. Isotopes differ: carbon-12, spin zero, stays silent, while carbon-13, spin one-half, answers at its own frequency.

---

Flashcards for this section are as follows:

- the nuclear magneton $\mu_N$ in terms of the Bohr magneton ::@:: $\mu_N = (m_e/m_p)\mu_B \approx \mu_B/1836$, the proton's mass replacing the electron's in $e\hbar/2m$.
- hydrogen's nuclear magnetic moment $\mu_p$ from the proton's g-factor $g_p$ ::@:: $g_p \approx 5.58$ and spin one-half give $\mu_p = g_p\mu_N/2 = 2.79\,\mu_N$, about $1.5 \times 10^{-3}\,\mu_B$.
- why the proton's g-factor $g_p \approx 5.58$ exceeds the electron's $g \approx 2$ ::@:: The electron is structureless, so $g \approx 2$ is all it carries; the proton's $g$ also counts the motion of charge inside it, so its moment is $2.79$ magnetons rather than one.
- what gives the hydrogen atom its nuclear magnetic moment ::@:: The lone proton: its charge and spin carry the moment, and the electron cloud contributes nothing to the nuclear resonance.
- why two carbon isotopes differ in a magnetic-resonance measurement ::@:: Carbon-12 has spin zero and stays silent; carbon-13 has spin one-half and absorbs at its own frequency.

## magnetic resonance imaging

A magnetic resonance imaging (MRI) scanner measures the same resonance inside the body, on the hydrogen nuclei of water. A field gradient makes the resonant field, and so the resonant frequency, depend on position; the frequency a voxel absorbs therefore names where it sits, and the image is the absorption mapped over the body.

---

Flashcards for this section are as follows:

- what a magnetic resonance imaging (MRI) scanner measures, and which nuclei it measures them on ::@:: The nuclear magnetic resonance of the hydrogen nuclei of water.
- how position becomes readable in magnetic resonance imaging ::@:: A field gradient makes the resonant field, and the resonant frequency, depend on position, so the frequency a voxel absorbs names where it sits.
