---
aliases:
  - quantum tunneling
  - quantum tunnelling
  - tunnel effect
  - tunnelling
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/quantum_tunnelling
  - language/in/English
---

# quantum tunnelling

Quantum tunnelling is the escape of a particle through a barrier it lacks the energy to surmount. Classically the particle reflects; quantum mechanically its wave function decays exponentially inside the barrier yet emerges nonzero on the far side, so a small but finite transmission probability remains. The effect is routine at atomic scales and unobservable for everyday objects, because the probability depends exponentially on barrier width and particle mass. A scanning tunnelling microscope leans on that sensitivity: it holds a sharp tip a nanometre above a conducting surface and reads the tunnelling current as a measure of distance. The instrument is described in [scanning probe microscopes](scanning%20probe%20microscopes.md).

---

Flashcards for this section are as follows:

- overview: what quantum tunnelling is for a barrier with $E < V_0$ ::@:: The transmission of a particle through a barrier with $E < V_0$, possible because its wave function decays exponentially inside the barrier yet stays nonzero on the far side. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the classical verdict on a barrier with $E < V_0$ ::@:: Total reflection — the particle never crosses; tunnelling is the quantum correction to that verdict. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## wave function inside the barrier

For a rectangular barrier of height $V_0$ and width $L$, region II ($0 < x < L$) carries $V = V_0$, so the time-independent Schrödinger equation reads $-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V_0\psi = E\psi$ there and rearranges to $\frac{d^2\psi}{dx^2} = \frac{2m(V_0 - E)}{\hbar^2}\psi$. A trial exponential $\psi = e^{\lambda x}$ satisfies that equation only when $\lambda^2 = 2m(V_0 - E)/\hbar^2$, so $\lambda = \pm\kappa$ with $\kappa = \sqrt{2m(V_0 - E)}/\hbar$, and the general solution is $\psi_{\mathrm{II}} = Ce^{\kappa x} + De^{-\kappa x}$: for $E < V_0$ these are decaying and growing exponentials rather than the oscillations of an allowed region. Outside, in regions I and III, $\psi$ is sinusoidal again. The wave function is thus exponentially damped, not killed, inside a classically forbidden region, the same leakage that binds states in the [finite potential well](finite%20potential%20well.md), now carrying flux from one side to the other.

The uncertainty principle explains why the barrier leaks at all. Across the interval $\Delta x = 1/\kappa$, where the density has already fallen to $e^{-2}$, the momentum spread is $\Delta p \gtrsim \hbar\kappa$. The kinetic energy the particle may carry there, $(\Delta p)^2/2m$, then reaches $(\hbar\kappa)^2/2m = V_0 - E$, exactly the deficit the barrier represents.

---

Flashcards for this section are as follows:

- the decay constant $\kappa$ inside a barrier ::@:: $\kappa = \sqrt{2m(V_0 - E)}/\hbar$, with $\psi_{\mathrm{II}} = Ce^{\kappa x} + De^{-\kappa x}$ — exponential, not oscillatory, for $E < V_0$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- how tunnelling and finite-well binding share the decay constant $\sqrt{2m(V_0-E)}/\hbar$ ::@:: Both are exponential decay in a classically forbidden region with decay constant set by $\sqrt{2m(V_0-E)}/\hbar$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the rearranged form of $-\frac{\hbar^2}{2m}\psi'' + V_0\psi = E\psi$ inside a barrier ::@:: Inside the barrier, where $V = V_0$, the equation rearranges to $\psi'' = 2m(V_0 - E)\psi/\hbar^2$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what the trial $\psi = e^{\lambda x}$ requires inside a barrier ::@:: Substitution into $\psi'' = 2m(V_0 - E)\psi/\hbar^2$ forces $\lambda^2 = 2m(V_0 - E)/\hbar^2$, giving $\lambda = \pm\kappa$ with $\kappa = \sqrt{2m(V_0 - E)}/\hbar$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the minimum kinetic energy the uncertainty principle allows inside a barrier, at $\Delta x = 1/\kappa$ ::@:: With the particle confined to $\Delta x = 1/\kappa$ the spread is $\Delta p \gtrsim \hbar\kappa$, so $K_{\min} = (\hbar\kappa)^2/2m = V_0 - E$, the energy deficit the barrier represents. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## transmission probability

Take a rectangular barrier of height $V_0$ and width $L$. The potential is zero for $x < 0$, jumps to $V_0$ across the barrier $0 < x < L$, and drops back to zero for $x > L$. A particle arrives from the left with energy $E < V_0$. Region I is the approach side, where the particle moves freely. There the particle both travels toward the barrier and gets reflected off it. Region II is the classically forbidden interior of the barrier. The particle's energy lies below the barrier height there, so no real oscillation is possible and only exponential decay or growth can appear. Region III is the far side, free again at the same potential as region I. Nothing travels back from region III, because no wave is incident from the right. Only the transmitted wave remains there.

Three regions carry three wave functions. For $x < 0$ the wave is incident plus reflected, $\psi_{\mathrm I} = e^{ikx} + re^{-ikx}$, with $k = \sqrt{2mE}/\hbar$. For $0 < x < L$ the wave is the decaying and growing pair from the [wave function inside the barrier](#wave%20function%20inside%20the%20barrier) section, $\psi_{\mathrm{II}} = Ae^{-\kappa x} + Be^{\kappa x}$, with $\kappa = \sqrt{2m(V_0 - E)}/\hbar$. For $x > L$ only a transmitted wave remains, $\psi_{\mathrm{III}} = te^{ikx}$, on the same $k$ as region I because the potential is the same there.

Both $\psi$ and its slope are continuous at each barrier edge, so matching at $x = 0$ and $x = L$ produces four equations. At $x = 0$ the two conditions are $1 + r = A + B$ from $\psi$ and $ik(1 - r) = \kappa(-A + B)$ from $\psi'$. At $x = L$ the two conditions are $Ae^{-\kappa L} + Be^{\kappa L} = te^{ikL}$ from $\psi$ and $\kappa(-Ae^{-\kappa L} + Be^{\kappa L}) = ikte^{ikL}$ from $\psi'$.

Eliminating $r$, $A$, and $B$ from the four equations leaves the transmitted amplitude $t = \frac{4k\kappa e^{-ikL}}{(k + i\kappa)^2 e^{-\kappa L} - (k - i\kappa)^2 e^{\kappa L}}$.

The transmission probability is $T = |t|^2$. Regions I and III share the same potential, so the incident and transmitted waves have equal speeds and no velocity prefactor appears. Squaring $|t|^2$ leaves a difference of exponentials in the denominator, and the identity $e^{\kappa L} - e^{-\kappa L} = 2\sinh(\kappa L)$ rewrites that difference as a hyperbolic sine. That single substitution is where $\sinh$ enters, and it reduces $T$ to the closed form $T = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0 - E)}\right]^{-1}$.

For a thick or high barrier, $\kappa L \gg 1$, the hyperbolic sine grows exponentially and $T$ collapses to $T \approx 16\frac{E}{V_0}\left(1 - \frac{E}{V_0}\right)e^{-2\kappa L}$. The exponent itself needs no algebra: inside the barrier the wave decays as $e^{-\kappa x}$, so between entry and exit it shrinks by a factor $e^{-\kappa L}$, and the transmitted probability, the square of the amplitude, carries $e^{-2\kappa L}$. Everything important sits in that exponential: doubling the width $L$ squares the transmission, and heavier particles are suppressed through $\kappa \propto \sqrt{m}$. Prefactors matter little compared with $e^{-2\kappa L}$. Width suppresses tunnelling more strongly than height: in the exponent, $L$ sits directly while the height enters only through the square root in $\kappa = \sqrt{2m(V_0 - E)}/\hbar$.

---

Flashcards for this section are as follows:

- the potential shape of a rectangular barrier of height $V_0$ and width $L$, and the role of each region ::@:: The potential is zero for $x < 0$, jumps to $V_0$ across $0 < x < L$, and drops back to zero for $x > L$. Region I is the free-motion approach side, where the particle travels toward the barrier and is reflected off it. Region II is the classically forbidden interior, where $E < V_0$ rules out real oscillation and only exponential decay or growth can appear. Region III is the free-motion far side at the same potential as region I, carrying only the transmitted wave. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why region III of a rectangular barrier carries no leftward-moving reflected term ::@:: Nothing travels back from region III, because no wave is incident from the right, so only the transmitted wave moving away from the barrier remains there. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the matching condition on $\psi$ at $x = 0$ ::@:: $1 + r = A + B$, matching $\psi_{\mathrm I}$ to $\psi_{\mathrm{II}}$ at the left barrier edge. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the matching condition on $\psi'$ at $x = 0$ ::@:: $ik(1 - r) = \kappa(-A + B)$, matching $\psi'_{\mathrm I}$ to $\psi'_{\mathrm{II}}$ at the left barrier edge. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the matching condition on $\psi$ at $x = L$ ::@:: $Ae^{-\kappa L} + Be^{\kappa L} = te^{ikL}$, matching $\psi_{\mathrm{II}}$ to $\psi_{\mathrm{III}}$ at the right barrier edge. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the matching condition on $\psi'$ at $x = L$ ::@:: $\kappa(-Ae^{-\kappa L} + Be^{\kappa L}) = ikte^{ikL}$, matching $\psi'_{\mathrm{II}}$ to $\psi'_{\mathrm{III}}$ at the right barrier edge. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- where $\sinh(\kappa L)$ in the closed form for $T$ comes from ::@:: The identity $e^{\kappa L} - e^{-\kappa L} = 2\sinh(\kappa L)$ rewrites the difference of exponentials left in the denominator of $|t|^2$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the transmission probability $T$ in terms of the transmitted amplitude $t$ ::@:: $T = |t|^2$, with no velocity prefactor because the incident and transmitted waves have equal speeds in regions I and III. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the exact transmission probability $T$ of a rectangular barrier ::@:: $T = \left[1 + \frac{V_0^2 \sinh^2(\kappa L)}{4E(V_0 - E)}\right]^{-1}$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the thick-barrier approximation to $T$ when $\kappa L \gg 1$ ::@:: $T \approx 16\frac{E}{V_0}\left(1 - \frac{E}{V_0}\right)e^{-2\kappa L}$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what dominates the barrier-width dependence of $T$ ::@:: The exponential factor $e^{-2\kappa L}$ with $\kappa = \sqrt{2m(V_0-E)}/\hbar$ — doubling $L$ squares the suppression. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the factor by which the tunnelling amplitude shrinks crossing a barrier of width $L$ ::@:: The wave decays as $e^{-\kappa x}$ inside the barrier, so entry to exit multiplies the amplitude by $e^{-\kappa L}$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why the transmitted probability carries $e^{-2\kappa L}$ rather than $e^{-\kappa L}$ ::@:: Probability is the amplitude squared, so the amplitude factor $e^{-\kappa L}$ becomes the probability factor $e^{-2\kappa L}$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- whether barrier width or barrier height suppresses tunnelling through $e^{-2\kappa L}$ more strongly, and why ::@:: Width: $L$ sits in $e^{-2\kappa L}$ directly while the height enters only through $\kappa \propto \sqrt{V_0 - E}$, so widening the barrier suppresses $T$ faster than raising it. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## energy above the barrier

With $E > V_0$ nothing is forbidden: the wave number inside, $k_{\mathrm{II}} = \sqrt{2m(E - V_0)}/\hbar$, is real, so the wave function oscillates through the barrier instead of decaying. The incoming wave $Ae^{ik_{\mathrm I}x}$ partly reflects as $Be^{-ik_{\mathrm I}x}$ and partly crosses the barrier to emerge as $Fe^{ik_{\mathrm I}x}$ on the far side; region III carries no leftward wave because nothing is incident from the right. The two probabilities are $R = |B|^2/|A|^2$ and $T = |F|^2/|A|^2$, and every particle is either reflected or transmitted, so $R + T = 1$.

Matching $\psi$ and its slope at both edges gives the transmission probability $T = \left[1 + \frac{V_0^2\sin^2(k_{\mathrm{II}}L)}{4E(E - V_0)}\right]^{-1}$, and perfect transmission occurs only at $k_{\mathrm{II}}L = n\pi$, where the round trip $2L$ is a whole number of interior wavelengths, $2L = n\lambda_{\mathrm{II}}$. The piece reflected off the far edge then comes back to cancel the piece reflected at the near edge, and nothing is reflected at all.

Classical mechanics allows no reflection for $E > V_0$ and total reflection for $E < V_0$. Quantum mechanics gives almost total transmission for $E \gg V_0$ and almost complete reflection for $E \ll V_0$, and where $E$ is comparable to $V_0$ the reflection oscillates with energy in a way no classical account predicts.

---

Flashcards for this section are as follows:

- the wave number of a particle with $E > V_0$ inside a barrier of height $V_0$ ::@:: $k_{\mathrm{II}} = \sqrt{2m(E - V_0)}/\hbar$, a real number, so the wave function oscillates through the barrier instead of decaying. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the constraint on the reflection and transmission probabilities $R = |B|^2/|A|^2$ and $T = |F|^2/|A|^2$ of a rectangular barrier ::@:: $R + T = 1$, because every particle is either reflected or transmitted. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the transmission probability through a barrier of height $V_0$ and width $L$ when $E > V_0$ ::@:: $T = \left[1 + \frac{V_0^2\sin^2(k_{\mathrm{II}}L)}{4E(E - V_0)}\right]^{-1}$ with $k_{\mathrm{II}} = \sqrt{2m(E - V_0)}/\hbar$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- when a barrier of height $V_0$ and width $L$ transmits perfectly ::@:: At $k_{\mathrm{II}}L = n\pi$, where the round trip $2L = n\lambda_{\mathrm{II}}$: the far-edge reflection returns to cancel the near-edge one, so $R = 0$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the classical and quantum verdicts at a barrier for $E \gg V_0$ and $E \ll V_0$ ::@:: Classically, no reflection for $E > V_0$ and total reflection for $E < V_0$; quantum mechanically, near-total transmission for $E \gg V_0$, near-total reflection for $E \ll V_0$, and oscillating reflection where $E \sim V_0$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## resonant transmission through a well

Turn the barrier into a well, $V = -V_0$ across $0 < x < L$ and zero outside, and a particle with $E > 0$ is accelerated through the region instead of held out of it. Reflection still occurs at each edge, and the wavelength inside the well is shorter than outside. When the width holds a whole or half number of those interior wavelengths, the wave reflected at the far edge returns out of step with the incident wave and the reflections cancel, so transmission runs almost pure; at other widths the reflections reinforce and almost the whole wave comes back.

---

Flashcards for this section are as follows:

- what makes a potential well of width $L$ almost transparent at particular wavelengths ::@:: The wavelength inside is shorter than outside; when $L$ holds a whole or half number of interior wavelengths the far-edge reflection returns out of step with the near-edge one, the reflections cancel, and $T$ approaches 1. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## macroscopic and microscopic estimates

The exponential is ruthless. A 500 kg lion facing a half-metre barrier has $V_0 = mgH$ at five metres and $E = mgh$ at three metres, so the height difference is $H - h = 2\ \mathrm{m}$. The barrier exceeds the lion's energy by $$V_0 - E = mg(H - h) = 500\ \mathrm{kg} \times 9.8\ \mathrm{m/s^2} \times 2\ \mathrm{m} \approx 10^4\ \mathrm{J}.$$ The decay constant inside the barrier follows as $$\kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar} \approx \frac{\sqrt{2 \times 500 \times 10^4}}{1.055 \times 10^{-34}} \approx 3 \times 10^{37}\ \mathrm{m^{-1}}.$$ With $L = 0.5\ \mathrm{m}$ the exponent reaches $\kappa L \approx 1.5 \times 10^{37}$, and $e^{-2\kappa L}$ underflows any scale, so $T$ rounds to zero in any finite decimal representation. Zoos need no tunnelling insurance.

Replace the lion by an electron, $m \approx 10^{-30}$ kg, with $E = 1$ eV and $V_0 = 5$ eV, so the barrier exceeds the electron's energy by $$V_0 - E = 4\ \mathrm{eV} \approx 6.4 \times 10^{-19}\ \mathrm{J}.$$ The decay constant is then $$\kappa = \frac{\sqrt{2 \times 10^{-30} \times 6.4 \times 10^{-19}}}{1.055 \times 10^{-34}} \approx 1.1 \times 10^{10}\ \mathrm{m^{-1}}.$$ A barrier of $L = 1\ \mathrm{nm}$ gives $\kappa L \approx 11$, so $e^{-2\kappa L} \approx 10^{-10}$, and with the prefactor $16(E/V_0)(1 - E/V_0) \approx 3$ the transmission sits near $10^{-9}$, small but measurable. The same mass scaling that makes tunnelling invisible in a lion's world makes it unavoidable in an atom's.

---

Flashcards for this section are as follows:

- the chain that gives $\kappa \approx 3 \times 10^{37}\ \mathrm{m^{-1}}$ inside a lion's barrier ::@:: $V_0 = mgH$ at $H = 5$ m and $E = mgh$ at $h = 3$ m give $V_0 - E = mg(H - h) = 500\ \mathrm{kg} \times 9.8\ \mathrm{m/s^2} \times 2\ \mathrm{m} \approx 10^4\ \mathrm{J}$. Then $\kappa = \sqrt{2m(V_0 - E)}/\hbar \approx \sqrt{2 \times 500 \times 10^4}/(1.055 \times 10^{-34}) \approx 3 \times 10^{37}\ \mathrm{m^{-1}}$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the chain that gives $T \sim 10^{-9}$ for an electron on a one-nanometre barrier ::@:: $V_0 - E = 4\ \mathrm{eV} \approx 6.4 \times 10^{-19}\ \mathrm{J}$, $\kappa \approx \sqrt{2 \times 10^{-30} \times 6.4 \times 10^{-19}}/(1.055 \times 10^{-34}) \approx 1.1 \times 10^{10}\ \mathrm{m^{-1}}$, $L = 1\ \mathrm{nm}$ gives $\kappa L \approx 11$ and $e^{-2\kappa L} \approx 10^{-10}$, and the prefactor $16(E/V_0)(1 - E/V_0) \approx 3$ lifts the transmission to near $10^{-9}$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why a lion cannot tunnel, given $\kappa \propto \sqrt{m}$ and $T \propto e^{-2\kappa L}$ ::@:: $\kappa$ grows as $\sqrt{m}$, so for a 500 kg mass and a half-metre barrier the exponent $2\kappa L$ is of order $10^{38}$ and $e^{-2\kappa L}$ is effectively zero. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why an electron with $m \approx 10^{-30}$ kg crosses a nanometre barrier readily ::@:: With $m \approx 10^{-30}$ kg and $L \approx 1$ nm, $\kappa L$ stays small enough that $T$ remains appreciable. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## alpha decay

A heavy nucleus holds an alpha particle in a square well and walls it in with a Coulomb barrier. Inside the nuclear radius $r_N$ the strong force dominates the Coulomb repulsion; outside, the Coulomb energy climbs as $1/r$ to a peak several times the alpha particle's few MeV of kinetic energy, so classically no path leads out. Quantum mechanics opens a path: the alpha's wave function decays through the barrier and emerges nonzero on the far side.

The rates carry the barrier's sensitivity. Many nuclei heavier than lead emit alpha particles at rates spanning a factor of $10^{13}$ while their emitted energies cluster between 4 and 8 MeV. The escape probability $T \propto e^{-2\kappa L}$ turns small nucleus-to-nucleus differences in barrier height and width into huge differences in rate.

A 4.2 MeV alpha in uranium-238 faces a Coulomb energy of 38 MeV at $r_N = 7$ fm, and its own energy matches the Coulomb potential at 63 fm, so it must cross about 56 fm of barrier. A square top at the full 38 MeV height gives $T \approx 4 \times 10^{-121}$; halving both the height and the width to follow the true curved barrier more closely gives $T \approx 1.5 \times 10^{-41}$. The alpha crosses the nucleus in about $10^{-21}$ s, so it strikes the barrier $10^{21}$ times a second, and at $T \approx 10^{-41}$ it escapes after roughly $10^{20}$ s. The measured half-life of uranium-238 is $4.5 \times 10^9$ years, about $10^{17}$ s, so a crude square barrier lands within a few orders of magnitude of it.

---

Flashcards for this section are as follows:

- what traps an alpha particle of energy $E_\alpha \approx 5$ MeV inside a heavy nucleus classically ::@:: Outside $r_N$ the repulsive Coulomb energy rises to several times $E_\alpha$ while the strong force holds it in, so the alpha never has the energy to climb over. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why alpha emission rates span $10^{13}$ while the emitted energies span only 4–8 MeV ::@:: The escape rate follows $T \propto e^{-2\kappa L}$, so small nucleus-to-nucleus differences in barrier height and width move the rate by orders of magnitude. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the barrier a 4.2 MeV alpha in uranium-238 must cross, with nuclear radius $r_N = 7$ fm ::@:: The Coulomb energy at $r_N = 7$ fm is 38 MeV and the alpha's energy matches it at 63 fm, so the barrier runs from 7 fm to 63 fm, about 56 fm wide under a 38 MeV peak. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- how a transmission probability near $10^{-41}$ gives a billion-year half-life ::@:: The alpha crosses the nucleus in $10^{-21}$ s, making $10^{21}$ attempts a second, so it escapes in about $10^{20}$ s against the measured $4.5 \times 10^9$ year (about $10^{17}$ s) half-life of uranium-238. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## tunnel diode

Tunnelling also carries current in a tunnel diode, a semiconductor junction only about 10 nm wide. A bias voltage adjusts the junction barrier and lets electrons tunnel through it in either direction. An ordinary junction depends on electrons and holes diffusing across it, a slow process; a tunnel diode's carriers cross by tunnelling instead, and the bias itself can be varied rapidly, so the device switches extremely fast. Leo Esaki discovered it in 1957; it went into switching circuits and high-frequency oscillators, and today it serves mainly in space electronics, valued for its longevity and resistance to radiation.

---

Flashcards for this section are as follows:

- why a tunnel diode switches faster than an ordinary semiconductor junction ::@:: Its carriers cross the roughly 10 nm barrier by tunnelling, while an ordinary junction depends on the slower diffusion of electrons and holes across it. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
