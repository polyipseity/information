---
aliases:
  - ELEC 2400 series and parallel circuits
  - ELEC2400 series and parallel circuits
  - HKUST ELEC 2400 series and parallel circuits
  - HKUST ELEC2400 series and parallel circuits
  - parallel connection
  - series and parallel circuits
  - series connection
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/series_and_parallel_circuits
  - language/in/English
---

# series and parallel circuits

A resistive network is resistors together with voltage sources and current sources. Resistors in such a network can be joined in series, sharing one current, or in parallel, sharing one voltage, and each way collapses to a single equivalent resistor.

Both rules follow from Kirchhoff's laws, the current law fixing how currents combine and the voltage law how voltages do. Mixed networks are reduced by applying the two rules in turn until one resistor remains.

---

Flashcards for this section are as follows:

- overview ::@:: Resistors joined in series share a current and add to give $R_{\text{eq}} = \sum_{k=1}^{n} R_k$; resistors joined in parallel share a voltage and add reciprocally to give $\frac{1}{R_{\text{eq}}} = \sum_{k=1}^{n} \frac{1}{R_k}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- resistive network: which elements does a resistive network consist of? ::@:: Only resistors, together with voltage sources and current sources.
- shared quantity: which quantity do resistors in series share, and which do resistors in parallel share? ::@:: Resistors in series share one current; resistors in parallel share one voltage.

## series connection

Two resistors are in series when they form a daisy chain: $R_1$ and $R_2$ meet at a node no other element touches, so one current $I$ flows through both. The current law forces $I_{R1} = I_{R2} = I$ and the voltage law gives $V_s = V_{R1} + V_{R2}$.

Ohm's law then gives $V_s = I(R_1 + R_2)$, so the pair is equivalent to one resistor of $R_{\text{eq}} = R_1 + R_2$, and $n$ resistors give $R_{\text{eq}} = \sum_{k=1}^{n} R_k$.

The order of the chain is immaterial: only the sum and the shared current enter the analysis.

---

Flashcards for this section are as follows:

- overview ::@:: Resistors in series form a daisy chain, share the same current, and add up to $R_{\text{eq}} = \sum_{k=1}^{n} R_k$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- derivation: two series resistors $R_1$ and $R_2$ carry a current $I$ under a source $V_s$; which law fixes their currents and which gives $R_{\text{eq}}$? ::@:: The current law forces $I_{R1} = I_{R2} = I$, and the voltage law with Ohm's law gives $V_s = I(R_1 + R_2)$, so $R_{\text{eq}} = R_1 + R_2$.
- shared quantity: two resistors in series carry the same current; what does the current law give for $I_{R1}$ and $I_{R2}$? ::@:: $I_{R1} = I_{R2} = I$: the node between them has no other element, so nothing diverts current.
- summation form: $n$ resistors $R_1$ to $R_n$ are in series; what is $R_{\text{eq}}$? ::@:: $R_{\text{eq}} = R_1 + R_2 + \dots + R_n = \sum_{k=1}^{n} R_k$.
- order of connection: two series resistors are swapped in the daisy chain; what changes in the analysis? ::@:: Nothing: the order is immaterial and the equivalent resistance is still the sum.
- worked sum: $R_1 = 5\ \Omega$ and $R_2 = 3\ \Omega$ carry $I = 2\text{ A}$ in series under a source $V_s$; find $R_{\text{eq}}$, $V_{R1}$, and $V_{R2}$. ::@:: $R_{\text{eq}} = 5\ \Omega + 3\ \Omega = 8\ \Omega$, $V_{R1} = I R_1 = 10\text{ V}$, and $V_{R2} = I R_2 = 6\text{ V}$, so the two branch voltages add to $V_s$.

## parallel connection

Two resistors are in parallel when both span the same two nodes, so both carry the same voltage. The voltage law forces $V_s = V_{R1} = V_{R2}$ and the current law gives $I = I_{R1} + I_{R2}$.

Ohm's law gives $I = V_s\left(\frac{1}{R_1} + \frac{1}{R_2}\right)$, so $\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2}$, and $n$ resistors give $\frac{1}{R_{\text{eq}}} = \sum_{k=1}^{n} \frac{1}{R_k}$.

The double bar writes the two-resistor case, $R_{\text{eq}} = R_1 \| R_2 = \frac{R_1 R_2}{R_1 + R_2}$, product over sum. That shortcut does not extend: three resistors give $\frac{R_1 R_2 R_3}{R_1 R_2 + R_1 R_3 + R_2 R_3}$, obtained by applying the two-resistor form twice, while $\frac{R_1 R_2 R_3}{R_1 + R_2 + R_3}$ is wrong because its dimensions do not match. The order of connection is again immaterial.

---

Flashcards for this section are as follows:

- overview ::@:: Resistors in parallel span the same two nodes, share the same voltage, and combine as $\frac{1}{R_{\text{eq}}} = \sum_{k=1}^{n} \frac{1}{R_k}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- derivation: two parallel resistors $R_1$ and $R_2$ sit under a source $V_s$; which law fixes their voltages and which gives $R_{\text{eq}}$? ::@:: The voltage law forces $V_s = V_{R1} = V_{R2}$, and the current law with Ohm's law gives $I = V_s\left(\frac{1}{R_1} + \frac{1}{R_2}\right)$, so $\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2}$.
- shared quantity: two resistors in parallel carry the same voltage; what does the current law give for $I_{R1}$ and $I_{R2}$? ::@:: $I = I_{R1} + I_{R2}$: the total current splits between the two branches.
- two-resistor shortcut: two resistors $R_1$ and $R_2$ are in parallel; write $R_{\text{eq}}$ with the double-bar symbol. ::@:: $R_{\text{eq}} = R_1 \| R_2 = \frac{R_1 R_2}{R_1 + R_2}$, product over sum.
- three-resistor shortcut: does $R_1 \| R_2 \| R_3$ equal $\frac{R_1 R_2 R_3}{R_1 + R_2 + R_3}$? ::@:: No: that expression has the wrong dimensions, and the correct equivalent $\frac{R_1 R_2 R_3}{R_1 R_2 + R_1 R_3 + R_2 R_3}$ comes from applying the two-resistor form twice.
- worked pair: $R_1 = 50\ \Omega$ and $R_2 = 50\ \Omega$ are in parallel; find $R_{\text{eq}}$. ::@:: $R_{\text{eq}} = 50\ \Omega \| 50\ \Omega = \frac{50 \times 50}{50 + 50}\ \Omega = 25\ \Omega$.

### neither series nor parallel

Sharing one terminal is neither. A third element reaching that terminal lets current branch there, so the two elements are neither in series nor in parallel, and neither combination rule applies to them.

A pair's verdict comes from the nodes its two elements touch, so a worked case has to state those nodes. Three small cases give the three verdicts. $R_1$ and $R_2$ meet at a node that reaches nothing else, their far ends being on $P$ and $S$: in series. $R_3$ and $R_4$ both join $P$ to $Q$: in parallel. $R_5$ and $R_6$ share node $P$, and $R_7$ reaches $P$ as well, so the pair is neither.

---

Flashcards for this section are as follows:

- overview ::@:: Two elements that share only one terminal are neither in series nor in parallel, because a third element at that terminal lets current branch there.
- verdict read off the nodes: what decides whether a pair of elements is in series, in parallel, or neither? ::@:: The nodes the two elements touch: sharing both terminals with nothing else between makes them series, spanning the same two nodes makes them parallel, and sharing a single terminal that a third element also reaches makes them neither.
- a series case: $R_1$ and $R_2$ meet at one node that reaches nothing else, their far ends being on $P$ and $S$; which? ::@:: In series, since the same current runs through both.
- a parallel case: $R_3$ and $R_4$ both join node $P$ to node $Q$; which? ::@:: In parallel, since they span the same two nodes and share the terminal voltage.
- a neither case: $R_5$ and $R_6$ share node $P$, and $R_7$ reaches $P$ as well; which? ::@:: Neither, since current can branch at $P$ and neither combination rule applies.

## equivalent conductance

Conductance is the reciprocal of [resistance](Ohm%27s%20law.md#resistance%20and%20conductance), $G = \frac{1}{R}$, measured in siemens where $1\text{ S} = 1\ \Omega^{-1}$. Applying the current law to $n$ parallel branches driven by $V_s$ gives $I = V_s(G_1 + \dots + G_n)$, so parallel conductances add, $G_{\text{eq}} = \sum_k G_k$.

The reciprocal reading holds for series: conductances combine as their resistances do, $\frac{1}{G_{\text{eq}}} = \frac{1}{G_1} + \frac{1}{G_2}$. Conductances of $\frac{1}{30}\ \Omega^{-1}$ and $\frac{1}{20}\ \Omega^{-1}$ in series are therefore the ordinary $30\ \Omega$ and $20\ \Omega$ in series, $G_{\text{eq}} = \frac{1}{50}\ \Omega^{-1} = 0.02\text{ S}$, while two branches of $\frac{1}{50}\ \Omega^{-1}$ in parallel add to $0.04\text{ S}$, the reciprocal of $25\ \Omega$.

---

Flashcards for this section are as follows:

- overview ::@:: Conductance is $G = \frac{1}{R}$ in siemens, and parallel branches add their conductances, $G_{\text{eq}} = \sum_k G_k$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why conductance: why is conductance $G = \frac{1}{R}$ convenient for parallel branches? ::@:: The current law gives $I = V_s(G_1 + \dots + G_n)$ directly, so parallel conductances add instead of combining reciprocally.
- conductance unit: conductance $G = \frac{1}{R}$ is measured in siemens; how is the siemens defined? ::@:: $1\text{ S} = 1\ \Omega^{-1}$.
- parallel conductances: two branches of $\frac{1}{50}\ \Omega^{-1}$ each are in parallel; find $G_{\text{eq}}$ and $R_{\text{eq}}$. ::@:: $G_{\text{eq}} = 0.02 + 0.02\text{ S} = 0.04\text{ S}$, so $R_{\text{eq}} = \frac{1}{G_{\text{eq}}} = 25\ \Omega$.
- series conductances: conductances of $\frac{1}{30}\ \Omega^{-1}$ and $\frac{1}{20}\ \Omega^{-1}$ are in series; find $G_{\text{eq}}$. ::@:: $\frac{1}{G_{\text{eq}}} = \frac{1}{G_1} + \frac{1}{G_2} = 30\ \Omega + 20\ \Omega$, so $G_{\text{eq}} = \frac{1}{50}\ \Omega^{-1} = 0.02\text{ S}$.

## reduction of a ladder network

A mixed network is reduced by applying the two rules from the innermost pair outwards, always to a pair unambiguously in series or in parallel. The rules apply to groups as well as to single resistors, so each reduction replaces a whole sub-network by its equivalent.

In a ladder of $50\ \Omega$ in parallel with a branch of $30\ \Omega$ in series with $30\ \Omega \| 60\ \Omega$, the innermost pair goes first: $30\ \Omega \| 60\ \Omega = 20\ \Omega$. The branch becomes $30\ \Omega + 20\ \Omega = 50\ \Omega$, and the two remaining parallel branches give $R_{\text{eq}} = 50\ \Omega \| 50\ \Omega = 25\ \Omega$.

---

Flashcards for this section are as follows:

- overview ::@:: A mixed network is reduced by applying the series and parallel rules from the innermost pair outwards until a single resistor remains.
- reduction order: which pair of a mixed network is reduced first? ::@:: The innermost pair that is unambiguously in series or in parallel.
- ladder step one: in a ladder of $50\ \Omega$ in parallel with ($30\ \Omega$ in series with $30\ \Omega \| 60\ \Omega$), what is the first reduction? ::@:: $30\ \Omega \| 60\ \Omega = \frac{30 \times 60}{30 + 60}\ \Omega = 20\ \Omega$.
- ladder result: after that first reduction, what is $R_{\text{eq}}$? ::@:: $30\ \Omega + 20\ \Omega = 50\ \Omega$, then $50\ \Omega \| 50\ \Omega = 25\ \Omega$.
- grouping: may the series and parallel rules be applied to a sub-network rather than to one resistor? ::@:: Yes: each reduction replaces a whole sub-network by its single equivalent resistor, and the rules then apply to the result.
