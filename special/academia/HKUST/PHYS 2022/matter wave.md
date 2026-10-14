---
aliases:
  - de Broglie waves
  - matter wave
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/matter_wave
  - language/in/English
---

# matter wave

A _matter wave_ is the wave carried by a particle. Louis de Broglie proposed in 1924 that every particle with momentum $p$ has an associated wavelength $\lambda = h/p$, where $h$ is the Planck constant; a particle of mass $m$ at speed $v$ has $p = mv$, so $\lambda = h/mv$. The proposal gave matter the wave side of the wave–particle duality that radiation already showed.

---

Flashcards for this section are as follows:

- overview: what a matter wave is, and the wavelength $\lambda$ it gives a particle of momentum $p$ ::@:: The wave Louis de Broglie associates with every particle: $\lambda = h/p$.
- the de Broglie wavelength of a particle of mass $m$ moving at speed $v$ ::@:: $\lambda = h/mv$, since $p = mv$.
- the Planck constant $h$ in de Broglie's relation $\lambda = h/p$: its value ::@:: $h = 6.626 \times 10^{-34}\ \text{J s}$.

## de Broglie hypothesis

The relation came out of radiation itself. A photon satisfies $E = hf$ and $E = pc$, with $f$ its frequency and $c$ the speed of light, so $p = hf/c$; inserting this into $\lambda = c/f$ gives $\lambda = h/p$. Photon wavelength and photon momentum are locked by the Planck constant. De Broglie's step was to drop the photon's special status: because electromagnetic waves show both wave and particle character, all matter does, and the wavelength of a particle's matter wave obeys the same relation $\lambda = h/p$.

The hypothesis explains why wave behaviour hides in everyday life. The wavelength of a runner of mass $100\ \text{kg}$ at $10\ \text{m/s}$ is $\lambda = h/mv \approx 7 \times 10^{-37}\ \text{m}$, far below anything a measurement could resolve. An electron of mass $10^{-30}\ \text{kg}$ at $5 \times 10^{6}\ \text{m/s}$ has $\lambda = h/mv \approx 1.3 \times 10^{-10}\ \text{m}$, a tenth of a nanometre and the spacing scale of atoms. Wave effects appear where the wavelength reaches atomic dimensions.

Electrons are not the only particles with a workable wavelength. A neutron in thermal equilibrium with its surroundings carries kinetic energy $3kT/2$, so $p = \sqrt{3mkT}$ and $\lambda = h/\sqrt{3mkT} = 2.52\ \text{nm}\cdot\text{K}^{1/2}/\sqrt{T}$: $0.145\ \text{nm}$ at $300\ \text{K}$ and $0.287\ \text{nm}$ at $77\ \text{K}$, both within the range of crystal plane spacings. Cooling lengthens the wavelength, so cold and supercold neutron beams are prepared when a longer one is wanted. A neutron carries no charge, so stray electric and magnetic fields bend its path far less than an electron's. [Neutron diffraction](neutron%20diffraction.md) now maps the crystal and molecular structure of biological substances, and hydrogen and helium atoms diffract as well.

---

Flashcards for this section are as follows:

- the photon relations $E = hf$ and $E = pc$: what wavelength–momentum relation do they give for a photon? ::@:: With $\lambda = c/f$ and $p = hf/c$, eliminating $f$ and $c$ gives $\lambda = h/p$ for the photon.
- the de Broglie hypothesis: what it postulates, and the wavelength $\lambda$ it gives a particle of momentum $p$ ::@:: Every particle has wave as well as particle character, and a particle of momentum $p$ carries $\lambda = h/p$, the relation photons obey.
- a runner of mass $m = 100\ \text{kg}$ at $v = 10\ \text{m/s}$: the de Broglie wavelength $\lambda = h/mv$ ::@:: About $7 \times 10^{-37}\ \text{m}$, far too small to observe.
- an electron of mass $m = 10^{-30}\ \text{kg}$ at $v = 5 \times 10^{6}\ \text{m/s}$: the de Broglie wavelength $\lambda = h/mv$ ::@:: About $1.3 \times 10^{-10}\ \text{m}$, atomic-scale and in principle observable.
- why the de Broglie wavelength $\lambda = h/mv$ stays invisible in everyday life ::@:: At everyday masses and speeds, $\lambda = h/mv$ is vanishingly small.
- the de Broglie wavelength of a neutron in thermal equilibrium at temperature $T$ ::@:: $\lambda = h/\sqrt{3mkT} = 2.52\ \text{nm}\cdot\text{K}^{1/2}/\sqrt{T}$: $0.145\ \text{nm}$ at $300\ \text{K}$ and $0.287\ \text{nm}$ at $77\ \text{K}$.
- how the thermal wavelength $\lambda = 2.52\ \text{nm}\cdot\text{K}^{1/2}/\sqrt{T}$ moves as the neutron temperature $T$ changes, and what that lets an experimenter do ::@:: $\lambda$ shrinks as $1/\sqrt{T}$, so cooling the neutrons lengthens it; cold and supercold beams are prepared for the longer wavelengths.
- why neutron beams suit crystal-structure studies where a charged particle beam would not ::@:: A neutron carries no charge, so stray electric and magnetic fields bend its path far less than an electron's, and thermal neutrons already sit within the range of crystal plane spacings.

## electron diffraction

If electrons are waves, they must diffract under the right conditions. Three experiments from the late 1920s showed exactly that.

---

Flashcards for this section are as follows:

- what the three late-1920s electron experiments showed that a particle picture could not ::@:: Diffraction: intensity maxima at angles set by the electron's de Broglie wavelength, as for waves through a grating.

<!-- check: ignore-next-line[header_style]: proper noun (eponym) -->
### Davisson and Germer

Clinton Davisson and Lester Germer fired an electron beam at a nickel single-crystal surface in 1927 and measured the scattered intensity as a function of angle. The rows of atoms on the surface act as a grating of row spacing $D$: a maximum appears at the scattering angle $\varphi$ when $$n\lambda = D \sin\varphi,$$ with $n$ an integer. The strongest maximum sat at $\varphi = 50^\circ$ with $D = 2.15\ \text{Å}$, giving $\lambda = D \sin\varphi \approx 0.165\ \text{nm}$. An electron accelerated from rest through a voltage $V$ gains the kinetic energy $eV$, so $\tfrac{1}{2}mv^2 = eV$ gives $v = \sqrt{2eV/m}$ and $p = mv = \sqrt{2meV}$. Its de Broglie wavelength is then $\lambda = h/\sqrt{2meV}$, near $V = 55\ \text{V}$ about $0.165\ \text{nm}$. With the constants evaluated, $\lambda = 1.226\ \text{nm}/\sqrt{V_0}$ for an electron accelerated through $V_0$ volts. The diffraction angle and the de Broglie formula agreed. Held at $\varphi = 50^\circ$, the peak exists only at the matching energy. As the beam rises through 44 and 48 eV it builds to its largest at 54 eV and fades again by 64 and 68 eV, because only near 54 eV does $\lambda = D\sin\varphi$ hold at that angle. Davisson and Germer shared the 1937 Nobel Prize in Physics for this work. The geometry behind the condition is drawn below, with $D$, $d$, $\varphi$, $\theta$, $2\theta$, and $\alpha$ marked. <p> ![Grating scattering geometry: rows of atoms with dashed lattice planes tilted through them, a vertical incident beam striking an atom and continuing straight past it as a dashed line, a scattered beam leaving up to the right, a thin plane normal between the two beams, and the spacings D between two atoms of a row and d between the planes; the arcs mark theta from the beam to a plane, phi between the beams with alpha on each side of the normal, and 2 theta from the straight-on line to the scattered beam](attachments/grating_scattering_geometry.svg)

[Low-energy electron diffraction](low-energy%20electron%20diffraction.md) grew out of this arrangement and still maps a crystal surface's periodicity routinely today.

---

Flashcards for this section are as follows:

- the grating condition $n\lambda = D \sin\varphi$ in the Davisson–Germer experiment: what $D$ and $\varphi$ are ::@:: $D$ is the spacing of the atomic rows on the nickel surface and $\varphi$ is the scattering angle of the intensity maximum.
- ![Grating scattering geometry: rows of atoms with dashed lattice planes tilted through them, a vertical incident beam striking an atom and continuing straight past it as a dashed line, a scattered beam leaving up to the right, a thin plane normal between the two beams, and the spacings D between two atoms of a row and d between the planes; the arcs mark theta from the beam to a plane, phi between the beams with alpha on each side of the normal, and 2 theta from the straight-on line to the scattered beam](attachments/grating_scattering_geometry.svg) the Davisson–Germer grating geometry for $n\lambda = D \sin\varphi$: what does the drawing show? ::@:: The incident beam strikes an atom and the scattered beam leaves it, the plane normal splitting $\varphi$ into two angles $\alpha$. $\theta$ is the glancing angle from beam to plane, and $2\theta$ is the angle from the straight-on direction to the scattered beam. The right triangle at lower right gives $d = D \sin\alpha$, with $D$ the spacing between neighbouring atoms and $d$ the perpendicular spacing between planes.
- in the Davisson–Germer experiment, the wavelength $\lambda$ from $D = 2.15\ \text{Å}$ and $\varphi = 50^\circ$ via $\lambda = D \sin\varphi$ ::@:: $\lambda \approx 0.165\ \text{nm}$.
- the de Broglie wavelength $\lambda = h/\sqrt{2meV}$ of an electron accelerated through $V = 55\ \text{V}$ ::@:: About $0.165\ \text{nm}$, matching the wavelength the diffraction maximum gave.
- the de Broglie wavelength of an electron accelerated from rest through $V_0$ volts, constants evaluated ::@:: $\lambda = 1.226\ \text{nm}/\sqrt{V_0}$.
- in the Davisson–Germer scattering from nickel held at $\varphi = 50^\circ$ with row spacing $D = 0.215\ \text{nm}$, what happens to the peak as the accelerating voltage rises past 54 V ::@:: It builds to its largest at 54 V, where $\lambda = 1.226\ \text{nm}/\sqrt{V_0}$ matches $D\sin 50^\circ = 0.165\ \text{nm}$, and fades on either side.
- what the 1927 Davisson–Germer result established about the electron wavelength $\lambda = h/p$ ::@:: Electrons diffract as waves, and the measured wavelength matches $\lambda = h/p$.
- the kinetic energy gained by an electron accelerated from rest through a voltage $V$ ::@:: The electron gains $eV$, so $\tfrac{1}{2}mv^2 = eV$.
- the speed $v$ that $\tfrac{1}{2}mv^2 = eV$ gives for an electron accelerated from rest through $V$ ::@:: $v = \sqrt{2eV/m}$.
- the momentum $p$ of an electron accelerated from rest through a voltage $V$ ::@:: $p = mv = \sqrt{2meV}$.

<!-- check: ignore-next-line[header_style]: proper noun (eponym) -->
### G. P. Thomson

George Paget Thomson, the son of J. J. Thomson, passed a beam of energetic electrons through polycrystalline thin metal foils in 1927 and photographed the result: rings of the kind X-rays produce through a powder, not the spot a particle beam would leave. Electrons accelerated through $150\ \text{V}$ gave the same ring pattern as X-rays of wavelength $1\ \text{Å}$, and $\lambda = h/\sqrt{2meV}$ at $150\ \text{V}$ is indeed about $0.1\ \text{nm} = 1\ \text{Å}$. He shared the 1937 Nobel Prize with Davisson and Germer.

---

Flashcards for this section are as follows:

- the G. P. Thomson electron diffraction experiment: the target and the pattern ::@:: Energetic electrons through a polycrystalline thin metal foil produced diffraction rings, the same pattern X-rays give through a powder.
- electrons accelerated through $V = 150\ \text{V}$: the de Broglie wavelength $\lambda = h/\sqrt{2meV}$ ::@:: About $0.1\ \text{nm} = 1\ \text{Å}$, the wavelength of the X-rays whose pattern matched.

## standing waves and quantisation

The wave picture reaches back into the Bohr model. An electron wave bound to a circular orbit must close on itself after one round trip, so the circumference holds a whole number of wavelengths: $$2\pi r = n\lambda, \qquad n = 1, 2, 3, \ldots$$ Inserting the de Broglie relation $\lambda = h/p$ turns this into $2\pi r = nh/p$, so the angular momentum is $L = rp = nh/2\pi = n\hbar$ with $\hbar = h/2\pi$. Bohr's quantisation of angular momentum, taken as a postulate in the model, falls out of the resonance condition instead. In hydrogen the allowed wavelengths are $\lambda_n = 2\pi r_n/n = 2\pi n a_0$ with $r_n = n^2 a_0$ the Bohr radii, so the first three are about $6.28 a_0$, $12.57 a_0$, and $18.85 a_0$. The model itself, its energies and its spectral series, stays in [Bohr model](Bohr%20model.md).

---

Flashcards for this section are as follows:

- the standing-wave resonance condition for an electron of wavelength $\lambda$ in a circular orbit of radius $r$ ::@:: $2\pi r = n\lambda$ for integer $n$: the circumference must hold a whole number of wavelengths.
- given the resonance condition $2\pi r = n\lambda$ and the de Broglie relation $\lambda = h/p$, what angular momentum $L = rp$ does the orbit carry? ::@:: $rp = nh/2\pi$, so $L = n\hbar$ with $\hbar = h/2\pi$.
- the first three standing-wave wavelengths $\lambda_n = 2\pi n a_0$ on hydrogen's Bohr orbits, in units of $a_0$ ::@:: $\lambda_1 \approx 6.28 a_0$, $\lambda_2 \approx 12.57 a_0$, and $\lambda_3 \approx 18.85 a_0$.
- what the standing-wave condition did to the Bohr model's postulate $L = n\hbar$ ::@:: It derived it: requiring the electron's matter wave to close on the orbit gives $L = n\hbar$ with no postulate left over.

## complementarity

Wave and particle aspects are complementary: neither alone describes matter or radiation fully, and the experimental arrangement decides which aspect a measurement reveals. A diffraction grating draws out the wave side of an electron; a photon counter draws out its particle side. The two are not rival theories but two faces one entity shows, each complete only with the other.

---

Flashcards for this section are as follows:

- complementarity: what Niels Bohr's principle states ::@:: Wave and particle aspects complement each other in matter and radiation alike; neither model alone describes them fully, and the experimental arrangement decides which appears.
- what decides which aspect, wave or particle, a measurement reveals ::@:: The experimental arrangement: a diffraction grating draws out the wave side, a particle counter the particle side.
