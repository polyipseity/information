---
aliases:
  - Wien approximation
  - Wien distribution
  - Wien's approximation
  - Wien's radiation law
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Wien_approximation
  - language/in/English
---

# Wien approximation

Two classical laws describe the [blackbody spectrum](black-body%20radiation.md), and each fails where the other holds. The [Rayleigh–Jeans law](Rayleigh%E2%80%93Jeans%20law.md) gives every mode the equipartition share $k_BT$ however fast that mode oscillates, and holds at long wavelengths. The Wien approximation lets a mode hold either nothing or one whole quantum of energy, denoted $\epsilon = hf$, with nothing in between, and holds at short wavelengths in the visible and ultraviolet.

Both laws multiply the same mode density $n(\lambda) = 8\pi/\lambda^4$, the number of electromagnetic modes a cavity holds per unit volume per unit wavelength. Neither may alter that count. Only the mean energy of a mode separates them, and each law breaks there.

Wilhelm Wien derived the [displacement law](Wien%27s%20displacement%20law.md) in $1893$ from thermodynamics and this distribution in $1896$, and both concern the same curve.

---

Flashcards for this section are as follows:

- the two classical laws of the blackbody spectrum, and the ends of the spectrum where each holds ::@:: The [Rayleigh–Jeans law](Rayleigh%E2%80%93Jeans%20law.md) at long wavelengths, the Wien approximation at short wavelengths in the visible and ultraviolet.
- what the Wien approximation allows a mode to hold, given the quantum $\epsilon = hf$ ::@:: Either nothing or a single whole quantum, with nothing in between.
- the mode density $n(\lambda) = 8\pi/\lambda^4$ both laws share, and the one quantity in which they differ ::@:: Modes per unit volume per unit wavelength, common to both laws; the mean energy of a mode is what differs.
- the scientist behind both this law and the displacement law, and when each result appeared ::@:: Wilhelm Wien, who derived the displacement law in $1893$ and this distribution in $1896$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## the single-quantum assumption

That a mode holds either nothing or a single quantum $\epsilon = hf = hc/\lambda$, with nothing in between, is already a claim that energy comes in quanta of size $hf$ rather than continuously. The calculation has not earned it.

The Boltzmann factor $e^{-\epsilon/(k_BT)}$ is the population of the occupied state relative to the empty one. Multiply it by the energy that state carries, and the mean energy of a mode of frequency $f$ is $E(f) = \epsilon e^{-\epsilon/(k_BT)}$. That result needs $hf \gg k_BT$.

Set the result beside the equipartition share $k_BT$, a constant with no $f$ in it. The Wien expression $hf\,e^{-hf/(k_BT)}$ falls as $e^{-f}$ for high $f$, while the equipartition share does not move.

---

Flashcards for this section are as follows:

- the single assumption behind the law ::@:: That a mode's energy is a whole number of quanta of size $hf = \epsilon$, rather than continuous, which the calculation has not earned. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the Boltzmann factor $e^{-\epsilon/(k_BT)}$ for the occupied state against the empty one ::@:: $e^{-\epsilon/(k_BT)}$, which sets the population of the occupied state relative to the empty one.
- the mean energy $E(f)$ that Boltzmann factor gives ::@:: $E(f) = \epsilon e^{-\epsilon/(k_BT)}$, with $\epsilon = hf = hc/\lambda$.
- the two mean energies set side by side, and how each behaves in $f$ ::@:: Equipartition gives $k_BT$, constant and independent of $f$; the Wien approximation gives $hf\,e^{-hf/(k_BT)}$, which falls as $e^{-f}$ for high $f$.

## the two-state average

The same expression reads the other way, as a truncation. The thermal average over a genuine quantum oscillator sums over all occupancies $n = 0, 1, 2, 3, \ldots$, each weighted by $e^{-nhf/(k_BT)}$. Keep the two lowest states and drop every term with $n \ge 2$, and what survives is a two-state average: $E = \dfrac{1\cdot hf\,e^{-hf/(k_BT)}}{1 + e^{-hf/(k_BT)}} = \dfrac{hf}{e^{hf/(k_BT)} + 1}$.

Wien takes one step further than that. In the limit $hf \gg k_BT$ the $1$ in the denominator is negligible beside the exponential, and the average reduces to $E \approx hf\,e^{-hf/(k_BT)}$. Only the first of the two steps is exact: the surviving states give $\frac{hf}{e^{hf/(k_BT)}+1}$ at every temperature. Below that limit the dropped terms dominate the sum, and the truncation is not an approximation at all.

---

Flashcards for this section are as follows:

- what the truncation drops from the thermal sum, and what the two surviving states give exactly ::@:: It drops every term with $n \ge 2$, leaving $E = \dfrac{1\cdot hf\,e^{-hf/(k_BT)}}{1 + e^{-hf/(k_BT)}} = \dfrac{hf}{e^{hf/(k_BT)} + 1}$, which holds at every temperature. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the further step from the two-state average to Wien's expression, and what it needs ::@:: Dropping the $1$ beside the exponential in the denominator, negligible when $hf \gg k_BT$, which gives $E \approx hf\,e^{-hf/(k_BT)}$ and is what makes the result approximate. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the truncation is harmless at high frequency ::@:: When $hf \gg k_BT$ the terms with $n \ge 2$ carry weights $e^{-2hf/(k_BT)}$ and smaller, so they are negligible. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- where the truncation stops being harmless, against $hf \gg k_BT$ ::@:: For $hf \ll k_BT$ those terms dominate the sum, so dropping them is not an approximation.

## the law

Every black-body spectrum runs through three quantities, whichever law supplies the mean energy. Multiply the mode density $n(\lambda) = 8\pi/\lambda^4$ by the mean energy of one mode, $\overline{E}$, and the result is the energy density $u_\lambda$, the energy per unit volume per unit wavelength. A quarter of $c$ times that gives the flux $I_\lambda$, the power a surface radiates per unit area per unit wavelength.

Substituting the Wien mean energy $\overline{E} = hf\,e^{-hf/(k_BT)}$, with $f = c/\lambda$ turning the $hf$ into $hc/\lambda$, gives $u_\lambda = \dfrac{8\pi}{\lambda^4}\cdot\dfrac{hc}{\lambda}e^{-hc/(\lambda k_BT)} = \dfrac{8\pi hc}{\lambda^5}e^{-hc/(\lambda k_BT)}$. Dividing by the $4\pi$ solid angle of an isotropic cavity and multiplying by $c$ gives the spectral radiance $B_\lambda$, the power per unit area per steradian per unit wavelength: $B_\lambda = \frac{c}{4\pi}u_\lambda = \dfrac{2hc^2}{\lambda^5} e^{-hc/(\lambda k_BT)}$. The $\tfrac{8\pi}{4\pi}$ leaves the $\pi$ cancelled.

Two constants fix the scale: $2hc^2 \approx 1.19 \times 10^{-16}\ \text{J}\cdot\text{m}^2\text{s}^{-1}$ and $\frac{hc}{k_B} = 1.439 \times 10^{-2}\ \text{m}\cdot\text{K}$. The units are $\text{W}\,\text{m}^{-3}\,\text{sr}^{-1}$: watts per square metre per steradian per metre of wavelength. The ratio $x = \frac{hc}{\lambda k_BT}$ decides whether the approximation is any good, and $x = 1$ at $T = 1.439 \times 10^{-2}/\lambda$.

---

Flashcards for this section are as follows:

- the shared chain $I_\lambda = \frac{2\pi c}{\lambda^4}\overline{E}$ this law plugs into ::@:: The mode density $n(\lambda)$, the energy density $u_\lambda = n(\lambda)\,\overline{E}$, and the flux $I_\lambda = \frac{1}{4}c\,u_\lambda$, entered with $\overline{E} = hf\,e^{-hf/(k_BT)}$.
- the law itself as a spectral radiance $B_\lambda$, the power per unit area per steradian per unit wavelength, and where the $\pi$ went ::@:: $B_\lambda = \frac{c}{4\pi}u_\lambda = \dfrac{2hc^2}{\lambda^5} e^{-hc/(\lambda k_BT)}$, the $\tfrac{8\pi}{4\pi}$ leaving the $\pi$ cancelled.
- the two constants that fix the scale of the law, $2hc^2$ and $\frac{hc}{k_B}$ ::@:: $2hc^2 \approx 1.19 \times 10^{-16}\ \text{J}\cdot\text{m}^2\text{s}^{-1}$ and $\frac{hc}{k_B} = 1.439 \times 10^{-2}\ \text{m}\cdot\text{K}$.
- the units the spectral radiance $B_\lambda$ is expressed in, and what they mean ::@:: $\text{W}\,\text{m}^{-3}\,\text{sr}^{-1}$, watts per square metre per steradian per metre of wavelength.
- the ratio $x$ that decides whether the approximation is good, and the temperature at which $x = 1$ ::@:: $x = \frac{hc}{\lambda k_BT}$, the ratio of a quantum of energy to the thermal energy, with $x = 1$ at $T = 1.439 \times 10^{-2}/\lambda$.

## where it holds

$\lambda$ enters the law twice, in the $1/\lambda^5$ prefactor and inside the exponential. The exponential falls faster than any power of $\lambda$, so the radiance falls exponentially in $1/\lambda$.

Take $x = \frac{hc}{\lambda k_BT}$, the ratio of a quantum of energy to the thermal energy, and the accuracy follows from how large it is. Where $x$ is large the dropped terms are small beside the two kept, and the truncated average agrees with the full one. Where $x$ is small the two classical expressions meet: $e^{-x} \approx 1$ leaves the mean energy close to $hf$, and $hf \approx k_BT$ there. The law degenerates to a fall-off as $1/\lambda^5$ alone, far steeper than the measurement.

At $300\ \text{K}$ the law agrees with the full result to better than five figures at $1\ \mu\text{m}$, where it predicts $1.7 \times 10^{-7}\ \text{W}\,\text{m}^{-3}\,\text{sr}^{-1}$, and to within $1\%$ at $10\ \mu\text{m}$. Beyond that the error grows. It is short by a factor of $21$ at $1\ \text{mm}$, and by a factor of $209$ at $1\ \text{cm}$, where it predicts $1.19 \times 10^{-6}\ \text{W}\,\text{m}^{-3}\,\text{sr}^{-1}$ against $2.48 \times 10^{-4}\ \text{W}\,\text{m}^{-3}\,\text{sr}^{-1}$ from the true spectrum.

---

Flashcards for this section are as follows:

- the two places $\lambda$ appears in the law ::@:: In the $1/\lambda^5$ prefactor, and inside $e^{-hc/(\lambda k_BT)}$, which falls faster than any power of $\lambda$ and so wins at short wavelengths.
- the law in the limit $x = \frac{hc}{\lambda k_BT} \gg 1$ ::@:: The dropped terms are negligible, so the truncated average and the full one agree, and the law is accurate.
- the law in the limit $x = \frac{hc}{\lambda k_BT} \ll 1$ ::@:: The exponential approaches $1$, leaving a radiance falling as $1/\lambda^5$ alone, far steeper than the measurement.
- the radiance predicted at $300\ \text{K}$ and $\lambda = 10^{-6}\ \text{m}$, from $2hc^2 \approx 1.19 \times 10^{-16}\ \text{J}\cdot\text{m}^2\text{s}^{-1}$ ::@:: $\dfrac{1.19 \times 10^{-16}}{10^{-30}} e^{-48.0} \approx 1.19 \times 10^{14} \times 1.4 \times 10^{-21} \approx 1.7 \times 10^{-7}\ \text{W}\,\text{m}^{-3}\,\text{sr}^{-1}$.
- the accuracy of the law at $300\ \text{K}$ at four wavelengths ::@:: Agreement to better than five figures at $1\ \mu\text{m}$, within $1\%$ at $10\ \mu\text{m}$, short by a factor of $21$ at $1\ \text{mm}$, and short by a factor of $209$ at $1\ \text{cm}$.
- the radiance predicted at $300\ \text{K}$ and $\lambda = 10^{-2}\ \text{m}$, against the true value ::@:: $\dfrac{1.19 \times 10^{-16}}{10^{-10}} e^{-0.0048} \approx 1.19 \times 10^{-6}\ \text{W}\,\text{m}^{-3}\,\text{sr}^{-1}$, against $2.48 \times 10^{-4}\ \text{W}\,\text{m}^{-3}\,\text{sr}^{-1}$ from the true spectrum, so the law is short by a factor of $209$.

## the peak

Take the logarithm, turning a product into a sum: $\ln B_\lambda = \ln(2hc^2) - 5\ln\lambda - \frac{hc}{\lambda k_BT}$. Differentiate term by term: $d\ln B_\lambda/d\lambda = -\frac{5}{\lambda} + \frac{hc}{\lambda^2 k_BT}$, where the second term is positive because $\frac{hc}{\lambda k_BT}$ grows as $\lambda$ shrinks. Set that sum to zero, $\frac{hc}{\lambda^2 k_BT} = \frac{5}{\lambda}$, and one power of $\lambda$ cancels, leaving $\lambda_{\max} = \frac{hc}{5k_BT}$.

The displacement constant that follows is $2.878 \times 10^{-3}\ \text{m}\cdot\text{K}$, against $2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$ from the true spectrum, an agreement of about $0.7\%$. The integrated power is a poorer test and fails: the law totals $180/(2\pi^4) = 0.924$ of the true power, so it comes out about $7.6$ percent low.

Neither the peak nor the integral can see the tail, so a law badly wrong for $x \ll 1$ can still get both right. The peak sits where $x = 5$ and dominates the total.

---

Flashcards for this section are as follows:

- the first two steps in finding the peak of $B_\lambda$, and the sign of the derivative's second term ::@:: Take the logarithm, $\ln B_\lambda = \ln(2hc^2) - 5\ln\lambda - \frac{hc}{\lambda k_BT}$, then differentiate to get $-\frac{5}{\lambda} + \frac{hc}{\lambda^2 k_BT}$, the second term positive because $\frac{hc}{\lambda k_BT}$ grows as $\lambda$ shrinks.
- the wavelength $\lambda_{\max}$ at which this law peaks ::@:: $\lambda_{\max} = \dfrac{hc}{5k_BT}$, from setting $\dfrac{hc}{\lambda^2 k_BT} = \dfrac{5}{\lambda}$ so that one power of $\lambda$ cancels.
- the displacement constant $hc/(5k_B)$ this law predicts, against the measured one ::@:: $2.878 \times 10^{-3}\ \text{m}\cdot\text{K}$ from this law, against $2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$ from the true peak, a difference of $0.7\%$.
- the total radiated power this law predicts, against the true total $180/(2\pi^4)$ ::@:: $0.924$ of the true power, so about $7.6$ percent low over all wavelengths.
- why the peak position and the total power agree so well while the law is badly wrong elsewhere ::@:: Neither can see the long-wavelength tail: the peak sits where $x = \frac{hc}{\lambda k_BT} = 5$ and the total is dominated by the peak. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## the opposite failure

The exponential is well behaved at every wavelength, so this law has no divergence. Its curve falls to zero far faster than the measured one, leaving it orders of magnitude too small at long wavelengths, where [Rayleigh–Jeans](Rayleigh%E2%80%93Jeans%20law.md) predicts a rising curve. That other failure is the [ultraviolet catastrophe](ultraviolet%20catastrophe.md).

The shortfall is exact. Write $x = \frac{hc}{\lambda k_BT} = \frac{hf}{k_BT}$. Where the full thermal average gives $E(f) = \frac{hf}{e^{x}-1}$, the truncated one gives $hf\,e^{-x}$, and the ratio of the two is $e^{-x}(e^{x}-1) = 1 - e^{-x}$. The truncation is at fault, not the mode count.

The correct mean energy must equal $hf\,e^{-x}$ for large $x$ and $k_BT$ for small $x$. [Planck's law](Planck%27s%20law.md) supplies it as $E(f) = \dfrac{hf}{e^{hf/(k_BT)} - 1}$.

---

Flashcards for this section are as follows:

- why this law's failure is milder than the other classical law's ::@:: The predicted curve still falls as the measurement does, so the error has the right sign and stays finite, unlike the divergence of the [ultraviolet catastrophe](ultraviolet%20catastrophe.md).
- the shortfall of the approximation against the full thermal average, in terms of $x = \frac{hc}{\lambda k_BT}$ ::@:: $1 - e^{-x}$, the ratio of $hf e^{-x}$ to $hf/(e^{x}-1)$, which is $0.0468$ at $x = 0.048$ and $0.992$ at $x = 4.8$.
- the two behaviours the correct mean energy $\overline{E}$ must have, in the two limits of $x = \frac{hc}{\lambda k_BT}$ ::@:: $hf\,e^{-x}$, the Wien expression, for $x \gg 1$; $k_BT$, the equipartition share, for $x \ll 1$.
- the mean energy that has both behaviours, from [Planck's law](Planck%27s%20law.md) ::@:: $E(f) = \dfrac{hf}{e^{hf/(k_BT)} - 1}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
