---
aliases:
  - ELEC 2400 electric power
  - ELEC2400 electric power
  - HKUST ELEC 2400 electric power
  - HKUST ELEC2400 electric power
  - electric power
  - power
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/electric_power
  - language/in/English
---

# electric power

Every two-terminal element exchanges energy with the rest of its circuit, and the rate of that exchange is the electric power. The quantity decides how hot a resistor runs and how long a battery lasts.

Voltage alone does not fix the power, because the same potential difference can drive charge at very different rates. The product of voltage and current does. With the reference direction drawn for the element, the sign of that product tells whether the element takes energy in or hands it back, which separates a load from a source.

---

Flashcards for this section are as follows:

- overview ::@:: Electric power is the rate of doing work, equivalently the rate of change of energy, measured in watts or in joules per second.
- why voltage alone does not fix the power ::@:: Charge can cross the same potential difference at very different rates.
- sign of $VI$ under the drawn reference direction ::@:: A positive product marks an element consuming energy; a negative product marks one that supplies it.
- instantaneous against average power ::@:: Power can be read at one instant or averaged over a period, and the average of a periodic product of voltage and current is well defined even when neither factor stays constant.

## instantaneous and average power

Electric power is the rate of doing work, equivalently the rate of change of energy, and its unit is the watt (W), one joule per second (J/s). During a time $\Delta t$, a charge $\Delta q$ flows from the high-voltage terminal of a two-terminal element to its low-voltage terminal and gives up electric potential energy $\Delta E = v(t)\,\Delta q$. Dividing that energy by the time gives the instantaneous power $p(t) = \Delta E/\Delta t = v(t)\,\Delta q/\Delta t = v(t)\,i(t)$.

At $t = 3\text{ s}$ the readings $v(3) = 12\text{ V}$ and $i(3) = 4\text{ A}$ give the instantaneous power $p(3) = v(3)\,i(3) = 12\text{ V}\times4\text{ A} = 48\text{ W}$.

A time-varying element needs an average instead of a single value. If $p(t) = v(t)\,i(t)$ repeats with period $T$, the average power is $P_\text{ave} = \frac{1}{T}\int_0^T p(t)\,dt = \frac{1}{T}\int_0^T v(t)\,i(t)\,dt$.

---

Flashcards for this section are as follows:

- overview ::@:: For a two-terminal element with the voltage $v(t)$ across it and the current $i(t)$ through it, the instantaneous power is $p(t) = v(t)\,i(t)$, and the average power over a period $T$ is $P_\text{ave} = \frac{1}{T}\int_0^T v(t)\,i(t)\,dt$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- energy given up by a charge crossing an element: the charge $\Delta q$ crosses from the high-voltage to the low-voltage terminal in the time $\Delta t$ under the voltage $v(t)$ ::@:: It gives up the electric potential energy $\Delta E = v(t)\,\Delta q$, and dividing that energy by the time gives $p(t) = \Delta E/\Delta t = v(t)\,\Delta q/\Delta t = v(t)\,i(t)$.
- instantaneous power from two readings: $v(3) = 12\text{ V}$ and $i(3) = 4\text{ A}$ at the time $t = 3\text{ s}$ ::@:: $p(3) = v(3)\,i(3) = 12\text{ V}\times4\text{ A} = 48\text{ W}$.
- average power of a periodic product: the product $p(t) = v(t)\,i(t)$ repeats with the period $T$ ::@:: $P_\text{ave} = \frac{1}{T}\int_0^T p(t)\,dt = \frac{1}{T}\int_0^T v(t)\,i(t)\,dt$.

## direct current power

Under direct current the voltage and the current both stay constant, so the power stays at one value, $P = VI$. The watt then follows from a volt and an ampere multiplied together: $1\text{ W} = (1\text{ V})\times(1\text{ A}) = 1\text{ VA}$.

A resistor converts that power into heat. Substituting Ohm's law into the product gives two further forms: $V = IR$ gives $P = I^2R$, and $I = V/R$ gives $P = V^2/R$. Which form applies matters when two resistances are compared, because a fixed current and a fixed voltage pull in opposite directions: $P = I^2R$ grows with the resistance while $P = V^2/R$ shrinks with it.

A resistor is drawn with the current arrow entering the terminal marked $+$ and leaving the terminal marked $-$. The product $VI$ is then positive, and it is the power the resistor absorbs and dissipates.

---

Flashcards for this section are as follows:

- overview ::@:: Under direct current conditions, with the voltage $V$ and the current $I$ both constant, the power stays at the constant value $P = VI$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- the watt as a volt-ampere: the voltage $V$ across an element and the current $I$ through it ::@:: $P = VI$, so the units multiply as $1\text{ W} = (1\text{ V})\times(1\text{ A}) = 1\text{ VA}$.
- power in terms of current and resistance: $P = VI$ with Ohm's law $V = IR$, for the current $I$ and the resistance $R$ ::@:: $P = VI = (IR)I = I^2R$.
- power in terms of voltage and resistance: $P = VI$ with Ohm's law $I = V/R$, for the voltage $V$ and the resistance $R$ ::@:: $P = V\times(V/R) = V^2/R$.
- energy consumed, also called the work done: a resistor dissipates the power $P$ for a duration $t$ ::@:: $W = Pt = VIt$, in joules when $P$ is in watts and $t$ is in seconds.
- fixed current against fixed voltage: the larger resistance $R$ of a pair, first with the two carrying the same current $I$ and then with the same voltage $V$ across each ::@:: At the same current the larger $R$ dissipates more, $P = I^2R$; at the same voltage it dissipates less, $P = V^2/R$.
- sign of the product: a resistor with the current arrow entering the terminal marked $+$ and leaving the terminal marked $-$, and $V$ across it ::@:: $P = VI$ comes out positive and is the power the resistor absorbs and dissipates.

### a single resistor across a source

A resistor of $R = 2\ \Omega$ sits across a $4\text{ V}$ source, so the voltage across it is $V = 4\text{ V}$. Its power follows from the voltage and the resistance alone, $P = V^2/R = (4\text{ V})^2/2\ \Omega = 8\text{ W}$. The current is $I = V/R = 4\text{ V}/2\ \Omega = 2\text{ A}$, and $P = VI = 4\text{ V}\times2\text{ A} = 8\text{ W}$ returns the same power. Sustained for $t = 2\text{ s}$, the resistor consumes $W = Pt = 8\text{ W}\times2\text{ s} = 16\text{ J}$.

---

Flashcards for this section are as follows:

- a single resistor across a source / power from voltage and resistance: a resistor of $R = 2\ \Omega$ has $V = 4\text{ V}$ across it; compute the power it dissipates from the voltage and the resistance. ::@:: $P = V^2/R = (4\text{ V})^2/2\ \Omega = 16/2 = 8\text{ W}$.
- a single resistor across a source / cross-check with the current: a $4\text{ V}$ source drives $I = 2\text{ A}$ through a $2\ \Omega$ resistor; check the dissipated power with $P = VI$, and state the resistance the ratio $V/I$ gives. ::@:: $P = VI = 4\text{ V}\times2\text{ A} = 8\text{ W}$, matching $P = V^2/R = 8\text{ W}$, and $V/I = 4\text{ V}/2\text{ A} = 2\ \Omega$.
- a single resistor across a source / energy over a duration: a resistor dissipates $P = 8\text{ W}$ for $t = 2\text{ s}$; what energy does it consume? ::@:: $W = Pt = 8\text{ W}\times2\text{ s} = 16\text{ J}$.

## power rating of a device

A wattage rating is quoted at a stated voltage, and that rating fixes the resistance the device presents. Two bulbs at $200\text{ V}$, one consuming $100\text{ W}$ and the other $400\text{ W}$, have $R_A = (200\text{ V})^2/100\text{ W} = 400\ \Omega$ and $R_B = (200\text{ V})^2/400\text{ W} = 100\ \Omega$: the higher-rated bulb has the lower resistance.

---

Flashcards for this section are as follows:

- overview ::@:: A power rating is quoted at a stated voltage, and it fixes the resistance the device presents at that voltage, so a bulb consuming $100\text{ W}$ at $200\text{ V}$ has $R_A = (200\text{ V})^2/100\text{ W} = 400\ \Omega$ and one consuming $400\text{ W}$ at $200\text{ V}$ has $R_B = (200\text{ V})^2/400\text{ W} = 100\ \Omega$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- which rated bulb is brighter alone: bulb A consuming $100\text{ W}$ at $200\text{ V}$ and bulb B consuming $400\text{ W}$ at $200\text{ V}$, each across $200\text{ V}$ on its own ::@:: Bulb B, the $400\text{ W}$ one: at the rated voltage its $R_B = 100\ \Omega$ is the lower resistance, against $R_A = 400\ \Omega$.

### two bulbs rated at the same voltage

In series across the same $200\text{ V}$ supply, the two bulbs share one current. Their series combination is $R_T = R_A + R_B = 400\ \Omega + 100\ \Omega = 500\ \Omega$, so the current is $I = 200\text{ V}/500\ \Omega = 0.4\text{ A}$. That current dissipates $P_A = I^2R_A = (0.4\text{ A})^2\times400\ \Omega = 64\text{ W}$ in bulb A against $P_B = I^2R_B = (0.4\text{ A})^2\times100\ \Omega = 16\text{ W}$ in bulb B. With brightness proportional to the dissipated power, the $100\text{ W}$ bulb A is now the brighter one.

---

Flashcards for this section are as follows:

- two bulbs rated at the same voltage / series current from $R_A = 400\ \Omega$ and $R_B = 100\ \Omega$ across the $200\text{ V}$ supply ::@:: $R_T = R_A + R_B = 500\ \Omega$, so the shared current is $I = 200\text{ V}/500\ \Omega = 0.4\text{ A}$.
- two bulbs rated at the same voltage / powers dissipated while the common current $I = 0.4\text{ A}$ flows through $R_A = 400\ \Omega$ and $R_B = 100\ \Omega$ ::@:: $P_A = I^2R_A = 64\text{ W}$ and $P_B = I^2R_B = 16\text{ W}$.
- two bulbs rated at the same voltage / which of the $100\text{ W}$ and $400\text{ W}$ bulbs is brighter in series across $200\text{ V}$, with brightness proportional to dissipated power ::@:: Bulb A, the $100\text{ W}$ one, dissipating $64\text{ W}$ against bulb B's $16\text{ W}$; across $200\text{ V}$ on its own instead, the $400\text{ W}$ bulb B is the brighter.
- two bulbs rated at the same voltage / fixed voltage against fixed current for the resistances $R_A = 400\ \Omega$ and $R_B = 100\ \Omega$ ::@:: At the same voltage the smaller $R_B$ takes the larger power; at the same current the larger $R_A$ dissipates more.

### resistance that varies with temperature

A filament bulb heats as it runs, so it does not hold one resistance: its rating describes the hot steady state rather than the first moment after switch-on. A bulb that draws $4\text{ A}$ from a $120\text{ V}$ DC source when cold and dissipates $60\text{ W}$ in the steady state has $R_\text{cold} = 120\text{ V}/4\text{ A} = 30\ \Omega$ against $R_\text{hot} = (120\text{ V})^2/60\text{ W} = 240\ \Omega$, an eightfold change. The cold bulb dissipates $P_\text{cold} = 120\text{ V}\times4\text{ A} = 480\text{ W}$, eight times its $60\text{ W}$ steady-state dissipation.

---

Flashcards for this section are as follows:

- resistance that varies with temperature / cold resistance of a bulb that draws $4\text{ A}$ from a $120\text{ V}$ DC source at start-up ::@:: $R_\text{cold} = 120\text{ V}/4\text{ A} = 30\ \Omega$.
- resistance that varies with temperature / hot resistance of a bulb that dissipates $60\text{ W}$ in the steady state under the same $120\text{ V}$ source ::@:: $R_\text{hot} = (120\text{ V})^2/60\text{ W} = 240\ \Omega$, eight times the cold value.
- resistance that varies with temperature / power dissipated at start-up, with $4\text{ A}$ flowing from the $120\text{ V}$ source into the $30\ \Omega$ cold filament ::@:: $P_\text{cold} = 120\text{ V}\times4\text{ A} = 480\text{ W}$.
- resistance that varies with temperature / inference from the $480\text{ W}$ cold power against the $60\text{ W}$ hot power of the same bulb ::@:: The cold filament dissipates eight times the power of the hot one.

## sign of power under the reference direction

Read along the reference direction, the product $VI$ states which way energy flows. A positive product means the element consumes or dissipates electric power: positive charge moves from the higher potential to the lower one and gives up electric potential energy. A resistor consumes power by turning electrical energy into heat. A rechargeable battery does so while charging, storing electrical energy as chemical energy.

A negative product means the element generates electric power: positive charge moves from the lower potential to the higher one and gains energy. A battery does so while discharging, converting stored chemical energy into electrical energy. A resistor cannot generate power under normal circumstances.

---

Flashcards for this section are as follows:

- overview ::@:: Read along the reference direction, a positive product $VI$ means the element consumes or dissipates electric power, so positive charge moves from the higher to the lower potential and gives up electric potential energy. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- negative product: $VI < 0$ for an element with the voltage $V$ and the current $I$ drawn along the reference direction ::@:: The element generates electric power, as positive charge moves from the lower to the higher potential and gains energy.
- power consumed by a resistor: what a resistor does with the electric power it consumes ::@:: It dissipates the power as heat, converting electrical energy into thermal energy.
- power consumed by a battery while charging: a rechargeable battery is being charged by the circuit ::@:: It consumes electric power and stores it as chemical energy.
- power generated by a discharging battery: the voltage $V$ and the current $I$ drawn along the reference direction on a battery discharging into the circuit ::@:: It generates electric power from its stored chemical energy, and the product $VI$ is negative.
- can a resistor generate power: how can the product $VI$ of a resistor come out negative ::@:: It cannot under normal circumstances, since only a source such as a battery supplies electric power.

### flashlight bulb and battery

A flashlight bulb modelled as a $3\ \Omega$ resistor carries $I_\text{bulb} = +2\text{ A}$ with $V_\text{bulb} = 6\text{ V}$ across it, so $P_\text{bulb} = V_\text{bulb}\times I_\text{bulb} = 6\text{ V}\times2\text{ A} = +12\text{ W}$, which the bulb dissipates. The battery of the same loop is measured on its own reference direction, giving $I_\text{bat} = -2\text{ A}$ against $V_\text{bat} = 6\text{ V}$, so $P_\text{bat} = V_\text{bat}\times I_\text{bat} = 6\text{ V}\times(-2\text{ A}) = -12\text{ W}$. The battery is an active element: it generates exactly the $12\text{ W}$ the bulb dissipates.

---

Flashcards for this section are as follows:

- flashlight bulb and battery / power of the bulb, modelled as a resistor, with $V_\text{bulb} = 6\text{ V}$ across it and $I_\text{bulb} = +2\text{ A}$ through it ::@:: $P_\text{bulb} = V_\text{bulb}\times I_\text{bulb} = 6\text{ V}\times2\text{ A} = +12\text{ W}$, a positive power that the bulb dissipates.
- flashlight bulb and battery / power of the battery with $V_\text{bat} = 6\text{ V}$ and $I_\text{bat} = -2\text{ A}$ on its own reference direction ::@:: $P_\text{bat} = V_\text{bat}\times I_\text{bat} = 6\text{ V}\times(-2\text{ A}) = -12\text{ W}$, so the battery is an active element whose generation covers the $12\text{ W}$ dissipated by the bulb.

## why the reference direction matters

With the reference direction drawn, the familiar forms $V = IR$ and $P = VI$ hold as written. Without it a minus sign has to be inserted in each, giving $V = -IR$ and $P = -VI$. Mechanics runs the same way: $F = ma$ holds along the chosen positive direction, and the opposite choice demands $F = -ma$.

---

Flashcards for this section are as follows:

- overview ::@:: With the reference direction drawn, the familiar relations $V = IR$ and $P = VI$ hold in their usual forms as written. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- relations with and without the reference direction: the forms $V = IR$ and $P = VI$ with the reference direction drawn ::@:: Without it the same content needs inserted minus signs, becoming $V = -IR$ and $P = -VI$.
- mechanical counterpart of the sign convention: a mass $m$ under a force $F$ has the acceleration $a$ along a chosen positive direction ::@:: Along the chosen positive direction the relation is $F = ma$; the opposite choice forces $F = -ma$.
