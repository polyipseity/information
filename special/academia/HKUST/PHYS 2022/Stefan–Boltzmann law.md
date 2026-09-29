---
aliases:
  - Stefan–Boltzmann
  - Stefan–Boltzmann law
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Stefan–Boltzmann_law
  - language/in/English
---

# Stefan–Boltzmann law

The Stefan–Boltzmann law gives the total power a surface radiates per unit area, the whole [black-body spectrum](black-body%20radiation.md) added up. Write $I_\lambda$ for the power the surface radiates per unit area per unit wavelength at absolute temperature $T$ in kelvin, and $\sigma$ for the Stefan–Boltzmann constant. The integral over every wavelength has a closed form, and it is the law: $R(T) = \int_0^\infty I_\lambda(\lambda,T)\,d\lambda = \epsilon\sigma T^4$, where $R(T)$ is the total power per unit area and $\epsilon$ the emissivity of the surface. A celsius reading is a different number from $T$, not a small correction to it.

Neither the fourth power nor the constant is a fact of its own; both fall out of the shape of the spectrum. Raise the temperature and the curve gets taller while its peak moves to shorter wavelengths, the position [Wien's displacement law](Wien's%20displacement%20law.md) fixes. Stefan and Boltzmann fitted $\sigma = 5.6704 \times 10^{-8}\ \text{W}/(\text{m}^2 \cdot \text{K}^4)$ from measurement, because Planck's law did not yet exist; integrating that law instead gives $\sigma = \dfrac{2\pi^5 k_B^4}{15 h^3 c^2}$ from $h$, $c$ and $k_B$ alone, reproducing the measured value. Where $I_\lambda$ comes from: [mode density of a cavity](mode%20density%20of%20a%20cavity.md).

---

Flashcards for this section are as follows:

- the law $R(T) = \epsilon\sigma T^4$, and the integral it comes from ::@:: $R(T) = \int_0^\infty I_\lambda(\lambda,T)\,d\lambda = \epsilon\sigma T^4$, the black-body spectrum summed over every wavelength.
- the symbol $I_\lambda$ in that integral, against $R(T)$ ::@:: $I_\lambda$ is the power per unit area per unit wavelength at temperature $T$ in kelvin, one term of the integral; $R(T)$ is the whole integral, the total power per unit area.
- the $T^4$ in the Stefan–Boltzmann law: where it comes from ::@:: From the shape of the black-body curve, which the integral over every wavelength inherits, so it is not an independent fact.
- the Stefan–Boltzmann constant $\sigma$: its value, and whether it can be derived from Planck's law ::@:: $\sigma = 5.6704 \times 10^{-8}\ \text{W}/(\text{m}^2 \cdot \text{K}^4)$, and it can: integrating Planck's law over every wavelength gives $\sigma = \dfrac{2\pi^5 k_B^4}{15 h^3 c^2}$ from $h$, $c$ and $k_B$ alone. Stefan and Boltzmann fitted it by measurement only because Planck's law did not yet exist.
- the temperature that must go in the $T^4$ ::@:: The absolute temperature in kelvin; a celsius reading is a different number, not a small correction to it.

## emissivity

The emissivity $\epsilon$ is the ratio of the radiative power of a real surface to that of an ideal black body at the same temperature, and no real surface is a black body. The ideal case is exactly $\epsilon = 1$, and every real material falls below $1$, because a surface reflects part of the radiation falling on it, and that reflected part is not thermal emission of its own.

Emissivity belongs to the surface, not the bulk, so a polished metal and the same metal roughened differ. A coating is the usual way to set one. Radiator tubes, spacecraft skins, and clinical thermometers are coated for their emissivity rather than their colour. A low $\epsilon$ cuts absorption and radiation together: the surface absorbs poorly and radiates poorly, in the same proportion.

---

Flashcards for this section are as follows:

- emissivity $\epsilon$: what it is, and its value for the ideal black body ::@:: The ratio of the radiative power of a real surface to that of an ideal black body at the same temperature, exactly $1$ for the ideal.
- why a real surface has $\epsilon < 1$ ::@:: It reflects part of the radiation falling on it, and that reflected part is not thermal emission of its own.
- emissivity against the material's bulk properties: what it depends on ::@:: On the surface, not on the bulk material, so polished and roughened or blackened versions of the same metal have different emissivities.
- a surface with low emissivity $\epsilon$: what it does to both absorption and radiation ::@:: It absorbs poorly and radiates poorly, in the same proportion.
- the coatings on a radiator tube, a spacecraft skin, and a clinical thermometer: what they are chosen for ::@:: Their emissivity, not their colour, which is the usual way to set an emissivity.

## temperature sensitivity

Take the ratio of two powers and everything cancels but the temperatures: the emissivity $\epsilon$, the surface area, and $\sigma$ all drop out, leaving $(T_2/T_1)^4$. A body at $40$ against $37\ ^{\circ}\text{C}$ sits at $313$ against $310\ \text{K}$, and $(313/310)^4 - 1 \approx 0.039$, so the radiated power rises by about $3.9$ percent. Doubling the temperature multiplies the power by sixteen.

The peak moves far less. Three degrees is a $1$ percent rise on $310\ \text{K}$, and by [Wien's displacement law](Wien's%20displacement%20law.md) it shifts $\lambda_{\max}$ by about $1$ percent, roughly $0.1\ \mu\text{m}$.

So the power answers about four times harder than the shape does. A black-body thermometer works from that power and inherits the strong response; a colour thermometer has to read the shape, and inherits the weak one.

A body running a fraction of a degree above its usual temperature is radiating a few percent more power, and the difference is extra heat to shed. That is what a fever is, and the gap is why a few degrees of it matter.

---

Flashcards for this section are as follows:

- a body at $40\ ^{\circ}\text{C}$ against the same body at $37\ ^{\circ}\text{C}$, given $R \propto T^4$: by what percentage does the radiated power increase ::@:: By about $3.9$ percent, from $(313/310)^4 - 1 \approx 0.039$.
- a body at $313\ \text{K}$ against the same body at $310\ \text{K}$: what cancels in the ratio of their radiated powers ::@:: The emissivity $\epsilon$, the surface area, and $\sigma$, since only the ratio of the two absolute temperatures survives in $(T_2/T_1)^4$.
- what doubling the temperature $T$ does to the radiated power ::@:: It multiplies it by sixteen, since $(2T)^4 = 16T^4$.
- a three degree rise in body temperature: what it does to $R$ against what it does to $\lambda_{\max}$ ::@:: It raises the radiated power by about $4$ percent, while a $1$ percent rise in absolute temperature moves the peak by about $1$ percent, which at $310\ \text{K}$ is roughly $0.1\ \mu\text{m}$.
- the power against the shape of the spectrum, for the same $1$ percent temperature rise ::@:: The power answers about four times harder, rising about $4$ percent where $\lambda_{\max}$ shifts about $1$ percent, so the output is the sensitive channel and the shape is the weak one.
- a black-body thermometer against a colour thermometer, given that contrast ::@:: The black-body thermometer reads the radiated power, where a small change registers four times more strongly, while the colour thermometer has to read the shape and inherits its weak response.
