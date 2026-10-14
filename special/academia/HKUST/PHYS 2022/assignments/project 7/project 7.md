---
aliases:
  - HKUST PHYS 2022 project 7 notes
  - HKUST PHYS2022 project 7 notes
  - PHYS 2022 project 7 notes
  - PHYS2022 project 7 notes
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/assignments/project_7/project_7
  - language/in/English
---

# project 7

- HKUST PHYS 2022 project 7
- parent: [project 7](index.md)

Project 7 measures nuclear magnetic resonance in four samples: hydrogen, then sodium, carbon-13, and an unknown. At each of five radiowave frequencies it finds the field at which the sample absorbs; the five frequency-field pairs fall on a straight line through the origin, and its slope fixes the nucleus's magnetic moment. The resonance condition, the level splitting behind it, and the units of nuclear moments are set out in [nuclear magnetic resonance](../../nuclear%20magnetic%20resonance.md).

---

Flashcards for this section are as follows:

- overview: what project 7 measures for each sample atom, and at how many settings ::@:: For each of four samples (hydrogen, then sodium, carbon-13, and an unknown): the magnetic field at which it absorbs, at each of five radiowave frequencies.

## the resonance line

Each sample contributes five points. The notations first: $\mu_N = e\hbar/2m_p$ is the nuclear magneton, the natural unit of nuclear magnetism and the same size for every nucleus. The moment grows in proportion to the nuclear spin, $\mu = g_N\mu_N m_I$ along the field with $m_I$ the spin projection, and the nuclear g-factor $g_N$ is that constant of proportionality: a dimensionless number, different for each nucleus, counting the magnetism its internal charge motion builds per unit of spin. The product $g_N\mu_N$ is the magnetic moment itself. The radiowave quantum meets the level spacing exactly when $hf = g_N \mu_N B$, so the absorbed field at frequency $f$ is $B = hf/(g_N \mu_N)$, and frequency and resonant field rise together; the five pairs fall on $f = (g_N \mu_N/h) B$ through the origin, a line because neither the moment nor $h$ changes along the sweep. The slope $s = g_N \mu_N / h$ therefore measures the moment: a larger moment needs less field to reach the same spacing, so its line is steeper, and the moment follows from the slope as $g_N \mu_N = h s$.

---

Flashcards for this section are as follows:

- what the five frequency-field pairs $(f, B)$ of one sample fall on ::@:: A straight line through the origin, $f = (g_N \mu_N/h) B$, with the absorbed field taken at each radiowave frequency.
- what the nuclear magneton $\mu_N$ is ::@:: $e\hbar/2m_p$, the natural unit of nuclear magnetism: the Bohr magneton with the proton's mass in place of the electron's, the same size for every nucleus.
- what the nuclear g-factor $g_N$ is ::@:: A dimensionless number, different for each nucleus: the magnetism built per unit of nuclear spin, telling how many magnetons that nucleus's moment carries.
- what the product $g_N\mu_N$ in the resonance condition $hf = g_N\mu_N B$ is ::@:: The nucleus's magnetic moment itself: $\mu_N$ supplies the unit, $g_N$ the number of units, and their product sets both the level spacing and the resonance line's slope.
- what the slope of a sample's resonance line gives ::@:: $g_N \mu_N / h$ for that nucleus, from which its magnetic moment follows. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- how a sample's resonance line of slope $s$ yields its nuclear magnetic moment ::@:: $g_N \mu_N = h s$, and dividing by $\mu_N$ counts the moment in nuclear magnetons.
- what a steeper resonance line says about the nucleus ::@:: A larger magnetic moment: it needs less field to reach the level spacing, so its frequency climbs faster with the field.

## moments and the unknown

The slope gives $g_N \mu_N$, and the sample atom's magnetic moment follows from it. The moment is counted in nuclear magnetons, roughly two thousand times below the Bohr-magneton scale, because the nuclear magneton carries the proton's mass where the Bohr magneton carries the electron's (see [moments in magnetons](../../nuclear%20magnetic%20resonance.md#moments%20in%20magnetons)). Hydrogen's line returns $\mu_p \approx 2.79\,\mu_N$: the proton's $g_p \approx 5.58$ and its spin one-half take half of the g-factor. The size of $g_p$ carries the interpretation: a structureless charged spin-half particle has $g \approx 2$ and one magneton, the electron being exactly such a particle, while the proton's $5.58$ counts the motion of charge inside it. In Bohr magnetons that is about $1.5 \times 10^{-3}\,\mu_B$, and the lone proton carries it all. The measured number sits above one magneton, which counting one unit of charge and one unit of spin would not give: the proton carries internal structure, and its moment reflects the motion of charge and spin inside it.

The unknown sample is read the same way. Each nucleus has its own g-factor and so its own slope, so matching the measured slope to a tabulated moment names the isotope.

---

Flashcards for this section are as follows:

- hydrogen's moment $\mu_p$ as its resonance line measures it ::@:: $\mu_p \approx 2.79\,\mu_N$, about $1.5 \times 10^{-3}\,\mu_B$.
- how the resonance line identifies an unknown sample ::@:: Each nucleus has its own g-factor and slope, so matching the measured slope to a tabulated moment names the isotope.
- why the proton's g-factor $g_p \approx 5.58$ exceeds the electron's $g \approx 2$ ::@:: The electron is structureless, so $g \approx 2$ is all it carries; the proton's $g$ also counts the motion of charge inside it, so its moment is $2.79$ magnetons rather than one.
- why hydrogen's measured moment $\mu_p \approx 2.79\,\mu_N$ exceeds one nuclear magneton ::@:: Counting one unit of charge and one unit of spin would give one magneton; the proton carries internal structure, so its moment reflects the motion of charge and spin inside it.
