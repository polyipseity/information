---
aliases:
  - ELEC 1100 final project
  - final project
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/final_project
  - language/in/English
---

# final project

The ELEC 1100 final project combines the earlier electronics, logic, and Arduino work into a single robot. The target is a line-following car that uses line sensors, a bumper sensor, motor drivers, and Arduino code to complete a staged route.

## project objective and hardware constraints

The robot follows a white line on a dark mat and is evaluated on staged tasks. The project guide sets these hardware constraints: the robot must use the course platform, the controller logic builds on the sensor-driver-Arduino stack from earlier labs, at most six sensors are allowed, two front sensors are required for line tracking, and one bumper sensor is required for start-line and white-wall detection.

---

Flashcards for this section are as follows:

- ELEC 1100 final project objective ::@:: Build a line-following robot car that completes the staged demonstration route on the white-line mat.
- maximum number of sensors allowed in the final project ::@:: At most six sensors are allowed.
- required sensor set in the final project ::@:: Two front line sensors and one bumper sensor are required.
- final project as integration ::@:: Combines sensing, logic, motor driving, programming, and debugging in one system.

## route, stages, and scoring logic

The route has curves, turns, junctions, looping behavior, and a white-wall end condition, so the robot needs more than simple line-following. The guide divides the work into staged tasks and awards a bonus for early-demo completion. A time bonus rewards fast completion, so both correctness and stable tuning matter.

---

Flashcards for this section are as follows:

- why simple line-following is not enough ::@:: The route has curves, junctions, turns, and a white-wall end, so multiple behaviors are needed.
- early-demo bonus ::@:: Early-demo completion earns bonus credit, rewarding a stable solution sooner.
- time bonus ::@:: A completion-time bonus means correctness and stable tuning both count.

## line-tracking logic and memory

The project guide makes the logic requirement explicit. The left and right sensors determine immediate steering behavior, but the bumper sensor and a memory variable such as `countBumper` are needed because the same line-sensor pattern can mean different things at different times. For example, both the start line and a later junction can present the same `00` pattern, so the controller must remember whether the robot has already left the starting state.

---

Flashcards for this section are as follows:

- why line sensors alone are not enough ::@:: The same sensor pattern can appear in different contexts, so extra state is needed.
- bumper sensor role in project logic ::@:: The bumper sensor provides a state-changing event for start and wall-detection logic.
- `countBumper` as sequential logic ::@:: Stores past information so the controller interprets the same sensor pattern differently at different times.
- control outputs ::@:: The code sets motor direction and speed via `L_DIR`, `R_DIR`, `L_PWM`, and `R_PWM`.

## code, demo, and report expectations

The code submission extends the robot-control template; the source header records group number and members. The report is individual, structured around introduction, logic design, debugging report, and results/conclusion. Formatting constraints (page limit, word count, font/margin) are also specified, so the project grades both robot performance and written communication.

---

Flashcards for this section are as follows:

- code starting point ::@:: Starts from the Lab 6 logic template, extended for the full route.
- code submission ::@:: Group-based; the source header records group number and members.
- report ownership ::@:: Individual submission despite group-based code and demo.
- core sections of the final project report ::@:: Introduction, logic design, debugging report, and results/conclusion.
- report grading ::@:: The project grades both robot behavior and written explanation.
