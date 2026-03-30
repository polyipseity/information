---
aliases:
  - ELEC 2100
  - ELEC 2100 index
  - ELEC2100
  - ELEC2100 index
  - HKUST ELEC 2100
  - HKUST ELEC 2100 index
  - HKUST ELEC2100
  - HKUST ELEC2100 index
  - Signals and Systems
  - Signals and Systems index
tags:
  - flashcard/active/special/academia/HKUST/ELEC_2100/index
  - function/index
  - language/in/English
---

# index

- HKUST ELEC 2100
- name: Signals and Systems
- credits: 4

---

ELEC 2100 is a foundation course on signals and systems for modelling and analysis of engineering systems.  The official syllabus covers Fourier analysis, LTI systems, sampling, Laplace transform, and engineering applications, with MATLAB used throughout the course.

This page is a logistics-first scaffold for the chosen sections L1, T2, and LA3.  Detailed schedules and per-item logistics live in the child index pages.

## logistics

- prerequisites
  - one of MATH 2011, MATH 2023, MATH 2111, MATH 2350, MATH 2351, or MATH 2352
- reference book
  - Alan V. Oppenheim, Alan S. Willsky, and S. H. Nawab, _Signals and Systems_, 2nd edition, Prentice-Hall International Editions
- grading
  - homework assignments: 18%
  - lab: 12%
    - prelabs: 4%
    - lab assignments: 8%
  - online quizzes: 5%
  - midterm: 25%
  - final: 40%
- sections
  - lecture: L1
    - L1: Lecture Theater D; TuesdayT12:00:00/TuesdayT13:20:00, ThursdayT12:00:00/ThursdayT13:20:00
  - tutorials: T2
    - T1: Room 2302; ThursdayT14:00:00/ThursdayT14:50:00
    - T2: Room 2464; WednesdayT11:00:00/WednesdayT11:50:00
    - T3: Room G009B; ThursdayT18:00:00/ThursdayT18:50:00
  - labs: LA3
    - LA1: Room 4225C; FridayT12:00:00/FridayT12:50:00 <!-- check: ignore-line[numeric_text_not_latex]: room code -->
    - LA2: Room 4225C; FridayT09:00:00/FridayT09:50:00 <!-- check: ignore-line[numeric_text_not_latex]: room code -->
    - LA3: Room 4225C; ThursdayT10:30:00/ThursdayT11:20:00 <!-- check: ignore-line[numeric_text_not_latex]: room code -->
    - LA4: Room 4225C; FridayT10:30:00/FridayT11:20:00 <!-- check: ignore-line[numeric_text_not_latex]: room code -->

## children

- [assignments](assignments/index.md)
- [labs](labs/index.md)
- [tutorials](tutorials/index.md)
- [AGENTS](AGENTS.md)
- [discrete-time signal](discrete-time%20signal.md)
- [signal](signal.md)
- [singular signal](singular%20signal.md)
- [system](system.md)

## official course outline

- lecture chapters
  - chapter 1: basic concepts of signals and systems
  - chapter 2: time-domain analysis of linear time-invariant systems
  - chapter 3: frequency-domain analysis of continuous-time signals
  - chapter 4: frequency-domain analysis of LTI systems and DTFT
  - chapter 5: Laplace transform — complex-frequency-domain analysis of continuous signals and systems
- laboratory outline
  - [lab 1](labs/lab%201/index.md): plot signals and process data files
  - [lab 2](labs/lab%202/index.md): impulse response and convolution
  - [lab 3](labs/lab%203/index.md): Fourier series and filters
  - [lab 4](labs/lab%204/index.md): modulation, demodulation, and sampling

## notes

- Detailed assignment, tutorial, and lab schedules live in the child index pages.
- Topic notes should be added only after the corresponding official materials are archived.

## week 1 lecture

- datetime: 2026-02-03T12:00:00+08:00/2026-02-03T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: course introduction; signals, systems, and core classifications
- ELEC 2100
  - ELEC 2100 / course scope ::@:: ELEC 2100 is a foundation course on signals and systems covering Fourier analysis, Laplace transform, LTI systems, sampling, differential/difference-equation models, and MATLAB-based analysis.
  - ELEC 2100 / curricular role ::@:: ELEC 2100 is positioned as a foundation for later study in automatic control, digital signal processing, and artificial intelligence.
  - ELEC 2100 / transform-domain motivation ::@:: Transform methods are introduced because they turn difficult signal-and-system operations into more structured algebraic or frequency-domain problems.
  - ELEC 2100 / intended learning outcomes ::@:: Students should describe continuous-time and discrete-time signals, analyze LTI systems, and later apply the theory to sampling, differential/difference-equation models, and engineering communication problems.
  - ELEC 2100 / assessment structure ::@:: The introductory deck gives the main weights as homework 18%, labs 12%, online quizzes 5%, midterm 25%, and final 40%.
- [signal](signal.md)
  - [§ signal meaning and representation](signal.md#signal%20meaning%20and%20representation)
  - [§ signal classifications](signal.md#signal%20classifications)
  - [§ periodicity, energy, and power](signal.md#periodicity-energy-and-power)
  - [§ standard continuous-time signal families](signal.md#standard%20continuous-time%20signal%20families)
  - [§ time transformations and basic operations](signal.md#time%20transformations%20and%20basic%20operations)
- [system](system.md)
  - [§ system meaning and communication context](system.md#system%20meaning%20and%20communication%20context)
  - [§ communication-system milestones and modern technologies](system.md#communication-system%20milestones%20and%20modern%20technologies)

---

The introduction deck is mainly a roadmap lecture rather than a derivation-heavy lecture.  It positions ELEC 2100 as a foundation for later control, DSP, and AI courses, previews the full map from signal description to transform-domain analysis, and highlights the practical toolchain of impulse response, convolution, frequency characteristics, and MATLAB-based analysis.

It also motivates the subject through concrete communication and signal-processing examples: historical telegraph and telephone milestones, the evolution toward fiber-optic, satellite, cable, and mobile systems, signal-processing tasks such as noise reduction, and explicit study advice about relating mathematical analysis back to physical meaning.

The lecture front-loads the administrative structure of the course as well: prerequisites, intended learning outcomes, assessment weights, and the broad quiz/exam format.  The detailed technical development begins only after this roadmap, when the course turns to the actual language of signals and their classifications.

## week 1 lecture 2

- datetime: 2026-02-05T12:00:00+08:00/2026-02-05T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: singular signals; step, ramp, gate, and signum; impulse foundations; signal decomposition
- [signal](signal.md)
  - [§ complex numbers and orthogonal decompositions](signal.md#complex%20numbers%20and%20orthogonal%20decompositions)
- [singular signal](singular%20signal.md)
  - [§ singular-signal overview](singular%20signal.md#singular-signal%20overview)
  - [§ ramp, step, gate, and signum](singular%20signal.md#ramp-step-gate-and-signum)
  - [§ unit impulse: pulse limits and generalized functions](singular%20signal.md#unit-impulse-pulse-limits-and-generalized-functions)
  - [§ impulse properties and graphing](singular%20signal.md#impulse%20properties%20and%20graphing)

---

This lecture now has durable note coverage for the foundational singular-signal toolkit rather than only headline definitions. The topic note covers how to draw ramp, step, gate, signum, and impulse graphs, how ordinary piecewise signals differ from generalized functions, and how delta-sequence families preserve unit area while concentrating at one point.

## week 2 lecture

- datetime: 2026-02-10T12:00:00+08:00/2026-02-10T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: discrete-time signals and operations; sequence energy and power; system characteristics; LTIS representation viewpoints
- [signal](signal.md)
  - [§ discrete-time sequences and periodicity](signal.md#discrete-time%20sequences%20and%20periodicity)
- [discrete-time signal](discrete-time%20signal.md)
  - [§ representation methods](discrete-time%20signal.md#representation%20methods)
  - [§ support patterns](discrete-time%20signal.md#support%20patterns)
  - [§ unit sample sequence](discrete-time%20signal.md#unit%20sample%20sequence)
  - [§ unit step and rectangular sequence](discrete-time%20signal.md#unit%20step%20and%20rectangular%20sequence)
  - [§ ramp and one-sided exponential sequences](discrete-time%20signal.md#ramp%20and%20one-sided%20exponential%20sequences)
  - [§ sinusoidal and complex exponential sequences](discrete-time%20signal.md#sinusoidal%20and%20complex%20exponential%20sequences)
  - [§ pointwise operations and index transformations](discrete-time%20signal.md#pointwise%20operations%20and%20index%20transformations)
  - [§ difference and running sum](discrete-time%20signal.md#difference%20and%20running%20sum)
  - [§ decimation and interpolation](discrete-time%20signal.md#decimation%20and%20interpolation)
  - [§ energy and power of sequences](discrete-time%20signal.md#energy%20and%20power%20of%20sequences)
- [system](system.md)
  - [§ system meaning and communication context](system.md#system%20meaning%20and%20communication%20context)
  - [§ continuous-time, discrete-time, and mathematical models](system.md#continuous-time-discrete-time-and-mathematical-models)
  - [§ memoryless, dynamic, lumped, and distributed systems](system.md#memoryless-dynamic-lumped-and-distributed-systems)
  - [§ invertibility, linearity, and time invariance](system.md#invertibility-linearity-and-time-invariance)
  - [§ causality and stability](system.md#causality-and-stability)
  - [§ representation methods for linear time-invariant systems](system.md#representation%20methods%20for%20linear%20time-invariant%20systems)
  - [§ system analysis viewpoints](system.md#system%20analysis%20viewpoints)

---

This lecture is now the main home for the discrete-time toolkit and the first pass over system characteristics. It gathers the canonical discrete-time sequence families, their elementary operations, sequence energy and power, and the main classification language for systems, together with the first representation and analysis viewpoints for linear time-invariant systems.

## week 2 lecture 2

- datetime: 2026-02-12T12:00:00+08:00/2026-02-12T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: worked examples on periodicity, transformations, singular-signal calculus, and response transfer
- [signal](signal.md)
  - [§ standard continuous-time signal families](signal.md#standard%20continuous-time%20signal%20families)
  - [§ time transformations and basic operations](signal.md#time%20transformations%20and%20basic%20operations)
  - [§ complex numbers and orthogonal decompositions](signal.md#complex%20numbers%20and%20orthogonal%20decompositions)
  - [§ discrete-time sequences and periodicity](signal.md#discrete-time%20sequences%20and%20periodicity)
- [discrete-time signal](discrete-time%20signal.md)
  - [§ sinusoidal and complex exponential sequences](discrete-time%20signal.md#sinusoidal%20and%20complex%20exponential%20sequences)
  - [§ pointwise operations and index transformations](discrete-time%20signal.md#pointwise%20operations%20and%20index%20transformations)
  - [§ difference and running sum](discrete-time%20signal.md#difference%20and%20running%20sum)
  - [§ decimation and interpolation](discrete-time%20signal.md#decimation%20and%20interpolation)
  - [§ energy and power of sequences](discrete-time%20signal.md#energy%20and%20power%20of%20sequences)
- [singular signal](singular%20signal.md)
  - [§ impulse properties and graphing](singular%20signal.md#impulse%20properties%20and%20graphing)
  - [§ derivatives of singular signals](singular%20signal.md#derivatives%20of%20singular%20signals)
  - [§ doublet and higher impulse derivatives](singular%20signal.md#doublet%20and%20higher%20impulse%20derivatives)
  - [§ convolution with impulse and impulse derivatives](singular%20signal.md#convolution%20with%20impulse%20and%20impulse%20derivatives)
- [system](system.md)
  - [§ invertibility, linearity, and time invariance](system.md#invertibility-linearity-and-time-invariance)
  - [§ causality and stability](system.md#causality-and-stability)
  - [§ linear time-invariant systems and response transfer](system.md#linear%20time-invariant%20systems%20and%20response%20transfer)

---

The worked-example lecture now connects directly to the richer topic notes: periodicity tests for continuous-time and discrete-time signals, graph-reading for transformed signals, singular-signal derivatives at switching edges, and generalized-function calculations involving impulse sampling or doublet differentiation.

## midterm examination

- datetime: 2026-04-01T19:30:00+08:00/2026-04-01T21:00:00+08:00, PT1H30M
- venue: LTA and LTB
- coverage
  - official lecture-notes page highlights revision of chapters 1, 2, 3, and chapter 4.1-4.2 immediately before the midterm

---

The midterm is explicitly listed on the Canvas course home page.

## final examination

- datetime: TBD
- venue: TBD
- weighting: 40%

---

The final-exam logistics are not visible in the provided Canvas pages yet.
