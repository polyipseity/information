---
aliases:
  - ELEC 2400 week 3 tutorial 1 tutorial
  - ELEC2400 week 3 tutorial 1 tutorial
  - HKUST ELEC 2400 week 3 tutorial 1 tutorial
  - HKUST ELEC2400 week 3 tutorial 1 tutorial
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/tutorials/week_3_tutorial_1/tutorial
  - language/in/English
---

# tutorial

- HKUST ELEC 2400 week 3 tutorial 1
- parent: [week 3 tutorial 1](index.md)

## sign of Ohm's law under the reference direction

A $4\ \Omega$ resistor marked $+$ at one end and $-$ at the other obeys $V_1 = +I_1R$ while its current arrow runs from the $+$ mark to the $-$ mark, so $I_1 = 2\text{ A}$ gives $V_1 = +(2\text{ A})(4\ \Omega) = +8\text{ V}$. With the arrow reversed the relation flips to $V_1 = -I_1R$, and the value written $I_1 = -2\text{ A}$ gives $V_1 = -(-2\text{ A})(4\ \Omega) = +8\text{ V}$: the two drawings describe one physical situation, so both readings agree. <p> ![a resistor marked plus at one end and minus at the other, with a current arrow below it running from the plus mark to the minus mark](../../attachments/reference_direction_with.svg) ![the same resistor with the current arrow below it running from the minus mark to the plus mark](../../attachments/reference_direction_against.svg)

---

Flashcards for this section are as follows:

- arrow with the marks: a $4\ \Omega$ resistor carries $V_1$ between a $+$ and a $-$ mark, and its current arrow $I_1 = 2\text{ A}$ runs from the $+$ mark to the $-$ mark; what is $V_1$? ::@:: $V_1 = +I_1R = +(2\text{ A})(4\ \Omega) = +8\text{ V}$.
- arrow against the marks: a $4\ \Omega$ resistor carries $V_1$ between a $+$ and a $-$ mark, and its current arrow points from the $-$ mark to the $+$ mark with the value $I_1 = -2\text{ A}$; what is $V_1$? ::@:: $V_1 = -I_1R = -(-2\text{ A})(4\ \Omega) = +8\text{ V}$, the same voltage the matching arrow gave.

## current law at a node and voltage law round a loop

Kirchhoff's current law (KCL) holds at every node, $\sum I = 0$, written just as well as current in equals current out, $\sum I_{\text{in}} = \sum I_{\text{out}}$; it is conservation of charge. Kirchhoff's voltage law (KVL) holds round every closed loop, $\sum V = 0$; it is conservation of energy.

A lattice of resistors fed by one source marks $V_1$, $V_2$, and $I_1$ on three of its branches and needs nothing beyond $V = IR$, $\sum I = 0$, and $\sum V = 0$. Ohm's law turns each branch current into a branch voltage, the current law ties the currents at each node, and the voltage law ties the voltages round each loop, and the three marked quantities fall out.

---

Flashcards for this section are as follows:

- the current law: what does Kirchhoff's current law (KCL) state at a node, and which conservation principle underlies it? ::@:: At any node $\sum I = 0$, equivalently $\sum I_{\text{in}} = \sum I_{\text{out}}$; it is conservation of charge. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the voltage law: what does Kirchhoff's voltage law (KVL) state round a closed loop, and which conservation principle underlies it? ::@:: Round any closed loop $\sum V = 0$; it is conservation of energy. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the three relations: a lattice of resistors fed by a source has $V_1$, $V_2$, and $I_1$ marked on three branches; which three relations determine all three? ::@:: $V = IR$ for each branch, $\sum I = 0$ at each node, and $\sum V = 0$ round each loop.

## voltage divider

Two resistors in series across a source split it in the ratio of their resistances: the output taken across $R_2$ is $V_{\text{out}} = \frac{R_2}{R_1 + R_2}V_{\text{in}}$.

The voltage law derives it in three steps. The loop gives $V_{\text{in}} = V_1 + V_{\text{out}}$, and the shared series current is $I_1 = \frac{V_{\text{in}}}{R_1 + R_2}$. The drop across $R_1$ is $I_1R_1$, so $V_{\text{out}} = V_{\text{in}} - I_1R_1 = \frac{R_2}{R_1 + R_2}V_{\text{in}}$. The resistance the output is taken across sits in the numerator.

---

Flashcards for this section are as follows:

- divider ratio: two resistors $R_1$ and $R_2$ sit in series across $V_{\text{in}}$ with the output across $R_2$; what is $V_{\text{out}}$? ::@:: $V_{\text{out}} = \frac{R_2}{R_1 + R_2}V_{\text{in}}$, the output resistor over the sum.
- deriving the ratio: two resistors $R_1$ and $R_2$ sit in series across $V_{\text{in}}$ with the output across $R_2$; derive $V_{\text{out}}$ from the voltage law. ::@:: The loop gives $V_{\text{in}} = V_1 + V_{\text{out}}$ and $I_1 = \frac{V_{\text{in}}}{R_1 + R_2}$, so $V_{\text{out}} = V_{\text{in}} - I_1R_1 = \frac{R_2}{R_1 + R_2}V_{\text{in}}$.

## current divider

Two resistors in parallel fed by a current source split it inversely: the wanted branch current is $I_{\text{out}} = \frac{R_1}{R_1 + R_2}I_{\text{in}}$, carrying the _other_ resistance in the numerator.

The current law derives it. The parallel branches share one voltage, so $I_1R_1 = I_{\text{out}}R_2$ and $I_1 = I_{\text{out}}\frac{R_2}{R_1}$; substituting into $I_{\text{in}} = I_1 + I_{\text{out}}$ leaves $I_{\text{out}} = \frac{R_1}{R_1 + R_2}I_{\text{in}}$.

---

Flashcards for this section are as follows:

- divider ratio: a current source $I_{\text{in}}$ feeds $R_1$ and $R_2$ in parallel, and $I_{\text{out}}$ is wanted through $R_2$; what is $I_{\text{out}}$? ::@:: $I_{\text{out}} = \frac{R_1}{R_1 + R_2}I_{\text{in}}$, the opposite resistance in the numerator.
- deriving the ratio: a current source $I_{\text{in}}$ feeds $R_1$ and $R_2$ in parallel, and $I_{\text{out}}$ runs through $R_2$; derive $I_{\text{out}}$ from the current law. ::@:: The shared voltage gives $I_1R_1 = I_{\text{out}}R_2$, so $I_1 = I_{\text{out}}\frac{R_2}{R_1}$; then $I_{\text{in}} = I_1 + I_{\text{out}}$ yields $I_{\text{out}} = \frac{R_1}{R_1 + R_2}I_{\text{in}}$.

## nodal analysis at one node

One node $A$ above ground gathers three branches: a $1\ \Omega$ resistor in series with a $10\text{ V}$ source, a $2\ \Omega$ resistor, and a $6.38\ \Omega$ resistor. Each branch current is written toward $A$ as its own end's voltage minus $V_A$ over its resistance, $I_1 = \frac{10 - V_A}{1}$, $I_2 = \frac{0 - V_A}{2}$, and $I = \frac{0 - V_A}{6.38}$.

The current law $I_1 + I_2 + I = 0$ then solves in one unknown and gives $V_A = 6.04\text{ V}$. The $6.38\ \Omega$ branch carries $I = \frac{0 - V_A}{6.38} = -0.947\text{ A}$, whose minus sign says the current runs away from $A$, against its arrow.

---

Flashcards for this section are as follows:

- branch expressions: node $A$ above ground gathers a $1\ \Omega$ resistor in series with a $10\text{ V}$ source, a $2\ \Omega$ resistor, and a $6.38\ \Omega$ resistor, each current drawn toward $A$; write the three branch currents and the node equation. ::@:: $I_1 = \frac{10 - V_A}{1}$, $I_2 = \frac{0 - V_A}{2}$, $I = \frac{0 - V_A}{6.38}$, with $I_1 + I_2 + I = 0$.
- node voltage: the current law at node $A$ reads $\frac{10 - V_A}{1} + \frac{0 - V_A}{2} + \frac{0 - V_A}{6.38} = 0$; what is $V_A$? ::@:: $V_A = 6.04\text{ V}$.
- branch current: node $A$ sits at $V_A = 6.04\text{ V}$ above ground, and a $6.38\ \Omega$ resistor joins it to ground with its current $I$ drawn toward $A$; what is $I$, and what does its sign mean? ::@:: $I = \frac{0 - V_A}{6.38} = -0.947\text{ A}$: the minus sign says the current in fact runs away from $A$, against its arrow.
