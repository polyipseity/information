---
aliases:
  - photoelectric effect
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/photoelectric_effect
  - language/in/English
---

# photoelectric effect

The photoelectric effect is the emission of electrons from a material when light of sufficient frequency shines on it. It established the particle nature of light and led to Einstein's photon hypothesis.

---

Flashcards for this section are as follows:

- the photoelectric effect: what it is ::@:: The emission of electrons from a material when light of sufficient frequency shines on it.

## historical background

In 1887, Heinrich Hertz used a spark gap to detect electromagnetic waves and noticed that the detector spark became more vigorous under ultraviolet light. In 1888, Wilhelm Hallwachs confirmed that UV light on a zinc plate generated positive charges through electron emission. By 1898, J. J. Thomson found that the number of emitted electrons varied with UV intensity. Philipp Lenard studied the effect in 1902, measuring how kinetic energy and electron count depended on light intensity and frequency.

---

Flashcards for this section are as follows:

- Hertz's observation: what he noticed about the spark gap under UV light ::@:: The small detector spark became more vigorous when exposed to ultraviolet light.
- Hallwachs's confirmation: what UV light on a zinc plate produced ::@:: Positive charges, due to electron emission.
- Lenard's systematic study: what he measured ::@:: The dependence of kinetic energy and the number of emitted electrons on the intensity and frequency of incident light.

## experimental setup

The standard apparatus uses a vacuum tube with a metallic emitter electrode and a collector electrode. Incident light strikes the emitter, ejecting electrons that travel to the collector. A variable voltage supply and ammeter allow measurement of the electron current and the stopping potential needed to halt the most energetic photoelectrons.

Different metals have different work functions, the minimum energy needed to free an electron from the surface. Typical values are sodium (Na) at about 2.3 eV, zinc (Zn) at about 4.3 eV, copper (Cu) at about 4.7 eV, and platinum (Pt) at about 6.35 eV. A retarding (negative) voltage applied to the collector repels the emitted electrons. At the stopping potential $V_s$, even the most energetic electrons are turned back, so the current drops to zero. The stopping potential gives the maximum kinetic energy directly: $KE_{\text{max}} = eV_s$.

---

Flashcards for this section are as follows:

- the photoelectric experiment: the two measurable quantities ::@:: The kinetic energy of the emitted electrons (via stopping potential) and the number of emitted electrons (via photocurrent).
- the work function: what it is and how it differs among materials ::@:: The minimum energy needed to free an electron from the surface; sodium is about 2.3 eV, zinc about 4.3 eV, copper about 4.7 eV, platinum about 6.35 eV.
- the stopping potential: what it gives directly ::@:: The maximum kinetic energy of the photoelectrons, through $KE_{\text{max}} = eV_s$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## classical predictions

Classical wave theory predicted that the kinetic energy of photoelectrons should depend on light intensity, that the number of photoelectrons should depend on frequency, and that at very low intensities there should be a measurable waiting time before any electron could escape.

---

Flashcards for this section are as follows:

- classical prediction for kinetic energy: what it depends on ::@:: Light intensity (stronger light gives more energy to electrons).
- classical prediction for electron count: what it depends on ::@:: Frequency of the light.
- classical prediction at low intensity: what should happen ::@:: A measurable waiting time before any electron escapes.

## experimental results

The actual results contradicted every classical prediction. The kinetic energy of photoelectrons is independent of light intensity. The maximum kinetic energy depends only on the frequency of the light, not its intensity. Each material has a threshold frequency below which no electrons are emitted, regardless of intensity. The number of photoelectrons is proportional to light intensity. Electrons are emitted almost instantaneously, even at very low intensities.

---

Flashcards for this section are as follows:

- the photoelectric effect: what determines the maximum kinetic energy of photoelectrons ::@:: The frequency of the incident light, not its intensity.
- the threshold frequency: what it means and what it depends on ::@:: The minimum frequency below which no electrons are emitted; it depends on the material's work function.
- the photoelectric effect: what the number of photoelectrons is proportional to ::@:: The intensity of the incident light.
- the photoelectric effect: the emission delay ::@:: Photoelectrons are emitted almost instantaneously, independent of light intensity.

<!-- check: ignore-next-line[header_style]: proper noun -->
## Einstein's interpretation

Einstein explained the photoelectric effect by treating light as a stream of photons, each carrying energy $E = hf$, where $h$ is the Planck constant and $f$ is the frequency. When a photon collides with an electron in the metal, it transfers all its energy. The electron must overcome the work function $\Phi$ (the binding energy holding it in the material) to escape. The maximum kinetic energy of the emitted electron is $K = hf - \Phi$. If $hf < \Phi$, no electron can be ejected.

---

Flashcards for this section are as follows:

- Einstein's photon hypothesis: the energy of a single photon ::@:: $E = hf$, where $h$ is the Planck constant and $f$ is the frequency of the light. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the photoelectric equation: maximum kinetic energy of a photoelectron ::@:: $K = hf - \Phi$, where $\Phi$ is the work function of the material. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the work function $\Phi$: what it represents ::@:: The minimum energy an electron must gain to escape from the surface of the material.
- the threshold frequency: its relation to the work function ::@:: $f_0 = \Phi / h$; below this frequency, no electrons are emitted. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why increasing light intensity increases photocurrent but not kinetic energy ::@:: More photons means more electrons ejected (proportional to intensity), but each photon's energy depends only on frequency.

## applications

<!-- check: ignore-next-line[header_style]: proper noun -->
### X-ray photoelectron spectroscopy

X-ray photoelectron spectroscopy (XPS) uses the photoelectric effect to identify the elemental composition of materials. Each element produces characteristic peaks at specific binding energies, making XPS an important experimental technique for surface analysis.

---

Flashcards for this section are as follows:

- XPS: what it measures and how ::@:: The elemental composition of materials by measuring the binding energies of electrons ejected by X-rays; each element has characteristic peaks.

### charge-coupled device cameras

A CCD sensor consists of millions of tiny pixels, each built around a metal-oxide-semiconductor (MOS) capacitor. When light strikes a pixel, the photoelectric effect ejects electrons, which are trapped in a potential well created by a gate voltage applied to the capacitor. The accumulated charge at each pixel is proportional to the light intensity during the exposure. After the exposure, the charges are transferred pixel by pixel along rows to a readout amplifier, like a bucket brigade, where each charge packet is converted to a voltage and digitised. This sequential readout is why CCDs are called charge-coupled devices. A typical CCD achieves a quantum efficiency of about 70% in the visible range, meaning roughly 70% of incident photons produce a measurable electron.

---

Flashcards for this section are as follows:

- CCD sensors: how they use the photoelectric effect ::@:: Light ejects electrons from pixels, and the accumulated charge at each pixel is proportional to light intensity, forming a digital image.
- the CCD pixel: the component that traps photoelectrons ::@:: A metal-oxide-semiconductor (MOS) capacitor, which creates a potential well that holds the ejected electrons.
- how CCD charges are read out ::@:: Charges are transferred pixel by pixel along rows to a readout amplifier (bucket-brigade readout), where each charge packet is converted to a voltage.
- a typical CCD quantum efficiency in the visible range ::@:: About 70% of incident photons produce a measurable electron.
