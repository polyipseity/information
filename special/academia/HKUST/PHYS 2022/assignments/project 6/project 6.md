---
aliases:
  - HKUST PHYS 2022 project 6 notes
  - HKUST PHYS2022 project 6 notes
  - PHYS 2022 project 6 notes
  - PHYS2022 project 6 notes
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/assignments/project_6/project_6
  - language/in/English
---

# project 6

- HKUST PHYS 2022 project 6
- parent: [project 6](index.md)

Project 6 measures how an electron's transmission probability through a rectangular potential barrier responds to each of three quantities: the barrier height, the barrier width, and the total energy, held always below the barrier top. Each quantity is swept across five values with the other two fixed; each sweep checks one dependence of the exact formula. The exact result and its thick-barrier limit are derived in [quantum tunnelling](../../quantum%20tunnelling.md#transmission%20probability).

---

Flashcards for this section are as follows:

- overview: what project 6 sweeps, and what it measures at each setting ::@:: Three quantities of an electron at a rectangular barrier: the barrier height, the barrier width, and the total energy, each across five values with the other two fixed; at each setting the transmission probability.

## transmission against barrier width

At fixed barrier height $V_0$ and fixed energy $E < V_0$, the decay constant inside the barrier is fixed too. Energy conservation there reads $E = p^2/2m + V_0$, and with $E$ below $V_0$ the momentum squared comes out negative: $p = i\hbar\kappa$ with $\kappa = \sqrt{2m(V_0-E)}/\hbar$. A wave $e^{ipx/\hbar}$ with that momentum stops oscillating and decays as $e^{-\kappa x}$, so $1/\kappa$ is the distance over which the amplitude falls by $e$. With $V_0$ and $E$ both fixed, $\kappa$ is fixed, and only $L$ varies, through the exponent $2\kappa L$.

The exact probability is $T = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0 - E)}\right]^{-1}$. Once $\kappa L$ exceeds about one the hyperbolic sine grows as $e^{\kappa L}/2$, so $\sinh^2(\kappa L)$ grows as $e^{2\kappa L}/4$, the bracket is overtaken by $\frac{V_0^2}{16E(V_0-E)}e^{2\kappa L}$, and inverting leaves $T \approx 16\frac{E}{V_0}\left(1 - \frac{E}{V_0}\right)e^{-2\kappa L}$. So $T$ against $L$ is a decaying exponential: the amplitude falls by $e^{-\kappa L}$ across the barrier, the probability by $e^{-2\kappa L}$; every extra $1/\kappa$ of width costs a factor $e^{2}$, and doubling $L$ squares $T$.

---

Flashcards for this section are as follows:

- at fixed barrier height $V_0$ and energy $E < V_0$, how the transmission probability $T$ depends on the barrier width $L$ ::@:: $T$ falls exponentially with $L$, as $e^{-2\kappa L}$: doubling the width squares the transmission.
- why the width dependence of $T$ is exponential rather than algebraic ::@:: The wave decays as $e^{-\kappa x}$ inside the barrier, so crossing the width $L$ multiplies the amplitude by $e^{-\kappa L}$ and the probability, its square, by $e^{-2\kappa L}$.
- the exact transmission probability of a rectangular barrier of height $V_0$ and width $L$ at energy $E < V_0$ ::@:: $T = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0 - E)}\right]^{-1}$ with $\kappa = \sqrt{2m(V_0-E)}/\hbar$.
- where the decay constant $\kappa = \sqrt{2m(V_0-E)}/\hbar$ inside the barrier comes from ::@:: Energy conservation $E = p^2/2m + V_0$ with $E < V_0$ forces $p = i\hbar\kappa$, so the wave stops oscillating and decays as $e^{-\kappa x}$.
- how the thick-barrier formula $T \approx 16(E/V_0)(1 - E/V_0)e^{-2\kappa L}$ follows from the exact one ::@:: For $\kappa L \gg 1$, $\sinh^2(\kappa L)$ grows as $e^{2\kappa L}/4$, the bracket is overtaken by $\frac{V_0^2}{16E(V_0-E)}e^{2\kappa L}$, and inverting drops the hyperbolic sine to the exponential.

## transmission against barrier height

At fixed width $L$ and fixed energy $E$, the height $V_0$ acts only through the deficit $V_0 - E$: raising the barrier widens the deficit, which raises $\kappa = \sqrt{2m(V_0 - E)}/\hbar$, and the transmission falls. The fall is weaker than the width's: $V_0$ enters through the square root inside $\kappa$, while $L$ enters the exponent directly. Lowering the barrier towards the particle's energy reverses the trend: the deficit $V_0 - E$ shrinks, $\kappa$ collapses, and $T$ climbs, but never reaches one. At $V_0 = E$ the barrier still has width $L$, and reflections off its two boundaries hold $T$ below one: it settles on the finite limit $T = \left[1 + \frac{m V_0 L^2}{2\hbar^2}\right]^{-1}$ given in [transmission against total energy](#transmission%20against%20total%20energy).

---

Flashcards for this section are as follows:

- at fixed width $L$ and energy $E$, what raising the barrier height $V_0$ does to the transmission probability ::@:: It lowers $T$: the deficit $V_0 - E$ grows, $\kappa = \sqrt{2m(V_0 - E)}/\hbar$ grows with it, and the exponent $2\kappa L$ suppresses the transmission.
- whether $T$ is more sensitive to the barrier height $V_0$ or the barrier width $L$, and why ::@:: The width: $L$ sits directly in the exponent $2\kappa L$ while the height enters only through the square root inside $\kappa = \sqrt{2m(V_0 - E)}/\hbar$.
- the transmission probability as the barrier height $V_0$ drops towards the electron's energy $E$ ::@:: It climbs steeply but stops short of one: the deficit $V_0 - E$ collapses and the exponential dies, yet a barrier at the electron's own height still reflects part of the wave.

## transmission against total energy

At fixed height $V_0$ and fixed width $L$, raising the total energy $E$ shrinks the same deficit $V_0 - E$ that raising $V_0$ widened. The exponent $2\kappa L$ collapses with it and $T$ climbs steeply. As $E \to V_0$ from below, the exponential dies and $T$ tends to a finite value. Two substitutions do the work. First, $\kappa \to 0$ turns $\sinh(\kappa L)$ into $\kappa L$, so the bracket's second term reads $\frac{V_0^2\kappa^2L^2}{4E(V_0-E)}$. Second, $\kappa^2 = 2m(V_0-E)/\hbar^2$ goes in: $\kappa^2$ vanishes like the denominator does, and its factor $V_0 - E$ cancels the $V_0 - E$ already standing there, resolving what looks like $0/0$. Written out, $\frac{V_0^2\kappa^2L^2}{4E(V_0-E)} = \frac{V_0^2L^2}{4E(V_0-E)} \cdot \frac{2m(V_0-E)}{\hbar^2} = \frac{mV_0^2L^2}{2E\hbar^2}$, with the two deficits gone. Setting $E = V_0$ then turns $V_0^2/E$ into $V_0$, and the transmission is $T = \left[1 + \frac{m V_0 L^2}{2\hbar^2}\right]^{-1}$. That size term counts the barrier width in reduced wavelengths $\bar{\lambda} = \hbar/\sqrt{2mV_0}$ at the barrier height, $\frac{1}{2}(L/\bar{\lambda})^2$: a barrier several wavelengths across still reflects part of the wave even at its own height. Only a barrier well below $\hbar^2/(mL^2)$ passes essentially everything.

---

Flashcards for this section are as follows:

- at fixed barrier height $V_0$ and width $L$, how raising the total energy $E$ below the barrier top changes $T$ ::@:: $T$ rises steeply, since the deficit $V_0 - E$ shrinks, the exponent $2\kappa L$ collapses, and the exponential suppression dies away.
- the transmission probability in the limit $E \to V_0$ from below, at barrier height $V_0$ and width $L$ ::@:: $T = \left[1 + \frac{m V_0 L^2}{2\hbar^2}\right]^{-1}$: no exponential suppression remains, and only the barrier's size sets the fraction.
- how the limit $T = \left[1 + \frac{m V_0 L^2}{2\hbar^2}\right]^{-1}$ follows from the exact expression ::@:: Let $\kappa \to 0$, so $\sinh(\kappa L) \to \kappa L$ and the second term reads $\frac{V_0^2\kappa^2L^2}{4E(V_0-E)}$; then $\kappa^2 = 2m(V_0-E)/\hbar^2$ cancels the $V_0 - E$ in the denominator and leaves $\frac{mV_0^2L^2}{2E\hbar^2}$, which at $E = V_0$ is $\frac{mV_0L^2}{2\hbar^2}$.
- why the $E \to V_0$ limit of the bracket's second term stays finite ::@:: The numerator's $\kappa^2 = 2m(V_0-E)/\hbar^2$ vanishes exactly like the denominator's $V_0 - E$: the two deficits cancel, so the apparent $0/0$ resolves into $\frac{mV_0^2L^2}{2E\hbar^2}$ instead of diverging.
- what the size term $\frac{mV_0L^2}{2\hbar^2}$ counts ::@:: The barrier width in reduced wavelengths at the barrier height, $\frac{1}{2}(L/\bar{\lambda})^2$ with $\bar{\lambda} = \hbar/\sqrt{2mV_0}$: a barrier several wavelengths wide still reflects.

## the three sweeps as one formula

All three sweeps are read off one formula, $T \approx 16\frac{E}{V_0}\left(1 - \frac{E}{V_0}\right)e^{-2\kappa L}$, and the split of its variables explains the trends. Inside the exponent, $V_0$ and $E$ enter only through their difference $V_0 - E$, so a taller barrier and a lower energy suppress $T$ in the same way. In the prefactor, $V_0$ and $E$ enter only through the ratio $E/V_0$. The width $L$ enters only through the exponent $2\kappa L = L/(1/2\kappa)$, which counts barrier widths in units of the probability's decay length: each extra unit costs one factor $e$ in $T$.

---

Flashcards for this section are as follows:

- the thick-barrier transmission probability of a rectangular barrier in terms of $V_0$, $L$, and $E$ ::@:: $T \approx 16\frac{E}{V_0}\left(1 - \frac{E}{V_0}\right)e^{-2\kappa L}$ with $\kappa = \sqrt{2m(V_0 - E)}/\hbar$.
- where the exponent and the prefactor of the thick-barrier formula get their $V_0$ and $E$ ::@:: The exponent $2\kappa L$ takes them only through the difference $V_0 - E$ inside $\kappa = \sqrt{2m(V_0 - E)}/\hbar$; the prefactor $16(E/V_0)(1 - E/V_0)$ takes them only through the ratio $E/V_0$.
- the unit the exponent $2\kappa L$ counts ::@:: The probability's decay length $1/(2\kappa)$: the exponent is $L/(1/2\kappa)$, the number of those units the barrier spans, and each unit costs one factor $e$ in $T$.
