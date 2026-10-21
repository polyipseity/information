---
aliases:
  - ELEC 2400 non-inverting amplifier
  - ELEC2400 non-inverting amplifier
  - HKUST ELEC 2400 non-inverting amplifier
  - HKUST ELEC2400 non-inverting amplifier
  - non-inverting amplifier
  - noninverting amplifier
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/non-inverting_amplifier
  - language/in/English
---

# non-inverting amplifier

A non-inverting amplifier amplifies without turning the signal around. Its gain is one plus the ratio of two resistors, so it never falls below one, and a divider off the output sets that ratio by returning a share of the output to the inverting input.

---

Flashcards for this section are as follows:

- why can a non-inverting amplifier with a $R_2$ over $R_1$ divider never attenuate, and what sets how much it amplifies? ::@:: Its gain is $1 + \frac{R_2}{R_1}$, at least one, so the output always at least equals the input; the divider of $R_2$ over $R_1$ sets how much larger it becomes.

## non-inverting circuit

The input $V_{\text{in}}$ drives the non-inverting terminal directly. $R_1$ drops from the inverting terminal to ground, and $R_2$ returns from the output to the inverting terminal as well, so the loop is negative feedback.

Picture a voltage divider standing on ground. $R_1$ and $R_2$ span from ground up to the output, and the inverting terminal is the tap between them, so the tap always sits at $\frac{R_1}{R_1+R_2}V_{\text{out}}$. The virtual short holds that tap at $V_{\text{in}}$. Set the two equal and the gain is $1+\frac{R_2}{R_1}$, one plus the ratio, with no current traced anywhere.

Two things follow from where the signal enters. Going into the non-inverting terminal, it meets the operational amplifier's own very high input resistance, so the source draws nothing. But the gain can never fall below 1, which means anything that has to attenuate needs the inverting circuit instead.

With the ideal device, $V_+ = V_{\text{in}}$, and the virtual short carries that to $V_- = V_{\text{in}}$. No current enters the inverting terminal, so $R_1$ and $R_2$ carry one current, which makes $V_{\text{out}} = V_- \frac{R_1 + R_2}{R_1}$ and the closed-loop gain $A_{cl} = \frac{V_{\text{out}}}{V_{\text{in}}} = 1 + \frac{R_2}{R_1}$. Two external resistors set that gain, and they can be chosen far more precisely than a gain buried inside the chip, so the operational amplifier's own imperfections drop out of the result.

With $R_1 = 2\text{ k}\Omega$ and $R_2 = 4\text{ k}\Omega$, the gain is $1 + \frac{4\text{ k}\Omega}{2\text{ k}\Omega} = 3$. An input $V_s = 2\text{ V}$ then gives $V_o = 6\text{ V}$, and $V_s(t) = 2\sin(2\pi 50t)\text{ V}$ gives $V_o(t) = 6\sin(2\pi 50t)\text{ V}$.

A second case takes $V_s = 1\text{ V}$ at the non-inverting terminal, $100\ \Omega$ from the inverting terminal to ground, $400\ \Omega$ from the output to that terminal, and a $2\text{ k}\Omega$ load. The one current $I_1 = \frac{1\text{ V}}{100\ \Omega} = 10\text{ mA}$ flows through both resistors of the divider, so $V_o = \left(1 + \frac{400\ \Omega}{100\ \Omega}\right) \times 1\text{ V} = 5\text{ V}$, and the load takes $I_2 = \frac{5\text{ V}}{2\text{ k}\Omega} = 2.5\text{ mA}$.

![non-inverting amplifier: the input drives the non-inverting input, and the divider of R 2 above R 1 tapped off the output feeds the inverting input](attachments/non_inverting_amplifier.svg)

---

Flashcards for this section are in the following format:

- the non-inverting amplifier: how does the drawing feed the inverting input? ::@:: Through the divider of $R_2$ above $R_1$ tapped off the output, while the input drives the non-inverting input directly. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- draw a non-inverting amplifier: which input receives the signal, and which resistors form the feedback divider? ::@:: The signal enters the non-inverting input, and the divider of $R_2$ above $R_1$ returns a fraction of the output to the inverting input. <p> ![non-inverting amplifier: the input drives the non-inverting input, and the divider of R 2 above R 1 tapped off the output feeds the inverting input](attachments/non_inverting_amplifier.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- read the gain $A_{cl}$ off the $R_1$ to $R_2$ divider without tracing a current: how? ::@:: $R_1$ and $R_2$ span from ground to $V_{\text{out}}$ with the inverting terminal as the tap, so the tap sits at $\frac{R_1}{R_1+R_2}V_{\text{out}}$; the virtual short puts it at $V_{\text{in}}$, giving $A_{cl} = 1 + \frac{R_2}{R_1}$.
- what does the non-inverting arrangement with $R_1$ and $R_2$ buy, and what does it cost? ::@:: The source sees the operational amplifier's very high input resistance and draws no current, but the gain $A_{cl} = 1 + \frac{R_2}{R_1}$ can never fall below 1.
- in $A_{cl} = 1 + \frac{R_2}{R_1}$, what does the $1$ stand for? ::@:: The input reaching the output through the non-inverting terminal with nothing taken off; anything above $1$ comes from the divider feeding back only a fraction of $V_{\text{out}}$.
- gain formula: the non-inverting amplifier drives $V_{\text{in}}$ into the non-inverting terminal of an operational amplifier, with $R_1$ from the inverting terminal to ground and $R_2$ from the output to that terminal; what is the closed-loop gain $A_{cl} = \frac{V_{\text{out}}}{V_{\text{in}}}$? ::@:: $V_+ = V_- = V_{\text{in}}$ and no input current make $R_1$ and $R_2$ carry one current, so $A_{cl} = 1 + \frac{R_2}{R_1}$.
- what sets the gain: which components set the gain of a non-inverting amplifier built from an operational amplifier, and why does that leave the device's imperfections out of it? ::@:: Two external resistors set the gain, $A_{cl} = 1 + \frac{R_2}{R_1}$, and they can be chosen precisely, so the gain is pretty much independent of the operational amplifier's imperfections. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- resistor pair 2 kΩ and 4 kΩ: an ideal operational amplifier builds a non-inverting amplifier with $R_1 = 2\text{ k}\Omega$ and $R_2 = 4\text{ k}\Omega$; what are its gain, its output for $V_s = 2\text{ V}$, and its output for $V_s(t) = 2\sin(2\pi 50t)\text{ V}$? ::@:: The gain is $1 + \frac{4\text{ k}\Omega}{2\text{ k}\Omega} = 3$, so $V_o = 6\text{ V}$ and $V_o(t) = 6\sin(2\pi 50t)\text{ V}$.
- resistor pair 100 Ω and 400 Ω: an ideal operational amplifier builds a non-inverting amplifier whose non-inverting terminal takes $V_s = 1\text{ V}$, with $100\ \Omega$ from the inverting terminal to ground, $400\ \Omega$ from the output to that terminal, and a $2\text{ k}\Omega$ load; what are $I_1$ through those two resistors, $V_o$, and the load current $I_2$? ::@:: $I_1 = \frac{1\text{ V}}{100\ \Omega} = 10\text{ mA}$ flows through both, so $V_o = \left(1 + \frac{400\ \Omega}{100\ \Omega}\right) \times 1\text{ V} = 5\text{ V}$, and $I_2 = \frac{5\text{ V}}{2\text{ k}\Omega} = 2.5\text{ mA}$.
