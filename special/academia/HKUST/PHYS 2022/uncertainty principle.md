---
aliases:
  - Heisenberg uncertainty principle
  - Heisenberg's uncertainty principle
  - indeterminacy principle
  - uncertainty principle
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/uncertainty_principle
  - language/in/English
---

# uncertainty principle

The uncertainty principle, introduced by Werner Heisenberg in 1927, sets a fundamental limit on how precisely certain pairs of physical quantities can be known at the same time. Position and momentum form the standard pair: the product of their uncertainties is bounded below, $\Delta x \cdot \Delta p_x \geq \hbar/2$, where $\hbar = h/2\pi$ is the reduced Planck constant. The limit is not a flaw of measuring instruments. It holds for quantum states themselves. The bound pairs only conjugate variables: $(x, p_x)$ and $(E, t)$ are the standard two. Angular momentum with angle $(L, \theta)$ and rotational inertia with angular velocity $(I, \omega)$ follow the same rule, and every pair's product carries the dimensions of $\hbar$. Products of non-conjugate variables need no lower bound at all: $\Delta p_z \cdot \Delta x$ can be zero.

---

Flashcards for this section are as follows:

- overview: what the uncertainty principle states for $\Delta x$ and $\Delta p_x$ ::@:: That certain pairs of physical quantities, such as position $x$ and momentum $p_x$, cannot both be known arbitrarily precisely: $\Delta x \cdot \Delta p_x \geq \hbar/2$.
- where the uncertainty limit $\Delta x \cdot \Delta p_x \geq \hbar/2$ comes from ::@:: From the quantum state itself ($\Delta x \cdot \Delta p_x \geq \hbar/2$), not from shortcomings of measuring instruments.
- other conjugate pairs beside $(x, p_x)$ and $(E, t)$, and the dimensions their products share ::@:: $(L, \theta)$ for angular momentum and angle, and $(I, \omega)$ for rotational inertia and angular velocity; each product carries the dimensions of $\hbar$.
- whether the uncertainty principle bounds $\Delta p_z \cdot \Delta x$ ::@:: No: $p_z$ and $x$ are not a conjugate pair, so $\Delta p_z \cdot \Delta x$ has no lower bound and can be zero.

## from wave packets to quantum uncertainty

A particle localised to a width $\Delta x$ is described by a wave packet built from wave numbers in a spread $\Delta k$. The Gaussian packet $\Psi(x) = A e^{-x^2/4(\Delta x)^2} e^{ik_0 x}$ shows the trade-off at its sharpest. Its density $|\Psi|^2 \propto e^{-x^2/2(\Delta x)^2}$ is a Gaussian of standard deviation $\Delta x$, and the Fourier transform of the envelope is a Gaussian in $k$ spread $\Delta k = 1/(2\Delta x)$. The product is then exactly $\Delta k \cdot \Delta x = 1/2$, so the Gaussian packet saturates the Fourier bound $\Delta k \cdot \Delta x \geq 1/2$ and every other packet shape gives a larger product. Since a particle's momentum is $p = \hbar k$, the spread in momentum is $\Delta p_x = \hbar \Delta k$, and the wave-number bound becomes the momentum bound $\Delta x \cdot \Delta p_x \geq \hbar/2$. Localising a particle in space necessarily spreads its momenta, and a spread of momenta keeps the packet from staying localised.

---

Flashcards for this section are as follows:

- the Fourier trade-off between the wave-number spread $\Delta k$ and the position spread $\Delta x$ ::@:: $\Delta k \cdot \Delta x \geq 1/2$ for any localised wave packet.
- how the wave-number bound $\Delta k \cdot \Delta x \geq 1/2$ becomes the momentum bound ::@:: With $p = \hbar k$ the momentum spread is $\Delta p_x = \hbar \Delta k$, so $\Delta x \cdot \Delta p_x \geq \hbar/2$.
- what perfect localisation of a particle would do to $\Delta p_x$ ::@:: Perfect localisation would need every wave number, hence every momentum, so the momentum spread $\Delta p_x$ would be unbounded.
- the position spread of the Gaussian packet $\Psi(x) = A e^{-x^2/4(\Delta x)^2} e^{ik_0 x}$ ::@:: Its density $|\Psi|^2 \propto e^{-x^2/2(\Delta x)^2}$ is a Gaussian of standard deviation $\Delta x$.
- the wave-number spread of the Gaussian packet $\Psi(x) = A e^{-x^2/4(\Delta x)^2} e^{ik_0 x}$ ::@:: The Fourier transform of the envelope is a Gaussian in $k$ with spread $\Delta k = 1/(2\Delta x)$.
- the product $\Delta k \cdot \Delta x$ of the Gaussian packet's two spreads ::@:: $\Delta k \cdot \Delta x = 1/2$ exactly, the equality case of the Fourier bound $\Delta k \cdot \Delta x \geq 1/2$.

## electron single-slit broadening

Send electrons through a slit of width $a$ and the diffraction angle satisfies $\theta \approx \lambda/a$. A screen a distance $L$ away shows a band of width $\Delta y \approx \lambda L/a$, so the transverse momentum spread is $\Delta p_y \approx h/a$. The product $\Delta y \cdot \Delta p_y \approx h$ matches the uncertainty bound. Narrowing the slit does not sharpen the beam. It broadens the pattern on the screen, because a tighter transverse localisation at the slit forces a wider momentum spread.

---

Flashcards for this section are as follows:

- what happens to the single-slit pattern as the slit width $a$ is reduced ::@:: The band on the screen broadens, since a smaller $\Delta y$ at the slit forces a larger $\Delta p_y$, with $\Delta y \cdot \Delta p_y \geq \hbar/2$.
- the transverse momentum spread for slit width $a$ ::@:: $\Delta p_y \approx h/a$, giving band width $\Delta y \approx \lambda L/a$.

## energy and time

The energy–time relation $\Delta E \cdot \Delta t \geq \hbar/2$ bounds how sharply a state's energy is defined when it lives for a finite time $\Delta t$. A short-lived excited state acquires a natural energy width $\Delta E \geq \hbar/(2\Delta t)$, which appears as a spread in the frequencies of emitted radiation, the natural linewidth of a spectral line. Long-lived states have sharp energies; states that decay quickly have broad ones.

The same trade-off runs a signal through a wire. A pulse confined to a time $\Delta t$ must carry a spread of angular frequencies $\Delta\omega$ of order $2\pi/\Delta t$, the bandwidth relation, and a circuit has to pass that band for its output to respond within the time $\Delta t$.

---

Flashcards for this section are as follows:

- the energy–time uncertainty relation $\Delta E \cdot \Delta t \geq \hbar/2$ ::@:: $\Delta E \cdot \Delta t \geq \hbar/2$: a state lasting a time $\Delta t$ has an energy spread of at least $\hbar/(2\Delta t)$.
- why spectral lines have a natural width, given $\Delta E \geq \hbar/(2\Delta t)$ ::@:: A decaying state lives for a finite $\Delta t$, so its energy is spread over $\Delta E \geq \hbar/(2\Delta t)$, spreading the emitted frequencies.
- the bandwidth relation: the angular-frequency spread $\Delta\omega$ a signal of duration $\Delta t$ must carry ::@:: $\Delta\omega$ of order $2\pi/\Delta t$, that is $\Delta f$ of order $1/\Delta t$; a circuit passes that band to respond within the time $\Delta t$.

## measurement disturbance

Heisenberg's original argument used a gamma-ray microscope: measuring an electron's position to within $\Delta x$ requires light of wavelength at most $\Delta x$, whose photons carry momentum $h/\Delta x$, kicking the electron by at least that much. The estimate $\Delta x \cdot \Delta p_x \gtrsim h$ reproduced the principle from the back door. The modern reading separates two roles. The uncertainty relation constrains the state before any measurement, preparation uncertainty. A measurement then also disturbs the measured quantity, measurement disturbance, but the inequality itself is a statement about quantum states, not about instruments.

The double-slit arrangement shows the disturbance role at work. To tell the two paths apart, the electron's position must be pinned to within $d/2$, half the slit separation; the position bound then forces a transverse momentum kick $\Delta p_y \geq \hbar/d$. The kick tilts the electron's direction by $\Delta\theta = \Delta p_y/p = \lambda/(2\pi d)$, the order of the fringe spacing, so the interference pattern washes out exactly when the path is pinned down.

---

Flashcards for this section are as follows:

- what the gamma-ray microscope argument shows about $\Delta x$ and $\Delta p_x$ ::@:: That measuring position to within $\Delta x$ with photons of momentum $h/\Delta x$ disturbs momentum by at least that amount, reproducing $\Delta x \cdot \Delta p_x \gtrsim h$.
- the two roles behind the uncertainty principle ::@:: Preparation uncertainty, which limits how narrow a quantum state can be, and measurement disturbance, which limits how gently a quantity can be measured.
- an electron pinned to within $d/2$ to reveal which of two slits of separation $d$ it crosses: the transverse kick $\Delta p_y$ and the angular spread $\Delta\theta$ that follow ::@:: $\Delta p_y \geq \hbar/d$, tilting the path by $\Delta\theta = \lambda/(2\pi d)$, the order of the fringe spacing, so the interference pattern washes out.

## order-of-magnitude estimates

Confining an electron to an atomic-sized region sets the scale of atomic physics. With $\Delta x \approx a_0 \approx 0.53 \times 10^{-10}$ m, the minimum momentum spread is $\Delta p_x \approx \hbar/a_0$, giving a momentum near $10^{-24}$ kg·m/s and a speed near $2 \times 10^6$ m/s. The electron's ground-state motion is therefore fast and its energy far from zero, even in the lowest state, the same zero-point behaviour that keeps a harmonic-oscillator ground state above the potential minimum. Classical physics, which allows a particle to sit still at the bottom of a potential, cannot explain atomic stability; quantum mechanics, through $\Delta x \cdot \Delta p_x \geq \hbar/2$, can.

Shrink the region to nuclear size and the estimate turns quantitative. An electron confined to a nuclear radius $\Delta x = 6 \times 10^{-15}\ \text{m}$ carries $\Delta p \geq \hbar/(2\Delta x) \approx 1.6 \times 10^{7}\ \text{eV}/c$. Taking the momentum at that floor, the relativistic energy $E = \sqrt{(pc)^2 + E_0^2}$ comes to $16.4\ \text{MeV}$, a kinetic energy of $15.9\ \text{MeV}$, far above the energies electrons carry when they stream out of a nucleus in beta decay. Confinement that costly says the nucleus holds no electrons: beta decay creates the electron as it emits it.

---

Flashcards for this section are as follows:

- the momentum scale $\Delta p_x$ of an electron confined to an atom ::@:: $\Delta p_x \approx \hbar/a_0 \approx 10^{-24}$ kg·m/s, a speed near $2 \times 10^6$ m/s.
- why atoms are not classically stable, given a ground-state momentum near $\hbar/a_0$ ::@:: Classical physics lets an electron sit still at the potential minimum and radiate away its energy; the uncertainty relation forces a ground-state momentum near $\hbar/a_0$ and a nonzero energy.
- the minimum energy of an electron confined to a nuclear radius $\Delta x = 6 \times 10^{-15}\ \text{m}$, from $\Delta p \geq \hbar/(2\Delta x)$ ::@:: $\Delta p \approx 1.6 \times 10^{7}\ \text{eV}/c$, so $E = \sqrt{(pc)^2 + E_0^2} = 16.4\ \text{MeV}$ and the kinetic energy is $15.9\ \text{MeV}$.
- what the 16 MeV floor says about electrons inside the nucleus ::@:: Beta-decay electrons come out with far less energy, so the nucleus holds no electrons; beta decay creates the electron as it emits it.
