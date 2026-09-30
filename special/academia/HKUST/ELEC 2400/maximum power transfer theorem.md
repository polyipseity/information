---
aliases:
  - ELEC 2400 maximum power transfer theorem
  - ELEC2400 maximum power transfer theorem
  - HKUST ELEC 2400 maximum power transfer theorem
  - HKUST ELEC2400 maximum power transfer theorem
  - maximum power transfer
  - maximum power transfer theorem
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/maximum_power_transfer_theorem
  - language/in/English
---

# maximum power transfer theorem

Maximum power transfer theorem fixes the load that extracts the most power from a source: a source of resistance $R_s$ delivers its largest power when the load resistance $R_L$ matches it. The theorem concerns the power reaching the load, not the fraction of generated power that survives, and the two objectives pull in opposite directions.

The result comes from writing the load power as a function of $R_L$ and differentiating. The same algebra reappears in power transmission, where the objective is a fixed delivered power at the least loss.

---

Flashcards for this section are as follows:

- overview ::@:: A source of resistance $R_s$ delivers its maximum power to a load when the load resistance equals the source resistance, $R_L = R_s$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## power delivered to the load

A voltage source $V_s$ with source resistance $R_s$ drives a load $R_L$. The divider gives the load voltage and current, $V_o = V_s \frac{R_L}{R_s + R_L}$ and $I_o = \frac{V_s}{R_s + R_L}$, whose product is the power dissipated in the load, $P_L = V_s^2 \frac{R_L}{(R_s + R_L)^2}$.

Both extremes of the load dissipate nothing: a short carries a large current at zero voltage, an open holds the full voltage at zero current. Some intermediate resistance therefore gives the most power.

---

Flashcards for this section are as follows:

- overview ::@:: A source $V_s$ with resistance $R_s$ driving a load $R_L$ gives $V_o = V_s\frac{R_L}{R_s+R_L}$, $I_o = \frac{V_s}{R_s+R_L}$, and $P_L = V_s^2\frac{R_L}{(R_s+R_L)^2}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- zero extremes: what power reaches a shorted load, and what power reaches an open load? ::@:: Zero in both cases: a short gives zero voltage and an open gives zero current.
- power expression: write the power delivered to the load $R_L$ of a source $V_s$ with source resistance $R_s$. ::@:: $P_L = V_s^2 \frac{R_L}{(R_s + R_L)^2}$.
- why a maximum: why must $P_L$ peak at some intermediate $R_L$? ::@:: It falls to zero at $R_L = 0$ and as $R_L \to \infty$, so the maximum lies between the extremes.

## matched load

Differentiating $P_L$ with respect to $R_L$ and setting the derivative to zero gives $\frac{(R_s + R_L)^2 - 2R_L(R_s + R_L)}{(R_s + R_L)^4} V_s^2 = 0$, which reduces to $R_L^2 + 2R_sR_L + R_s^2 - 2R_LR_s - 2R_L^2 = 0$ and hence $R_L = R_s$.

The load is then matched to the source, and the largest power the source can deliver is $P_{L(\text{max})} = \frac{V_s^2}{4R_s}$. The $4$ is the price of matching: at $R_L = R_s$ the load and the source resistance dissipate equally, so only half the generated power reaches the load.

---

Flashcards for this section are as follows:

- overview ::@:: Maximizing $P_L$ over $R_L$ gives $R_L = R_s$, at which the load receives $P_{L(\text{max})} = \frac{V_s^2}{4R_s}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- condition for maximum: how is $\frac{dP_L}{dR_L} = 0$ solved for the matching condition? ::@:: $(R_s + R_L)^2 - 2R_L(R_s + R_L) = 0$ simplifies to $R_L^2 - R_s^2 = 0$, so $R_L = R_s$.
- maximum power: a source $V_s$ has source resistance $R_s$; what is the largest power the load can receive? ::@:: $P_{L(\text{max})} = \frac{V_s^2}{4R_s}$, attained at $R_L = R_s$.
- cost of matching: how is the generated power divided when $R_L = R_s$? ::@:: The load and the source resistance dissipate equal amounts, so half the generated power reaches the load.
- matched load value: a $12\text{ V}$ source has $R_s = 3\ \Omega$; what load draws the maximum power, and what is that power? ::@:: $R_L = 3\ \Omega$ and $P_{L(\text{max})} = \frac{(12\text{ V})^2}{4 \times 3\ \Omega} = 12\text{ W}$.

## high-voltage transmission

Transmission has a different objective: deliver a given power $P_{\text{load}} = V_L I_L$ to a substation while losing as little as possible in the line. The line loss is $P_{\text{loss}} = I_L^2 \sum R_{\text{line}}$, which substituting the line current turns into $P_{\text{loss}} = \frac{P_{\text{load}}^2}{V_L^2} \sum R_{\text{line}}$, proportional to $\frac{1}{V_L^2}$.

The transmission voltage is therefore the lever: at a fixed delivered power the loss falls with the square of the voltage. China's highest transmission voltage now exceeds $1\text{ MV}$, with $P_{\text{load}}$ rated above $10\text{ GW}$.

Matching the line to its source would give the largest power, but only half of it would arrive, which is the opposite of what a transmission system wants. The line runs at high voltage and low current instead, holding the delivered power fixed while shrinking the loss.

---

Flashcards for this section are as follows:

- overview ::@:: At a fixed delivered power the line loss is $P_{\text{loss}} = \frac{P_{\text{load}}^2}{V_L^2}\sum R_{\text{line}}$, proportional to $\frac{1}{V_L^2}$, so a high transmission voltage lowers the loss. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- loss formula: write the loss of a line of total resistance $\sum R_{\text{line}}$ delivering $P_{\text{load}}$ at voltage $V_L$. ::@:: $P_{\text{loss}} = I_L^2 \sum R_{\text{line}} = \frac{P_{\text{load}}^2}{V_L^2}\sum R_{\text{line}}$.
- scaling: how does $P_{\text{loss}}$ change when $V_L$ is doubled at a fixed delivered power? ::@:: It falls to a quarter, since $P_{\text{loss}} \propto \frac{1}{V_L^2}$.
- why not matching: why is a transmission line not matched to its source? ::@:: Matching maximizes the delivered power but sends only half the generated power to the load, whereas transmission wants a given delivered power at the least loss.
- present practice: what $V_L$ and $P_{\text{load}}$ are now reached in China? ::@:: A voltage above $1\text{ MV}$ with $P_{\text{load}}$ rated over $10\text{ GW}$.
