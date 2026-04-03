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

- motor definition: What does a motor do? ::@:: A motor converts electrical energy into mechanical energy (e.g. rotation). <!--SR:!2026-06-07,63,310!2026-04-06,16,290-->
- generator vs motor: What is the reverse of a motor? ::@:: A generator converts mechanical energy into electrical energy; same device principle, opposite energy flow. <!--SR:!2026-04-06,16,290!2026-04-06,16,290-->
- power equivalence: Electrical power is voltage $\times$ current; mechanical power is rotating speed $\times$ torque. ::@:: $P_{\text{elec}}=VI$; $P_{\text{mech}}=\omega\times\tau$ (speed $\times$ torque) for rotational output. <!--SR:!2026-05-29,55,310!2026-04-06,16,290-->
- brushed DC motor in ELEC 1100: Which motor type is used in labs and project? ::@:: Brushed DC motors are used in ELEC 1100 labs and the robot project. <!--SR:!2026-06-04,60,310!2026-05-30,56,310-->

## what are motors and classification

### what is a motor and applications

A motor is an electric–mechanical device that converts electrical power (voltage $\times$ current) into mechanical power (rotating speed $\times$ torque). Electric motors are ubiquitous: vacuum cleaners, fans, air conditioners, printers, water pumps, manufacturing, conventional and hybrid cars, and subway systems.

---

Flashcards for this section are as follows:

- motor definition (classification section): What is a motor in terms of energy conversion? ::@:: A motor converts electrical power (voltage $\times$ current) into mechanical power (rotating speed $\times$ torque). <!-- check: ignore-line[two_sided_calc_warning]: conceptual --> <!--SR:!2026-04-06,16,290!2026-04-06,16,290-->
- motor applications: Where are electric motors used? ::@:: Vacuum cleaners, fans, air conditioners, printers, water pumps, manufacturing, cars (conventional and hybrid), subway systems, and many other applications. <!--SR:!2026-06-03,59,310!2026-05-31,57,310-->

### classification by power source

Electric motors are classified by power source: **DC motors** are powered by direct current; **AC motors** by alternating current. DC motors are further divided into brushed motors (commutator and brushes), brushless motors (electronic commutation), and stepper motors. AC motors include induction and synchronous types. In ELEC 1100 labs and the project we use **brushed DC motors**, which are simple to drive with an H-bridge and a single DC supply.

---

Flashcards for this section are as follows:

- classification by power source: How are motors classified by power source? ::@:: DC motors use direct current; AC motors use alternating current. <!--SR:!2026-05-28,54,310!2026-04-06,16,290-->
- DC motor types: What are the main DC motor types? ::@:: Brushed (commutator and brushes), brushless (electronic commutation), and stepper motors. <!--SR:!2026-06-07,63,310!2026-06-03,59,310-->
- ELEC 1100 motor choice: Why use brushed DC motors in the course? ::@:: Brushed DC motors are straightforward to drive with an H-bridge and a single DC supply; they are used in labs and the robot project. <!--SR:!2026-05-30,56,310!2026-04-06,16,290-->

## origin and history

The first DC motor was demonstrated by Michael Faraday in 1821, one year after Hans Christian Oersted discovered electromagnetism; at that time only DC sources were available. AC motors became practical in the 1890s when AC power distribution was available; Nikola Tesla identified the principle of the rotating magnetic field, enabling industrial AC motor development.

---

Flashcards for this section are as follows:

- Faraday DC motor: When and by whom was the first DC motor demonstrated? ::@:: Michael Faraday demonstrated the first DC motor in 1821, one year after Oersted's discovery of electromagnetism. <!--SR:!2026-04-06,16,290!2026-04-06,16,290-->
- AC motors and Tesla: When did AC motors become practical and who is associated with their principle? ::@:: AC motors became practical in the 1890s with AC power; Nikola Tesla identified the principle of the rotating magnetic field for AC motors. <!--SR:!2026-06-01,58,310!2026-06-06,62,310-->

## magnetic basics

Most electric motors rely on magnetic fields.

### poles and forces

A magnet has two poles, north (N) and south (S); like poles repel and opposite poles attract. Magnetic poles always come in pairs. **Magnetic monopoles** — isolated north or south poles with no partner — are predicted by some theories but have no experimental evidence yet; all known magnets have paired N and S poles. The **Earth's magnetic field** behaves as if a giant bar magnet lay inside the planet: the *magnetic* south pole of that equivalent magnet sits near Earth's *geographic* north pole (and vice versa), which is why a compass needle (N-seeking) points toward geographic north.

---

Flashcards for this section are as follows:

- magnet poles: What are the two poles of a magnet and how do they interact? ::@:: North and south; like poles repel, opposite poles attract. <!--SR:!2026-06-01,58,310!2026-05-31,57,310-->
- magnetic monopoles: Do magnetic monopoles exist and what are they? ::@:: Magnetic monopoles are isolated N or S poles with no partner; they are predicted by some theories but have no experimental evidence; all known magnets have paired poles. <!--SR:!2026-06-03,59,310!2026-06-01,58,310-->
- Earth's magnetic field: How is Earth's field described and where are its poles? ::@:: Earth's field is like a giant bar magnet inside the planet; the magnetic south pole of that equivalent magnet is near geographic north, and the magnetic north pole near geographic south, so a compass (N-seeking) points toward geographic north. <!--SR:!2026-05-29,55,310!2026-05-28,54,310-->

### permanent magnet

A **permanent magnet** has fixed N and S positions and produces a magnetic field from N to S; it is effectively always "on" and cannot be turned off.

---

Flashcards for this section are as follows:

- permanent magnet: What is a permanent magnet and can it be turned off? ::@:: A permanent magnet has fixed N and S poles and a fixed field from N to S; it cannot be turned off. <!--SR:!2026-05-30,56,310!2026-06-05,61,310-->

### electromagnet and right-hand rule

An **electromagnet** is made by passing current through a wire (often wound as a solenoid). The direction of current determines which end is N and which is S; the poles reverse if the current direction is reversed. The direction of the magnetic field around a current-carrying wire can be found using the **right-hand rule**. **Applying the right-hand rule:** for a straight wire, point your right thumb in the direction of conventional current; your fingers curl in the direction of the magnetic field around the wire. For a solenoid, grip the coil with your right hand so your fingers follow the current direction along the turns; your thumb then points toward the north pole of the electromagnet. Electromagnets can be turned on or off and their polarity reversed by changing the current, which is essential for motor control.

---

Flashcards for this section are as follows:

- electromagnet: How does an electromagnet differ from a permanent magnet? ::@:: An electromagnet's N/S poles are set by the direction of current through the wire; it can be turned on/off and its polarity reversed by changing the current. <!--SR:!2026-04-06,16,290!2026-06-06,62,310-->
- right-hand rule: What is the right-hand rule used for in motor context? ::@:: To find the direction of the magnetic field produced by a current-carrying wire (or solenoid). <!--SR:!2026-06-06,62,310!2026-06-01,58,310-->
- applying the right-hand rule (straight wire): How do you use the right-hand rule for a straight current-carrying wire? ::@:: Point the right thumb in the direction of conventional current; the fingers curl in the direction of the magnetic field around the wire. <!--SR:!2026-06-05,61,310!2026-06-06,62,310-->
- applying the right-hand rule (solenoid): How do you use the right-hand rule for a solenoid to find which end is north? ::@:: Grip the coil with the right hand so the fingers follow the current direction along the turns; the thumb points toward the north pole of the electromagnet. <!--SR:!2026-06-04,60,310!2026-05-28,54,310-->

## stator and rotor interaction

### stator and rotor roles

An electric motor operates through the interaction of the magnetic fields of a **stator** (fixed part) and a **rotor** (moving part). In a simple brushed DC motor the stator may be a permanent magnet and the rotor an electromagnet (solenoid).

---

Flashcards for this section are as follows:

- stator and rotor: What are the stator and rotor in a motor? ::@:: The stator is the fixed part; the rotor is the part that moves (rotates). <!--SR:!2026-06-03,59,310!2026-04-06,16,290-->

### attraction, repulsion, and continuous rotation

When power is applied, current in the rotor creates a magnetic field; the rotor's N and S poles are attracted to the opposite poles of the stator and repelled by the like poles, so the rotor turns until opposite poles align. Because of inertia the rotor overshoots; if we then **reverse the current** in the rotor, its N and S poles flip, and the forces again push it in the same rotational direction. Repeating this polarity reversal keeps the rotor spinning in one direction; the mechanical commutator and brushes perform this reversal automatically when the motor is driven by a DC source.

---

Flashcards for this section are as follows:

- why rotor turns: Why does the rotor rotate when power is applied? ::@:: The rotor's magnetic field interacts with the stator's; opposite poles attract and like poles repel, producing a torque that rotates the rotor. <!--SR:!2026-06-07,63,310!2026-06-07,63,310-->
- reversing rotor polarity: Why do we reverse the current (and thus polarity) in the rotor? ::@:: After the rotor overshoots (due to inertia), reversing the rotor's polarity keeps the torque in the same rotational direction so the motor continues spinning. <!--SR:!2026-06-05,61,310!2026-04-06,16,290-->
- inertia in motor: What role does inertia play in a simple motor? ::@:: The rotor overshoots the aligned position; then reversing the rotor's magnetic polarity keeps it spinning in the same direction. <!--SR:!2026-05-28,54,310!2026-04-06,16,290-->

## commutation and brushed construction

### commutation and the commutator and brushes

The switching of the magnetic field in the rotor (reversing current direction) is called **commutation**. A DC source cannot by itself reverse the current in the rotor. In a **brushed DC motor** this is done mechanically: a **commutator** (e.g. a copper sleeve split into segments) rotates with the rotor, and **carbon brushes** (fixed) slide on the commutator and make contact with different segments. As the rotor turns, the brushes contact different segments so that the current through the rotor windings is effectively reversed at the right moments, keeping rotation in one direction. The DC current from the supply is in one direction at the brushes, but inside the motor the commutator and brushes perform the switching needed for continuous rotation.

---

Flashcards for this section are as follows:

- commutation definition: What is commutation in a DC motor? ::@:: Commutation is the switching of the magnetic field in the rotor by reversing the current direction in the rotor windings at the right moments. <!--SR:!2026-04-06,16,290!2026-04-06,16,290-->
- why mechanical commutation: Why can't a DC source alone reverse the rotor current? ::@:: A DC source provides current in one direction; we need a mechanism (commutator and brushes) to switch which part of the rotor sees which polarity so the rotor keeps turning. <!--SR:!2026-05-31,57,310!2026-06-06,62,310-->
- commutator and brushes: What are the commutator and brushes in a brushed motor? ::@:: The commutator is a rotating part (e.g. copper sleeve with segments) that rotates with the rotor; the brushes are fixed carbon contacts that slide on the commutator and connect the supply to different segments as the rotor turns. <!--SR:!2026-05-29,55,310!2026-05-29,55,310-->
- brushed motor current path: Where is the current from the DC supply in one direction, and where is it switched? ::@:: At the brushes the current from the DC source is in one direction; the commutator and brushes switch which rotor segments are connected so that the effective current in the rotor windings reverses as it rotates. <!--SR:!2026-05-20,45,290!2026-04-06,16,290-->

## direction control with H-bridge

To change the rotation direction of a brushed DC motor we change the direction of current through the motor: reversing the applied voltage (or swapping which terminal is positive and which is negative) reverses the current and thus the direction of the magnetic field in the rotor. An [H-bridge](H-bridge.md) does this electronically: a single direction (DIR) signal ($5\text{ V}$ or $0\text{ V}$), often with an inverter to obtain the complementary logic levels, drives the four transistors so that one diagonal pair is on for one direction and the other diagonal for the opposite direction. Clockwise with one polarity, anti-clockwise with the other; the H-bridge is the standard way to achieve reversible motor control from one supply in the course.

---

Flashcards for this section are as follows:

- how to reverse motor direction: How do we change the rotation direction of a brushed DC motor? ::@:: Change the direction of current through the motor (reverse the applied voltage polarity); the rotor's magnetic field then opposes the stator in the opposite sense, so the motor reverses. <!--SR:!2026-04-06,16,290!2026-05-30,56,310-->
- H-bridge and direction: How does the H-bridge change motor direction? ::@:: The H-bridge reverses the voltage (and current) across the motor by closing one diagonal pair of switches for one direction and the other diagonal for the opposite direction. <!--SR:!2026-06-07,63,310!2026-06-04,60,310-->
- DIR signal: What does the DIR signal (e.g. $5\text{ V}$ or $0\text{ V}$) control in the H-bridge motor circuit? ::@:: DIR selects which diagonal of the H-bridge is on, hence the direction of current through the motor and thus the rotation direction (clockwise or anti-clockwise). <!--SR:!2026-06-01,58,310!2026-05-28,54,310-->

## speed control and limitations of variable resistor

### factors affecting speed

Besides direction, we need to control **motor speed**. Speed can be influenced by the strength of the magnetic field: more coils in the solenoid or a higher voltage (larger current) generally give higher speed. In a built motor the number of coils is fixed, so speed control is usually done by changing the **voltage** (and thus current) supplied to the motor.

---

Flashcards for this section are as follows:

- how to control motor speed: What two factors affect motor speed in principle? ::@:: Strength of the magnetic field: more coils or higher voltage (larger current) generally give higher speed. <!--SR:!2026-06-04,60,310!2026-05-31,57,310-->
- why control voltage for speed: Why is motor speed usually controlled by changing voltage? ::@:: The number of coils in a built motor is fixed; changing the supply voltage (and thus current) is the practical way to vary speed. <!--SR:!2026-06-05,61,310!2026-04-06,16,290-->

### variable resistor, drawbacks, and PWM

One simple method is a **variable resistor** in series with the motor: reducing the resistor increases the voltage across the motor and speeds it up. This approach has drawbacks: it is **inefficient** (energy dissipated as heat in the resistor, especially at low speeds), **imprecise**, and requires mechanical adjustment, so it is not computer-friendly. The course uses **pulse-width modulation (PWM)** for efficient, precise, and software-controllable speed control, covered in the next lecture.

---

Flashcards for this section are as follows:

- variable resistor for speed: How does a variable resistor in series with the motor affect speed? ::@:: A smaller series resistor leaves more voltage across the motor, so current and speed increase; a larger resistor reduces voltage across the motor and slows it down. <!--SR:!2026-04-06,16,290!2026-05-29,55,310-->
- disadvantages of variable resistor speed control: What are the drawbacks of using a variable resistor for motor speed control? ::@:: Inefficient (energy wasted as heat in the resistor, especially at low speeds); difficult to control precisely; requires mechanical adjustment, not computer-friendly. <!--SR:!2026-06-05,61,310!2026-05-30,56,310-->
- next topic (PWM): What is used in the course for efficient motor speed control? ::@:: Pulse-width modulation (PWM), covered in the next lecture; it is efficient, precise, and software-controllable. <!--SR:!2026-04-06,16,290!2026-05-19,44,290-->
