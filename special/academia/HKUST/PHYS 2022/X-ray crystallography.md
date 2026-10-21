---
aliases:
  - X-ray crystallography
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/X-ray_crystallography
  - language/in/English
---

# X-ray crystallography

_X-ray crystallography_ reads a crystal's atomic and molecular structure from the way the crystal diffracts an X-ray beam. Measuring the angles and the intensities of the diffracted beams builds a three-dimensional map of the electron density inside the crystal, from which the positions of the atoms, their chemical bonds, and their disorder follow.

The angles come from [Bragg's law](Bragg%27s%20law.md): each set of lattice planes reflects strongly at the glancing angles that solve $n\lambda = 2d\sin\theta$. The technique belongs to the diffraction family beside [neutron diffraction](neutron%20diffraction.md). Bragg reflection is not tied to X-rays: the electron waves of [low-energy electron diffraction](low-energy%20electron%20diffraction.md) obey the same law at the surface of a crystal.

The Braggs, William Henry and William Lawrence, father and son, shared the 1915 Nobel Prize in Physics for the crystal-structure analysis Bragg's law made possible. The method reached its most famous structure in the double helix of deoxyribonucleic acid (DNA), whose determination won the 1962 Nobel Prize in Physiology or Medicine.

---

Flashcards for this section are as follows:

- overview: what X-ray crystallography builds from the measured angles and intensities of diffracted beams ::@:: A three-dimensional map of the crystal's electron density, from which atom positions, chemical bonds, and disorder follow.
- the law that turns a measured diffraction angle $\theta$ into a plane spacing $d$ in X-ray crystallography ::@:: Bragg's law, $n\lambda = 2d\sin\theta$, with $d$ the plane spacing and $\theta$ the glancing angle.
- waves besides X-rays that obey $n\lambda = 2d \sin\theta$, as surface diffraction shows ::@:: Electron waves, obeying the law at crystal surfaces in low-energy electron diffraction.
- the 1915 Nobel Prize in Physics for crystal-structure analysis by X-ray diffraction ::@:: Shared by William Henry Bragg and William Lawrence Bragg, father and son.
- the structure whose determination won the 1962 Nobel Prize in Physiology or Medicine ::@:: The double helix of deoxyribonucleic acid (DNA).

## reading a pattern

The peak positions come first: every measured scattering angle $2\theta$ returns its plane spacing $d$ through $n\lambda = 2d\sin\theta$, and the spacings identify the lattice through its [Miller indices](Bragg%27s%20law.md#Miller%20indices%20and%20d-spacings). The intensities come second: they set how much scattering each part of the cell contributes, and the density map is built and refined until it reproduces the measured intensities.

---

Flashcards for this section are as follows:

- the first pass over an X-ray diffraction pattern, from each measured scattering angle $2\theta$: what it returns ::@:: The plane spacing $d$ of each family, through Bragg's law $n\lambda = 2d\sin\theta$, and the spacings identify the lattice through its Miller indices.
- the second pass over an X-ray diffraction pattern, and what it returns ::@:: The peak intensities: they set how much scattering each part of the cell contributes, and the electron-density map is refined until it reproduces them.

## temperature of the target

The lattice that satisfies Bragg's law is the lattice of the atoms' mean positions. At any temperature the atoms vibrate about those positions, and the diffraction pattern reads the vibration as lost intensity. An atom that scatters from a displaced position reradiates waves that slip out of step with the waves from its neighbours, so the elastic Bragg peaks lose intensity to a diffuse thermal background. That loss is the Debye–Waller factor: the peak intensity falls as $\exp(-2M)$, with $M = 8\pi^2\langle u^2\rangle\sin^2\theta/\lambda^2$. Here $\langle u^2\rangle$ is the mean-square displacement of an atom along the scattering vector, the direction in which the beam's momentum changes, and it is a third of the atom's total mean-square displacement when the vibration is isotropic.

The vibration leaves that mean lattice where it is, so it does not shift the peaks; the intensities pay for it instead. Because $M$ grows with $\sin^2\theta$, the high-angle peaks of a warm sample fade first: heating raises $\langle u^2 \rangle$ and drains the pattern into the diffuse background, while cooling restores the weak high-angle peaks. Even at absolute zero the zero-point vibration leaves a residual attenuation.

Temperature reaches the peak positions by a second route. A solid expands as it warms, so every plane spacing $d$ grows, and $n\lambda = 2d\sin\theta$ then needs a smaller $\theta$: each peak moves toward the beam. The shift is small but measurable, and it makes a lattice parameter belong to the temperature at which the sample was measured. Heating the sample inside the diffractometer and following the shift measures the thermal expansion directly.

Both effects belong to the diffraction family, not to X-rays alone. [Neutron diffraction](neutron%20diffraction.md) scatters from the nucleus of the vibrating atom and [low-energy electron diffraction](low-energy%20electron%20diffraction.md) from its vibrating surface layer. Every member of the family reads the same lattice, so every one loses intensity through the Debye–Waller factor and every one shifts its peaks as the crystal expands; intensities and lattice parameters are quoted at a stated target temperature.

---

Flashcards for this section are as follows:

- what vibration of a target's atoms does to its elastic Bragg peaks through the Debye–Waller attenuation $\exp(-2M)$ ::@:: Each atom reradiates from a displaced position, out of step with the waves from its neighbours, so the peak intensity falls as $\exp(-2M)$ and the lost intensity reappears as diffuse thermal background.
- the Debye–Waller exponent $M$ for an atom with mean-square displacement $\langle u^2\rangle$ along the scattering vector, at Bragg angle $\theta$ and wavelength $\lambda$ ::@:: $M = 8\pi^2\langle u^2\rangle\sin^2\theta/\lambda^2$, so the elastic intensity falls as $\exp(-2M)$; $\langle u^2\rangle$ is the component along the scattering vector, a third of the total mean-square displacement for isotropic vibration.
- which peaks of a diffraction pattern fade first when the Debye–Waller exponent $M$ grows with $\sin^2\theta$ ::@:: The high-angle peaks, since the attenuation $\exp(-2M)$ bites hardest at large $\theta$.
- how target temperature, through the mean-square vibration amplitude $\langle u^2 \rangle$, moves a diffraction pattern's intensities ::@:: Heating raises $\langle u^2 \rangle$, draining the elastic peaks into diffuse background; cooling restores them, and at absolute zero the zero-point vibration leaves a residual attenuation.
- how temperature reaches the peak positions through the plane spacing $d$, even though the vibration itself does not shift them ::@:: The atoms vibrate about fixed mean sites, so the mean lattice stays put and only the intensities fall; a solid also expands as it warms, every $d$ grows, and $n\lambda = 2d\sin\theta$ then needs a smaller $\theta$, so each peak moves to a smaller $2\theta$ and a lattice parameter belongs to a stated temperature.
- why the Debye–Waller attenuation acts on X-ray, neutron, and low-energy electron diffraction alike ::@:: All three scatter from atoms about vibrating lattice sites: X-rays from the electrons, neutrons from the nucleus, low-energy electrons from the surface layer; they read the same lattice motion.
