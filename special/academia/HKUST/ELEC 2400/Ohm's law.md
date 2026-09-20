---
aliases:
  - ELEC 2400 Ohm's law
  - ELEC2400 Ohm's law
  - HKUST ELEC 2400 Ohm's law
  - HKUST ELEC2400 Ohm's law
  - Ohm's law
  - conductance
  - resistance
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/Ohm_s_law
  - language/in/English
---

<!-- check: ignore-file[numeric_text_not_latex]: the course alias "ELEC 2400 Ohm's law" reads as a quantity in ohms to the rule -->

# Ohm's law

Applying a voltage across a material drives a current through it. For many materials the current is proportional to that voltage. The constant of proportionality is the resistance $R$, so the relation reads $V = IR$, or $I = GV$ with the conductance $G = 1/R$.

Any two of $V$, $I$, and $R$ fix the third. The relation holds for many materials but not all. A device whose current is not proportional to its voltage cannot be described by one resistance value.

---

Flashcards for this section are as follows:

- overview ::@:: For many materials the current $I$ through a material is proportional to the voltage $V$ across it, with $R$ the constant of proportionality, so $V = IR$, $I = V/R$, and $I = GV$ with $G = 1/R$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- proportionality: a material obeying Ohm's law with resistance $R$ carries current $I$ at voltage $V$; what happens to $I$ when $V$ doubles? ::@:: $I$ doubles.
- proportionality: which ratio of $V$, $I$, and $R$ stays fixed for a material obeying Ohm's law? ::@:: $V/I = R$.
- limits: a device whose current is not proportional to its voltage; what does that rule out about $V = IR$? ::@:: A single constant resistance $R$.

## resistance and conductance

Resistance $R$ measures how much a material opposes the flow of charge. Conductance $G = 1/R$ is its reciprocal. In $V = IR$, the resistance is measured in the ohm, written $\Omega$, and the conductance in the siemens, where $1\text{ S} = 1\ \Omega^{-1}$.

Plotting the current through an element against the voltage across it gives that element's I-V characteristic. A material obeying Ohm's law traces a straight line through the origin of slope $G$.

---

Flashcards for this section are as follows:

- overview ::@:: Resistance $R$ and conductance $G = 1/R$ are reciprocals, so Ohm's law reads $V = IR$ with $R$ in ohms and $I = GV$ with $G$ in siemens. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- unit of resistance: the resistance $R$ that carries $I = 1\text{ A}$ under an applied $V = 1\text{ V}$ ::@:: $V = IR$ gives $R = 1\text{ V}/1\text{ A} = 1\ \Omega$, the ohm, written $\Omega$.
- unit of conductance: which unit does $G = 1/R$ carry, and how is it written in terms of the ohm? ::@:: The siemens, written $\text{S}$, with $1\text{ S} = 1\ \Omega^{-1}$.
- current from voltage and resistance: what current $I$ flows when $V = 6\text{ V}$ is across $R = 3\ \Omega$? ::@:: $I = V/R = 6\text{ V}/3\ \Omega = 2\text{ A}$.
- resistance and conductance from voltage and current: what are $R$ and $G$ for a resistor carrying $I = 2\text{ A}$ with $V = 6\text{ V}$ across it? ::@:: $R = V/I = 6\text{ V}/2\text{ A} = 3\ \Omega$ and $G = 1/R = 1/3\ \Omega^{-1} \approx 0.33\text{ S}$.
- larger resistance against larger conductance: at a fixed $V$, two resistors, one with the larger $R$ and one with the larger $G$; which carries the larger current $I$? ::@:: The one with the larger $G$: $I = V/R = GV$ at fixed $V$.
- I-V characteristic: an element obeying Ohm's law with conductance $G$; what is plotted, and what is the slope? ::@:: The current $I$ through the element against the voltage $V$ across it: a straight line through the origin of slope $G$.

## resistor

A resistor is a device made to have a precise resistance and placed in a circuit to control the current. Its resistance comes from how the device is built rather than from the material at hand. The current a given voltage drives is known in advance.

On a diagram a resistor is a zigzag line labelled $R$, with one terminal marked $+$ and the other $-$. The marks and the current arrow are reference directions chosen for the analysis, not readings off the circuit: the arrow is normally drawn from the $+$ mark to the $-$ mark, and the resistor then obeys $V = +IR$. Reversing the arrow reverses the sign of the current quoted under it, and the relation becomes $V = -IR$.

Water running downhill is the picture for a resistor. Water moves from a higher elevation to a lower elevation. The volume passing each second, in cubic meters per second, measures that flow. In a hose, a pressure difference does the same job. The voltage difference across the resistor is the counterpart of the elevation or pressure difference. The current is the counterpart of the volume of water per second: the positive charge passing a point per second, in coulombs per second, that is, amperes. The resistance is the restriction the path imposes.

---

Flashcards for this section are as follows:

- overview ::@:: A resistor is a device made to have a precise resistance, used in a circuit to control the flow of current.
- precision: what does the precise resistance of a resistor give a circuit designer? ::@:: A resistance fixed by the device, so the current a given voltage drives can be chosen.
- symbol and reference direction: a resistor is drawn with one terminal marked $+$, one marked $-$, and a current arrow between them; what do the marks and the arrow fix? ::@:: Reference directions chosen for the analysis: the marks fix the sign of the voltage $V$ and the arrow the sign of the current $I$.
- arrow from $+$ to $-$: a $4\ \Omega$ resistor carries $I_1 = 2\text{ A}$ along an arrow running from its $+$ mark to its $-$ mark; what is $V$ under those marks? ::@:: $V = +I_1 R = (2\text{ A})(4\ \Omega) = 8\text{ V}$.
- reversed arrow: the arrow on that resistor is reversed while the marks stay, and carries $I_2 = -2\text{ A}$; what is $V$? ::@:: $V = -I_2 R = -(-2\text{ A})(4\ \Omega) = 8\text{ V}$.
- sign of the current: a resistor carries a current arrow $I_1$ with no value written beside it; does the drawing decide whether $I_1$ is positive or negative? ::@:: No: the arrow is a reference direction, so the sign comes from the charge flow it measures.
- analogy by elevation: in the water picture of a resistor, which mechanical quantity plays the part of the voltage difference? ::@:: A difference in elevation: water flows from the higher elevation to the lower one.
- analogy by pressure: in the water picture, which mechanical quantity takes the place of the elevation difference when water is forced through a hose? ::@:: A difference in pressure, driving the water out of the higher-pressure end.
- analogy by flow rate: in the water picture, what corresponds to the electric current, and in which units is each measured? ::@:: The volume of water per second, in cubic meters per second, corresponds to the current, the positive charge per second in coulombs per second, that is amperes.
- analogue of resistance: in the water picture, what does the resistance $R$ represent? ::@:: The restriction the path imposes on the flow: it sets how much current a given voltage difference drives.
