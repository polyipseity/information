---
aliases:
  - ELEC 2400 summing amplifier
  - ELEC2400 summing amplifier
  - HKUST ELEC 2400 summing amplifier
  - HKUST ELEC2400 summing amplifier
  - summing amplifier
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/summing_amplifier
  - language/in/English
---

# summing amplifier

A summing amplifier adds several inputs into one output, and each input keeps the weight its own resistor gives it. The circuit is an inverting amplifier with extra input branches: the virtual ground that sets the gain also lets those branch currents add without disturbing one another. The price is the sign, which comes out inverted for every input, and one resistor per branch on top of the shared feedback resistor.

---

Flashcards for this section are as follows:

- how does a summing amplifier with input resistors $R_1$ and $R_2$ and feedback $R_f$ turn several inputs into one weighted output? ::@:: Each input reaches the inverting input through its own resistor, so their currents add at the virtual ground, and the single feedback resistor gives $V_o = -\frac{R_f}{R_1}V_{s1} - \frac{R_f}{R_2}V_{s2}$.

## the summing circuit

An inverting amplifier takes its input through $R_1$ into the inverting terminal, returns $R_f$ from the output to that terminal, and grounds the non-inverting terminal. A summing amplifier is that circuit with more than one input: $V_{s1}$ through $R_1$ and $V_{s2}$ through $R_2$ both reach the inverting terminal, and $R_f$ still returns from the output to it. The build-up is one amplifier plus one resistor per extra input, with $R_f$ the only resistor they share.

Read it as several inverting amplifiers sharing one feedback resistor. Each branch on its own would give $V_o = -\frac{R_f}{R_i}V_{si}$. The shared node does not move while the branches take turns: it stays at $0\text{ V}$ however many sources push into it, so no branch disturbs another. The separate answers then add up to the weighted sum.

The non-inverting terminal sits at ground, so the inverting terminal holds $0\text{ V}$ as a [virtual ground](virtual%20ground.md). No current enters that terminal, so the branch currents must cancel against the feedback current, $\frac{V_{s1}}{R_1} + \frac{V_{s2}}{R_2} = -\frac{V_o}{R_f}$. Solving for the output gives $V_o = -\frac{R_f}{R_1}V_{s1} - \frac{R_f}{R_2}V_{s2}$, a weighted sum of the inputs.

With $R_f = 6\text{ k}\Omega$, $V_{s1} = 1\text{ V}$ through $3\text{ k}\Omega$ and $V_{s2} = 2\text{ V}$ through $2\text{ k}\Omega$, $V_o = -\frac{6\text{ k}\Omega}{3\text{ k}\Omega}\times 1\text{ V} - \frac{6\text{ k}\Omega}{2\text{ k}\Omega}\times 2\text{ V} = -2 - 6 = -8\text{ V}$. Keeping $V_{s2}(t) = 2\sin\omega t\text{ V}$ gives $V_o(t) = -2 - 6\sin\omega t\text{ V}$, swinging between $-8\text{ V}$ and $4\text{ V}$.

An audio mixer is the same circuit with more inputs and a variable resistor in each branch to set that branch's gain; karaoke machines, equalizers and synthesizers use the arrangement. The same circuit becomes a [digital-to-analog converter](digital-to-analog%20converter.md) when bits drive those branches instead of signals.

![two-input summing amplifier: both sources reach the inverting input through their own resistor, the feedback resistor R f returns from the output to the same node, and the non-inverting input is grounded](attachments/summing_amplifier.svg)

---

Flashcards for this section are in the following format:

- the summing amplifier: how does the drawing combine two sources? ::@:: Each source reaches the inverting input through its own resistor, and $R_f$ returns from the output to the same node, so the output voltage adds the two scaled inputs. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- draw a two-input summing amplifier: where do the two input branches meet, and what returns from the output? ::@:: They meet at the inverting input, and the feedback resistor $R_f$ returns from the output to that node. <p> ![two-input summing amplifier: both sources reach the inverting input through their own resistor, the feedback resistor R f returns from the output to the same node, and the non-inverting input is grounded](attachments/summing_amplifier.svg) <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- how is a summing amplifier built from an inverting amplifier, what does each extra input add, and which resistor $R_f$ stays shared? ::@:: One input resistor per extra input, all meeting at the same virtual-ground node with the single feedback resistor $R_f$ shared, so each branch carries its own weight $-\frac{R_f}{R_i}$.
- why can a summing amplifier with feedback $R_f$ be read as several inverting amplifiers added together? ::@:: Each branch alone gives $-\frac{R_f}{R_i}V_{si}$ and the shared node stays at $0\text{ V}$ however many branches feed it, so superposition adds those answers and no branch disturbs another.
- in a summing amplifier, why does the weight $R_f$ over $R_i$ of one branch hold whatever the other branches do? ::@:: The node they share sits at $0\text{ V}$, so each branch drives its own $\frac{V_{si}}{R_i}$ into it and nothing else draws from that branch.
- what does a summing amplifier with the shared $R_f$ cost? ::@:: A resistor in every input branch beside $R_f$ itself, and an inverted sign on every input.
- summing amplifier: sources $V_{s1}$ and $V_{s2}$ enter the inverting terminal of an ideal operational amplifier through $R_1$ and $R_2$ with $R_f$ as feedback; what is $V_o$, and what is the output called? ::@:: $V_o = -\frac{R_f}{R_1}V_{s1} - \frac{R_f}{R_2}V_{s2}$: the output is a weighted sum of the inputs.
- summing amplifier with two DC sources: with $R_f = 6\text{ k}\Omega$, $V_{s1} = 1\text{ V}$ through $3\text{ k}\Omega$ and $V_{s2} = 2\text{ V}$ through $2\text{ k}\Omega$ feeding a summing amplifier built from an ideal operational amplifier, what is $V_o$? ::@:: $V_o = -\frac{6\text{ k}\Omega}{3\text{ k}\Omega}\times 1\text{ V} - \frac{6\text{ k}\Omega}{2\text{ k}\Omega}\times 2\text{ V} = -2 - 6 = -8\text{ V}$.
- summing amplifier with an alternating input: the same summing amplifier keeps $V_{s1} = 1\text{ V}$ while $V_{s2}(t) = 2\sin\omega t\text{ V}$; what is $V_o(t)$, and between which values does it swing? ::@:: $V_o(t) = -2 - 6\sin\omega t\text{ V}$, swinging between $-8\text{ V}$ and $4\text{ V}$.
- audio mixer: how does a summing amplifier become an audio mixer, and which applications use that arrangement? ::@:: More inputs are added, and a variable resistor in each input branch adjusts that branch's gain; karaoke machines, equalizers and synthesizers use it.
