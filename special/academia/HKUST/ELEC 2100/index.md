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

## children

- [assignments](assignments/index.md)
- [labs](labs/index.md)
- [questions](questions/index.md)
- [AGENTS](AGENTS.md)
- [Fourier series](Fourier%20series.md)
- [Fourier transform](Fourier%20transform.md)
- [continuous-time LTI system](continuous-time%20LTI%20system.md)
- [convolution](convolution.md)
- [discrete Fourier transform](discrete%20Fourier%20transform.md)
- [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md)
- [discrete-time LTI system](discrete-time%20LTI%20system.md)
- [discrete-time signal](discrete-time%20signal.md)
- [frequency response](frequency%20response.md)
- [modulation](modulation.md)
- [sampling theorem](sampling%20theorem.md)
- [signal](signal.md)
- [singular signal](singular%20signal.md)
- [system](system.md)
- [unified Fourier representations](unified%20Fourier%20representations.md)

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
    - LA1: Room 4225C; FridayT12:00:00/FridayT12:50:00
    - LA2: Room 4225C; FridayT09:00:00/FridayT09:50:00
    - LA3: Room 4225C; ThursdayT10:30:00/ThursdayT11:20:00
    - LA4: Room 4225C; FridayT10:30:00/FridayT11:20:00

## overview

- lecture themes
  - basic concepts of signals and systems
  - time-domain analysis of linear time-invariant systems
  - frequency-domain analysis of continuous-time signals
  - frequency-domain analysis of LTI systems and DTFT
  - Laplace transform — complex-frequency-domain analysis of continuous signals and systems
- laboratory outline
  - [lab 1](labs/lab%201/index.md): plot signals and process data files
  - [lab 2](labs/lab%202/index.md): impulse response and convolution
  - [lab 3](labs/lab%203/index.md): Fourier series and filters
  - [lab 4](labs/lab%204/index.md): modulation, demodulation, and sampling
- quiz pages
  - [questions](questions/index.md): canonical public home for ELEC 2100 quizzes, including detailed review pages for archived quizzes and schedule-only placeholders when only quiz timing is known
- basic signal language and graphical intuition
  - [signal](signal.md)
  - [singular signal](singular%20signal.md)
  - [discrete-time signal](discrete-time%20signal.md)
- system vocabulary, properties, and modelling viewpoints
  - [system](system.md)
- continuous-time and discrete-time response analysis
  - [continuous-time LTI system](continuous-time%20LTI%20system.md)
  - [discrete-time LTI system](discrete-time%20LTI%20system.md)
  - [convolution](convolution.md)
- periodic and aperiodic Fourier analysis
  - [Fourier series](Fourier%20series.md)
  - [Fourier transform](Fourier%20transform.md)
  - [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md)
  - [discrete Fourier transform](discrete%20Fourier%20transform.md)

The four Fourier notes are organized by two axes: continuous time versus discrete time, and periodic structure versus aperiodic or finite-record structure. Read them as a small family rather than as four unrelated chapters: [Fourier series](Fourier%20series.md) is for continuous-time periodic signals, [Fourier transform](Fourier%20transform.md) extends that viewpoint to continuous-time aperiodic signals, [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md) is for general sequences on a continuous digital-frequency axis, and [discrete Fourier transform](discrete%20Fourier%20transform.md) is the finite-grid computational transform for periodic-sequence or finite-record data. The extra note [unified Fourier representations](unified%20Fourier%20representations.md) remains enrichment rather than the main official route through the course material.

- frequency-domain system behavior and filtering
  - [frequency response](frequency%20response.md)
- communication applications
  - [modulation](modulation.md)
  - [sampling theorem](sampling%20theorem.md)
- Detailed homework and lab schedules live in the child index pages; quiz pages live under [questions](questions/index.md).
- Topic notes should be added only after the corresponding official materials are archived.

## week 1 lecture

- datetime: 2026-02-03T12:00:00+08:00/2026-02-03T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: course introduction; signals, systems, and core classifications
- ELEC 2100
  - ELEC 2100 / course scope ::@:: ELEC 2100 is a foundation course on signals and systems covering Fourier analysis, Laplace transform, LTI systems, sampling, differential/difference-equation models, and MATLAB-based analysis. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
  - ELEC 2100 / curricular role ::@:: ELEC 2100 is positioned as a foundation for later study in automatic control, digital signal processing, and artificial intelligence. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
  - ELEC 2100 / transform-domain motivation ::@:: Transform methods are introduced because they turn difficult signal-and-system operations into more structured algebraic or frequency-domain problems. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
  - ELEC 2100 / intended learning outcomes ::@:: Students should describe continuous-time and discrete-time signals, analyze LTI systems, and later apply the theory to sampling, differential/difference-equation models, and engineering communication problems. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
  - ELEC 2100 / assessment structure ::@:: The introductory deck gives the main weights as homework 18%, labs 12%, online quizzes 5%, midterm 25%, and final 40%. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- [signal](signal.md)
  - [§ signal meaning and representation](signal.md#signal%20meaning%20and%20representation)
  - [§ signal classifications](signal.md#signal%20classifications)
  - [§ periodicity, energy, and power](signal.md#periodicity-energy-and-power)
  - [§ standard continuous-time signal families](signal.md#standard%20continuous-time%20signal%20families)
  - [§ time transformations and basic operations](signal.md#time%20transformations%20and%20basic%20operations)
- [system](system.md)
  - [§ system meaning and communication context](system.md#system%20meaning%20and%20communication%20context)

---

The introduction deck is mainly a roadmap lecture rather than a derivation-heavy lecture.  It positions ELEC 2100 as a foundation for later control, DSP, and AI courses, previews the full map from signal description to transform-domain analysis, and highlights the practical toolchain of impulse response, convolution, frequency characteristics, and MATLAB-based analysis.

It also motivates the subject through concrete communication and signal-processing examples: historical telegraph and telephone milestones, the evolution toward fiber-optic, satellite, cable, and mobile systems, signal-processing tasks such as noise reduction, and explicit study advice about relating mathematical analysis back to physical meaning.

The lecture front-loads the administrative structure of the course as well: prerequisites, intended learning outcomes, assessment weights, and the broad quiz/exam format.  The detailed technical development begins only after this roadmap, when the course turns to the actual language of signals and their classifications.

## week 1 tutorial

- datetime: 2026-02-04T11:00:00+08:00/2026-02-04T11:50:00+08:00, PT50M
- venue: Room 2464
- status: unscheduled

---

The selected T2 tutorial stream does not have an archived tutorial sheet for the first teaching week, and the first recorded tutorial round in the provided timetable begins in week 2.

## week 1 lab

- datetime: 2026-02-05T10:30:00+08:00/2026-02-05T11:20:00+08:00, PT50M
- venue: Room 4225C
- status: no class

---

The chosen LA3 lab stream does not yet begin in the first teaching week; the first archived lab activity for this course appears in week 4.

## week 1 lecture 2

- datetime: 2026-02-05T12:00:00+08:00/2026-02-05T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: singular signals; step, ramp, gate, and signum; impulse foundations; signal decomposition
- [signal](signal.md)
  - [§ complex numbers and orthogonal decompositions](signal.md#complex%20numbers%20and%20orthogonal%20decompositions)
  - [§ atan2 and quadrant-aware phase extraction](signal.md#atan2%20and%20quadrant-aware%20phase%20extraction)
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
  - [§ memorylessness](system.md#memorylessness)
  - [§ lumped and distributed viewpoints](system.md#lumped%20and%20distributed%20viewpoints)
  - [§ invertibility](system.md#invertibility)
  - [§ linearity](system.md#linearity)
  - [§ time invariance](system.md#time%20invariance)
  - [§ causality](system.md#causality)
  - [§ boundedness (BIBO stability)](system.md#boundedness%20bibo%20stability)
  - [§ representation methods for linear time-invariant systems](system.md#representation%20methods%20for%20linear%20time-invariant%20systems)
  - [§ system analysis viewpoints](system.md#system%20analysis%20viewpoints)

---

This lecture is now the main home for the discrete-time toolkit and the first pass over system characteristics. It gathers the canonical discrete-time sequence families, their elementary operations, sequence energy and power, and the main classification language for systems, together with the first representation and analysis viewpoints for linear time-invariant systems.

## week 2 tutorial

- datetime: 2026-02-11T11:00:00+08:00/2026-02-11T11:50:00+08:00, PT50M
- venue: Room 2464
- topic: continuous-time signal language; classification; periodicity; energy and power; time transformations; singular-signal toolkit
- [signal](signal.md)
  - [§ signal meaning and representation](signal.md#signal%20meaning%20and%20representation)
  - [§ signal classifications](signal.md#signal%20classifications)
  - [§ periodicity, energy, and power](signal.md#periodicity-energy-and-power)
  - [§ standard continuous-time signal families](signal.md#standard%20continuous-time%20signal%20families)
  - [§ time transformations and basic operations](signal.md#time%20transformations%20and%20basic%20operations)
  - [§ complex numbers and orthogonal decompositions](signal.md#complex%20numbers%20and%20orthogonal%20decompositions)
- [singular signal](singular%20signal.md)
  - [§ singular-signal overview](singular%20signal.md#singular-signal%20overview)
  - [§ ramp, step, gate, and signum](singular%20signal.md#ramp-step-gate-and-signum)
  - [§ unit impulse: pulse limits and generalized functions](singular%20signal.md#unit%20impulse-pulse-limits-and-generalized-functions)
  - [§ impulse properties and graphing](singular%20signal.md#impulse%20properties%20and%20graphing)
  - [§ derivatives of singular signals](singular%20signal.md#derivatives%20of%20singular%20signals)
  - [§ doublet and higher impulse derivatives](singular%20signal.md#doublet%20and%20higher%20impulse%20derivatives)
- [discrete-time signal](discrete-time%20signal.md)
  - [§ sinusoidal and complex exponential sequences](discrete-time%20signal.md#sinusoidal%20and%20complex%20exponential%20sequences)

---

This tutorial consolidates the opening signal vocabulary: what classification labels answer, how graph-transformation questions differ from singular-signal calculus questions, and how waveform, algebraic, and complex-number viewpoints should be kept distinct while revising.

## week 2 lab

- datetime: 2026-02-12T10:30:00+08:00/2026-02-12T11:20:00+08:00, PT50M
- venue: Room 4225C
- status: no class

---

No selected LA3 lab activity is archived for this week; the lab program begins later in the term.

## week 2 lecture 2

- datetime: 2026-02-12T12:00:00+08:00/2026-02-12T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: worked examples on periodicity, transformations, singular-signal calculus, and response transfer
- [signal](signal.md)
  - [§ standard continuous-time signal families](signal.md#standard%20continuous-time%20signal%20families)
  - [§ time transformations and basic operations](signal.md#time%20transformations%20and%20basic%20operations)
  - [§ complex numbers and orthogonal decompositions](signal.md#complex%20numbers%20and%20orthogonal%20decompositions)
  - [§ atan2 and quadrant-aware phase extraction](signal.md#atan2%20and%20quadrant-aware%20phase%20extraction)
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
  - [§ linearity](system.md#linearity)
  - [§ time invariance](system.md#time%20invariance)
  - [§ causality](system.md#causality)
  - [§ boundedness (BIBO stability)](system.md#boundedness%20bibo%20stability)
  - [§ linear time-invariant systems and response transfer](system.md#linear%20time-invariant%20systems%20and%20response%20transfer)

---

The worked-example lecture now connects directly to the richer topic notes: periodicity tests for continuous-time and discrete-time signals, graph-reading for transformed signals, singular-signal derivatives at switching edges, and generalized-function calculations involving impulse sampling or doublet differentiation.

## week 3 lecture

- datetime: 2026-02-17T12:00:00+08:00/2026-02-17T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- status: unscheduled; public holiday: Lunar New Year Holiday

---

No lecture was held in this slot because it fell on Lunar New Year's Day.

## week 3 tutorial

- datetime: 2026-02-18T11:00:00+08:00/2026-02-18T11:50:00+08:00, PT50M
- venue: Room 2464
- status: unscheduled; public holiday: Lunar New Year Holiday

---

No T2 tutorial was scheduled in this week according to the provided timetable; the next recorded T2 tutorial round is on 2026-02-25.

## week 3 lab

- datetime: 2026-02-19T10:30:00+08:00/2026-02-19T11:20:00+08:00, PT50M
- venue: Room 4225C
- status: unscheduled; public holiday: Lunar New Year Holiday

---

No lab was held in this slot because it fell on the Lunar New Year Holiday.

## week 3 lecture 2

- datetime: 2026-02-19T12:00:00+08:00/2026-02-19T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- status: unscheduled; public holiday: Lunar New Year Holiday

---

No lecture was held in this slot because it fell on the Lunar New Year Holiday.

## week 4 lecture

- datetime: 2026-02-24T12:00:00+08:00/2026-02-24T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: continuous-time LTI system analysis roadmap; zero-input and zero-state response; impulse and step response; continuous-time convolution introduction
- [system](system.md)
  - [§ time-domain analysis methods and differential-equation viewpoint](system.md#time-domain%20analysis%20methods%20and%20differential-equation%20viewpoint)
- [continuous-time LTI system](continuous-time%20LTI%20system.md)
  - [§ time-domain analysis roadmap](continuous-time%20LTI%20system.md#time-domain%20analysis%20roadmap)
  - [§ response classifications](continuous-time%20LTI%20system.md#response%20classifications)
  - [§ zero-input and zero-state solution logic](continuous-time%20LTI%20system.md#zero-input%20and%20zero-state%20solution%20logic)
  - [§ state continuity and jump discontinuities](continuous-time%20LTI%20system.md#state%20continuity%20and%20jump%20discontinuities)
  - [§ impulse response and step response](continuous-time%20LTI%20system.md#impulse%20response%20and%20step%20response)
  - [§ typical impulse responses and what they mean](continuous-time%20LTI%20system.md#typical%20impulse%20responses%20and%20what%20they%20mean)
  - [§ causality and stability from the impulse response](continuous-time%20LTI%20system.md#causality%20and%20stability%20from%20the%20impulse%20response)
- [convolution](convolution.md)
  - [§ impulse-decomposition viewpoint](convolution.md#impulse-decomposition%20viewpoint)
  - [§ zero-state response via convolution](convolution.md#zero-state%20response%20via%20convolution)
  - [§ physical interpretation of convolution](convolution.md#physical%20interpretation%20of%20convolution)

---

This lecture starts the continuous-time LTI-system sequence by reframing system study in terms of time-domain response analysis. It first contrasts input-output and state-variable descriptions, recalls the classical homogeneous-plus-particular solution method, and then shifts to the response classifications that engineers use to interpret what a solution means.

The lecture then makes the impulse response central. Zero-input response is tied to stored initial energy, zero-state response to external excitation, and the impulse and step responses become the canonical test signals. The final move is the introduction of convolution through impulse decomposition, showing how an arbitrary input can be assembled from weighted shifted impulses and therefore how its zero-state response can be assembled from weighted shifted copies of $h(t)$.

## week 4 tutorial

- datetime: 2026-02-25T11:00:00+08:00/2026-02-25T11:50:00+08:00, PT50M
- venue: Room 2464
- topic: discrete-time signal families; periodicity rules; sequence operations; energy and power; system-property testing
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
  - [§ continuous-time, discrete-time, and mathematical models](system.md#continuous-time-discrete-time-and-mathematical-models)
  - [§ memorylessness](system.md#memorylessness)
  - [§ invertibility](system.md#invertibility)
  - [§ linearity](system.md#linearity)
  - [§ time invariance](system.md#time%20invariance)
  - [§ causality](system.md#causality)
  - [§ boundedness (BIBO stability)](system.md#boundedness%20bibo%20stability)
  - [§ representation methods for linear time-invariant systems](system.md#representation%20methods%20for%20linear%20time-invariant%20systems)

---

This tutorial is the discrete-time companion to the first signal tutorial. The most useful revision habit is to keep the sequence toolkit and the system-property toolkit separate, and then test one system property at a time instead of mixing several property questions into one vague judgment.

## week 4 lab

- datetime: 2026-02-26T10:30:00+08:00/2026-02-26T11:20:00+08:00, PT50M
- venue: Room 4225C
- topic: lab 1 prelab; plot signals and process data files
- [lab 1](labs/lab%201/index.md)
  - [prelab](labs/lab%201/prelab.md)

---

This is the selected LA3 prelab slot for lab 1.  It prepares the MATLAB workflow for signal plotting, sampled-audio handling, and RGB-image inspection before the graded live-script assignment.

## week 4 lecture 2

- datetime: 2026-02-26T12:00:00+08:00/2026-02-26T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: convolution properties; impulse and step kernels; differentiation and integration rules; analytical and graphical convolution calculation
- [convolution](convolution.md)
  - [§ algebraic properties and system interconnections](convolution.md#algebraic%20properties%20and%20system%20interconnections)
  - [§ time shift and special kernels](convolution.md#time%20shift%20and%20special%20kernels)
  - [§ differentiation and integration properties](convolution.md#differentiation%20and%20integration%20properties)
  - [§ analytical convolution and integration limits](convolution.md#analytical%20convolution%20and%20integration%20limits)
  - [§ graphical convolution and overlap geometry](convolution.md#graphical%20convolution%20and%20overlap%20geometry)

---

This lecture develops convolution from a definition into a working toolkit. It shows how the commutative, distributive, and associative properties explain parallel and cascade interconnections, how delays and impulse-like kernels act inside convolution, and why differentiation or integration can often be moved through the convolution sign.

The second half of the lecture is computational. First, the analytical method stresses that correct overlap limits matter more than blindly integrating from $-\infty$ to $\infty$. Then the graphical method turns convolution into a moving-overlap problem, making support intervals, trapezoidal overlap shapes, and width-addition rules visible at a glance.

## week 5 lecture

- datetime: 2026-03-03T12:00:00+08:00/2026-03-03T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: Fourier synthesis in audio signals; harmonic interpretation of musical tones; bandwidth intuition from pulse trains and spectra; Fourier analysis as analysis and synthesis
- [discrete-time LTI system](discrete-time%20LTI%20system.md)
  - [§ difference-equation solution viewpoints](discrete-time%20LTI%20system.md#difference-equation%20solution%20viewpoints)
  - [§ iterative method and recursion intuition](discrete-time%20LTI%20system.md#iterative%20method%20and%20recursion%20intuition)
  - [§ discrete-time impulse response](discrete-time%20LTI%20system.md#discrete-time%20impulse%20response)
  - [§ causality and stability from discrete-time impulse response](discrete-time%20LTI%20system.md#causality%20and%20stability%20from%20discrete-time%20impulse%20response)
- [convolution](convolution.md)
  - [§ discrete-time convolution sum](convolution.md#discrete-time%20convolution%20sum)
  - [§ discrete-time properties and support range](convolution.md#discrete-time%20properties%20and%20support%20range)
  - [§ computing discrete convolution](convolution.md#computing%20discrete%20convolution)

---

This lecture mirrors the continuous-time LTI-system story in discrete form. Difference equations are introduced as recursive models, the iterative method is presented as the sample-by-sample computational viewpoint, and the classical homogeneous-plus-particular logic is revisited as the conceptual bridge to later z-transform methods.

The lecture then shifts to the discrete-time impulse response and the convolution sum. The key message is that a discrete-time LTI system can be analyzed by the same structural ideas as a continuous-time one, but with shifted unit samples and sums instead of shifted impulses and integrals.

## week 5 tutorial

- datetime: 2026-03-04T11:00:00+08:00/2026-03-04T11:50:00+08:00, PT50M
- venue: Room 2464
- topic: zero-input and zero-state response; impulse response; step response; continuous-time convolution; LTI-system properties from $h(t)$
- [continuous-time LTI system](continuous-time%20LTI%20system.md)
  - [§ response classifications](continuous-time%20LTI%20system.md#response%20classifications)
  - [§ mapping the response labels to ODE solutions](continuous-time%20LTI%20system.md#mapping%20the%20response%20labels%20to%20ode%20solutions)
  - [§ zero-input and zero-state solution logic](continuous-time%20LTI%20system.md#zero-input%20and%20zero-state%20solution%20logic)
  - [§ impulse response and step response](continuous-time%20LTI%20system.md#impulse%20response%20and%20step%20response)
  - [§ causality and stability from the impulse response](continuous-time%20LTI%20system.md#causality%20and%20stability%20from%20the%20impulse%20response)
  - [§ impulse-response case studies](continuous-time%20LTI%20system.md#impulse-response%20case%20studies)
- [convolution](convolution.md)
  - [§ impulse-decomposition viewpoint](convolution.md#impulse-decomposition%20viewpoint)
  - [§ zero-state response via convolution](convolution.md#zero-state%20response%20via%20convolution)
  - [§ physical interpretation of convolution](convolution.md#physical%20interpretation%20of%20convolution)
  - [§ algebraic properties and system interconnections](convolution.md#algebraic%20properties%20and%20system%20interconnections)
  - [§ time shift and special kernels](convolution.md#time%20shift%20and%20special%20kernels)
  - [§ analytical convolution and integration limits](convolution.md#analytical%20convolution%20and%20integration%20limits)
  - [§ graphical convolution and overlap geometry](convolution.md#graphical%20convolution%20and%20overlap%20geometry)
  - [§ convolution case studies and intuition](convolution.md#convolution%20case%20studies%20and%20intuition)

---

This is the first fully systems-focused tutorial. The revision chain to keep visible is: step response integrates impulse response, convolution superposes shifted impulse responses, and causality or stability can often be read directly from the support and total weight of $h(t)$.

## week 5 lab

- datetime: 2026-03-05T10:30:00+08:00/2026-03-05T11:20:00+08:00, PT50M
- venue: Room 4225C
- topic: lab 1 assignment; plot signals and process data files
- [lab 1](labs/lab%201/index.md)
  - [lab](labs/lab%201/lab.md)

---

This is the selected LA3 graded lab-1 slot.  The archived assignment turns the prelab's plotting, audio, and image-array ideas into student-parameterized live-script tasks.

## week 5 lecture 2

- datetime: 2026-03-05T12:00:00+08:00/2026-03-05T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: worked examples on continuous-time and discrete-time LTI systems; impulse response, convolution shape, causality, stability, and interconnections
- [continuous-time LTI system](continuous-time%20LTI%20system.md)
  - [§ impulse-response case studies](continuous-time%20LTI%20system.md#impulse-response%20case%20studies)
- [convolution](convolution.md)
  - [§ convolution case studies and intuition](convolution.md#convolution%20case%20studies%20and%20intuition)
- [discrete-time LTI system](discrete-time%20LTI%20system.md)
  - [§ causality, stability, and interconnection case studies](discrete-time%20LTI%20system.md#causality-stability-and-interconnection%20case%20studies)

---

The examples lecture consolidates the time-domain LTI-system toolkit by turning definitions into recognition patterns. The examples show how to read a block diagram into an impulse response, how weighted shifted impulses build staircase-like outputs, how pulse self-convolution produces a triangle whose maximum occurs at full overlap, and how the general causality and stability tests are applied in one line once $h(t)$ or $h[n]$ is known.

The final discrete-time interconnection example is especially valuable because it mixes cascade, parallel addition, impulse-response algebra, and geometric-series summation in one problem. It ties together the lecture's main message that LTI analysis becomes systematic once one can move confidently between structure, impulse response, and convolution.

## week 6 lecture

- datetime: 2026-03-10T12:00:00+08:00/2026-03-10T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: spectrum concept; frequency-domain viewpoint; orthogonal decomposition; complete orthogonal bases; Parseval's theorem
- [signal](signal.md)
  - [§ complex numbers and orthogonal decompositions](signal.md#complex%20numbers%20and%20orthogonal%20decompositions)
  - [§ atan2 and quadrant-aware phase extraction](signal.md#atan2%20and%20quadrant-aware%20phase%20extraction)
- [Fourier series](Fourier%20series.md)
  - [§ spectrum concept and frequency-domain viewpoint](Fourier%20series.md#spectrum%20concept%20and%20frequency-domain%20viewpoint)
  - [§ orthogonal decomposition, completeness, and Parseval's theorem](Fourier%20series.md#orthogonal-decomposition-completeness-and-parsevals-theorem)

---

This lecture opens the frequency-domain part of the course by explaining why a waveform should ever be re-described as a spectrum.  The key idea is that physical systems and signals often reveal their structure more clearly when viewed by frequency content rather than by waveform shape alone.

The mathematical bridge is orthogonal decomposition.  Signals are projected onto orthogonal basis functions just as vectors are projected onto perpendicular directions, and Parseval's theorem gives the corresponding power bookkeeping law once the basis is complete.

## week 6 tutorial

- datetime: 2026-03-11T11:00:00+08:00/2026-03-11T11:50:00+08:00, PT50M
- venue: Room 2464
- topic: discrete-time zero-input and zero-state response; convolution sum; support range; graphical discrete-time convolution; orthogonality and Parseval bridge
- [discrete-time LTI system](discrete-time%20LTI%20system.md)
  - [§ continuous-time and discrete-time parallels](discrete-time%20LTI%20system.md#continuous-time%20and%20discrete-time%20parallels)
  - [§ difference-equation solution viewpoints](discrete-time%20LTI%20system.md#difference-equation%20solution%20viewpoints)
  - [§ mapping the response labels to difference-equation solutions](discrete-time%20LTI%20system.md#mapping%20the%20response%20labels%20to%20difference-equation%20solutions)
  - [§ iterative method and recursion intuition](discrete-time%20LTI%20system.md#iterative%20method%20and%20recursion%20intuition)
  - [§ discrete-time impulse response](discrete-time%20LTI%20system.md#discrete-time%20impulse%20response)
  - [§ causality and stability from discrete-time impulse response](discrete-time%20LTI%20system.md#causality%20and%20stability%20from%20discrete-time%20impulse%20response)
  - [§ causality, stability, and interconnection case studies](discrete-time%20LTI%20system.md#causality-stability-and-interconnection%20case%20studies)
- [convolution](convolution.md)
  - [§ discrete-time convolution sum](convolution.md#discrete-time%20convolution%20sum)
  - [§ discrete-time properties and support range](convolution.md#discrete-time%20properties%20and%20support%20range)
  - [§ computing discrete convolution](convolution.md#computing%20discrete%20convolution)
- [Fourier series](Fourier%20series.md)
  - [§ spectrum concept and frequency-domain viewpoint](Fourier%20series.md#spectrum%20concept%20and%20frequency-domain%20viewpoint)
  - [§ orthogonal decomposition, completeness, and Parseval's theorem](Fourier%20series.md#orthogonal-decomposition-completeness-and-parsevals-theorem)

---

This tutorial mirrors the continuous-time systems sheet in discrete form and then pivots into the frequency-domain geometry that prepares the Fourier-series block. A good revision split is to use recursion and convolution for sample-domain problems, but switch to inner-product language when the problem asks how a waveform is decomposed into orthogonal frequency components.

## week 6 lab

- datetime: 2026-03-12T10:30:00+08:00/2026-03-12T11:20:00+08:00, PT50M
- venue: Room 4225C
- topic: lab 2 prelab; impulse response and convolution
- [lab 2](labs/lab%202/index.md)
  - [prelab](labs/lab%202/prelab.md)

---

This is the selected LA3 prelab slot for lab 2.  It prepares discrete convolution support bookkeeping, echo modeling, and two-dimensional image filtering in MATLAB.

## week 6 lecture 2

- datetime: 2026-03-12T12:00:00+08:00/2026-03-12T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: trigonometric and exponential Fourier series; coefficient extraction; symmetry rules; Fourier synthesis; Gibbs phenomenon; periodic pulse-train spectra; periodic summation and transform sampling
- [Fourier series](Fourier%20series.md)
  - [§ trigonometric Fourier series and harmonic form](Fourier%20series.md#trigonometric%20Fourier%20series%20and%20harmonic%20form)
  - [§ exponential Fourier series, symmetry, and discrete spectra](Fourier%20series.md#exponential-fourier-series-symmetry-and-discrete-spectra)
  - [§ periodic summation and transform sampling](Fourier%20series.md#periodic%20summation%20and%20transform%20sampling)
  - [§ approximation, Gibbs phenomenon, and periodic pulse-train spectra](Fourier%20series.md#approximation-gibbs-phenomenon-and-periodic-pulse-train-spectra)

---

This lecture turns orthogonal decomposition into a working periodic-signal tool.  The trigonometric and exponential Fourier-series forms are derived as two equivalent ways to describe the same harmonic content, and symmetry is used to predict which coefficients must vanish before any integral is carried out.

The lecture also connects the theory to recognizable engineering patterns: Gibbs oscillation near jumps, the sinc-envelope spectrum of pulse trains, bandwidth changes caused by pulse-width changes, Fourier synthesis as the harmonic reconstruction viewpoint, and the bridge from periodic summation in time to transform sampling on the harmonic grid.

The note now also makes the periodic line-spectrum convention more explicit: an exponential Fourier-series coefficient $F_k$ corresponds in the Fourier-transform picture to the weighted impulse $2\pi F_k\,\delta(\omega-k\omega_0)$ with $\omega_0=2\pi/T$, and engineering magnitude/phase sketches are usually drawn in that transform-style impulse-spectrum convention rather than as a raw coefficient table.

## week 7 lecture

- datetime: 2026-03-17T12:00:00+08:00/2026-03-17T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: derivation of the Fourier transform; inverse transform; continuous spectra; transform-density viewpoint; existence conditions; typical Fourier transforms of aperiodic signals
- [Fourier transform](Fourier%20transform.md)
  - [§ from Fourier series to Fourier transform](Fourier%20transform.md#from%20Fourier%20series%20to%20Fourier%20transform)
  - [§ representations, physical meaning, and existence](Fourier%20transform.md#representations-physical-meaning-and-existence)
  - [§ typical Fourier transforms of aperiodic signals](Fourier%20transform.md#typical-fourier-transforms-of-aperiodic-signals)

---

The course now leaves discrete line spectra and moves to continuous spectra.  The Fourier transform is introduced as the limit of a Fourier-series description whose period grows without bound, so the harmonic spacing shrinks into a continuum and the discrete line weights become a continuous transform-density viewpoint.

The lecture then builds transform intuition through standard pairs rather than properties alone: pulses, one-sided exponentials, constants, signum, impulse, and doublet-type signals each show how time-domain localization, decay, or singularity reappears in frequency.

## week 7 tutorial

- datetime: 2026-03-18T11:00:00+08:00/2026-03-18T11:50:00+08:00, PT50M
- venue: Room 2464
- topic: trigonometric, harmonic, and exponential Fourier-series forms; coefficient conversion; spectrum plotting; symmetry shortcuts; Parseval-based power calculations
- [Fourier series](Fourier%20series.md)
  - [§ spectrum concept and frequency-domain viewpoint](Fourier%20series.md#spectrum%20concept%20and%20frequency-domain%20viewpoint)
  - [§ orthogonal decomposition, completeness, and Parseval's theorem](Fourier%20series.md#orthogonal-decomposition-completeness-and-parsevals-theorem)
  - [§ trigonometric Fourier series and harmonic form](Fourier%20series.md#trigonometric%20fourier%20series%20and%20harmonic%20form)
  - [§ exponential Fourier series, symmetry, and discrete spectra](Fourier%20series.md#exponential-fourier-series-symmetry-and-discrete-spectra)
  - [§ approximation, Gibbs phenomenon, and periodic pulse-train spectra](Fourier%20series.md#approximation-gibbs-phenomenon-and-periodic-pulse-train-spectra)

---

This tutorial is the main consolidation point for continuous-time periodic Fourier analysis. The highest-payoff workflow is: identify period and symmetry first, choose the most efficient coefficient form second, and only then compute or convert coefficients.

## week 7 lab

- datetime: 2026-03-19T10:30:00+08:00/2026-03-19T11:20:00+08:00, PT50M
- venue: Room 4225C
- topic: lab 2 assignment; impulse response and convolution
- [lab 2](labs/lab%202/index.md)
  - [lab](labs/lab%202/lab.md)

---

This is the selected LA3 graded lab-2 slot.  The archived assignment focuses on series and parallel system composition across sequence, audio, and image-filter examples.

## week 7 lecture 2

- datetime: 2026-03-19T12:00:00+08:00/2026-03-19T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: Fourier-transform properties; scaling; time and frequency shifting; differentiation and integration; convolution theorems; periodic signals under the Fourier transform; Dirac comb and sampling/repetition bridge
- [Fourier series](Fourier%20series.md)
  - [§ periodic summation and transform sampling](Fourier%20series.md#periodic%20summation%20and%20transform%20sampling)
- [Fourier transform](Fourier%20transform.md)
  - [§ symmetry, scaling, and shifting properties](Fourier%20transform.md#symmetry-scaling-and-shifting-properties)
  - [§ differentiation, integration, and convolution theorems](Fourier%20transform.md#differentiation-integration-and-convolution-theorems)
  - [§ periodic signals in the Fourier-transform view](Fourier%20transform.md#periodic%20signals%20in%20the%20Fourier-transform%20view)

---

This lecture turns the Fourier transform from a definition into a calculus.  Delays become phase factors, modulation becomes spectral shifting, differentiation becomes multiplication by $j\omega$, and convolution becomes multiplication of spectra.

It also resolves the relationship between the transform and periodic signals: a periodic waveform still has a meaningful Fourier transform, but the result is a weighted impulse train in frequency rather than an ordinary continuous curve.  The Dirac comb becomes the key bridge object linking periodic repetition in time with harmonic-grid sampling in frequency, and the notes now make the reverse Fourier-series-to-Fourier-transform intuition explicit in both directions.

The transform note now also stresses the exact line weight and plotting convention: each Fourier-series coefficient $F_k$ contributes the Fourier-transform line $2\pi F_k\,\delta(\omega-k\omega_0)$, so periodic magnitude/phase diagrams are typically drawn as Fourier-transform impulse spectra with the factor $2\pi$ included in the line magnitude.

## week 8 lecture

- datetime: 2026-03-24T12:00:00+08:00/2026-03-24T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: Fourier synthesis in audio signals; harmonic interpretation of musical tones; bandwidth intuition from pulse trains and spectra; Fourier analysis as analysis and synthesis; worked examples on Fourier-series coefficient extraction, spectrum plotting, periodic summation and Dirac-comb sampling, transform-pair recognition, and duality-based reasoning
- [Fourier series](Fourier%20series.md)
  - [§ spectrum concept and frequency-domain viewpoint](Fourier%20series.md#spectrum%20concept%20and%20frequency-domain%20viewpoint)
  - [§ trigonometric Fourier series and harmonic form](Fourier%20series.md#trigonometric%20Fourier%20series%20and%20harmonic%20form)
  - [§ exponential Fourier series, symmetry, and discrete spectra](Fourier%20series.md#exponential-fourier-series-symmetry-and-discrete-spectra)
  - [§ periodic summation and transform sampling](Fourier%20series.md#periodic%20summation%20and%20transform%20sampling)
  - [§ approximation, Gibbs phenomenon, and periodic pulse-train spectra](Fourier%20series.md#approximation-gibbs-phenomenon-and-periodic-pulse-train-spectra)
- [Fourier transform](Fourier%20transform.md)
  - [§ typical Fourier transforms of aperiodic signals](Fourier%20transform.md#typical-fourier-transforms-of-aperiodic-signals)
  - [§ symmetry, scaling, and shifting properties](Fourier%20transform.md#symmetry-scaling-and-shifting-properties)
  - [§ periodic signals in the Fourier-transform view](Fourier%20transform.md#periodic%20signals%20in%20the%20Fourier-transform%20view)

---

The Fourier-series application deck uses musical audio as the intuitive payoff for the periodic-spectrum viewpoint.  A note can be read as a fundamental plus harmonics, and changing those harmonic amplitudes changes timbre while leaving pitch anchored by the fundamental.

This application lecture is also a reminder that Fourier analysis runs in both directions: one may analyze a waveform into harmonics, or synthesize a waveform from a chosen harmonic recipe.  The same bidirectional idea also underlies the periodic-summation and transform-sampling bridge between Fourier series and Fourier transform.

## week 8 tutorial

- datetime: 2026-03-25T11:00:00+08:00/2026-03-25T11:50:00+08:00, PT50M
- venue: Room 2464
- topic: Fourier-series-to-Fourier-transform limit; transform pairs; property-based derivations; Fourier-domain system analysis; RC low-pass filtering; ideal filter models
- [Fourier transform](Fourier%20transform.md)
  - [§ from Fourier series to Fourier transform](Fourier%20transform.md#from%20Fourier%20series%20to%20Fourier%20transform)
  - [§ representations, physical meaning, and existence](Fourier%20transform.md#representations-physical-meaning-and-existence)
  - [§ typical Fourier transforms of aperiodic signals](Fourier%20transform.md#typical-fourier-transforms-of-aperiodic-signals)
  - [§ symmetry, scaling, and shifting properties](Fourier%20transform.md#symmetry-scaling-and-shifting-properties)
  - [§ differentiation, integration, and convolution theorems](Fourier%20transform.md#differentiation-integration-and-convolution-theorems)
  - [§ periodic signals in the Fourier-transform view](Fourier%20transform.md#periodic%20signals%20in%20the%20Fourier-transform%20view)
- [frequency response](frequency%20response.md)
  - [§ time-domain and frequency-domain zero-state viewpoints](frequency%20response.md#time-domain%20and%20frequency-domain%20zero-state%20viewpoints)
  - [§ complex exponentials as LTI eigenfunctions](frequency%20response.md#complex%20exponentials%20as%20lti%20eigenfunctions)
  - [§ magnitude response and phase response](frequency%20response.md#magnitude%20response%20and%20phase%20response)
  - [§ ways to determine the system function](frequency%20response.md#ways%20to%20determine%20the%20system%20function)
  - [§ first-order RC low-pass filter](frequency%20response.md#first-order%20rc%20low-pass%20filter)
  - [§ ideal low-pass, high-pass, and band-pass filters](frequency%20response.md#ideal%20low-pass-high-pass-and-band-pass%20filters)

---

This tutorial is the bridge from periodic Fourier analysis to full transform-domain signal and system analysis. For revision, use `Fourier transform.md` for signal-side derivations and `frequency response.md` for system-side interpretation so that transform-pair memorization, property use, and filter meaning stay connected.

## week 8 lab

- datetime: 2026-03-26T10:30:00+08:00/2026-03-26T11:20:00+08:00, PT50M
- venue: Room 4225C
- topic: lab 3 prelab; Fourier series and filters
- [lab 3](labs/lab%203/index.md)
  - [prelab](labs/lab%203/prelab.md)

---

This is the selected LA3 prelab slot for lab 3.  The prelab note now stays on preparation-stage habits only: audio time indexing, FFT normalization, centered frequency axes, Butterworth normalization, and before/after response reading.

## week 8 lecture 2

- datetime: 2026-03-26T12:00:00+08:00/2026-03-26T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: system function in the Fourier domain; complex exponentials as eigenfunctions; magnitude and phase response; RC low-pass filter; ideal low-pass, high-pass, and band-pass filters
- [frequency response](frequency%20response.md)
  - [§ complex exponentials as LTI eigenfunctions](frequency%20response.md#complex%20exponentials%20as%20LTI%20eigenfunctions)
  - [§ magnitude response and phase response](frequency%20response.md#magnitude%20response%20and%20phase%20response)
  - [§ ways to determine the system function](frequency%20response.md#ways%20to%20determine%20the%20system%20function)
  - [§ first-order RC low-pass filter](frequency%20response.md#first-order%20RC%20low-pass%20filter)
  - [§ ideal low-pass, high-pass, and band-pass filters](frequency%20response.md#ideal%20low-pass-high-pass-and-band-pass-filters)

---

This lecture moves from transform pairs of signals to transform-domain analysis of systems.  The central structural idea is that complex exponentials are LTI eigenfunctions, so an entire system can be summarized by one frequency-dependent complex multiplier $H(\omega)$.

The lecture then turns that abstract statement into engineering patterns: magnitude response tells which frequencies are passed or attenuated, phase response tells how timing is shifted and when that shift behaves like an approximate delay, and the RC low-pass circuit is derived both from loop equations in the time domain and from impedance-based voltage division in the frequency domain.  The resulting first-order system is then compared with ideal low-pass, high-pass, and band-pass filters, including the half-power meaning of cutoff, the rect-to-normalized-sinc derivation behind the ideal low-pass impulse response, and the modulated-sinc interpretation of ideal band-pass selection.

The note now also includes the standard lecture-style ideal-filter example workflow: read the plotted magnitude and phase of an ideal high-pass filter, rewrite the response as the complement of an ideal low-pass filter, and then recover the impulse response directly; the low-pass and band-pass analogues are kept beside it so the three ideal kernels can be compared in one place.

## week 9 lecture

- datetime: 2026-03-31T12:00:00+08:00/2026-03-31T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: communication role of modulation and demodulation; spectrum scarcity and channel allocation; ASK, FSK, and PSK overview; modulation and demodulation block diagrams; amplitude modulation; coherent detection with low-pass recovery; frequency-division and time-division multiplexing; demultiplexing with band-pass filters
- [modulation](modulation.md)
  - [§ communication setting, channel constraints, and implementation overview](modulation.md#communication%20setting-channel%20constraints-and%20implementation%20overview)
  - [§ why modulation is needed](modulation.md#why%20modulation%20is%20needed)
  - [§ common modulation methods: ASK, FSK, and PSK](modulation.md#common%20modulation%20methods-ask-fsk-and-psk)
  - [§ trigonometric identities behind modulation](modulation.md#trigonometric%20identities%20behind%20modulation)
  - [§ suppressed-carrier amplitude modulation](modulation.md#suppressed-carrier%20amplitude%20modulation)
  - [§ coherent demodulation, low-pass recovery, and implementation](modulation.md#coherent%20demodulation-low-pass%20recovery-and%20implementation)
  - [§ multiplexing, demultiplexing, and channel filters](modulation.md#multiplexing-demultiplexing-and%20channel%20filters)
  - [§ other multiplexing methods](modulation.md#other%20multiplexing%20methods)

---

This lecture applies the frequency-shifting property to communication systems, but now starts from the broader communication setting rather than from one product formula alone.  The note explains why modulation exists physically and economically: useful channels occupy particular spectral windows, spectrum is tightly allocated, and neighboring channels are often packed closely enough that good filtering becomes essential.

The lecture then turns that motivation into engineering workflow.  The note now includes ASK-FSK-PSK comparison, explicit transmitter and receiver block-diagram descriptions, detailed trigonometric derivations, AM-SC sideband formulas, coherent demodulation with mandatory low-pass recovery, the one-half and one-quarter scaling picture created by repeated mixing, and the channel-selection logic behind FDM, demultiplexing BPFs, TDM, and other multiplexing methods.

It now also includes the standard point-by-point spectrum-tracing example for a modulation / BPF / coherent-demodulation / LPF chain, so the reader can track the spectra at successive nodes and see explicitly why the normalized recovered output is $y(t)=\frac12 f(t)$ before any gain compensation.

## week 9 tutorial

- datetime: 2026-04-01T11:00:00+08:00/2026-04-01T11:50:00+08:00, PT50M
- venue: Room 2464
- topic: midterm examination
- status: midterm examination

---

The provided timetable records this as an updated extra tutorial round for the selected T2 stream, but no archived tutorial sheet or routing material has been provided yet.

## week 9 lab

- datetime: 2026-04-02T10:30:00+08:00/2026-04-02T11:20:00+08:00, PT50M
- venue: Room 4225C
- status: no class

---

No selected LA3 lab activity is archived for this week.  The lab sequence resumes in week 10 with the graded lab-3 slot.

## week 9 lecture 2

- datetime: 2026-04-02T12:00:00+08:00/2026-04-02T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: sampling model; choosing the sampling frequency; spectrum replication under sampling; Nyquist sampling theorem; ideal Sa/sinc reconstruction; practical hold reconstruction; aliasing and anti-aliasing
- [sampling theorem](sampling%20theorem.md)
  - [§ sampling model and notation](sampling%20theorem.md#sampling%20model%20and%20notation)
  - [§ choosing the sampling frequency](sampling%20theorem.md#choosing%20the%20sampling%20frequency)
  - [§ spectrum of a sampled signal](sampling%20theorem.md#spectrum%20of%20a%20sampled%20signal)
  - [§ sampling theorem and Nyquist limit](sampling%20theorem.md#sampling%20theorem%20and%20Nyquist%20limit)
  - [§ reconstruction and interpolation](sampling%20theorem.md#reconstruction%20and%20interpolation)
  - [§ practical reconstruction filters](sampling%20theorem.md#practical%20reconstruction%20filters)
  - [§ aliasing and anti-aliasing](sampling%20theorem.md#aliasing%20and%20anti-aliasing)
  - [§ reading maximum sampling interval from a spectrum](sampling%20theorem.md#reading%20maximum%20sampling%20interval%20from%20a%20spectrum)

---

This lecture turns the modulation material into the time-division side of communication theory.  Sampling is written as multiplication by a Dirac-comb train in time, so the frequency-domain picture becomes an immediate repetition of the original spectrum at multiples of the sampling frequency.

The theorem itself is taught as a non-overlap condition.  Exact reconstruction is possible when the replicated copies stay separate, and aliasing is precisely the failure of that separation.  The note coverage now also includes the practical question of how the sampling frequency should be chosen, using motion pictures, high-speed recording, and time-lapse capture as intuitive examples of matching the frame rate to the target dynamics.

The reconstruction discussion now makes the scaling and filter logic explicit: the sampled spectrum carries a $1/T$ factor, so the ideal low-pass reconstructor must restore that scaling while selecting the central replica, and the time-domain interpolation formula is derived as convolution with the Sa/$\operatorname{sinc}_{\pi}$ kernel.  The note also contrasts that ideal reconstruction with practical zero-order and first-order hold circuits and expands the anti-aliasing discussion with concrete examples from telephony, image thumbnails, and digital cameras.

The note now also spells out the standard maximum-sampling-interval example: read $\omega_m$ from the spectrum, compute $T_{\max}=\pi/\omega_m$, and sketch the sampled spectrum at the Nyquist limit where adjacent replicas just touch.

## week 10 lecture

- datetime: 2026-04-07T12:00:00+08:00/2026-04-07T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: Fourier transform of a sequence; DTFT derivation from sampled impulse trains; digital angular frequency; periodicity and inverse DTFT; sampled-spectrum interpretation
- [discrete-time Fourier transform](discrete-time%20Fourier%20transform.md)
  - [§ deriving the DTFT from a sampled signal](discrete-time%20Fourier%20transform.md#deriving%20the%20DTFT%20from%20a%20sampled%20signal)
  - [§ periodicity and inverse DTFT](discrete-time%20Fourier%20transform.md#periodicity%20and%20inverse%20DTFT)
  - [§ analog frequency, digital frequency, and Nyquist range](discrete-time%20Fourier%20transform.md#analog%20frequency-digital%20frequency-and%20Nyquist%20range)
  - [§ sampled-spectrum interpretation of the DTFT](discrete-time%20Fourier%20transform.md#sampled-spectrum%20interpretation%20of%20the%20DTFT)
  - [§ existence and basic symmetry](discrete-time%20Fourier%20transform.md#existence%20and%20basic%20symmetry)

---

This lecture moves the course fully into discrete-time frequency analysis.  The DTFT is introduced not as a brand-new mystery formula but as the Fourier transform of the sampled impulse train rewritten in normalized frequency $\Omega=\omega T$.

That viewpoint makes the most important qualitative property immediate: DTFT is periodic with period $2\pi$.  So one period already contains the full frequency description of a sequence, and the principal interval $[-\pi,\pi]$ becomes the discrete-time analogue of the Nyquist frequency range.  The note also now makes the notation map explicit among the original analog spectrum $X(\omega)$, the sampled-spectrum $X_s(\omega)$, and the normalized-frequency form $X(e^{j\Omega})$, ties DTFT periodicity directly to sampling-induced spectrum replication, explains the engineering impulse-decomposition route via the time-shift property, and makes explicit the course-convention link that views the DTFT pair as a complex Fourier-series pair in the variable $\Omega$.

## week 10 tutorial

- datetime: 2026-04-08T11:00:00+08:00/2026-04-08T11:50:00+08:00, PT50M
- venue: Room 2464
- status: no class

---

No T2 tutorial was scheduled in this slot according to the provided timetable.

## week 10 lab

- datetime: 2026-04-09T10:30:00+08:00/2026-04-09T11:20:00+08:00, PT50M
- venue: Room 4225C
- topic: lab 3 assignment; Fourier series and filters
- [lab 3](labs/lab%203/index.md)
  - [lab](labs/lab%203/lab.md)

---

This is the selected LA3 graded lab-3 slot.  The archived submission has now been distilled into the companion lab note, which records the lab-specific reasoning for peak identification, cosine reconstruction, Butterworth cutoff selection, datatip reading, and the difference between the Butterworth output and the ideal-filter picture.

## week 10 lecture 2

- datetime: 2026-04-09T12:00:00+08:00/2026-04-09T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: discrete-time Fourier series; orthogonality of discrete exponentials; coefficient derivation; periodicity, shifting, symmetry, Parseval, and circular convolution for periodic sequences
- [discrete Fourier transform](discrete%20Fourier%20transform.md)
  - [§ relation between DTFS and DFT](discrete%20Fourier%20transform.md#relation%20between%20DTFS%20and%20DFT)
  - [§ periodic sequences and discrete-time Fourier series](discrete%20Fourier%20transform.md#periodic%20sequences%20and%20discrete-time%20Fourier%20series)
  - [§ orthogonality and DTFS coefficient derivation](discrete%20Fourier%20transform.md#orthogonality%20and%20DTFS%20coefficient%20derivation)
  - [§ normalization map between DTFS and DFT](discrete%20Fourier%20transform.md#normalization%20map%20between%20DTFS%20and%20DFT)
  - [§ periodicity, symmetry, and circular operations for DTFS](discrete%20Fourier%20transform.md#periodicity-symmetry-and-circular%20operations%20for%20DTFS)

---

This lecture is the periodic companion to the DTFT lecture.  A period-$N$ sequence is expanded in a finite set of discrete harmonics, and the coefficient formula is derived by orthogonality of the discrete complex exponential basis over one period.

The payoff is that all the familiar Fourier ideas reappear in discrete periodic form: delays become phase factors, modulation becomes index shifting, Parseval becomes finite-sum energy bookkeeping, and convolution becomes circular because both time and frequency descriptions already wrap modulo $N$.  The periodic-sequence material now lives mainly in the DFT note, where the course distinction that DTFS/DFS is for periodic data while DFT is for implicit periodic extension can be kept together with the equally important algebraic fact that the two are the same finite harmonic decomposition up to the placement of the factor $1/N$.

The note now also makes the line-spectrum bridge more explicit: it explains why one would derive the DTFT of a periodic sequence from DTFS at all, carefully separates the discrete harmonic index $k$ from the continuous digital-frequency variable $\Omega$, derives how one harmonic becomes one repeated spectral-line family, explains why the infinite exponential sum becomes a $2\pi$-weighted Dirac line train, and walks through the orthogonality, coefficient-extraction, conjugation, and reversal properties with more explicit algebra.

## week 11 lecture

- datetime: 2026-04-14T12:00:00+08:00/2026-04-14T13:20:00+08:00, PT1H20M
- venue: Lecture Theater D
- topic: DFT as sampled DTFT; finite-length spectral computation; zero padding; circular shift; circular convolution versus linear convolution
- [discrete Fourier transform](discrete%20Fourier%20transform.md)
  - [§ definition and inverse transform](discrete%20Fourier%20transform.md#definition%20and%20inverse%20transform)
  - [§ matrix viewpoint of the DFT](discrete%20Fourier%20transform.md#matrix%20viewpoint%20of%20the%20DFT)
  - [§ relation to DTFT and periodic extension](discrete%20Fourier%20transform.md#relation%20to%20DTFT%20and%20periodic%20extension)
  - [§ linearity and zero padding](discrete%20Fourier%20transform.md#linearity%20and%20zero%20padding)
  - [§ principal value interval extraction](discrete%20Fourier%20transform.md#principal%20value%20interval%20extraction)
  - [§ circular shift](discrete%20Fourier%20transform.md#circular%20shift)
  - [§ circular convolution and its relation to linear convolution](discrete%20Fourier%20transform.md#circular%20convolution%20and%20its%20relation%20to%20linear%20convolution)

---

This lecture turns discrete-time Fourier analysis into a practical computational tool.  The DFT is presented as frequency sampling of the DTFT over a finite data record, while the periodic-extension viewpoint explains why finite transforms naturally produce circular shift and circular convolution laws.

The most important engineering distinction here is circular versus linear thinking.  Direct DFT multiplication computes circular convolution, and zero padding is the deliberate device used to recover ordinary linear convolution when finite records are being processed numerically.  The topic note now also adds the matrix form $\mathbf{X}=F_N\mathbf{x}$ with a $4$-point worked example, emphasizes that zero padding densifies the sampled DTFT grid without creating new spectral information, explains principal value interval extraction as repeating a record periodically and then windowing back one chosen period, and uses explicit modulo-index and alias-sum calculations to contrast circular and linear convolution.

## week 11 tutorial

- datetime: 2026-04-15T11:00:00+08:00/2026-04-15T11:50:00+08:00, PT50M
- venue: Room 2464
- status: unscheduled

---

The timetable reserves this T2 tutorial slot, but no archived tutorial material has been ingested yet.

## week 11 lab

- datetime: 2026-04-16T10:30:00+08:00/2026-04-16T11:20:00+08:00, PT50M
- venue: Room 4225C
- topic: lab 4 prelab; modulation, demodulation, and sampling
- [lab 4](labs/lab%204/index.md)

---

This is the selected LA3 prelab slot for lab 4.  The schedule metadata for the modulation/demodulation/sampling lab is archived, but the detailed prelab content has not yet been ingested.

## week 12 tutorial

- datetime: 2026-04-22T11:00:00+08:00/2026-04-22T11:50:00+08:00, PT50M
- venue: Room 2464
- status: unscheduled

---

The timetable reserves this T2 tutorial slot, but no archived tutorial material has been ingested yet.

## week 12 lab

- datetime: 2026-04-23T10:30:00+08:00/2026-04-23T11:20:00+08:00, PT50M
- venue: Room 4225C
- topic: lab 4 assignment; modulation, demodulation, and sampling
- [lab 4](labs/lab%204/index.md)

---

This is the selected LA3 graded lab-4 slot.  As with the corresponding prelab, the official timing is archived but the assignment content has not yet been ingested into a dedicated note page.

## week 13 tutorial

- datetime: 2026-04-29T11:00:00+08:00/2026-04-29T11:50:00+08:00, PT50M
- venue: Room 2464
- status: unscheduled

---

The timetable reserves this T2 tutorial slot, but no archived tutorial material has been ingested yet.

## week 13 lab

- datetime: 2026-04-30T10:30:00+08:00/2026-04-30T11:20:00+08:00, PT50M
- venue: Room 4225C
- status: no class

---

The selected LA3 lab program has already completed by this point in the archived schedule, so no further lab meeting is recorded for week 13.

## week 14 tutorial

- datetime: 2026-05-06T11:00:00+08:00/2026-05-06T11:50:00+08:00, PT50M
- venue: Room 2464
- status: unscheduled

---

The timetable reserves this T2 tutorial slot, but no archived tutorial material has been ingested yet.

## week 14 lab

- datetime: 2026-05-07T10:30:00+08:00/2026-05-07T11:20:00+08:00, PT50M
- venue: Room 4225C
- status: no class

---

The archived Spring 2026 LA3 lab schedule ends before this week, so the course root records the empty lab slot explicitly for chronology completeness.

## midterm examination

- datetime: 2026-04-01T19:30:00+08:00/2026-04-01T21:00:00+08:00, PT1H30M
- venue: LTA and LTB
- coverage
  - official lecture-notes page highlights revision of basic concepts, time-domain analysis, frequency-domain analysis of continuous-time signals, and the early part of frequency-domain analysis of LTI systems and DTFT immediately before the midterm

---

The midterm is explicitly listed on the Canvas course home page.

## final examination

- datetime: TBD
- venue: TBD
- weighting: 40%

---

The final-exam logistics are not visible in the provided Canvas pages yet.
