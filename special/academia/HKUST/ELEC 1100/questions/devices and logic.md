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
> ---
>
> - solution: {@{The transistor saturates}@}
> - explanation: The base current is {@{$I_B\approx0.144\text{ mA}$, worked from $(3.3-0.7)/18\text{ k}\Omega$}@}, so an active collector current would be {@{$\beta I_B\approx11.5\text{ mA}$, far above the limit}@}. {@{The collector can pass only $10.36\text{ mA}$}@}, so the device {@{saturates}@}.

<!-- markdownlint MD028 -->

> A transistor inverter is pulled up to $5\text{ V}$. What logic output is expected when the input is LOW, and why?
>
> ---
>
> - solution: {@{HIGH, because the pull-up holds the output high}@}
> - explanation: {@{An input LOW turns the transistor off}@}, so {@{almost no collector current flows}@} and {@{the pull-up resistor raises the output near $5\text{ V}$}@}.

<!-- markdownlint MD028 -->

> In an H-bridge, why is it unsafe to turn on both transistors connected to the same supply rail at the same time?
>
> ---
>
> - solution: {@{It shorts the supply rail to ground}@}
> - explanation: That creates {@{a direct short path from the supply to ground}@} instead of {@{forcing current through the motor}@}, so it can {@{damage the driver circuit}@}.

<!-- markdownlint MD028 -->

> A PWM signal switches between $0\text{ V}$ and $12\text{ V}$ with duty cycle $0.25$. Find the average voltage.
>
> ---
>
> - solution: {@{The average voltage is $3\text{ V}$}@}

<!-- markdownlint MD028 -->

> For the same PWM signal as Question 4, what is the equivalent DC voltage for the same resistive-load power?
>
> ---
>
> - solution: {@{The equivalent DC voltage for the same resistive power is $6\text{ V}$}@}

<!-- markdownlint MD028 -->

> Build the truth table and simplified output for a warning lamp that turns on only when exactly one of two sensor inputs `A` and `B` is HIGH.
>
> ---
>
> - solution: {@{XOR, so the simplified expression is $A\oplus B=A'B+AB'$}@}
> - explanation: {@{The truth table is $00\to0$, $01\to1$, $10\to1$, $11\to0$, which matches an exclusive-OR gate}@}

<!-- markdownlint MD028 -->

> Simplify the Boolean expression $XY + XY' + Z$.
>
> ---
>
> - solution: {@{The expression simplifies to $X+Z$}@}

<!-- markdownlint MD028 -->

> A two-sensor robot must drive `FORWARD=1` only when both sensors see the line, and `STOP=1` only when neither sensor sees the line. Write the expressions.
>
> ---
>
> - solution: {@{FORWARD $=LR$ and STOP $=L'R'$}@}
> - explanation: If {@{the sensor variables are `L` and `R`}@} and {@{1 means on-line}@}, the two rules give those expressions. {@{A course using the opposite sensor convention inverts them}@} before implementing..

## extra exam-style questions

> A majority-vote alarm should output HIGH when at least two of `A`, `B`, and `C` are HIGH. Give a sum-of-products expression.
>
> ---
>
> - solution: {@{The sum of products is $AB+AC+BC$}@}

<!-- markdownlint MD028 -->

> A motor driver has `DIR` and `PWM` separated. Which signal should be pulsed to change speed without changing direction?
>
> ---
>
> - solution: {@{Pulse the PWM or enable path, not the DIR path}@}
> - explanation: {@{Pulsing the enable path changes the average motor drive while the chosen direction stays fixed}@}

<!-- markdownlint MD028 -->

> A student claims that equal $V_{\text{ave}}$ always implies equal lamp brightness. Why is that incomplete?
>
> ---
>
> - solution: {@{Waveform shape matters, so equal average voltage does not give equal resistive power}@}
> - explanation: {@{Lamp brightness and resistor heating}@} depend on {@{power, so waveform shape matters}@}. {@{Equal average voltage}@} does not guarantee {@{equal resistive power}@} unless {@{the waveforms are equivalent in the RMS/equivalent-DC sense}@}.
