---
aliases:
  - ELEC 2400 Kirchhoff's circuit laws
  - ELEC2400 Kirchhoff's circuit laws
  - HKUST ELEC 2400 Kirchhoff's circuit laws
  - HKUST ELEC2400 Kirchhoff's circuit laws
  - KCL
  - KVL
  - Kirchhoff's circuit laws
  - Kirchhoff's current law
  - Kirchhoff's voltage law
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/Kirchhoff_s_circuit_laws
  - language/in/English
---

# Kirchhoff's circuit laws

Kirchhoff's circuit laws are the two equalities that govern the currents and voltages of the lumped-element model. Kirchhoff's current law constrains the currents meeting at a node, Kirchhoff's voltage law the voltages taken round a loop, and both hold at every instant, so they apply to a changing circuit as well as a steady one.

Each rests on a conservation principle: the current law on charge, the voltage law on energy. That is what sets the assumptions under which each may be used.

---

Flashcards for this section are as follows:

- overview ::@:: Kirchhoff's circuit laws are the two instantaneous equalities of the lumped-element model: the current law constrains the currents at a node and the voltage law constrains the voltages round a loop.
- namesake ::@:: Gustav Robert Kirchhoff, who lived from 1824 to 1887.

<!-- check: ignore-next-line[header_style]: Kirchhoff is a proper noun -->
## Kirchhoff's current law

Kirchhoff's current law states that at any instant the algebraic sum of the currents entering a node is zero, $\sum i = 0$, a current leaving the node counting with the opposite sign. It reads more conveniently as current in equals current out, $\sum I_{\text{in}} = \sum I_{\text{out}}$.

The law follows from [conservation of charge](electric%20charge.md#conservation%20of%20charge): charge entering a node must leave it instantaneously, so the net charge does not accumulate, and $\sum q_i = 0$ gives $\frac{d}{dt}\sum q_i = 0$.

The derivation assumes something further, that the net charge inside each element does not change, so an element passes on what enters it. Writing $q_i$ for the net charge inside the $i$-th element, a different quantity from the charge that has moved through a given plane, the assumption is $\frac{dq_i}{dt} = 0$ for every element, and it makes the current the same on both sides of an element.

At a node fed by five currents it gives $I_1 - I_2 + I_3 - I_4 + I_5 = 0$ where $I_2$ and $I_4$ leave, or $I_1 + I_3 + I_5 = I_2 + I_4$ in current-in, current-out form. A five-node circuit gives $I_1 + I_2 = 0$ at A, $I_2 = I_3 + I_5$ at B, $I_3 = I_4 + I_7$ at C, $I_5 + I_7 = I_6$ at D, and $I_1 + I_4 + I_6 = 0$ at E. Where $I_1 = 5\text{ A}$ meets $I_8 = -2\text{ A}$, $I_1 = I_6 + I_8$ gives $I_6 = 7\text{ A}$; sources of $10\text{ A}$ and $5\text{ A}$ feeding one node deliver $I = 15\text{ A}$ to the branch that remains; and a node admitting $5\text{ A}$ while sending out $10\text{ A}$ admits no solution, so the circuit is invalid.

Two nodes joined by a wire are one node, since the wire holds no element, but the current through that wire is not determined by the fact, and the voltage between the two points is zero.

Which direction counts as positive is a free choice. With $i_1$ and $i_2$ drawn into a node and $i_3$ and $i_4$ drawn out, taking _in_ as positive gives $i_1 + i_2 + (-1)i_3 + (-1)i_4 = 0$, while taking _out_ as positive gives $(-1)i_1 + (-1)i_2 + i_3 + i_4 = 0$; the two constrain the node identically. When every branch arrow is drawn into the node the signed form degenerates to the bare sum $i_1 + i_2 + i_3 + i_4 = 0$, which forces some values to be negative: currents that all run inward cannot otherwise sum to zero.

---

Flashcards for this section are as follows:

- overview ::@:: At any instant the algebraic sum of the currents entering a node is zero, equivalently current in equals current out.
- signed sum at a node: a node receives $I_1$, $I_3$, and $I_5$ and sends out $I_2$ and $I_4$; what equation does the current law give, in both forms? ::@:: $I_1 + I_3 + I_5 = I_2 + I_4$, or $I_1 - I_2 + I_3 - I_4 + I_5 = 0$ with $I_2$ and $I_4$ counted negative.
- conservation basis: which conservation principle does $\sum i = 0$ follow from, and through what intermediate statement? ::@:: Conservation of charge: the net charge at a node does not accumulate, so $\sum q_i = 0$ implies $\sum i = 0$.
- element assumption: what must be assumed about $\frac{dq_i}{dt}$ inside each circuit element for the current on both sides of it to be equal? ::@:: That the net charge inside each element does not change, $\frac{dq_i}{dt} = 0$.
- invalid circuit: a $10\text{ A}$ source runs from A to B while a $5\text{ A}$ source feeds A; what does the current law say at A? ::@:: $5\text{ A} \ne 10\text{ A}$, so no solution exists and the circuit is invalid.
- five-node circuit: a circuit has nodes A to E carrying currents $I_1$ to $I_7$; what equation does the current law give at each node? ::@:: $I_1 + I_2 = 0$ at A, $I_2 = I_3 + I_5$ at B, $I_3 = I_4 + I_7$ at C, $I_5 + I_7 = I_6$ at D, and $I_1 + I_4 + I_6 = 0$ at E.
- parallel sources feeding a node: sources of $10\text{ A}$ and $5\text{ A}$ feed one node and a single branch carries what remains; what current does that branch carry? ::@:: $I = 10\text{ A} + 5\text{ A} = 15\text{ A}$.
- unknown branch current: a node receives $I_1 = 5\text{ A}$ and sends out $I_8 = -2\text{ A}$ along one branch; what is the remaining outgoing current $I_6$? ::@:: $I_1 = I_6 + I_8$ gives $I_6 = I_1 - I_8 = 5\text{ A} - (-2\text{ A}) = 7\text{ A}$.
- wire between nodes: two nodes are joined by a wire alone; are they one node, what is $V_{AB}$, and is the wire current $I_y$ determined? ::@:: They are one node and the voltage between them is $V_{AB} = 0$, but the wire current cannot be determined from that fact.
- choosing the positive direction: a node has $i_1$ and $i_2$ drawn in and $i_3$ and $i_4$ drawn out; what do the two signed forms of the law give, and do they constrain the node in the same way? ::@:: Taking _in_ as positive gives $i_1 + i_2 + (-1)i_3 + (-1)i_4 = 0$ and taking _out_ as positive gives $(-1)i_1 + (-1)i_2 + i_3 + i_4 = 0$; they constrain it identically.
- all arrows drawn inward: four branch currents $i_1$ to $i_4$ all have their arrows drawn into the node, with values $3\text{ A}$, $2\text{ A}$, $-4\text{ A}$, and $-1\text{ A}$; what does the law give? ::@:: $i_1 + i_2 + i_3 + i_4 = 0$, satisfied as $(+3) + (+2) + (-4) + (-1) = 0$ and as $(-3) + (-2) + (+4) + (+1) = 0$.
- why some values must be negative: four branch currents all have their arrows drawn into one node; why must some of the values come out negative? ::@:: Currents that all run inward can sum to zero only if some of them in fact run outward, against their arrows.

<!-- check: ignore-next-line[header_style]: Kirchhoff is a proper noun -->
## Kirchhoff's voltage law

Kirchhoff's voltage law states that at any instant the algebraic sum of the branch voltages around a loop is zero, $\sum v_i = 0$, a voltage rise counting positive and a drop negative.

It holds only when the electric field is conservative, which needs no varying magnetic field through the circuit outside its elements, so that no invisible source arises from induction. Faraday's law gives the voltage round a loop as $\oint E \cdot dl = -\iint \frac{\partial B}{\partial t} \cdot dS$, which vanishes exactly when the flux term does.

Reading a loop means summing the marked voltages in one direction, and the loop need not be a walkable path. A mesh holding a $5\text{ V}$ source, a $10\text{ V}$ source, and an unknown $V_o$, tracked through the rises, gives $-5\text{ V} - 10\text{ V} + V_o = 0$, so $V_o = 15\text{ V}$; a mesh whose sources of $10\text{ V}$ and $5\text{ V}$ act in parallel gives $10\text{ V} - 5\text{ V} = 5\text{ V} \ne 0$ and so has no solution, which is why unequal voltage sources cannot be connected in parallel.

A loop driven by a current source alone shows the discipline in reverse. A $2\text{ A}$ source in series with a $4\text{ V}$ source and a $2\ \Omega$ resistor forces $I_R = 2\text{ A}$, so the marked voltage across the resistor is $V_2 = -I_R \times 2\ \Omega = -4\text{ V}$, its marked polarity opposing the current, and $4\text{ V} + V_1 = -V_2$ gives $V_1 = 0\text{ V}$ across the source. With the $4\text{ V}$ source and the $2\ \Omega$ resistor sharing a node across a $2\text{ A}$ source instead, $I_1 = \frac{4\text{ V}}{2\ \Omega} = 2\text{ A}$, $I_2 = I_1 - 2\text{ A} = 0\text{ A}$, and $V_A = -4\text{ V}$. Grounding the same loop at its far end instead gives $V_D = 4\text{ V}$ and $V_C = V_D + 2\text{ A} \times 4\ \Omega = 12\text{ V}$.

The sign of a term is fixed by the element's marked polarity read against the direction of travel: passing from the $-$ mark to the $+$ mark is a rise and counts positive, passing from $+$ to $-$ a drop and counts negative. Marks facing opposite ways round a loop therefore always carry opposite signs, as with $V_1 + V_2 = 0$ for a source marked $+$ at the top beside a load marked $-$ at the top, and reversing both marks gives $(-1)V_1 + V_2 = 0$ in which $V_1$ negative goes with $V_2$ negative. A longer loop is read the same way, one element at a time, each term taking the sign of its own mark against the direction of travel.

---

Flashcards for this section are as follows:

- overview ::@:: At any instant the algebraic sum of the branch voltages around a loop is zero, counting a rise as positive and a drop as negative.
- sign convention: a loop is tracked through a resistor and then through a source; which sign does a voltage rise take and which a drop? ::@:: A rise is positive and a drop is negative.
- field assumption: under what condition on the electric field does the voltage law hold? ::@:: Only when the field is conservative, which requires that no varying magnetic field links the circuit outside its elements.
- induction: Faraday's law gives the voltage round a loop as a closed line integral of $E$; what makes it zero? ::@:: The magnetic flux term $-\iint \frac{\partial B}{\partial t} \cdot dS$ vanishes when no varying magnetic field passes through the circuit.
- loop walk: a loop visits nodes $A \to B \to C \to D \to E \to A$; must that sequence be a physically walkable path? ::@:: No: it is a reading order for the branch voltages, not a route anyone travels.
- reading a loop: in which direction are a loop's marked branch voltages summed, and what fixes each one's sign? ::@:: In one chosen direction, with each voltage taking the sign its own mark gives read against that direction.
- unknown mesh voltage: a clockwise mesh holds a $5\text{ V}$ source and a $10\text{ V}$ source in the same sense and an unknown $V_o$ opposed to them; what is $V_o$? ::@:: $-5\text{ V} - 10\text{ V} + V_o = 0$, so $V_o = 15\text{ V}$.
- unequal parallel sources: a mesh has a $10\text{ V}$ source and a $5\text{ V}$ source in parallel; what does the voltage law give, and what follows? ::@:: $10\text{ V} - 5\text{ V} = 5\text{ V} \ne 0$, so no solution exists and the circuit is invalid: unequal voltage sources cannot be connected in parallel.
- series current source: a $2\text{ A}$ source drives a loop holding a $4\text{ V}$ source and a $2\ \Omega$ resistor whose marked voltage $V_2$ opposes the current; find $I_R$ and $V_2$. ::@:: $I_R = 2\text{ A}$ and $V_2 = -I_R \times 2\ \Omega = -4\text{ V}$, since the marked polarity is opposite to the current.
- voltage across a current source: in that $2\text{ A}$ loop the $4\text{ V}$ source opposes the marked $V_2 = -4\text{ V}$; what is the voltage $V_1$ across the current source? ::@:: $4\text{ V} + V_1 = -V_2 = 4\text{ V}$, so $V_1 = 0\text{ V}$.
- current source against a voltage source: a $4\text{ V}$ source sits between ground and a node shared by a $2\ \Omega$ resistor and a $2\text{ A}$ source; find $I_1$, $I_2$, and $V_A$. ::@:: $I_1 = \frac{4\text{ V}}{2\ \Omega} = 2\text{ A}$, $I_2 = I_1 - 2\text{ A} = 0\text{ A}$, and $V_A = 0 - 4\text{ V} = -4\text{ V}$.
- node voltages in a loop: a $2\text{ A}$ source drives a $4\ \Omega$ resistor and a $4\text{ V}$ source in series, with $V_A$ between them; find $I_{R1}$, $V_A$, and $V_B$ at the source's far terminal. ::@:: $I_{R1} = 2\text{ A}$, $V_A = 0 - 2\text{ A} \times 4\ \Omega = -8\text{ V}$, and $V_B = V_A - 4\text{ V} = -12\text{ V}$.
- mirrored loop: the same loop is grounded at its far end instead; find $I_{R2}$, $V_D$, and $V_C$. ::@:: $I_{R2} = 2\text{ A}$, $V_D = 0 + 4\text{ V} = 4\text{ V}$, and $V_C = V_D + 2\text{ A} \times 4\ \Omega = 12\text{ V}$.
- sign against the marked polarity: a loop is tracked through an element; what sign does passing from its $-$ mark to its $+$ mark take, and what does passing the other way take? ::@:: A rise from $-$ to $+$ counts positive, and a drop from $+$ to $-$ counts negative.
- marks facing opposite ways: a loop holds a source marked $+$ at the top beside a load marked $-$ at the top; what equation does the law give, and what follows? ::@:: $V_1 + V_2 = 0$, so the two always carry opposite signs.
- reversing both marks: both elements of that loop have their marks reversed; what equation does the law give, and what follows? ::@:: $(-1)V_1 + V_2 = 0$, in which $V_1$ negative goes with $V_2$ negative and $V_1$ positive with $V_2$ positive. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- a longer loop: does the sign of a term depend on how many elements the loop holds? ::@:: No: each term takes the sign of its own mark read against the direction of travel, whatever the loop's length.

### reversing every mark in a loop

Reversing the marks on every element of a loop negates every term of its equation and leaves the solution unchanged, so the two readings of one loop are the same constraint. A $24\text{ V}$ source, a $6\ \Omega$ resistor, and a $2\ \Omega$ resistor in one loop, with the current $I_1$ running through the $6\ \Omega$ and on down through the $2\ \Omega$, reads as $V_1 + V_2 + V_3 = 0$ and so as $+(24 - 0) + (-I_1)(6) + (-I_1)(2) = 0$, which gives $24 = 8I_1$ and $I_1 = 3\text{ A}$. Reversing the marks on the source and on the $6\ \Omega$ reads as $(-V_1) + (-V_2) + V_3 = 0$ and expands to $+[-(0 - 24)] + [-(I_1)(6)] + (-I_1)(2) = 0$, giving the same $24 = 8I_1$ and the same $I_1 = 3\text{ A}$.

---

Flashcards for this section are as follows:

- overview ::@:: Reversing the marks on every element of a loop negates each term of its equation and leaves the solution unchanged, so both readings state the same constraint.
- the first reading: a $24\text{ V}$ source, a $6\ \Omega$, and a $2\ \Omega$ in one loop carry $I_1$ through the $6\ \Omega$ and down through the $2\ \Omega$; what does the loop equation give? ::@:: $V_1 + V_2 + V_3 = 0$, that is $+(24 - 0) + (-I_1)(6) + (-I_1)(2) = 0$, so $24 = 8I_1$ and $I_1 = 3\text{ A}$.
- the reversed reading: the marks on the source and on the $6\ \Omega$ are reversed in that same loop; what does the equation give? ::@:: $(-V_1) + (-V_2) + V_3 = 0$, that is $+[-(0 - 24)] + [-(I_1)(6)] + (-I_1)(2) = 0$, giving the same $I_1 = 3\text{ A}$.

## ground reference

The voltage law follows from conservation of energy, with voltage the energy per unit charge, $V = E/q$: a gain in energy between two points is a voltage rise and a loss a drop.

Voltage is relative, so one node is taken as the [ground reference](voltage.md#ground%20reference) and assigned $0\text{ V}$, drawn as stacked horizontal strokes. Ground here is a node designation, not a physical connection to earth.

With a ground node the voltage law restates as: the voltage at a node, referred to ground, is the algebraic sum of the branch voltages along any path from ground to that node, independent of which path is taken. A node reached one way through $+3\text{ V}$, $+2\text{ V}$, and $-4\text{ V}$ and another way through $+5\text{ V}$, $-10\text{ V}$, and $+6\text{ V}$ has node voltage $1\text{ V}$ either way.

---

Flashcards for this section are as follows:

- overview ::@:: One circuit node is designated ground and assigned $0\text{ V}$; <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> every other node voltage is the sum of the branch voltages along any path from ground to it, and that sum does not depend on the path.
- energy basis: how does the voltage law follow from conservation of energy and $V = E/q$? ::@:: Voltage is energy per unit charge, $V = E/q$, so a gain in energy along a branch is a voltage rise and a loss is a drop, and the rises and drops round a closed loop cancel.
- path independence: a node is reached from ground by two different paths; do the two branch-voltage sums agree? ::@:: Yes: the node voltage referred to ground is the same along every path, since both sums are that node voltage.
- path sum: a node is reached from ground through branches bearing $+3\text{ V}$, $+2\text{ V}$, and $-4\text{ V}$, and by another route through $+5\text{ V}$, $-10\text{ V}$, and $+6\text{ V}$; what is the node voltage? ::@:: $+3\text{ V} + 2\text{ V} - 4\text{ V} = 1\text{ V}$, and the other route gives $+5\text{ V} - 10\text{ V} + 6\text{ V} = 1\text{ V}$ as well.
- ground symbol: how is a ground node drawn, and must it be connected to earth? ::@:: As stacked horizontal strokes at the node; it is usually only a node designation, not a physical earth connection.

## external ground and supply connections

A circuit connected to the outside only through a single ground connection carries no current there, $I_{GND} = 0$, since the ground is a dead end with no return path.

With several ground connections the individual currents need not vanish, but their total does, $I_{GND1} + I_{GND2} + I_{GND3} = 0$, since no charge accumulates in the circuit.

With supplies connected as well, the total current entering through the supplies equals the total leaving through the grounds, $I_{S1} + I_{S2} = I_{GND1} + I_{GND2} + I_{GND3}$.

---

Flashcards for this section are as follows:

- overview ::@:: A circuit with one external ground connection carries no current there; with several grounds the currents need not each vanish but sum to zero, and with supplies connected the total supply current equals the total ground current.
- single ground: a circuit has one ground connection and no other external connection; what is the ground current $I_{GND}$? ::@:: $I_{GND} = 0$: the ground is a dead end with no return path.
- several grounds: a circuit has three ground connections but no supply connection; what constrains $I_{GND1}$, $I_{GND2}$, and $I_{GND3}$? ::@:: Their total is zero, $I_{GND1} + I_{GND2} + I_{GND3} = 0$; they need not each be zero.
- supplies and grounds together: a circuit is fed by two supplies $I_{S1}$ and $I_{S2}$ and grounded at three points $I_{GND1}$ to $I_{GND3}$; how do the five currents relate? ::@:: The total supply current equals the total ground current, $I_{S1} + I_{S2} = I_{GND1} + I_{GND2} + I_{GND3}$.
