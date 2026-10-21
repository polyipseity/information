---
aliases:
  - photoelectric effect
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/photoelectric_effect
  - language/in/English
---

# photoelectric effect

The photoelectric effect is the emission of electrons from a material when light of sufficient frequency shines on it. Light is one of four ways to free an electron from a material; the others are heating it, striking it with a fast particle, and pulling on it with a strong electric field. Measuring the kinetic energy of the emitted electrons against the frequency of the light is [photoemission spectroscopy](photoemission%20spectroscopy.md), the technique built on the effect.

---

Flashcards for this section are as follows:

- the photoelectric effect: what it is ::@:: The emission of electrons from a material when light of sufficient frequency shines on it.
- the four ways an electron can leave a material ::@:: Light shining on it (the photoelectric effect), heat (thermionic emission), a fast particle striking it (secondary emission), and a strong external electric field pulling it out (field emission).

## historical background

In 1887, Heinrich Hertz used a spark gap to detect electromagnetic waves and found the detector spark grew more vigorous under ultraviolet light. In 1888, Wilhelm Hallwachs confirmed that ultraviolet light on a zinc plate generated positive charges by electron emission. By 1898, J. J. Thomson found that the number of emitted electrons varied with ultraviolet intensity. Philipp Lenard studied the effect in 1902, measuring how kinetic energy and electron count depended on intensity and frequency.

Millikan set out to show Einstein wrong and spent almost ten years on the attempt instead. From 1916 he reported the stopping potential on sodium rising in a straight line with the frequency of the light, with no photoelectrons at all below $4.39 \times 10^{14}\ \text{Hz}$, a wavelength of $683\ \text{nm}$. The slope of that line gave $h = 4.1 \times 10^{-15}\ \text{eV}\cdot\text{s}$, in agreement with the value Planck found from black-body radiation.

---

Flashcards for this section are as follows:

- the two observations before 1900, by Heinrich Hertz and Wilhelm Hallwachs ::@:: Heinrich Hertz's detector spark grew stronger under ultraviolet light in 1887. Wilhelm Hallwachs found positive charges on a zinc plate in 1888.
- J. J. Thomson's 1898 finding ::@:: The number of emitted electrons varied with the intensity of the ultraviolet light.
- Philipp Lenard's systematic study: what he measured ::@:: The dependence of kinetic energy and the number of emitted electrons on the intensity and frequency of incident light.
- Robert Millikan's 1916 photoelectric measurements on sodium: the threshold frequency ::@:: No photoelectrons below $4.39 \times 10^{14}\ \text{Hz}$, a wavelength of $683\ \text{nm}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the slope of Robert Millikan's 1916 line of maximum kinetic energy against light frequency ::@:: Planck's constant, $h = 4.1 \times 10^{-15}\ \text{eV}\cdot\text{s}$, in agreement with the value from black-body radiation. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## experimental setup

The standard apparatus is a vacuum tube with a metallic emitter electrode and a collector electrode. Light ejects electrons from the emitter, and they travel to the collector. A variable voltage supply and ammeter measure the electron current and stopping potential.

Different metals have different work functions, the minimum energy needed to free an electron from the surface. Typical values are sodium at 2.36 eV, zinc 4.3 eV, copper 4.7 eV, and platinum 6.35 eV. Work functions depend on the surface, so other recommended tables give different numbers: the CRC Handbook lists copper at 4.48 eV and platinum at 5.64 eV, and a clean-surface review puts polycrystalline platinum near 5.65 eV. A retarding voltage on the collector repels the emitted electrons. At the stopping potential $V_s$, even the most energetic electrons turn back and the current drops to zero. That gives the maximum kinetic energy directly: $KE_{\text{max}} = eV_s$.

---

Flashcards for this section are as follows:

- the work function: what it is and how it differs among materials ::@:: The minimum energy needed to free an electron from the surface; sodium is 2.36 eV, zinc about 4.3 eV, copper about 4.7 eV, platinum about 6.35 eV.
- the stopping potential: what it gives directly ::@:: The maximum kinetic energy of the photoelectrons, through $KE_{\text{max}} = eV_s$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## classical predictions

Classical wave theory puts the electron's energy in the wave's intensity: brighter light should hand a photoelectron more kinetic energy. It sets no threshold frequency, since a weak wave of any frequency still delivers energy, only slowly. At very low intensity an electron should wait a long time to collect enough to escape; for sodium at $10^{-8}\ \text{W/m}^2$ the estimate comes to about 15 years. One point it gets right: more intensity means more photoelectrons per second.

---

Flashcards for this section are as follows:

- classical prediction for kinetic energy: what it depends on ::@:: Light intensity.
- classical theory and a threshold frequency: what it cannot do ::@:: It cannot produce one. Any frequency delivers energy given enough intensity, so classical theory has no cutoff below which nothing happens.
- classical prediction at low intensity of $10^{-8}\ \text{W/m}^2$ on sodium: what should happen ::@:: A measurable waiting time before any electron escapes; classical theory gives about 15 years for a photoelectron of kinetic energy $1.00\ \text{eV}$.
- classical prediction for the number of photoelectrons, against experiment ::@:: It rises with light intensity, and the measurements agree.

## experimental results

The maximum kinetic energy depends only on the frequency of the light, not its intensity, which classical wave theory cannot explain. Neither can it produce the threshold frequency each material has, below which no electrons are emitted, whatever the intensity. The number of photoelectrons is proportional to light intensity, one point where classical theory agrees. Electrons are emitted almost instantaneously, even at low intensities, where classical theory expects the longest wait.

---

Flashcards for this section are as follows:

- the photoelectric effect: what determines the maximum kinetic energy of photoelectrons ::@:: The frequency of the incident light, not its intensity.
- the threshold frequency: what it means and what it depends on ::@:: The minimum frequency below which no electrons are emitted; it depends on the material's work function.
- the photoelectric effect: what the number of photoelectrons is proportional to ::@:: The intensity of the incident light.
- the photoelectric effect: the emission delay ::@:: Photoelectrons are emitted almost instantaneously, within about $3 \times 10^{-9}\ \text{s}$ of illumination, independent of light intensity. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

<!-- check: ignore-next-line[header_style]: proper noun -->
## Einstein's interpretation

Einstein explained the photoelectric effect by treating light as a stream of photons, each carrying energy $E = hf$, where $h$ is the Planck constant and $f$ is the frequency. A photon transfers all its energy in one collision with an electron in the metal. Energy conservation splits that energy in two: the electron pays the work function $\Phi$, the binding energy holding it in the material, and keeps the rest as kinetic energy, $$hf = \Phi + K,$$ so the kinetic energy left over is $K = hf - \Phi$. The most energetic photoelectrons are those freed from the surface with no energy spent travelling out of the metal, so $KE_{\text{max}} = hf - \Phi$. The threshold frequency is $f_0 = \Phi / h$; below it, $hf < \Phi$ and no electron is ejected.

Run together with $KE_{\text{max}} = eV_s$ from the apparatus, the photoelectric equation makes the stopping voltage a straight line in the frequency, $V_s = (h/e)f - \Phi/e$. Its slope $h/e$ is the same for every metal, and each metal contributes only its work function through the intercept: a larger work function drops the line and pushes the threshold frequency $f_0 = \Phi/h$ higher.

---

Flashcards for this section are as follows:

- Albert Einstein's photon hypothesis: the energy of a single photon ::@:: $E = hf$, where $h$ is the Planck constant and $f$ is the frequency of the light. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the photoelectric equation: maximum kinetic energy of a photoelectron ::@:: $K = hf - \Phi$, where $\Phi$ is the work function of the material. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the energy-conservation balance behind the photoelectric equation: what the photon energy $hf$ splits into ::@:: The work function $\Phi$ paid to free the electron plus the kinetic energy $K$ it keeps, $hf = \Phi + K$.
- the most energetic photoelectrons: where they are freed from, and their maximum kinetic energy $KE_{\text{max}}$ in terms of $hf$ and $\Phi$ ::@:: From the surface, with no energy spent travelling out of the metal, so $KE_{\text{max}} = hf - \Phi$.
- the work function $\Phi$: what it represents ::@:: The minimum energy an electron must gain to escape from the surface of the material.
- the threshold frequency: its relation to the work function ::@:: $f_0 = \Phi / h$; below this frequency, no electrons are emitted. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the stopping voltage against frequency for a metal of work function $\Phi$ ::@:: $V_s = (h/e)f - \Phi/e$: a straight line whose slope $h/e$ is the same for every metal and whose intercept fixes the work function.

## applications

Two instruments turn the photoelectric effect into a measurement tool.

---

Flashcards for this section are as follows:

- overview: the two applications of the photoelectric effect covered here ::@:: X-ray photoelectron spectroscopy, which reads elemental composition from binding energies, and charge-coupled device cameras, which trap photoelectrons as charge.

<!-- check: ignore-next-line[header_style]: proper noun -->
### X-ray photoelectron spectroscopy

[X-ray photoelectron spectroscopy](X-ray%20photoelectron%20spectroscopy.md) (XPS) uses the photoelectric effect to identify the elemental composition of materials. Each element produces characteristic peaks at specific binding energies.

---

Flashcards for this section are as follows:

- X-ray photoelectron spectroscopy (XPS): what it measures and how ::@:: The elemental composition of materials, from the binding energies of electrons ejected by X-rays; each element has characteristic peaks.

### charge-coupled device cameras

A charge-coupled device (CCD) sensor consists of millions of tiny pixels, each built around a metal-oxide-semiconductor (MOS) capacitor. Light ejects electrons from a pixel into a potential well created by a gate voltage on the capacitor. The accumulated charge is proportional to the light intensity. After the exposure, each charge packet travels along a row to a readout amplifier, which converts it to a voltage. The transfer is sequential, like a bucket brigade. That is where the name charge-coupled comes from. Quantum efficiency is the fraction of incident photons that produce a measurable electron. Front-illuminated CCDs peak near 40% in the visible, while back-thinned scientific CCDs exceed 90%.

---

Flashcards for this section are as follows:

- a charge-coupled device (CCD) pixel: the component that traps photoelectrons, and what it records ::@:: A metal-oxide-semiconductor (MOS) capacitor, which makes a potential well that holds the electrons. The charge built up is proportional to light intensity.
- how charge-coupled device (CCD) charges are read out ::@:: Charges are transferred pixel by pixel along rows to a readout amplifier (bucket-brigade readout), where each charge packet is converted to a voltage.
- front-illuminated and back-thinned charge-coupled devices (CCDs): which has a visible quantum efficiency near $40\%$, and which exceeds $90\%$? ::@:: The front-illuminated kind peaks near $40\%$ in the visible. Back-thinned scientific devices exceed $90\%$.
