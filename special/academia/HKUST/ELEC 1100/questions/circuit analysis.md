---
aliases:
    - ELEC 1100 circuit analysis
    - ELEC1100 circuit analysis
    - HKUST ELEC 1100 circuit analysis questions
    - HKUST ELEC1100 circuit analysis questions
tags:
    - flashcard/active/special/academia/HKUST/ELEC_1100/questions/circuit_analysis
    - language/in/English
---

# circuit analysis

- HKUST ELEC 1100

These questions are course-authored practice variants based on the official additional exercises, with changed numbers and slightly reworded scenarios. Each solution is short but complete enough to show the method.

- topics: resistor networks; KCL; KVL; regulation; diodes; Zener regulators; bridge circuits.

## resistor networks, KCL, KVL, and regulation

> A $15\text{ V}$ source is connected across two series resistors, $R_1=1.8\text{ k}\Omega$ and $R_2=4.2\text{ k}\Omega$. Find the voltage across $R_2$.
>
> Solution: First find {@{the series current}@} is {@{$I=\frac{15}{1.8+4.2}\text{ mA}=2.5\text{ mA}$}@}. Then by {@{Ohm's law, the voltage across $R_2$}@} is {@{$V_{R_2}=IR_2=2.5\text{ mA}\times4.2\text{ k}\Omega=10.5\text{ V}$}@}.

<!-- markdownlint MD028 -->

> A node splits into two branches: one branch has $2.0\text{ k}\Omega$, the other has $3.0\text{ k}\Omega$. If $10\text{ mA}$ enters the node from the source side, how much current goes through each branch?
>
> Solution: In {@{a parallel circuit, voltage is the same on both branches}@}. First find {@{$R_{\text{eq}}=\frac{2\times3}{2+3}\text{ k}\Omega=1.2\text{ k}\Omega$}@}. The node voltage is {@{$V=10\text{ mA}\times1.2\text{ k}\Omega=12\text{ V}$}@}. So {@{$I_1=\frac{12}{2}=6\text{ mA}$}@} and {@{$I_2=\frac{12}{3}=4\text{ mA}$}@}.

<!-- markdownlint MD028 -->

> One loop contains a $9\text{ V}$ source, a $4\text{ V}$ source opposing it, and a $250\Omega$ resistor. Find the loop current and resistor power.
>
> Solution: By {@{KVL, the net resistor voltage}@} is {@{$9-4=5\text{ V}$}@}. {@{The current}@} is {@{$I=\frac{5}{250}=0.02\text{ A}$}@}. {@{Resistor power}@} is {@{$P=I^2R=(0.02)^2\times250=0.10\text{ W}$}@}.

<!-- markdownlint MD028 -->

> A silicon diode is in series with a $680\Omega$ resistor and a $5\text{ V}$ source. Using the $0.7\text{ V}$ drop model, find the diode current when forward biased.
>
> Solution: {@{The resistor}@} sees {@{$5-0.7=4.3\text{ V}$}@}. Hence {@{the diode current}@} is {@{$I_D=\frac{4.3}{680}\approx6.32\text{ mA}$}@}.

<!-- markdownlint MD028 -->

> A Zener regulator uses a $7.2\text{ V}$ reverse-breakdown diode; a $390\Omega$ resistor in series with the input, the diode and the load; and a $1.2\text{ k}\Omega$ load. Explain what happens as the input rises from $5\text{ V}$ to $12\text{ V}$.
>
> Solution: Below {@{the combined threshold}@}, {@{the Zener is effectively off}@} and the node {@{behaves like an ordinary voltage divider}@}. Once the current is {@{large enough to drive the Zener into reverse breakdown}@}, the node is {@{clamped near $7.2\text{ V}$}@} and extra {@{source variation mainly changes the current through the series path}@}.

<!-- markdownlint MD028 -->

> A practical source is modeled as an ideal $12\text{ V}$ source in series with $0.8\Omega$. What terminal voltage appears when the load current is $1.5\text{ A}$?
>
> Solution: Use {@{$V_{\text{out}}=V_S-iR_S=12-1.5\times0.8=10.8\text{ V}$}@}.

<!-- markdownlint MD028 -->

> Challenge: A bridge network has two branches from a $12\text{ V}$ source to ground: left branch $1.0\text{ k}\Omega$ over $2.0\text{ k}\Omega$, right branch $1.5\text{ k}\Omega$ over $3.0\text{ k}\Omega$, and a $6.0\text{ k}\Omega$ resistor connecting the two midpoints. Explain whether the midpoint voltages are equal before solving the bridge current.
>
> Solution: {@{Both branches}@} have the same {@{divider ratio, because the lower resistor is twice the upper resistor in each branch}@}. {@{Each midpoint}@} therefore sits at {@{$8\text{ V}$}@}, so the bridge resistor has {@{zero voltage across it and carries no current}@}. {@{The network}@} can then be {@{solved as two independent dividers}@}.

## extra exam-style questions

> A lamp is driven by a $10\text{ V}$ pulse waveform with duty cycle $0.36$ and LOW level $0\text{ V}$. What is the equivalent DC voltage for the same resistive power?
>
> Solution: {@{The equivalent DC voltage}@} is {@{$V_{\text{eq}}=\sqrt{0.36}\times10=6\text{ V}$}@}.

<!-- markdownlint MD028 -->

> A student measures a loop and finds the signed sum of the rises and drops to be $-0.15\text{ V}$ instead of exactly zero. Is KVL automatically wrong?
>
> Solution: No. In {@{lab measurements a small nonzero residual}@} can come from {@{meter tolerance, lead resistance, and rounding}@}. KVL still applies; {@{it sums the voltages around any closed loop}@}; the result is {@{approximately consistent}@} if {@{the error is small compared with the measured voltages}@}.
