---
aliases:
  - ELEC 1100 PWM
  - PWM
  - pulse-width modulation
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/pulse-width_modulation
  - language/in/English
---

# pulse-width modulation

Pulse-width modulation (PWM) is a practical way to turn a digital controller into an adjustable motor-speed command. Instead of trying to generate a continuously variable analog voltage directly, the controller switches between LOW and HIGH rapidly and lets the motor-driver-plus-load respond to the average effect.

## pulse waveform quantities

A rectangular pulse waveform is described by its HIGH duration $H$, LOW duration $L$, period $T=H+L$, frequency $f=1/T$, and duty cycle $D=H/T$. In ELEC 1100 the HIGH level is usually the logic or motor command voltage and the LOW level is usually $0\text{ V}$. Duty cycle is the fraction of each period for which the signal stays HIGH, so it is the first number to check when a waveform looks "mostly on" or "mostly off" on the DSO.

---

Flashcards for this section are as follows:

- PWM waveform quantities: what are $H$, $L$, $T$, $f$, and duty cycle? ::@:: $H$ is HIGH time, $L$ is LOW time, $T=H+L$ is the period, $f=1/T$ is the frequency, and duty cycle is $D=H/T$.
- PWM duty cycle meaning: what does a larger duty cycle mean physically? ::@:: The signal spends a larger fraction of each period at the HIGH level, so the load receives more average drive.
- DSO PWM reading: what are the first quantities to identify on a pulse waveform? ::@:: The HIGH time, LOW time, period, frequency, and duty cycle.

## average voltage and equivalent DC voltage

For a pulse source that switches between $V_H$ and $V_L$, the average voltage over one period is $V_{\text{ave}}=(HV_H+LV_L)/(H+L)$. If the load is resistive and we care about equal power rather than equal arithmetic mean, the equivalent DC voltage is $V_{\text{eq}}=\sqrt{(HV_H^2+LV_L^2)/(H+L)}$. When $V_L=0$, this becomes $V_{\text{eq}}=\sqrt{D}\,V_H$. ELEC 1100 uses this distinction to explain why two signals can share the same average voltage yet produce different brightness or heating if their waveforms are different.

---

Flashcards for this section are as follows:

- PWM average voltage: for levels $V_H$ and $V_L$, what is $V_{\text{ave}}$? ::@:: $V_{\text{ave}}=(HV_H+LV_L)/(H+L)$.
- PWM equivalent DC voltage: for a resistive load, what is $V_{\text{eq}}$? ::@:: $V_{\text{eq}}=\sqrt{(HV_H^2+LV_L^2)/(H+L)}$.
- PWM with $V_L=0$: what does $V_{\text{eq}}$ reduce to? ::@:: $V_{\text{eq}}=\sqrt{D}\,V_H$ when the LOW level is $0\text{ V}$.
- average vs equivalent voltage: why does ELEC 1100 distinguish $V_{\text{ave}}$ from $V_{\text{eq}}$? ::@:: Equal arithmetic mean does not always imply equal delivered power, so $V_{\text{eq}}$ is needed when comparing heating or lamp brightness in a resistive load.

<!-- check: ignore-next-line[header_style]: acronym -->
## PWM in motor control

In the robot car, direction and speed are separated. The H-bridge direction inputs decide whether current flows forward or backward through the motor, while the enable/PWM input decides how much average motor voltage is applied. The Arduino therefore sends one signal such as `DIR` for direction and a second PWM signal for speed. The late-course pin map is stable: `D9` and `D11` generate left/right PWM, and `D10` and `D12` provide left/right direction.

When a pulse voltage is applied to a DC motor, the motor speed is closely related to the average voltage across its terminals. In practice, for most motors on this robot platform that means the speed is _approximately_ linear in the PWM duty cycle when the supply rail is fixed, because the average motor voltage rises with duty cycle. Real motors can deviate from perfect linearity because of friction, driver voltage drop, unequal motors, battery droop, mechanical load, and dead-zone behavior at low duty cycle.

The Arduino `analogWrite(pin, value)` call is the standard PWM interface on this platform. The numeric value ranges from 0 to 255, where 0 means always LOW, 255 means always HIGH, and intermediate values produce intermediate duty cycles.

---

Flashcards for this section are as follows:

- PWM vs DIR in the robot car: what is the difference? ::@:: DIR selects the current direction through the motor, while PWM controls the average motor drive and therefore the speed.
- PWM motor-speed relation: for most motors on this robot platform, how does speed vary with duty cycle at fixed supply? ::@:: Motor speed is approximately linear in duty cycle because the average motor voltage rises with duty cycle.
- PWM motor-speed caveat: why is the speed-vs-duty-cycle relation not perfectly linear in practice? ::@:: Real motors can deviate because of friction, driver voltage drop, unequal motors, battery droop, mechanical load, and low-duty-cycle dead-zone effects.
- Arduino PWM pins in ELEC 1100: which pins generate left and right PWM? ::@:: `D9` is `L_PWM` and `D11` is `R_PWM`.
- Arduino DIR pins in ELEC 1100: which pins control left and right direction? ::@:: `D10` is `L_DIR` and `D12` is `R_DIR`.
- Arduino `analogWrite(pin, value)`: what does the `value` range mean? ::@:: The value ranges from 0 to 255, where 0 is always LOW, 255 is always HIGH, and intermediate values set the duty cycle.

<!-- check: ignore-next-line[header_style]: acronym -->
## PWM generation methods

There are two direct physical ways to generate pulses. A positive pulse can be generated mechanically by pressing a switch so the circuit alternates between ON and OFF states. It can also be generated electrically by an oscillator, which is a circuit that produces a continuous, repeated AC waveform. In the robot car, the practical digital version comes from the Arduino, which changes the pulse width in software to produce the required PWM duty cycle.

---

Flashcards for this section are as follows:

- PWM generation methods: what pulse-generation methods are highlighted? ::@:: Pulses can be generated mechanically by switching ON and OFF, electrically by an oscillator, or digitally by a controller such as the Arduino.
- oscillator in PWM generation: what is it? ::@:: An oscillator is a circuit that produces a continuous, repeated AC waveform.
- why the Arduino is a natural PWM source in ELEC 1100 ::@:: The Arduino is a digital controller, so it can change pulse width in software and generate PWM signals that are easy to control and use.

## practical PWM habits

ELEC 1100 treats PWM as an empirical design tool as well as a formula topic. If two motors do not behave identically, you may intentionally drive them with different PWM values to compensate. PWM is also preferable to a large variable resistor because it controls speed without wasting as much power as heat in an extra resistor. When debugging, confirm both the duty cycle and the direction logic; a motor that spins the wrong way at the correct speed is still wired or programmed incorrectly.

---

Flashcards for this section are as follows:

- why PWM is preferred to a variable resistor for motor speed control ::@:: PWM changes the average drive electronically instead of burning a large amount of power in a series resistor.
- unequal motors and PWM: why might left and right PWM values differ? ::@:: Real motors and wheels are not perfectly matched, so different PWM values can be used to equalize the robot's motion.
- PWM debugging habit: which two things must you verify together? ::@:: Verify both the duty cycle and the direction logic because speed and direction are controlled separately.
