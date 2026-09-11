---
aliases:
    - ELEC 1100 written exam review
    - ELEC1100 written exam review
    - HKUST ELEC 1100 written exam review
    - HKUST ELEC1100 written exam review
tags:
    - flashcard/active/special/academia/HKUST/ELEC_1100/questions/written_exam_review
    - language/in/English
---

# written exam review

- HKUST ELEC 1100

This file repackages the written-exam review deck into public practice questions with changed values and equivalent reasoning targets.

- topics: voltage dividers; diode models; H-bridge drive; Boolean simplification; Zener regulators; transistor saturation; combinational logic; blocking delay.

## mixed written-exam practice

> A $12\text{ V}$ source feeds a divider of $2.0\text{ k}\Omega$ on top and $1.0\text{ k}\Omega$ on the bottom. What is the output voltage at the midpoint measured relative to ground?
>
> Solution: {@{The output voltage}@} is {@{$V_{out}=12\times\frac{1}{2+1}=4\text{ V}$}@}.

<!-- markdownlint MD028 -->

> A silicon diode is tested in a network and the computed diode current under the ON assumption is negative. What should you conclude?
>
> Solution: The ON assumption is {@{inconsistent with the circuit conditions}@}, so {@{the diode}@} should instead be {@{treated as OFF and the circuit solved again}@}.

<!-- markdownlint MD028 -->

> In an H-bridge, the top devices are PNP and the bottom devices are NPN. Which kind of pair must be active for one legal drive direction?
>
> Solution: {@{One top PNP and the diagonally opposite bottom NPN}@} must be active so current {@{flows through the motor rather than shorting the supply}@}.

<!-- markdownlint MD028 -->

> Simplify $AB + A'B + BC$.
>
> Solution: {@{The first two terms}@} {@{reduce to $B$}@}, so the whole expression becomes {@{$B + BC = B$}@}.

<!-- markdownlint MD028 -->

> A student wires a Zener diode forward like an ordinary diode in a regulator circuit. Why is that wrong?
>
> Solution: {@{A Zener regulator}@} relies on {@{reverse breakdown}@}, so {@{the Zener must be reverse-connected}@} to clamp {@{the voltage near its breakdown value}@}.

<!-- markdownlint MD028 -->

> An NPN switch uses $V_{CC}=5\text{ V}$, $R_C=330\Omega$, $R_B=47\text{ k}\Omega$, $\beta=90$, and $V_{in}=5\text{ V}$. Estimate whether it is saturated.
>
> Solution: {@{The base current}@} is {@{$I_B=\frac{5-0.7}{47\text{ k}\Omega}\approx0.0915\text{ mA}$}@}, so {@{the collector current}@} would be {@{$\beta I_B\approx8.24\text{ mA}$}@}. {@{The collector-limited maximum}@} is {@{$I_{C,\max}=\frac{5-0.2}{330\Omega}\approx14.55\text{ mA}$}@}, so because {@{$\beta I_B<I_{C,\max}$}@}, the transistor is {@{not forced into saturation by this base drive}@}.

<!-- markdownlint MD028 -->

> A logic system should sound an alarm when the door is open and the safety key is absent. If `D=1` means door open and `K=1` means key present, write the alarm expression.
>
> Solution: {@{The alarm}@} is {@{`DK'`}@}.

<!-- markdownlint MD028 -->

> A student uses a long `delay(5000)` in a temperature-control sketch and then complains that motion events are missed. What is the software reason?
>
> Solution: {@{The long blocking delay}@} prevents {@{the code from checking new sensor inputs during that interval}@}.

## extra challenging items

> A resistor network gives a negative current when solved with an assumed clockwise loop direction. What does the negative sign mean physically?
>
> Solution: {@{The negative sign}@} means {@{the true current direction is opposite the assumed clockwise direction}@}, and {@{the magnitude is still meaningful}@}.

<!-- markdownlint MD028 -->

> A robot controller uses only current line-sensor inputs and fails at a junction that looks identical to the start line. What extra design idea is missing?
>
> Solution: The design is {@{missing stored state, such as a counter or memory bit}@}, so it cannot {@{distinguish identical present inputs that occur in different stages of the run}@}.
