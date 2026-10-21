---
aliases:
  - ELEC 2400 inverting amplifier
  - ELEC2400 inverting amplifier
  - HKUST ELEC 2400 inverting amplifier
  - HKUST ELEC2400 inverting amplifier
  - inverting amplifier
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/inverting_amplifier
  - language/in/English
---

# inverting amplifier

An inverting amplifier amplifies the signal and flips its sign. Two external resistors decide how much. What makes the relation that simple is the node the two resistors share, which sits at ground potential without being wired there.

---

Flashcards for this section are as follows:

- how is the gain $A_{cl}$ of an inverting amplifier set by its resistors $R_1$ and $R_2$, and what does the minus sign mean? ::@:: The ratio of the feedback resistor to the input resistor, $A_{cl} = -\frac{R_2}{R_1}$; the minus sign means the output moves opposite to the input.

## the inverting circuit

The input $V_{\text{in}}$ enters the inverting terminal through $R_1$, $R_2$ returns from the output to that terminal, and the non-inverting terminal sits at ground. Grounding that input sets $V_+ = 0$, and the virtual short gives $V_- = 0$: a [virtual ground](virtual%20ground.md).

Think of a seesaw balanced on the virtual ground. The node the two resistors share is pinned at $0\text{ V}$, so $R_1$ carries the whole input voltage and $R_2$ the whole output voltage. One current runs through both, so the two drops stand in the ratio of the two resistances. Push the input up and the output goes the other way, by the input's amount times $\frac{R_2}{R_1}$.

No current enters the inverting terminal, so $R_1$ carries $\frac{V_{\text{in}} - V_-}{R_1} = \frac{V_{\text{in}}}{R_1}$, and $R_2$ carries that same current on to the output. The closed-loop gain follows as $A_{cl} = \frac{V_{\text{out}}}{V_{\text{in}}} = -\frac{R_2}{R_1}$, and the transfer characteristic is a line through the origin of slope $A_{cl}$, capped at $V_{dd}$ and at $-V_{ss}$. Adding more inputs, each through its own resistor, gives the [summing amplifier](summing%20amplifier.md).

The price is on the input side. The source drives $R_1$ straight into a virtual ground, so it sees $R_1$ itself and has to supply $\frac{V_{\text{in}}}{R_1}$. What the arrangement buys instead is a gain that can drop below 1, and a summing node held at $0\text{ V}$, which is what the weighted sums and the impedance ratio rest on.

The analysis above assumed $A_V = \infty$. At finite gain instead, the model $V_{\text{out}} = A_V(V_+ - V_-)$, the grounded input $V_+ = 0$ and the current law at the inverting terminal give $K_F = \frac{V_{\text{out}}}{V_{\text{in}}} = -\frac{1 - \left[\frac{R_1}{R_1 + R_2}\right]}{\frac{1}{A_V} + \left[\frac{R_1}{R_1 + R_2}\right]}$. The limit $A_V \to \infty$ then removes the $\frac{1}{A_V}$ term to leave $-\frac{R_2}{R_1}$.

One current runs through the input path and the feedback path, so each path's drop is that current times its impedance and the two drops stand in the ratio of the two impedances. The gain $-\frac{R_2}{R_1}$ is that ratio written for two resistors: with impedances in the paths it reads $A_{cl} = -\frac{Z_2}{Z_1}$.

The ratio then gives the two calculus stages away. Put a capacitor in the feedback path and $Z_2 = \frac{1}{j\omega C_1}$ leaves $A_{cl} = -\frac{1}{j\omega C_1 R_1}$, a magnitude that falls as the frequency rises: an [integrator](integrator.md). Put the capacitor in the input path instead and $Z_1 = \frac{1}{j\omega C_1}$ leaves $A_{cl} = -j\omega C_1 R_2$, a magnitude that rises with frequency: a [differentiator](differentiator.md). Only the two paths change, and the wiring stays that of the inverting amplifier.

![inverting amplifier: the source drives the inverting input through R 1, the feedback resistor R 2 returns from the output to the same node, and the non-inverting input is grounded](attachments/inverting_amplifier.svg)

---

Flashcards for this section are in the following format:

- the inverting amplifier: what does the drawing ground, and what carries the input? ::@:: The non-inverting input is grounded, and the source carries its voltage through $R_1$ to the inverting input, with $R_2$ returning from the output to the same node. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- draw an inverting amplifier: which resistor sets the gain ratio, and where does the gain ratio's sign come from? ::@:: The ratio of $R_2$ over $R_1$ sets the magnitude, and the sign is negative because the input enters the inverting input. <p> ![inverting amplifier: the source drives the inverting input through R 1, the feedback resistor R 2 returns from the output to the same node, and the non-inverting input is grounded](attachments/inverting_amplifier.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- seesaw reading of the inverting amplifier: what does the virtual ground pin, and what does the ratio of $R_1$ to $R_2$ give? ::@:: It pins the shared node at $0\text{ V}$, so $R_1$ carries the whole input voltage and $R_2$ the whole output voltage; one current through both makes $V_o = -\frac{R_2}{R_1}V_{\text{in}}$, the input scaled and reversed.
- in an inverting amplifier, why does a rise at $V_{\text{in}}$ force a fall at $V_{\text{out}}$? ::@:: One current runs through $R_1$ and $R_2$ with their junction pinned at $0\text{ V}$, so whatever $R_1$ gains at its outer end, $R_2$ gives up at its own, scaled by $\frac{R_2}{R_1}$.
- what does the inverting amplifier with $R_1$ and $R_2$ cost at its input, and what does that buy? ::@:: The source drives $R_1$ into a virtual ground, so it sees $R_1$ and supplies $\frac{V_{\text{in}}}{R_1}$; in exchange the gain can fall below 1 and the summing node stays at $0\text{ V}$.
- gain as a ratio of impedances: why does the inverting stage's gain $-\frac{R_2}{R_1}$ become $-\frac{Z_2}{Z_1}$ once the two paths carry impedances? ::@:: One current runs through both paths, so each path's drop is that current times its impedance and the two drops stand in the ratio of the two impedances.
- capacitor in the feedback path: what does the inverting amplifier become when $R_2$ is replaced by a capacitor $C_1$, and what does the gain become? ::@:: An integrator: $A_{cl} = -\frac{1}{j\omega C_1 R_1}$, a magnitude that falls as the frequency rises.
- capacitor in the input path: what does the inverting amplifier become when $R_1$ is replaced by a capacitor $C_1$, and what does the gain become? ::@:: A differentiator: $A_{cl} = -j\omega C_1 R_2$, a magnitude that rises with frequency.
- virtual ground: the non-inverting terminal of an ideal operational amplifier sits at ground in an inverting amplifier; what potential does the inverting terminal hold, and what is this called? ::@:: $V_+ = 0$ and the virtual short give $V_- = 0$: the inverting terminal holds ground's potential without being ground itself, which is called a virtual ground. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- ideal gain: an inverting amplifier feeds $V_{\text{in}}$ through $R_1$ into the inverting terminal of an ideal operational amplifier, returns $R_2$ from the output to that terminal, and grounds the non-inverting terminal; what is $A_{cl} = \frac{V_{\text{out}}}{V_{\text{in}}}$? ::@:: $V_+ = 0$ and the virtual short give $V_- = 0$, so $R_1$ carries $\frac{V_{\text{in}}}{R_1}$ and $R_2$ carries the same current on: $A_{cl} = -\frac{R_2}{R_1}$.
- finite gain: an inverting amplifier feeds $V_{\text{in}}$ through $R_1$ into an operational amplifier's inverting terminal, returns $R_2$ from the output to that terminal, and grounds the non-inverting terminal; with the model $V_{\text{out}} = A_V(V_+ - V_-)$ at finite gain $A_V$, what is $K_F = \frac{V_{\text{out}}}{V_{\text{in}}}$, and what does it become as $A_V \to \infty$? ::@:: $K_F = -\frac{1 - \left[\frac{R_1}{R_1 + R_2}\right]}{\frac{1}{A_V} + \left[\frac{R_1}{R_1 + R_2}\right]}$, which becomes $-\frac{R_2}{R_1}$ as $A_V \to \infty$.
- why the output is inverted: why is the output of an inverting amplifier built from an operational amplifier said to be inverted relative to its input? ::@:: Its closed-loop gain $A_{cl} = -\frac{R_2}{R_1}$ is negative, so $V_{\text{out}}$ carries polarity opposite to $V_{\text{in}}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## inverting amplifier with parallel feedback

The feedback resistor need not be one part, and the gain never notices: two resistors in parallel behave as their equivalent. Take $V_s$ through $1\text{ k}\Omega$ into the inverting terminal and return $6\text{ k}\Omega$ in parallel with $3\text{ k}\Omega$ from the output to that terminal, and the pair is an equivalent $2\text{ k}\Omega$. The gain is $A_{cl} = -\frac{6\text{ k}\Omega \parallel 3\text{ k}\Omega}{1\text{ k}\Omega} = -2$, so $V_s = 1\text{ V}$ gives $V_o = -2\text{ V}$, while $V_s(t) = \sin(2\pi 50t)\text{ V}$ gives $V_o(t) = -2\sin(2\pi 50t)\text{ V}$, a sine swinging between $2\text{ V}$ and $-2\text{ V}$.

![inverting amplifier with parallel feedback: the source drives the inverting input through a 1 kilohm resistor, a 6 kilohm resistor and a 3 kilohm resistor in parallel return from the output to the same node, and the non-inverting input is grounded](attachments/inverting_parallel_feedback.svg)

---

Flashcards for this section are in the following format:

- the parallel-feedback inverting amplifier: what does the feedback path consist of? <p> ![inverting amplifier with parallel feedback: the source drives the inverting input through a 1 kilohm resistor, a 6 kilohm resistor and a 3 kilohm resistor in parallel return from the output to the same node, and the non-inverting input is grounded](attachments/inverting_parallel_feedback.svg) ::@:: A $6\,\mathrm{k}\Omega$ resistor and a $3\,\mathrm{k}\Omega$ resistor in parallel between the output and the inverting input, ahead of the $1\,\mathrm{k}\Omega$ input resistor. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- replace a feedback resistor with two in parallel: what does the drawing beside the inverting amplifier with parallel feedback show? <p> ![inverting amplifier with parallel feedback: the source drives the inverting input through a 1 kilohm resistor, a 6 kilohm resistor and a 3 kilohm resistor in parallel return from the output to the same node, and the non-inverting input is grounded](attachments/inverting_parallel_feedback.svg) ::@:: The $1\,\mathrm{k}\Omega$ input resistor into the inverting input, with $6\,\mathrm{k}\Omega$ and $3\,\mathrm{k}\Omega$ in parallel returning from the output to that node. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- draw the inverting amplifier with a $1\text{ k}\Omega$ input resistor and a split feedback path: which resistors return from the output, and what single resistor do they stand in for? ::@:: $V_s$ drives the inverting input through $1\text{ k}\Omega$, with $6\text{ k}\Omega$ and $3\text{ k}\Omega$ in parallel from the output to that node, standing in for one $2\text{ k}\Omega$ feedback resistor. <p> ![inverting amplifier with parallel feedback: the source drives the inverting input through a 1 kilohm resistor, a 6 kilohm resistor and a 3 kilohm resistor in parallel return from the output to the same node, and the non-inverting input is grounded](attachments/inverting_parallel_feedback.svg)
- parallel feedback pair: an ideal operational amplifier builds an inverting amplifier that feeds back $6\text{ k}\Omega$ in parallel with $3\text{ k}\Omega$ and takes $V_s$ through $1\text{ k}\Omega$; what is its gain, and what outputs follow from $V_s = 1\text{ V}$ and $V_s(t) = \sin(2\pi 50t)\text{ V}$? ::@:: $A_{cl} = -\frac{6\text{ k}\Omega \parallel 3\text{ k}\Omega}{1\text{ k}\Omega} = -2$, so $V_o = -2\text{ V}$ and $V_o(t) = -2\sin(2\pi 50t)\text{ V}$, swinging between $2\text{ V}$ and $-2\text{ V}$.
