---
aliases:
  - ELEC 2400 voltage source
  - ELEC2400 voltage source
  - HKUST ELEC 2400 voltage source
  - HKUST ELEC2400 voltage source
  - voltage source
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/voltage_source
  - language/in/English
---

# voltage source

A circuit needs at least one element that drives charge around it. The ideal voltage source is the simplest such driver: it holds a fixed potential difference across its two terminals however the rest of the circuit is arranged. Its voltage is fixed, while the current through it is set by the circuit around it.

A battery is the familiar physical realisation.

---

Flashcards for this section are as follows:

- overview ::@:: A circuit needs at least one element that drives charge around it. The ideal voltage source is the simplest such model. It holds a fixed potential difference across its two terminals however the rest of the circuit is arranged.
- what the source fixes: which terminal quantity of an ideal voltage source of voltage $V_s$ is known from the source alone, and which is not? ::@:: $V_s$ is known from the source alone. The current is set by the external circuit.

## ideal voltage source

An ideal voltage source, also called an independent voltage source, maintains the constant voltage $V_s$ across its terminals independently of the load and of the current it carries. Circuit diagrams mark it with a circle holding a $+$ mark and a $-$ mark, with a rectangle holding the same two marks, or with the battery symbol of two parallel lines of unequal length whose longer line is the positive terminal. <p> ![battery symbol: two parallel lines of unequal length, the longer line on top](attachments/symbol_source_battery.svg) ![source symbol: a circle holding a plus mark above a minus mark](attachments/symbol_source_circle.svg) ![source symbol: a rectangle holding a plus mark above a minus mark](attachments/symbol_source_rectangle.svg)

Because the voltage is fixed, the element has no single operating current: its current plotted against its voltage is the single vertical line at $V_s$, so a current of any size in either direction pairs with the same terminal voltage.

---

Flashcards for this section are as follows:

- overview ::@:: An ideal voltage source, also named an independent voltage source, maintains the constant voltage $V_s$ across its terminals independently of the load and of the current through it. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- circuit symbol: which drawings stand for an ideal voltage source of voltage $V_s$ in a circuit diagram? <p> ![battery symbol: two parallel lines of unequal length, the longer line on top](attachments/symbol_source_battery.svg) ![source symbol: a circle holding a plus mark above a minus mark](attachments/symbol_source_circle.svg) ![source symbol: a rectangle holding a plus mark above a minus mark](attachments/symbol_source_rectangle.svg) ::@:: A circle carrying a $+$ mark and a $-$ mark inside it, a rectangle carrying the same two marks, or the battery symbol of two parallel lines of unequal length with the longer line at the positive terminal.
- draw the source: how is an ideal voltage source of voltage $V_s$ drawn in a circuit diagram? ::@:: A circle, a rectangle, or a battery, each carrying a $+$ mark and a $-$ mark, with the longer line or the $+$ mark at the positive terminal. <p> ![battery symbol: two parallel lines of unequal length, the longer line on top](attachments/symbol_source_battery.svg) ![source symbol: a circle holding a plus mark above a minus mark](attachments/symbol_source_circle.svg) ![source symbol: a rectangle holding a plus mark above a minus mark](attachments/symbol_source_rectangle.svg)
- physical realisation: which physical device is the standard realisation of a voltage source? ::@:: The battery.
- I-V characteristic: what does the current-against-voltage plot of an ideal voltage source of voltage $V_s$ look like? ::@:: The current $I_s$ plotted against the voltage is the vertical line at $V_s$. With the voltage plotted against the current, the same relation is the horizontal line at $V_s$.
- which quantity follows the load: which terminal quantity of an ideal voltage source of voltage $V_s$ follows the load, and which stays fixed? ::@:: The current follows the load, while the terminal voltage stays at $V_s$.

### output voltage under several loads

An ideal source of $30\text{ V}$ drives a load $R$ across its terminals, with the output $V_o$ taken across that load. It holds $V_o = 30\text{ V}$ for the resistances $1\ \Omega$, $1\text{ G}\Omega$, and $0.1\ \Omega$ alike, a span of ten orders of magnitude, while the current is what changes: $I = V_o/R$ gives $30\text{ A}$, $30\text{ nA}$, and $300\text{ A}$ respectively. At $R = 0\ \Omega$ the load becomes a short circuit, holding the terminals at $0\text{ V}$ while the source insists on $30\text{ V}$, so $V_o$ has no defined value and an ideal voltage source cannot drive a short circuit.

---

Flashcards for this section are as follows:

- finite loads: an ideal voltage source of $30\text{ V}$ drives a load $R$ with $V_o$ across it; give $V_o$ for $R = 1\ \Omega$, $R = 1\text{ G}\Omega$, and $R = 0.1\ \Omega$. ::@:: $V_o = 30\text{ V}$ in all three cases, while the load current runs $30\text{ A}$, $30\text{ nA}$, and $300\text{ A}$.
- short circuit: an ideal voltage source of $30\text{ V}$ is connected across a load of $R = 0\ \Omega$; what is $V_o$? ::@:: Undefined: $30\text{ V}$ across the terminals and $0\text{ V}$ across the short cannot both hold.
- why the short circuit fails: how does a load of $R = 0\ \Omega$ conflict with an ideal voltage source of voltage $V_s$? ::@:: The load demands $0\text{ V}$ across the terminals while the source insists on $V_s$ at every current.

## sourcing and sinking current

Reference directions give the current through a voltage source a sign, and the sign decides whether the element delivers energy or absorbs it. The voltage $V_s$ is marked $+$ at one terminal and $-$ at the other, and the reference current $I_s$ is drawn into the $+$ terminal, so the power absorbed by the source is $P = V_sI_s$.

A positive $I_s$ means current entering the $+$ terminal, so the source sinks current and dissipates power. A negative $I_s$ means current leaving the $+$ terminal, so the source sources current and generates power, with $P < 0$.

---

Flashcards for this section are as follows:

- overview ::@:: With $V_s$ marked $+$ at one terminal and $-$ at the other and the reference current $I_s$ drawn into the $+$ terminal, the sign of $I_s$ decides whether the source sinks or sources current, and the power absorbed by the source is $P = V_sI_s$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- sinking: with $I_s$ drawn into the $+$ terminal of a voltage source of voltage $V_s$ and $I_s > 0$, what is the source doing and what is the sign of its power? ::@:: It sinks current and dissipates power, with $P = V_sI_s > 0$.
- sourcing: with $I_s$ drawn into the $+$ terminal of a voltage source of voltage $V_s$ and $I_s < 0$, what is the source doing and what is the sign of its power? ::@:: It sources current and generates power, with $P = V_sI_s < 0$. That is the normal operation of a voltage source.
- reading the sign: for a voltage source whose reference current $I_s$ runs into its $+$ terminal, does $I_s > 0$ mean the source delivers current to the circuit? ::@:: No: a positive $I_s$ enters the $+$ terminal, so the source absorbs power. It delivers current to the circuit when $I_s < 0$.

## parallel connection of voltage sources

Each source sinks or sources whatever current it takes to force the circuit in parallel with it to adopt its own potential difference. With $V_1 > V_2$, the first sources a large current to force the second up to $V_1$ while the second sinks a large current to force the first down to $V_2$. Two sources whose potentials differ, $V_1 \neq V_2$, must never be connected in parallel.

Both sources hold their own terminal voltage at every current, so no single potential difference across the pair can equal both $V_1$ and $V_2$. The ideal model cannot resolve the conflict. With physical devices, the large current each one drives may destroy both.

---

Flashcards for this section are as follows:

- overview ::@:: Two voltage sources of different potentials must never be connected in parallel: each sinks or sources whatever current it takes to force the circuit in parallel with it to adopt its own potential difference.
- mechanism when one potential is larger: voltage sources of $V_1$ and $V_2$ sit in parallel with $V_1 > V_2$; what does each source do? ::@:: $V_1$ sources a large current to force $V_2$ to become $V_1$, while $V_2$ sinks a large current to force $V_1$ to become $V_2$.
- conflict in the model: voltage sources of $V_1$ and $V_2$ sit in parallel with $V_1 \neq V_2$; why does an ideal model give no consistent answer? ::@:: Each source fixes its own terminal voltage at every current, so a single potential difference across the pair cannot equal both $V_1$ and $V_2$.
- physical consequence: two physical voltage sources of different potentials are connected in parallel; what can result? ::@:: The large current each one drives may destroy both devices.

## practical voltage source

A practical voltage source is modelled as an ideal voltage source of voltage $V_s$ with a small but non-zero internal resistance $R_s$ in series. The series resistance bounds the current the device delivers. Keeping it small brings the device close to the ideal element.

Its terminal voltage follows the divider between $R_s$ and the load: slightly below $V_s$, and approaching $V_s$ as the load resistance grows large against $R_s$.

---

Flashcards for this section are as follows:

- overview ::@:: A practical voltage source is modelled as an ideal voltage source of voltage $V_s$ with a small but non-zero internal resistance $R_s$ in series. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- why the internal resistance is non-zero: why must the internal resistance $R_s$ of a practical voltage source of voltage $V_s$ be non-zero? ::@:: A real device cannot deliver unlimited current. The series resistance bounds it.
- why the internal resistance is kept small: why is $R_s$ kept small in a practical voltage source of voltage $V_s$? ::@:: Keeping it small holds the terminal voltage close to $V_s$.

### terminal voltage under load

With the internal resistance $R_s$ in series with the load $R$, the source and its load form a divider: the output across the load is $V_o = V_sR/(R + R_s)$, and the shortfall from $V_s$ is the drop across $R_s$.

A $5\text{ V}$ source with $R_s = 1\text{ m}\Omega$ driving $R = 100\ \Omega$ gives $V_o = 5\text{ V}\times100\ \Omega/(100\ \Omega + 1\text{ m}\Omega) \approx 4.99995\text{ V}$, about $5\text{ V}$. The load current is about $50\text{ mA}$ and the drop across $R_s$ about $50\ \mu\text{V}$.

---

Flashcards for this section are as follows:

- divider formula: a practical voltage source of voltage $V_s$ has an internal resistance $R_s$ in series with a load $R$; express the output voltage $V_o$ across the load. ::@:: $V_o = V_sR/(R + R_s)$.
- worked output: a $5\text{ V}$ source has an internal resistance $R_s = 1\text{ m}\Omega$ and drives a load $R = 100\ \Omega$; find the output voltage $V_o$. ::@:: $V_o = V_sR/(R + R_s) = 5\text{ V}\times100\ \Omega/(100\ \Omega + 1\text{ m}\Omega) \approx 4.99995\text{ V}$, about $5\text{ V}$.
- size of the effect: a $5\text{ V}$ source with $R_s = 1\text{ m}\Omega$ drives a $100\ \Omega$ load to $V_o \approx 5\text{ V}$; what are the load current and the drop across $R_s$? ::@:: The load current is about $50\text{ mA}$, and the drop across $R_s$ is about $50\ \mu\text{V}$.
