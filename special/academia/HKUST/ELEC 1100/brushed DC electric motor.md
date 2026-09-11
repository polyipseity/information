---
aliases:
  - DC brushed motor
  - DC brushed motors
  - brushed DC electric motor
  - brushed DC electric motors
  - brushed DC motor
  - brushed DC motors
  - brushed motor
  - brushed motors
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/brushed_DC_electric_motor
  - language/in/English
---

# brushed DC electric motor

A brushed DC electric motor is an electromechanical device that converts electrical energy into mechanical energy (rotation). It uses a mechanical commutator and carbon brushes to switch the current direction in the rotor windings so that a single DC supply can produce continuous rotation. The reverse conversion—mechanical to electrical—is a generator. For a concise treatment of the general concept see [brushed DC electric motor](../../../../general/brushed%20DC%20electric%20motor.md). This note summarises the ELEC 1100 coverage: motor definition, classification, magnetic basics, stator–rotor interaction, commutation, direction and speed control, and the link to the H-bridge and PWM.

---

Flashcards for this section are as follows:

- motor definition ::@:: Converts electrical energy into mechanical energy (rotation).
- generator ::@:: Converts mechanical energy into electrical energy; same principle, opposite energy flow.
- power equivalence ::@:: $P_{\text{elec}}=VI$; $P_{\text{mech}}=\omega\times\tau$ (speed × torque).
- ELEC 1100 motor type ::@:: Brushed DC motors in labs and the robot project.

## what are motors and classification

### what is a motor and applications

A motor is an electric–mechanical device that converts electrical power (voltage $\times$ current) into mechanical power (rotating speed $\times$ torque). Electric motors are ubiquitous: vacuum cleaners, fans, air conditioners, printers, water pumps, manufacturing, conventional and hybrid cars, and subway systems.

---

Flashcards for this section are as follows:

- motor energy conversion ::@:: Electrical power (voltage × current) → mechanical power (speed × torque). <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
- motor applications ::@:: Vacuum cleaners, fans, pumps, manufacturing, cars, subway systems, and many others.

### classification by power source

Electric motors are classified by power source: __DC motors__ are powered by direct current; __AC motors__ by alternating current. DC motors are further divided into brushed motors (commutator and brushes), brushless motors (electronic commutation), and stepper motors. AC motors include induction and synchronous types. In ELEC 1100 labs and the project we use __brushed DC motors__, which are simple to drive with an H-bridge and a single DC supply.

---

Flashcards for this section are as follows:

- power-source classification ::@:: DC motors: direct current. AC motors: alternating current.
- DC motor types ::@:: Brushed (commutator/brushes), brushless (electronic commutation), stepper.
- why brushed DC in ELEC 1100 ::@:: Simple to drive with an H-bridge and a single DC supply.

## origin and history

The first DC motor was demonstrated by Michael Faraday in 1821, one year after Hans Christian Oersted discovered electromagnetism; at that time only DC sources were available. AC motors became practical in the 1890s when AC power distribution was available; Nikola Tesla identified the principle of the rotating magnetic field, enabling industrial AC motor development.

---

Flashcards for this section are as follows:

- first DC motor ::@:: Faraday, 1821, one year after Oersted's discovery of electromagnetism.
- AC motors ::@:: Practical from the 1890s with AC power; Tesla identified the rotating magnetic field principle.

## magnetic basics

Most electric motors rely on magnetic fields.

### poles and forces

A magnet has two poles, north (N) and south (S); like poles repel and opposite poles attract. Magnetic poles always come in pairs. __Magnetic monopoles__ — isolated north or south poles with no partner — are predicted by some theories but have no experimental evidence yet; all known magnets have paired N and S poles. The __Earth's magnetic field__ behaves as if a giant bar magnet lay inside the planet: the _magnetic_ south pole of that equivalent magnet sits near Earth's _geographic_ north pole (and vice versa), which is why a compass needle (N-seeking) points toward geographic north.

---

Flashcards for this section are as follows:

- magnet poles ::@:: North and south; like poles repel, opposite poles attract.
- magnetic monopoles ::@:: Isolated N or S poles with no partner; predicted by some theories but no experimental evidence.
- Earth's magnetic field ::@:: Like a giant bar magnet inside the planet; the magnetic south is near geographic north, so a compass (N-seeking) points north.

### permanent magnet

A __permanent magnet__ has fixed N and S positions and produces a magnetic field from N to S; it is effectively always "on" and cannot be turned off.

---

Flashcards for this section are as follows:

- permanent magnet ::@:: Fixed N and S poles with a field from N to S; cannot be turned off.

### electromagnet and right-hand rule

An __electromagnet__ is made by passing current through a wire (often wound as a solenoid). The direction of current determines which end is N and which is S; the poles reverse if the current direction is reversed. The direction of the magnetic field around a current-carrying wire can be found using the __right-hand rule__. __Applying the right-hand rule:__ for a straight wire, point your right thumb in the direction of conventional current; your fingers curl in the direction of the magnetic field around the wire. For a solenoid, grip the coil with your right hand so your fingers follow the current direction along the turns; your thumb then points toward the north pole of the electromagnet. Electromagnets can be turned on or off and their polarity reversed by changing the current, which is essential for motor control.

---

Flashcards for this section are as follows:

- electromagnet ::@:: N/S poles set by current direction; can be turned on/off and polarity reversed.
- right-hand rule purpose ::@:: Find the magnetic field direction around a current-carrying wire or solenoid.
- right-hand rule (straight wire) ::@:: Thumb in current direction; fingers curl in the magnetic field direction.
- right-hand rule (solenoid) ::@:: Fingers follow current along turns; thumb points toward the north pole.

## stator and rotor interaction

### stator and rotor roles

An electric motor operates through the interaction of the magnetic fields of a __stator__ (fixed part) and a __rotor__ (moving part). In a simple brushed DC motor the stator may be a permanent magnet and the rotor an electromagnet (solenoid).

---

Flashcards for this section are as follows:

- stator and rotor ::@:: Stator = fixed part; rotor = moving part.

### attraction, repulsion, and continuous rotation

When power is applied, current in the rotor creates a magnetic field; the rotor's N and S poles are attracted to the opposite poles of the stator and repelled by the like poles, so the rotor turns until opposite poles align. Because of inertia the rotor overshoots; if we then __reverse the current__ in the rotor, its N and S poles flip, and the forces again push it in the same rotational direction. Repeating this polarity reversal keeps the rotor spinning in one direction; the mechanical commutator and brushes perform this reversal automatically when the motor is driven by a DC source.

---

Flashcards for this section are as follows:

- why rotor turns ::@:: Rotor and stator fields interact; opposite poles attract, like poles repel, producing torque.
- why reverse rotor polarity ::@:: After overshoot (inertia), reversing polarity keeps torque in the same direction.
- inertia role ::@:: Rotor overshoots the aligned position; polarity reversal keeps it spinning.

## commutation and brushed construction

### commutation and the commutator and brushes

The switching of the magnetic field in the rotor (reversing current direction) is called __commutation__. A DC source cannot by itself reverse the current in the rotor. In a __brushed DC motor__ this is done mechanically: a __commutator__ (e.g. a copper sleeve split into segments) rotates with the rotor, and __carbon brushes__ (fixed) slide on the commutator and make contact with different segments. As the rotor turns, the brushes contact different segments so that the current through the rotor windings is effectively reversed at the right moments, keeping rotation in one direction. The DC current from the supply is in one direction at the brushes, but inside the motor the commutator and brushes perform the switching needed for continuous rotation.

---

Flashcards for this section are as follows:

- commutation ::@:: Switching the rotor's magnetic field by reversing current direction at the right moments.
- why mechanical commutation ::@:: A DC source provides current in one direction; the commutator and brushes switch which rotor segments see which polarity.
- commutator and brushes ::@:: Commutator: rotating copper sleeve with segments. Brushes: fixed carbon contacts that slide on the commutator.
- current path ::@:: At the brushes, DC current is one direction; the commutator switches segments so rotor winding current reverses as it rotates.

## direction control with H-bridge

To change the rotation direction of a brushed DC motor we change the direction of current through the motor: reversing the applied voltage (or swapping which terminal is positive and which is negative) reverses the current and thus the direction of the magnetic field in the rotor. An [H-bridge](H-bridge.md) does this electronically: a single direction (DIR) signal ($5\text{ V}$ or $0\text{ V}$), often with an inverter to obtain the complementary logic levels, drives the four transistors so that one diagonal pair is on for one direction and the other diagonal for the opposite direction. Clockwise with one polarity, anti-clockwise with the other; the H-bridge is the standard way to achieve reversible motor control from one supply in the course.

---

Flashcards for this section are as follows:

- reversing motor direction ::@:: Reverse the current direction (voltage polarity); the rotor field opposes the stator in the opposite sense.
- H-bridge direction control ::@:: Reverses voltage across the motor by closing one diagonal pair for one direction, the other for the opposite.
- DIR signal ::@:: Selects which H-bridge diagonal is on, controlling current direction and thus rotation direction.

## speed control and limitations of variable resistor

### factors affecting speed

Besides direction, we need to control __motor speed__. Speed can be influenced by the strength of the magnetic field: more coils in the solenoid or a higher voltage (larger current) generally give higher speed. In a built motor the number of coils is fixed, so speed control is usually done by changing the __voltage__ (and thus current) supplied to the motor.

---

Flashcards for this section are as follows:

- speed factors ::@:: Magnetic field strength (more coils or higher voltage/current → higher speed).
- why voltage for speed control ::@:: Coil count is fixed in a built motor; changing supply voltage is the practical way to vary speed.

### variable resistor, drawbacks, and PWM

One simple method is a __variable resistor__ in series with the motor: reducing the resistor increases the voltage across the motor and speeds it up. This approach has drawbacks: it is __inefficient__ (energy dissipated as heat in the resistor, especially at low speeds), __imprecise__, and requires mechanical adjustment, so it is not computer-friendly. The course uses __pulse-width modulation (PWM)__ for efficient, precise, and software-controllable speed control, covered in the next lecture.

---

Flashcards for this section are as follows:

- variable resistor effect ::@:: Smaller resistor → more voltage across motor → faster. Larger resistor → slower.
- variable resistor drawbacks ::@:: Inefficient (heat waste at low speeds), imprecise, requires mechanical adjustment.
- PWM ::@:: Used in the course for efficient, precise, software-controllable speed control.
