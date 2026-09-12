---
aliases:
    - ELEC 1100 lab exam
    - ELEC1100 lab exam
    - HKUST ELEC 1100 lab exam questions
    - HKUST ELEC1100 lab exam questions
tags:
    - flashcard/active/special/academia/HKUST/ELEC_1100/questions/lab_exam_review
    - language/in/English
---

# lab exam review

- HKUST ELEC 1100

These questions are practical variants based on the lab-exam preparation material. They are written as public study prompts rather than as direct copies of the official handout.

- topics: DMM usage; DSO measurement; current measurement safety; inverter identification; sensor calibration; PWM diagnostics.

## practical build and measurement practice

> You are given a breadboarded resistor-divider circuit and a DMM. What is the safest order of actions before measuring the midpoint voltage?
>
> Solution: {@{Confirm the power and ground rails}@}, identify {@{the circuit reference node}@}, set {@{the DMM to voltage mode}@}, connect {@{the negative lead to the reference node}@}, and then touch {@{the positive lead to the midpoint}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A DSO trace spans 4.5 horizontal divisions and the time scale is $200\,\mu\text{s}/\text{div}$. Find the period and frequency.
>
> Solution: {@{The period}@} is {@{$T=4.5\times200\,\mu\text{s}=900\,\mu\text{s}$}@}, so {@{the frequency}@} is {@{$f=\frac{1}{T}\approx1.11\text{ kHz}$}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A square wave spans 3 vertical divisions at $2\text{ V}/\text{div}$. What is the peak-to-peak voltage?
>
> Solution: {@{$V_{pp}=3\times2=6\text{ V}$}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> During a current measurement, a student connects the DMM current terminals directly across a source. What is the mistake?
>
> Solution: The current input behaves like {@{a near-short and must be inserted in series, not in parallel}@}, so the student has {@{effectively shorted the source}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> An unknown IC produces LOW when its input is HIGH and HIGH when its input is LOW. What functional behavior does it match?
>
> Solution: It matches {@{an inverter or NOT gate}@}, which produces {@{the complement of its input}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A regulator circuit becomes too hot to touch during a lab. Name one electrical reason and one safe response.
>
> Solution: One reason is {@{excessive power dissipation}@} from {@{a large input-output voltage drop or heavy load current}@}. {@{A safe response}@} is to {@{turn off the supply, re-check the wiring and load current}@}, and only then {@{power the circuit again}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A line sensor is adjusted too close to the mat and always reports black. What should be changed first?
>
> Solution: Re-adjust {@{the sensor threshold or mounting distance}@} so {@{the reflected-light contrast between white and black surfaces}@} can be {@{distinguished again}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A practical bridge circuit gives a small KVL mismatch instead of exact zero. Should the result be discarded immediately?
>
> Solution: No. First compare {@{the mismatch with expected meter, lead, and rounding error}@}; {@{small residuals are normal in real measurements}@}, so {@{the KVL result is still valid}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## extra challenging items

> A PWM waveform has a duty cycle of $0.40$. The motor seems slower than expected even though the duty cycle is correct. Give one hardware-side explanation and one software-side explanation.
>
> Solution: {@{Hardware-side, the motor supply or wiring}@} may be {@{dropping voltage under load}@}. {@{Software-side, the direction logic or enable path}@} may be {@{incorrect so the full PWM command is not reaching the motor driver}@}. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> A student rebuilds the H-bridge and the motor no longer moves, but both the Arduino and the sensors still power up. Which supply-domain mistake should be checked first?
>
> Solution: Check whether the {@{logic rail and the motor-power rail have been mixed up}@} or whether the motor-side supply to the L293 driver is missing while the logic side is still powered. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
