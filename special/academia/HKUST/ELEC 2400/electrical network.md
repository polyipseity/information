---
aliases:
  - ELEC 2400 electrical network
  - ELEC2400 electrical network
  - HKUST ELEC 2400 electrical network
  - HKUST ELEC2400 electrical network
  - circuit
  - electrical circuit
  - electrical network
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2400/electrical_network
  - language/in/English
---

# electrical network

A vehicle once carried only a few essential circuits, lighting and wiping among them. Today's vehicle mixes continually evolving subsystems whose electronic and electrical components reach a hundred or more. Circuit construction moved from discrete components toward mainly integrated circuits and smaller transistors. Moore's law captures that growth. Gordon Moore, co-founder of Fairchild Semiconductor and co-founder and CEO of Intel, posited in 1965 that the number of components per integrated circuit doubles every year. In 1975, looking forward to the next decade, he revised the forecast to a doubling every two years.

A modern phone carries a large number of transducers, sensing motion, the environment, touch, light, sound, and radio. In the general electronics model an electronic circuit sits between a sensor/transducer and an actuator/transducer, exchanging electrical signals and controls with the physical world. A circuit is an interconnection of circuit elements forming a closed circuit. The simplest case is a battery driving a light bulb: the battery becomes a $9\text{ V}$ voltage source and the bulb a resistor $R$. Devices are modelled as comprising circuit elements, and circuit analysis manipulates those element models.

---

Flashcards for this section are as follows:

- overview ::@:: An electrical network, or circuit, is an interconnection of circuit elements forming a closed circuit, analysed through models of those elements. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- circuit from devices: a battery of $9\text{ V}$ drives a bulb of resistance $R$; which circuit elements model them? ::@:: The battery becomes a $9\text{ V}$ voltage source and the bulb a resistor $R$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- devices and their elements: batteries, lamps, transistors, amplifiers, and computer chips are devices; which circuit elements model them? ::@:: Voltage sources, switches, resistors, capacitors, inductors, diodes, and transistors. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- vehicle electronics: how complex are a vehicle's circuits today? ::@:: Continually evolving subsystems that often have different electronic and electrical components, sometimes 100 or more, among them microcontrollers, digital signal processors, isolators, power supply stabilization systems, and analog high-voltage chips. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- Moore's law / 1965 forecast: who posited Moore's law, and what did the 1965 forecast say about integrated circuits? ::@:: Gordon Moore, co-founder of Fairchild Semiconductor and co-founder and CEO of Intel, posited a doubling every year in the number of components per integrated circuit. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- Moore's law / 1975 revision: what did Moore revise the forecast to in 1975? ::@:: A doubling every two years, looking forward to the next decade. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- circuit construction: what replaced discrete components, and what happened to transistor size as feature sizes reached $45\text{ nm}$? ::@:: Circuits became mainly integrated circuits, and transistors grew smaller. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- transducers / motion and environment: name the phone transducers that sense motion and the environment. ::@:: Accelerometer, gyroscope, barometer, magnetometer, Hall effect sensor, thermometer, and humidity sensor. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- transducers / touch, optics, and light: name the phone transducers that handle touch, imaging, and light. ::@:: Proximity sensor, touch screen, fingerprint sensor, ambient light sensor, display, visible and infrared cameras, LED, and infrared laser. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- transducers / audio and radio: name the phone transducers that handle sound, vibration, and radio. ::@:: Microphone, speaker, vibrator, and antenna. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- general electronics model: what sits between a sensor and an actuator, and what passes between them? ::@:: An electronic circuit sits between the sensor/transducer and the actuator/transducer, exchanging electrical signals and controls with the physical world. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- input signals / mechanical, thermal, and fluid: which quantities reach the electronic circuit as mechanical, thermal, or fluid inputs? ::@:: Mechanical, thermal, pressure, humidity, weight, sound, and flow quantities. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- input signals / field and chemical: which quantities reach the electronic circuit as field or chemical inputs? ::@:: Electrical, magnetic, electromagnetic, chemical, and optical quantities. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- output actions / motion, fluid, and heat: which outputs of the electronic circuit act mechanically, fluidly, or thermally? ::@:: Motion, pneumatic action, hydraulic action, valve position, heating, and cooling. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- output signals / sound, electromagnetic, and display: which outputs of the electronic circuit are acoustic, electromagnetic, or visual? ::@:: Speaker sound, electrical, magnetic, and electromagnetic quantities, display, LED, and scanner output. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## circuit modelling

The microscopic route to element behaviour is impractical. Conduction inside a resistor is the drift of free electrons through a lattice of metal ions under an applied electric field. The Drude model describes it in far more detail than a current-voltage relation needs. The fields of a capacitor and of an inductor are governed by Maxwell's equations. Their general solution settles every such element at once, but solving them is the hard way. Each element therefore receives a compact model with a few parameters, from which the voltages and currents of the whole interconnection follow.

---

Flashcards for this section are as follows:

- overview ::@:: Each device is replaced by circuit elements with a compact set of parameters, and the voltages and currents of the whole interconnection follow from those models. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- microscopic conduction: an applied electric field acts on a conductor; which microscopic model describes the conduction? ::@:: The Drude model: free electrons drift past metal ions and exchange momentum through collisions. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- capacitor and inductor fields: what governs the fields of a capacitor and of an inductor? ::@:: Maxwell's equations; their general solution settles every such element at once, but solving them is the hard way. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- element models: once each device is replaced by circuit elements, what remains to be developed? ::@:: Models for the circuit elements themselves, such as the voltage source, the resistor, the capacitor, and the inductor. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## lumped-element model

A lumped circuit element is physically small compared with the wavelength of the signals concerned. That wavelength is $\lambda = c/f$, where $c$ is the speed of light. Every circuit component is treated as a lumped element, an assumption that stops holding for radio frequency (RF) circuits.

---

Flashcards for this section are as follows:

- overview ::@:: A lumped element is physically small compared with the signal wavelength $\lambda$, so its behaviour follows from a few idealized lumped parameters rather than from fields distributed over its body. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- wavelength: a signal has frequency $f$ and travels at the speed of light $c$; how is its wavelength written, and what does the lumped assumption compare with it? ::@:: The wavelength is $\lambda = c/f$, and a lumped element must be physically small compared with that $\lambda$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- radio frequency: which circuits break the lumped assumption? ::@:: Radio frequency (RF) circuits, where a component is no longer physically small compared with the wavelength of the signals concerned. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

### mechanical analogue

An applied force $F$ on an object of any shape is replaced by a point mass carrying one parameter, its mass $m$: the linear acceleration follows from $F = ma$. What such a model cannot tell is the effect of the object's size, shape, or point of action of the force. It also cannot tell the object's rotation or the deformation within it.

---

Flashcards for this section are as follows:

- overview ::@:: The mechanical analogue of the lumped parameter model replaces an object of any shape by a point mass carrying the single parameter $m$; an applied force $F$ then gives the linear acceleration through $F = ma$. <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what is lost / size, shape, and point of action: an object is reduced to a point mass under a force $F$; which effects of its extent disappear? ::@:: The effect of the object's size or shape, and the effect of the point of action of the force. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- what is lost / rotation and deformation: an object of finite extent is reduced to a point mass; which effects inside the body disappear? ::@:: Its rotation and its internal deformation. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

### concentrated elements

The circuit version models the circuit as an interconnection of concentrated elements such as resistors, capacitors, and inductors, joined by a network of perfectly conducting wires. Each element carries an idealized lumped parameter, such as its resistance, its capacitance, or its inductance.

---

Flashcards for this section are as follows:

- topology of the model: how is a circuit modelled in the concentrated-element picture? ::@:: As an interconnection of concentrated elements joined by a network of perfectly conducting wires. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- idealized parameters: what does each of those concentrated elements carry? ::@:: An idealized lumped parameter, such as its resistance, its capacitance, or its inductance. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## classes of electronic circuit

Analog circuits handle continuously varying quantities, digital circuits deal in 0s and 1s, and mixed-signal circuits handle both. Levels of integration run from a system-on-chip (SOC) through a chipset and a single integrated circuit (IC) to discrete and hybrid assemblies. Frequency separates low frequency (LF) from radio frequency (RF). Current, voltage, or power separates microelectronics from high voltage and high power. Operating temperature names a high-temperature class. Discrete analog circuits provide the foundation for the other types.

---

Flashcards for this section are as follows:

- overview ::@:: Electronic circuits are classed by signal type, level of integration, frequency, current, voltage, or power, and operating temperature. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- signal type: name the three signal-type classes and what each carries. ::@:: Analog circuits carry continuously varying signals, digital circuits carry 0s and 1s, and mixed-signal circuits carry both. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- levels of integration: name the levels of integration of electronic circuits. ::@:: System-on-chip (SOC), chipset, integrated circuit (IC), discrete, and hybrid. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- frequency: name the two frequency classes of electronic circuits. ::@:: Low frequency (LF) and radio frequency (RF). <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- current, voltage, or power: name the three classes set by current, voltage, or power. ::@:: Microelectronics, high voltage, and high power. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- operating temperature: which class names an operating temperature? ::@:: High temperature. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- foundation: which class of circuit provides the foundation for the other types? ::@:: Discrete analog circuits. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## terminals and ports

A circuit element has at least two external connections, called terminals. A $1.5\text{ V}$ AA battery is the simplest case, with a positive terminal and a negative terminal. Two terminals of a circuit constitute a port, either an input port or an output port. A one-port element uses the same pair of terminals as its input port and its output port. Which terminals are joined to which, and through which elements, is the circuit's [topology](circuit%20topology%20(electrical).md), read off as its nodes, branches, paths, loops, and meshes.

---

Flashcards for this section are as follows:

- overview ::@:: A circuit element has at least two external connections called terminals, and two terminals of a circuit constitute a port. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- battery terminals: a $1.5\text{ V}$ AA battery is a circuit element; which terminals does it have? ::@:: A positive terminal and a negative terminal. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- port definition ::@:: Two terminals of a circuit constitute a port, for example an input port or an output port. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- one-port element: a one-port element has the same port as its input port and its output port; what may the input and the output be? ::@:: The input may be a current, and the output is then the voltage across that same port. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

### multi-terminal elements

Some elements carry more than two terminals. An operational amplifier is a five-terminal element when its supplies are counted and a three-terminal element otherwise. With $V_{dd} = 5\text{ V}$ and $V_{ss} = 0\text{ V}$ as the supply terminals, the remaining three are the inverting input $V_-$, the non-inverting input $V_+$, and the output $V_{out}$. A MOS transistor is a four-terminal element with a gate (G), a body (B), a source (S), and a drain (D).

---

Flashcards for this section are as follows:

- operational amplifier, supplies $V_{dd} = 5\text{ V}$, $V_{ss} = 0\text{ V}$: how many terminals with the supplies counted, and how many without them? ::@:: Five terminals with $V_{dd}$ and $V_{ss}$ counted, and three terminals otherwise. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- operational amplifier terminals: an operational amplifier has supplies $V_{dd} = 5\text{ V}$ and $V_{ss} = 0\text{ V}$; name its three signal terminals. ::@:: The inverting input $V_-$, the non-inverting input $V_+$, and the output $V_{out}$. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- MOS transistor: how many terminals does a MOS transistor have, and what are they? ::@:: Four terminals: the gate (G), the body (B), the source (S), and the drain (D). <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## reference direction

A two-terminal, or one-port, circuit element is characterized by one current and one voltage. The pair marked on the diagram is the reference direction. The current enters from the positive terminal, chosen arbitrarily, and exits from the negative terminal. The voltage is measured across that same pair of positive and negative terminals. The relation between the current and the voltage is the I-V characteristic of the element.

---

Flashcards for this section are as follows:

- overview ::@:: The reference direction is the pair of a current and a voltage marked on a two-terminal element. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- the two conditions: a one-port element carries a marked current and a marked voltage; what must the current and the voltage obey? ::@:: The current enters from the arbitrarily defined positive terminal and exits from the negative terminal, and the voltage is measured across that same pair of positive and negative terminals. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- free choice of the positive terminal: which of the two terminals of a one-port element is the positive one? ::@:: Either one; the reference direction is a choice made for the analysis. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- I-V characteristic: a one-port element has one current and one voltage under its reference direction; what is the relation between them called? ::@:: The I-V characteristic, or I-V relation, of the element. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- why the marking is essential: why must the reference direction be drawn on the diagram? ::@:: Because every relation is written as though the current ran from the marked positive terminal to the marked negative one, and the marks fix the sign of the reported values for a given physical flow. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->

## passive and active elements

Passive elements only consume or store electrical energy, while active elements generate it. Read along the reference direction, that becomes a test on average power: a passive element has a non-negative average power $P_{\text{ave}} = (VI)_{\text{ave}} \ge 0$ and an active element has a negative average power $P_{\text{ave}} < 0$. Resistors, capacitors, inductors, transformers, and diodes are passive. Batteries, voltage and current sources, transistors, and op amps are active.

---

Flashcards for this section are as follows:

- overview ::@:: Passive elements only consume or store electrical energy, while active elements generate electrical energy. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- average power test: an element carries a voltage $V$ and a current $I$ along its reference direction; what does its average power $P_{\text{ave}} = (VI)_{\text{ave}}$ show for a passive element, and for an active one? ::@:: A passive element has $P_{\text{ave}} \ge 0$ and consumes or stores power; an active element has $P_{\text{ave}} < 0$ and generates it. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- passive components: which circuit elements are passive? ::@:: Resistors, capacitors, inductors, transformers, and diodes. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- active components: which circuit elements are active? ::@:: Batteries, voltage and current sources, transistors, and op amps. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
- op amp power: how does an op amp's output signal power compare with its input signal power, and where does the difference come from? ::@:: The output signal power exceeds the input signal power, and the difference comes from DC power supplies. <!--SR:!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z!fsrs,2026-11-10T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-11-02T00:00:00.000Z-->
