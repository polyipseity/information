---
aliases:
  - ELEC 2400 differentiator
  - ELEC2400 differentiator
  - HKUST ELEC 2400 differentiator
  - HKUST ELEC2400 differentiator
  - differentiator
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/differentiator
  - language/in/English
---

# differentiator

A differentiator reports the slope of its input voltage: the output is proportional to how fast that voltage moves, not to the level it has reached.

---

Flashcards for this section are as follows:

- what does an operational amplifier differentiator report about its input, and what sets that report? ::@:: The rate of change of the input voltage: a capacitor in the input path and a resistor in the feedback path make the output proportional to the input's slope.

## from the inverting amplifier

The [inverting amplifier](inverting%20amplifier.md) has gain $-\frac{R_2}{R_1}$, the feedback impedance over the input impedance. Swap $R_1$ for a capacitor and the gain is $A_{cl} = -j\omega C_1 R_2$, which is nothing at DC. So a slow drift leaves almost no output and a fast edge leaves a large one.

---

Flashcards for this section are in the following format:

- swapping the input resistor: what does the inverting amplifier's gain $-\frac{R_2}{R_1}$ become when $R_1$ is a capacitor $C_1$? ::@:: $A_{cl} = -j\omega C_1 R_2$.
- how that swapped gain shows up on the output ::@:: It grows with frequency and falls to zero at DC, so a fast edge comes out large, a slow drift comes out small, and a steady level comes out at nothing.
- why a flat input gives nothing: reading the edge-detector's gain $-j\omega C_1 R_2$, why does a constant input produce no output at all? ::@:: The gain falls to zero as the frequency falls, so a component that never changes is filtered out and only changes get through.

## differentiator circuit

A differentiator is an inverting amplifier with the two parts exchanged: the capacitor sits in the input path and the resistor in the feedback path. The non-inverting terminal goes to ground, the virtual short carries that $0\text{ V}$ to the inverting terminal, and the capacitor charges at the rate the input voltage moves, $I(t) = C_1\frac{dV_{in}(t)}{dt}$.

Nothing enters the inverting terminal, so that current carries on through the feedback resistor and develops $V_o = -I(t)R$ across it. Substituting the capacitor current gives $V_o(t) = -C_1R\frac{dV_{in}(t)}{dt}$. The output waveform is the derivative of the input waveform, and the product $C_1R$ sets its size.

A faster change pushes more current through the same capacitor, so the gain rises with frequency without bound. High-frequency noise comes out amplified.

With $R = 10\text{ k}\Omega$ and $C_1 = 0.05\ \mu\text{F}$, the time constant is $C_1R = 0.5\text{ ms}$. The input is a triangle swinging between $1\text{ V}$ and $-1\text{ V}$. A falling edge runs from $1\text{ V}$ to $-1\text{ V}$ over $t = 0$ to $t = 0.2\text{ ms}$. That is $-2\text{ V}$ per $0.2\text{ ms}$, or $-10{,}000\text{ V/s}$, so $V_o = -(0.05\ \mu\text{F})(10\text{ k}\Omega)\times(-10{,}000\text{ V/s}) = 5\text{ V}$. The rising edge carries the opposite slope and gives $-5\text{ V}$. The output is a square waveform alternating between $5\text{ V}$ and $-5\text{ V}$, with an edge every $0.2\text{ ms}$.

![operational amplifier differentiator: the input source reaches the inverting input through the capacitor C 1, the resistor R returns from the output to that node while the non-inverting input is grounded, and one current I runs through both](attachments/differentiator.svg)

---

Flashcards for this section are in the following format:

- differentiator relations: $V_{in}(t)$ runs through a capacitor $C_1$ into the inverting terminal, and a resistor $R$ returns from the output; what is $V_o(t)$? ::@:: $I(t) = C_1\frac{dV_{in}(t)}{dt}$, so $V_o(t) = -C_1R\frac{dV_{in}(t)}{dt}$: the output waveform is the derivative of the input waveform.
- draw an operational amplifier differentiator: where do the capacitor $C_1$, the resistor $R$ and the non-inverting terminal connect? ::@:: The capacitor $C_1$ sits in the input path, the resistor $R$ in the feedback path, and the non-inverting terminal goes to ground, so the virtual short holds the inverting terminal at $0\text{ V}$. <p> ![operational amplifier differentiator: the input source reaches the inverting input through the capacitor C 1, the resistor R returns from the output to that node while the non-inverting input is grounded, and one current I runs through both](attachments/differentiator.svg)
- why noise comes out amplified: why does a differentiator built from an operational amplifier amplify high-frequency noise? ::@:: A faster change pushes more current through the same capacitor, so its gain rises with frequency without bound and noise comes out larger than the slow parts of the signal.
- differentiator example, triangular input: $R = 10\text{ k}\Omega$ and $C_1 = 0.05\ \mu\text{F}$, with the input falling from $1\text{ V}$ to $-1\text{ V}$ over $t = 0$ to $t = 0.2\text{ ms}$; what is $V_o$ in that interval? ::@:: The slope is $\frac{-2\text{ V}}{0.2\text{ ms}} = -10{,}000\text{ V/s}$, so $V_o = -(0.05\ \mu\text{F})(10\text{ k}\Omega)\times(-10{,}000\text{ V/s}) = 5\text{ V}$, and the rising edge gives $-5\text{ V}$.
- what waveform the output carries across the $0.2\text{ ms}$ interval ::@:: A square waveform alternating between $5\text{ V}$ and $-5\text{ V}$, with an edge every $0.2\text{ ms}$.
