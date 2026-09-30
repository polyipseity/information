---
aliases:
  - ELEC 2400 current source
  - ELEC2400 current source
  - HKUST ELEC 2400 current source
  - HKUST ELEC2400 current source
  - current sink
  - current source
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/current_source
  - language/in/English
---

# current source

Every two-terminal element is described by the relation between its current and its voltage. An independent ideal current source maintains a constant current $I_s$ through its terminals, independent of the voltage $V_s$ across them.

A real current source is built from complicated electronic circuits, and it gives up once the voltage it must produce rises past its compliance voltage. It is modelled as an ideal source with a large internal resistance in parallel.

---

Flashcards for this section are as follows:

- overview ::@:: A current source maintains a constant current $I_s$ through its terminals, independent of the voltage $V_s$ across them. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- overview / which quantity the source fixes: which of the current $I_s$ and the terminal voltage $V_s$ of a current source does the source itself fix? ::@:: The current $I_s$: a current source can tell you its current but not its voltage. The rest of the circuit decides the voltage across it.

## ideal current source

An ideal current source is an independent source: a constant current $I_s$ flows through its terminals whatever the voltage $V_s$ across them. Its I-V characteristic is the line $I = I_s$: horizontal when $I$ is drawn against $V$, vertical when $V$ is drawn against $I$.

The branch current through the source is fixed at $I_s$, while the voltage across it is whatever the rest of the circuit demands. A source rated $I_s = 3\text{ A}$ feeding a resistor of resistance $R$ therefore drives $I_o = 3\text{ A}$ through the resistor both at $R = 0\ \Omega$ and at $R = 1\text{ G}\Omega$. The load changes the terminal voltage, $V_o = I_oR$: it is $0$ across the $0\ \Omega$ load and $3\text{ A}\times1\text{ G}\Omega = 3\times10^{9}\text{ V}$ across the $1\text{ G}\Omega$ load.

With the same source feeding an infinite resistance, $I_o$ is undefined. An open circuit admits no current, while the source holds $3\text{ A}$ through the branch. The ideal model cannot satisfy both at once, so an ideal current source cannot drive an open circuit.

---

Flashcards for this section are as follows:

- overview ::@:: An ideal current source is an independent source whose terminal current is the constant $I_s$ at every terminal voltage $V_s$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- ideal current source / I-V characteristic: an ideal current source has terminal current $I$ and terminal voltage $V$; what is the shape of its I-V characteristic? ::@:: The line $I = I_s$: horizontal when $I$ is plotted against $V$, vertical when $V$ is plotted against $I$.
- ideal current source / construction ::@:: A real current source is built from complicated electronic circuits.
- ideal current source / current in the load: what current $I_o$ flows in a resistor of resistance $R$ fed by a source of $I_s = 3\text{ A}$, at $R = 0\ \Omega$ and at $R = 1\text{ G}\Omega$? ::@:: $I_o = 3\text{ A}$ in both loads.
- ideal current source / terminal voltage of a 3 A source with loads $R = 0\ \Omega$ and $R = 1\text{ G}\Omega$: what is $V_o = I_oR$? ::@:: $V_o = 3\text{ A}\times0\ \Omega = 0$ across the short, and $V_o = 3\text{ A}\times1\text{ G}\Omega = 3\times10^{9}\text{ V}$ across the $1\text{ G}\Omega$ load.
- ideal current source / open circuit: what is $I_o$ for an ideal current source $I_s$ with a load $R = \infty$ across its terminals? ::@:: Undefined: the open circuit carries no current while the source holds $I_s$ through the branch.

## series connection of current sources

A branch carries one current, so two current sources sharing a branch must agree on that current. A source of current $I_1$ forces its branch to carry $I_1$, and a second source of current $I_2$ in the same branch forces it to carry $I_2$. When $I_1\ne I_2$ the branch would have to carry two different currents at once, so such a pair is never connected in series.

The ideal model fixes each source's current and contains nothing that could resolve the contradiction.

---

Flashcards for this section are as follows:

- overview ::@:: Two ideal current sources of different currents must never be connected in series, because one branch cannot carry two different currents.
- series connection of current sources / the two demands: a branch contains ideal current sources of currents $I_1$ and $I_2$, with $I_1\ne I_2$; what does each demand of the branch current? ::@:: The source $I_1$ forces it to $I_1$ and the source $I_2$ forces it to $I_2$.
- series connection of current sources / failure of the ideal model: a series pair with $I_1 \ne I_2$; what does the ideal current source model contribute to the conflict? ::@:: Nothing: the model cannot resolve the conflict, so a more sophisticated model is needed.

## practical current source

A practical current source is modelled as an ideal current source $I_s$ with a large internal resistance $R_s$ in parallel. The source current divides: the load receives $I_o = I_s\frac{R_s}{R_s + R}$ for a load resistance $R$, and the shortfall grows as $R$ approaches the size of $R_s$. A practical voltage source is modelled the other way round, as an ideal voltage source with a small but non-zero internal resistance in series.

A source of $I_s = 3\text{ A}$ with $R_s = 10\text{ k}\Omega$ in parallel drives a load of $R = 10\ \Omega$, with the two resistances a factor of $1000$ apart. The load takes $I_o = 3\text{ A}\times\frac{10\text{ k}\Omega}{10\text{ k}\Omega + 10\ \Omega}\approx3\text{ A}$, and only $3\text{ A}\times\frac{10\ \Omega}{10.01\text{ k}\Omega}\approx3\text{ mA}$ bypasses the load through the internal resistance.

---

Flashcards for this section are as follows:

- overview ::@:: A practical current source is modelled as an ideal current source of current $I_s$ with a large internal resistance $R_s$ in parallel with it. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- practical current source / comparison with a practical voltage source: where does the internal resistance $R_s$ sit in each model, and how large is it? ::@:: Large and in parallel with the source for the practical current source; small but non-zero and in series with the source for the practical voltage source.
- practical current source / worked example with $I_s = 3\text{ A}$, $R_s = 10\text{ k}\Omega$, and a load of $R = 10\ \Omega$: what current $I_o$ reaches the load? ::@:: $I_o = 3\text{ A}\times\frac{10\text{ k}\Omega}{10\text{ k}\Omega + 10\ \Omega}\approx3\text{ A}$.
- practical current source / path through $R_s$ of the same source, with $I_s = 3\text{ A}$, $R_s = 10\text{ k}\Omega$, and a load of $R = 10\ \Omega$: what current bypasses the load? ::@:: $I_{R_s} = I_s\frac{R}{R_s + R} = 3\text{ A}\times\frac{10\ \Omega}{10.01\text{ k}\Omega}\approx3\text{ mA}$.
- practical current source / compliance voltage: what is the compliance voltage of a current source, and why is it there? ::@:: The terminal voltage above which the source will not deliver the requested current. The limit is there for protection.
