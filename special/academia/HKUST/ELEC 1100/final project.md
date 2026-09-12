---
aliases:
  - ELEC 1100 final project
  - final project
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/final_project
  - language/in/English
---

# final project

The ELEC 1100 final project turns the earlier electronics, logic, and Arduino work into one integrated robot. The target system is a line-following robot car that uses line sensors, a bumper sensor, motor drivers, and Arduino code to complete a staged demonstration route.

## project objective and hardware constraints

The robot follows a white line on a dark mat and is evaluated on a staged sequence of tasks rather than on one vague impression of "it kind of works". The project guide fixes several hardware constraints: the robot must use the course platform, the controller logic is built on the established sensor-driver-Arduino stack from the earlier robot build, at most six sensors are allowed, two front sensors are required for line tracking, and one bumper sensor is required for the start line and white-wall detection.

---

Flashcards for this section are as follows:

- ELEC 1100 final project objective ::@:: Build a line-following robot car that completes the staged demonstration route on the white-line mat. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- maximum number of sensors allowed in the final project ::@:: At most six sensors are allowed. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- required sensor set in the final project ::@:: Two front line sensors and one bumper sensor are required. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why the final project is an integration task ::@:: It combines sensing, logic, motor driving, Arduino programming, and debugging into one system. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## route, stages, and scoring logic

The project route includes curves, turns, branching sections, looping behavior, and a white-wall end condition, so the robot must do more than follow one straight strip. The guide divides the work into staged tasks and also awards a bonus for strong early-demo performance. A separate performance bonus is tied to fast completion, which means the project rewards both correctness and stable tuning rather than raw code length.

---

Flashcards for this section are as follows:

- why the project route needs more than one simple line-following rule ::@:: The route includes curves, junction-like situations, turns, and a white-wall end condition, so the robot needs multiple behaviors. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- early-demo bonus idea in the final project ::@:: Strong early-demo completion earns bonus credit, so the project rewards reaching a stable solution early. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why timing matters in project scoring ::@:: The project includes a completion-time bonus, so correctness and stable tuning both matter. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## line-tracking logic and memory

The project guide makes the logic requirement explicit. The left and right sensors determine immediate steering behavior, but the bumper sensor and a memory variable such as `countBumper` are needed because the same line-sensor pattern can mean different things at different times. For example, both the start line and a later junction can present the same `00` pattern, so the controller must remember whether the robot has already left the starting state.

This is a clear example of the transition from combinational logic to sequential logic in a real embedded system.

---

Flashcards for this section are as follows:

- why the final project cannot rely on line sensors alone ::@:: The same current sensor pattern can appear in different contexts, so extra state information is needed. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- bumper sensor role in project logic ::@:: The bumper sensor provides a state-changing event for start and wall-detection logic. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why `countBumper` is a sequential-logic idea ::@:: It stores past information so the controller can interpret the same current sensor pattern differently at different times. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- final project control outputs: what signals must the code ultimately choose? ::@:: The code must choose motor direction and speed outputs such as `L_DIR`, `R_DIR`, `L_PWM`, and `R_PWM`. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->

## code, demo, and report expectations

The deliverable structure is clear. The group code submission extends the existing robot-control template, and the source header is expected to record the group number and member information. The written report is individual and is structured around introduction, logic design, debugging report, and results/conclusion. The report guideline also fixes formatting constraints such as page limit, minimum word count, and font/margin expectations, so the project is assessed as both a technical system and a communicated engineering result.

---

Flashcards for this section are as follows:

- where the final project code starts from in ELEC 1100 ::@:: It starts from the Lab 6 logic template and then extends that code for the full route. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- final project code submission style ::@:: The code submission is group-based and should keep the group/member header information. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- final project report ownership ::@:: The report is an individual submission even though the robot code and demo are group-based. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- core sections of the final project report ::@:: Introduction, logic design, debugging report, and results/conclusion. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
- why the report guideline matters ::@:: The project is graded not only on robot behavior but also on how clearly the engineering work is explained and documented. <!--SR:!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z!fsrs,2026-10-29T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-10-21T00:00:00.000Z-->
