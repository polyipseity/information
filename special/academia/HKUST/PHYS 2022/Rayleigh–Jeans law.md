---
aliases:
  - Rayleigh-Jeans law
  - Rayleigh–Jeans
  - Rayleigh–Jeans law
  - classical radiation law
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Rayleigh–Jeans_law
  - language/in/English
---

# Rayleigh–Jeans law

Classical physics predicts the [radiation](black-body%20radiation.md) inside a cavity with the Rayleigh–Jeans law, without assuming anything about quanta. Write $I_\lambda$ for the power a surface radiates per unit area per unit wavelength at temperature $T$. The law is one line long, $I_\lambda = \dfrac{2\pi c k_B T}{\lambda^4}$, and the geometry of the cavity settles everything in it except the average energy of a mode. A mode is one standing-wave pattern the cavity walls allow, each with its own frequency.

---

Flashcards for this section are as follows:

- the Rayleigh–Jeans law in terms of wavelength $\lambda$ and temperature $T$, and what $I_\lambda$ measures ::@:: $I_\lambda = \dfrac{2\pi c k_B T}{\lambda^4}$, proportional to $1/\lambda^4$, where $I_\lambda$ is the power a surface radiates per unit area per unit wavelength at temperature $T$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- a mode of the electromagnetic field, and what one is ::@:: One standing-wave pattern the cavity walls allow, each with its own frequency. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the single number specific to this law, and what it is ::@:: The average energy of a mode, here $k_BT$ for every mode whatever its frequency. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the mean energy this law adds to the cavity geometry it is built on ::@:: Equipartition's $k_BT$ per mode, the value [Planck's law](Planck%27s%20law.md) replaces. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## the mean energy: equipartition

This part of the law is a theorem of the theory of gases, carried over to the modes of the field. Equipartition says that a quadratic degree of freedom carries an average energy of $\tfrac{1}{2}k_BT$, with no dependence on how heavy or stiff the oscillator is.

A harmonic oscillator has two such degrees of freedom, one potential and one kinetic, so a mode of frequency $f$ has average energy $\tfrac{1}{2}k_BT + \tfrac{1}{2}k_BT = k_BT$.

Nothing in that argument separates a mode at frequency $f$ from one at a far higher frequency. Both draw the same $k_BT$.

---

Flashcards for this section are as follows:

- what equipartition assigns to one quadratic degree of freedom, the share $\tfrac{1}{2}k_BT$ ::@:: $\tfrac{1}{2}k_BT$, whatever the mass or stiffness of the oscillator. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the average energy of a mode of frequency $f$ under equipartition ::@:: $k_BT$, from $\tfrac{1}{2}k_BT$ potential and $\tfrac{1}{2}k_BT$ kinetic. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the property of equipartition that causes the failure ::@:: The share is $k_BT$ whatever the frequency $f$, so a high-frequency mode is given as much energy as a low one. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why this average energy is a theorem of classical physics rather than an extra assumption ::@:: It is equipartition from the theory of gases, carried over to the modes of the electromagnetic field. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## the law

The mode density counts how many modes fit in each narrow band of wavelength, and the two solid-angle factors turn a per-volume quantity into a per-area one. Neither is specific to this law. Both belong to the cavity calculation in [mode density of a cavity](mode%20density%20of%20a%20cavity.md). Write $\overline{E}$ for the average energy of a single mode, and the law reads $I_\lambda = \dfrac{2\pi c}{\lambda^4}\overline{E}$. Setting $\overline{E} = k_BT$ gives $I_\lambda = \dfrac{2\pi c k_B T}{\lambda^4}$.

Temperature enters as a linear factor only. Raising it scales the curve at every wavelength by the same proportion and leaves the shape alone, because all the wavelength dependence sits in the mode density $8\pi/\lambda^4$, which the geometry of the box fixes.

---

Flashcards for this section are as follows:

- the mode density and the two solid-angle factors, and where they belong ::@:: A count of how many modes fit in each narrow band of wavelength, plus two solid-angle factors that turn a per-volume quantity into a per-area one; neither is specific to this law, and both belong to the cavity calculation in [mode density of a cavity](mode%20density%20of%20a%20cavity.md). <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the symbol $\overline{E}$ in that chain, and what it measures ::@:: The average energy of a single mode. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what the temperature $T$ does to the shape of the predicted curve ::@:: Nothing; $T$ enters as a linear factor, so raising it scales the curve at every wavelength by the same proportion. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why the shape of the curve is fixed by $1/\lambda^4$ alone ::@:: The mode density $8\pi/\lambda^4$ carries all the wavelength dependence, and it comes from the geometry of the box rather than from the temperature. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## where it fits and where it breaks

The law's accuracy depends on the mean energy. The mode count is correct throughout. Equipartition's $k_BT$ is the right answer only if the steps between neighbouring energy levels are small compared with $k_BT$. A mode of frequency $f$ has steps of size $hf$ in a quantum treatment, so equipartition holds while $hf \ll k_BT$. With $f = c/\lambda$ the condition is a condition on the wavelength, and the law settles down for $\lambda \gg hc/(k_BT) = 1.4388 \times 10^{-2}\ \text{m}\cdot\text{K}/T$, which at $300\ \text{K}$ puts the crossover at about $48\ \mu\text{m}$. A millimetre is already well beyond that, so the law is accurate by the far infrared and fails only as the wavelength approaches the peak.

As $\lambda$ shrinks, $I_\lambda$ grows as $1/\lambda^4$ with no sign of turning over. The measured spectrum peaks and falls steeply toward the ultraviolet instead, so the gap grows without bound. Integrating over all wavelengths gives an infinite total power at any non-zero temperature, the absurdity the [ultraviolet catastrophe](ultraviolet%20catastrophe.md) names.

---

Flashcards for this section are as follows:

- why the accuracy of the law is settled by the mean energy $\overline{E}$ rather than by the mode count ::@:: The count is correct at every wavelength, while equipartition's $k_BT$ is right only while $hf \ll k_BT$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the condition under which equipartition's $k_BT$ is the correct mean energy for a mode of frequency $f$ ::@:: $hf \ll k_BT$, so the steps between energy levels are small compared with the thermal energy. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- that condition rewritten as one on wavelength, using $f = c/\lambda$ ::@:: $\lambda \gg hc/(k_BT) = 1.4388 \times 10^{-2}\ \text{m}\cdot\text{K}/T$, a crossover of about $48\ \mu\text{m}$ at $300\ \text{K}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- where on the spectrum the law agrees with measurement ::@:: The long-wavelength tail, far beyond the peak, where the steps between neighbouring energy levels are small compared with $k_BT$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the total power the law predicts when integrated over all wavelengths ::@:: Infinite, for any non-zero temperature, the absurdity the [ultraviolet catastrophe](ultraviolet%20catastrophe.md) names. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## checking the numbers

At $T = 300\ \text{K}$ the constant is $8\pi k_B T \approx 1.04 \times 10^{-19}\ \text{J}\cdot\text{m}^4$, and it multiplies $1/\lambda^4$ to give the energy density $u_\lambda$, the energy the field holds per unit volume, per unit wavelength. At $\lambda = 1\ \text{mm}$ it is about $1.04 \times 10^{-7}\ \text{J}\,\text{m}^{-4}$. With $c = 3 \times 10^{8}\ \text{m/s}$ the flux works out to $I_\lambda \approx \dfrac{7.80 \times 10^{-12}}{\lambda^4}$ in $\text{W}\,\text{m}^{-3}$, about $7.8\ \text{W/m}^3$ at $1\ \text{mm}$ and about $7.8 \times 10^{8}\ \text{W/m}^3$ at $10^{-5}\ \text{m}$.

How far off that is comes down to one ratio, $x = hc/(\lambda k_BT)$: the energy in one quantum measured against the thermal energy $k_BT$. It is the exponent that appears in [Planck's law](Planck%27s%20law.md). The full Planck result exceeds the classical one by $e^{x}-1$ at short wavelengths, and the classical one exceeds the full result by $\frac{x}{e^{x}-1}$ at long ones. At $300\ \text{K}$ that gives an overestimate of about $2\%$ at $1\ \text{mm}$, a factor of $25$ at $10^{-5}\ \text{m}$, and about $4.5 \times 10^{41}$ at $500\ \text{nm}$.

The mode count is right at $500\ \text{nm}$ as well as at $1\ \text{mm}$, so the geometry is not what failed. The mean energy per mode is. [Planck's law](Planck%27s%20law.md) supplies the replacement, $E(f) = \dfrac{hf}{e^{hf/(k_BT)} - 1}$, and it reduces to $k_BT$ as $hf/(k_BT) \to 0$, since $e^{hf/(k_BT)} - 1 \approx hf/(k_BT)$ there.

---

Flashcards for this section are as follows:

- the energy density $u_\lambda$ at $T = 300\ \text{K}$, and what the quantity is ::@:: The energy the field holds per unit volume per unit wavelength; $u_\lambda = \dfrac{8\pi k_B T}{\lambda^4}$ with $8\pi k_B T \approx 1.04 \times 10^{-19}\ \text{J}\cdot\text{m}^4$, so at $\lambda = 1\ \text{mm}$ it is about $1.04 \times 10^{-7}\ \text{J}\,\text{m}^{-4}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the flux at $T = 300\ \text{K}$, as a function of $\lambda$ ::@:: $I_\lambda \approx \dfrac{7.80 \times 10^{-12}}{\lambda^4}$ in $\text{W}\,\text{m}^{-3}$, about $7.8\ \text{W/m}^3$ at $1\ \text{mm}$ and about $7.8 \times 10^{8}\ \text{W/m}^3$ at $10^{-5}\ \text{m}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the ratio $x$ that measures the distance from the classical limit, and its definition ::@:: $x = hc/(\lambda k_BT)$, the energy in one quantum against the thermal energy $k_BT$, and the exponent that appears in [Planck's law](Planck%27s%20law.md). <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the classical overestimate at $T = 300\ \text{K}$ at $1\ \text{mm}$, at $10^{-5}\ \text{m}$ and at $500\ \text{nm}$ ::@:: About $2\%$ at $1\ \text{mm}$, where $x \approx 0.048$; a factor of $25$ at $10^{-5}\ \text{m}$, where $x \approx 4.8$; and about $4.5 \times 10^{41}$ at $500\ \text{nm}$, where $x \approx 96$ and $e^{x}-1 \approx e^{96}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- which law assumes the opposite about a mode's mean energy, and is right where this one is wrong ::@:: The [Wien approximation](Wien%20approximation.md). <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what follows from each classical law being right where the other fails ::@:: The mode density is sound and was left unchanged, so the mean energy per mode is the assumption at fault. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the replacement for the equipartition mean energy, and the limit in which it returns the classical one ::@:: $E(f) = \dfrac{hf}{e^{hf/(k_BT)} - 1}$, from [Planck's law](Planck%27s%20law.md), and for $hf \ll k_BT$ it gives $k_BT$ because $e^{hf/(k_BT)} - 1 \approx hf/(k_BT)$ there. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
