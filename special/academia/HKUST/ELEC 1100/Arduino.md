---
aliases:
  - Arduino
  - Arduino programming
  - ELEC 1100 Arduino
tags:
  - flashcard/active/special/academia/HKUST/ELEC_1100/Arduino
  - language/in/English
---

# Arduino

The Arduino Nano is the specific microcontroller board used for the robot. This note collects the board, IDE workflow, pin model, and programming conventions needed to turn sensor states into motor commands.

## board, IDE, compiler, and sketch workflow

Arduino is an open-source microcontroller-board family that began in 2003 at the Interaction Design Institute in Ivrea, Italy as a low-cost platform for building interactive devices. On this robot platform the Nano board is preferred physically, while the Uno is similar enough to use in simulation because both are built around the ATmega328 microcontroller. The Arduino IDE is a cross-platform C/C++ environment with an editor, compiler, and upload tools.

### from sketch to running hardware

Write a sketch, verify or compile it, and upload it through USB. The compiler converts source code into machine language the microcontroller can execute.

---

Flashcards for this section are as follows:

- Arduino definition ::@:: An open-source microcontroller-board platform for building interactive digital devices.
- why Nano and Uno are similar ::@:: Both use the ATmega328, so the Uno works for simulation while the Nano is used on the physical robot.
- Arduino workflow ::@:: Write a sketch, verify/compile in the IDE, upload via USB.
- compiler role ::@:: Converts source code into machine language the microcontroller can execute.

## sketch structure, comments, constants, and variables

An Arduino sketch is organized around `setup()` and `loop()`.

### required sketch functions

The `setup()` function runs once after reset or power-up and is used for initialization such as setting pin modes. The `loop()` function then runs repeatedly and forms the ongoing control behavior.

---

Flashcards for this section are as follows:

- `setup()` ::@:: Runs once after reset or power-up; used for initialization (e.g. pin configuration).
- `loop()` ::@:: Runs repeatedly; carries the ongoing control behavior.

### comments, `const`, and `int`

Comments explain intent without affecting execution. `const` marks values that should not change (e.g. named pin assignments); `int` stores whole-number quantities such as sensor states, counters, or delay times.

---

Flashcards for this section are as follows:

- named constants ::@:: Keep pin numbers and hardware roles readable instead of hiding them in raw numbers.
- comments ::@:: Explain intent and wiring roles without changing execution.
- `const` ::@:: Marks a value that should not change during execution (e.g. named pin assignment).
- `int` ::@:: Stores whole-number values such as sensor readings, counters, and delay times.

### local variables and stored state

Where a variable is declared determines its lifetime. A variable inside a function or control block is local to that block; one declared outside `loop()` preserves state between passes. A memory variable such as `countBumper` must live in persistent scope so the robot remembers previous bumper hits across `loop()` iterations.

---

Flashcards for this section are as follows:

- persistent scope for `countBumper` ::@:: Must be outside the decision block so it is not reinitialized every time `loop()` repeats.

## digital and analog pin naming, input logic, and output limits

The Nano exposes digital and analog-labeled pins with distinct names and typical roles.

### digital pins, analog pins, and naming

Pins labeled `D0` to `D13` are used mainly for digital HIGH/LOW signals. Pins `A0`–`A5` connect to ADC hardware but can also serve as digital inputs. The line and bumper sensors use headers `A5`, `A3`, and `A4` even when the code treats them as digital.

---

Flashcards for this section are as follows:

- `D` vs `A` pin labels ::@:: `D` pins are for digital HIGH/LOW; `A` pins are tied to ADC hardware but can also be used as named digital inputs.
- ADC ::@:: Analog-to-digital conversion: converts a continuously varying signal into a numerical value.

### built-in pin functions and logic values

`pinMode()` configures a pin as `INPUT` or `OUTPUT`. `digitalRead()` returns `HIGH` or `LOW`, and `digitalWrite()` drives an output to `HIGH` or `LOW`. Arduino also treats `HIGH`, `1`, and `true` equivalently, while `LOW`, `0`, and `false` are equivalent; more generally, any non-zero integer is treated as true in a Boolean context. Compare values of the same data type. `=` assigns; `==` compares.

---

Flashcards for this section are as follows:

- `pinMode()` ::@:: Configures a pin as INPUT or OUTPUT.
- `digitalRead()` ::@:: Returns HIGH or LOW from an input pin.
- `digitalWrite()` ::@:: Drives an output pin to HIGH or LOW.
- Arduino true/false ::@:: `HIGH`/`1`/`true` are equivalent; `LOW`/`0`/`false` are equivalent; any non-zero integer is true.
- `=` vs `==` ::@:: `=` assigns, `==` compares.

### analog input and output limits

Analog pins read through ADC. On this board, above ~$3.0\text{ V}$ reads HIGH, below ~$1.5\text{ V}$ reads LOW. Output pins drive only small loads (up to ~$40\text{ mA}$), so motors need interface circuitry such as the L293.

---

Flashcards for this section are as follows:

- why motors need a driver ::@:: Output pins can drive only small loads; motors require interface circuitry (e.g. L293).
- digital thresholds ::@:: Above ~$3.0\text{ V}$ is HIGH; below ~$1.5\text{ V}$ is LOW. <!-- check: ignore-line[two_sided_calc_warning]: threshold values are conceptual here -->

## control flow, operators, and reusable functions

Regular code flow proceeds line by line, but embedded control needs decisions, repetition, and modular blocks.

### regular flow versus controlled flow

In regular flow, statements execute in written order. In controlled flow, conditions and loops choose different paths.

---

Flashcards for this section are as follows:

- regular vs controlled flow ::@:: Regular: statements in written order. Controlled: conditions and loops choose different paths.
- emphasized control structures ::@:: `if`, `else if`, `for`, and `while`.

### conditionals, comparisons, and Boolean operators

Conditional statements such as `if`, `else if`, and `else` choose actions from sensor states. Comparison operators such as `!=`, `<`, `<=`, `==`, `>`, and `>=` test values, while Boolean operators such as `!`, `&&`, and `||` combine or invert conditions. This is the core pattern for turning left-sensor, right-sensor, and bumper readings into different motor commands.

---

Flashcards for this section are as follows:

- Boolean operators ::@:: `!` = NOT, `&&` = AND, `||` = OR.
- comparison operators ::@:: `!=`, `<`, `<=`, `==`, `>`, `>=`.

### loops and refreshing the tested condition

Repetition can be expressed with `for` loops when the repeat count is known and `while` loops when execution depends on a changing condition. A `while` loop must refresh the tested condition, such as a sensor reading, or it can continue acting on stale information forever. A sensor-controlled `while` loop must re-read the sensor (e.g. `digitalRead()`) so the exit condition can change.

---

Flashcards for this section are as follows:

- `for` vs `while` ::@:: `for` when the count is known; `while` when it depends on a changing condition.
- `while` loop danger ::@:: If the tested condition is not refreshed, the loop acts on stale information forever.
- sensor-controlled `while` ::@:: Must re-read the sensor (e.g. `digitalRead()`) so the exit condition can change.

### compound operators and counters

Compound operators (`++`, `+=`, `--`, `-=`) shorten repeated updates. A counter such as `countBumper` increments each time the bumper fires, letting the robot react differently on the first, second, or later trigger.

---

Flashcards for this section are as follows:

- compound operators ::@:: `++`, `+=`, `--`, `-=`: shorthand for increment, add, decrement, subtract.
- counter usefulness ::@:: Let the robot remember event counts so later decisions depend on past state.

### logic flowcharts and user-defined functions

A flowchart uses terminals, processing boxes, I/O boxes, decision diamonds, and flow lines to map the robot task to program structure before coding.

The built-in functions emphasized in the lectures are `pinMode()`, `digitalRead()`, `digitalWrite()`, `delay()`, and `analogWrite()`. User-defined functions package repeated tasks into named blocks with a return type, name, and optional parameters. Define, call, optionally use the return value. Functions must be declared outside `setup()` and `loop()`. For example, `void myBlink(int delayTime, int led)` reuses one blink routine with different LEDs or speeds.

---

Flashcards for this section are as follows:

- flowchart purpose ::@:: Turns the task into explicit decision, process, and I/O steps before coding.
- built-in functions ::@:: `pinMode()`, `digitalRead()`, `digitalWrite()`, `delay()`, `analogWrite()`.
- user-defined function contents ::@:: Return type, function name, optional parameters, function body.
- function placement ::@:: Declared outside `setup()` and `loop()`.
- function usage order ::@:: Define → call → optionally use returned result.
- parameter usefulness ::@:: One function reused with different values instead of hard-coding.
- `void myBlink(int delayTime, int led)` ::@:: Shows that parameters let the same blink logic work with different delays and LED pins.

## robot pin map

The robot platform uses a fixed pin map so the wiring, driver circuit, and code all match.

### sensor inputs

The left and right line sensors connect to `A5` and `A3`, and the bumper sensor connects to `A4`.

---

Flashcards for this section are as follows:

- line sensor pins ::@:: `A5` = left, `A3` = right.
- bumper sensor pin ::@:: `A4`.

### motor outputs

The left and right PWM commands use `D9` and `D11`, and the left and right direction commands use `D10` and `D12`.

---

Flashcards for this section are as follows:

- PWM pins ::@:: `D9` = `L_PWM`, `D11` = `R_PWM`.
- direction pins ::@:: `D10` = `L_DIR`, `D12` = `R_DIR`.
- fixed pin map ::@:: Keeps code, driver circuit, and sensor wiring consistent.

## timing, PWM output, and debugging habits

### `delay()` and PWM output

`delay(ms)` pauses the program for `ms` milliseconds; long blocking delays reduce responsiveness. `analogWrite(pin, value)` generates PWM on supported output pins for LED fading or motor-speed control.

---

Flashcards for this section are as follows:

- `delay()` ::@:: Pauses the program for a chosen number of milliseconds.
- `delay()` risk ::@:: Long blocking delays slow the controller's reaction to new input.
- `analogWrite(pin, value)` ::@:: Generates PWM on supported output pins for LED fading or motor-speed control.
- `analogWrite` misnomer ::@:: Despite the name, it produces a PWM waveform, not a true analog voltage.

### debugging habits

Debugging checklist: verify pin map, power rails, sensor reads, logic values, and upload path. Remove the Nano from socketed hardware before uploading if the setup interferes with reprogramming.

---

Flashcards for this section are as follows:

- debugging checks ::@:: Verify pin map, power rails, sensor reads, logic values, and upload path.
- Nano removal before upload ::@:: Remove when surrounding socketed hardware interferes with reprogramming.
