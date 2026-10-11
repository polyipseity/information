---
aliases:
  - pyrometer
  - radiation thermometer
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/pyrometer
  - language/in/English
---

# pyrometer

A _pyrometer_ reads a body's temperature from a distance, from the thermal radiation the body itself emits. Nothing touches the body and nothing is embedded in it. The technique is pyrometry, a branch of radiometry, and [thermal radiation](thermal%20radiation.md) is the signal it runs on.

The reading rests on black-body physics. A [black body](black-body%20radiation.md) radiates a spectrum fixed by temperature alone, so a measured radiance returns a temperature with no assumption about the material behind it. The small hole in a heated cavity is the calibration ideal: it radiates exactly the black-body spectrum at the cavity's temperature, and instruments are compared against that.

---

Flashcards for this section are as follows:

- overview: what a pyrometer does ::@:: It reads a body's temperature from a distance, from the thermal radiation the body emits, with no contact and no embedded sensor.
- the technique of reading a temperature off emitted thermal radiation ::@:: Pyrometry, a branch of radiometry; the pyrometer is its instrument.
- what makes a radiation temperature reading possible at all ::@:: A black body's spectrum is fixed by temperature alone, so a measured radiance returns a temperature without contact or material knowledge.
- the calibration ideal behind pyrometer readings ::@:: The small hole in a heated cavity, which radiates exactly the black-body spectrum at the cavity's temperature.

## reading a temperature

Three parts of one curve give three designs. A brightness pyrometer measures the radiance $B_\lambda$ at a single wavelength and inverts [Planck's law](Planck's%20law.md) for $T$. A total-radiation pyrometer collects the emitted power over a wide band and reads it through the Stefan–Boltzmann law $R = \sigma T^4$. A third reads the peak: put the measured $\lambda_{\max}$ into [Wien's displacement law](Wien's%20displacement%20law.md), $\lambda_{\max}T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$, and $T$ follows.

The [infrared thermometer](infrared.md) that reads a person's temperature near the $9\ \mu\text{m}$ peak of body radiation belongs to the same family. It works where the eye does not reach, which is most of the temperature range: only roughly $3000$ to $8000\ \text{K}$ puts a black-body peak inside the visible.

---

Flashcards for this section are as follows:

- overview: the three ways a pyrometer turns emitted radiation into a temperature ::@:: Radiance at one wavelength inverted through Planck's law; collected power read through $R = \sigma T^4$; and the measured peak wavelength $\lambda_{\max}$ put into Wien's displacement law. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- brightness pyrometry: what is measured and what it is inverted through ::@:: The spectral radiance $B_\lambda$ at a single wavelength, inverted through Planck's law to give $T$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- total-radiation pyrometry: what is measured and the law it is read through ::@:: The emitted power collected over a wide band, read through the Stefan–Boltzmann law $R = \sigma T^4$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the route Wien's displacement law $\lambda_{\max}T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$ offers a pyrometer ::@:: Measure where the emitted spectrum peaks and solve for $T$.
- where an infrared thermometer sits in the pyrometer family ::@:: It is one member, reading near the $9\ \mu\text{m}$ peak of body radiation, in the infrared the eye cannot see. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## emissivity

A real surface is not a perfect black body, so its emissivity $\varepsilon$ sits below $1$ and the instrument's black-body scale has to be corrected by it. Reading the surface as a black body underestimates the temperature, since a surface of emissivity $\varepsilon$ radiates less than a black body at the same temperature. Near room temperature two errors dominate: radiation from hotter surroundings reflected into the instrument, and an emissivity assumed wrongly.

---

Flashcards for this section are as follows:

- the correction a real surface asks of a pyrometer reading ::@:: Its emissivity $\varepsilon$, below $1$ for a real surface, since the instrument's scale is the black-body one. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what reading an emissivity-$\varepsilon$ surface as a black body does to the temperature it reports ::@:: It underestimates it, because such a surface radiates less than a black body at the same temperature.
- the two dominant error sources for a pyrometer near room temperature ::@:: Radiation from hotter surroundings reflected into the instrument, and an emissivity assumed wrongly.
