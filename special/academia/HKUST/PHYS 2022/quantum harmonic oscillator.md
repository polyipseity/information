---
aliases:
  - harmonic oscillator
  - quantum SHO
  - quantum harmonic oscillator
  - simple harmonic oscillator
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/quantum_harmonic_oscillator
  - language/in/English
---

# quantum harmonic oscillator

The quantum harmonic oscillator is the quantum version of any system with a restoring force, springs, diatomic molecules, atoms vibrating in a lattice. Expanding any smooth potential about its minimum leaves a parabola, $V(x) = \tfrac{1}{2}kx^2$, and the Schrödinger equation for that parabola has solutions at the discrete energies $E_n = (n + \tfrac{1}{2})\hbar\omega$ for $n = 0, 1, 2, \ldots$, with $\omega = \sqrt{k/m}$. The lowest level, $E_0 = \tfrac{1}{2}\hbar\omega$, is nonzero: the oscillator never rests.

---

Flashcards for this section are as follows:

- overview: what the quantum harmonic oscillator is, and its levels $E_n$ ::@:: The quantum theory of any system with a restoring force, $V = \tfrac{1}{2}kx^2$ near its minimum, with levels $E_n = (n + \tfrac{1}{2})\hbar\omega$ and $\omega = \sqrt{k/m}$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the zero-point energy $E_0$ of the oscillator ::@:: $E_0 = \tfrac{1}{2}\hbar\omega$ — the $n = 0$ level, nonzero because confinement forbids rest. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## why every potential looks parabolic near its minimum

Any potential can be Taylor-expanded about an equilibrium point $x_0$: $V(x) = V_0 + V_1(x - x_0) + \tfrac{1}{2}V_2(x - x_0)^2 + \cdots$. At a minimum the slope vanishes, $V_1 = 0$, so near $x_0$ the parabolic term dominates and $V(x) \approx V_0 + \tfrac{1}{2}k(x - x_0)^2$ with $k = V_2$. Shifting the origin so the minimum sits at zero potential, $V(x) = \tfrac{1}{2}kx^2$, the oscillator problem is universal: every stable equilibrium, at every energy low enough to stay near the bottom, behaves this way.

---

Flashcards for this section are as follows:

- why a generic potential $V$ reduces to the harmonic oscillator near equilibrium ::@:: The Taylor expansion about the minimum has no linear term, so the parabolic term $\tfrac{1}{2}k(x-x_0)^2$ dominates at small displacements. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- when the parabolic approximation to a potential $V$ breaks down ::@:: Away from the minimum, where the cubic and higher Taylor terms stop being negligible against $\tfrac{1}{2}k(x-x_0)^2$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## quantised energies and wave functions

Substituting $V = \tfrac{1}{2}kx^2$ into the time-independent Schrödinger equation and writing $\omega = \sqrt{k/m}$ gives $\frac{d^2\psi}{dx^2} + \left(\frac{2mE}{\hbar^2} - \frac{m^2\omega^2}{\hbar^2}x^2\right)\psi = 0$. Rescaling to $\xi = \sqrt{m\omega/\hbar}\,x$ and $\varepsilon = 2E/(\hbar\omega)$ turns this into $\psi'' + (\varepsilon - \xi^2)\psi = 0$, where the prime now means $d/d\xi$.

Normalisability demands $\psi \to 0$ at large $|\xi|$, so write $\psi = H(\xi)e^{-\xi^2/2}$ with a polynomial $H$ carrying everything that is not the Gaussian falloff. The derivatives are $\psi' = (H' - \xi H)e^{-\xi^2/2}$ and $\psi'' = (H'' - 2\xi H' + (\xi^2 - 1)H)e^{-\xi^2/2}$. Substituting these into $\psi'' + (\varepsilon - \xi^2)\psi = 0$ cancels the $\xi^2$ terms and leaves the Hermite equation $H'' - 2\xi H' + (\varepsilon - 1)H = 0$.

Seek the polynomial as a series $H = \sum_j h_j \xi^j$. Collecting the coefficient of $\xi^j$ in the Hermite equation gives $(j+2)(j+1)h_{j+2} + (\varepsilon - 1 - 2j)h_j = 0$, the two-term recurrence $h_{j+2} = (2j + 1 - \varepsilon)h_j / ((j+1)(j+2))$. Each even or odd chain of coefficients is fixed by its first entry.

Termination at order $n$ needs $h_{n+2} = 0$ with $h_n \neq 0$, which forces $\varepsilon = 2n + 1$ and hence $E_n = (n + \tfrac{1}{2})\hbar\omega$. The energies fall out of the normalisability requirement alone. No differential equation needs solving.

Any other $\varepsilon$ leaves $h_{j+2}/h_j$ tending to $1$ at large $j$, so $H$ grows like $e^{+\xi^2}$ and $\psi = He^{-\xi^2/2}$ grows like $e^{+\xi^2/2}$. No normalisation survives.

This pattern of series plus termination producing a spectrum recurs in quantum mechanics wherever confinement is imposed by normalisability: a power series is forced to terminate, and the termination condition alone picks out the discrete energies.

The corresponding wave functions are Hermite polynomials of order $n$ times a Gaussian envelope, $\psi_n(x) = H_n(x)e^{-m\omega x^2/2\hbar}$. The ground state is a bare Gaussian, and each successive level multiplies in one more polynomial oscillation, adding one node.

---

Flashcards for this section are as follows:

- the quantisation condition $E_n(\omega)$ for the oscillator ::@:: $E_n = (n + \tfrac{1}{2})\hbar\omega$ for $n = 0, 1, 2, \ldots$ — equally spaced levels with spacing $\hbar\omega$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the shape $\psi_n(x)$ of the oscillator wave functions ::@:: Hermite polynomials $H_n$ times a Gaussian envelope, $\psi_n(x) = H_n(x)e^{-m\omega x^2/2\hbar}$, with $n$ nodes. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the derivatives of $\psi = H(\xi)e^{-\xi^2/2}$ needed in $\psi'' + (\varepsilon - \xi^2)\psi = 0$ ::@:: $\psi' = (H' - \xi H)e^{-\xi^2/2}$ and $\psi'' = (H'' - 2\xi H' + (\xi^2 - 1)H)e^{-\xi^2/2}$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the equation obeyed by $H$ after $\psi = H(\xi)e^{-\xi^2/2}$ is substituted into $\psi'' + (\varepsilon - \xi^2)\psi = 0$ ::@:: The Hermite equation, $H'' - 2\xi H' + (\varepsilon - 1)H = 0$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the recurrence for the Hermite-series coefficients $h_j$ of $H = \sum_j h_j \xi^j$ ::@:: Collecting the coefficient of $\xi^j$ in the Hermite equation $H'' - 2\xi H' + (\varepsilon - 1)H = 0$ gives $h_{j+2} = (2j + 1 - \varepsilon)h_j / ((j+1)(j+2))$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the condition that terminates the Hermite series $H = \sum_j h_j \xi^j$ at order $n$, and the level $E_n$ it forces ::@:: $h_{n+2} = 0$ with $h_n \neq 0$ forces $\varepsilon = 2n + 1$ and hence $E_n = (n + \tfrac{1}{2})\hbar\omega$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why the oscillator energies $E_n = (n + \tfrac{1}{2})\hbar\omega$ can be read off without solving the differential equation ::@:: Only a terminating Hermite series stays normalisable, and termination forces $\varepsilon = 2n + 1$, so $E_n$ falls out of the normalisability requirement alone. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why every non-terminating $\varepsilon$ fails to give a normalisable oscillator state ::@:: Any other $\varepsilon$ leaves $h_{j+2}/h_j \to 1$ at large $j$, so $H$ grows like $e^{+\xi^2}$ and $\psi = He^{-\xi^2/2}$ grows like $e^{+\xi^2/2}$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## zero-point energy and the Heisenberg limit

The ground-state energy $E_0 = \tfrac{1}{2}\hbar\omega$ is the zero-point energy, sometimes called the Heisenberg limit because the uncertainty principle demands it. It is the lowest level of the ladder $E_n = (n + \tfrac{1}{2})\hbar\omega$, and it is nonzero.

Take a state localised to a width $\Delta x$ near the bottom of the parabola. A minimum-uncertainty packet is enough. The uncertainty principle then gives $\Delta p \geq \hbar/(2\Delta x)$. For such a state $\langle p \rangle = 0$ once the packet's mean momentum is set to zero, so $\langle p^2 \rangle = (\Delta p)^2$. With $V = \tfrac{1}{2}m\omega^2x^2$ the potential term is $\langle V \rangle = \tfrac{1}{2}m\omega^2\langle x^2 \rangle$, and a packet centred at the minimum has $\langle x^2 \rangle \approx (\Delta x)^2$. The energy estimate is $E \approx (\Delta p)^2/2m + \tfrac{1}{2}m\omega^2(\Delta x)^2 \geq \hbar^2/(8m(\Delta x)^2) + \tfrac{1}{2}m\omega^2(\Delta x)^2$.

Every state of width $\Delta x$ costs at least this much energy. Minimising the bound over $\Delta x$ therefore gives a lower bound on $E_0$, not the energy of any particular state.

The bound as a function of the width is $E(\Delta x) = \hbar^2/(8m(\Delta x)^2) + \tfrac{1}{2}m\omega^2(\Delta x)^2$. Its derivative vanishes when $dE/d\Delta x = -\hbar^2/(4m(\Delta x)^3) + m\omega^2\Delta x = 0$, that is, when $\Delta x^4 = \hbar^2/(4m^2\omega^2)$. The stationary point sits at $\Delta x = \sqrt{\hbar/(2m\omega)}$.

Substituting that width back, both terms equal $\hbar\omega/4$: the confinement term is $\hbar^2/(8m\Delta x^2) = \hbar\omega/4$ at $\Delta x^2 = \hbar/(2m\omega)$, and the potential term is $\tfrac{1}{2}m\omega^2\Delta x^2 = \hbar\omega/4$. The bound's minimum is $E = \hbar\omega/2$. The true ground state saturates the bound, so the estimate is exact for it rather than approximate. That exactness is why the heuristic is trusted.

A classical oscillator can sit at rest at the bottom; a quantum one cannot. Normalising the ground state $\psi_0$ confirms the estimate directly: the integrals give $\langle x \rangle = 0$ by parity and $\langle x^2 \rangle = \hbar/(2m\omega)$ exactly, the width the uncertainty argument optimised to. Every level obeys the same virial relation, since the potential term holds half the energy: $\tfrac{1}{2}m\omega^2\langle x^2\rangle = E_n/2$, so $\langle x^2\rangle = (n + \tfrac{1}{2})\hbar/(m\omega)$, of which the ground state's value is the $n = 0$ case. Parity keeps $\langle x \rangle = 0$ on every level, so $\Delta x = \sqrt{(n + \tfrac{1}{2})\hbar/(m\omega)}$. Zero-point motion has visible consequences: the zero-point energy of liquid helium-4 is large enough to stop it freezing at atmospheric pressure however cold it gets, so it stays liquid near 0 K.

---

Flashcards for this section are as follows:

- the zero-point energy in terms of $\omega$ ::@:: $E_0 = \tfrac{1}{2}\hbar\omega$, the $n = 0$ level of the ladder $E_n = (n + \tfrac{1}{2})\hbar\omega$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what $\langle p^2 \rangle$ equals for an oscillator packet of width $\Delta x$ with $\langle p \rangle = 0$ ::@:: $\langle p^2 \rangle = (\Delta p)^2$, bounded below by the uncertainty principle as $(\Delta p)^2 \geq \hbar^2/(4(\Delta x)^2)$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the energy estimate for an oscillator state localised to width $\Delta x$ ::@:: $E \approx (\Delta p)^2/2m + \tfrac{1}{2}m\omega^2(\Delta x)^2 \geq \hbar^2/(8m(\Delta x)^2) + \tfrac{1}{2}m\omega^2(\Delta x)^2$, using $\langle p^2 \rangle = (\Delta p)^2$ and $\langle x^2 \rangle \approx (\Delta x)^2$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why minimising the zero-point estimate over $\Delta x$ bounds $E_0$ from below ::@:: Every state of width $\Delta x$ costs at least the bound's value, so the smallest bound over all widths is a lower bound on the ground-state energy. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the stationary point of the zero-point estimate $E(\Delta x) \approx \hbar^2/(8m\Delta x^2) + \tfrac{1}{2}m\omega^2\Delta x^2$ ::@:: $dE/d\Delta x = -\hbar^2/(4m\Delta x^3) + m\omega^2\Delta x = 0$ gives $\Delta x^4 = \hbar^2/(4m^2\omega^2)$, so $\Delta x = \sqrt{\hbar/(2m\omega)}$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why both terms of the zero-point estimate equal $\hbar\omega/4$ at $\Delta x = \sqrt{\hbar/(2m\omega)}$ ::@:: At $\Delta x^2 = \hbar/(2m\omega)$ the confinement term $\hbar^2/(8m\Delta x^2)$ and the potential term $\tfrac{1}{2}m\omega^2\Delta x^2$ each equal $\hbar\omega/4$, so the minimum is $E = \hbar\omega/2$ exactly. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why the zero-point estimate $E = \hbar\omega/2$ is exact for the oscillator ground state ::@:: The true ground state saturates the uncertainty bound, so the estimate's minimum is its actual energy. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the exact ground-state moments $\langle x \rangle$ and $\langle x^2 \rangle$ of the harmonic oscillator ::@:: $\langle x \rangle = 0$ by parity, and $\langle x^2 \rangle = \hbar/(2m\omega)$, the width the uncertainty estimate optimised to. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the position variance $\langle x^2 \rangle$ of oscillator level $n$ ::@:: $\langle x^2 \rangle = (n + \tfrac{1}{2})\hbar/(m\omega)$, half the level's energy over $m\omega^2$, with $\langle x \rangle = 0$ on every level. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the position spread $\Delta x$ of oscillator level $n$ ::@:: $\Delta x = \sqrt{(n + \tfrac{1}{2})\hbar/(m\omega)}$, the square root of the variance since parity keeps $\langle x \rangle = 0$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- how the zero-point energy $E_0 = \hbar\omega/2$ shows in liquid helium-4 ::@:: The zero-point energy keeps it liquid however cold it gets: helium-4 does not freeze at atmospheric pressure, even near 0 K. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## probability, classical and quantum

The ground state puts its largest probability at the centre of the well, where a classical oscillator moves fastest and spends the least time. Classically the probability is greatest at the turning points, where the mass lingers.

A classical oscillator of amplitude $A$ spends $dt = dx/v(x)$ near $x$, with $v(x) = \omega\sqrt{A^2 - x^2}$. Its probability density is therefore $p_{\mathrm{cl}}(x) = 1/(\pi\sqrt{A^2 - x^2})$. The density is largest at the turning points $\pm A$, where it diverges. The divergence is integrable, so the density still normalises.

The quantum density at large $n$ oscillates $n$ times between the turning points $x_T$. Averaged over those oscillations, its envelope is proportional to $1/\sqrt{x_T^2 - x^2}$. The averaged density diverges at $\pm x_T$ just like $p_{\mathrm{cl}}$, and the divergence is again integrable.

"Reproduces" has a precise meaning. For any smooth observable $g(x)$ that varies slowly compared with the oscillation spacing, the expectation value $\langle g \rangle$ over $\psi_n^2$ tends to the classical cycle average of $g$ as $n$ rises. The probability of finding the particle within a fixed window near a turning point, with the oscillations averaged out, grows toward the classical value the same way. The ground state is the outlier: its density still peaks at the centre, while the classical density is smallest there.

---

Flashcards for this section are as follows:

- where the quantum and classical oscillator probabilities peak ::@:: The quantum ground state peaks at the centre; the classical distribution peaks at the turning points where the mass moves slowest. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the classical probability density for an oscillator of amplitude $A$, and where it diverges ::@:: $p_{\mathrm{cl}}(x) = 1/(\pi\sqrt{A^2 - x^2})$, from $dt = dx/v(x)$ with $v(x) = \omega\sqrt{A^2 - x^2}$; it diverges integrably at the turning points $\pm A$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what the large-$n$ quantum density averages to between its turning points $x_T$ ::@:: An envelope proportional to $1/\sqrt{x_T^2 - x^2}$, diverging integrably at $\pm x_T$ just like the classical distribution. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what "the quantum density reproduces the classical distribution" means for a smooth observable $g(x)$ ::@:: Averaged over the oscillations, $\langle g \rangle$ over $\psi_n^2$ tends to the classical cycle average of $g$ as $n$ rises. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
