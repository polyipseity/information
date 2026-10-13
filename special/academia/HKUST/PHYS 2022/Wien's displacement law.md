---
aliases:
  - Wien's displacement law
  - Wien's law
tags:
  - flashcard/active/special/academia/HKUST/PHYS_2022/Wien_s_displacement_law
  - language/in/English
---

# Wien's displacement law

Wilhelm Wien's displacement law fixes where the peak of a [black-body spectrum](black-body%20radiation.md) sits, given the temperature. It concerns $I_\lambda$, the power a black body radiates per unit area per unit wavelength at the absolute temperature $T$, measured in kelvin. Write $\lambda_{\max}$ for the wavelength at which that spectrum is tallest. The peak moves toward shorter wavelengths as the temperature rises, in inverse proportion. The law reads $\lambda_{\max}T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$, and that number is Wien's displacement constant, the same for every material.

The relation works either way: a temperature gives a peak wavelength, a measured peak gives a temperature. Doubling the temperature halves the peak wavelength.

The $1800\ \text{K}$ curve peaks near $1.6\ \mu\text{m}$, where $\mu\text{m}$ is a micrometre; at $900\ \text{K}$ the peak has moved past $3\ \mu\text{m}$. The $900\ \text{K}$ curve also sits far below the $1800\ \text{K}$ one. The height tracks the power a surface radiates, which grows with temperature under the [Stefan–Boltzmann law](Stefan%E2%80%93Boltzmann%20law.md). Plot $I_\lambda/T^5$ against $\lambda T$ and every spectrum collapses onto a single curve.

Height reports the power a body radiates; the peak reports a wavelength. This law fixes only the peak.

The height has a scaling of its own. The peak sits at $\lambda_{\max} \propto 1/T$, so the spectrum evaluated there carries one extra factor of temperature beyond the curve's own shape, and the peak intensity rises as the fifth power of $T$. The total power a surface radiates rises as the fourth power instead, the [Stefan–Boltzmann law](Stefan–Boltzmann%20law.md), because integrating over every wavelength adds no such factor.

---

Flashcards for this section are as follows:

- Wien's displacement law: what it says about the peak wavelength $\lambda_{\max}$ of a black-body spectrum against the absolute temperature $T$ ::@:: They are inversely proportional, $\lambda_{\max}T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$, where $\lambda_{\max}$ is the wavelength at which the spectrum is tallest and $T$ is the absolute temperature in kelvin. The constant is the same for every material. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the quantity $I_\lambda$ that the law speaks about: what it measures ::@:: The power a black body radiates per unit area per unit wavelength at temperature $T$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the two things the product form of the law lets you do ::@:: Given a temperature, return the peak wavelength; given a measured peak, return a temperature. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the temperature doubled from $T$ to $2T$ in $\lambda_{\max}T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$: what happens to the peak wavelength ::@:: It is halved, because the peak wavelength is inversely proportional to the absolute temperature. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the $1800\ \text{K}$ curve: where its peak sits, with $\mu\text{m}$ the micrometre, and the check against $\lambda_{\max}T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$ ::@:: Near $1.6\ \mu\text{m}$, and $2.898\times10^{-3}/1800 \approx 1.61\times10^{-6}\ \text{m}$ confirms it. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the $900\ \text{K}$ curve: where its peak sits against the $1800\ \text{K}$ curve ::@:: Past $3\ \mu\text{m}$, roughly twice as long as the $1800\ \text{K}$ peak, because the temperature is half as large. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the height of a black-body curve against the position of its peak: what each one reports ::@:: Height reports the power a body radiates, the peak reports a wavelength, and this law fixes only the peak. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the peak intensity of a black-body spectrum against the absolute temperature $T$ ::@:: Proportional to the fifth power of the absolute temperature, because the peak sits at $\lambda_{\max} \propto 1/T$ and picks up one extra factor of $T$; the total power rises as the fourth power instead.

## deriving the peak position

Planck's spectrum is built so that wavelength and temperature enter only through the combination $x = hc/(\lambda k_B T)$, and the peak position follows from that. Differentiate $B_\lambda \propto \lambda^{-5}/(e^x - 1)$ with respect to $\lambda$ and set the result to zero. The chain rule turns the condition into $$5(1 - e^{-x}) = x,$$ whose only nonzero root is $x \approx 4.9651$. The peak therefore sits where $hc/(\lambda_{\max} k_B T) = 4.9651$, so $\lambda_{\max} T = \dfrac{hc}{4.9651\,k_B} = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$. That constant is built from $h$, $c$ and $k_B$ alone, which is why the same number serves every material.

---

Flashcards for this section are as follows:

- the peak condition on the Planck spectrum $B_\lambda \propto \lambda^{-5}/(e^x - 1)$ with $x = hc/(\lambda k_B T)$: the equation it becomes ::@:: Set $dB_\lambda/d\lambda = 0$; the chain rule turns the condition into $5(1 - e^{-x}) = x$.
- the nonzero root of $5(1 - e^{-x}) = x$: what it fixes about the peak ::@:: $x \approx 4.9651$, so $hc/(\lambda_{\max} k_B T) = 4.9651$ and $\lambda_{\max}T = hc/(4.9651\,k_B) = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$, a constant built from $h$, $c$, and $k_B$ alone.

## reading a body temperature

The law turns a body into a non-contact thermometer. A person at $37\ ^{\circ}\text{C}$ sits at $310\ \text{K}$, and the peak lies at $\lambda_{\max} = 2.898 \times 10^{-3}/310 \approx 9.3\ \mu\text{m}$. That peak is deep in the infrared, past anything the eye reaches. The body looks dark while the [pyrometer](pyrometer.md) family reads the glow: reading a body's temperature off the thermal radiation it emits is pyrometry, and the infrared thermometer is one of its instruments.

At $40\ ^{\circ}\text{C}$, or $313\ \text{K}$, the same constant gives $2.898 \times 10^{-3}/313 \approx 9.3\ \mu\text{m}$. Three degrees is about $1$ percent of $310\ \text{K}$, so the peak moves by about $0.1\ \mu\text{m}$. That is easy to miss.

A curve labelled "human body at $37\ ^{\circ}\text{C}$" has a peak labelled $9550\ \text{nm}$. The peak sits slightly long of the $9.3\ \mu\text{m}$ the law returns at core temperature ($9.34\ \mu\text{m}$ at $37\ ^{\circ}\text{C}$). Read the peak backwards: $2.898 \times 10^{-3}/(9.55 \times 10^{-6}) \approx 303\ \text{K}$. That is several degrees below core, which is what a radiating skin surface sits at. Skin runs near $30$ to $32\ ^{\circ}\text{C}$, and at those temperatures the law itself returns about $9.5\ \mu\text{m}$. The gap is the skin temperature, not a failure of the law.

---

Flashcards for this section are as follows:

- a body at $37\ ^{\circ}\text{C}$, or $310\ \text{K}$, given $\lambda_{\max}T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$: where does its peak sit ::@:: $\lambda_{\max} = 2.898\times10^{-3}/310 \approx 9.3\times10^{-6}\ \text{m}$, about $9.3\ \mu\text{m}$, deep in the infrared. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- a body at $40\ ^{\circ}\text{C}$, or $313\ \text{K}$: where does its peak sit ::@:: $\lambda_{\max} = 2.898\times10^{-3}/313 \approx 9.3\times10^{-6}\ \text{m}$, about $9.3\ \mu\text{m}$, the same value as at $37\ ^{\circ}\text{C}$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the same body at $310\ \text{K}$ and at $313\ \text{K}$: how far its peak actually moves ::@:: About $0.1\ \mu\text{m}$: three degrees is about $1$ percent of $310\ \text{K}$, and the peak moves in inverse proportion. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the curve labelled "human body at $37\ ^{\circ}\text{C}$": where its peak sits, in nanometres, against the $9.3\ \mu\text{m}$ the law returns at $37\ ^{\circ}\text{C}$ ::@:: Near $9550\ \text{nm}$, slightly long, because reading the peak backwards gives $303\ \text{K}$, several degrees below core, where a radiating skin surface sits near $30$ to $32\ ^{\circ}\text{C}$ and the law returns about $9.5\ \mu\text{m}$. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the peak of a $37\ ^{\circ}\text{C}$ body: why the eye cannot see it ::@:: At about $9.3\ \mu\text{m}$ the peak is deep in the infrared, past anything the eye reaches, so the body looks dark while an infrared thermometer reads the glow. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the technique family an infrared thermometer belongs to ::@:: Pyrometry, the [pyrometer](pyrometer.md) family of reading a body's temperature off the thermal radiation it emits; the instrument is one member of it.

## reading a stellar temperature

A star is a body, and here the same relation runs the other way: the peak gives the temperature. A redder black body peaks at a longer wavelength, so a longer peak means a lower temperature. Betelgeuse, the red star at the top left of Orion, is cooler than Rigel, the blue star at the bottom right. Betelgeuse is at roughly $3500\ \text{K}$, and its peak is at $\lambda_{\max} = 2.898 \times 10^{-3}/3500 \approx 8.3 \times 10^{-7}\ \text{m}$, about $830\ \text{nm}$, just past the red edge at the far end of the visible band, in the near infrared.

Rigel is near $12000\ \text{K}$. Its peak is at $2.898 \times 10^{-3}/12000 \approx 2.4 \times 10^{-7}\ \text{m}$, about $240\ \text{nm}$, well inside the ultraviolet. The star still looks blue-white, because the eye responds to the whole visible band and the peak has already left that band at that temperature. Colour and peak disagree.

The sun's measured spectrum peaks near $500\ \text{nm}$, and the law reads its surface straight off: $T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}/(500 \times 10^{-9}\ \text{m}) \approx 5800\ \text{K}$.

---

Flashcards for this section are as follows:

- Betelgeuse at roughly $3500\ \text{K}$, given $\lambda_{\max}T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$: where does its peak sit ::@:: $\lambda_{\max} = 2.898\times10^{-3}/3500 \approx 8.3\times10^{-7}\ \text{m}$, about $830\ \text{nm}$, just past the red edge, the far end of the visible band, in the near infrared. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- Rigel at roughly $12000\ \text{K}$: where does its peak sit ::@:: $\lambda_{\max} = 2.898\times10^{-3}/12000 \approx 2.4\times10^{-7}\ \text{m}$, about $240\ \text{nm}$, inside the ultraviolet. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- Rigel at roughly $12000\ \text{K}$ with its peak in the ultraviolet: why does it look blue-white and not invisible ::@:: The eye responds to the whole visible band, not the peak, and by that temperature the peak has already left the visible altogether. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the red star and the blue star in Orion: which is cooler ::@:: Betelgeuse, the red one, because a redder black body peaks at a longer wavelength and a longer peak wavelength means a lower temperature. <!--SR:!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z!fsrs,2027-01-15T00:00:00.000Z,66,65.62422648,1,2,2,0,0,2026-11-10T00:00:00.000Z-->
- the sun's spectrum peaking near $500\ \text{nm}$, read through $\lambda_{\max}T = 2.898 \times 10^{-3}\ \text{m}\cdot\text{K}$ ::@:: A surface temperature of about $5800\ \text{K}$.
