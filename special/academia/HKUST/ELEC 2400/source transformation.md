---
aliases:
  - ELEC 2400 source transformation
  - ELEC2400 source transformation
  - HKUST ELEC 2400 source transformation
  - HKUST ELEC2400 source transformation
  - source conversion
  - source transformation
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/source_transformation
  - language/in/English
---

# source transformation

Source transformation converts between the two forms of a linear network's equivalent, trading a voltage source in series with a resistor for a current source in parallel with the same resistor, and back. An ideal source on its own cannot be converted; the pair with its resistor can.

It is a statement about the terminals: the voltage and current seen from outside are preserved, and the quantities inside the replaced part are not.

---

Flashcards for this section are as follows:

- overview ::@:: Source transformation converts a voltage source $V$ in series with $R$ into a current source $\frac{V}{R}$ in parallel with $R$, and back, preserving the terminal voltage and current. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## the two forms

A linear network can be described by either its Thévenin or its Norton equivalent, and the validity of one proves the other. From the series form the parallel form follows by shorting the terminals, which drives $I_{sc} = \frac{V_{oc}}{R_{\text{eq}}}$ through the short. From the parallel form the series form follows by opening the terminals, where all of $I_{sc}$ passes through $R_{\text{eq}}$ and gives $V_{oc} = I_{sc}R_{\text{eq}}$.

Only the arrangement changes, series one way and parallel the other; the resistance stays the same.

---

Flashcards for this section are as follows:

- overview ::@:: The two equivalent forms are interchangeable: series becomes parallel with $I_{sc} = \frac{V_{oc}}{R_{\text{eq}}}$, and parallel becomes series with $V_{oc} = I_{sc}R_{\text{eq}}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- from series to parallel: how is the parallel form obtained from $V_{oc}$ in series with $R_{\text{eq}}$? ::@:: Short the terminals: the current that flows is $I_{sc} = \frac{V_{oc}}{R_{\text{eq}}}$, giving that current source in parallel with $R_{\text{eq}}$.
- from parallel to series: how is the series form obtained from $I_{sc}$ in parallel with $R_{\text{eq}}$? ::@:: Open the terminals: the whole $I_{sc}$ passes through $R_{\text{eq}}$, giving $V_{oc} = I_{sc}R_{\text{eq}}$ in series with $R_{\text{eq}}$.
- what is preserved: which quantity survives a source transformation? ::@:: The equivalent resistance, and with it the terminal voltage and current; only the arrangement of source and resistor changes.

## external quantities only

A transformation may be used only to compute voltages and currents external to the equivalent circuits. Quantities inside the network being replaced are not preserved, since the conversion rearranges exactly the elements whose currents and voltages are in question.

A $9\text{ A}$ source in parallel with a $3\ \Omega$ resistor, with a $6\ \Omega$ resistor across the same pair, converts to a $27\text{ V}$ source in series with the $3\ \Omega$ resistor; the $6\ \Omega$ resistor is the external element whose current $I_o$ is asked for. The current divider gives $I_{3\Omega} = 6\text{ A}$ and $I_o = 3\text{ A}$ in the original circuit. The transformed circuit still gives $I_o = 3\text{ A}$, but the $3\ \Omega$ resistor now carries $3\text{ A}$ rather than $6\text{ A}$: the transformation moved the very branch whose current was in question.

---

Flashcards for this section are as follows:

- overview ::@:: A source transformation is valid only for voltages and currents external to the equivalent circuits; quantities inside the transformed part are not preserved.
- scope of validity: which voltages and currents does a source transformation preserve? ::@:: Those external to the equivalent circuits; internal branch quantities are not preserved.
- worked conversion: a $9\text{ A}$ source in parallel with $3\ \Omega$ is transformed; what is the resulting series form? ::@:: A $27\text{ V}$ source in series with $3\ \Omega$, since $V_{oc} = 9\text{ A} \times 3\ \Omega = 27\text{ V}$.
- lost quantity: after that conversion the external $I_o = 3\text{ A}$ is unchanged while the $3\ \Omega$ resistor no longer carries $6\text{ A}$; why? ::@:: The transformation rearranges the elements whose internal current was asked for, so only external quantities survive it.

## reducing a circuit by transformation

Repeated transformation replaces simultaneous equations: each source-resistor pair is converted into whichever form makes the surrounding network reducible, and the series and parallel rules take over.

A circuit of a $2\text{ A}$ source across $4\ \Omega$ with a $4\text{ V}$ source and $4\ \Omega$ resistor alongside is solved in two moves. Turning the $4\text{ V}$ source and its resistor into a $1\text{ A}$ source across $4\ \Omega$ puts the two current sources in parallel and the two resistors in parallel, so $V_a = 3\text{ A} \times (4\ \Omega \| 4\ \Omega) = 6\text{ V}$. Converting the other branch instead gives the same answer by loop: $I = \frac{8\text{ V} - 4\text{ V}}{4\ \Omega + 4\ \Omega} = 0.5\text{ A}$ and $V_a = 8\text{ V} - 0.5\text{ A} \times 4\ \Omega = 6\text{ V}$.

A longer chain follows the same pattern: a $40\text{ V}$ source with $20\ \Omega$, a $5\text{ A}$ source with $8\ \Omega$, and resistors of $30\ \Omega$ and $12\ \Omega$ reduce step by step to a $24\text{ V}$ source with $12\ \Omega$ and $8\ \Omega$ in series, where $I = \frac{16\text{ V}}{32\ \Omega} = -0.5\text{ A}$ once the polarity of the reduced source is followed.

---

Flashcards for this section are as follows:

- overview ::@:: Repeated transformation converts source-resistor pairs into whichever form lets the surrounding network be reduced by series and parallel rules, avoiding simultaneous equations.
- why transform: what does transforming sources in turn replace? ::@:: The need to solve simultaneous equations: each conversion leaves the neighbouring network reducible by series and parallel rules.
- worked conversion and reduction: a $2\text{ A}$ source across $4\ \Omega$ and a $4\text{ V}$ source with $4\ \Omega$ are to be solved for $V_a$; how does converting the voltage source help? ::@:: It becomes a $1\text{ A}$ source across $4\ \Omega$, so the currents add and the resistors combine: $V_a = 3\text{ A} \times (4\ \Omega \| 4\ \Omega) = 6\text{ V}$.
- same answer by loop: how does the alternative conversion reproduce $V_a = 6\text{ V}$? ::@:: Converting the current-source branch gives $8\text{ V}$ in series with $4\ \Omega$ against $4\text{ V}$, so $I = \frac{8\text{ V} - 4\text{ V}}{4\ \Omega + 4\ \Omega} = 0.5\text{ A}$ and $V_a = 8\text{ V} - 0.5\text{ A} \times 4\ \Omega = 6\text{ V}$.
- chain of conversions: a $40\text{ V}$ source with $20\ \Omega$, a $5\text{ A}$ source with $8\ \Omega$, and resistors of $30\ \Omega$ and $12\ \Omega$ reduce to what? ::@:: Step by step to a $24\text{ V}$ source with $12\ \Omega$ and $8\ \Omega$ in series, where $I = \frac{16\text{ V}}{32\ \Omega} = -0.5\text{ A}$ once the reduced source's polarity is followed.
