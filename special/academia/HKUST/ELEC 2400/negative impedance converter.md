---
aliases:
  - ELEC 2400 negative impedance converter
  - ELEC2400 negative impedance converter
  - HKUST ELEC 2400 negative impedance converter
  - HKUST ELEC2400 negative impedance converter
  - NIC
  - negative impedance converter
  - negative resistance converter
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/negative_impedance_converter
  - language/in/English
---

# negative impedance converter

A negative impedance converter (NIC) is a one-port circuit that behaves like a negative resistance: where an ordinary load absorbs energy, it supplies it, and its terminal current runs opposite to its terminal voltage. Built from one [operational amplifier](operational%20amplifier.md), the source $V_s$ holds the non-inverting terminal, so the virtual short fixes the inverting terminal at $V_s$ too. $R_2$ returns from the output to that terminal and $R_1$ drops from it to ground, which makes the output $V = V_s\left(1+\frac{R_2}{R_1}\right)$: the converter is a [non-inverting amplifier](non-inverting%20amplifier.md) with one part added. $R$ bridges the input node to that output and carries $I_i = \frac{V_s - V}{R}$, so the converter presents $R_i = \frac{V_s}{I_i} = -\frac{R R_1}{R_2}$, the negative of a resistance set by the three resistors.

The negative sign comes from where the output sits. Because the inverting terminal is pinned at $V_s$, the divider hanging from the output down to ground has $V_s$ at its tap, and a tap always sits below the output it hangs from. So the output has to climb above $V_s$. $R$ spans $V_s$ and that higher node, so its drop points from the output back towards the input, the other way round from an ordinary resistor. A current running backwards while the terminal voltage stays positive is what a negative resistance looks like from outside.

The circuit is still under negative feedback throughout: $V_+$ is pinned by $V_s$, so a deviation at the inverting terminal is opposed rather than reinforced.

![negative resistance converter: the source holds the non-inverting input, the resistor R bridges the input node to the output, and the inverting input taps the divider of R 2 over R 1 hung from the output, so the resistance looking into the input is minus R 1 over R 2 times R](attachments/negative_impedance_converter.svg)

---

Flashcards for this section are as follows:

- the negative resistance converter: which input holds the source voltage, and what does the divider do? <p> ![negative resistance converter: the source holds the non-inverting input, the resistor R bridges the input node to the output, and the inverting input taps the divider of R 2 over R 1 hung from the output, so the resistance looking into the input is minus R 1 over R 2 times R](attachments/negative_impedance_converter.svg) ::@:: The non-inverting input holds $V_s$, the divider of $R_2$ over $R_1$ feeds the inverting input, and the loop forces the resistance seen at the input to $-(R_1/R_2)R$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- draw a negative resistance converter: how is the divider wired to the two inputs, and what does R bridge? ::@:: The source holds the non-inverting input, the $R_2$ over $R_1$ divider feeds the inverting input, and $R$ bridges the input node to the output. <p> ![negative resistance converter: the source holds the non-inverting input, the resistor R bridges the input node to the output, and the inverting input taps the divider of R 2 over R 1 hung from the output, so the resistance looking into the input is minus R 1 over R 2 times R](attachments/negative_impedance_converter.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- how is a negative resistance converter built from a non-inverting amplifier of gain $1 + \frac{R_2}{R_1}$, and which single resistor is the extra part? ::@:: A non-inverting amplifier of gain $1 + \frac{R_2}{R_1}$, plus one extra resistor $R$ across its input and lifted output, and that resistor is what makes the current run the wrong way.
- what lifts the converter's output above $V_s$, and why does that make the resistance negative? ::@:: $V_s$ drives the non-inverting terminal, so the virtual short puts the inverting terminal at $V_s$ and the divider forces the output above it; $R$ then spans $V_s$ and that higher node, so its current runs the wrong way for a positive input voltage.
- in the negative impedance converter, which direction does the current in $R$ run? ::@:: From the output, which sits above $V_s$, back down to $V_s$, so the circuit sends energy out to whatever it drives instead of absorbing it.
- negative resistance converter: $V_s$ holds the non-inverting terminal of an operational amplifier, $R_2$ returns from the output to the inverting terminal, $R_1$ drops from that terminal to ground, and $R$ carries $I_i = \frac{V_s-V}{R}$; what resistance $R_i = \frac{V_s}{I_i}$ does the converter present? <p> ![negative resistance converter: the source holds the non-inverting input, the resistor R bridges the input node to the output, and the inverting input taps the divider of R 2 over R 1 hung from the output, so the resistance looking into the input is minus R 1 over R 2 times R](attachments/negative_impedance_converter.svg) ::@:: $V = V_s\left(1+\frac{R_2}{R_1}\right)$, so $R_i = \frac{V_s}{I_i} = -\frac{R R_1}{R_2}$: the negative of a resistance set by $R$, $R_1$ and $R_2$.
- feedback in the converter: why does the negative resistance converter stay under negative feedback even though it presents a negative resistance? <p> ![negative resistance converter: the source holds the non-inverting input, the resistor R bridges the input node to the output, and the inverting input taps the divider of R 2 over R 1 hung from the output, so the resistance looking into the input is minus R 1 over R 2 times R](attachments/negative_impedance_converter.svg) ::@:: The $V_+$ node is held fixed by $V_s$, so the loop still opposes deviations at the inverting terminal, and overall the circuit is under negative feedback. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## as a voltage-to-current converter

The load tries to move the node. The converter answers. Change $R_L$ and the node voltage shifts, but the converter's $-R$ shifts it back by the same amount the other way. The voltage across the feeding $R$ stays where it was, and so does the current through it.

Placing a negative resistance converter beside a feeding resistor turns it into a current source with a grounded load. The source reaches the load node through $R$, the converter presents $-R$ at that same node, and the two cancel, so the node's own load current becomes $I_L = \frac{V_s}{R}$ whatever $R_L$ is. The load sits on ground, which the operational amplifier current source cannot do.

![voltage-to-current converter: the source feeds the node through R, the grounded load hangs from that node carrying I L, and the negative resistance converter presenting minus R at the node cancels the feeding resistor, with the node at V 1 and the output at twice V 1](attachments/voltage_to_current_converter.svg)

---

Flashcards for this section are as follows:

- the voltage-to-current converter: how does the drawing make the load current independent of the load? <p> ![voltage-to-current converter: the source feeds the node through R, the grounded load hangs from that node carrying I L, and the negative resistance converter presenting minus R at the node cancels the feeding resistor, with the node at V 1 and the output at twice V 1](attachments/voltage_to_current_converter.svg) ::@:: The converter subtree presents $-R$ at the node, cancelling the $R$ that feeds it from the source, so $I_L=V_s/R$ flows through the grounded load whatever its resistance. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why does changing $R_L$ leave the load current alone? ::@:: The load moves the node voltage and the converter's $-R$ moves it back by the same amount the other way, so the voltage across the feeding $R$ stands still and $I_L=\frac{V_s}{R}$ holds.
- draw the voltage-to-current converter: where does the grounded load hang, and what does the node see in place of $R$? ::@:: The source feeds the node through $R$ and the grounded load draws $I_L$ from it, while the converter presents $-R$ there and cancels the feeding resistor. <p> ![voltage-to-current converter: the source feeds the node through R, the grounded load hangs from that node carrying I L, and the negative resistance converter presenting minus R at the node cancels the feeding resistor, with the node at V 1 and the output at twice V 1](attachments/voltage_to_current_converter.svg)
- build a load-independent current source from a negative resistance converter: what cancels what, and which current follows? <p> ![negative resistance converter: the source holds the non-inverting input, the resistor R bridges the input node to the output, and the inverting input taps the divider of R 2 over R 1 hung from the output, so the resistance looking into the input is minus R 1 over R 2 times R](attachments/negative_impedance_converter.svg) ::@:: The $-R$ seen at the node cancels the feeding $R$, and the load current becomes $I_L=V_s/R$, set by the source and the two equal resistors. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- voltage-to-current converter: a voltage-to-current converter built from a negative resistance converter drives a grounded load $R_L$ from the source $V_s$ through $R$; what current $I_L$ flows, and what is it independent of? <p> ![voltage-to-current converter: the source feeds the node through R, the grounded load hangs from that node carrying I L, and the negative resistance converter presenting minus R at the node cancels the feeding resistor, with the node at V 1 and the output at twice V 1](attachments/voltage_to_current_converter.svg) ::@:: $I_L = \frac{V_s}{R}$, independent of the load resistance $R_L$: another current source, with the load grounded.
