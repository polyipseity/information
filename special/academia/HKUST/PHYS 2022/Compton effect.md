---
aliases:
  - Compton effect
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Compton_effect
  - language/in/English
---

# Compton effect

The Compton effect is the change in wavelength of an X-ray photon when it scatters off an electron. The shift is direct evidence that photons carry momentum.

---

Flashcards for this section are as follows:

- what the Compton effect is ::@:: The increase in the wavelength of an X-ray photon after it scatters off an electron. The shift is direct evidence that photons carry momentum. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->

## experimental setup

A crystal spectrometer and an ionisation chamber measure X-rays scattered from a graphite target at several angles. Classical theory expected every scattered ray to keep the incident wavelength: the wave makes the electrons oscillate, and the atom reradiates at the same frequency, the process called Thomson scattering. The spectra at the larger angles show a second line at a longer wavelength, pulled further from the incident line as the angle grows, beside the unshifted line. Compton shared the 1927 Nobel Prize in Physics with Charles Wilson.

Reading the wavelength shift against the scattering angle is one member of the inelastic X-ray scattering family: the energy a photon hands to an electron is read from the wavelength the photon loses.

---

Flashcards for this section are as follows:

- the scattered spectrum at the larger angles: the lines it shows ::@:: The unshifted line classical theory predicts, plus a second line at a longer wavelength that moves further out as the scattering angle grows. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the measurement setup: how the scattered rays were read ::@:: X-rays scattered off a graphite target, and a crystal spectrometer with an ionisation chamber measured the rays at various angles. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- Thomson scattering: what classical theory expects of the scattered wavelength ::@:: The same frequency as the incident wave, since the electrons reradiate at the frequency the wave drives them with.
- the 1927 Nobel Prize in Physics: who shared it ::@:: Arthur Compton and Charles Wilson.
- the technique family of measuring the Compton wavelength shift against scattering angle ::@:: Inelastic X-ray scattering, where the energy a photon hands to an electron is read from the wavelength the photon loses.

## photon momentum and energy

A photon carries energy $E = hf$ and momentum $p = E/c = h/\lambda$. The electron it strikes has relativistic energy $E_e^2 = (mc^2)^2 + p_e^2 c^2$. The Compton shift comes from conserving energy and momentum in the elastic collision. Take the struck particle at rest before the collision, with mass $m$. The photon arrives with energy $E_\gamma$ and momentum $p_\gamma$, scatters through angle $\theta$ to energy $E_\gamma'$ and momentum $p_\gamma'$, and the struck particle recoils with energy $E_e$ and momentum $p_e$, so $$E_\gamma + mc^2 = E_\gamma' + E_e, \qquad \vec p_\gamma = \vec p_\gamma' + \vec p_e.$$

Rearrange the momentum law for $\vec p_e$ and square it. The cross term is $2\vec p_\gamma \cdot \vec p_\gamma' = 2p_\gamma p_\gamma' \cos\theta$, which gives $$p_e^2 = p_\gamma^2 + p_\gamma'^2 - 2p_\gamma p_\gamma' \cos\theta.$$

Rearrange the energy law for $E_e$ and square it too: $$E_e^2 = E_\gamma^2 + E_\gamma'^2 + (mc^2)^2 - 2E_\gamma E_\gamma' + 2mc^2(E_\gamma - E_\gamma').$$

The relativistic relation $E_e^2 = p_e^2 c^2 + (mc^2)^2$ then ties the two results together. Substitute $p_e^2 c^2$ for $E_e^2 - (mc^2)^2$ and equate the outcome with the squared energy law. The terms $E_\gamma^2$, $E_\gamma'^2$ and $(mc^2)^2$ cancel, leaving $$E_\gamma E_\gamma'(1 - \cos\theta) = mc^2(E_\gamma - E_\gamma').$$

Divide by $E_\gamma E_\gamma'$ and use $1/E = \lambda/(hc)$ on the right-hand side, which turns the energy difference into a wavelength difference: $$1 - \cos\theta = mc^2 \frac{\lambda' - \lambda}{hc}.$$

Solving for the wavelength difference gives the Compton shift $\Delta\lambda = \lambda' - \lambda = \dfrac{h}{mc}(1 - \cos\theta)$, where $\theta$ is the scattering angle and $m$ is the mass of the struck particle.

---

Flashcards for this section are as follows:

- the momentum of a photon ::@:: $p = E/c = hf/c = h/\lambda$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the Compton shift formula: the change in wavelength ::@:: $\Delta\lambda = \dfrac{h}{mc}(1 - \cos\theta)$, where $\theta$ is the scattering angle and $m$ is the struck particle's mass. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the struck electron: which relation links its total energy $E_e$ to its momentum $p_e$ ::@:: $E_e^2 = (mc^2)^2 + p_e^2 c^2$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the elastic collision assumption: what it fixes ::@:: Energy is conserved across the collision. Together with momentum conservation, that fixes the photon's final energy, and so the shift. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the energy conservation law in the Compton collision, between $E_\gamma$, $E_\gamma'$, $E_e$, and $mc^2$ ::@:: $E_\gamma + mc^2 = E_\gamma' + E_e$: the incident photon energy plus the rest energy of the struck particle at rest equals the scattered photon energy plus the recoil energy.
- the momentum conservation law in the Compton collision, between $\vec p_\gamma$, $\vec p_\gamma'$, and $\vec p_e$ ::@:: $\vec p_\gamma = \vec p_\gamma' + \vec p_e$: the incident photon momentum equals the scattered photon momentum at angle $\theta$ plus the recoil momentum of the struck particle.
- squaring the momentum law rearranged for $\vec p_e$: the cross term it leaves ::@:: $p_e^2 = p_\gamma^2 + p_\gamma'^2 - 2p_\gamma p_\gamma' \cos\theta$, from the cross term $2\vec p_\gamma \cdot \vec p_\gamma' = 2p_\gamma p_\gamma' \cos\theta$.
- tying the squared momentum law $p_e^2 = p_\gamma^2 + p_\gamma'^2 - 2p_\gamma p_\gamma' \cos\theta$ to the squared energy law through $E_e^2 = p_e^2c^2 + (mc^2)^2$: what survives ::@:: The terms $E_\gamma^2$, $E_\gamma'^2$, and $(mc^2)^2$ cancel, leaving $E_\gamma E_\gamma'(1 - \cos\theta) = mc^2(E_\gamma - E_\gamma')$.
- turning the energy relation $E_\gamma E_\gamma'(1 - \cos\theta) = mc^2(E_\gamma - E_\gamma')$ into a wavelength relation: the step that does it ::@:: Divide by $E_\gamma E_\gamma'$ and use $1/E = \lambda/(hc)$ on the right, which gives $1 - \cos\theta = mc^2\dfrac{\lambda' - \lambda}{hc}$.
- the angle dependence of the factor $(1 - \cos\theta)$: what it gives at $\theta = 0$ and at backscattering ::@:: The shift vanishes at $\theta = 0$ and doubles at $\theta = 180°$, where $1 - \cos\theta = 2$.

<!-- check: ignore-next-line[header_style]: proper noun -->
## Compton wavelength

The Compton wavelength of the electron is $\lambda_C = h/(m_e c) \approx 2.43 \times 10^{-12}$ m, and the same expression $\lambda_C = h/(mc)$ holds for any particle of mass $m$. The proton's is $\lambda_C = h/(m_p c) \approx 1.32 \times 10^{-15}$ m. Since $\lambda_C$ scales as $1/m$, a proton target shifts a photon far less than an electron target at the same angle. The shift is one Compton wavelength at $\theta = 90°$ and two at $\theta = 180°$ (backscattering).

Whether a shift can be seen comes down to $\lambda_C$ against the incident wavelength. Compton's $0.071\ \text{nm}$ X-rays shift by about $0.03$ of their wavelength at a right angle, while visible light at $500\ \text{nm}$ never shifts by more than about $10^{-5}$, too small to resolve and rare to occur. The effect matters for X-rays and gamma rays rather than for light. The unshifted line in the same spectra has an origin of its own: a photon that meets a tightly bound inner electron recoils against the whole atom, thousands of times heavier than the electron, and the shift shrinks to nothing.

---

Flashcards for this section are as follows:

- the Compton wavelength of the electron ::@:: $\lambda_C = h/(m_e c) \approx 2.43 \times 10^{-12}$ m. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the Compton wavelength for a particle of mass $m$ other than the electron ::@:: $\lambda_C = h/(mc)$.
- the Compton wavelength of the proton ::@:: $\lambda_C = h/(m_p c) \approx 1.32 \times 10^{-15}$ m. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the maximum Compton shift: at what angle it occurs ::@:: At $\theta = 180°$ (backscattering), where $\Delta\lambda = 2\lambda_C$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the shift at a scattering angle of $\theta = 90°$ ::@:: $\Delta\lambda = \lambda_C$, one Compton wavelength.
- the fractional shift $\Delta\lambda/\lambda$ for Compton's $0.071\ \text{nm}$ X-rays and for visible light at $500\ \text{nm}$ ::@:: About $0.03$ for the X-rays, and at most about $10^{-5}$ for the visible light, so the effect is measurable only for X-rays and gamma rays.
- the origin of the unshifted line in a Compton spectrum ::@:: Scattering from a tightly bound inner electron, where the photon recoils against the whole atom and the atom's far larger mass makes the shift negligible.

## single-photon double-slit experiment

The scattering above measures a photon's momentum. A double slit lit one photon at a time measures the same quantum. Each photon arrives as a single spot, and the spots accumulate into an interference pattern. That pattern is read as each photon passing through both slits and interfering with itself.

---

Flashcards for this section are as follows:

- a double slit lit one photon at a time: what arrives at the screen ::@:: Each photon arrives as a single spot, and the spots accumulate into an interference pattern. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- single-photon interference: how it is read ::@:: Each photon passes through both slits and interferes with itself. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
