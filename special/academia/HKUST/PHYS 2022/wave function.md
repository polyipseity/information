---
aliases:
  - probability amplitude
  - quantum state
  - wave function
  - wavefunction
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/wave_function
  - language/in/English
---

# wave function

The wave function $\Psi(x,t)$ is a complex-valued function that completely describes a quantum system. Max Born's 1926 interpretation makes its role statistical: the squared modulus $|\Psi(x,t)|^2$ is the probability density for finding the particle at position $x$ at time $t$. The wave function does not say where the particle is. It says how likely each outcome is.

---

Flashcards for this section are as follows:

- overview: what a wave function is, and what $|\Psi|^2$ gives ::@:: A complex-valued function $\Psi(x,t)$ that describes a quantum system, with $|\Psi(x,t)|^2$ giving the probability density of finding the particle at position $x$ at time $t$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what knowing $|\Psi(x,t)|$ does not determine ::@:: Where the particle is with certainty — only the probability $|\Psi|^2$ of finding it at each place. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## probability density and normalisation

The square law shows itself in light first. In a double-slit run dimmed until flashes arrive one at a time, each flash lands at a definite point; the first twenty arrivals show no pattern, and by about five hundred the interference fringes are clear. The flash rate carries the intensity, $I = Nhf$, while the wave description gives $I = \varepsilon_0 c\langle E^2\rangle$, so arrival probability follows the mean square field. Born's rule hands matter waves the same square: $|\Psi|^2$ stands where $\langle E^2\rangle$ stood.

The probability of finding the particle in a region from $a$ to $b$ at time $t$ is the integral $\int_a^b |\Psi(x,t)|^2 dx$. Because the particle must be found somewhere, the total probability over all space is one: $\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1$. This normalisation condition fixes the overall constant of any physical wave function. A wave function that cannot be normalised does not describe a single particle.

The free-particle wave $\psi = Ae^{i(kx - \omega t)}$ is the standard example that fails. Its density $|\psi|^2 = |A|^2$ is the same everywhere along the axis, so the normalisation integral diverges. One sharp wave number and one sharp frequency also fix $p$ and $E$ exactly, and the uncertainty principle pays for that certainty with $\Delta x = \Delta t = \infty$: the particle sits nowhere in particular. Such waves still do useful work once the particle is confined to a region, and a spread of them superposes into a wave packet that localises.

---

Flashcards for this section are as follows:

- the probability of finding the particle between $a$ and $b$ ::@:: $P(a \leq x \leq b) = \int_a^b |\Psi(x,t)|^2 dx$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the normalisation condition $\int |\Psi|^2 dx = 1$ on a wave function ::@:: $\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1$: the particle must be found somewhere with probability one. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what happens to a wave function that cannot satisfy $\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1$ ::@:: It does not describe a single particle, since the total probability of finding that particle somewhere must be one. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why the free-particle wave $Ae^{i(kx - \omega t)}$ cannot be normalised ::@:: Its density $|\psi|^2 = |A|^2$ is uniform along the whole $x$ axis, so $\int_{-\infty}^{\infty} |\psi|^2\,dx$ diverges. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what one sharp $k$ and one sharp $\omega$ cost a particle's localisation ::@:: $p$ and $E$ are then exact, so the uncertainty principle forces $\Delta x = \Delta t = \infty$; the wave localises nothing until a spread of such waves is superposed into a packet. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- a double-slit light run dimmed to single photons of energy $hf$, counted after 20 and after 500 arrivals: what the two pictures show, and what sets each flash's probability ::@:: Each flash lands at a definite point; the first twenty show no pattern and by five hundred the fringes are clear, with the flash probability following the mean square field $\langle E^2\rangle$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- equating the particle-side intensity $I = Nhf$ with the wave-side $I = \varepsilon_0 c\langle E^2\rangle$: what the photon arrival rate follows ::@:: The mean square electric field, since $N = I/hf$ ties the photon count to the intensity the field carries. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## conditions on a valid wave function

Not every function is an admissible wave function. $\Psi$ must be finite everywhere, single-valued at each point, and continuous, with $\Psi$ and $d\Psi/dx$ both continuous wherever the potential $V(x)$ is finite. It must approach zero as $x$ approaches plus or minus infinity so that it can be normalised. At a point where $V$ is infinite, an impenetrable wall, only $\Psi$ itself is required to vanish; its slope may be discontinuous there.

---

Flashcards for this section are as follows:

- the conditions a wave function must satisfy, including where $V$ is finite ::@:: Finite everywhere, single-valued, continuous with continuous slope where $V$ is finite, and vanishing as $x \to \pm\infty$ so that it is normalisable. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what must vanish at an infinite potential wall: $\Psi$ or $d\Psi/dx$? ::@:: The wave function $\Psi$ itself; its slope $d\Psi/dx$ may be discontinuous there because $V$ is not finite. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## expectation values

Any average over many identical preparations is computed from $\Psi$. The mean position is $\langle x \rangle = \int x |\Psi(x,t)|^2 dx$, and more generally $\langle g(x) \rangle = \int g(x) |\Psi(x,t)|^2 dx$ for any function of position. The spread in position follows from the same integrals, $\Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}$. Momentum averages need the operator $\hat{p} = -i\hbar \partial/\partial x$ rather than a plain integral of $|\Psi|^2$.

---

Flashcards for this section are as follows:

- how the mean position $\langle x \rangle$ is computed from the wave function ::@:: $\langle x \rangle = \int x |\Psi(x,t)|^2 dx$ — the position-weighted probability density integrated over all space. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- why momentum averages need the operator $\hat{p} = -i\hbar\,\partial/\partial x$ ::@:: Momentum is not a function of position; $\langle p \rangle$ requires $\hat{p} = -i\hbar \partial/\partial x$ inside the integral, because $|\Psi|^2$ carries position probabilities only. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- how the spread in position $\Delta x$ follows from $\langle x \rangle$ and $\langle x^2 \rangle$ ::@:: $\Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}$, the square root of the variance built from the two expectation values. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## superposition and interference

The Schrödinger equation is linear, so any linear combination of valid wave functions is itself valid. A particle can therefore occupy a superposition of states at once, and the components interfere like waves: $\Psi = \Psi_1 + \Psi_2$ gives $|\Psi|^2 = |\Psi_1|^2 + |\Psi_2|^2 + 2\,\mathrm{Re}(\Psi_1 \Psi_2^*)$, whose last term is the interference contribution. Localised states, wave packets, are built this way, from plane waves spread over a range of wave numbers, and the price of localisation is the momentum spread of the [uncertainty principle](uncertainty%20principle.md).

---

Flashcards for this section are as follows:

- why wave functions can be added ::@:: The Schrödinger equation is linear, so any linear combination of valid wave functions is again a valid wave function. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- where interference appears in a superposition $\Psi = \Psi_1 + \Psi_2$ ::@:: In the cross term $2\,\mathrm{Re}(\Psi_1 \Psi_2^*)$ of $|\Psi_1 + \Psi_2|^2$; it is absent from classical probability. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- the price of building a localised wave packet, in terms of $\Delta x \cdot \Delta p$ ::@:: A spread of wave numbers, hence a spread of momenta, bounded by $\Delta x \cdot \Delta p \geq \hbar/2$. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->

## phases and interpretation

Because only $|\Psi|^2$ is measured, the overall phase of a wave function carries no observable meaning; two wave functions differing by a constant complex factor of unit modulus describe the same state. Relative phases between superposed components are observable, since they shift the interference term. Whether $\Psi$ itself is a real physical wave or a bookkeeping device for predictions is the divide between interpretive schools, of which the [Copenhagen interpretation](Copenhagen%20interpretation.md) is the standard taught view.

---

Flashcards for this section are as follows:

- what an overall constant phase of a wave function changes ::@:: Nothing observable — only relative phases between components affect interference. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
- what decides whether a wave function is more than a prediction device, given that only $|\Psi|^2$ is measured ::@:: Interpretive stance; the Copenhagen interpretation treats $|\Psi|^2$ statistically and assigns no independent reality to $\Psi$ itself. <!--SR:!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z!fsrs,2026-11-18T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-10T00:00:00.000Z-->
