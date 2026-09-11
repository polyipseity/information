---
aliases:
  - ELEC 1100 electronic component
  - ELEC 1100 electronic components
  - ELEC1100 electronic component
  - ELEC1100 electronic components
  - HKUST ELEC 1100 electronic component
  - HKUST ELEC 1100 electronic components
  - HKUST ELEC1100 electronic component
  - HKUST ELEC1100 electronic components
  - electronic component
  - electronic components
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/electronic_component
  - language/in/English
---

# electronic component

- HKUST ELEC 1100

---

- see: [general/electronic component](../../../../general/electronic%20component.md)

Electronic components range from passive elements (resistors, capacitors) to active semiconductor devices ([diodes](diode.md), [transistors](transistor.md)). ELEC 1100 also covers the underlying electrical concepts and power sources (batteries, supplies) needed to understand component behaviour in the robot.

Common schematic symbols used throughout the notes: <p> ![resistor symbol](attachments/symbol_resistor.svg) <p> ![capacitor symbol](attachments/symbol_capacitor.svg) <p> ![voltage source symbol](attachments/symbol_voltage_source.svg) <p> ![ground symbol](attachments/symbol_ground.svg)

---

Flashcards for this section are as follows:

- electronic component ::@:: Elements used in electronic circuits that influence current and voltage behaviour.
- passive vs active ::@:: Passive: resistors, capacitors. Active: diodes, transistors.
- course scope ::@:: ELEC 1100 also covers basic electrical concepts and power sources (batteries, supplies).
- resistor symbol <p> ![resistor symbol](attachments/symbol_resistor.svg) ::@:: Limits current and creates voltage drops.
- capacitor symbol <p> ![capacitor symbol](attachments/symbol_capacitor.svg) ::@:: Stores charge/energy in an electric field.
- voltage source symbol <p> ![voltage source symbol](attachments/symbol_voltage_source.svg) ::@:: Maintains a fixed potential difference.
- ground symbol <p> ![ground symbol](attachments/symbol_ground.svg) ::@:: $0\text{ V}$ reference; the circuit's common return.

## electrical fundamentals

Charges at rest produce _static electricity_ (e.g. rubbing a balloon on hair transfers electrons, causing attraction). Opposite charges attract; like charges repel. Moving charges produce _current electricity_, the focus of this course.

---

Flashcards for this section are as follows:

- electricity ::@:: Flow of electrical power or charge; static = charges at rest, current = charges in motion.
- static electricity ::@:: Electrical effects from charge imbalance between objects.
- charge attraction/repulsion ::@:: Opposite charges attract; like charges repel.
- current electricity ::@:: Moving charges; the primary focus of ELEC 1100.

### atoms and charge

Atoms contain protons (+), neutrons (neutral), and electrons (−). Equal protons and electrons give a neutral atom; removing electrons produces a positive ion, adding them a negative ion. Outermost electrons are held most weakly and participate in conduction. The elementary charge is $q = 1.6\times10^{-19}\,\mathrm{C}$.

---

Flashcards for this section are as follows:

- outer electrons ::@:: Held most weakly; added or removed easily, so they participate in conduction.
- atom structure ::@:: Protons (+), neutrons (neutral), electrons (−); neutral when protons = electrons.
- elementary charge ::@:: $q = 1.6\times10^{-19}\,\mathrm{C}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- charge imbalance ::@:: Lose electrons → positive ion. Gain electrons → negative ion.

### conductors and insulators

Metals are _conductors_ (outer electrons move freely); glass and plastic are _insulators_ (tightly bound electrons restrict charge motion).

---

Flashcards for this section are as follows:

- material classification ::@:: Conductors: charges move easily. Insulators: charges are restricted.
- conductor ::@:: Charge flows readily because outer electrons require little energy to remove.
- insulator ::@:: Charge does not move easily due to tightly bound electrons.

### current

By convention, current flows in the direction positive charges would move (opposite to electron flow in metals). $I = \Delta q/\Delta t$; unit: ampere (A) = one coulomb per second.

---

Flashcards for this section are as follows:

- current definition ::@:: $I = \Delta q/\Delta t$; unit: ampere (A). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- current unit ::@:: One coulomb of charge passing a point per second.
- conventional direction ::@:: By convention, current flows in the direction positive charges would move (opposite to electron flow).
- heater example ::@:: $8.5\times10^{20}$ electrons in 10 s → $q \approx 136\,\textrm{C}$, $I \approx 13.6\,\textrm{A}$.
- battery example ::@:: 50 A for 4 s → $q = 200\,\textrm{C}$, electrons $\approx 1.25\times10^{21}$.

### voltage and potential difference

Voltage (electric potential difference) is the energy per unit charge that drives current, measured in volts between two points. _Ground_ (GND) is the $0\,\text{V}$ reference. A battery maintains a fixed voltage between its terminals, forcing current through a load.

---

Flashcards for this section are as follows:

- voltage definition ::@:: Energy per unit charge that drives current; symbol V, unit volt. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- potential difference ::@:: Voltage between two points; current flows only with a potential difference.
- ground reference ::@:: GND = $0\,\text{V}$ reference; voltage measurements are always relative.

## resistance and resistors

Resistance describes how strongly a material opposes current. For a uniform conductor: $$R = \rho\frac{L}{A}$$ where ρ is resistivity, L is length, A is cross-sectional area. An ideal wire has zero resistance; an ideal insulator has infinite resistance. Resistors have specified resistance and are used to control currents and create voltage drops. Ohm's law: $$V = IR.$$ Unit: ohm ($\Omega$). All loads and wires have resistance. Multimeters measure resistance, voltage, or current. Prefixes: kilo ($k = 10^{3}$), milli ($m = 10^{-3}$) (e.g. $10\,\text{k}\Omega = 10000\,\Omega$; $50\,\text{mA} = 0.05\,\text{A}$).

---

Flashcards for this section are as follows:

- resistance ::@:: Difficulty passing current through a substance. Unit: ohm ($\Omega$). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- resistivity formula ::@:: $R = \rho\frac{L}{A}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- resistivity ::@:: Depends on material; different materials have different values.
- ideal wire ::@:: Perfect conductor, zero resistance.
- ideal insulator ::@:: Infinite resistance.
- resistor ::@:: Limits or regulates current; colour bands encode resistance value.
- resistor usage ::@:: Controls current and creates voltage drops; all loads and wires have resistance.
- Ohm's law ::@:: $V = IR$; I–V plot is a straight line with slope $1/R$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- Ohm's law example ::@:: $V = 5\,\textrm{V}$, $R = 200\,\Omega$ → $I = 25\,\textrm{mA}$.
- multimeter ::@:: Measures resistance, voltage, or current.
- metric prefixes ::@:: kilo ($k=10^3$), milli ($m=10^{-3}$). E.g. $10\,\text{k}\Omega = 10000\,\Omega$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

## capacitors

A capacitor stores electrical energy on two conductive plates separated by an insulator. When voltage is applied, opposite charges accumulate on the plates. Removing the source lets the capacitor discharge, temporarily powering a circuit (like a water tank under pressure).

---

Flashcards for this section are as follows:

- capacitor ::@:: Passive device that stores electrical energy when connected to a voltage source.
- capacitor structure ::@:: Two conductive plates separated by an insulating material.
- capacitor energy storage ::@:: Opposite charges accumulate on plates when voltage is applied.
- capacitor action ::@:: Charges when connected, discharges when disconnected, temporarily powering loads.
- capacitor analog ::@:: Like a water tank storing fluid under pressure.

### capacitor actions

Without a capacitor, a lamp lights only while the switch is closed. A capacitor in parallel with the lamp provides a charge reservoir: when the switch opens, the capacitor discharges through the lamp, keeping it lit briefly after the source is removed.

- switch off, lamp off – capacitor initially uncharged and electrically neutral.
- switch on, lamp on – current flows from the source and the capacitor charges, plates accumulating $\pm$ charge.
- switch opened again, lamp keeps on for a while – capacitor discharges through the lamp and gradually returns to neutral.

---

Flashcards for this section are as follows:

- capacitor behaviour ::@:: Charges when connected, discharges when disconnected; smooths voltage changes.
- parallel capacitor ::@:: Gives the circuit a charge reservoir that smooths transient behaviour.
- capacitor sequence ::@:: Switch off → lamp off. Switch on → lamp on, capacitor charges. Switch opens → lamp stays on briefly as capacitor discharges.

## energy and power

Energy takes many forms (mechanical, thermal, electrical, chemical) and is conserved during conversion. In circuits, electrical energy converts to other forms (e.g. a generator converts mechanical to electrical). ELEC 1100 robots use batteries (LiPo cells) or lab DC power supplies; theoretical analysis models sources as ideal voltage generators.

Electrical energy delivered to a charge $q$ moving through a potential difference $V$ is $E = qV$, and the smallest discrete charge is $q = 1.6\times10^{-19}\,\mathrm{C}$.

Power is the rate of energy transfer: $P = E/\Delta t = \Delta q\,V/\Delta t = IV$, and by substituting Ohm's law we obtain $P = I^{2}R = V^{2}/R$ for purely resistive components.

Sources deliver DC (constant voltage/current, e.g. batteries) or AC (sinusoidal, reverses periodically: $50\,\text{Hz}$ in Hong Kong, $60\,\text{Hz}$ elsewhere). AC suits long-distance transmission and converts to DC with rectifiers.

---

Flashcards for this section are as follows:

- energy definition ::@:: Ability to do work; takes mechanical, thermal, electrical, chemical forms; conserved during conversion.
- battery role ::@:: Supplies electrical energy via electrochemical reactions; DC power with long storage.
- DC vs AC ::@:: DC: constant polarity. AC: oscillates and reverses periodically.
- household AC frequency ::@:: 50 Hz (Hong Kong) or 60 Hz (other countries). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- energy formula ::@:: $E = qV$; $q$ in coulombs. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- power definition ::@:: $P = E/\Delta t = IV$; for resistors $P = I^2R = V^2/R$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->

### energy sources in lab

Lab circuits use bench DC power supplies (regulated constant voltage) and function generators (AC waveforms for testing). See [lab equipment](lab%20equipment.md). The robot uses a rechargeable LiPo battery with a voltage/current monitor.

---

Flashcards for lab sources are as follows:

- lab DC supply ::@:: Provides regulated constant voltage for breadboard experiments.
- function generator ::@:: Produces AC waveforms of selectable frequency and amplitude.
- robot battery ::@:: Rechargeable LiPo batteries with a battery monitor.

### energy conversion

An object falling from height $h$ converts potential energy $mgh$ into kinetic energy $\tfrac12 m v^{2}$, giving $v=\sqrt{2gh}$. In circuits, the analogous conversion is between electrical potential energy and other forms when charges move through a voltage.

---

Flashcards for energy conversion are as follows:

- energy conversion example ::@:: $v=\sqrt{2gh}$; potential $mgh$ → kinetic $\tfrac12 mv^{2}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- gravitational acceleration ::@:: Independent of mass; all objects fall at the same rate neglecting air resistance.

### human body energy

For scale, the human body uses watts to tens of watts: body heat ($2\text{--}5\,\text{W}$), heartbeat ($\sim1.4\,\text{W}$), arm motion ($\sim60\,\text{W}$). Resistor power dissipation in this course is much smaller.

---

Flashcards for human body energy are as follows:

- human body energy ::@:: A few watts for heartbeat and heat; tens of watts for limb motion — much larger than small-resistor power dissipation.

### resistor networks

Series resistors add: $R_{\text{eq}} = R_1 + R_2 + \cdots$; same current through each. A voltage divider gives $V\cdot\frac{R_L}{R_S + R_L}$ at the junction.

Parallel resistors: $1/R_{\text{eq}} = 1/R_1 + 1/R_2 + \cdots$; total is smaller than the smallest branch. Conductance $G = 1/R$ (siemens).

Mixed networks reduce stepwise (e.g. $30\,\Omega + (40\,\Omega\parallel 60\,\Omega) = 54\,\Omega$). An _infinite ladder_ repeats a series/parallel pattern; model the tail as $R_{\text{eq}}$ and solve (e.g. $R_{\text{eq}} = 2R + (1.5R\parallel R_{\text{eq}})$ gives $R_{\text{eq}} = 3R$). When series/parallel alone cannot reduce a network, use [Kirchhoff's circuit laws](Kirchhoff%27s%20circuit%20laws.md).

A short circuit bypasses a component (R→0), causing very high current that can damage parts.

---

Flashcards for this section are as follows:

- series resistors ::@:: $R_{\text{eq}} = R_1 + R_2 + \cdots$; same current through each. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- voltage divider ::@:: Two series resistors; voltage at node N: $V\cdot\frac{R_L}{R_S + R_L}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- divider assumptions ::@:: Ideal wire (zero resistance) and ground ($0\,\text{V}$) reference. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- parallel resistors ::@:: $1/R_{\text{eq}} = 1/R_1 + 1/R_2 + \cdots$; conductance $G = 1/R$, unit siemens. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- infinite ladder concept ::@:: Replace the infinite tail with $R_{\text{eq}}$ and solve the equation.
- ELEC 1100 ladder example ::@:: $R_{\text{eq}} = 2R + (1.5R\parallel R_{\text{eq}})$ → $R_{\text{eq}} = 3R$.
- network example ::@:: 5 V → 30 Ω + (40 Ω ∥ 60 Ω) → $R_{\text{eq}}=54\,\Omega$, $I\approx0.093\,\textrm{A}$.
- short circuit ::@:: Near-zero-resistance path causing very high current; can damage components.

### worked calculations

- Example power dissipated by a $200\,\Omega$ resistor with $5\text{ V}$ across it: $P = V^{2}/R = 0.125\text{ W}$.
- Network example: a $10\text{ V}$ source drives a $2\,\Omega$ resistor in series with a parallel combination of a single $2\,\Omega$ branch and another branch composed of two $2\,\Omega$ resistors in series; the equivalent resistance is $R=\tfrac{10}{3}\,\Omega$ and the total current is $I=3\text{ A}$ (slide example).
- Challenging series/parallel example: a source of $5\text{ V}$ drives two equal resistors $R_S=R_L=2.4\text{ k}\Omega$; total $R=4.8\text{ k}\Omega$ giving $I=1.04\text{ mA}$, so $P_{R_L}=I^{2}R_L\approx2.6\text{ mW}$ (same result whether computed via current or halving total power).

---

Flashcards for this section are as follows:

- power calculation ::@:: $200\,\Omega$ with 5 V → $P=V^{2}/R = 0.125\text{ W}$.
- parallel current ::@:: Two 2 Ω in parallel with 10 V → $R_{\text{eq}}=1\,\Omega$, $I=10\,\text{A}$.
- series-plus-parallel network ::@:: 10 V → 2 Ω + (2 Ω ∥ 4 Ω) → $R=10/3\,\Omega$, $I=3\text{ A}$.
- series/parallel power ::@:: 5 V, two 2.4 kΩ in series → $P_{R_L}\approx2.6\text{ mW}$.
