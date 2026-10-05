---
aliases:
  - black-body
  - black-body radiation
  - blackbody
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/black-body_radiation
  - language/in/English
---

# black-body radiation

_A black body_ absorbs every wavelength that falls on it and emits [thermal radiation](thermal%20radiation.md) of its own. None of the incoming light comes back out.

What it emits depends on the temperature alone: two cavities at the same temperature give the same spectrum whatever their walls are made of. Classical physics could not account for that: it is one of the three problems of 1895 in [modern physics](modern%20physics.md), alongside the ether and the speed of light.

The spectrum is smooth and continuous, with a single peak. Line emission is different: excited atoms emit at discrete wavelengths identifying the element, and [emission spectrum](emission%20spectrum.md) covers those.

---

Flashcards for this section are as follows:

- overview ::@:: A black body absorbs every wavelength falling on it, emits thermal radiation of its own, and returns none of the incoming light. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what a black body's spectrum depends on ::@:: On the temperature alone, not the material, surface finish, colour, or shape; two cavities at the same temperature radiate the same spectrum whatever their walls are made of. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- black-body spectrum against line emission ::@:: A black body radiates a smooth continuous spectrum with a single peak, while excited atoms radiate discrete lines at wavelengths that identify the element. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the three problems of 1895: the one black-body radiation belongs to ::@:: The failure of classical physics to explain black-body radiation, alongside the ether and the speed of light. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## the cavity realisation

No real surface is a perfect black body, so a cavity stands in for one: an enclosure of opaque, highly absorbing material, heated and read through a small hole. Radiation entering the hole meets the walls and is absorbed, so what comes back out is the cavity's own, with the spectrum of an ideal black body at the cavity's temperature.

![blackbody cavity: a thick-walled enclosure seen in section with a small hole in the right-hand wall, a ray path crossing the interior, and a beam escaping through the hole](attachments/Hole%20in%20Cavity%20as%20Blackbody.png)

The walls absorb so strongly that the hole has to be small. A large hole would let incoming radiation escape before the walls took it in, and the cavity would stop behaving like a black body.

Reading the brightness of the hole at one wavelength gives the temperature. An [infrared thermometer](infrared.md) works the same way.

---

Flashcards for this section are as follows:

- how a cavity stands in for a black body ::@:: An opaque, highly absorbing enclosure is heated and read through a small hole; radiation entering is absorbed by the walls, so what leaves is the cavity's own radiation. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the hole: why it must be small ::@:: A large hole would let incoming radiation escape before the walls absorbed it, and the cavity would no longer behave like a black body. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- a small hole as a thermometer ::@:: A cavity absorbs well and a small hole emits well, so the brightness of the hole at a given wavelength reads the cavity's temperature directly. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- an infrared thermometer against the cavity arrangement ::@:: It reproduces the arrangement well enough to compare a body's radiation against that of a black body. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## the shape of the curve

Plot the power radiated per unit area per unit wavelength against wavelength at a fixed temperature: a single smooth hump. It is zero at both ends, with one maximum, rising slowly on the long-wavelength side and falling steeply on the short-wavelength side.

Raise the temperature and the whole curve lifts, since a hotter body radiates more power at every wavelength, and the maximum moves to shorter wavelengths. Six tungsten-halogen lamp filament curves show both at once, at $2000$, $2500$, $2800$, $3000$, $3200$, and $3300\ \text{K}$ over a visible band from $400$ to $700\ \text{nm}$.

The law that reproduces this curve is [Planck's law](Planck's%20law.md), which states the spectral radiance $B_\lambda$ of a body at absolute temperature $T$ in kelvin: the power it radiates per square metre of surface, per steradian of direction, per metre of wavelength. Written out, $B_\lambda(T) = \frac{2hc^2}{\lambda^5}\,\frac{1}{e^{hc/(\lambda k_BT)} - 1}$, with $h$ Planck's constant, $c$ the speed of light, and $k_B$ the Boltzmann constant.

The same spectrum is also quoted as an energy density $u_\lambda$, the energy per unit volume of the cavity per unit wavelength, with $B_\lambda = \frac{c}{4\pi}u_\lambda$ because an isotropic cavity field spreads its energy over the full $4\pi$ steradians of a sphere. As a flux, the power leaving each square metre of surface per unit wavelength, it is $I_\lambda = \pi B_\lambda$, that factor coming from a cosine-weighted integral over the $2\pi$ steradians of a hemisphere.

Integrating over all wavelengths gives the $T^4$ of the [Stefan–Boltzmann law](Stefan%E2%80%93Boltzmann%20law.md), so that law follows from the curve.

---

Flashcards for this section are as follows:

- the shape of a black-body spectrum against wavelength at a fixed temperature ::@:: A single smooth hump, zero at both ends, with one maximum, and steeper on the short-wavelength side than on the long-wavelength side. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- black-body spectrum: what rising the temperature does to the curve ::@:: It lifts, since a hotter body radiates more power at every wavelength, and the maximum moves to shorter wavelengths. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the six tungsten-halogen filament curves at $2000$, $2500$, $2800$, $3000$, $3200$, and $3300\ \text{K}$: what changes across the family ::@:: The curves lift and their maxima move to shorter wavelengths, over a visible band of $400$ to $700\ \text{nm}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the law that reproduces the black-body curve, $B_\lambda$ the spectral radiance at absolute temperature $T$ in kelvin ::@:: [Planck's law](Planck's%20law.md), $B_\lambda(T) = \frac{2hc^2}{\lambda^5}\,\frac{1}{e^{hc/(\lambda k_BT)} - 1}$, where $h$ is Planck's constant, $c$ the speed of light, and $k_B$ the Boltzmann constant. $B_\lambda$ is the power radiated per unit area, per steradian, per unit wavelength. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the three symbols for one black-body spectrum, $B_\lambda$ the radiance, $u_\lambda$ the energy density, and $I_\lambda$ the flux, each carrying a different prefactor for the same curve ::@:: Radiance is the power per unit area, per steradian, per unit wavelength; energy density is energy per unit volume per unit wavelength; flux is power per unit area per unit wavelength leaving the surface. An isotropic cavity spreads its energy over the full solid angle $4\pi$, so $B_\lambda = \frac{c}{4\pi}u_\lambda$, and a surface gives $I_\lambda = \pi B_\lambda$ from a cosine-weighted integral over a hemisphere of $2\pi$ steradians. Both steps are worked through in [mode density of a cavity](mode%20density%20of%20a%20cavity.md). <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- where the $T^4$ of the Stefan–Boltzmann law comes from ::@:: From integrating the spectrum over all wavelengths, so it follows from the curve rather than standing on its own. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## the two classical laws

Two classical laws came before Planck's law, and each got one end of the curve right.

The [Rayleigh–Jeans law](Rayleigh%E2%80%93Jeans%20law.md) gives every mode of the field the equipartition share of energy, whatever the mode's frequency. It matches the measurement at long wavelengths and fails at short ones, where it runs to a divergence the measurement does not show. That failure is the [ultraviolet catastrophe](ultraviolet%20catastrophe.md).

The [Wien approximation](Wien%20approximation.md) makes the opposite assumption about the same modes, letting a mode hold either nothing or one whole quantum of energy and nothing in between. It matches the measurement at short wavelengths, in the visible and ultraviolet, and fails at longer wavelengths.

Both count the cavity modes the same way, and that count is sound. Planck's law has both classical laws as limits: it reduces to Rayleigh–Jeans when $hc/\lambda \ll k_BT$, and to the Wien approximation when $hc/\lambda \gg k_BT$.

---

Flashcards for this section are as follows:

- Rayleigh–Jeans law: where it matches measurement and where it fails ::@:: It matches at long wavelengths and fails at short ones, where it predicts a divergence the measurement does not show. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- Wien approximation: where it matches measurement and where it fails ::@:: It matches at short wavelengths, in the visible and ultraviolet, and fails at longer wavelengths. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the Rayleigh–Jeans law: what it assumes about the energy in a mode ::@:: That every mode gets the equipartition share, whatever its frequency, so a fast mode is given as much as a slow one. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the Wien approximation: what it assumes about the energy in a mode ::@:: That a mode holds either nothing or one whole quantum of energy, with nothing in between. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what the two classical laws agree on ::@:: They count the cavity modes the same way, and that count is sound. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- Planck's law taken to the limits $hc/\lambda \ll k_BT$ and $hc/\lambda \gg k_BT$: which classical law does it reduce to in each ::@:: Rayleigh–Jeans in the long-wavelength limit and the Wien approximation in the short-wavelength limit. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## reading a temperature off the peak

A fixed product ties the peak wavelength to the temperature. Write $\lambda_{\max}$ for the wavelength at that peak; a measured $\lambda_{\max}$ gives a temperature on the same scale for every material, with no contact at all. [Wien's displacement law](Wien's%20displacement%20law.md) is the name for that product, and the constant it fixes is $\lambda_{\max}T = 2.898\times10^{-3}\ \text{m}\cdot\text{K}$.

The Wien approximation shares the name and nothing else: it was a failed guess at the energy in a mode, while the displacement law states where the peak sits and is read off the measured curve.

The eye is a cruder instrument: it saturates before the peak reaches the blue, so a star hot enough to peak in the ultraviolet still looks blue-white. Only roughly $3000$ to $8000\ \text{K}$ puts the peak inside the visible at all. Across that range the colour runs red, orange, yellow, white, then blue-white, and never green, because no black-body curve concentrates its emission in one narrow part of the visible. A redder body peaks at a longer wavelength, so the redder of two stars is the cooler: Betelgeuse at the top left of Orion is red and cool, Rigel at the bottom right is blue and hot.

---

Flashcards for this section are as follows:

- what makes the product $\lambda_{\max}T$ a thermometer ::@:: The product is a fixed constant and the scale is the same for every material, so a measured $\lambda_{\max}$ returns a temperature without contact. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the constant that the Wien displacement law fixes between the peak wavelength $\lambda_{\max}$ and the temperature $T$ ::@:: $\lambda_{\max}T = 2.898\times10^{-3}\ \text{m}\cdot\text{K}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the Wien approximation against the Wien displacement law ::@:: Different results sharing a name. The approximation was a failed guess at the energy in a mode, while the displacement law states where the peak of the curve sits and is read off the measured curve. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the eye against the peak position: why a star hot enough to peak in the ultraviolet still looks blue-white ::@:: The eye saturates before the peak reaches the blue, so the visible appearance stops changing once the peak is well into the ultraviolet. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the temperature range in $\text{K}$ over which a black-body peak falls inside the visible spectrum ::@:: Roughly $3000$ to $8000\ \text{K}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- can a star appear green, and why not ::@:: No. No black-body curve concentrates its emission in one narrow part of the visible, which is what a green star would need; the colours stars do show run red, orange, yellow, white, then blue-white. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the red star and the blue star in Orion: which is cooler ::@:: Betelgeuse, the red one, since a redder black body peaks at a longer wavelength. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## the cosmic microwave background

The cosmic microwave background, the relic radiation of the hot early universe, is a body nobody can build, and it has been measured with microwave receivers and fitted to a black-body curve. The fit holds to the limit of the measurement, and no free parameter is left over to absorb a mismatch.

That temperature is $2.73\ \text{K}$, which puts the peak near $1\ \text{mm}$, in the microwave rather than the infrared.

No material took part in making this radiation, and a cavity at $2.73\ \text{K}$ in a laboratory radiates the same way. The fit carries from the laboratory to the whole observable universe.

---

Flashcards for this section are as follows:

- the spectrum of the cosmic microwave background ::@:: The relic radiation of the hot early universe, measured with microwave receivers and fitted to a black-body curve. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the temperature in $\text{K}$ that fits the measured spectrum of the cosmic microwave background, and where that puts the peak ::@:: $2.73\ \text{K}$, which puts the peak near $1\ \text{mm}$, in the microwave rather than the infrared. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the fitted temperature $2.73\ \text{K}$ checked against $\lambda_{\max}T = 2.898\times10^{-3}\ \text{m}\cdot\text{K}$: where should the peak be ::@:: $\lambda_{\max} = 2.898\times10^{-3}/2.73 \approx 1.06\times10^{-3}\ \text{m}$, that is about $1.06\ \text{mm}$, which is where the data show the maximum. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why the fit counts as a test of the spectrum's universality ::@:: It is a body nobody can build, and its measured spectrum still fits a black-body curve, with no free parameter left over. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- a cavity at $2.73\ \text{K}$ radiates the same way as the cosmic microwave background: why does that carry the result so far ::@:: No material took part in making the radiation, so the fit of its spectrum holds across the whole observable universe rather than only in a laboratory. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
