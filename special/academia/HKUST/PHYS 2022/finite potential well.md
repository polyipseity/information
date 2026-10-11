---
aliases:
  - finite potential well
  - finite square well
  - finite square-well potential
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/finite_potential_well
  - language/in/English
---

# finite potential well

The finite square well is the [particle in a box](particle%20in%20a%20box.md) with impenetrable walls lowered to a depth $V_0$. A particle with $E < V_0$ is still bound: its wave function decays exponentially into both walls instead of vanishing at them, its levels sit below the infinite-well values, and only finitely many levels fit under the top of the well.

---

Flashcards for this section are as follows:

- overview: how the finite well with depth $V_0$ differs from the infinite one ::@:: The walls have depth $V_0$ instead of infinity, so the wave function leaks into the walls with decay constant $\alpha = \sqrt{2m(V_0-E)}/\hbar$, every level drops below its infinite-well value, and only finitely many bound states exist.

## three regions

Split the line into region I ($x < 0$, $V = V_0$), region II ($0 < x < L$, $V = 0$), and region III ($x > L$, $V = V_0$). In regions I and III the potential is $V_0$, so the Schrödinger equation $-\frac{\hbar^2}{2m}\psi'' + V_0\psi = E\psi$ rearranges to $\frac{d^2\psi}{dx^2} = \frac{2m(V_0 - E)}{\hbar^2}\psi$; the trial $\psi = e^{\lambda x}$ then requires $\lambda^2 = 2m(V_0 - E)/\hbar^2$, so $\lambda = \pm\alpha$ with $\alpha = \sqrt{2m(V_0 - E)}/\hbar$. The bounded solutions are then $\psi_{\mathrm{I}} = Ae^{\alpha x}$ and $\psi_{\mathrm{III}} = Be^{-\alpha x}$, exponentials that decay away from the well. In region II the equation is the free-particle one, $\frac{d^2\psi}{dx^2} = -k^2\psi$ with $k = \sqrt{2mE}/\hbar$, whose solutions oscillate: $\psi_{\mathrm{II}} = Ce^{ikx} + De^{-ikx}$. The particle therefore has a nonzero probability of being found outside a well it cannot classically escape.

---

Flashcards for this section are as follows:

- the decay constant $\alpha$ outside a finite well of depth $V_0$ ::@:: $\alpha = \sqrt{2m(V_0 - E)}/\hbar$, with $\psi_{\mathrm{I}} = Ae^{\alpha x}$ and $\psi_{\mathrm{III}} = Be^{-\alpha x}$ decaying away from the well.
- the wave number $k$ inside the finite well ::@:: $k = \sqrt{2mE}/\hbar$, with $\psi_{\mathrm{II}} = Ce^{ikx} + De^{-ikx}$ oscillating in region II.
- the rearranged form of $-\frac{\hbar^2}{2m}\psi'' + V_0\psi = E\psi$ in the wall regions of a finite well ::@:: There $V = V_0$, so the equation rearranges to $\psi'' = 2m(V_0 - E)\psi/\hbar^2$.
- what the trial $\psi = e^{\lambda x}$ requires in the wall regions of a finite well ::@:: Substitution into $\psi'' = 2m(V_0 - E)\psi/\hbar^2$ forces $\lambda^2 = 2m(V_0 - E)/\hbar^2$, giving $\lambda = \pm\alpha$ with $\alpha = \sqrt{2m(V_0 - E)}/\hbar$.

## boundary matching

The wave function and its slope must both be continuous where the regions meet, at $x = 0$ and $x = L$, because neither $V$ nor the Schrödinger equation there is singular. The equation $-(\hbar^2/2m)\psi'' = (E - V)\psi$ ties the curvature of $\psi$ to the force, so a kink in $\psi'$ would mean a delta-function force at the wall. Continuity of $\psi'$ therefore encodes a finite force there. The infinite well breaks this rule: its wall forces $\psi$ to zero across zero width, so $\psi'$ jumps there. The slope discontinuity is the mathematical trace of an infinitely repulsive force, and $V = \infty$ is an idealisation of a very steep finite wall rather than a physical potential. Matching $\psi_{\mathrm{I}} = \psi_{\mathrm{II}}$ and $\psi'_{\mathrm{I}} = \psi'_{\mathrm{II}}$ at $x = 0$, and $\psi_{\mathrm{II}} = \psi_{\mathrm{III}}$ and $\psi'_{\mathrm{II}} = \psi'_{\mathrm{III}}$ at $x = L$, ties $A$, $B$, $C$, and $D$ together and quantises $E$, though now through transcendental equations with no closed-form solution, solved graphically or numerically. The interior form $\psi_{\mathrm{II}} = Ce^{ikx} + De^{-ikx}$ can be rewritten with Euler's formula, $e^{\pm ikx} = \cos kx \pm i\sin kx$, as cosine and sine terms. For a symmetric well the real parity-adapted basis $C\cos kx$ and $D\sin kx$ is the easier one because each class solves the boundary conditions separately. The parity classification behind that sorting rests on the well's symmetry: mirroring $x$ to $L - x$ leaves the potential unchanged, so any solution has a mirrored partner and the independent solutions can be chosen even or odd about the centre. The matching then sorts the states by that symmetry: the even solutions are cosine-like inside with symmetric tails, the odd ones are sine-like with antisymmetric tails, and they interleave in energy exactly as the infinite-well levels do.

---

Flashcards for this section are as follows:

- what must be continuous at each wall: $\psi$ or $d\psi/dx$? ::@:: Both $\psi$ and $d\psi/dx$ at $x = 0$ and $x = L$, since the potential there is finite.
- what the matching conditions $\psi_{\mathrm{I}} = \psi_{\mathrm{II}}$ and $\psi'_{\mathrm{I}} = \psi'_{\mathrm{II}}$ give ::@:: From transcendental equations set by matching $\psi$ and $\psi'$ at both walls — no closed form, solved graphically or numerically.
- how finite-well states are organised ::@:: By parity about the well's centre: even (cosine-like) and odd (sinusoidal) solutions interleave in energy.
- why the bound states of a finite well of width $L$ fall into even and odd classes ::@:: The well is symmetric under $x \to L - x$, so mirroring leaves the potential unchanged and the solutions can be chosen symmetric (even) or antisymmetric (odd).
- Euler's formula connecting $e^{\pm ikx}$ to the trigonometric functions ::@:: $e^{\pm ikx} = \cos kx \pm i\sin kx$.
- what Euler's formula $e^{\pm ikx} = \cos kx \pm i\sin kx$ does for the interior solution $\psi_{\mathrm{II}} = Ce^{ikx} + De^{-ikx}$ ::@:: It rewrites $\psi_{\mathrm{II}}$ as cosine and sine terms.
- why the real parity basis $C\cos kx$ and $D\sin kx$ is the easier interior basis for a symmetric well ::@:: Each parity class solves the boundary conditions separately, so the even and odd states can be matched on their own.
- why $\psi'$ must be continuous at a finite step, and what a kink would mean ::@:: The equation $-(\hbar^2/2m)\psi'' = (E - V)\psi$ ties the curvature of $\psi$ to the force, so a kink in $\psi'$ would mean a delta-function force at the wall; continuity of $\psi'$ encodes a finite force there.

## penetration depth

The penetration depth $\delta = 1/\alpha = \hbar/\sqrt{2m(V_0 - E)}$ is the e-folding length of the amplitude: $\psi \sim e^{-x/\delta}$ falls by a factor $e$ over one $\delta$. The probability density falls twice as fast, $|\psi|^2 \sim e^{-2x/\delta}$, so its e-folding length is $\delta/2$. The two lengths must not be confused. $\delta$ scales directly with $\hbar$, a purely quantum length, zero in the classical limit, and shrinks for heavier particles and for levels lying deeper below the top of the well. A level near the top, $E \to V_0$, has $\alpha \to 0$ and $\delta \to \infty$: it is barely bound and spreads far into the walls. The uncertainty principle accounts for the same scale: staying in the wall needs an energy allowance of order $V_0 - E$, and $\Delta E\,\Delta t \geq \hbar/2$ grants it only for a time of order $\hbar/(V_0 - E)$.

---

Flashcards for this section are as follows:

- what the penetration depth $\delta = 1/\alpha$ of a finite well is ::@:: $\delta = \hbar/\sqrt{2m(V_0 - E)} = 1/\alpha$ is the e-folding length of the amplitude: $\psi \sim e^{-x/\delta}$ falls by a factor $e$ over one $\delta$.
- what the e-folding length of the probability density $|\psi|^2$ outside a finite well is ::@:: $\delta/2$, where $\delta = 1/\alpha$: $|\psi|^2 \sim e^{-2x/\delta}$ falls twice as fast as the amplitude $\psi \sim e^{-x/\delta}$.
- how $\delta$ varies with particle mass and level depth ::@:: Heavier mass or deeper level (larger $V_0 - E$) shrinks $\delta$; a level near the top of the well, $E \to V_0$, has $\delta \to \infty$.

## bound states

Only finitely many levels fit below $V_0$, and the count grows with two knobs. Deepening the well at fixed width adds states. As $V_0 \to \infty$ the finite well becomes the infinite one with its infinite tower of levels. Increasing the particle's mass at fixed $V_0$ and width also adds states, because $\alpha$ grows and the tails shrink, letting shorter wavelengths fit. The levels also sit below the infinite-well ladder: a wave function that decays past both walls spans more than $L$, so its standing wave is longer than $\lambda_n = 2L/n$, its wave number is smaller, and $E = \hbar^2k^2/2m$ drops accordingly. Inside, the bound wave functions keep the infinite-well shapes, the ground state nodeless and centred, each excited state adding a node, merely rounded off at the walls by their exponential skirts. Past the top of the well, $E \geq V_0$, the particle is no longer bound, and [reflection and transmission take over](quantum%20tunnelling.md#energy%20above%20the%20barrier).

---

Flashcards for this section are as follows:

- what adds bound states to a finite well: deeper $V_0$ or larger mass $m$? ::@:: A deeper $V_0$, or a heavier particle at fixed $V_0$ and width; both shrink the penetration depth $\delta$.
- what the bound states look like compared with infinite-well states ::@:: The same node-counting shapes — ground state nodeless, each level adding a node — rounded at the walls by exponential tails.
- why finite-well levels sit below the infinite-well ladder $E_n = n^2h^2/(8mL^2)$ ::@:: The wave function reaches past both walls, so the standing wave spans more than $L$: longer $\lambda$, smaller $k$, and a lower $E = \hbar^2k^2/2m$.
