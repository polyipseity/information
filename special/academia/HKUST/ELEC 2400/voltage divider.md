---
aliases:
  - ELEC 2400 voltage divider
  - ELEC2400 voltage divider
  - HKUST ELEC 2400 voltage divider
  - HKUST ELEC2400 voltage divider
  - divider
  - voltage divider
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/voltage_divider
  - language/in/English
---

# voltage divider

A voltage divider is two resistors in series across a source. The source voltage divides in proportion to the resistances, so the resistor the output is taken across supplies the numerator, $V_{R2} = V_s \frac{R_2}{R_1 + R_2}$.

The ratio holds only while both resistors carry one common current. Anything hung across the output that draws current breaks that, so a bare divider is a reference rather than a supply.

---

Flashcards for this section are as follows:

- overview ::@:: Two series resistors divide the source voltage in the ratio of the resistances, $V_{R2} = V_s \frac{R_2}{R_1 + R_2}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## division ratio

Across the series pair the voltage law gives $V_s = V_{R1} + V_{R2}$, and Ohm's law gives $V_s = I(R_1 + R_2)$. Dividing the output voltage by the source voltage cancels the current, $\frac{V_{R2}}{V_s} = \frac{R_2}{R_1 + R_2}$.

Choosing $R_1$ and $R_2$ then yields any $V_{R2}$ between $0$ and $V_s$. The output is a fraction of the source, so a divider attenuates and never amplifies.

---

Flashcards for this section are as follows:

- overview ::@:: The source divides as $\frac{V_{R2}}{V_s} = \frac{R_2}{R_1 + R_2}$, with the output resistor in the numerator. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- derivation: two series resistors $R_1$ and $R_2$ carry a common current $I$ under a source $V_s$; derive $\frac{V_{R2}}{V_s}$. ::@:: $V_s = I(R_1 + R_2)$ and $V_{R2} = I R_2$, so $\frac{V_{R2}}{V_s} = \frac{R_2}{R_1 + R_2}$.
- range of output: which values of $V_{R2}$ can $R_1$ and $R_2$ produce? ::@:: Any value between $0$ and $V_s$, approached as $R_2$ is made small or large against $R_1$.
- amplification: can a divider deliver more than $V_s$? ::@:: No: the output is the fraction $\frac{R_2}{R_1+R_2} \le 1$ of the source, so it only attenuates.
- worked ratio: a $12\text{ V}$ source feeds $R_1 = 3\text{ k}\Omega$ and $R_2 = 1\text{ k}\Omega$ in series; find $V_{R2}$. ::@:: $V_{R2} = 12\text{ V} \times \frac{1}{3+1} = 3\text{ V}$.

## loading a divider

The output voltage cannot drive a load. If a network $N$ across $R_2$ draws $I''$, the current in $R_1$ becomes $I' = I - I'' \ne I$, so the two resistors no longer share one current and the ratio $\frac{V_{R2}}{V_s} = \frac{R_2}{R_1 + R_2}$ fails.

A drawing load must therefore be treated as a third branch of the network and the circuit re-analyzed.

---

Flashcards for this section are as follows:

- overview ::@:: A divider's output cannot drive a load: once a network draws $I''$, the source resistor carries $I' = I - I'' \ne I$ and the ratio fails. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- loading condition: when is the divider ratio exact? ::@:: Only while both resistors carry one common current, which fails as soon as the output draws any current.
- loaded divider: a network $N$ across the output draws $I''$; why does the ratio fail? ::@:: The upper resistor now carries $I' = I - I''$, unequal to the lower one, so the two no longer share $I$ and $V_{R2} \ne V_s\frac{R_2}{R_1+R_2}$.
- treating a load: a divider feeds a drawing load; how is it handled? ::@:: The load becomes another branch of the network and the circuit is re-analyzed without the unloaded ratio.
