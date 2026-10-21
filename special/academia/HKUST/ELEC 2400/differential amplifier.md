---
aliases:
  - ELEC 2400 differential amplifier
  - ELEC2400 differential amplifier
  - HKUST ELEC 2400 differential amplifier
  - HKUST ELEC2400 differential amplifier
  - difference amplifier
  - differential amplifier
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/differential_amplifier
  - language/in/English
---

# differential amplifier

A differential amplifier amplifies the difference between its two inputs and suppresses whatever those two inputs share. Four resistors and one operational amplifier do it.

---

Flashcards for this section are as follows:

- what does a differential amplifier do with a voltage that appears equally on both of its inputs? ::@:: It suppresses that common part and amplifies only the difference between the two inputs.

## difference amplifier

The four resistors come in two matched pairs. $R_1$ runs from $V_1$ to the inverting terminal, and $R_2$ returns from the output to that terminal. On the other side $R_1$ runs from $V_2$ to the non-inverting terminal, with $R_2$ from there to ground. So $V_+ = \frac{R_2}{R_1+R_2}V_2$. With the virtual short $V_- = V_+$, the inverting-side $R_1$ and $R_2$ carry the same current, so $V_o = \frac{R_2}{R_1}(V_2-V_1)$. This is negative feedback.

The quickest way to read it is an [inverting amplifier](inverting%20amplifier.md) with one extra divider on the other input. Set $V_2$ to zero and what is left is an inverting amplifier, answering $V_1$ with $-\frac{R_2}{R_1}V_1$. Now set $V_1$ to zero instead. The second source reaches the non-inverting terminal through its own $R_1$ and $R_2$ divider, so it arrives scaled by $\frac{R_2}{R_1+R_2}$ and is then amplified by $1+\frac{R_2}{R_1}$, which comes to $\frac{R_2}{R_1}V_2$. Add the two answers and the ratios cancel into $\frac{R_2}{R_1}(V_2-V_1)$. That cancellation is what the matching is for: the $V_2$ side has to divide and amplify by the same ratio the $V_1$ side uses.

With $V_1 = 1\text{ V}$, $V_2 = 2\text{ V}$, $R_1 = 2\text{ k}\Omega$ and $R_2 = 10\text{ k}\Omega$, $V_o = \frac{10\text{ k}\Omega(2\text{ V}-1\text{ V})}{2\text{ k}\Omega} = 5\text{ V}$.

The circuit has two disadvantages. Changing the gain means changing two resistors, all the $R_1$'s or all the $R_2$'s. An ideal voltage amplifier has infinite input resistance, while this circuit presents only $2R_1$. The mesh between $V_1$ and $V_2$ draws $I_{in} = \frac{V_2-V_1}{2R_1}$ from the input pair, a current that grows when $R_1$ is lowered to gain more. The [instrumentation amplifier](instrumentation%20amplifier.md) removes both disadvantages by buffering the two inputs.

![difference amplifier: the source V 1 reaches the inverting input through R 1 with R 2 returning from the output, and the source V 2 reaches the non-inverting input through its own matched R 1 with its own R 2 to ground](attachments/difference_amplifier.svg)

![difference amplifier input mesh: the same four-resistor circuit with a mesh arrow I in through the two matched input resistors, where the input current is the difference of the two source voltages divided by twice R 1](attachments/difference_amplifier_iin_mesh.svg)

---

Flashcards for this section are in the following format:

- the difference amplifier: what makes the four resistors work in matched pairs? ::@:: Both input resistors are $R_1$ and both ground-side resistors are $R_2$, so the output responds to the difference $V_2-V_1$ scaled by $R_2/R_1$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- read the difference amplifier as two half-circuits: what does each of $V_1$ and $V_2$ contribute, and why must the $R_1$ and $R_2$ pairs match? ::@:: $V_1$ alone gives $-\frac{R_2}{R_1}V_1$; $V_2$ alone is scaled by $\frac{R_2}{R_1+R_2}$ and then amplified by $1+\frac{R_2}{R_1}$, which is $\frac{R_2}{R_1}V_2$. The two add to $\frac{R_2}{R_1}(V_2-V_1)$, and equal pairs are what makes the ratios cancel.
- the difference amplifier drives $V_1$ through $R_1$ into a virtual ground; what does $V_2$ drive? ::@:: $R_1$ in series with $R_2$ down to ground, since nothing enters the non-inverting terminal.
- sketch a difference amplifier: which resistor pairs share a value, and which source enters which input? ::@:: $V_1$ enters the inverting input through $R_1$ with $R_2$ in feedback, and $V_2$ enters the non-inverting input through its own $R_1$ with its own $R_2$ to ground. <p> ![difference amplifier: the source V 1 reaches the inverting input through R 1 with R 2 returning from the output, and the source V 2 reaches the non-inverting input through its own matched R 1 with its own R 2 to ground](attachments/difference_amplifier.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the input mesh: why do the two matched input resistors behave as 2 R 1 in series? ::@:: No current enters the op-amp inputs, so the same mesh current $I_{in}=(V_2-V_1)/(2R_1)$ flows through both matched $R_1$ resistors in one loop. <p> ![difference amplifier input mesh: the same four-resistor circuit with a mesh arrow I in through the two matched input resistors, where the input current is the difference of the two source voltages divided by twice R 1](attachments/difference_amplifier_iin_mesh.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- find the input mesh current of a difference amplifier: what is I in in terms of the source difference and R 1? ::@:: $I_{in}=(V_2-V_1)/(2R_1)$, set by the two matched input resistors in series across the source difference. <p> ![difference amplifier input mesh: the same four-resistor circuit with a mesh arrow I in through the two matched input resistors, where the input current is the difference of the two source voltages divided by twice R 1](attachments/difference_amplifier_iin_mesh.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- draw the input mesh on the difference amplifier: where does the loop through $R_1$ run, and what does its arrow mark? ::@:: The same four-resistor circuit, redrawn with a mesh arrow through both matched $R_1$'s from one source toward the other. That arrow marks $I_{in}$. <p> ![difference amplifier input mesh: the same four-resistor circuit with a mesh arrow I in through the two matched input resistors, where the input current is the difference of the two source voltages divided by twice R 1](attachments/difference_amplifier_iin_mesh.svg)
- difference amplifier gain: $V_1$ feeds the inverting terminal of an ideal operational amplifier through $R_1$ with $R_2$ as feedback, and $V_2$ feeds the non-inverting terminal through $R_1$ with $R_2$ to ground; what is $V_o$? ::@:: $V_o = \frac{R_2}{R_1}(V_2-V_1)$, the amplified difference of the two inputs.
- difference amplifier numbers: a difference amplifier with $R_1 = 2\text{ k}\Omega$ and $R_2 = 10\text{ k}\Omega$ takes $V_1 = 1\text{ V}$ and $V_2 = 2\text{ V}$; what is its output $V_o$? ::@:: $V_o = \frac{10\text{ k}\Omega(2\text{ V}-1\text{ V})}{2\text{ k}\Omega} = 5\text{ V}$.
- difference amplifier disadvantages: why does adjusting the difference amplifier's gain cost two resistor changes, and what input resistance does it present instead of the infinite value an ideal voltage amplifier promises? ::@:: The gain change must touch all the $R_1$'s or all the $R_2$'s, and the input resistance is only $2R_1$, drawing $I_{in} = \frac{V_2-V_1}{2R_1}$ from the input pair, a current that grows as $R_1$ is lowered for more gain. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
