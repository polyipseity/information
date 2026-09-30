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

The current source is the network's short-circuit current and the resistor is the same equivalent resistance the voltage-source form uses, so either form converts into the other by source transformation.

---

Flashcards for this section are as follows:

- overview ::@:: A linear network seen from a terminal pair can be replaced by an ideal current source $I_{sc}$ in parallel with a resistor $R_{\text{eq}}$, where $I_{sc}$ is the short-circuit current and $R_{\text{eq}}$ the resistance at the terminals with independent sources set to zero. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## the equivalent circuit

The equivalent is an ideal current source $I_{sc}$ in parallel with a resistor $R_{\text{eq}}$. $I_{sc}$ is the short-circuit current of the network, the current that flows when the terminals are joined; $R_{\text{eq}}$ is the resistance looking in with every independent source set to zero and dependent sources left operative.

$R_{\text{eq}}$ is the same number as in the Thévenin form, so computing it once serves both. The forms are related by $V_{oc} = I_{sc} R_{\text{eq}}$: the open-circuit voltage is $I_{sc}$ flowing through $R_{\text{eq}}$ alone.

---

Flashcards for this section are as follows:

- overview ::@:: The equivalent circuit is $I_{sc}$ in parallel with $R_{\text{eq}}$, $I_{sc}$ being the short-circuit current and $R_{\text{eq}}$ the same resistance as in the Thévenin form. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- short-circuit current: what is the current source $I_{sc}$ of a Norton equivalent? ::@:: The short-circuit current of the network, the current that flows when the terminal pair is joined.
- shared resistance: how does the Norton resistance compare with the Thévenin one? ::@:: They are equal: both are the resistance seen at the terminals with the independent sources set to zero.
- relation between forms: how are $V_{oc}$, $I_{sc}$, and $R_{\text{eq}}$ related? ::@:: $V_{oc} = I_{sc} R_{\text{eq}}$, the open-circuit voltage being the source current through the equivalent resistance alone.
- direction of the source: what must be observed about the direction of $I_{sc}$ when drawing the equivalent? ::@:: Its sense, which must match the short-circuit current so that the parallel resistor carries the correct remaining current.

## computing the equivalent

The load is set aside. The short-circuit current comes from joining the terminals and solving for the current through the joint; $R_{\text{eq}}$ comes from zeroing every independent source, voltage sources shorted and current sources opened, and reducing the dead network.

For a network of $4\ \Omega$, $36\text{ V}$, $3\ \Omega$, and $6\text{ A}$ with $R_{\text{eq}} = 7\ \Omega$, the current law at the node above the short gives $\frac{36 - V_C}{4} = \frac{V_C}{3} + 6$, so $V_C = \frac{72}{7}\text{ V}$ and $I_{sc} = \frac{V_C}{4\ \Omega} = \frac{18}{7}\text{ A}$. The $7$ in the denominator is no accident: the two forms must satisfy $V_{oc} = I_{sc}R_{\text{eq}}$ for the same network.

Neither source need be known for the reduction to work. An unknown $V_{s1}$ with $2\ \Omega$ and an unknown $I_{s2}$ with $4\ \Omega$ sit in a network feeding a load $R$: shorting the load draws $I_R = 4\text{ A}$, so $I_{sc} = 4\text{ A}$; zeroing the sources leaves $R_{\text{eq}} = 4\ \Omega$, and a $4\ \Omega$ load takes $I_R = 4\text{ A} \times \frac{4\ \Omega}{4\ \Omega + 4\ \Omega} = 2\text{ A}$.

---

Flashcards for this section are as follows:

- overview ::@:: $I_{sc}$ comes from shorting the terminals and solving for the current through the short, and $R_{\text{eq}}$ from zeroing the independent sources and reducing the network. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- worked short-circuit current: the network of $4\ \Omega$, $36\text{ V}$, $3\ \Omega$, and $6\text{ A}$ has $R_{\text{eq}} = 7\ \Omega$; how is its $I_{sc}$ found? ::@:: The current law at the node above the short gives $\frac{36 - V_C}{4} = \frac{V_C}{3} + 6$, so $V_C = \frac{72}{7}\text{ V}$ and $I_{sc} = \frac{V_C}{4\ \Omega} = \frac{18}{7}\text{ A}$.
- consistency check: the same network has $V_{oc} = 18\text{ V}$, $I_{sc} = \frac{18}{7}\text{ A}$, and $R_{\text{eq}} = 7\ \Omega$; do these agree? ::@:: Yes: $I_{sc}R_{\text{eq}} = \frac{18}{7}\text{ A} \times 7\ \Omega = 18\text{ V} = V_{oc}$.
- reduction with unknown sources: a network holds an unknown $V_{s1}$, an unknown $I_{s2}$, a $2\ \Omega$ resistor, and a $4\ \Omega$ resistor, and a shorted load draws $4\text{ A}$; find $I_R$ for $R = 4\ \Omega$. ::@:: $I_{sc} = 4\text{ A}$ and $R_{\text{eq}} = 4\ \Omega$ give $I_R = 4\text{ A} \times \frac{4\ \Omega}{4\ \Omega + 4\ \Omega} = 2\text{ A}$.
- what a short measures: a network's load is replaced by a short and $4\text{ A}$ flows through it; which quantity of the equivalent does that give? ::@:: The short-circuit current $I_{sc}$, which is the current of the Norton source itself.

## series and parallel shortcuts

A resistor in series with an ideal current source can be neglected when other circuit variables are computed, since the source fixes the branch current whatever the resistance. A network of $8\text{ A}$ with $2\ \Omega$ in series is therefore equivalent to a bare $8\text{ A}$ source, with $I_{sc} = 8\text{ A}$ and $R_{\text{eq}} = \infty$.

An ideal current source has no open-circuit state, so its Norton resistance is infinite. An ideal voltage source is the mirror image, with zero equivalent resistance.

---

Flashcards for this section are as follows:

- overview ::@:: A resistor in series with an ideal current source may be neglected in computing other circuit variables, leaving $I_{sc} = 8\text{ A}$ and $R_{\text{eq}} = \infty$ for $8\text{ A}$ with $2\ \Omega$ in series. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the series branch drops out: why may a resistor in series with an ideal current source be ignored? ::@:: The source fixes the branch current regardless of the resistance, so the resistor cannot change any other branch current or voltage.
- infinite resistance: why is the Norton resistance of an ideal current source infinite? ::@:: The source delivers its current whatever voltage appears across it, and an infinite resistance is the parallel element that carries no current.
- dual case: what is the equivalent resistance of an ideal voltage source, and why? ::@:: Zero: the source holds its voltage under any current, which is a short circuit.
