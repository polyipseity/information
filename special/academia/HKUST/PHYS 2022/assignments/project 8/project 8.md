---
aliases:
  - HKUST PHYS 2022 project 8 notes
  - HKUST PHYS2022 project 8 notes
  - PHYS 2022 project 8 notes
  - PHYS2022 project 8 notes
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/assignments/project_8/project_8
  - language/in/English
---

# project 8

- HKUST PHYS 2022 project 8
- parent: [project 8](index.md)

Project 8 measures the potential energy between two neutral atoms, the [Lennard-Jones potential](../../Lennard-Jones%20potential.md). It derives the potential's length and energy scales from the oxygen–oxygen coefficients, sets the axes of the potential-energy curve with those scales, measures the same two scales for five more atom pairs, and reads each pair's oscillation frequency about its equilibrium separation. The ideal-gas model in [kinetic theory of gases](../../kinetic%20theory%20of%20gases.md#ideal%20gas%20law) neglects exactly this attraction and repulsion between neighbouring atoms, and the same repulsive wall is what an [atomic force microscope](../../scanning%20probe%20microscopes.md#atomic%20force%20microscope) rides on.

---

Flashcards for this section are as follows:

- overview: what project 8 derives, measures, and compares for each atom pair ::@:: The length scale $\sigma$ and energy scale $\varepsilon$ of the pair potential, the coefficients $C_{12}$ and $C_6$ that follow from them, and the small-oscillation frequency about the equilibrium separation. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## scales and coefficients

The curve's two terms and their physical origins are set out in [Lennard-Jones potential](../../Lennard-Jones%20potential.md); the project applies the conversions. Two short steps give both scales. Setting $V(\sigma) = 0$ gives $-C_6/\sigma^6 + C_{12}/\sigma^{12} = 0$, that is $C_{12}/C_6 = \sigma^6$, so $\sigma = (C_{12}/C_6)^{1/6}$; $C_{12}/C_6$ carries $\mathrm{m}^6$, so the sixth root is a length. The energy scale follows from the same matching: $C_6 = 4\varepsilon\sigma^6$, so $\varepsilon = C_6/(4\sigma^6) = C_6^2/(4C_{12})$ once $\sigma^6 = C_{12}/C_6$ is substituted; $(\text{J}\,\text{m}^6)^2/(\text{J}\,\text{m}^{12})$ leaves an energy, as it must.

The two scales then read straight off the curve. $\sigma$ is the separation where attraction and repulsion cancel: closer in, the $r^{-12}$ wall takes over and the pair resists compression; farther out, the $r^{-6}$ tail takes over and the pair pulls itself together. So $\sigma$ acts as the atom's own diameter, and $\varepsilon$ as the depth of the trap holding the pair together. $\varepsilon$ also sets the temperature scale of the attraction: rare-gas wells are a few meV deep, room temperature carries $k_B T \approx 25$ meV, and thermal motion that far above the well depth keeps the atoms apart, which is why the rare gases stay gaseous. Those two scales set the axes of the potential-energy curve. The other pairs (neon–neon, argon–argon, neon–argon, neon–oxygen, and argon–oxygen) are then measured against those axes and converted back to $C_{12}$ and $C_6$ with the same two relations.

---

Flashcards for this section are as follows:

- where project 8's axis scales $\sigma$ and $\varepsilon$ come from ::@:: The oxygen–oxygen coefficients: $\sigma = (C_{12}/C_6)^{1/6}$ and $\varepsilon = C_6^2/(4C_{12})$, set once and reused for every pair.
- how the zero crossing fixes $\sigma$ from the coefficients ::@:: $V(\sigma) = 0$ gives $C_{12}/C_6 = \sigma^6$, so $\sigma = (C_{12}/C_6)^{1/6}$; $C_{12}/C_6$ carries $\mathrm{m}^6$, so the sixth root is a length.
- how $\varepsilon$ follows from $C_6$ and the scale $\sigma$ ::@:: Term matching gives $C_6 = 4\varepsilon\sigma^6$, so $\varepsilon = C_6/(4\sigma^6) = C_6^2/(4C_{12})$ using $\sigma^6 = C_{12}/C_6$; the units leave an energy.
- the pairs whose scales $\sigma$ and $\varepsilon$ project 8 measures against those axes ::@:: Neon–neon, argon–argon, neon–argon, neon–oxygen, and argon–oxygen, each converted back to $C_{12}$ and $C_6$ with the same relations.
- what the scale $\sigma$ means physically on the Lennard-Jones curve ::@:: The separation where attraction and repulsion cancel: inside it the $r^{-12}$ wall dominates and resists compression, outside it the $r^{-6}$ tail dominates and pulls the pair together; it acts as the atom's own diameter.
- what the depth $\varepsilon$ means physically, and what it is measured against ::@:: The depth of the trap holding the pair together, set against the thermal energy $k_B T$: rare-gas wells a few meV deep lose to $k_B T \approx 25$ meV at room temperature, which is why the rare gases stay gaseous.

## equilibrium and oscillation

The equilibrium separation follows from the same coefficients: setting $\mathrm{d}V/\mathrm{d}r = 6C_6/r^7 - 12C_{12}/r^{13} = 0$ gives $r_{\min}^6 = 2C_{12}/C_6 = 2\sigma^6$, so $r_{\min} = 2^{1/6}\sigma$, the bottom sitting about 12% outside the zero crossing. Substituting back into $V$ gives $V(r_{\min}) = -C_6^2/(4C_{12}) = -\varepsilon$, the depth the conversion already predicted. A pair displaced slightly from $r_{\min}$ swings about it, and near the bottom the curve is a parabola, $V \approx -\varepsilon + \frac12 V''(r_{\min})(r - r_{\min})^2$, so the restoring force obeys Hooke's law with spring constant $V''(r_{\min})$. The two atoms both move, and their joint motion reduces to one coordinate of mass $\mu = m_1 m_2/(m_1 + m_2)$, the reduced mass, measured about the common centre of mass. The angular frequency is $\omega = \sqrt{V''(r_{\min})/\mu}$. The stiffness $V''(r_{\min}) = 36 \cdot 2^{2/3}\varepsilon/\sigma^2$, given in [equilibrium and small oscillation](../../Lennard-Jones%20potential.md#equilibrium%20and%20small%20oscillation), makes the trend readable: at fixed masses $\omega \propto \sqrt{\varepsilon}/\sigma$, so a deeper, narrower pair vibrates faster, and a heavier pair slower. The project computes that frequency from the measured coefficients, then displaces the moving atom and times the swing in the simulation; the ratio of measured to computed frequency converts simulated time into real time.

---

Flashcards for this section are as follows:

- how the equilibrium separation $r_{\min}$ follows from the coefficients ::@:: Setting $\mathrm{d}V/\mathrm{d}r = 6C_6/r^7 - 12C_{12}/r^{13} = 0$ gives $r_{\min}^6 = 2C_{12}/C_6 = 2\sigma^6$, so $r_{\min} = 2^{1/6}\sigma$.
- how the well depth $\varepsilon$ read off the minimum follows from the coefficients ::@:: Substituting $r_{\min}^6 = 2C_{12}/C_6$ into $V$ gives $V(r_{\min}) = -C_6^2/(4C_{12}) = -\varepsilon$, the depth the conversion $\varepsilon = C_6^2/(4C_{12})$ already predicted.
- where the harmonic frequency $\omega = \sqrt{V''(r_{\min})/\mu}$ comes from ::@:: Near $r_{\min}$ the potential is a parabola of stiffness $V''(r_{\min})$, so the restoring force is Hooke-like and $\mu\ddot{x} = -V''x$ gives $\omega = \sqrt{V''/\mu}$.
- why the reduced mass $\mu = m_1 m_2/(m_1 + m_2)$ governs the swing ::@:: Both atoms move about their common centre of mass, and the two-body motion reduces to one coordinate of mass $\mu$; at the same stiffness the heavier pair swings more slowly.
- the parabola $V \approx -\varepsilon + \frac12 V''(r_{\min})(r - r_{\min})^2$ the pair feels near the bottom ::@:: A harmonic well: the restoring force obeys Hooke's law with spring constant $V''(r_{\min})$, which is why small displacements oscillate at $\omega = \sqrt{V''(r_{\min})/\mu}$.
- how $\omega \propto \sqrt{\varepsilon}/\sigma$ reads as physics ::@:: A deeper, narrower well is a stiffer spring and vibrates faster; a heavier pair, through $\mu$ under the root, vibrates slower.
- how project 8 obtains a pair's oscillation frequency twice ::@:: Computed from the measured coefficients through $\omega = \sqrt{V''(r_{\min})/\mu}$, and measured by displacing the atom slightly and reading the swing. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what comparing the measured and computed oscillation frequencies calibrates ::@:: The simulation's clock: their ratio converts simulated time into real time.
