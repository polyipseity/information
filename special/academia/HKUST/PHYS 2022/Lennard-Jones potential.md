---
aliases:
  - LJ potential
  - Lennard-Jones 12-6 potential
  - Lennard-Jones potential
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Lennard-Jones_potential
  - language/in/English
---

# Lennard-Jones potential

The Lennard-Jones potential is the standard model of the energy between two neutral atoms. It carries a steep repulsive core and a slow attractive tail, written either with the coefficients $C_6$ and $C_{12}$ or with the length and energy scales $\sigma$ and $\varepsilon$, the two writings converting into each other.

---

Flashcards for this section are as follows:

- overview: the shape of the Lennard-Jones potential ::@:: A steep repulsive core under a slow attractive tail, the energy between two neutral atoms.
- the two ways the Lennard-Jones potential is written: with $C_6$ and $C_{12}$, or with $\sigma$ and $\varepsilon$ ::@:: With the coefficients $C_6$ and $C_{12}$, or with the scales $\sigma$ and $\varepsilon$; the writings convert into each other.

## dispersion and exclusion terms

$V(r) = -C_6/r^6 + C_{12}/r^{12}$: the $r^{-6}$ term attracts and the $r^{-12}$ term repels. The attraction is the dispersion interaction: each atom's electron cloud fluctuates into an instantaneous dipole, and the two dipoles pull on each other. The repulsion is the exclusion principle refusing the overlap of the two electron clouds as they are forced together.

---

Flashcards for this section are as follows:

- the Lennard-Jones potential between two neutral atoms a distance $r$ apart ::@:: $V(r) = -C_6/r^6 + C_{12}/r^{12}$: an $r^{-6}$ attraction under an $r^{-12}$ repulsion.
- the origin of the $r^{-6}$ attraction in the Lennard-Jones potential ::@:: The dispersion interaction: fluctuating electron clouds form instantaneous dipoles that pull on each other.
- the origin of the $r^{-12}$ repulsion in the Lennard-Jones potential ::@:: The exclusion principle resisting the overlap of the two electron clouds as they are pushed together.

## reduced form

Written in the scales the curve is built from, the same potential reads $V(r) = 4\varepsilon\left[(\sigma/r)^{12} - (\sigma/r)^6\right]$. There $\sigma$ is the separation where $V$ crosses zero and $\varepsilon$ is the well depth, the potential reaching $-\varepsilon$ at its bottom. Matching the two writings term by term gives $C_6 = 4\varepsilon\sigma^6$ and $C_{12} = 4\varepsilon\sigma^{12}$, so each pair of constants converts into the other: $\sigma = (C_{12}/C_6)^{1/6}$ and $\varepsilon = C_6^2/(4C_{12})$.

---

Flashcards for this section are as follows:

- the scale form $V(r)$ of the Lennard-Jones potential, in the scales $\sigma$ and $\varepsilon$ ::@:: $V(r) = 4\varepsilon\left[(\sigma/r)^{12} - (\sigma/r)^6\right]$.
- what the scales $\sigma$ and $\varepsilon$ mark on the Lennard-Jones curve ::@:: $\sigma$ is the separation where $V$ crosses zero; $\varepsilon$ is the well depth, $V = -\varepsilon$ at the bottom.
- the conversions between $C_6$, $C_{12}$, $\sigma$, and $\varepsilon$ ::@:: $C_6 = 4\varepsilon\sigma^6$ and $C_{12} = 4\varepsilon\sigma^{12}$, hence $\sigma = (C_{12}/C_6)^{1/6}$ and $\varepsilon = C_6^2/(4C_{12})$.

## equilibrium and small oscillation

The potential bottoms out at $r_{\min} = 2^{1/6}\sigma \approx 1.12\,\sigma$, where $V(r_{\min}) = -\varepsilon$. A pair held there feels no force, and a pair displaced slightly swings about it: expanding $V$ about $r_{\min}$ leaves a harmonic stiffness $V''(r_{\min}) = 36 \cdot 2^{2/3}\varepsilon/\sigma^2$, so the angular frequency is $\omega = \sqrt{V''(r_{\min})/\mu}$ with $\mu = m_1 m_2/(m_1 + m_2)$ the reduced mass of the pair. Equal scales then separate the pairs by mass alone: the heavier pair swings more slowly.

---

Flashcards for this section are as follows:

- the separation $r_{\min}$ at which the Lennard-Jones potential bottoms out, and the value of $V$ there ::@:: $r_{\min} = 2^{1/6}\sigma \approx 1.12\,\sigma$, with $V(r_{\min}) = -\varepsilon$.
- the angular frequency of a pair's small oscillation about $r_{\min}$ ::@:: $\omega = \sqrt{V''(r_{\min})/\mu}$, with the stiffness $V''(r_{\min}) = 36 \cdot 2^{2/3}\varepsilon/\sigma^2$ and $\mu$ the reduced mass.
- the reduced mass of two atoms of masses $m_1$ and $m_2$ ::@:: $\mu = m_1 m_2/(m_1 + m_2)$, and at equal scales it sets the pair's oscillation frequency.
- two atom pairs with equal $\sigma$ and $\varepsilon$ but different masses: how their oscillation frequencies compare ::@:: The heavier pair swings more slowly, since the reduced mass sits under the square root in $\omega = \sqrt{V''/\mu}$.

## neutral atom pairs

The potential describes pairs of neutral atoms, the rare gases first among them: the same dispersion attraction that binds liquid argon is the attraction an ideal gas neglects, and the repulsive wall is what stops a condensed phase from collapsing. It is not a chemical bond: no charges are exchanged, and the well depth measures in thousandths to hundredths of an electronvolt, far below the electronvolts that hold a bond together.

---

Flashcards for this section are as follows:

- which atoms the Lennard-Jones potential describes, and what kind of interaction it is ::@:: Pairs of neutral atoms, rare gases first among them; a dispersion attraction under an overlap repulsion, with no charges exchanged.
- how the Lennard-Jones well depth compares with the energy of a chemical bond ::@:: Thousandths to hundredths of an electronvolt, far below the electronvolts that hold a bond together.
- what the attraction of the Lennard-Jones potential is that the ideal-gas model neglects ::@:: The dispersion attraction between the atoms' fluctuating electron clouds, the same attraction that binds liquid argon.
