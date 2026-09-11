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

The workflow is straightforward: write a sketch, verify or compile it, and upload it through USB so the board can execute the instructions. The compiler is the program that converts the source code into machine language that the microcontroller can execute.

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

Comments explain the code without affecting execution, while named constants and simple variable types make the sketch readable instead of hiding meaning inside raw pin numbers and magic values. In the lecture sequence, `const` is used for values that should not change, such as named pin assignments, while `int` is used for whole-number quantities such as sensor states, counters, or delay times.

---

Flashcards for this section are as follows:

- named constants ::@:: Keep pin numbers and hardware roles readable instead of hiding them in raw numbers.
- comments ::@:: Explain intent and wiring roles without changing execution.
- `const` ::@:: Marks a value that should not change during execution (e.g. named pin assignment).
- `int` ::@:: Stores whole-number values such as sensor readings, counters, and delay times.

### local variables and stored state

Where a variable is declared affects how long it keeps its value. A variable declared inside a function or inside a control block is local to that block, while a variable declared outside `loop()` can preserve state between successive passes through the control program. That is why a memory variable such as `countBumper` should live in persistent scope when the robot must remember previous bumper hits instead of forgetting them every time `loop()` repeats.

---

Flashcards for this section are as follows:

- persistent scope for `countBumper` ::@:: Must be outside the decision block so it is not reinitialized every time `loop()` repeats.

## digital and analog pin naming, input logic, and output limits

The Nano exposes digital and analog-labeled pins with distinct names and typical roles.

### digital pins, analog pins, and naming

Pins labeled `D0` to `D13` are used mainly for digital HIGH/LOW signals. Pins labeled `A0` to `A5` are identified as analog inputs because they connect to the board's analog-to-digital conversion (ADC) hardware, but in this course they also appear as ordinary digital sensor pins when the robot only needs black-versus-white logic states. That is why the line and bumper sensors are still named by their physical headers `A5`, `A3`, and `A4` even when the code treats them as digital inputs.

---

Flashcards for this section are as follows:

- `D` vs `A` pin labels ::@:: `D` pins are for digital HIGH/LOW; `A` pins are tied to ADC hardware but can also be used as named digital inputs.
- ADC ::@:: Analog-to-digital conversion: converts a continuously varying signal into a numerical value.

### built-in pin functions and logic values

`pinMode()` configures a pin as `INPUT` or `OUTPUT`. `digitalRead()` returns `HIGH` or `LOW`, and `digitalWrite()` drives an output to `HIGH` or `LOW`. Arduino also treats `HIGH`, `1`, and `true` equivalently, while `LOW`, `0`, and `false` are equivalent; more generally, any non-zero integer is treated as true in a Boolean context. The lecture sequence also recommends comparing values of the same data type and remembering that `=` assigns a value while `==` compares two values.

---

Flashcards for this section are as follows:

- `pinMode()` ::@:: Configures a pin as INPUT or OUTPUT.
- `digitalRead()` ::@:: Returns HIGH or LOW from an input pin.
- `digitalWrite()` ::@:: Drives an output pin to HIGH or LOW.
- Arduino true/false ::@:: `HIGH`/`1`/`true` are equivalent; `LOW`/`0`/`false` are equivalent; any non-zero integer is true.
- `=` vs `==` ::@:: `=` assigns, `==` compares.

### analog input and output limits

The analog-labeled pins can be used for sensor inputs through ADC, which turns a continuously varying electrical signal into a numerical value. On this board, a value above about $3.0\text{ V}$ is read as HIGH and a value below about $1.5\text{ V}$ is read as LOW. Pins configured as outputs can drive only small loads — up to about $40\text{ mA}$ — so motors must be driven through interface circuitry such as the L293 rather than directly from the board.

---

Flashcards for this section are as follows:

- why motors need a driver ::@:: Output pins can drive only small loads; motors require interface circuitry (e.g. L293).
- digital thresholds ::@:: Above ~$3.0\text{ V}$ is HIGH; below ~$1.5\text{ V}$ is LOW. <!-- check: ignore-line[two_sided_calc_warning]: threshold values are conceptual here -->

## control flow, operators, and reusable functions

Regular code flow proceeds line by line, but embedded control needs decisions, repetition, and modular blocks.

### regular flow versus controlled flow

In a regular flow, statements execute in the order they are written. In a controlled flow, the code takes different paths depending on conditions and loop structure. The important idea is not memorizing syntax in isolation, but translating a human logic process into step-by-step instructions that the controller can execute.

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

Repetition can be expressed with `for` loops when the repeat count is known and `while` loops when execution depends on a changing condition. A `while` loop must refresh the tested condition, such as a sensor reading, or it can continue acting on stale information forever. If a control block uses `while` for sensor-based behavior, it should call `digitalRead()` again inside the loop so the exit condition can actually change.

---

Flashcards for this section are as follows:

- `for` vs `while` ::@:: `for` when the count is known; `while` when it depends on a changing condition.
- `while` loop danger ::@:: If the tested condition is not refreshed, the loop acts on stale information forever.
- sensor-controlled `while` ::@:: Must re-read the sensor (e.g. `digitalRead()`) so the exit condition can change.

### compound operators and counters

Compound operators such as `++`, `+=`, `--`, and `-=` make repeated updates shorter and clearer. The lecture examples use them in loops and fading patterns, but the same idea is useful for project counters: a variable such as `countBumper` can be incremented each time the bumper event occurs so the robot can react differently on the first, second, or later trigger.

---

Flashcards for this section are as follows:

- compound operators ::@:: `++`, `+=`, `--`, `-=`: shorthand for increment, add, decrement, subtract.
- counter usefulness ::@:: Let the robot remember event counts so later decisions depend on past state.

### logic flowcharts and user-defined functions

A flowchart represents a process using start or stop terminals, processing boxes, input or output boxes, decision diamonds, and flow lines. In this course it is not decoration: it is the design bridge between the robot task and the program structure that will appear in the project report.

The built-in functions emphasized in the lectures are `pinMode()`, `digitalRead()`, `digitalWrite()`, `delay()`, and `analogWrite()`. Reusable user-defined functions package repeated tasks such as blinking or motion helpers into one named block with a return type, a function name, and optional parameters. To use a function, define it, call it, and optionally use its return value. User-defined functions must be declared outside `setup()` and `loop()`. A parameterized example is `void myBlink(int delayTime, int led)`, which allows one blink routine to be reused with different LEDs or different blink speeds.

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

`delay()` pauses the program for a chosen number of milliseconds, so it is useful when a motion or output state needs to be held for a short time. However, long blocking delays reduce responsiveness. `analogWrite(pin, value)` generates a PWM wave on supported output pins, which makes it useful for tasks such as LED fading and motor-speed control.

---

Flashcards for this section are as follows:

- `delay()` ::@:: Pauses the program for a chosen number of milliseconds.
- `delay()` risk ::@:: Long blocking delays slow the controller's reaction to new input.
- `analogWrite(pin, value)` ::@:: Generates PWM on supported output pins for LED fading or motor-speed control.
- `analogWrite` misnomer ::@:: Despite the name, it produces a PWM waveform, not a true analog voltage.

### debugging habits

When debugging, verify the pin map, power rails, sensor reads, logic values, and upload path. If the board is installed in a socketed hardware setup that interferes with reprogramming, remove the Nano before uploading when that hardware configuration requires it.

---

Flashcards for this section are as follows:

- debugging checks ::@:: Verify pin map, power rails, sensor reads, logic values, and upload path.
- Nano removal before upload ::@:: Remove when surrounding socketed hardware interferes with reprogramming.
