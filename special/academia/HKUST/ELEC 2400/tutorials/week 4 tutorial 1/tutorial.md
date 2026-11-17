---
aliases:
  - ELEC 2400 week 4 tutorial 1 tutorial
  - ELEC2400 week 4 tutorial 1 tutorial
  - HKUST ELEC 2400 week 4 tutorial 1 tutorial
  - HKUST ELEC2400 week 4 tutorial 1 tutorial
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/tutorials/week_4_tutorial_1/tutorial
  - language/in/English
---

# tutorial

- HKUST ELEC 2400 week 4 tutorial 1
- parent: [week 4 tutorial 1](index.md)

## superposition with independent sources

A circuit of linear elements carrying several independent sources is solved one source at a time, and the partial outputs are added, $V_{\text{out}} = V_{1\text{out}} + V_{2\text{out}}$. Each contribution is computed with every other independent source set to zero: an unused current source is opened and an unused voltage source is shorted.

Two voltage sources, $5\text{ V}$ and $2\text{ V}$, contribute one at a time, each shorting the other out of its partial circuit. A current source of $5\text{ A}$ beside a voltage source of $2\text{ V}$ opens the current source for the voltage source's contribution and shorts the voltage source for the current source's.

A worked circuit feeds resistors of $10\ \Omega$, $12\ \Omega$, $2\ \Omega$, and $5\ \Omega$ from a $3\text{ V}$ source and a $5\text{ A}$ current source: the $3\text{ V}$ contribution is taken with the current source opened, the $5\text{ A}$ contribution with the voltage source shorted, and the two add to $V_{\text{out}} = V_{1\text{out}} + V_{2\text{out}}$.

---

Flashcards for this section are as follows:

- setting sources to zero: in a linear circuit with several independent sources, what does each unused source become while one contribution is computed? ::@:: A current source becomes an open and a voltage source becomes a short.
- adding the contributions: how are the single-source partial outputs combined into $V_{\text{out}}$? ::@:: By direct addition, $V_{\text{out}} = V_{1\text{out}} + V_{2\text{out}}$.
- worked superposition: a $3\text{ V}$ source and a $5\text{ A}$ current source drive resistors of $10\ \Omega$, $12\ \Omega$, $2\ \Omega$, and $5\ \Omega$; how is $V_{\text{out}}$ obtained? ::@:: Take the $3\text{ V}$ contribution with the current source opened and the $5\text{ A}$ contribution with the voltage source shorted, then add them, $V_{\text{out}} = V_{1\text{out}} + V_{2\text{out}}$.

## voltage law with a dependent voltage source

A dependent voltage source enters the loop equation like any other element; only its value is an expression rather than a number. A loop holding a $24\text{ V}$ source, a $6\ \Omega$ resistor, a $2\ \Omega$ resistor, and a dependent source of value $3V_3$, where $V_3$ is the voltage marked across the $2\ \Omega$ and $I_1$ runs through both resistors, reads $\{3V_3 - 0\} + (-I_1)(6) + (-I_1)(2) = 0$.

The controlling quantity is fixed by the same current that runs the loop, $V_3 = (-I_1)(2)$. Substituting it into the loop equation leaves one equation in the single unknown $I_1$.

---

Flashcards for this section are as follows:

- loop equation with a dependent source: a loop holds a $24\text{ V}$ source, a $6\ \Omega$ resistor, a $2\ \Omega$ resistor, and a dependent voltage source of value $3V_3$ with $V_3$ marked across the $2\ \Omega$, all carrying $I_1$; write the voltage law round the loop. ::@:: $\{3V_3 - 0\} + (-I_1)(6) + (-I_1)(2) = 0$.
- controlling relation: in that loop, what is $V_3$ in terms of $I_1$, and what does substituting it achieve? ::@:: $V_3 = (-I_1)(2)$, and substituting it leaves the loop equation with $I_1$ as its only unknown.

## source transformation

A voltage source in series with a resistor and a current source in parallel with the same resistor are the same one-port, in either direction. $5\text{ V}$ in series with $10\ \Omega$ becomes $0.5\text{ A}$ in parallel with $10\ \Omega$ because $\frac{5\text{ V}}{10\ \Omega} = 0.5\text{ A}$, and back again because $0.5\text{ A} \times 10\ \Omega = 5\text{ V}$. Only the terminal voltage and current survive; the arrangement inside the pair is free.

---

Flashcards for this section are as follows:

- series to parallel: what current source replaces a $5\text{ V}$ source in series with $10\ \Omega$? ::@:: $0.5\text{ A}$ in parallel with the same $10\ \Omega$, since $\frac{5\text{ V}}{10\ \Omega} = 0.5\text{ A}$.
- parallel to series: what voltage source replaces a $0.5\text{ A}$ source in parallel with $10\ \Omega$? ::@:: $5\text{ V}$ in series with the same $10\ \Omega$, since $0.5\text{ A} \times 10\ \Omega = 5\text{ V}$.

## reducing a network by source transformation

One transformation can leave a network reducible by the series and parallel rules alone. A $640\text{ V}$ source behind a $5\ \Omega$ series resistor feeds node $A$, which carries a $50\ \Omega$ to ground; the voltage $V_1$ is wanted across that $50\ \Omega$. A $12.8\text{ A}$ current source drawing down across a $5\ \Omega$ shunt converts to a $64\text{ V}$ source with its minus on top in series with that $5\ \Omega$, since $12.8\text{ A} \times 5\ \Omega = 64\text{ V}$, and that $5\ \Omega$ joins the original one for $10\ \Omega$ in series.

The current law at node $A$ then reads $\frac{640 - V_A}{5} + \frac{0 - V_A}{50} + \frac{(-64) - V_A}{10} = 0$, which gives $V_A = 380\text{ V}$. The voltage $V_1$ is the node voltage itself, so $V_1 = V_A = 380\text{ V}$.

---

Flashcards for this section are as follows:

- the transformation: what does a $12.8\text{ A}$ current source drawing down across a $5\ \Omega$ shunt convert to, and how does the branch continue? ::@:: A $64\text{ V}$ source with its minus on top in series with the $5\ \Omega$, since $12.8\text{ A} \times 5\ \Omega = 64\text{ V}$; that $5\ \Omega$ adds to the $5\ \Omega$ already in series for $10\ \Omega$.
- the node equation: node $A$ is fed by a $640\text{ V}$ source behind a $5\ \Omega$ series resistor, carries a $50\ \Omega$ to ground, and also receives the transformed branch of $10\ \Omega$ in series with a $64\text{ V}$ source whose minus faces the node; write the current law at $A$ and solve for $V_1$, the voltage across the $50\ \Omega$. ::@:: $\frac{640 - V_A}{5} + \frac{0 - V_A}{50} + \frac{(-64) - V_A}{10} = 0$ gives $V_A = 380\text{ V}$, so $V_1 = V_A = 380\text{ V}$.
