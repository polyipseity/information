---
aliases:
  - Rayleigh-Jeans catastrophe
  - ultraviolet catastrophe
  - ultraviolet divergence
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/ultraviolet_catastrophe
  - language/in/English
---

# ultraviolet catastrophe

Classical statistical mechanics predicted an infinite radiated power. Write $I_\lambda$ for the power a surface radiates per unit area per unit wavelength. Integrated over every wavelength, it is infinite at any temperature above absolute zero. The divergence belongs to the 1900 prediction, and Paul Ehrenfest supplied the name in 1911.

A mode is one standing wave pattern inside the cavity, and $k_B$ is the Boltzmann constant. One narrow assumption produces the divergence: every mode holds the equipartition share $k_BT$ whatever its frequency, the energy classical physics assigns to such a pattern at absolute temperature $T$.

---

Flashcards for this section are as follows:

- the one assumption the failure rests on ::@:: that every mode holds the equipartition share $k_BT$ whatever its frequency. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what a mode is here, and what $k_BT$ is ::@:: A mode is one standing wave pattern inside the cavity; $k_B$ is the Boltzmann constant, so $k_BT$ is the energy classical physics assigns to such a pattern at absolute temperature $T$.
- who named the failure and when, against when the divergence itself appeared ::@:: Ehrenfest named it in 1911; the divergence belongs to the 1900 prediction, so the name came after the result.

## a divergence, not a discrepancy

An ordinary discrepancy between theory and measurement stays finite. Two curves can differ by a factor of two at one wavelength. Both remain finite there, and a fit absorbs the disagreement into a parameter. A divergence is different in kind: the predicted quantity has no value to stand against the measurement, so no adjustment of anything measurable closes the gap.

---

Flashcards for this section are as follows:

- what makes this failure different in kind from an ordinary theory-measurement discrepancy ::@:: The predicted quantity is infinite where the measurement is finite, so there is no value to compare and no parameter to absorb the disagreement.

## the two classical laws, and the gap in the infrared

Both classical laws are wrong, and they are wrong in opposite directions. The [Rayleigh–Jeans law](Rayleigh%E2%80%93Jeans%20law.md) holds at long wavelengths, where it gives $I_\lambda = 2\pi c k_B T/\lambda^4$, a number that diverges as $\lambda \to 0$ and never turns over. The [Wien approximation](Wien%20approximation.md) holds at short wavelengths, where it gives $I_\lambda = 2hc^2 e^{-hc/(\lambda k_BT)}/\lambda^5$, which vanishes there. Between them, across the [infrared](infrared.md), sits a gap where neither is reliable.

The Wien error is bounded: its predicted $I_\lambda$ stays a finite number at every wavelength, and it misses by a factor of twenty or more in places, which is severe but not absurd. The Rayleigh–Jeans law misses by an infinite factor, and only that one earns the name.

The ultraviolet sat in a poorly measured part of the spectrum in the 1890s, so on its own a divergence there could have been written off as an experimental gap. The well-measured infrared removed that excuse. The law had to be exactly right about the shape of the well-measured tail to be wrong about the peak, and no reasonable choice of constants could do both.

---

Flashcards for this section are as follows:

- the value $I_\lambda$ the [Rayleigh–Jeans law](Rayleigh%E2%80%93Jeans%20law.md) predicts, and what it does as $\lambda \to 0$ ::@:: $I_\lambda = 2\pi c k_B T/\lambda^4$, which diverges with no maximum to compare it against.
- the value $I_\lambda$ the [Wien approximation](Wien%20approximation.md) predicts, and what it does as $\lambda \to 0$ ::@:: $I_\lambda = 2hc^2 e^{-hc/(\lambda k_BT)}/\lambda^5$, which vanishes.
- which range neither classical law covers reliably ::@:: The [infrared](infrared.md), lying between the long-wavelength Rayleigh–Jeans limit and the short-wavelength Wien limit.
- which of the two classical laws earns the name ultraviolet catastrophe, and whether the other's error is bounded ::@:: The [Rayleigh–Jeans law](Rayleigh%E2%80%93Jeans%20law.md) earns it, since it misses by an infinite factor; the Wien error stays finite, missing by a factor of twenty or more in places.
- why a divergence in the poorly measured ultraviolet could not be written off as an experimental gap ::@:: Because the well-measured infrared tail had to be fitted exactly right for the law to reach the ultraviolet, and no reasonable choice of constants could do both.

## how wrong the classical law gets

One number measures the distance between the two limits: $x = hc/(\lambda k_BT)$, the energy of one quantum $hf$ at this wavelength divided by the thermal energy $k_BT$. A small $x$ means the classical law is nearly right; a large one means it is far out. At $500\ \text{nm}$ and $300\ \text{K}$, $x \approx 96$, so $e^{x}-1 \approx e^{96} \approx 4.5 \times 10^{41}$, and the classical law overestimates the true $I_\lambda$ by that factor. At the other end, $\lambda = 10^{-5}\ \text{m}$ with $300\ \text{K}$ gives $x \approx 4.8$ and $x/(e^{x}-1) \approx 0.040$, a factor of about $25$.

---

Flashcards for this section are as follows:

- the ratio $x$, and what it measures ::@:: $x = hc/(\lambda k_BT)$, the energy of one quantum $hf$ at that wavelength divided by the thermal energy $k_BT$, so a small $x$ is near the classical limit and a large one is far from it.
- the classical overestimate at $T = 300\ \text{K}$ and $\lambda = 500\ \text{nm}$ ::@:: $x \approx 96$, so $e^{x}-1 \approx e^{96} \approx 4.5 \times 10^{41}$.
- the classical overestimate at $T = 300\ \text{K}$ and $\lambda = 10^{-5}\ \text{m}$ ::@:: $x \approx 4.8$, giving $x/(e^{x}-1) \approx 0.040$, a factor of about $25$.

## the mode count is not to blame

The tempting repair keeps the equipartition share and fixes the mode density instead. Since the divergence sits where there is very little energy anyway, the argument puts the fault in the $1/\lambda^4$.

But the mode density is not a free parameter. Write $n(\lambda)$ for the count, the number of modes per unit volume of cavity per unit wavelength. It comes to $n(\lambda) = 8\pi/\lambda^4$, and that is a plain count: how many standing waves of a given wavelength a box of a given size admits. It carries no assumption about energy, and direct experiment confirms it by counting the modes in a cavity. Any change large enough to tame the ultraviolet would spoil a number that is already right, and [Planck's law](Planck%27s%20law.md) keeps that same count.

---

Flashcards for this section are as follows:

- the tempting repair, and the argument behind it ::@:: Modify the mode density rather than the mean energy, on the grounds that the divergence sits where there is very little energy anyway.
- what $n(\lambda)$ counts, and its value ::@:: The number of modes per unit volume of cavity per unit wavelength, $n(\lambda) = 8\pi/\lambda^4$.
- why the mode count is not available as a free parameter ::@:: It is a plain count of standing waves carrying no energy assumption, confirmed by the number of modes in a cavity, so any change large enough to tame the ultraviolet would spoil a number that is already right, and it is the count [Planck's law](Planck%27s%20law.md) keeps.

## two constraints on the mean energy

With the mode count ruled out, the freedom that remains sits in the mean energy. The mean energy must approach $k_BT$ in the long-wavelength limit, where the law works and the measurement agrees. It must also suppress the short-wavelength end, where the divergence is. Both requirements fall on the same function, and no continuous function of frequency meets both as long as the average is a classical one.

The size of the suppression rules out a gentle fix. At $500\ \text{nm}$ and $300\ \text{K}$ the exponential factor is about $e^{-96}$, a fall by a factor of $10^{41}$ or so from the long-wavelength value of $k_BT$. Only a mechanism that discards energy in lumps can do that, and a classical oscillator has none. The required change is a jump, and no adjustment of a continuous parameter supplies one.

Planck's resolution was a change in the set of values an oscillator is allowed to take, not a better function. A mode of frequency $f$ may hold only $0, hf, 2hf, 3hf, \ldots$, each step one quantum of energy $hf$. The average then becomes a sum over integers weighted by $e^{-nhf/(k_BT)}$ instead of an integral over continuous energies. That sum has the closed form $\dfrac{hf}{e^{hf/(k_BT)} - 1}$, evaluated in [Planck's law](Planck%27s%20law.md). What matters here is what the sum does at each end. It reduces to $k_BT$ when $hf \ll k_BT$, the long-wavelength constraint, and to $hf\,e^{-hf/(k_BT)}$ when $hf \gg k_BT$, the suppression the short-wavelength end demands. One expression meets both constraints that no continuous function could.

The mean energy falls as an exponential in the frequency, and $I_\lambda$ acquires the $e^{-hc/(\lambda k_BT)}$ factor that turns a $1/\lambda^4$ rise into a curve with a maximum. The ultraviolet divergence is gone: the exponential beats every power of $\lambda$. The mode count, the cavity geometry and the Boltzmann weights from statistical mechanics stay as they were.

---

Flashcards for this section are as follows:

- the two constraints on the mean energy of a mode of frequency $f$ ::@:: It must approach $k_BT$ for $hf \ll k_BT$, and must suppress $I_\lambda$ for $hf \gg k_BT$.
- the suppression factor required at $500\ \text{nm}$ and $300\ \text{K}$ ::@:: About $e^{-96}$, a fall by a factor of $10^{41}$ or so from the long-wavelength value of $k_BT$.
- why no adjustment of a continuous classical parameter can supply that suppression ::@:: The required change is a jump rather than a slope, and a classical oscillator has no mechanism that discards energy in lumps.
- the change in the allowed energies of an oscillator, and the thermal sum it produces ::@:: Only $0, hf, 2hf, 3hf, \ldots$, so the average is a sum over integers with weights $e^{-nhf/(k_BT)}$ rather than an integral over continuous energies, and that sum has the closed form $\dfrac{hf}{e^{hf/(k_BT)} - 1}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the two limits of that expression, and the classical law each recovers ::@:: $k_BT$ for $hf \ll k_BT$ gives the [Rayleigh–Jeans law](Rayleigh%E2%80%93Jeans%20law.md); $hf\,e^{-hf/(k_BT)}$ for $hf \gg k_BT$ gives the [Wien approximation](Wien%20approximation.md). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- what Planck left untouched ::@:: The mode count, the cavity geometry and the Boltzmann weights from statistical mechanics.
- the factor that turns a rising $1/\lambda^4$ $I_\lambda$ into a curve with a maximum, and why it removes the divergence ::@:: $e^{-hc/(\lambda k_BT)}$, since an exponential beats every power of $\lambda$.
