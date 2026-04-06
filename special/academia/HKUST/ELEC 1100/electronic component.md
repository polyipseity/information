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

Electronic components are the building blocks of electronic circuits; they affect how currents flow and voltages appear, and range from passive elements such as resistors and capacitors to active semiconductor devices like [diodes](diode.md) and [transistors](transistor.md).  In ELEC 1100 the scope is expanded to include the underlying electrical concepts required to understand component behaviour, together with the power sources and delivery systems (batteries, supplies) that energise a robot's electronic subsystems.

Common schematic symbols used throughout the notes: <p> ![resistor symbol](attachments/symbol_resistor.svg) <p> ![capacitor symbol](attachments/symbol_capacitor.svg) <p> ![voltage source symbol](attachments/symbol_voltage_source.svg) <p> ![ground symbol](attachments/symbol_ground.svg)

---

Flashcards for this section are as follows:

- electronic component definition ::@:: Electronic components are the building blocks used in electronic circuits that influence the behaviour of currents and voltages. <!--SR:!2026-05-12,54,310!2026-05-20,61,310-->
- passive vs active examples ::@:: Passive elements like resistors and capacitors contrast with active semiconductor devices such as diodes and transistors. <!--SR:!2026-05-24,64,310!2026-05-17,58,310-->
- course context ::@:: In ELEC 1100, electronic components also include basic electrical concepts needed to understand how components operate. <!--SR:!2026-05-15,57,310!2026-05-14,56,310-->
- active device examples ::@:: Active semiconductor devices include diodes and transistors, distinguishing them from passive elements. <!--SR:!2026-05-13,55,310!2026-05-24,64,310-->
- power/energy context ::@:: In ELEC 1100, electronic components also encompass power sources and delivery systems such as batteries and supplies that provide energy. <!--SR:!2026-06-29,83,363!2026-05-28,56,343-->
- schematic symbol: resistor <p> ![resistor symbol](attachments/symbol_resistor.svg) ::@:: Resistor symbol (zigzag/box style depending on standard) representing a component that limits current and creates voltage drops. <!--SR:!2026-06-29,83,363!2026-06-25,79,363-->
- schematic symbol: capacitor <p> ![capacitor symbol](attachments/symbol_capacitor.svg) ::@:: Capacitor symbol (two plates) representing a component that stores charge/energy in an electric field. <!--SR:!2026-06-26,80,363!2026-07-04,87,363-->
- schematic symbol: DC voltage source <p> ![voltage source symbol](attachments/symbol_voltage_source.svg) ::@:: Ideal DC voltage source symbol representing a supply that maintains a fixed potential difference. <!--SR:!2026-07-05,88,363!2026-06-29,83,363-->
- schematic symbol: ground (GND, $0\text{ V}$ reference) <p> ![ground symbol](attachments/symbol_ground.svg) ::@:: Ground/reference node symbol ( $0\text{ V}$ reference) used as the circuit's common return. <!--SR:!2026-04-09,19,343!2026-07-04,87,363-->

## electrical fundamentals

Electricity arises from electric charge; when charges accumulate at rest the phenomenon is called _static electricity_, a behaviour often demonstrated with balloons and combs (for example, rubbing a balloon on hair transfers electrons onto the balloon, leaving the hair positively charged and causing attraction or repulsion).  Opposite charges attract while like charges repel, and when charges move in an organised way the result is _current electricity_, which is the focus of this course.

---

Flashcards for this section are as follows:

- electricity ::@:: Electricity is the flow of electrical power or charge; static electricity occurs when charges gather in one place and current electricity is when they move. <!--SR:!2026-05-15,57,310!2026-05-17,58,310-->
- static electricity ::@:: Electrical effects caused by an imbalance of positive and negative charges between objects. <!--SR:!2026-05-17,58,310!2026-05-22,62,310-->
- charge attraction/repulsion ::@:: Opposite charges attract; like charges repel. <!--SR:!2026-04-30,42,290!2026-05-15,57,310-->
- current electricity focus ::@:: Current electricity refers to moving charges and is the primary focus of ELEC 1100. <!--SR:!2026-05-23,63,310!2026-05-20,61,310-->

### atoms and charge

Atoms contain positively charged protons, neutral neutrons and negatively charged electrons; when protons and electrons are equal the atom is electrically neutral, but removing electrons leaves a positive ion and adding them produces a negative ion.  The outermost electrons are held most weakly and can be added or removed with relatively little energy, which is why they participate in electrical conduction.  The elementary charge carried by one proton (or the magnitude carried by one electron) is approximately $1.6\times10^{-19}\,\mathrm{C}$.

---

Flashcards for this section are as follows:

- outer electrons conduction ::@:: Electrons in the outermost orbit are held most weakly and can be added or removed easily, which is why they participate in conduction. <!--SR:!2026-05-22,63,310!2026-05-21,62,310-->
- atom structure ::@:: An atom consists of protons (positive), neutrons (neutral), and electrons (negative); it is electrically neutral when protons equal electrons. <!--SR:!2026-05-18,59,310!2026-05-13,55,310-->
- elementary charge ::@:: The smallest amount of electric charge is the charge of one proton or electron, $q = 1.6\times10^{-19}\,\mathrm{C}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-12,54,310!2026-05-22,63,310-->
- charge imbalance ::@:: When atoms lose electrons they become positively charged; when they gain electrons they become negatively charged. <!--SR:!2026-05-25,65,310!2026-05-27,67,310-->

### conductors and insulators

Materials are classified by how easily charges can move through them. Metals are _conductors_ because their outer electrons are loosely bound and can move freely; materials such as glass or plastic are _insulators_ and restrict charge motion due to tightly bound electrons.

---

Flashcards for this section are as follows:

- material classification ::@:: Materials are classified by how easily charges can move through them, with conductors allowing easy flow and insulators restricting movement. <!--SR:!2026-05-20,61,310!2026-05-23,63,310-->
- conductor definition ::@:: A conductor is a material through which charge flows readily because its atoms require little energy to remove outer electrons. <!--SR:!2026-05-19,60,310!2026-05-22,63,310-->
- insulator definition ::@:: An insulator is a material that does not allow charge to move easily due to tightly bound electrons. <!--SR:!2026-05-13,55,310!2026-05-19,60,310-->

### current

By convention, the direction of current is taken to be the direction in which positive charges would move, which is opposite to the actual electron flow in metals.  Current quantifies the rate at which charge passes a point in a circuit; by definition $I = \Delta q/\Delta t$ where $\Delta q$ is the charge transported in time $\Delta t$, and the unit is the ampere (A), equivalent to one coulomb per second.  Although the carriers in metallic conductors are electrons, the conventional current direction remains that of hypothetical positive charges.

---

Flashcards for this section are as follows:

- current definition ::@:: Current is the orderly movement of charged particles; $I = \Delta q/\Delta t$, measured in amperes (1&nbsp;A = 1&nbsp;C/s). <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-07-01,84,363!2026-06-28,82,363-->
- current unit ::@:: The unit of current is the ampere, defined as one coulomb of charge passing a point per second. <!--SR:!2026-07-01,84,363!2026-06-25,79,363-->
- electron vs conventional direction ::@:: In metal wires only electrons move; by convention current direction is the direction positive charges would move (opposite electron flow). <!--SR:!2026-06-26,80,363!2026-06-26,80,363-->
- current example heater: A heater draws $8.5\times10^{20}$ electrons in $10\,\textrm{s}$ ($e=1.6\times10^{-19}\,\textrm{C}$); find $q$ and $I$. ::@:: $q=Ne\approx136\,\textrm{C}$ and $I=q/t\approx13.6\,\textrm{A}$. <!--SR:!2026-06-29,83,363!2026-05-28,56,343-->
- battery example: A battery supplies $50\,\textrm{A}$ for $4\,\textrm{s}$ ($e=1.6\times10^{-19}\,\textrm{C}$); find $q$ and number of electrons. ::@:: $q=It=200\,\textrm{C}$, electrons = $q/e\approx1.25\times10^{21}$. <!--SR:!2026-04-09,19,343!2026-06-12,65,343-->

### voltage and potential difference

voltage (electric potential difference) is the energy per unit charge that drives current. It is measured in volts and is always defined between two points; a reference point called _ground_ (GND) is conventionally assigned $0\,\text{V}$. A battery, for example, maintains a fixed voltage difference between its terminals that forces current through a connected load.

---

Flashcards for this section are as follows:

- voltage definition ::@:: Voltage is the force that makes electrons move through a conductor; symbol V, unit volt (V). <!--SR:!2026-05-15,57,310!2026-05-25,65,310-->
- potential difference ::@:: Voltage is a difference in electric potential between two points; current flows only if there is a potential difference. <!--SR:!2026-05-12,54,310!2026-05-26,66,310-->
- ground reference ::@:: Ground (GND) is a circuit reference point defined to be $0\,\text{V}$; voltage measurements are always relative to another point. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-05-12,54,310!2026-05-27,67,310-->

## resistance and resistors

Resistance describes how strongly a material opposes the flow of current. For a uniform conductor its resistance is given by $$R = \rho\frac{L}{A}$$ where ρ is the material's resistivity, L its length and A its cross-sectional area. The resistivity ρ depends on the material – copper, aluminium and stainless steel all have different values. An "ideal wire" is treated as an ideal conductor with zero resistance, while an ideal insulator has infinite resistance; real components fall between these extremes, exhibiting finite resistance. Components called resistors have a specified resistance and are used to control currents and create voltage drops. Ohm's law relates voltage, current and resistance: $$V = IR.$$ The unit of resistance is the ohm ($\Omega$), and the symbol R is commonly used in formulas. Resistance can be added to avoid large currents; all loads (light bulbs, motors) and even wires have resistance. Digital multimeters may be used to measure resistance, voltage, or current in lab. Prefixes such as kilo ($k = 10^{3}$) and milli ($m = 10^{-3}$) are applied to ohms and amperes (e.g. $10\,\text{k}\Omega = 10000\,\Omega$; $50\,\text{mA} = 0.05\,\text{A}$).

---

Flashcards for this section are as follows:

- resistance definition ::@:: Resistance is a measure of the difficulty in passing current through a substance. <!--SR:!2026-04-09,19,343!2026-07-03,86,363-->
- unit of resistance ::@:: The unit of resistance is the ohm ($\Omega$), symbol $R$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-06-24,78,363!2026-04-09,19,343-->
- resistivity formula ::@:: $R = \rho\frac{L}{A}$ for a wire of length $L$ and area $A$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-09,19,343!2026-04-09,19,343-->
- resistivity depends on material ::@:: The resistivity ρ in the resistance formula depends on the material of the conductor; different materials have different resistivities. <!--SR:!2026-07-04,87,363!2026-06-29,83,363-->
- ideal wire ::@:: An ideal wire is treated as a perfect conductor and therefore has no resistance. <!--SR:!2026-07-04,87,363!2026-06-29,83,363-->
- ideal insulator ::@:: An ideal insulator has infinite resistance and does not allow current to flow. <!--SR:!2026-06-28,82,363!2026-07-05,88,363-->
- resistor definition ::@:: A resistor is a device that limits or regulates current flow in a circuit; colour bands on a resistor encode its resistance value. <!--SR:!2026-04-09,19,343!2026-04-09,19,343-->
- resistor usage ::@:: Resistors control current and create voltage drops; all loads and even connecting wires inherently have resistance. <!--SR:!2026-06-23,77,363!2026-06-27,81,363-->
- Ohm's law ::@:: $V = IR$; an I–V plot for a resistor is a straight line with slope $1/R$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-07-05,88,363!2026-04-09,19,343-->
- Ohm's law example: Given $V = 5\,\textrm{V}$ across a resistor $R = 200\,\Omega$, what is the current? ::@:: Use $I = V/R$ to calculate $25\,\textrm{mA}$. <!--SR:!2026-07-04,87,363!2026-04-09,19,343-->
- multimeter use ::@:: Digital multimeters may be used to measure resistance, voltage, or current in laboratory circuits. <!--SR:!2026-06-27,81,363!2026-07-03,86,363-->
- metric prefixes ::@:: Prefixes such as kilo ($k=10^{3}$) and milli ($m=10^{-3}$) are applied to ohms and amperes (e.g. $10\,\text{k}\Omega = 10000\,\Omega$; $50\,\text{mA} = 0.05\,\text{A}$). <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-09,19,343!2026-06-28,82,363-->

## capacitors

A capacitor consists of two conductive plates separated by an insulating material. When a voltage is applied, opposite charges accumulate on the plates, storing electrical energy. If the voltage source is removed the capacitor can discharge and supply current for a short period, temporarily powering a circuit. A common analogy is a water tank storing fluid under pressure.

---

Flashcards for this section are as follows:

- capacitor definition ::@:: A capacitor is a passive device that can store electrical energy when connected to a voltage source. <!--SR:!2026-05-14,56,310!2026-05-15,57,310-->
- capacitor structure ::@:: A capacitor consists of two conductive plates separated by an insulating material. <!--SR:!2026-05-15,57,310!2026-05-21,62,310-->
- capacitor energy storage ::@:: When a voltage is applied, opposite charges accumulate on the plates, storing electrical energy. <!--SR:!2026-05-13,55,310!2026-05-20,61,310-->
- capacitor action ::@:: When connected, the capacitor charges and current flows; when disconnected it discharges and can keep a lamp lit for a while. <!--SR:!2026-05-22,63,310!2026-05-14,56,310-->
- capacitor discharge ::@:: If the voltage source is removed the capacitor can discharge and supply current for a short period, temporarily powering a circuit. <!--SR:!2026-05-14,56,310!2026-05-18,59,310-->
- capacitor analog ::@:: The water analog for a capacitor is a tank that stores fluid under pressure; the capacitor stores charge under voltage. <!--SR:!2026-05-19,60,310!2026-05-04,44,290-->

### capacitor actions

Simple circuits illustrate how a capacitor changes transient behaviour. Without any capacitor the lamp only lights while the switch is closed; opening the switch immediately extinguishes the lamp because the supply and load are disconnected. Inserting a capacitor in parallel with the lamp gives the circuit a charge reservoir. When the switch is opened the capacitor discharges through the lamp, allowing it to stay lit for a short time even though the source is removed. The sequence can be summarised as follows:

- switch off, lamp off – capacitor initially uncharged and electrically neutral.
- switch on, lamp on – current flows from the source and the capacitor charges, plates accumulating $\pm$ charge.
- switch opened again, lamp keeps on for a while – capacitor discharges through the lamp and gradually returns to neutral.

---

Flashcards for this section are as follows:

- capacitor action ::@:: A capacitor charges when connected and discharges when disconnected, smoothing voltage changes and temporarily powering loads. <!--SR:!2026-05-16,58,310!2026-05-19,60,310-->
- parallel capacitor role ::@:: Placing a capacitor in parallel with a load gives the circuit a charge reservoir that helps smooth transient behaviour when switches change state. <!--SR:!2026-05-17,58,310!2026-05-18,59,310-->
- capacitor sequence ::@:: Switch off, lamp off; switch on, lamp on and capacitor charges; switch opened again lamp keeps on for a while as the capacitor discharges. <!--SR:!2026-05-21,61,310!2026-05-21,61,310-->

## energy and power

Energy is the ability to do work and, although it can take many forms — mechanical, thermal, electrical, chemical, and so on — our interest in circuits is with electrical energy; this quantity may be converted from one form to another while the total energy remains conserved (for example, mechanical energy becomes electrical energy in a generator).

Just as people gain energy by eating food, robots must be fed electrical power from a source such as a battery or power supply.

In the context of ELEC 1100, robots derive their power primarily from batteries (disposable or rechargeable LiPo cells) or, in the lab, from DC power supplies and function generators; batteries supply direct‑current power through electrochemical reactions and can hold energy for days or years, and for theoretical analysis sources are usually modelled as ideal voltage generators.

Electrical energy delivered to a charge $q$ moving through a potential difference $V$ is $E = qV$, and the smallest discrete charge is $q = 1.6\times10^{-19}\,\mathrm{C}$.

Power is the rate of energy transfer: $P = E/\Delta t = \Delta q\,V/\Delta t = IV$, and by substituting Ohm's law we obtain $P = I^{2}R = V^{2}/R$ for purely resistive components.

Electrical sources may deliver either direct current (DC) or alternating current (AC).  In a DC supply the voltage and current are essentially constant in time – batteries and the LiPo packs used on your robot are examples – so the direction of current flow never reverses.  Household mains power is AC: the voltage oscillates sinusoidally and the current changes direction periodically ($50\,\text{Hz}$ in Hong Kong, $60\,\text{Hz}$ in some other countries).  AC is convenient for transmission over long distances and can be converted to DC with rectifiers.

---

Flashcards for this section are as follows:

- energy definition ::@:: Energy is the ability to do work and can take forms like mechanical, thermal, electrical, or chemical; it is conserved during conversion. <!--SR:!2026-07-03,86,363!2026-04-09,19,343-->
- battery energy role ::@:: Batteries supply electrical energy through electrochemical reactions and provide DC power with long storage times. <!--SR:!2026-06-29,83,363!2026-07-03,86,363-->
- human/robot analogy ::@:: People get energy by eating food while robots obtain energy from batteries or power supplies. <!--SR:!2026-04-09,19,343!2026-06-05,59,343-->
- DC vs AC ::@:: Direct current (DC) has constant polarity and amplitude; alternating current (AC) oscillates and reverses direction periodically. <!--SR:!2026-06-29,83,363!2026-07-02,85,363-->
- household AC frequency ::@:: Mains electricity typically alternates at $50\,\text{Hz}$ (Hong Kong) or $60\,\text{Hz}$ (some other countries). <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-07-03,86,363!2026-04-09,19,343-->
- energy formula circuit ::@:: Electrical energy delivered to charge $q$ through a voltage $V$ is $E = qV$, with $q$ measured in coulombs. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-07-05,88,363!2026-04-09,19,343-->
- power definition ::@:: Power is the rate of energy consumption; $P = E/\Delta t = IV$ and for resistors $P = I^2R = V^2/R$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-06-29,83,363!2026-04-09,19,343-->

### energy sources in lab

At the HKUST electronics lab you will typically power circuits from bench supplies: a DC power supply provides a regulated constant-voltage source, while a function generator can supply small AC waveforms (sine, square, triangle) for testing.  Both connect to your breadboard where components are assembled. See [lab equipment](lab%20equipment.md) for the DC supply, function generator, DSO, and breadboard.  For your project robot the primary energy source is a rechargeable lithium‑polymer (LiPo) battery paired with a battery monitor that reports voltage and current.

---

Flashcards for lab sources are as follows:

- lab DC supply ::@:: A DC power supply provides a regulated constant voltage for breadboard experiments. <!--SR:!2026-04-09,19,343!2026-04-09,19,343-->
- function generator ::@:: A function generator produces AC waveforms of selectable frequency and amplitude. <!--SR:!2026-07-05,88,363!2026-04-09,19,343-->
- robot battery ::@:: Project robots use rechargeable LiPo batteries monitored by a battery monitor. <!--SR:!2026-06-29,83,363!2026-04-09,19,343-->

### energy conversion

One way to visualise energy is by considering gravitational potential becoming kinetic energy.  Galileo's famous Leaning‑Tower‑of‑Pisa experiment (or the later Apollo 15 Moon drop) showed that acceleration due to gravity $g$ is independent of mass.  An object falling from height $h$ converts potential energy $mgh$ into kinetic energy $\tfrac12 m v^{2}$, giving the relation $v=\sqrt{2gh}$.  In circuits the analogous conversion is between electrical potential energy and other forms when charges move through a voltage.

---

Flashcards for energy conversion are as follows:

- energy conversion example ::@:: Galileo's falling objects experiment shows $v=\sqrt{2gh}$, relating potential $mgh$ to kinetic $\tfrac12 mv^{2}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-09,19,343!2026-07-02,85,363-->
- gravitational acceleration ::@:: The acceleration due to gravity is independent of mass, so all objects fall at the same rate neglecting air resistance. <!--SR:!2026-04-09,19,343!2026-07-05,88,363-->

### human body energy

For context, the human body itself uses electrical, chemical and mechanical power on the order of watts to tens of watts: body heat ($2\text{--}5\,\text{W}$), heartbeat ($\sim1.4\,\text{W}$), arm motion ($\sim60\,\text{W}$), footfalls ($\sim67\,\text{W}$) and so on.  This comparison emphasises that the milliwatt and watt‑level powers we calculate for resistors are small compared with everyday biological energy use.

---

Flashcards for human body energy are as follows:

- human body energy ::@:: A human body expends a few watts for heartbeat and thermal output, and tens of watts for limb motion, much larger than the power dissipated in small resistors. <!--SR:!2026-06-29,83,363!2026-04-09,19,343-->

### resistor networks

Resistors in series add: $R_{\text{eq}} = R_1 + R_2 + \cdots$; the same current flows through each. A voltage divider is a pair of series resistors; the voltage at the junction N relative to ground is $V\cdot\frac{R_L}{R_S + R_L}$ assuming ideal wire (zero resistance) and ground reference.

Resistors in parallel combine as $1/R_{\text{eq}} = 1/R_1 + 1/R_2 + \cdots$; the total resistance is always smaller than the smallest branch. Conductance $G = 1/R$ is useful, unit siemens (S).

For a network with mixed series/parallel elements the total resistance may be computed stepwise (e.g. $30\,\Omega + (40\,\Omega\parallel 60\,\Omega) = 54\,\Omega$). Some tutorial problems use an _infinite resistor network_ (ladder): a small series/parallel pattern (such as a $2R$ series resistor followed by a $1.5R$ shunt to ground) is repeated indefinitely so that the "tail" of the ladder looks identical to the whole network. In that case you model the infinite tail by a single unknown equivalent $R_{\text{eq}}$ and write an equation like $R_{\text{eq}} = 2R + (1.5R\parallel R_{\text{eq}})$ using the usual parallel formula; solving gives $R_{\text{eq}} = 3R$ in the ELEC 1100 example. When a network cannot be reduced by series/parallel alone, use [Kirchhoff's circuit laws](Kirchhoff%27s%20circuit%20laws.md) to relate currents and voltages at nodes and loops.

Short circuit occurs when a low-resistance path bypasses a component (R→0); current through the short tends to infinity and components may be damaged. In an ideal short the branch current is infinite and the other branch zero.

Resistors dissipate electrical power as heat, which is why excessive current can make a resistor get hot or even burn.  The video linked in the slides demonstrates a resistor glowing when driven beyond its power rating.

---

Flashcards for this section are as follows:

- series resistors formula ::@:: Resistors in series simply add: $R_{\text{eq}} = R_1 + R_2 + \cdots$ (same current through each). <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-07-04,87,363!2026-06-29,83,363-->
- voltage divider ::@:: A voltage divider is two series resistors; assuming an ideal wire and ground, setup the circuit as V → RS → N → RL → GND → (V), then the voltage at node N is $V\cdot\frac{R_L}{R_S + R_L}$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-09,19,343!2026-06-29,83,363-->
- series divider assumptions ::@:: The voltage-divider formula assumes an ideal wire (zero resistance) and that the reference node is ground ($0\,\text{V}$). <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-07-05,88,363!2026-04-09,19,343-->
- parallel resistors formula ::@:: Resistors in parallel satisfy $1/R_{\text{eq}} = 1/R_1 + 1/R_2 + \cdots$; conductance $G = 1 / R$ with unit siemens. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-09,19,343!2026-07-03,86,363-->
- conductance units ::@:: Conductance $G=1/R$ is measured in siemens (S); older units mho or ℧ are equivalent. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-09,19,343!2026-07-05,88,363-->
- infinite ladder concept: Given an infinite resistor ladder built by repeating a small series/parallel cell, how can you model the resistance of the "tail" of the network in terms of an unknown $R_{\text{eq}}$? ::@:: Because the part of the ladder to the right of any cell looks identical to the whole, you can replace the infinite tail by a single unknown equivalent resistance $R_{\text{eq}}$ and solve for it. <!--SR:!2026-04-09,19,343!2026-06-27,81,363-->
- ELEC 1100 infinite ladder example: Given the ELEC 1100 ladder made from repeating a $2R$ series resistor with a $1.5R$ shunt to ground, how do you find its equivalent resistance? ::@:: Write the equation $R_{\text{eq}} = 2R + (1.5R\parallel R_{\text{eq}})$ using the usual parallel formula and solve to obtain $R_{\text{eq}} = 3R$. <!--SR:!2026-07-02,85,363!2026-07-02,85,363-->
- network calculation example: A $5\,\textrm{V}$ source drives $30\,\Omega$ in series with parallel $40\,\Omega$ and $60\,\Omega$ branches; what are $R_{\text{eq}}$ and total current? ::@:: $R_{\parallel}=24\,\Omega$, $R_{\text{eq}}=54\,\Omega$, $I=5/54\approx0.093\,\textrm{A}$. <!--SR:!2026-04-09,19,343!2026-07-02,85,363-->
- short circuit danger ::@:: A short circuit is a near-zero-resistance path (close to zero, like through a metal wire) causing very high current and has the potential to damage components. <!--SR:!2026-04-09,19,343!2026-06-28,82,363-->

### worked calculations

- Example power dissipated by a $200\,\Omega$ resistor with $5\text{ V}$ across it: $P = V^{2}/R = 0.125\text{ W}$.
- Network example: a $10\text{ V}$ source drives a $2\,\Omega$ resistor in series with a parallel combination of a single $2\,\Omega$ branch and another branch composed of two $2\,\Omega$ resistors in series; the equivalent resistance is $R=\tfrac{10}{3}\,\Omega$ and the total current is $I=3\text{ A}$ (slide example).
- Challenging series/parallel example: a source of $5\text{ V}$ drives two equal resistors $R_S=R_L=2.4\text{ k}\Omega$; total $R=4.8\text{ k}\Omega$ giving $I=1.04\text{ mA}$, so $P_{R_L}=I^{2}R_L\approx2.6\text{ mW}$ (same result whether computed via current or halving total power).

---

Flashcards for this section are as follows:

- example power calculation: Given a $200\,\Omega$ resistor with $5\text{ V}$ across it, what power is dissipated? ::@:: Use $P=V^{2}/R$ to get $0.125\text{ W}$. <!--SR:!2026-07-02,85,363!2026-07-03,86,363-->
- parallel circuit current: Two $2\,\Omega$ resistors are in parallel with $10\,\text{V}$ applied; find the total current. ::@:: First compute $R_{\text{eq}}=(1/2+1/2)^{-1}=1\,\Omega$ then $I=V/R_{\text{eq}}=10\,\text{A}$. <!--SR:!2026-04-09,19,343!2026-07-02,85,363-->
- 10&nbsp;V series-plus-parallel network: A $10\text{ V}$ source drives a $2\,\Omega$ resistor in series with a parallel combination of a single $2\,\Omega$ branch and another branch composed of two $2\,\Omega$ resistors in series; what is the total current? ::@:: Equivalent resistance $10/3\,\Omega$ gives $I=3\text{ A}$. <!--SR:!2026-04-09,19,343!2026-07-05,88,363-->
- series/parallel power: A $5\text{ V}$ source drives two equal resistors $R_S=R_L=2.4\text{ k}\Omega$ in series; calculate the power dissipated by $R_L$. ::@:: The answer is about $2.6\text{ mW}$ (use $I=1.04\text{ mA}$, then $I^{2}R$, or halve the total power). <!--SR:!2026-04-09,19,343!2026-06-11,64,343-->
