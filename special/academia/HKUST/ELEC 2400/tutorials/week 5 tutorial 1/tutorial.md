---
aliases:
  - ELEC 2400 week 5 tutorial 1 tutorial
  - ELEC2400 week 5 tutorial 1 tutorial
  - HKUST ELEC 2400 week 5 tutorial 1 tutorial
  - HKUST ELEC2400 week 5 tutorial 1 tutorial
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/tutorials/week_5_tutorial_1/tutorial
  - language/in/English
---

# tutorial

- HKUST ELEC 2400 week 5 tutorial 1
- parent: [week 5 tutorial 1](index.md)

## statement of Thévenin's theorem

However tangled a linear two-terminal network is, its terminal pair behaves for every load exactly like one voltage source in series with one resistor. The two numbers are the network's open-circuit voltage and its resistance seen from the terminals, and any load attached to the pair draws the same current as it would from that two-element circuit.

---

Flashcards for this section are as follows:

- Thévenin's theorem: what two-element circuit stands in for a linear two-terminal network at its terminals? ::@:: One ideal voltage source in series with one resistor, carrying the network's open-circuit voltage and its resistance seen from the terminals; every load draws the same current either way.

## open-circuit voltage

With the terminals open nothing flows, so a resistor beside the source drops nothing. A $10\text{ V}$ source behind a $3\ \Omega$ whose terminals are left open reads $V_{AB} = 10\text{ V}$ directly from the voltage law.

When the same idea meets a loaded divider, the open terminals read the divider's output. A $36\text{ V}$ source behind $3\ \Omega$ in series with the $6\ \Omega$ that spans $A$ to $B$ gives $V_{oc} = \frac{6}{3 + 6} \times 36\text{ V} = 24\text{ V}$.

---

Flashcards for this section are as follows:

- open terminals, no drop: a $10\text{ V}$ source is in series with a $3\ \Omega$ resistor, and the pair's terminals $A$ and $B$ are left open; what is $V_{AB}$? ::@:: $V_{AB} = 10\text{ V}$: with the terminals open no current runs, so the $3\ \Omega$ drops nothing.
- open-circuit voltage of a divider: a $36\text{ V}$ source is in series with a $3\ \Omega$ resistor, and a $6\ \Omega$ resistor spans terminals $A$ and $B$; what is the open-circuit voltage $V_{oc}$ across them? ::@:: $V_{oc} = \frac{6}{3 + 6} \times 36\text{ V} = 24\text{ V}$, the divider's output.

## equivalent resistance

The resistance at the terminals is read off the dead network: every independent source is set to zero, current sources opened and voltage sources shorted, and what remains is reduced. The $36\text{ V}$, $3\ \Omega$, $6\ \Omega$ network leaves $3\ \Omega$ in parallel with $6\ \Omega$ once its source is shorted, $R_{\text{eq}} = \frac{1}{\frac{1}{3} + \frac{1}{6}} = 2\ \Omega$. The two measurements, the open-circuit voltage and the short-circuit current, give the same number, $R_{\text{eq}} = \frac{V_{oc}}{I_{sc}}$.

A longer dead network reduces the same way from the innermost pair. Zeroing a $10\text{ A}$ source and a $500\text{ V}$ source leaves $8\ \Omega$ in parallel with $12\ \Omega$, which is $4.8\ \Omega$; in series with $5.2\ \Omega$ that branch becomes $10\ \Omega$, and in parallel with the $30\ \Omega$ it gives $R_{\text{eq}} = 7.5\ \Omega$.

---

Flashcards for this section are as follows:

- setting sources to zero: what does each independent source become when the terminal resistance is computed? ::@:: A current source becomes an open and a voltage source becomes a short, and the remaining dead network is reduced to one resistance.
- worked resistance: the $36\text{ V}$, $3\ \Omega$, $6\ \Omega$ network has its source shorted for the resistance computation; what does $A$ to $B$ see? ::@:: $3\ \Omega$ in parallel with $6\ \Omega$, so $R_{\text{eq}} = \frac{1}{\frac{1}{3} + \frac{1}{6}} = 2\ \Omega$.
- measurement route: how do the open-circuit voltage $V_{oc}$ and the short-circuit current $I_{sc}$ give the terminal resistance $R_{\text{eq}}$? ::@:: $R_{\text{eq}} = \frac{V_{oc}}{I_{sc}}$, the same number the dead-network reduction gives.
- dead-network ladder: zeroing a $10\text{ A}$ source and a $500\text{ V}$ source leaves $8\ \Omega$ in parallel with $12\ \Omega$, that combination in series with $5.2\ \Omega$, and the branch in parallel with $30\ \Omega$; what is $R_{\text{eq}}$? ::@:: $8\ \Omega \| 12\ \Omega = 4.8\ \Omega$, plus $5.2\ \Omega$ gives $10\ \Omega$, and $30\ \Omega \| 10\ \Omega = 7.5\ \Omega$.

## statement of Norton's theorem

The same network is equally one current source in parallel with one resistor: the short-circuit current $I_{sc}$, the current that flows when the terminals are joined, beside the same $R_{\text{eq}}$ the Thévenin form uses. The two forms convert into each other by source transformation, tied by $V_{oc} = I_{sc}R_{\text{eq}}$.

---

Flashcards for this section are as follows:

- Norton equivalent: what two-element circuit stands in for a linear two-terminal network in the current-source form? ::@:: One ideal current source $I_{sc}$, the network's short-circuit current, in parallel with the same $R_{\text{eq}}$ the Thévenin form uses. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- tying the two forms: how are the open-circuit voltage $V_{oc}$, the short-circuit current $I_{sc}$, and the terminal resistance $R_{\text{eq}}$ related? ::@:: $V_{oc} = I_{sc}R_{\text{eq}}$, and the two equivalent circuits convert into each other by source transformation.

## load current by the Thévenin equivalent

The $36\text{ V}$, $3\ \Omega$, $6\ \Omega$ network reduces to $V_{oc} = 24\text{ V}$ in series with $R_{\text{eq}} = 2\ \Omega$. Attaching a $2\ \Omega$ load closes one loop, and the voltage law reads $24 - 2I_1 - 2I_1 = 0$, so the load current is $I_1 = 6\text{ A}$.

---

Flashcards for this section are as follows:

- load current, Thévenin form: a network of $V_{oc} = 24\text{ V}$ and $R_{\text{eq}} = 2\ \Omega$ drives a $2\ \Omega$ load; what current does the load carry? ::@:: The loop reads $24 - 2I_1 - 2I_1 = 0$, so $I_1 = 6\text{ A}$.

## load current by the Norton equivalent

The same load on the Norton form uses $I_{sc} = 12\text{ A}$ beside $R_{\text{eq}} = 2\ \Omega$. The load and the equivalent resistance are two equal branches under the source, so the current divider gives $I_1 = \frac{2}{2 + 2} \times 12\text{ A} = 6\text{ A}$, the current the Thévenin form reported.

---

Flashcards for this section are as follows:

- load current, Norton form: a network of $I_{sc} = 12\text{ A}$ in parallel with $R_{\text{eq}} = 2\ \Omega$ drives a $2\ \Omega$ load; what current does the load carry? ::@:: The current divider gives $I_1 = \frac{2}{2 + 2} \times 12\text{ A} = 6\text{ A}$, the same current the Thévenin form gives.
