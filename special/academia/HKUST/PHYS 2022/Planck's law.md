---
aliases:
  - Planck radiation law
  - Planck's law
  - Planck's wavelength distribution function
  - black-body spectrum formula
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Planck_s_law
  - language/in/English
---

# Planck's law

_Planck's law_ gives the spectrum of the radiation inside a [black body](black-body%20radiation.md) at a temperature $T$: energy per unit area, per unit time, per unit wavelength, per steradian, which is the spectral radiance $B_\lambda$. The standard form is $B_\lambda(T) = \dfrac{2hc^2}{\lambda^5}\,\dfrac{1}{e^{hc/(\lambda k_BT)} - 1}$. Any cavity at the same temperature radiates that same curve, whatever its walls are made of.

Here $h$ is Planck's constant and $c$ the speed of light. $k_B$ is the Boltzmann constant, the same constant that fixes the mean kinetic energy of a molecule in the [kinetic theory of gases](kinetic%20theory%20of%20gases.md).

Two laws came before it, each failing on half the spectrum. The Rayleigh–Jeans law rests on equipartition: it matched the measurements at long wavelengths and ran away at short ones, predicting a divergent $I_\lambda$ in the ultraviolet. Wien's distribution law was put forward on semi-empirical grounds, and it matched the ultraviolet while failing at long wavelengths. The three are the same calculation with one number changed, the average energy a single mode holds, written $E(f)$ for a mode of frequency $f$.

A cavity of a fixed size holds a fixed number of modes per unit volume per unit wavelength: the mode density $n(\lambda) = 8\pi/\lambda^4$. Multiplying it by the mean energy gives the energy density $u_\lambda$, the energy per unit volume per unit wavelength. Two solid-angle factors carry that out to a surface, first to the radiance $B_\lambda$ and then to the flux $I_\lambda$, the power per unit area per unit wavelength leaving a surface, with $I_\lambda = \frac{1}{4}c\,u_\lambda$. Both factors are derived in [mode density of a cavity](mode%20density%20of%20a%20cavity.md).

---

Flashcards for this section are as follows:

- overview: what Planck's law gives for a black body at temperature $T$ ::@:: The spectrum of the radiation: energy per unit area, per unit time, per unit wavelength, per steradian, which is the spectral radiance $B_\lambda$.
- Planck's law in its standard form, in terms of $\lambda$, $T$, $h$, $c$, and $k_B$ ::@:: $B_\lambda(T) = \dfrac{2hc^2}{\lambda^5}\,\dfrac{1}{e^{hc/(\lambda k_BT)} - 1}$.
- what the symbols $h$, $c$, and $k_B$ in Planck's law stand for ::@:: $h$ is Planck's constant, $c$ is the speed of light, and $k_B$ is the Boltzmann constant, the same constant that fixes the mean kinetic energy of a molecule in the kinetic theory of gases.
- what Planck's law predicts about two black bodies at the same temperature ::@:: That they radiate identical spectra, whatever their walls are made of.
- the two laws Planck's law replaced, the half of the spectrum each matched, and what the Rayleigh–Jeans law predicts for $I_\lambda$ at short wavelengths ::@:: Rayleigh–Jeans matched the long wavelengths and predicts a divergent $I_\lambda$ in the ultraviolet; Wien's distribution law was put forward on semi-empirical grounds, matched the ultraviolet, and failed at long wavelengths.
- overview: the one factor in which the three laws differ, and what the other factors measure ::@:: Only the average energy $E(f)$ a single mode holds. The rest is common: the mode density $n(\lambda) = 8\pi/\lambda^4$ counts modes per unit volume per unit wavelength, multiplying it by the mean energy gives the energy density $u_\lambda$, and the two solid-angle factors carry that out to the flux $I_\lambda$, derived in full in [mode density of a cavity](mode%20density%20of%20a%20cavity.md). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- overview: the two relations $u_\lambda = n(\lambda)\,E(f)$ and $I_\lambda = \frac{1}{4}c\,u_\lambda$ that start the calculation, and what each quantity in them measures ::@:: The energy density $u_\lambda$ is energy per unit volume per unit wavelength, and the flux $I_\lambda$ is power per unit area per unit wavelength leaving a surface.
- why a quoted prefactor such as $2hc^2/\lambda^5$ cannot be read on its own, and which quantity carries which prefactor ::@:: The quantity has to be named: spectral radiance per unit wavelength carries $2hc^2/\lambda^5$, and energy density per unit wavelength carries $8\pi hc/\lambda^5$ for the same curve.

## the two modifications

Planck took the radiation in the cavity to be emitted and absorbed by oscillators in the walls, then applied Boltzmann's statistical method to them. Two modifications take that outside classical physics.

The first is the set of energies an oscillator of frequency $f$ may hold, which is discrete: $E_n = nhf$, where $n$ is an integer.

The constant that sets the size of a quantum is $h = 6.6261 \times 10^{-34}\ \text{J}\cdot\text{s}$, the value accepted today. Planck's own first calculation gave $6.55 \times 10^{-27}\ \text{erg}\cdot\text{s}$, which is $1.15$ percent below the modern value, and he called the constant the elementary quantum of action. See [Max Planck](Max%20Planck.md).

The second modification is that the oscillators absorb and emit only in multiples of the fundamental quantum, $\Delta E = hf$. It follows from the first: discrete levels have discrete gaps, and a drop of one step carries exactly $hf$.

Together they remove the continuous exchange that equipartition needs, and with it the result $\tfrac{1}{2}k_BT$ per degree of freedom. The mode count does not change: counting standing waves and shells assumes nothing about how the energy inside a mode is distributed.

---

Flashcards for this section are as follows:

- what Planck assumed the radiation in the cavity was emitted and absorbed by ::@:: Oscillators in the walls of the cavity.
- Planck's first modification: the energies an oscillator of frequency $f$ may hold ::@:: Only the discrete values $E_n = nhf$, where $n$ is an integer, so an oscillator carries $0$, $1$, $2$, $3, \ldots$ quanta and nothing between.
- the value of Planck's constant $h$ ::@:: $6.6261 \times 10^{-34}\ \text{J}\cdot\text{s}$, the value accepted today. Planck's own first calculation gave $6.55 \times 10^{-27}\ \text{erg}\cdot\text{s}$, which is $1.15$ percent lower, and he called it the elementary quantum of action; see [Max Planck](Max%20Planck.md).
- Planck's second modification: the size of each exchange, in terms of the oscillator frequency $f$ and the constant $h$ ::@:: $\Delta E = hf$, the fundamental quantum.
- why the second modification follows from the ladder $E_n = nhf$ ::@:: The gaps between discrete levels are discrete, and a drop of one step carries exactly $hf$.
- what equipartition gives per degree of freedom at temperature $T$, and what the two modifications take away from it ::@:: $\tfrac{1}{2}k_BT$, which needs continuous states and continuous exchange.
- which factor of $u_\lambda = n(\lambda)E(f)$ Planck's two modifications change, and why the mode count is not that factor ::@:: The mean energy $E(f)$. The mode density $n(\lambda) = 8\pi/\lambda^4$ stays the classical count, because counting standing waves and shells assumes nothing about how the energy inside a mode is distributed.

## the mean energy of a quantised oscillator

An oscillator of frequency $f$ in level $n$ carries a Boltzmann weight $e^{-nhf/(k_BT)}$. The mean energy is a sum of energies over a sum of weights, $E(f) = \dfrac{\sum_{n} n\,hf\,e^{-nhf/(k_BT)}}{\sum_{n} e^{-nhf/(k_BT)}}$.

Write $z = e^{-hf/(k_BT)}$, so that $z$ is the Boltzmann factor for one step up and the weight of level $n$ is $z^n$. Both sums are then geometric, with $\sum_{n} z^n = \dfrac{1}{1-z}$ and $\sum_{n} n z^n = \dfrac{z}{(1-z)^2}$, and the ratio is $E(f) = hf\,\dfrac{z/(1-z)^2}{1/(1-z)} = \dfrac{hf\,z}{1-z} = \dfrac{hf}{e^{hf/(k_BT)} - 1}$.

It falls back to $k_BT$ only when $hf$ is small compared with $k_BT$.

---

Flashcards for this section are as follows:

- the mean energy $E(f)$ of an oscillator of frequency $f$ at temperature $T$, as a sum over weights ::@:: $E(f) = \dfrac{\sum_{n} n\,hf\,e^{-nhf/(k_BT)}}{\sum_{n} e^{-nhf/(k_BT)}}$, a sum of energies over a sum of Boltzmann weights.
- the substitution $z = e^{-hf/(k_BT)}$ that turns the sum into a geometric series ::@:: $z$ is the Boltzmann factor for one step up, so the weight of level $n$ is $z^n$ and both sums become geometric in $z$.
- the two geometric-series identities in $z$ ::@:: $\sum_{n} z^n = \dfrac{1}{1-z}$ and $\sum_{n} n z^n = \dfrac{z}{(1-z)^2}$.
- the mean energy $E(f)$ after the two sums are collapsed ::@:: $hf\,\dfrac{z/(1-z)^2}{1/(1-z)} = \dfrac{hf\,z}{1-z} = \dfrac{hf}{e^{hf/(k_BT)} - 1}$.
- the limit in which this mean energy equals the equipartition share $k_BT$ ::@:: Where the lowest step $hf$ is small compared with $k_BT$, where $E(f) \to k_BT$.

## assembling the law

The mode density times that mean energy gives the energy density, $u_\lambda = \dfrac{8\pi}{\lambda^4}\cdot\dfrac{hc/\lambda}{e^{hc/(\lambda k_BT)} - 1} = \dfrac{8\pi hc}{\lambda^5}\,\dfrac{1}{e^{hc/(\lambda k_BT)} - 1}$, with $f = c/\lambda$ turning $hf$ into $hc/\lambda$.

The radiance follows from that, $B_\lambda = \frac{c}{4\pi}u_\lambda = \dfrac{2hc^2}{\lambda^5}\,\dfrac{1}{e^{hc/(\lambda k_BT)} - 1}$.

The constant is not a convention. The mode count gives $8\pi$, the mean energy $hc$, and the radiance conversion $c$ over $4\pi$, so $8\pi \times hc \times \frac{c}{4\pi} = 2hc^2$. Quoted the same curve as an energy density, the prefactor is $8\pi hc$ instead.

Swap the mean energy back to the equipartition value $k_BT$ and the same chain returns the [Rayleigh–Jeans law](Rayleigh%E2%80%93Jeans%20law.md) exactly, with the mode count and both solid-angle factors untouched.

---

Flashcards for this section are as follows:

- the energy density $u_\lambda$ from the mode density and that mean energy ::@:: $u_\lambda = \dfrac{8\pi}{\lambda^4}\cdot\dfrac{hc/\lambda}{e^{hc/(\lambda k_BT)} - 1} = \dfrac{8\pi hc}{\lambda^5}\,\dfrac{1}{e^{hc/(\lambda k_BT)} - 1}$, using $f = c/\lambda$.
- the radiance $B_\lambda = \frac{c}{4\pi}u_\lambda$ obtained from that energy density, and the prefactor it carries ::@:: $B_\lambda = \frac{c}{4\pi}u_\lambda = \dfrac{2hc^2}{\lambda^5}\,\dfrac{1}{e^{hc/(\lambda k_BT)} - 1}$, the form quoted at the start.
- where the constant $2hc^2$ comes from, and whether it can be chosen ::@:: It cannot be chosen. The mode count gives $8\pi$, the mean energy gives $hc$, and the radiance conversion gives $c/(4\pi)$, so $8\pi \times hc \times \frac{c}{4\pi} = 2hc^2$; quoted as an energy density the prefactor is $8\pi hc$ instead, with the argument unchanged.
- the law that comes out of the classical mode density $n(\lambda) = 8\pi/\lambda^4$ with an equipartition mean energy $k_BT$ ::@:: The Rayleigh–Jeans law, with the mode count and both solid-angle factors untouched.

## the two limits

At long wavelengths $hf/(k_BT)$ is small, so $e^{hf/(k_BT)} - 1 \approx hf/(k_BT)$ and the mean energy per mode goes to $k_BT$. The law then gives $I_\lambda = \dfrac{2\pi c k_BT}{\lambda^4}$, the Rayleigh–Jeans law.

At short wavelengths $hf/(k_BT)$ is large and the $1$ in the denominator is negligible against the exponential, so the law falls off as $e^{-hc/(\lambda k_BT)}$, the Wien form. Dropping the exponential is what produces the ultraviolet catastrophe.

Integrating the law over all wavelengths gives a total power proportional to $T^4$, the [Stefan–Boltzmann law](Stefan–Boltzmann%20law.md).

---

Flashcards for this section are as follows:

- what $u_\lambda = n(\lambda)E(f)$ gives at long wavelengths, with $n(\lambda) = 8\pi/\lambda^4$ ::@:: $u_\lambda = \dfrac{8\pi k_BT}{\lambda^4}$, which becomes $I_\lambda = \dfrac{2\pi c k_BT}{\lambda^4}$ after the two solid-angle factors: the Rayleigh–Jeans law.
- the short-wavelength limit, in terms of the denominator $e^{hc/(\lambda k_BT)} - 1$ ::@:: The $1$ becomes negligible against the exponential, and the law falls off as $e^{-hc/(\lambda k_BT)}$ in the Wien form.
- the ultraviolet catastrophe against Planck's short-wavelength limit ::@:: The exponential suppresses the ultraviolet, where Rayleigh–Jeans diverged; the divergence was an artefact of dropping the exponential.
- the total power the law implies, and the law that names it ::@:: Integrating over all wavelengths gives the $T^4$ of the [Stefan–Boltzmann law](Stefan–Boltzmann%20law.md). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## the cosmic microwave background

The cosmic microwave background, radiation left over from the hot early universe, is the curve to test. It is a black body at $2.73\ \text{K}$, peaking at $\lambda_{\max} = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}/T \approx 1.06\ \text{mm}$ by the [Wien's displacement law](Wien's%20displacement%20law.md).

That peak is not in the Rayleigh–Jeans limit: there $hc/(\lambda k_BT) \approx 4.97$, and the classical law is high by a factor of about $29$. The limit holds on the long-wavelength tail, where $\lambda \gg hc/(k_BT) \approx 5.3\ \text{mm}$, the range radio observations are made in. The COBE data sit on the blackbody curve at $T = 2.73\ \text{K}$ across the whole range measured.

---

Flashcards for this section are as follows:

- the cosmic microwave background's temperature $T$ and its peak wavelength, from $\lambda_{\max} = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}/T$ ::@:: $2.73\ \text{K}$, peaking at about $1.06\ \text{mm}$.
- whether the Rayleigh–Jeans limit holds at that peak, and how far off the classical law is there, in terms of $hc/(\lambda k_BT)$ ::@:: It does not hold. There $hc/(\lambda k_BT) \approx 4.97$ and the classical law is high by a factor of about $29$.
- where the Rayleigh–Jeans limit does hold for the background, and why that is where radio observations are made, in terms of $\lambda$ and $hc/(k_BT)$ ::@:: On the long-wavelength tail, where $\lambda \gg hc/(k_BT) \approx 5.3\ \text{mm}$.
- what the COBE measurements of the cosmic microwave background show against the curve at $T = 2.73\ \text{K}$ ::@:: That the data sit on the blackbody curve across the whole range measured.
