---
aliases:
  - ELEC 1100
  - ELEC 1100 index
  - HKUST ELEC 1100
  - HKUST ELEC 1100 index
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100
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
- Make-up sessions and special accommodations are handled by the
  instructor or IA; consult the official syllabus or LMS for contact
  details rather than embedding names or email addresses in the note.
  Submit proof of absence within one week to arrange a make-up session.
  Medical accommodations require a hard copy of the original
  certificate.

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
- [electronic component](electronic%20component.md)

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
    - [§ current](electronic%20component.md#current) ::@:: current $I=\Delta q/\Delta t$ and conventional direction
    - [§ voltage and potential difference](electronic%20component.md#voltage%20and%20potential%20difference) ::@:: voltage is energy per charge between two points
    - [§ resistance and resistors](electronic%20component.md#resistance%20and%20resistors) ::@:: Ohm's law $V=IR$, resistivity formula $R=\rho L/A$
    - [§ capacitors](electronic%20component.md#capacitors) ::@:: two plates store charge, discharge provides transient power
    - [§ energy and power](electronic%20component.md#energy%20and%20power) ::@:: $E=qV$, $P=IV=I^{2}R=V^{2}/R$ <p> Human/robot energy analogy; DC vs AC sources; lab gear (bench supply, function generator, breadboard, battery monitor, LiPo); human body energy comparison; Galileo $v=\sqrt{2gh}$; resistor heating/short‑circuit hazard and worked numerical examples.
    - [§ resistor networks](electronic%20component.md#resistor%20networks) ::@:: series add, parallel combine via reciprocal conductance

### week 2 lecture 2

- datetime: 2026-02-13T11:30:00+08:00/2026-02-13T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: KCL & KVL

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
  - ELEC 1100 / DC regulation ::@:: Voltage regulation basics

### week 4 lecture 2

- datetime: 2026-02-27T11:30:00+08:00/2026-02-27T12:20:00+08:00, PT50M
- venue: CYT-LTL
- topic: transistors

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
