---
aliases:
  - photoelectric effect
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/photoelectric_effect
  - language/in/English
---

# photoelectric effect

The photoelectric effect is the emission of electrons from a material when light of sufficient frequency shines on it.

---

Flashcards for this section are as follows:

- the photoelectric effect: what it is ::@:: The emission of electrons from a material when light of sufficient frequency shines on it.

## historical background

In 1887, Heinrich Hertz used a spark gap to detect electromagnetic waves and found the detector spark grew more vigorous under ultraviolet light. In 1888, Wilhelm Hallwachs confirmed that ultraviolet light on a zinc plate generated positive charges by electron emission. By 1898, J. J. Thomson found that the number of emitted electrons varied with ultraviolet intensity. Philipp Lenard studied the effect in 1902, measuring how kinetic energy and electron count depended on intensity and frequency.

---

Flashcards for this section are as follows:

- the two observations before 1900, by Hertz and Hallwachs ::@:: Hertz's detector spark grew more vigorous under ultraviolet light in 1887, and Hallwachs found positive charges on a zinc plate in 1888, produced by electron emission.
- Thomson's 1898 finding ::@:: The number of emitted electrons varied with the intensity of the ultraviolet light.
- Lenard's systematic study: what he measured ::@:: The dependence of kinetic energy and the number of emitted electrons on the intensity and frequency of incident light.

## experimental setup

The standard apparatus is a vacuum tube with a metallic emitter electrode and a collector electrode. Light ejects electrons from the emitter, and they travel to the collector. A variable voltage supply and ammeter measure the electron current and stopping potential.

Different metals have different work functions, the minimum energy needed to free an electron from the surface. Typical values are sodium at about 2.3 eV, zinc 4.3 eV, copper 4.7 eV, and platinum 6.35 eV. A retarding voltage on the collector repels the emitted electrons. At the stopping potential $V_s$, even the most energetic electrons turn back and the current drops to zero, giving the maximum kinetic energy directly: $KE_{\text{max}} = eV_s$.

---

Flashcards for this section are as follows:

- the work function: what it is and how it differs among materials ::@:: The minimum energy needed to free an electron from the surface; sodium is about 2.3 eV, zinc about 4.3 eV, copper about 4.7 eV, platinum about 6.35 eV.
- the stopping potential: what it gives directly ::@:: The maximum kinetic energy of the photoelectrons, through $KE_{\text{max}} = eV_s$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## classical predictions

Classical wave theory predicted that the kinetic energy of photoelectrons should depend on light intensity, that the number of photoelectrons should depend on frequency, and that at low intensities there should be a measurable waiting time before any electron escapes.

---

Flashcards for this section are as follows:

- classical prediction for kinetic energy: what it depends on ::@:: Light intensity.
- classical prediction for electron count: what it depends on ::@:: Frequency of the light.
- classical prediction at low intensity: what should happen ::@:: A measurable waiting time before any electron escapes.

## experimental results

Every classical prediction failed. The maximum kinetic energy depends only on the frequency of the light, not its intensity. Each material has a threshold frequency below which no electrons are emitted, regardless of intensity. The number of photoelectrons is proportional to light intensity, and electrons are emitted almost instantaneously, even at low intensities.

---

Flashcards for this section are as follows:

- the photoelectric effect: what determines the maximum kinetic energy of photoelectrons ::@:: The frequency of the incident light, not its intensity.
- the threshold frequency: what it means and what it depends on ::@:: The minimum frequency below which no electrons are emitted; it depends on the material's work function.
- the photoelectric effect: what the number of photoelectrons is proportional to ::@:: The intensity of the incident light.
- the photoelectric effect: the emission delay ::@:: Photoelectrons are emitted almost instantaneously, independent of light intensity.

<!-- check: ignore-next-line[header_style]: proper noun -->
## Einstein's interpretation

Einstein explained the photoelectric effect by treating light as a stream of photons, each carrying energy $E = hf$, where $h$ is the Planck constant and $f$ is the frequency. A photon transfers all its energy in one collision with an electron in the metal. The electron must overcome the work function $\Phi$, the binding energy holding it in the material, to escape, so the maximum kinetic energy is $K = hf - \Phi$. The threshold frequency is $f_0 = \Phi / h$; below it, $hf < \Phi$ and no electron is ejected.

---

Flashcards for this section are as follows:

- Einstein's photon hypothesis: the energy of a single photon ::@:: $E = hf$, where $h$ is the Planck constant and $f$ is the frequency of the light. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the photoelectric equation: maximum kinetic energy of a photoelectron ::@:: $K = hf - \Phi$, where $\Phi$ is the work function of the material. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the work function $\Phi$: what it represents ::@:: The minimum energy an electron must gain to escape from the surface of the material.
- the threshold frequency: its relation to the work function ::@:: $f_0 = \Phi / h$; below this frequency, no electrons are emitted. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## applications

<!-- check: ignore-next-line[header_style]: proper noun -->
### X-ray photoelectron spectroscopy

X-ray photoelectron spectroscopy (XPS) uses the photoelectric effect to identify the elemental composition of materials. Each element produces characteristic peaks at specific binding energies.

---

Flashcards for this section are as follows:

- XPS: what it measures and how ::@:: The elemental composition of materials, from the binding energies of electrons ejected by X-rays; each element has characteristic peaks.

### charge-coupled device cameras

A CCD sensor consists of millions of tiny pixels, each built around a metal-oxide-semiconductor (MOS) capacitor. Light ejects electrons from a pixel into a potential well created by a gate voltage on the capacitor, and the accumulated charge is proportional to the light intensity. After the exposure, each charge packet travels along a row to a readout amplifier, which converts it to a voltage, like a bucket brigade. This sequential transfer is why the sensor is called charge-coupled. A typical CCD achieves a quantum efficiency of about 70% in the visible range, meaning roughly 70% of incident photons produce a measurable electron.

---

Flashcards for this section are as follows:

- a CCD pixel: the component that traps photoelectrons, and what it records ::@:: A metal-oxide-semiconductor (MOS) capacitor, which creates a potential well that holds the ejected electrons; the accumulated charge is proportional to the light intensity.
- how CCD charges are read out ::@:: Charges are transferred pixel by pixel along rows to a readout amplifier (bucket-brigade readout), where each charge packet is converted to a voltage.
- a typical CCD quantum efficiency in the visible range ::@:: About 70% of incident photons produce a measurable electron.
