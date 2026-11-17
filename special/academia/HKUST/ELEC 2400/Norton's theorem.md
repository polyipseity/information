---
aliases:
  - ELEC 2400 Norton's theorem
  - ELEC2400 Norton's theorem
  - HKUST ELEC 2400 Norton's theorem
  - HKUST ELEC2400 Norton's theorem
  - Norton equivalent circuit
  - Norton's theorem
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/Norton_s_theorem
  - language/in/English
---

# Norton's theorem

Norton's theorem replaces a whole linear network, seen from a pair of terminals, by one ideal current source in parallel with one resistor. It is the current-source twin of Thévenin's theorem, with voltage and current, series and parallel exchanged.

Its source is the network's short-circuit current. Its resistor is the same equivalent resistance the voltage-source form uses, so either form converts into the other by source transformation.

---

Flashcards for this section are as follows:

- Norton equivalent: what does a whole linear network, seen from a pair of terminals, reduce to? ::@:: An ideal current source $I_{sc}$ in parallel with a resistor $R_{\text{eq}}$. The source is the network's short-circuit current, and the resistor is the resistance at the terminals with the independent sources set to zero. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## equivalent circuit

$I_{sc}$ is the short-circuit current of the network: the current that flows when the terminals are joined. $R_{\text{eq}}$ is the resistance looking in with every independent source set to zero and the dependent sources left operative.

$R_{\text{eq}}$ is the same number as in the Thévenin form, so computing it once serves both. The forms are related by $V_{oc} = I_{sc} R_{\text{eq}}$: the open-circuit voltage is $I_{sc}$ flowing through $R_{\text{eq}}$ alone.

---

Flashcards for this section are as follows:

- equivalent circuit: what two elements make up the Norton equivalent, and how are they joined? ::@:: An ideal current source $I_{sc}$ in parallel with a resistor $R_{\text{eq}}$. The source is the short-circuit current, and the resistor is the same one the Thévenin form uses. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- short-circuit current: what is the current source $I_{sc}$ of a Norton equivalent? ::@:: The short-circuit current of the network, the current that flows when the terminal pair is joined.
- shared resistance: how does the Norton resistance compare with the Thévenin one? ::@:: They are equal: both are the resistance seen at the terminals with the independent sources set to zero.
- relation between forms: how are $V_{oc}$, $I_{sc}$, and $R_{\text{eq}}$ related? ::@:: $V_{oc} = I_{sc} R_{\text{eq}}$, the open-circuit voltage being the source current through the equivalent resistance alone.
- direction of the source: what must be observed about the direction of $I_{sc}$ when drawing the equivalent? ::@:: Its sense must match the short-circuit current you computed. That way the resistor carries the rest, and the terminal current and voltage come out as they did in the original network.

## computing the equivalent

The load is set aside. Joining the terminals and solving for the current through the joint gives the short-circuit current. Zeroing every independent source, voltage sources shorted and current sources opened, and reducing the dead network gives $R_{\text{eq}}$.

Circuit lines in these notes follow one notation. `(X)` names a node, with `(GND)` the zero-volt ground node; `[...]` holds one element, its value and marks spelled out in words; `—` is a wire joining consecutive items; and `A ∥ B` puts two elements in parallel between the same pair of nodes. The line `(A) — [2 Ω] — (B)` reads node $A$ feeding a $2\ \Omega$ resistor that reaches node $B$.

The worked network is the one the Thévenin form uses, drawn `(GND) — [36 V source, + up] — (P) — [4 Ω] — (a)` and `(GND) — [3 Ω ∥ 6 A source, up] — (b)`. A $36\text{ V}$ source sits between ground and a node $P$, a $4\ \Omega$ resistor runs from $P$ to terminal $a$, and terminal $b$ reaches ground through a $3\ \Omega$ resistor that a $6\text{ A}$ source feeds in parallel. Shorting the terminals joins the $4\ \Omega$ resistor to the node where the $3\ \Omega$ resistor and the $6\text{ A}$ source already meet. The current law at that node $V_C$ then gives $\frac{36 - V_C}{4} + 6 = \frac{V_C}{3}$, which is $V_C = \frac{180}{7}\text{ V}$. The short carries the $4\ \Omega$ resistor's own current, $I_{sc} = \frac{36 - V_C}{4\ \Omega} = \frac{18}{7}\text{ A}$. The $7$ in the denominator is no accident: the two forms must satisfy $V_{oc} = I_{sc}R_{\text{eq}}$ for the same network.

Neither source need be known for the reduction to work. An unknown $V_{s1}$ and an unknown $I_{s2}$ sit in a network feeding a load $R$. Shorting the load draws $I_R = 4\text{ A}$, so $I_{sc} = 4\text{ A}$, and zeroing both sources leaves $R_{\text{eq}} = 4\ \Omega$ at the terminals. A $4\ \Omega$ load then takes $I_R = 4\text{ A} \times \frac{4\ \Omega}{4\ \Omega + 4\ \Omega} = 2\text{ A}$.

---

Flashcards for this section are as follows:

- equivalent quantities: how are the short-circuit current and the equivalent resistance each found? ::@:: $I_{sc}$ comes from shorting the terminals and solving for the current through the short, and $R_{\text{eq}}$ from zeroing the independent sources and reducing the network. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- worked short-circuit current: the worked network is `(GND) — [36 V source, + up] — (P) — [4 Ω] — (a)` and `(GND) — [3 Ω ∥ 6 A source, up] — (b)`; with the two terminals shorted together, what is $I_{sc}$? ::@:: The short puts both resistors at one node $V_C$, where the current law gives $\frac{36 - V_C}{4} + 6 = \frac{V_C}{3}$, so $V_C = \frac{180}{7}\text{ V}$ and the short carries the $4\ \Omega$ resistor's current, $I_{sc} = \frac{36 - V_C}{4\ \Omega} = \frac{18}{7}\text{ A}$.
- consistency check: a network has $V_{oc} = 18\text{ V}$, $I_{sc} = \frac{18}{7}\text{ A}$, and $R_{\text{eq}} = 7\ \Omega$; do these agree? ::@:: Yes: $I_{sc}R_{\text{eq}} = \frac{18}{7}\text{ A} \times 7\ \Omega = 18\text{ V} = V_{oc}$.
- reduction with unknown sources: a network holds an unknown $V_{s1}$ and an unknown $I_{s2}$, its shorted load draws $4\text{ A}$, and zeroing both sources leaves $4\ \Omega$ at the terminals; what current reaches a $4\ \Omega$ load? ::@:: Neither source value is needed: $I_{sc} = 4\text{ A}$ and $R_{\text{eq}} = 4\ \Omega$ give $I_R = 4\text{ A} \times \frac{4\ \Omega}{4\ \Omega + 4\ \Omega} = 2\text{ A}$.
- reading a circuit line: in the notation `(X) — [elements] — (Y)`, what do the parentheses, the brackets, the dash, and `∥` mean? ::@:: `(X)` names a node, with `(GND)` the zero-volt ground node; `[...]` holds one element with its value and marks spelled out; `—` is a wire joining consecutive items; and `A ∥ B` puts A and B in parallel between the same pair of nodes.

## series and parallel shortcuts

A resistor in series with an ideal current source can be neglected when other circuit variables are computed. The source fixes the branch current whatever the resistance, so the resistor changes nothing else in the network. A network of $8\text{ A}$ with $2\ \Omega$ in series is therefore equivalent to a bare $8\text{ A}$ source, with $I_{sc} = 8\text{ A}$ and $R_{\text{eq}} = \infty$.

An ideal current source has no open-circuit state, so its Norton resistance is infinite. An ideal voltage source is the mirror image, with zero equivalent resistance.

---

Flashcards for this section are as follows:

- series resistor: what equivalent does an ideal current source with a resistor in series reduce to? ::@:: A resistor in series with an ideal current source may be neglected in computing other circuit variables, leaving $I_{sc} = 8\text{ A}$ and $R_{\text{eq}} = \infty$ for $8\text{ A}$ with $2\ \Omega$ in series. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the series branch drops out: why may a resistor in series with an ideal current source be ignored? ::@:: The source fixes the branch current regardless of the resistance, so the resistor cannot change any other branch current or voltage.
- infinite resistance: why is the Norton resistance of an ideal current source infinite? ::@:: The source delivers its current whatever voltage appears across it, and an infinite resistance is the parallel element that carries no current.
- dual case: what is the equivalent resistance of an ideal voltage source, and why? ::@:: Zero: the source holds its voltage under any current, which is a short circuit.

## in the phasor domain

The short-circuit current phasor takes the place of $I_N$, in parallel with the same $\mathbf{Z}_N = \mathbf{Z}_{th}$ the Thévenin form uses. The source becomes $\mathbf{I}_N = \mathbf{V}_{th}/\mathbf{Z}_{th}$, and that parallel form suits the phasor domain, where admittances add for elements sitting in parallel ([admittance](admittance.md), [phasor](phasor.md)).

---

Flashcards for this section are as follows:

- in the phasor domain / the equivalent: what makes up a Norton equivalent in the phasor domain? ::@:: The short-circuit current phasor $\mathbf{I}_N$ in parallel with $\mathbf{Z}_N = \mathbf{Z}_{th}$, the same impedance the Thévenin form uses. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- in the phasor domain / the conversion: how is the Norton current obtained from the Thévenin pair? ::@:: $\mathbf{I}_N = \mathbf{V}_{th}/\mathbf{Z}_{th}$, a complex division that carries both magnitude and phase. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
