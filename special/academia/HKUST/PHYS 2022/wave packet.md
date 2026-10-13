---
aliases:
  - Gaussian wave packet
  - wave group
  - wave packet
  - wave train
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/wave_packet
  - language/in/English
---

# wave packet

A wave packet is a short, localised burst of wave action: many component waves of nearby wave numbers, added with phases that make them interfere constructively over a small region and destructively everywhere else. In quantum mechanics the packet is the standard picture of a particle, localised in space, spread in momentum, moving at the group velocity of its envelope.

---

Flashcards for this section are as follows:

- overview: what a wave packet is ::@:: A localised burst built from many component waves of nearby wave numbers that interfere constructively only over a small region.
- why quantum particles are modelled as wave packets ::@:: A particle must be localised in space, and localisation requires a spread of wave numbers, exactly what a packet is.

## localisation and spread

The Gaussian packet $\Psi(x,0) = A\,e^{-x^2/4(\Delta x)^2}\,e^{ik_0 x}$ has an envelope of width $\Delta x$ centred on wave number $k_0$. Fourier decomposition gives a spread $\Delta k \sim 1/(2\Delta x)$, and the two limits are the same statement: squeezing the packet in space, $\Delta x \to 0$, needs every wave number, $\Delta k \to \infty$, and a packet spread over all space, $\Delta x \to \infty$, collapses to a single wave number. The product $\Delta k \cdot \Delta x \geq 1/2$ is the Fourier bound; with $p = \hbar k$ it becomes the quantum uncertainty relation $\Delta x \cdot \Delta p \geq \hbar/2$. Perfect localisation and a definite momentum are therefore mutually exclusive properties of any state.

---

Flashcards for this section are as follows:

- the Fourier width relation between $\Delta k$ and $\Delta x$ for a Gaussian packet ::@:: $\Delta k \cdot \Delta x \geq 1/2$; with $p = \hbar k$ this is $\Delta x \cdot \Delta p \geq \hbar/2$.
- what perfect localisation would require ::@:: Every wave number, hence an unbounded momentum spread — why no state is a point particle.

## group velocity

Superpose two waves of nearly equal frequencies and wave numbers, $\omega_0 \pm \Delta\omega$ and $k_0 \pm \Delta k$, and their sum contains a fast carrier at $\omega_0, k_0$ and a slow envelope at $\Delta\omega, \Delta k$. The beats travel at the envelope's speed $u = \Delta\omega/\Delta k$, which tends to $d\omega/dk$ as the component spacing shrinks. This limit is the group velocity $u = d\omega/dk$, and it is the speed at which the packet, the localisation, the place a particle could be found, moves. The carrier crests inside it move at the phase velocity $v_{\text{ph}} = \omega/k$, which need not match: in the beats example the crests outrun the envelope, appearing at the back, crossing it, and vanishing at the front.

---

Flashcards for this section are as follows:

- the group velocity $u$ of a wave packet ::@:: $u = d\omega/dk$ — the speed of the envelope, and of the localisation it carries.
- how the group velocity $u$ and phase velocity $v_{\text{ph}}$ differ in the two-wave case ::@:: The envelope moves at $u = \Delta\omega/\Delta k$ near $\omega_0/k_0$, while crests move at $v_{\text{ph}} = \omega_0/k_0$; the crests can outrun the envelope, entering at its back and leaving at its front.

## dispersion

A medium is non-dispersive when $\omega$ is proportional to $k$, so phase and group velocities coincide and a packet keeps its shape. When $\omega(k)$ is nonlinear the two speeds differ and the packet spreads as it travels. Each case splits the components' speeds: $\omega = \alpha k$ gives $u = v_{\text{ph}} = \alpha$; $\omega = \beta k^2$ gives $u = 2v_{\text{ph}}$; $\omega = \gamma\sqrt{k}$ gives $u = v_{\text{ph}}/2$. The general relation behind the cases is $u = v_{\text{ph}} + k\,dv_{\text{ph}}/dk$: the group speed runs above the phase speed where the phase speed rises with $k$, and below it where the phase speed falls. Deep water is the falling case: $v_{\text{ph}} = \sqrt{g\lambda/2\pi}$ gives $\omega = \sqrt{gk}$ and $u = v_{\text{ph}}/2$, and a rock thrown in a still pond shows individual crests running through an envelope that trails them.

---

Flashcards for this section are as follows:

- the condition $\omega \propto k$ for a packet to keep its shape ::@:: Non-dispersive propagation, $\omega \propto k$, so $u = d\omega/dk = \omega/k = v_{\text{ph}}$.
- the group-to-phase velocity ratio for $\omega = \beta k^2$ ::@:: $u = 2\beta k = 2v_{\text{ph}}$.
- the group-to-phase velocity ratio for $\omega = \gamma\sqrt{k}$ ::@:: $u = \tfrac{1}{2}\gamma k^{-1/2} = v_{\text{ph}}/2$.
- the general relation between group velocity $u$ and phase velocity $v_{\text{ph}}$ at wave number $k$ ::@:: $u = v_{\text{ph}} + k\,dv_{\text{ph}}/dk$, so $u$ runs above $v_{\text{ph}}$ where $v_{\text{ph}}$ rises with $k$ and below it where $v_{\text{ph}}$ falls.
- deep-water waves: the phase speed $v_{\text{ph}}$ in terms of wavelength $\lambda$, and the group speed $u$ that follows ::@:: $v_{\text{ph}} = \sqrt{g\lambda/2\pi}$, hence $\omega = \sqrt{gk}$ and $u = d\omega/dk = v_{\text{ph}}/2$; in a pond the envelope trails the crests running through it.

## packet as a particle

Reading the packet as a particle binds the wave description to quantum mechanics: the envelope locates the particle, $\Delta x$ is its position spread, and the component momenta $\hbar k$ supply its momentum spread, with $\Delta x \cdot \Delta p \geq \hbar/2$ from the Fourier bound. Motion at the group velocity is then particle motion. For a free non-relativistic particle the energy relations $E = p^2/2m$ with $E = \hbar\omega$ and $p = \hbar k$ fix the dispersion $\omega = \hbar k^2/2m$, so the group velocity is $u = d\omega/dk = \hbar k/m = p/m$, the classical particle speed, while the phase velocity $v_{\text{ph}} = \omega/k = \hbar k/2m$ is half of it. A relativistic particle keeps the identification. Differentiating $E^2 = p^2c^2 + m^2c^4$ gives the group velocity $u = dE/dp = pc^2/E$, which reduces to the particle's speed $v$ for a slow particle. The phase velocity $v_{\text{ph}} = E/p = c^2/v$ again runs ahead of it. The de Broglie relation $\lambda = h/p$ names the carrier, while the [uncertainty principle](uncertainty%20principle.md) names the trade-off. A single-slit beam is the same physics in one transverse dimension: the narrower the slit localises the electron, the wider the diffracted momentum spread.

---

Flashcards for this section are as follows:

- how the packet picture reproduces the uncertainty relation between $\Delta x$ and $\Delta p$ ::@:: Localisation width $\Delta x$ forces a wave-number spread $\Delta k \geq 1/(2\Delta x)$, hence $\Delta p = \hbar\Delta k$ with $\Delta x \cdot \Delta p \geq \hbar/2$.
- what moves at the group velocity in the particle picture ::@:: The envelope, and with it the place where the particle is likely to be found.
- the dispersion relation $\omega(k)$ of a free non-relativistic matter wave ::@:: From $E = p^2/2m$ with $E = \hbar\omega$ and $p = \hbar k$ comes $\omega = \hbar k^2/2m$.
- the group velocity $u$ of a free matter wave with $\omega = \hbar k^2/2m$ ::@:: $u = d\omega/dk = \hbar k/m = p/m$, the classical particle speed.
- the phase velocity $v_{\text{ph}}$ of a free matter wave with $\omega = \hbar k^2/2m$ ::@:: $v_{\text{ph}} = \omega/k = \hbar k/2m$, half the group velocity $u = p/m$.
- for a relativistic matter wave with $E^2 = p^2c^2 + m^2c^4$, the group and phase velocities ::@:: $u = dE/dp = pc^2/E$, the particle's speed $v$; $v_{\text{ph}} = E/p = c^2/v$, which is larger and not the particle's speed.
