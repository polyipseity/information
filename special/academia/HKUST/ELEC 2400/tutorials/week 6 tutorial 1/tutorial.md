---
aliases:
  - ELEC 2400 week 6 tutorial 1 tutorial
  - ELEC2400 week 6 tutorial 1 tutorial
  - HKUST ELEC 2400 week 6 tutorial 1 tutorial
  - HKUST ELEC2400 week 6 tutorial 1 tutorial
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/tutorials/week_6_tutorial_1/tutorial
  - language/in/English
---

# tutorial

- HKUST ELEC 2400 week 6 tutorial 1
- parent: [week 6 tutorial 1](index.md)

## circuit model of an operational amplifier

An operational amplifier is drawn as a triangle with two input terminals, $V_-$ and $V_+$, one output $V_o$, and two supply connections. Inside the triangle sit an input resistance $R_i$ between the two input terminals, a dependent voltage source of value $A_V V_{\text{in}}$ whose controlling difference is $V_{\text{in}}$ between the input terminals, and an output resistance $R_o$ between that source and the output. The ideal operational amplifier pushes all three to their limits: $R_i \to \infty$, $R_o \to 0$, and $A_V \to \infty$.

---

Flashcards for this section are as follows:

- the model: what does the circuit model of an operational amplifier hold between the input terminals $V_-$ and $V_+$, and between its internal source and the output $V_o$? ::@:: An input resistance $R_i$ between the input terminals, a dependent voltage source $A_V V_{\text{in}}$ controlled by their difference, and an output resistance $R_o$ toward the output.
- ideal limits: which three limits define an ideal operational amplifier? ::@:: Input resistance $R_i \to \infty$, output resistance $R_o \to 0$, and voltage gain $A_V \to \infty$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## input resistance of an operational amplifier

A large input resistance keeps the amplifier from loading the circuit ahead of it. A $10\text{ V}$ source behind $1\text{ k}\Omega$ delivers into the input resistance $R_i$, and the divider rule gives $V_{\text{in}} = \frac{R_i}{R_i + 1\text{ k}\Omega} \times 10$: with $R_i = 10\text{ k}\Omega$ the input sees $9.09\text{ V}$, while with $R_i = 10000\text{ k}\Omega$ it sees $9.999\text{ V}$. The larger $R_i$ is, the closer $V_{\text{in}}$ tracks the source.

---

Flashcards for this section are as follows:

- input loading: a $10\text{ V}$ source behind $1\text{ k}\Omega$ feeds an input resistance $R_i = 10\text{ k}\Omega$; what voltage appears at the input, and what happens when $R_i$ grows to $10000\text{ k}\Omega$? ::@:: $V_{\text{in}} = \frac{10\text{ k}\Omega}{10\text{ k}\Omega + 1\text{ k}\Omega} \times 10 = 9.09\text{ V}$; at $R_i = 10000\text{ k}\Omega$ it rises to $V_{\text{in}} = \frac{10000\text{ k}\Omega}{10000\text{ k}\Omega + 1\text{ k}\Omega} \times 10 = 9.999\text{ V}$.

## output resistance of an operational amplifier

A small output resistance keeps the output terminal at the internal source's voltage under load. A $10\text{ V}$ internal source behind an output resistance $R_o$ drives a $2\text{ k}\Omega$ load, and the divider rule gives $V_{\text{out}} = \frac{2\text{ k}\Omega}{R_o + 2\text{ k}\Omega} \times 10$: with $R_o = 1\text{ k}\Omega$ the load sees $6.6667\text{ V}$, while with $R_o = 0.0001$ it sees almost the whole source, $V_{\text{out}} \approx 10\text{ V}$.

---

Flashcards for this section are as follows:

- output loading: a $10\text{ V}$ internal source behind an output resistance $R_o$ drives a $2\text{ k}\Omega$ load; what does the load see at $R_o = 1\text{ k}\Omega$, and at $R_o = 0.0001$? ::@:: At $R_o = 1\text{ k}\Omega$, $V_{\text{out}} = \frac{2\text{ k}\Omega}{1\text{ k}\Omega + 2\text{ k}\Omega} \times 10 = 6.6667\text{ V}$; at $R_o = 0.0001$, $V_{\text{out}} = \frac{2\text{ k}\Omega}{0.0001 + 2\text{ k}\Omega} \times 10 \approx 10\text{ V}$.

## ideal operational amplifier

The three limits collapse the model to two working rules. $R_i \to \infty$ means no current enters either input terminal, $I_i \approx 0$. $R_o \to 0$ leaves $V_{\text{out}} = A_V V_{\text{in}}$ with $V_{\text{in}} = V_+ - V_-$, so $V_+ - V_- = \frac{V_{\text{out}}}{A_V}$; with $A_V \to \infty$ the difference is driven to nothing and $V_+ \approx V_-$. The two input terminals then sit at one voltage while sharing no current.

---

Flashcards for this section are as follows:

- input current: what does the limit $R_i \to \infty$ give for the current into the input terminals? ::@:: $I_i \approx 0$: no current enters either input terminal.
- virtual short: starting from $R_o \to 0$ and $A_V \to \infty$ with $V_{\text{in}} = V_+ - V_-$, why do the input terminals share a voltage? ::@:: $R_o \to 0$ gives $V_+ - V_- = \frac{V_{\text{out}}}{A_V}$, and $A_V \to \infty$ drives that difference to nothing, so $V_+ \approx V_-$ while $I_i \approx 0$ keeps the terminals current-free.

## inverting amplifier

An inverting amplifier feeds $V_{\text{in}}$ into the inverting terminal through $R_1$, returns $R_2$ from the output to that terminal, and grounds the non-inverting terminal. The gain $K_F = \frac{V_{\text{out}}}{V_{\text{in}}}$ follows from three relations: the model $V_{\text{out}} = A_V(V_+ - V_-)$, the grounded input $V_+ = 0$, and the current law at the inverting terminal $\frac{V_{\text{in}} - V_-}{R_1} + \frac{V_{\text{out}} - V_-}{R_2} = 0$.

Solving before any idealization gives $K_F = -\frac{1 - \left[\frac{R_1}{R_1 + R_2}\right]}{\frac{1}{A_V} + \left[\frac{R_1}{R_1 + R_2}\right]}$, and the limit $A_V \to \infty$ removes the $\frac{1}{A_V}$ term to leave $K_F = \frac{V_{\text{out}}}{V_{\text{in}}} = -\frac{R_2}{R_1}$.

The ideal rules pin that node at $0\text{ V}$, and most of the circuit's behaviour follows from it. The inverting terminal is a virtual ground, so the source driving $R_1$ is loaded by $R_1$ alone: $R_{\text{in}} = R_1$, and a source carrying appreciable resistance loses part of its own voltage before the amplifier sees any of it. All of $V_{\text{in}}$ then falls across $R_1$, the same current crosses $R_2$, and the output lands at $-\frac{R_2}{R_1}V_{\text{in}}$.

The sign and the range follow as well. The output moves opposite to the input, and $\frac{R_2}{R_1}$ can fall below 1 when $R_2 < R_1$, so the circuit attenuates as readily as it amplifies. Both terminals sit near $0\text{ V}$, so almost no common-mode voltage reaches the operational amplifier. Because the node holds a fixed $0\text{ V}$, several input resistors can meet there, each carrying its own $V_s/R$ without disturbing the others, which is what builds a summing amplifier.

---

Flashcards for this section are as follows:

- the three relations: an inverting amplifier feeds $V_{\text{in}}$ through $R_1$ into the inverting terminal, returns $R_2$ from the output to that terminal, and grounds the non-inverting terminal; which three relations determine the gain? ::@:: $V_{\text{out}} = A_V(V_+ - V_-)$, $V_+ = 0$, and the current law at the inverting terminal $\frac{V_{\text{in}} - V_-}{R_1} + \frac{V_{\text{out}} - V_-}{R_2} = 0$.
- finite gain: those three relations solve to which gain $K_F = \frac{V_{\text{out}}}{V_{\text{in}}}$ at finite $A_V$? ::@:: $K_F = -\frac{1 - \left[\frac{R_1}{R_1 + R_2}\right]}{\frac{1}{A_V} + \left[\frac{R_1}{R_1 + R_2}\right]}$.
- ideal gain: what gain $K_F = \frac{V_{\text{out}}}{V_{\text{in}}}$ remains for an inverting amplifier once $A_V \to \infty$? ::@:: $K_F = -\frac{R_2}{R_1}$.
- input resistance: why does an inverting amplifier present $R_{\text{in}} = R_1$ to its source, and what does that cost a source with appreciable resistance? ::@:: The inverting terminal is a virtual ground, so the source is loaded by $R_1$ alone; such a source loses part of its own voltage across its output resistance before the amplifier sees it.
- sign and range: what do the minus sign and the ratio $\frac{R_2}{R_1}$ allow that a non-inverting amplifier cannot do? ::@:: The output is inverted, and $R_2 < R_1$ gives a gain magnitude below 1, so the circuit attenuates as well as amplifies.
- several inputs: why can several input resistors meet at the inverting terminal without disturbing one another? ::@:: The node holds a fixed $0\text{ V}$, so each branch carries its own $V_s/R$ whatever the others are doing, which is what builds a summing amplifier. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## gain with parallel feedback resistors

Feedback resistors combine as any parallel pair does. $3.3\text{ k}\Omega$ in parallel with $2.0\text{ k}\Omega$ is $\frac{1}{\frac{1}{3.3\text{ k}\Omega} + \frac{1}{2.0\text{ k}\Omega}} = 1.245\text{ k}\Omega$, so an inverting amplifier with that pair as its feedback and $200\ \Omega$ as its input resistance gains $A_F = \frac{V_{\text{out}}}{V_{\text{in}}} = -\frac{1.245\text{ k}\Omega}{200\ \Omega} = -6.23$.

---

Flashcards for this section are as follows:

- parallel feedback pair: what is $3.3\text{ k}\Omega$ in parallel with $2.0\text{ k}\Omega$? ::@:: $\frac{1}{\frac{1}{3.3\text{ k}\Omega} + \frac{1}{2.0\text{ k}\Omega}} = 1.245\text{ k}\Omega$.
- gain with that pair: an inverting amplifier uses $3.3\text{ k}\Omega$ in parallel with $2.0\text{ k}\Omega$ as its feedback resistance and $200\ \Omega$ as its input resistance; what is $A_F = \frac{V_{\text{out}}}{V_{\text{in}}}$? ::@:: $A_F = -\frac{1.245\text{ k}\Omega}{200\ \Omega} = -6.23$.

## non-inverting amplifier

A non-inverting amplifier puts the signal on the non-inverting terminal and takes a divider from the output back to the inverting terminal. A $12\text{ V}$ source drives the non-inverting terminal directly, $12\text{ k}\Omega$ returns from the output to the inverting terminal, $2\text{ k}\Omega$ drops from that terminal to ground, and a $10\text{ k}\Omega$ load spans the output. The ideal rules settle it step by step: $V_+ = V_- = 12\text{ V}$, so the $2\text{ k}\Omega$ carries $I_{2k} = \frac{V_-}{2\text{ k}\Omega} = 6\text{ mA}$. No current enters the inverting terminal, so the feedback branch carries the same current, $I_{12k} = I_{2k} = 6\text{ mA}$.

The output follows from the two resistances in series under that current, $V_{\text{out}} = (12\text{ k}\Omega + 2\text{ k}\Omega) \times 6\text{ mA} = 84\text{ V}$, and the load takes $I_o = \frac{84\text{ V}}{10\text{ k}\Omega} = 8.4\text{ mA}$.

The same steps in letters give the gain. The divider holds the inverting terminal at $V_- = \frac{R_1}{R_1 + R_2}V_{\text{out}}$, and the virtual short makes that $V_{\text{in}}$, so $V_{\text{out}} = \left(1 + \frac{R_2}{R_1}\right)V_{\text{in}}$. The numbers agree: $1 + \frac{12\text{ k}\Omega}{2\text{ k}\Omega} = 7$, and $7 \times 12\text{ V} = 84\text{ V}$.

That gain never falls below 1, the output keeps the phase of the input, and $R_2 = 0$ gives exactly 1, the unity-gain buffer. The input resistance is where this circuit parts company with the inverting one: the source drives an input terminal that draws no current, so it keeps its full voltage instead of losing a share across $R_1$. What the circuit gives up is common-mode range, since the feedback holds both terminals at $V_{\text{in}}$ and the whole input signal arrives as common voltage, leaving the common-mode rejection ratio of the device to decide how faithfully the difference survives. The same $R_1 = 2\text{ k}\Omega$ and $R_2 = 12\text{ k}\Omega$ wired the inverting way would give $-6$ rather than $+7$.

---

Flashcards for this section are as follows:

- first steps: a $12\text{ V}$ source drives the non-inverting terminal of an operational amplifier, with $12\text{ k}\Omega$ from the output to the inverting terminal and $2\text{ k}\Omega$ from that terminal to ground; what are $V_-$ and the current $I_{2k}$? ::@:: $V_+ = V_- = 12\text{ V}$ by the ideal rules, so $I_{2k} = \frac{V_-}{2\text{ k}\Omega} = 6\text{ mA}$.
- feedback branch and output: in that circuit no current enters the inverting terminal; what does $I_{12k}$ carry and what is $V_{\text{out}}$? ::@:: $I_{12k} = I_{2k} = 6\text{ mA}$, so $V_{\text{out}} = (12\text{ k}\Omega + 2\text{ k}\Omega) \times 6\text{ mA} = 84\text{ V}$.
- load current: that amplifier ends at $V_{\text{out}} = 84\text{ V}$ and drives a $10\text{ k}\Omega$ load; what current does the load carry? ::@:: $I_o = \frac{84\text{ V}}{10\text{ k}\Omega} = 8.4\text{ mA}$.
- the gain: a non-inverting amplifier returns $R_2$ from the output to the inverting terminal and drops $R_1$ from there to ground; what gain $K_F = \frac{V_{\text{out}}}{V_{\text{in}}}$ results, and what does the same pair give in the inverting configuration? ::@:: $V_- = \frac{R_1}{R_1 + R_2}V_{\text{out}} = V_{\text{in}}$ gives $V_{\text{out}} = \left(1 + \frac{R_2}{R_1}\right)V_{\text{in}}$; with $R_1 = 2\text{ k}\Omega$ and $R_2 = 12\text{ k}\Omega$ that is $+7$, where the inverting arrangement would give $-6$.
- range and phase: what is the lowest gain a non-inverting amplifier can have, what happens to the phase, and which resistor value gives that lowest gain? ::@:: The gain never falls below 1, the output keeps the phase of the input, and $R_2 = 0$ gives exactly 1, the unity-gain buffer. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- input resistance: why does a resistive source keep its full voltage at a non-inverting input, while the inverting circuit would take a share of it? ::@:: The source drives an input terminal that draws no current, so nothing is lost across its output resistance; the inverting circuit loads it with $R_1$ instead. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- common-mode cost: what voltage sits on the input terminals of a non-inverting amplifier, and which device property then limits its accuracy? ::@:: The feedback holds both terminals at $V_{\text{in}}$, so the whole input signal arrives as common voltage and the common-mode rejection ratio decides how faithfully the difference survives. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
