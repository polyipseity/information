---
aliases:
  - ELEC 2400 tutorial 1 tutorial
  - ELEC2400 tutorial 1 tutorial
  - HKUST ELEC 2400 tutorial 1 tutorial
  - HKUST ELEC2400 tutorial 1 tutorial
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/tutorials/tutorial_1/tutorial
  - language/in/English
---

# tutorial

- HKUST ELEC 2400 tutorial 1
- parent: [tutorial 1](index.md)

Every voltage is a difference between two points. A potential quoted at a single point takes a value only once a reference point is fixed; the difference itself is unchanged by that choice.

## measuring voltage

A voltmeter reads the potential difference between the two points its probes touch. The red probe is the positive terminal of the meter and the black probe the negative one, so the reading is $V_{\text{red}} - V_{\text{black}}$.

On a $1.5\text{ V}$ AA cell, the red probe touching the positive terminal and the black probe touching the negative one gives $1.5\text{ V}$. Exchanging the probes keeps the magnitude and reverses the sign, to $-1.5\text{ V}$: $V_{BA} = V_B - V_A = -(V_A - V_B) = -V_{AB}$.

A voltage written on a diagram is read the same way: the value is the potential at the plus mark minus the potential at the minus mark. An element between $A$ and $B$ labelled $V_1$ beside a minus mark at $A$ and a plus mark at $B$ therefore has $V_1 = V_B - V_A = V_{BA} = -V_{AB}$.

---

Flashcards for this section are as follows:

- overview ::@:: A voltmeter reads the potential difference between its two probes.
- meter probes: the red probe touches $A$ and the black probe touches $B$, whose potentials are $V_A$ and $V_B$; what does the meter read? ::@:: $V_A - V_B$.
- correct probes on a cell: a $1.5\text{ V}$ AA cell has its positive terminal at $A$ and its negative terminal at $B$, and the red probe touches $A$ while the black probe touches $B$; what does the meter read? ::@:: $1.5\text{ V}$.
- reversed probes on the cell: a $1.5\text{ V}$ AA cell has its positive terminal at $A$ and its negative terminal at $B$, and the red probe touches $B$ while the black probe touches $A$; what does the meter read? ::@:: $-1.5\text{ V}$.
- subscript order: how do the two ways of quoting the difference between $A$ and $B$ relate? ::@:: $V_{BA} = V_B - V_A = -(V_A - V_B) = -V_{AB}$.
- marked label: an element between $A$ and $B$ carries $V_1$ beside a minus mark at $A$ and a plus mark at $B$; what does the label state? ::@:: $V_1 = V_B - V_A = V_{BA} = -V_{AB}$.

## reference point

A potential quoted at a single point is a difference from a chosen reference, so every quoted potential shifts with that reference. A $1.5\text{ V}$ AA cell standing alone between $A$ and $B$ fixes only their difference, so neither $V_A$ nor $V_B$ has a value on its own.

Taking the point $0$ as the reference gives $V_{CB} = V_C - V_B = V_{C0} - V_{B0}$, and any other reference $A$ gives $V_{CB} = V_{CA} - V_{BA} = (V_C - V_A) - (V_B - V_A) = V_C - V_B$: the reference cancels.

In a $10\text{ V}$ source feeding a $1\ \Omega$ resistor, with $A$ at the source's positive terminal and $B$ at its negative terminal, grounding $B$ puts $V_B$ at $0\text{ V}$ and $V_A$ at $10\text{ V}$. Grounding $A$ instead puts $V_A$ at $0\text{ V}$ and $V_B$ at $-10\text{ V}$. Both grounding choices leave the $10\text{ V}$ across the source unchanged.

Reference marks carry no value of their own: an element between $A$ and $B$ marked only with a positive and a negative terminal leaves both the ordering of the two potentials and their values against zero undecided.

---

Flashcards for this section are as follows:

- overview ::@:: A potential at a single point is quoted against a chosen reference; a difference between two points is not.
- unconnected cell: a $1.5\text{ V}$ AA cell stands between $A$ and $B$ with nothing else connected to it; what are $V_A$ and $V_B$? ::@:: Both stay undetermined: only the difference $V_A - V_B = 1.5\text{ V}$ is fixed.
- reference cancels: with $0$ as the reference point, how is $V_{CB}$ related to $V_{C0}$ and $V_{B0}$? ::@:: $V_{CB} = V_C - V_B = V_{C0} - V_{B0}$.
- ground at the negative terminal: a $10\text{ V}$ source feeds a $1\ \Omega$ resistor, $A$ lies at the source's positive terminal and $B$ at its negative terminal, and $B$ is grounded; what are $V_A$ and $V_B$? ::@:: $V_B = 0\text{ V}$ and $V_A = 10\text{ V}$.
- ground at the positive terminal: a $10\text{ V}$ source feeds a $1\ \Omega$ resistor, $A$ lies at the source's positive terminal and $B$ at its negative terminal, and $A$ is grounded; what are $V_A$ and $V_B$? ::@:: $V_A = 0\text{ V}$ and $V_B = -10\text{ V}$.
- reference marks without a value, ordering: an element between $A$ and $B$ carries a positive mark at one terminal and a negative mark at the other, with no value written; can any ordering of $V_A$ and $V_B$ be decided? ::@:: No: $V_A > V_B$, $V_A < V_B$, and $V_A = V_B$ all stay undecided.
- reference marks without a value, values against zero: an element between $A$ and $B$ carries a positive mark at one terminal and a negative mark at the other, with no value written; what follows about $V_A$ and $V_B$ compared with zero? ::@:: Nothing: $V_A = 0$, $V_A > 0$, $V_B = 0$, and $V_B > 0$ all stay undecided.

## reference directions

The sign in Ohm's law follows the reference direction drawn on the current. With the current arrow running from the plus mark to the minus mark of the resistor voltage, $V = +IR$. With the arrow the other way, $V = -IR$.

A $4\ \Omega$ resistor with $I_1 = 2\text{ A}$ along an arrow running from its plus mark to its minus mark gives $V_1 = +I_1 R = (2\text{ A})(4\ \Omega) = 8\text{ V}$. Reversing the current reference and taking $I_2 = -2\text{ A}$ gives the same $8\text{ V}$: $V_1 = -I_2 R = -(-2\text{ A})(4\ \Omega) = 8\text{ V}$.

The arrow fixes a reference direction, not the sign of the current: only the relation $V_1 = +I_1 R$ is known, and $V_2 = -I_2 R$ once the arrow is reversed.

---

Flashcards for this section are as follows:

- overview: a resistor carries a current reference arrow $I$ and a voltage marked with a plus and a minus mark; how does the sign of the voltage follow the arrow? ::@:: $V = +IR$ when the arrow runs from the plus mark to the minus mark, and $V = -IR$ when the arrow runs the other way.
- matching arrow: a $4\ \Omega$ resistor has $I_1 = 2\text{ A}$ along the arrow that runs from its plus mark to its minus mark; what is $V_1$? ::@:: $V_1 = +I_1 R = (2\text{ A})(4\ \Omega) = 8\text{ V}$.
- reversed arrow: a $4\ \Omega$ resistor has its voltage marked plus at one end and minus at the other, with the current arrow $I_2 = -2\text{ A}$ running from the minus mark to the plus mark; what is $V_1$? ::@:: $V_1 = -I_2 R = -(-2\text{ A})(4\ \Omega) = 8\text{ V}$.
- sign of the current: a current reference arrow $I_1$ is drawn through a resistor with no value given; does the direction fix whether $I_1$ is positive or negative? ::@:: No: the arrow is a reference direction, so $I_1$ may take either sign.
- reversed arrow relation: a resistor carries $V_2$ beside a plus and a minus mark, with the current arrow $I_2$ running from the minus mark to the plus mark; what relation holds? ::@:: $V_2 = -I_2 R$.
