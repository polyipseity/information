---
aliases:
    - ELEC 1100 devices and logic
    - ELEC1100 devices and logic
    - HKUST ELEC 1100 devices and logic questions
    - HKUST ELEC1100 devices and logic questions
tags:
    - flashcard/active/special/academia/HKUST/ELEC_1100/questions/devices_and_logic
    - language/in/English
---

# devices and logic

- HKUST ELEC 1100

This set combines transistor, H-bridge, PWM, Boolean-algebra, and gate-design questions in the style of the official Part II exercises and written-exam review material.

- topics: transistor switching; H-bridge safety; PWM duty cycle; Boolean algebra simplification; XOR gates.

## transistor, motor control, and Boolean logic

> An NPN switch has $V_{CC}=6\text{ V}$, $R_C=560\Omega$, $R_B=18\text{ k}\Omega$, $\beta=80$, and a driving input of $3.3\text{ V}$. Assume $V_{BE}=0.7\text{ V}$ and saturated $V_{CE}=0.2\text{ V}$. Is the transistor in saturation?
>
> Solution: {@{The base current}@} is {@{$I_B=\frac{3.3-0.7}{18\text{ k}\Omega}\approx0.144\text{ mA}$}@}, so if {@{active the collector current would be}@} {@{$\beta I_B\approx11.5\text{ mA}$}@}. {@{The collector-limited maximum}@} is {@{$I_{C,\max}=\frac{6-0.2}{560\Omega}\approx10.36\text{ mA}$}@}. Since {@{$\beta I_B>I_{C,\max}$}@}, {@{the transistor saturates}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A transistor inverter is pulled up to $5\text{ V}$. What logic output is expected when the input is LOW, and why?
>
> Solution: {@{The transistor is off}@}, so there is {@{almost no collector current}@} and {@{the pull-up resistor}@} raises {@{the output near $5\text{ V}$}@}. Therefore {@{LOW in gives HIGH out}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> In an H-bridge, why is it unsafe to turn on both transistors connected to the same supply rail at the same time?
>
> Solution: That creates {@{a direct short path from the supply to ground}@} instead of forcing {@{current through the motor}@}, so it can {@{damage the driver circuit}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A PWM signal switches between $0\text{ V}$ and $12\text{ V}$ with duty cycle $0.25$. Find the average voltage.
>
> Solution: {@{The average voltage}@} is {@{$V_{\text{ave}}=0.25\times12=3\text{ V}$}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> For the same PWM signal as Question 4, what is the equivalent DC voltage for the same resistive-load power?
>
> Solution: {@{The equivalent DC voltage}@} is {@{$V_{\text{eq}}=\sqrt{0.25}\times12=6\text{ V}$}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Build the truth table and simplified output for a warning lamp that turns on only when exactly one of two sensor inputs `A` and `B` is HIGH.
>
> Solution: {@{The truth table}@} is {@{$00\to0$, $01\to1$, $10\to1$, $11\to0$}@}. The output matches {@{an XOR gate, so the simplified expression}@} is {@{$A\oplus B=A'B+AB'$}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Simplify the Boolean expression $XY + XY' + Z$.
>
> Solution: Factor $X$: {@{$X(Y+Y')+Z=X+Z$}@} because {@{$Y+Y'=1$}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A two-sensor robot must drive `FORWARD=1` only when both sensors see the line, and `STOP=1` only when neither sensor sees the line. Write the expressions.
>
> Solution: If {@{the sensor variables are `L` and `R`}@}, then {@{`FORWARD = LR`}@} and {@{`STOP = L'R'`}@} if {@{1 means on-line}@}. (If the course uses the opposite sensor convention, invert the definitions before implementing.) <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## extra exam-style questions

> A majority-vote alarm should output HIGH when at least two of `A`, `B`, and `C` are HIGH. Give a sum-of-products expression.
>
> Solution: {@{Any two of three inputs HIGH}@} gives {@{$AB+AC+BC$}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A motor driver has `DIR` and `PWM` separated. Which signal should be pulsed to change speed without changing direction?
>
> Solution: Pulse {@{the PWM or enable path, not the DIR path}@}, so {@{the average motor drive changes}@} while {@{the chosen direction remains fixed}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A student claims that equal $V_{\text{ave}}$ always implies equal lamp brightness. Why is that incomplete?
>
> Solution: {@{Lamp brightness and resistor heating}@} depend on {@{power, so waveform shape matters}@}. {@{Equal average voltage}@} does not guarantee {@{equal resistive power}@} unless {@{the waveforms are equivalent in the RMS/equivalent-DC sense}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
