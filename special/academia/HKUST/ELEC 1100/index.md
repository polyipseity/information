---
aliases:
  - ELEC 1100
  - ELEC 1100 index
  - HKUST ELEC 1100
  - HKUST ELEC 1100 index
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/index
  - function/index
  - language/in/English
---

# index

- HKUST ELEC 1100
- name: Introduction to Electro-Robot Design
- credits: 4

---

ELEC1100 is designed to provide the fundamental knowledge in electrical engineering, basic electronic components and skills needed for the design, implementation and evaluation of a robot and its subsystems. It covers the basic electronic engineering principles and techniques. Hands-on laboratory sessions, complemented with lectures and tutorials, are provided to allow students to have a systematic view of the electronic engineering principles. Students apply the knowledge and principles learnt to design and build a functional robot by themselves.

- For any grading components, late submission will NOT be accepted.
- Make-up sessions and special accommodations are handled by the instructor or IA; consult the official syllabus or LMS for contact details rather than embedding names or email addresses in the note.  Submit proof of absence within one week to arrange a make-up session.  Medical accommodations require a hard copy of the original certificate.

The content is in teaching order.

## logistics

- grading
  - labs ×6: 29%; first 5 labs 5% each, final lab 4%
  - quizzes ×8: 3%; pop‑up in‑tutorial open book; to earn full 3% answer at least 6 questions correctly (each worth 0.5 points)
  - lab exam: 20%; close book
  - written exam: 25%; close book
  - project demo: 20%
  - project report: 3%
- sections:
  - lecture: L1
    - L1: CYT-LTL; MondayT16:00:00/MondayT16:50:00,FridayT11:30:00/FridayT12:20:00
  - tutorials: T2
    - T1: CYT-G001; FridayT10:30:00/FridayT11:20:00
    - T2: CYT-G001; MondayT14:30:00/MondayT15:20:00
    - T3: LG3009; ThursdayT16:30:00/ThursdayT17:20:00
  - labs: LA3
    - LA1: Room 2133 & 2134, Academic Building; TuesdayT13:30:00/TuesdayT16:20:00
    - LA2: Room 2133 & 2134, Academic Building; FridayT13:30:00/FridayT16:20:00
    - LA3: Room 2133 & 2134, Academic Building; MondayT10:30:00/MondayT13:20:00

<!-- The source timetable contained a duplicated week‑9 row: the first instance covers **30 Mar 2026 – 03 Apr 2026** (lab exam, tutorial, lecture plus the public holiday on 3 Apr).  A second copy of week‑9 appeared for **06 Apr 2026 – 10 Apr 2026** (three consecutive public holidays followed by the final project lecture).  We treat the latter region as *week 10* and renumber all subsequent weeks accordingly.  Holiday days are represented as public‑holiday sessions with status `public holiday` so they remain visible without inflating the lecture count. -->

## children

- [assignments/](assignments/index.md)
- [attachments/](attachments/index.md)
- [labs/](labs/index.md)
- [questions/](questions/index.md)
- [tutorials/](tutorials/index.md)
- [diode](diode.md)
- [electronic component](electronic%20component.md)
- [Kirchhoff's circuit laws](Kirchhoff%27s%20circuit%20laws.md)
- [transistor](transistor.md)
- [voltage regulator](voltage%20regulator.md)

## assignments

- assignment 1
  - due: 2025-09-??
  - points: ?
  - link: [assignment 1](assignments/assignment%201/index.md)

### week 1 lab 1

- datetime: 2026-02-02T10:30:00+08:00/2026-02-02T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- status: no lab

### week 1 tutorial 1

- datetime: 2026-02-02T14:30:00+08:00/2026-02-02T15:20:00+08:00, PT50M
- venue: CYT-G001
- status: no tutorial

### week 1 lecture 1

- datetime: 2026-02-02T16:00:00+08:00/2026-02-02T16:50:00+08:00, PT50M
- venue: CYT-LTL
- status: scheduled
- topic: course introduction
- ELEC 1100
  - ELEC 1100 / course overview
    - ELEC 1100 / course overview / description ::@:: Designed to provide fundamental knowledge in electrical engineering, basic electronic components and robot design
    - ELEC 1100 / course overview / outcomes ::@:: Analyze and design simple analog circuits; implement control strategies; build/debug systems using hierarchical design; manage projects; execute full project lifecycle
  - ELEC 1100 / pedagogy
    - ELEC 1100 / pedagogy / methodology ::@:: Reverse engineering approach: start with engineering, then physics, then mathematics; emphasizes learning by doing
    - ELEC 1100 / pedagogy / traditional approach ::@:: Traditional: mathematics ➜ physics ➜ engineering; may tell you and you forget, teach you and you remember
    - ELEC 1100 / pedagogy / reverse approach details ::@:: Reverse engineering: engineering ➜ physics ➜ mathematics; many things can be learned but not taught; learning requires an objective usually from needs and experience; involve me and I learn
    - ELEC 1100 / pedagogy / traditional limitations ::@:: Traditional education teaches knowledge that may become obsolete and does not focus on application; may not evolve with information era; knowledge may be forgotten or redundant after graduation
    - ELEC 1100 / pedagogy / retention question ::@:: One month after taking a class, how much material can you still recall?
  - ELEC 1100 / class expectation ::@:: Attend lectures, tutorials and labs on time; be ready to learn, ask questions and enjoy the experience
  - ELEC 1100 / what is this class about? ::@:: Not a LEGO robot programming class; start from basic concepts and construct robot from basic components; learn managing power supply, driving motors, reading sensor output, logic control and decision making; will construct autonomous “robot” to finish a task
  - ELEC 1100 / what is a robot?
    - ELEC 1100 / what is a robot? / history ::@:: Word “robot” first used in 1921 by Czech playwright Karel Capek; “robotic” appeared in Issac Asimov’s 1942 story – these predate modern computers, ICs, transistors, and AI
    - ELEC 1100 / what is a robot? / laws ::@:: Asimov’s Three Laws of Robotics (1950): 1) A robot may not injure a human or through inaction allow harm. 2) A robot must obey human orders unless they conflict with Law 1. 3) A robot must protect its own existence unless such protection conflicts with Law 1 or 2
    - ELEC 1100 / what is a robot? / definitions ::@:: Robot Institute of America definition: a reprogrammable, multifunctional manipulator designed to move material, parts, tools, or specialised devices through various programmed motions for the performance of a variety of tasks; Webster definition: “an automatic device that performs functions normally ascribed to humans or a machine in the form of a human.”
    - ELEC 1100 / what is a robot? / features ::@:: - artificially created and programmable <br/>  - can sense its environment and manipulate or interact with things in it <br/>  - has some ability to make choices based on the environment, often using automatic control or a preprogrammed sequence <br/>  - moves without direct human interaction <br/>  - discussion questions: are animals robots? is a motorcycle a robot? is a helicopter a robot?
    - ELEC 1100 / what is a robot? / examples ::@:: - First real robot Unimate (Engelberger & Devol, 1961) – development began 1954 inspired by Asimov <br/>  - Modern robots: Boston Dynamics dancing robots; Roomba vacuum cleaner; Aqua 2 underwater robot; DJI Air 2S drone <br/>  - Categories: aerospace, consumer, exoskeletons, drones, self-driving cars, industrial, disaster response, humanoids
  - ELEC 1100 / robotics discipline ::@:: Science of perceiving and manipulating the physical world through computer-controlled mechanical devices; interdisciplinary branch of computer science and engineering involving design, construction, operation, and use of robots to help and assist humans
  - ELEC 1100 / human vs robot analogy ::@:: Compare sensing, structure, motion, fuel, control and communication between humans and robots
  - ELEC 1100 / mobile robot components ::@:: Sensing: vision, sonar, GPS, gyro compass; Controller: signal processing, memory map, planned motion command, control algorithm; Power: DC for analog/digital circuits, solar/portable sources; Mechanical motion: wheels, axles, structures
  - ELEC 1100 / design principles
    - ELEC 1100 / design principles / hierarchical decomposition ::@:: Divide-and-conquer decomposition into subsystems such as power, sensors, controller, mechanical; complex systems like a Mars rover use specialised subteams (control, communication, signal processing, mechanical, rocket, etc.) each handling tasks (e.g. control team: obstacle avoidance, speed/landing control)
  - ELEC 1100 / robot system structure ::@:: Robot system accepts inputs and produces actions; electronic and mechanical subsystems feed into the overall system with further sub‑subsystems
    - ELEC 1100 / robot system structure / electronic decomposition ::@:: Electronic subsystem breaks into control processor (sensor/other input, memory, logic power supply, control logic), motor drive and motor power supply with power amplifier; outputs to mechanical subsystem; mobile robot components include sensing (vision, sonar, GPS, gyro), controller, power sources, mechanical motion elements
  - ELEC 1100 / course roadmap ::@:: Weekly topics from basic electronics through Arduino programming and final project (sensor basics wk6; logic & MCU wk7‑9; motor power/transistor/H‑bridge/ PWM wk4‑6; basic electronics and KCL/KVL early weeks)
  - ELEC 1100 / references ::@:: - No major text; mainly use handouts provided by the instructors <br/>  - Major references: L. Richard Carley and Pradeep Khosla, “Introduction to Electrical and Computer Engineering- taught in Context”, The McGraw-Hill Companies, Inc. <br/>  - G. Rizzoni, “Principles and Applications of Electrical Engineering,” 5th edition, McGraw Hill, 2007 <br/>  - D. V. Kerns and J.D. Irwin, “Essentials of Electrical and Computer Engineering”, Pearson, 2004 <br/>  - M. M. Mano and C.R. Kime, “Logic and Computer Design fundamentals”, 3rd edition, Prentice-Hall, 2004

---

During the first lecture the instructor went over {@{the course logistics}@}.  You should regularly check {@{the Canvas home page and syllabus}@} for {@{the complete schedule and any exam announcements}@} and monitor your HKUST email account for updates; {@{next week the tutorials}@} start on 2026‑02‑09, 2026‑02‑12, and 2026‑02‑13 and {@{the first lab sessions}@} begin on 2026‑02‑13, so be prepared for Lab #1.  The teaching team consists of the {@{course instructor supported by an instructional assistant and a technical officer}@}.  Grading is weighted as follows: {@{six labs totalling 29%, eight pop‑up quizzes worth up to 3%, a closed‑book lab exam 20%, a closed‑book written exam 25%, a project demo 20%, and a short project report 3%}@}.  {@{Late work}@} is not accepted; if you {@{miss a submission for a legitimate reason}@} you must {@{contact the IA within one week and provide documentation}@} to arrange a make‑up.  Finally, all students are expected to observe {@{the HKUST academic honour code}@} – {@{violations such as plagiarism}@} may result in {@{failing the course}@}.  The next lecture will cover {@{basic components and charge/current/voltage/resistor}@}.

### week 1 lecture 2

- datetime: 2026-02-06T11:30:00+08:00/2026-02-06T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: basic components
- ELEC 1100
  - ELEC 1100 / ECE areas relevant to robotics ::@:: Robotics draws on multiple ECE subfields grouped by function: **hardware** (nanoelectronics for core devices; MEMS for micro‑robots and sensors; photonics for optical sensors), **computation & control** (integrated circuits & systems and system automation for control algorithms; multimedia & signal processing for information processing; computer engineering for decision‑making) and **communications** (wireless communication and networking for robot links).
  - ELEC 1100 / [electronic component](electronic%20component.md#electrical%20fundamentals)
    - [§ electricity](electronic%20component.md#electricity)
    - [§ atoms and charge](electronic%20component.md#atoms%20and%20charge)
    - [§ conductors and insulators](electronic%20component.md#conductors%20and%20insulators)
    - [§ current](electronic%20component.md#current)
    - [§ voltage and potential difference](electronic%20component.md#voltage%20and%20potential%20difference)
    - [§ resistance and resistors](electronic%20component.md#resistance%20and%20resistors)
    - [§ capacitors](electronic%20component.md#capacitors)
    - [§ capacitor actions](electronic%20component.md#capacitor%20actions)

### week 2 lab 1

- datetime: 2026-02-09T10:30:00+08:00/2026-02-09T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- status: no lab

### week 2 tutorial 1

- datetime: 2026-02-09T14:30:00+08:00/2026-02-09T15:20:00+08:00, PT50M
- venue: CYT-G001
- topic: prepare for lab 1

### week 2 lecture 1

- datetime: 2026-02-09T16:00:00+08:00/2026-02-09T16:50:00+08:00, PT50M
- venue: CYT-LTL
- status: scheduled
- topic: basic electronics review, energy & power, resistor networks
- ELEC 1100
  - ELEC 1100 / [electronic component](electronic%20component.md#electrical%20fundamentals)
    - [§ electrical fundamentals](electronic%20component.md#electrical%20fundamentals)
    - [§ atoms and charge](electronic%20component.md#atoms%20and%20charge) ::@:: outer electrons are weakly held and participate in conduction
    - [§ conductors and insulators](electronic%20component.md#conductors%20and%20insulators) ::@:: conductors allow easy charge flow, insulators restrict it
    - [§ current](electronic%20component.md#current) ::@:: current $I=\Delta q/\Delta t$ and conventional direction <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
    - [§ voltage and potential difference](electronic%20component.md#voltage%20and%20potential%20difference) ::@:: voltage is energy per charge between two points
    - [§ resistance and resistors](electronic%20component.md#resistance%20and%20resistors) ::@:: Ohm's law $V=IR$, resistivity formula $R=\rho L/A$ <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
    - [§ capacitors](electronic%20component.md#capacitors) ::@:: two plates store charge, discharge provides transient power
    - [§ energy and power](electronic%20component.md#energy%20and%20power) ::@:: $E=qV$, $P=IV=I^{2}R=V^{2}/R$ <p> Human/robot energy analogy; DC vs AC sources; lab gear (bench supply, function generator, breadboard, battery monitor, LiPo); human body energy comparison; Galileo $v=\sqrt{2gh}$; resistor heating/short‑circuit hazard and worked numerical examples. <!-- check: ignore-line[two_sided_calc_warning]: conceptual -->
    - [§ resistor networks](electronic%20component.md#resistor%20networks) ::@:: series add, parallel combine via reciprocal conductance

### week 2 lecture 2

- datetime: 2026-02-13T11:30:00+08:00/2026-02-13T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: KCL & KVL
- ELEC 1100
  - ELEC 1100 / [Kirchhoff's circuit laws](Kirchhoff%27s%20circuit%20laws.md) ::@:: Two fundamental relations (KCL and KVL)
    - [§ background](Kirchhoff%27s%20circuit%20laws.md#background) ::@:: Series/parallel formulas motivate the need for general laws
    - [§ Kirchhoff's current law](Kirchhoff%27s%20circuit%20laws.md#kirchhoff%27s%20current%20law) ::@:: Sum of currents entering a node equals sum leaving it
    - [§ Kirchhoff's voltage law](Kirchhoff%27s%20circuit%20laws.md#kirchhoff%27s%20voltage%20law) ::@:: Sum of voltage drops around a closed loop equals zero
    - [§ circuit analysis using Kirchhoff's laws](Kirchhoff%27s%20circuit%20laws.md#circuit%20analysis%20using%20kirchhoff%27s%20laws) ::@:: Procedure combining KCL and KVL to solve networks
    - [§ integrated numerical calculations](Kirchhoff%27s%20circuit%20laws.md#integrated%20numerical%20calculations) ::@:: Worked calculations using KCL and KVL for simple and bridge circuits
    - [§ equivalence and application](Kirchhoff%27s%20circuit%20laws.md#equivalence%20and%20application) ::@:: When to apply KCL and KVL laws and how to compute equivalent resistance

### week 3 lab 1

- datetime: 2026-02-16T10:30:00+08:00/2026-02-16T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- status: no lab

### week 3 tutorial 1

- datetime: 2026-02-16T14:30:00+08:00/2026-02-16T15:20:00+08:00, PT50M
- venue: CYT-G001
- status: no tutorial

### week 3 lecture 1

- datetime: 2026-02-16T16:00:00+08:00/2026-02-16T16:50:00+08:00, PT50M
- venue: CYT-LTL
- status: no lecture; public holiday

### week 3 lecture 2

- datetime: 2026-02-20T11:30:00+08:00/2026-02-20T12:20:00+08:00, PT50M
- venue: CYT-LTL
- status: no lecture; public holiday

### week 4 lab 1

- datetime: 2026-02-23T10:30:00+08:00/2026-02-23T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: lab 1 equipment
- ELEC 1100
  - ELEC 1100 / Lab1 equipment ::@:: Setup and component check

### week 4 tutorial 1

- datetime: 2026-02-23T14:30:00+08:00/2026-02-23T15:20:00+08:00, PT50M
- venue: CYT-G001
- topic: prepare for lab 2

### week 4 lecture 1

- datetime: 2026-02-23T16:00:00+08:00/2026-02-23T16:50:00+08:00, PT50M
- venue: CYT-LTL
- topic: DC regulation
- ELEC 1100
  - ELEC 1100 / DC regulation: why use a regulator with a DC source? ::@:: DC sources are non-ideal; regulation provides predictable output voltage rails.
    - ELEC 1100 / DC regulation / direct current (DC) ::@:: “Unidirectional” current flow; in practice used as an adjective meaning approximately “constant” voltage/current (vs AC oscillation).
    - ELEC 1100 / DC regulation / common DC source ::@:: Batteries provide DC voltage from chemical reactions; AC adapters convert wall AC into DC for devices like laptops.
    - ELEC 1100 / DC regulation / connecting ideal sources ::@:: Ideal voltage sources can be in series; they can be in parallel only if they have the same value (different values in parallel is invalid).
    - ELEC 1100 / DC regulation / KVL two-source example: A single loop has two ideal DC sources $V_1=9\text{ V}$ and $V_2=5\text{ V}$ connected in series but opposing (their + terminals face the resistor), with a resistor $R=100\,\Omega$ between the two + terminals. Assume loop current $I$ flows from the $V_1$ + terminal through $R$ toward the $V_2$ + terminal. Find the resistor voltage magnitude $V_R$, the current $I$, and resistor power $P$. ::@:: With the stated polarities and traversal direction, KVL gives $-V_1 + IR + V_2 = 0$, so $IR = V_1 - V_2 = 4\text{ V}$. Therefore $I = V_R/R = 4/100 = 0.04\text{ A}$ and $P = V_R^{2}/R = 4^{2}/100 = 0.16\text{ W}$.
    - ELEC 1100 / DC regulation / why regulation is needed ::@:: Battery terminal voltage varies with discharge, temperature, and internal resistance; a regulator makes the supply predictable for circuits.
    - ELEC 1100 / DC regulation / non-ideal source model: Use $V_{\text{out}} = V_{S} - iR_{S}$ to model source droop. ::@:: Practical source has internal resistance $R_S$ in series so $V_{\text{out}} = V_{S} - iR_{S}$ (output droops as load current increases).
  - ELEC 1100 / [voltage regulator](voltage%20regulator.md): define regulated $V_{\text{out}}$ vs $V_{\text{in}}$ and load. ::@:: A regulator maintains approximately constant $V_{\text{out}}$ despite changes in $V_{\text{in}}$ and load current (within range).
    - [§ why regulation is needed](voltage%20regulator.md#why%20regulation%20is%20needed) ::@:: Batteries droop with discharge/temperature and with load due to internal resistance.
    - [§ diode and zener diode as regulators](voltage%20regulator.md#diode%20and%20zener%20diode%20as%20regulators): what does the Zener clamp near $V_Z$ do? ::@:: A Zener in reverse breakdown can clamp a node near $V_Z$ when used with a series current-limiting resistor.
    - [§ integrated-circuit linear regulators (LM7805)](voltage%20regulator.md#integrated-circuit%20linear%20regulators%20(LM7805)): what rails are produced ($12\text{ V}$ motor, $5\text{ V}$ logic)? ::@:: LM7805 provides regulated $5\text{ V}$ from a higher input; project uses $12\text{ V}$ for motors and regulated $5\text{ V}$ for other circuits with stabilizing capacitors.
    - [§ regulator performance metrics](voltage%20regulator.md#regulator%20performance%20metrics): define line and load regulation as $\Delta V_O/\Delta V_I$ and $\Delta V_O/\Delta I_O$. ::@:: Line regulation $\Delta V_O/\Delta V_I$ and load regulation $\Delta V_O/\Delta I_O$ should ideally be $0$.

### week 4 lecture 2

- datetime: 2026-02-27T11:30:00+08:00/2026-02-27T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: transistors
- ELEC 1100
  - ELEC 1100 / [diode](diode.md)
    - ELEC 1100 / diode / circuit analysis (ideal or $0.7\text{ V}$ drop model): overall method? ::@:: Pick a diode model (ideal or constant $0.7\text{ V}$). Assume the diode is ON or OFF, replace it with the equivalent circuit (ON: short/short + $0.7\text{ V}$ drop; OFF: open), then solve the circuit using KVL/Ohm’s law.
    - ELEC 1100 / diode / circuit analysis consistency check ($V_D$, $I_D$): what do you verify? ::@:: After solving, check that the computed diode voltage/current match the assumed state (forward-bias with $V_D\approx0.7\text{ V}$ and $I_D>0$ for ON; reverse/blocked with $I_D\approx0$ for OFF). If inconsistent, flip the assumption and re-solve.
    - ELEC 1100 / diode / [pn junction and biasing](diode.md#pn%20junction%20and%20biasing) ($\approx0.7\text{ V}$ barrier, anode/cathode): key ideas? ::@:: PN junction is formed by joining P-type and N-type semiconductor regions; the depletion region creates a barrier potential of about $0.7\text{ V}$ for silicon.<br/> The P side is the anode and the N side the cathode; forward bias (anode higher than cathode) allows current, reverse bias blocks it. Conventional current flows from anode to cathode when forward biased.
    - ELEC 1100 / diode / [diode i–v characteristic and models](diode.md#diode%20i%E2%80%93v%20characteristic%20and%20models) (ideal vs $0.7\text{ V}$ model, ON/OFF method): key points? ::@:: Ideal model: diode is a short when forward biased and an open when reverse biased.<br/> Constant-voltage model: when ON, $V_D\approx0.7\text{ V}$; when OFF, $I_D\approx0$. Use the ON/OFF assumption method: assume a state, replace with the equivalent circuit, solve, then check consistency of $V_D$ and $I_D$ with that state.
    - ELEC 1100 / diode / [simple diode circuit analysis and safety](diode.md#simple%20diode%20circuit%20analysis%20and%20safety) (e.g. $1\text{ k}\Omega$ series $R$): why? ::@:: In a series source–resistor–diode circuit, use $I_D\approx(V_S-0.7\text{ V})/R$ when the diode is ON and $V_S>0.7\text{ V}$; when $V_S<0.7\text{ V}$ the diode is OFF and $I_D\approx0$.<br/> A series resistor (e.g. $1\text{ k}\Omega$) is essential to limit current through the diode or LED so that the device is not damaged by excessive current when it turns on.
  - ELEC 1100 / transistor basics: terminals and types (C, B, E; NPN/PNP)? ::@:: A BJT has three terminals: collector (C), base (B), emitter (E). The two main types are NPN and PNP.
  - ELEC 1100 / transistor basics: what are $V_{CC}$ and $V_{CE}$ ($V_{CE}=V_C-V_E$)? ::@:: $V_{CC}$ is the DC supply rail feeding the collector/load network. $V_{CE}$ is the collector-to-emitter voltage: $V_{CE}=V_C-V_E$.
  - ELEC 1100 / transistor basics: three modes (OFF/AMP/SAT) using $I_B$, $I_C$, $\beta$, $V_{CE}$? ::@:: OFF: $I_B\approx0\Rightarrow I_C\approx0$. AMPLIFICATION: $I_C\approx\beta I_B$. SATURATION: $I_C$ limited by the external circuit and $V_{CE}\approx0.2\text{ V}$.
    - ELEC 1100 / transistor / [structure](transistor.md#structure) (C, B, E; NPN/PNP symbol): key points? ::@:: BJT is a PN junction with an extra layer (NPN or PNP); base is the middle leg in the symbol, emitter has the arrow (out for NPN, in for PNP), collector is the other leg.
    - ELEC 1100 / transistor / [historical context](transistor.md#historical%20context): key points? ::@:: First working transistor at Bell Labs (1947, Bardeen, Brattain, Shockley); foundation of modern electronics (computers, phones); Shockley’s company in Palo Alto helped start Silicon Valley.
    - ELEC 1100 / transistor / [transistor operation modes](transistor.md#transistor%20operation%20modes): OFF condition ($V_{BE}<0.7\text{ V}$)? ::@:: OFF: if $V_{BE}<0.7\text{ V}$ then the B–E junction is not forward-biased, so $I_B\approx0$ and therefore $I_C\approx0$ (no conduction).
    - ELEC 1100 / transistor / [transistor operation modes](transistor.md#transistor%20operation%20modes): amplification/active ($V_{BE}>0.7\text{ V}$, $I_C\approx\beta I_B$)? ::@:: AMPLIFICATION (active): with $V_{BE}>0.7\text{ V}$, a small base current flows and the collector current is approximately $I_C\approx\beta I_B$; $V_{CE}$ is not forced tiny (it sits somewhere between saturation and the supply).
    - ELEC 1100 / transistor / [transistor operation modes](transistor.md#transistor%20operation%20modes): saturation ($V_{CE}\approx0.2\text{ V}$, $I_C\approx I_{C,\max}$)? ::@:: SATURATION: base drive is strong enough that the circuit limits the collector current, so $I_C\approx I_{C,\max}$ (e.g. $\approx(V_{CC}-0.2\text{ V})/R_C$) and $V_{CE}\approx0.2\text{ V}$; increasing $I_B$ further does not increase $I_C$ much.
    - ELEC 1100 / transistor / [transistor as a switch](transistor.md#transistor%20as%20a%20switch): what does “NPN low-side” mean? ::@:: “Low-side” means the transistor is between the load and ground, so current flows supply → load → transistor → ground (when on).
    - ELEC 1100 / transistor / [transistor as a switch](transistor.md#transistor%20as%20a%20switch): NPN low-side connections (E, C, base / $R_B$)? ::@:: Emitter to ground, collector to the load (and the other side of the load to $V_{CC}$), base driven from $V_{\text{IN}}$ through a resistor $R_B$ to limit $I_B$.
    - ELEC 1100 / transistor / [transistor as a switch](transistor.md#transistor%20as%20a%20switch): OFF vs ON condition ($V_{\text{IN}}<0.7\text{ V}$, saturation)? ::@:: If $V_{\text{IN}}<0.7\text{ V}$ then $V_{BE}$ is not forward-biased and the transistor is OFF ($I_C\approx0$). If $V_{\text{IN}}$ is high enough to drive base current, the transistor can turn ON; if base drive is strong it saturates with $V_{CE}\approx0.2\text{ V}$ and the load current is near its maximum.

### week 5 lab 1

- datetime: 2026-03-02T10:30:00+08:00/2026-03-02T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: lab 2 KCL & KVL

### week 5 tutorial 1

- datetime: 2026-03-02T14:30:00+08:00/2026-03-02T15:20:00+08:00, PT50M
- venue: CYT-G001
- topic: prepare for lab 3

### week 5 lecture 1

- datetime: 2026-03-02T16:00:00+08:00/2026-03-02T16:50:00+08:00, PT50M
- venue: CYT-LTL
- topic: H-bridge

### week 5 lecture 2

- datetime: 2026-03-06T11:30:00+08:00/2026-03-06T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: DC motors

### week 6 lab 1

- datetime: 2026-03-09T10:30:00+08:00/2026-03-09T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: diodes & DC regulation

### week 6 tutorial 1

- datetime: 2026-03-09T14:30:00+08:00/2026-03-09T15:20:00+08:00, PT50M
- venue: CYT-G001
- topic: prepare for lab 4

### week 6 lecture 1

- datetime: 2026-03-09T16:00:00+08:00/2026-03-09T16:50:00+08:00, PT50M
- venue: CYT-LTL
- topic: pulse & PWM

### week 6 lecture 2

- datetime: 2026-03-13T11:30:00+08:00/2026-03-13T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: sensors

### week 7 lab 1

- datetime: 2026-03-16T10:30:00+08:00/2026-03-16T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: transistor & h-bridge

### week 7 tutorial 1

- datetime: 2026-03-16T14:30:00+08:00/2026-03-16T15:20:00+08:00, PT50M
- venue: CYT-G001
- topic: Lab practice (for lab exam)

### week 7 lecture 1

- datetime: 2026-03-16T16:00:00+08:00/2026-03-16T16:50:00+08:00, PT50M
- venue: CYT-LTL
- topic: Boolean algebra

### week 7 lecture 2

- datetime: 2026-03-20T11:30:00+08:00/2026-03-20T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: logic control

### week 8 lab 1

- datetime: 2026-03-23T10:30:00+08:00/2026-03-23T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: Lab practice (for lab exam)

### week 8 tutorial 1

- datetime: 2026-03-23T14:30:00+08:00/2026-03-23T15:20:00+08:00, PT50M
- venue: CYT-G001
- status: no tutorial

### week 8 lecture 1

- datetime: 2026-03-23T16:00:00+08:00/2026-03-23T16:50:00+08:00, PT50M
- venue: CYT-LTL
- topic: MCU & arduino

### week 8 lecture 2

- datetime: 2026-03-27T11:30:00+08:00/2026-03-27T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: arduino programming (i)

### week 9 lab 1

- datetime: 2026-03-30T10:30:00+08:00/2026-03-30T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: lab exam

### week 9 tutorial 1

- datetime: 2026-03-30T14:30:00+08:00/2026-03-30T15:20:00+08:00, PT50M
- venue: CYT-G001
- topic: prepare for lab 5

### week 9 lecture 1

- datetime: 2026-03-30T16:00:00+08:00/2026-03-30T16:50:00+08:00, PT50M
- venue: CYT-LTL
- topic: Arduino programming (II)

### week 9 lecture 2

- datetime: 2026-04-03T11:30:00+08:00/2026-04-03T12:20:00+08:00, PT50M
- venue: CYT-LTL
- status: public holiday

### week 10 lab 1

- datetime: 2026-04-06T10:30:00+08:00/2026-04-06T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- status: public holiday; unscheduled

### week 10 tutorial 1

- datetime: 2026-04-06T14:30:00+08:00/2026-04-06T15:20:00+08:00, PT50M
- venue: CYT-G001
- status: public holiday; unscheduled

### week 10 lecture 1

- datetime: 2026-04-06T16:00:00+08:00/2026-04-06T16:50:00+08:00, PT50M
- venue: CYT-LTL
- status: public holiday; unscheduled

### week 10 lecture 2

- datetime: 2026-04-10T11:30:00+08:00/2026-04-10T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: final project

### week 11 lab 1

- datetime: 2026-04-13T10:30:00+08:00/2026-04-13T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: lab 5 sensor & MCU

### week 11 tutorial 1

- datetime: 2026-04-13T14:30:00+08:00/2026-04-13T15:20:00+08:00, PT50M
- venue: CYT-G001
- topic: prepare for lab 6

### week 11 lecture 1

- datetime: 2026-04-13T16:00:00+08:00/2026-04-13T16:50:00+08:00, PT50M
- venue: CYT-LTL
- topic: written exam review

### week 11 lecture 2

- datetime: 2026-04-17T11:30:00+08:00/2026-04-17T12:20:00+08:00, PT50M
- venue: CYT-LTL
- status: unscheduled

### week 12 lab 1

- datetime: 2026-04-20T10:30:00+08:00/2026-04-20T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: lab 6 assembly of the robot car

### week 12 tutorial 1

- datetime: 2026-04-20T14:30:00+08:00/2026-04-20T15:20:00+08:00, PT50M
- venue: CYT-G001
- topic: prepare for project demo

<!-- T3 & T1 will provide T2 video recording during this week (around 2026-04-20) as noted in the schedule. -->

### week 12 lecture 1

- datetime: 2026-04-20T16:00:00+08:00/2026-04-20T16:50:00+08:00, PT50M
- venue: CYT-LTL
- status: unscheduled

### week 12 lecture 2

- datetime: 2026-04-24T11:30:00+08:00/2026-04-24T12:20:00+08:00, PT50M
- venue: CYT-LTL
- status: unscheduled

### week 13 lab 1

- datetime: 2026-04-27T10:30:00+08:00/2026-04-27T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: early demo

### week 13 tutorial 1

- datetime: 2026-04-27T14:30:00+08:00/2026-04-27T15:20:00+08:00, PT50M
- venue: CYT-G001
- status: unscheduled

### week 13 lecture 1

- datetime: 2026-04-27T16:00:00+08:00/2026-04-27T16:50:00+08:00, PT50M
- venue: CYT-LTL
- status: unscheduled

### week 13 lecture 2

- datetime: 2026-05-01T11:30:00+08:00/2026-05-01T12:20:00+08:00, PT50M
- venue: CYT-LTL
- status: unscheduled

### week 14 lab 1

- datetime: 2026-05-04T10:30:00+08:00/2026-05-04T13:20:00+08:00, PT2H50M
- venue: Room 2133 & 2134, Academic Building
- topic: final demo

### week 14 tutorial 1

- datetime: 2026-05-04T14:30:00+08:00/2026-05-04T15:20:00+08:00, PT50M
- venue: CYT-G001
- status: unscheduled

### week 14 lecture 1

- datetime: 2026-05-04T16:00:00+08:00/2026-05-04T16:50:00+08:00, PT50M
- venue: CYT-LTL
- status: unscheduled

### week 14 lecture 2

- datetime: 2026-05-08T11:30:00+08:00/2026-05-08T12:20:00+08:00, PT50M
- venue: CYT-LTL
- status: unscheduled

<!-- additional sessions will be added in chronological order -->

## lab examination

- datetime: 2026-03-30T10:30:00+08:00/2026-03-30T13:20:00+08:00, PT2H50M
- venue: CYT-LTL
- venue: lab sessions (LA3)
- format:
  - cheatsheet: no
  - open book: no
  - questions: lab‑style and theory

## final examination

- datetime: 2026-05-16T00:00:00+08:00/2026-05-29T23:59:00+08:00
- venue: CYT-LTL
- venue: Spring Term Final Examinations, arranged by ARO
- format:
  - cheatsheet: no
  - open book: no
  - questions: lab‑style and theory

## aftermath

### total

- grades: 100/100
  - statistics: ?
