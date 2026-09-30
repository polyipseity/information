---
aliases:
  - ELEC 2400 electric current
  - ELEC2400 electric current
  - HKUST ELEC 2400 electric current
  - HKUST ELEC2400 electric current
  - current
  - electric current
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/electric_current
  - language/in/English
---

# electric current

Electric current is the rate of change of charge, measured in amperes: one coulomb per second.

Charge carries a sign, and the arrow drawn on a diagram fixes a reference direction, so the same physical flow can be reported as a positive or a negative number. Conduction in a wire is mostly by electrons, while conventional current follows positive charge.

---

Flashcards for this section are as follows:

- what a reported current value is relative to ::@:: A reported current is meaningful only together with its reference direction and the sign of its charge carriers.

## current as a rate of charge flow

Current is the rate of change of charge, and its unit is the ampere (A), $1\text{ A} = 1\text{ C/s}$, named after André-Marie Ampère (1775-1836).

Charge arrives in discrete carriers. An electron carries $q = -1.6\times10^{-19}\text{ C}$. The charge $\Delta Q$ that has crossed is found by multiplying the number of carriers that pass a cross-section by the charge each one carries. The current is $\Delta Q$ divided by the elapsed time.

---

Flashcards for this section are as follows:

- current as a rate of charge flow / definition and unit of current ::@:: Electric current is the rate of change (flow) of charge; its unit is the ampere (A), $1\text{ A} = 1\text{ C/s}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- current as a rate of charge flow / charge carried by $N = 5\times10^{18}$ electrons of charge $q = -1.6\times10^{-19}\text{ C}$ ::@:: Carriers crossing a wire cross-section at a uniform rate carry the charge $\Delta Q = Nq$; here $\Delta Q = 5\times10^{18}\times(-1.6\times10^{-19}\text{ C}) = -0.8\text{ C}$.
- current as a rate of charge flow / why $1\text{ A} = 1\text{ C/s}$ ::@:: Charge and time are the measured quantities, and current is the quotient $\Delta Q/\Delta t$, whose unit is the coulomb per second.

## direction of current

The direction of a current is the direction in which positive charges flow, and the circuit diagram must show it. Conduction in a wire is mostly by electrons, yet picturing positive charges moving the opposite way speeds up reasoning about signs.

A drawn arrow is a reference direction, not a measurement: flow along the arrow gives a positive current value, flow against it a negative value, and reversing the arrow flips the sign of the reported current.

The load settles which way the current runs out of a source, once the load is known. With a $10\text{ V}$ source driving a $1\ \Omega$ resistor, the current leaves the source at the terminal marked $+$ and runs along the top of the loop into the resistor. Put a battery charger where the resistor was and the current at the top runs the other way, back into the terminal marked $+$, so the source is being charged. Leave the load unspecified and the direction cannot be determined from the source alone.

---

Flashcards for this section are as follows:

- direction of current / definition and diagram requirement ::@:: The direction in which positive charges flow; the circuit diagram must show it.
- direction of current / positive-charge mental picture ::@:: Although currents in wires are mostly conducted by electrons, thinking of positive charges flowing the other way speeds up reasoning about signs.
- direction of current / sign rule for an arrow labelled $I_1 = -1\text{ A}$ ::@:: Flow along the drawn arrow gives a positive current value and flow against it a negative one, so the same charge flow on the reversed arrow is $I_2 = 1\text{ A}$.
- direction of current / worked example: $N = 5\times10^{18}$ electrons of charge $q = -1.6\times10^{-19}\text{ C}$ crossing in $\Delta t = 2\text{ s}$ against the assumed arrow ::@:: $\Delta Q = Nq = 5\times10^{18}\times(-1.6\times10^{-19}\text{ C}) = -0.8\text{ C}$, so $I = \Delta Q/\Delta t = -0.8\text{ C}/2\text{ s} = -0.4\text{ A}$: a current of $0.4\text{ A}$ opposite the arrow.
- direction of current / what sets the direction at a source: a $10\text{ V}$ source drives a $1\ \Omega$ resistor back to its $-$ terminal, with that $-$ terminal grounded; which way does the current run along the top of the loop? ::@:: Away from the source, out of its $+$ terminal and into the resistor.
- direction of current / a load that is itself a source: the $1\ \Omega$ resistor is replaced by a battery charger; which way does the current at the top of the $10\text{ V}$ source run? ::@:: Into its $+$ terminal, the opposite way, so the source is being charged.
- direction of current / an unspecified load: a $10\text{ V}$ source drives a load that has not been stated; which way does the current leave it? ::@:: It cannot be determined: the direction follows from the load, and the load is unknown.

## average, instantaneous, and constant current

A current that does not change has a single value, so the charge that passes in a given interval follows from $I = \Delta Q/\Delta t$. Such a current equals its own time average.

The instantaneous current is the derivative of the charge with respect to time, $i(t) = \frac{dq(t)}{dt}$. The average current over $0$ to $T$ is the time average of $i(t)$, $I = \frac{1}{T}\int_0^T i(t)\,dt$. For a charge $q(t) = 5t$ measured in coulombs with $t$ in seconds, differentiating gives $i(t) = \frac{d}{dt}(5t) = 5\text{ A}$, a constant current.

---

Flashcards for this section are as follows:

- average, instantaneous, and constant current / three descriptions for charge $q(t)$ and interval $0$ to $T$ ::@:: A constant current obeys $I = \Delta Q/\Delta t$, a time-varying current has the instantaneous value $i(t) = \frac{dq(t)}{dt}$, and its average over $0$ to $T$ is $I = \frac{1}{T}\int_0^T i(t)\,dt$.
- average, instantaneous, and constant current / constant current for charge $\Delta Q$ crossing uniformly in time $\Delta t$ ::@:: The current is the constant $I = \Delta Q/\Delta t$.
- average, instantaneous, and constant current / instantaneous current for charge $q(t)$ at the instant $t$ ::@:: $i(t) = \frac{dq(t)}{dt}$.
- average, instantaneous, and constant current / average current of $i(t)$ over $0$ to $T$ ::@:: $I = \frac{1}{T}\int_0^T i(t)\,dt$.
- average, instantaneous, and constant current / instantaneous current for the charge $q(t) = 5t$ in coulombs with $t$ in seconds ::@:: $i(t) = \frac{dq(t)}{dt} = \frac{d}{dt}(5t) = 5\text{ A}$.

## charge capacity units

Hybrid units are sometimes used instead of SI units. The electron-volt, the ampere-hour, and the kilowatt-hour are examples. The ampere-hour is a unit of charge: $1\text{ Ah}$ is a current of $1\text{ A}$ for $1$ hour, which is $1\text{ C/s}\times3600\text{ s} = 3600\text{ C}$, and $1\text{ Ah} = 1000\text{ mAh}$.

A lithium-ion rechargeable battery with a capacity of $2000\text{ mAh}$ ($= 2\text{ Ah}$) can supply $2000\text{ mA}$ ($= 2\text{ A}$) for $1$ hour. A capacity of $1450\text{ mAh}$ is $5220\text{ C}$: $1.45\text{ A}$ for $1$ hour of battery operation, $145\text{ mA}$ for $10$ hours, or $2.9\text{ A}$ for $0.5$ hour.

---

Flashcards for this section are as follows:

- charge capacity units / charge in coulombs of $1\text{ Ah}$ ::@:: A current of $1\text{ A}$ flowing for $1$ hour, that is $1\text{ C/s}\times3600\text{ s} = 3600\text{ C}$; $1\text{ Ah} = 1000\text{ mAh}$.
- charge capacity units / why the electron-volt, the ampere-hour, and the kilowatt-hour are used ::@:: They are easier to use and to understand than the corresponding SI units.
- charge capacity units / discharge of a $2000\text{ mAh}$ battery label ::@:: A lithium-ion rechargeable battery of $2\text{ Ah}$ capacity supplies $2000\text{ mA}$ ($= 2\text{ A}$) for $1$ hour; manufacturers prefer $\text{mAh}$ to $\text{Ah}$ on such labels.
- charge capacity units / convert $1450\text{ mAh}$ to coulombs ::@:: With $1\text{ Ah} = 1000\text{ mAh} = 3600\text{ C}$, a capacity of $1450\text{ mAh}$ is $1.45\text{ Ah}\times3600\text{ C/Ah} = 5220\text{ C}$.
- charge capacity units / discharge rates of $1450\text{ mAh}$ ($= 5220\text{ C}$) ::@:: Such a capacity delivers $1.45\text{ A}$ for $1$ hour of battery operation, or $145\text{ mA}$ for $10$ hours, or $2.9\text{ A}$ for $0.5$ hour.

## direct current and alternating current

A steady charge flow whose current is constant is a direct current (DC). A charge flow that fluctuates, sometimes stronger and sometimes weaker and possibly reversing direction, is an alternating current (AC).

Historically an alternating current always meant a sinusoidal current. Nowadays DC specifies a quantity independent of time, at a constant value, and AC specifies a time-dependent quantity. Upper-case symbols denote DC quantities such as $V_1$, $I_2$, and $V_{dd}$; lower-case symbols denote time-dependent variables such as $v_3(t)$ and $i_4(t)$.

Time-dependent quantities need not be simple sinusoids.

---

Flashcards for this section are as follows:

- direct current and alternating current / original distinction ::@:: A direct current (DC) is a steady charge flow whose current is a constant, while an alternating current (AC) is a fluctuating charge flow, sometimes stronger and sometimes weaker and possibly reversing direction.
- direct current and alternating current / meaning of the two terms today ::@:: DC now specifies a quantity that is independent of time, at a constant value, and AC now specifies a time-dependent quantity.
- direct current and alternating current / adjectival use ::@:: DC and AC are adjectives that can refer to voltages as well as to currents.
- direct current and alternating current / symbol case for $V_1$, $I_2$, $V_{dd}$ against $v_3(t)$, $i_4(t)$ ::@:: Upper-case symbols denote DC quantities such as $V_1$; lower-case symbols denote time-dependent variables such as $v_3(t)$.
- direct current and alternating current / beyond sinusoids ::@:: A time-dependent quantity need not be a simple sinusoid.

### sinusoidal alternating current

In its historical sense an alternating current was always the sinusoid $i(t) = I_o\sin(\omega t + \theta)$, fixed by its amplitude $I_o$, its angular frequency $\omega = 2\pi f$ with $f$ the frequency, and its phase $\theta$.

---

Flashcards for this section are as follows:

- sinusoidal alternating current / historical meaning ::@:: In its historical sense an alternating current is always the sinusoid $i(t) = I_o\sin(\omega t + \theta)$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sinusoidal alternating current / parameters of $i(t) = I_o\sin(\omega t + \theta)$ ::@:: Its amplitude $I_o$, its angular frequency $\omega = 2\pi f$ where $f$ is the frequency, and its phase $\theta$.

### analysis of time dependence

In transient analysis the time dependence decays to a constant value eventually. In harmonic analysis a periodic steady-state time series is decomposed as a superposition of many sinusoids at harmonic (multiple) frequencies, each with its own amplitude and phase. That is Fourier series analysis.

---

Flashcards for this section are as follows:

- analysis of time dependence / transient analysis ::@:: Transient analysis handles time dependence that will decay to a constant value eventually.
- analysis of time dependence / harmonic analysis ::@:: Harmonic analysis decomposes any periodic steady-state time series as a superposition of sinusoids at harmonic (multiple) frequencies, each with its own amplitude and phase; it is Fourier series analysis.
