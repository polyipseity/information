---
aliases:
  - ELEC 2400 current divider
  - ELEC2400 current divider
  - HKUST ELEC 2400 current divider
  - HKUST ELEC2400 current divider
  - current divider
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/current_divider
  - language/in/English
---

# current divider

A current divider is two resistors in parallel fed by a current source. The current splits in inverse proportion to the resistances, so the branch a current is wanted in has the _other_ resistance in the numerator, $I_{R1} = I_s \frac{R_2}{R_1 + R_2}$.

It is the dual of the voltage divider: parallel replaces series, the shared current becomes a shared voltage, and the source is a current.

---

Flashcards for this section are as follows:

- split of the source current: how do two parallel resistors fed by a current source divide it between them? ::@:: Two parallel resistors fed by $I_s$ split the current in the inverse ratio of the resistances, $I_{R1} = I_s \frac{R_2}{R_1 + R_2}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## dual of the voltage divider

Two parallel resistors share a voltage rather than a current. The current law gives $I_s = I_{R1} + I_{R2}$, and Ohm's law writes each branch through the shared $V_o$, $I_s = \frac{V_o}{R_1} + \frac{V_o}{R_2} = \frac{V_o}{R_1 \| R_2}$.

Every exchange is mirrored: series becomes parallel, the shared current becomes a shared voltage, the voltage source becomes a current source. Each statement about one divider then reads in the other.

---

Flashcards for this section are as follows:

- voltage-divider counterpart: what does the duality of the two dividers amount to? ::@:: The current divider is the dual of the voltage divider: parallel replaces series, the shared quantity becomes a voltage, the source becomes a current.
- shared quantity: which quantity $V_o$ do the branches of a current divider share, and how do their currents combine into $I_s$? ::@:: The voltage $V_o$ across them, with $I_s = I_{R1} + I_{R2}$ by the current law.
- dual correspondence: how does each element of the voltage divider appear in the current divider? ::@:: Series resistors become parallel resistors, the common current becomes a common voltage, and the voltage source becomes a current source.

## division ratio

Dividing the branch current by the source current cancels the shared voltage, $\frac{I_{R1}}{I_s} = \frac{V_o / R_1}{V_o / (R_1 \| R_2)} = \frac{R_2}{R_1 + R_2}$. The resistance of the branch asked about sits in the denominator, the other in the numerator.

In conductances the same statement is a proportion, $I_{R1} = I_s \frac{G_1}{G_1 + G_2}$: a branch takes the share of the current equal to its share of the conductance.

With two sources feeding the parallel pair, $I_2 = (8\text{ A} + 4\text{ A}) \times \frac{2}{2 + 4} = 4\text{ A}$ in the $4\ \Omega$ branch and $I_3 = 12\text{ A} - 4\text{ A} = 8\text{ A}$ in the $2\ \Omega$ branch.

---

Flashcards for this section are as follows:

- branch share: which resistance goes in the numerator of a branch's share of the source current, and which in the denominator? ::@:: Each branch takes $\frac{I_{R1}}{I_s} = \frac{R_2}{R_1 + R_2}$ of the source current, the opposite resistance supplying the share. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- derivation: two parallel resistors $R_1$ and $R_2$ carry $I_{R1}$ and $I_{R2}$ under a shared voltage $V_o$ from a source $I_s$; derive $\frac{I_{R1}}{I_s}$. ::@:: $I_s = \frac{V_o}{R_1 \| R_2}$ and $I_{R1} = \frac{V_o}{R_1}$, so $\frac{I_{R1}}{I_s} = \frac{R_2}{R_1 + R_2}$.
- conductance form: express $I_{R1}$ through the conductances $G_1$ and $G_2$. ::@:: $I_{R1} = I_s \frac{G_1}{G_1 + G_2}$: a branch takes the share of the current equal to its share of the conductance.
- worked split: a $6\text{ A}$ source feeds $R_1 = 2\ \Omega$ and $R_2 = 4\ \Omega$ in parallel; find $I_{R1}$ and $I_{R2}$. ::@:: $I_{R1} = 6\text{ A} \times \frac{4}{2+4} = 4\text{ A}$ and $I_{R2} = 6\text{ A} \times \frac{2}{2+4} = 2\text{ A}$.
- worked split with two sources: sources of $8\text{ A}$ and $4\text{ A}$ feed a parallel pair of a $4\ \Omega$ resistor and a $2\ \Omega$ resistor; what current does each branch carry? ::@:: The $4\ \Omega$ branch carries $12\text{ A} \times \frac{2}{2+4} = 4\text{ A}$ and the $2\ \Omega$ branch carries $12\text{ A} - 4\text{ A} = 8\text{ A}$.

## which branch takes more current

$I_{R1}$ is proportional to $R_2$ and $I_{R2}$ to $R_1$, so the smaller resistor draws the larger current.

The limits follow: a branch whose resistance falls to zero carries the whole source current, and one of very large resistance carries almost nothing.

---

Flashcards for this section are as follows:

- branch currents against resistances: how does each branch current depend on the branch resistances? ::@:: Each branch current is proportional to the opposite resistance, so the smaller resistor draws the larger current.
- proportionality: a current divider has $R_1 < R_2$; which branch carries more? ::@:: The $R_1$ branch: $I_{R1} \propto R_2$ and $I_{R2} \propto R_1$, so the smaller resistance takes the larger share.
- limiting cases: one branch of a parallel pair is shorted, or one is removed; what does the other branch carry of the source current $I_s$? ::@:: A shorted branch takes the whole source current and the other takes none; a removed branch leaves the whole $I_s$ to the remaining one.
