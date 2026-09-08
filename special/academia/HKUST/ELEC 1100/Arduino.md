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

- what is Arduino in one sentence ::@:: Arduino is an open-source microcontroller-board platform for building interactive digital devices.
- why Nano and Uno are similar in this context ::@:: Both are built around the ATmega328 microcontroller, so the Uno is close enough for simulation while the Nano is preferred on the physical robot.
- Arduino workflow in one line ::@:: Write a sketch, verify or compile it in the IDE, and upload it through USB to the board.
- what a compiler does for Arduino code ::@:: The compiler converts the source code into machine language that the microcontroller can execute.

## sketch structure, comments, constants, and variables

An Arduino sketch is organized around `setup()` and `loop()`.

### required sketch functions

The `setup()` function runs once after reset or power-up and is used for initialization such as setting pin modes. The `loop()` function then runs repeatedly and forms the ongoing control behavior.

---

Flashcards for this section are as follows:

- `setup()` role in Arduino ::@:: `setup()` runs once after reset or power-up and is used for initialization such as pin configuration.
- `loop()` role in Arduino ::@:: `loop()` runs repeatedly and carries the ongoing control behavior.

### comments, `const`, and `int`

Comments explain the code without affecting execution, while named constants and simple variable types make the sketch readable instead of hiding meaning inside raw pin numbers and magic values. In the lecture sequence, `const` is used for values that should not change, such as named pin assignments, while `int` is used for whole-number quantities such as sensor states, counters, or delay times.

---

Flashcards for this section are as follows:

- why named constants help in an Arduino sketch ::@:: Named constants keep pin numbers and hardware roles readable instead of burying them in raw numbers.
- why comments matter in an Arduino sketch ::@:: Comments explain intent and wiring roles without changing program execution.
- what `const` communicates in an Arduino sketch ::@:: `const` marks a value that should not change during execution, such as a named pin assignment or fixed threshold.
- what `int` is used for in the course Arduino examples ::@:: `int` stores whole-number values such as sensor readings, counters, and delay times.

### local variables and stored state

Where a variable is declared affects how long it keeps its value. A variable declared inside a function or inside a control block is local to that block, while a variable declared outside `loop()` can preserve state between successive passes through the control program. That is why a memory variable such as `countBumper` should live in persistent scope when the robot must remember previous bumper hits instead of forgetting them every time `loop()` repeats.

---

Flashcards for this section are as follows:

- why a variable such as `countBumper` must have persistent scope ::@:: If the robot must remember previous events across repeated passes through `loop()`, the variable must be stored outside the momentary decision block so it is not reinitialized every time.

## digital and analog pin naming, input logic, and output limits

The Nano exposes digital and analog-labeled pins with distinct names and typical roles.

### digital pins, analog pins, and naming

Pins labeled `D0` to `D13` are used mainly for digital HIGH/LOW signals. Pins labeled `A0` to `A5` are identified as analog inputs because they connect to the board's analog-to-digital conversion (ADC) hardware, but in this course they also appear as ordinary digital sensor pins when the robot only needs black-versus-white logic states. That is why the line and bumper sensors are still named by their physical headers `A5`, `A3`, and `A4` even when the code treats them as digital inputs.

---

Flashcards for this section are as follows:

- Nano pin naming: what is the practical difference between `D` and `A` labels? ::@:: `D` labels identify pins usually used for digital HIGH/LOW signals, while `A` labels identify pins tied to the ADC hardware for analog input; the `A` pins can still be used as named digital inputs in this course.
- ADC meaning in the Arduino context ::@:: ADC means analog-to-digital conversion, which converts a continuously varying electrical signal into a numerical value.

### built-in pin functions and logic values

`pinMode()` configures a pin as `INPUT` or `OUTPUT`. `digitalRead()` returns `HIGH` or `LOW`, and `digitalWrite()` drives an output to `HIGH` or `LOW`. Arduino also treats `HIGH`, `1`, and `true` equivalently, while `LOW`, `0`, and `false` are equivalent; more generally, any non-zero integer is treated as true in a Boolean context. The lecture sequence also recommends comparing values of the same data type and remembering that `=` assigns a value while `==` compares two values.

---

Flashcards for this section are as follows:

- what `pinMode()` does ::@:: `pinMode()` configures a pin to behave as an input or an output.
- what values `pinMode()` expects for basic direction setup ::@:: In the basic ELEC 1100 usage, `pinMode()` is called with `INPUT` or `OUTPUT` to choose whether a pin reads a signal or drives one.
- what `digitalRead()` returns ::@:: `digitalRead()` returns a logical HIGH or LOW from an input pin.
- what `digitalWrite()` does ::@:: `digitalWrite()` drives an output pin to a logical HIGH or LOW.
- what values Arduino treats as true and false in the lecture examples ::@:: Arduino treats `HIGH`, `1`, and `true` equivalently, and treats `LOW`, `0`, and `false` equivalently; more generally, any non-zero integer is treated as true.
- `=` versus `==` in Arduino code ::@:: `=` assigns a value, while `==` compares values.

### analog input and output limits

The analog-labeled pins can be used for sensor inputs through ADC, which turns a continuously varying electrical signal into a numerical value. On this board, a value above about $3.0\text{ V}$ is read as HIGH and a value below about $1.5\text{ V}$ is read as LOW. Pins configured as outputs can drive only small loads — up to about $40\text{ mA}$ — so motors must be driven through interface circuitry such as the L293 rather than directly from the board.

---

Flashcards for this section are as follows:

- why motors must not be connected directly to Arduino output pins ::@:: The output pins can drive only small loads, so motors require interface circuitry such as the L293 driver.
- Nano digital thresholds: what voltages are interpreted as HIGH and LOW? ::@:: Above about $3.0\text{ V}$ is interpreted as HIGH, and below about $1.5\text{ V}$ is interpreted as LOW. <!-- check: ignore-line[two_sided_calc_warning]: threshold values are conceptual here -->

## control flow, operators, and reusable functions

Regular code flow proceeds line by line, but embedded control needs decisions, repetition, and modular blocks.

### regular flow versus controlled flow

In a regular flow, statements execute in the order they are written. In a controlled flow, the code takes different paths depending on conditions and loop structure. The important idea is not memorizing syntax in isolation, but translating a human logic process into step-by-step instructions that the controller can execute.

---

Flashcards for this section are as follows:

- regular flow versus controlled flow ::@:: Regular flow executes statements in written order, while controlled flow uses conditions and loops to choose different execution paths.
- which control structures were emphasized in the ELEC 1100 Arduino lectures ::@:: The lectures emphasized `if`, `else if`, `for`, and `while` as the core control structures for turning logic flow into code.

### conditionals, comparisons, and Boolean operators

Conditional statements such as `if`, `else if`, and `else` choose actions from sensor states. Comparison operators such as `!=`, `<`, `<=`, `==`, `>`, and `>=` test values, while Boolean operators such as `!`, `&&`, and `||` combine or invert conditions. This is the core pattern for turning left-sensor, right-sensor, and bumper readings into different motor commands.

---

Flashcards for this section are as follows:

- Boolean operators in Arduino code ::@:: `!` means NOT, `&&` means AND, and `||` means OR.
- comparison operators emphasized in the lecture ::@:: The lecture highlights `!=`, `<`, `<=`, `==`, `>`, and `>=` as the core comparison operators used inside conditions.

### loops and refreshing the tested condition

Repetition can be expressed with `for` loops when the repeat count is known and `while` loops when execution depends on a changing condition. A `while` loop must refresh the tested condition, such as a sensor reading, or it can continue acting on stale information forever. If a control block uses `while` for sensor-based behavior, it should call `digitalRead()` again inside the loop so the exit condition can actually change.

---

Flashcards for this section are as follows:

- when a `for` loop is more natural than a `while` loop ::@:: A `for` loop is more natural when the repetition count is known in advance.
- why a `while` loop can be dangerous in robot control ::@:: If it does not refresh the tested condition, it can keep acting on stale information forever.
- what must happen inside a sensor-controlled `while` loop ::@:: The code must re-read the sensor, for example with `digitalRead()`, so the loop condition can change and the loop can exit.

### compound operators and counters

Compound operators such as `++`, `+=`, `--`, and `-=` make repeated updates shorter and clearer. The lecture examples use them in loops and fading patterns, but the same idea is useful for project counters: a variable such as `countBumper` can be incremented each time the bumper event occurs so the robot can react differently on the first, second, or later trigger.

---

Flashcards for this section are as follows:

- compound operators introduced in the lecture ::@:: `++`, `+=`, `--`, and `-=` are shorthand for repeated updates such as incrementing, decrementing, or adding a step value.
- why `countBumper`-style counters are useful ::@:: They let the robot remember how many times an event has happened so later decisions can depend on past state instead of only the current sensor reading.

### logic flowcharts and user-defined functions

A flowchart represents a process using start or stop terminals, processing boxes, input or output boxes, decision diamonds, and flow lines. In this course it is not decoration: it is the design bridge between the robot task and the program structure that will appear in the project report.

The built-in functions emphasized in the lectures are `pinMode()`, `digitalRead()`, `digitalWrite()`, `delay()`, and `analogWrite()`. Reusable user-defined functions package repeated tasks such as blinking or motion helpers into one named block with a return type, a function name, and optional parameters. To use a function, define it, call it, and optionally use its return value. User-defined functions must be declared outside `setup()` and `loop()`. A parameterized example is `void myBlink(int delayTime, int led)`, which allows one blink routine to be reused with different LEDs or different blink speeds.

---

Flashcards for this section are as follows:

- why flowcharts matter before coding the robot ::@:: A flowchart turns the task into explicit decision, process, and input/output steps, making the later code structure and project explanation clearer.
- built-in functions emphasized in the ELEC 1100 Arduino lectures ::@:: The lectures highlighted `pinMode()`, `digitalRead()`, `digitalWrite()`, `delay()`, and `analogWrite()` as the main built-in functions for the project.
- what a user-defined function contains ::@:: A return type, a function name, an optional parameter list, and the function body.
- where user-defined functions must be placed in an Arduino sketch ::@:: They must be declared outside `setup()` and `loop()`.
- how to use a user-defined function in order ::@:: First define the function, then call it where needed, and optionally use the returned result in later code.
- why parameters are useful in a function ::@:: Parameters let one function be reused with different values instead of hard-coding one case.
- what `void myBlink(int delayTime, int led)` shows about user-defined functions ::@:: It shows that one function can accept parameters so the same blink logic can be reused with different delays and different LED pins.

## robot pin map

The robot platform uses a fixed pin map so the wiring, driver circuit, and code all match.

### sensor inputs

The left and right line sensors connect to `A5` and `A3`, and the bumper sensor connects to `A4`.

---

Flashcards for this section are as follows:

- robot line sensor pins ::@:: `A5` is the left sensor input and `A3` is the right sensor input.
- robot bumper sensor pin ::@:: `A4` is the bumper sensor input.

### motor outputs

The left and right PWM commands use `D9` and `D11`, and the left and right direction commands use `D10` and `D12`.

---

Flashcards for this section are as follows:

- robot PWM output pins ::@:: `D9` is `L_PWM` and `D11` is `R_PWM`.
- robot direction output pins ::@:: `D10` is `L_DIR` and `D12` is `R_DIR`.
- why the fixed pin map matters ::@:: It keeps the code, driver circuit, and sensor wiring consistent across the robot platform.

## timing, PWM output, and debugging habits

### `delay()` and PWM output

`delay()` pauses the program for a chosen number of milliseconds, so it is useful when a motion or output state needs to be held for a short time. However, long blocking delays reduce responsiveness. `analogWrite(pin, value)` generates a PWM wave on supported output pins, which makes it useful for tasks such as LED fading and motor-speed control.

---

Flashcards for this section are as follows:

- what `delay()` does ::@:: `delay()` pauses the program for a chosen number of milliseconds.
- why long `delay()` calls are risky in robot control ::@:: Long blocking delays reduce how quickly the controller can react to new input.
- what `analogWrite(pin, value)` is used for ::@:: It generates PWM on supported output pins for tasks such as LED fading or motor-speed control.
- what the lecture means by `analogWrite(pin, value)` ::@:: Despite its name, `analogWrite()` produces a PWM waveform rather than a true continuously variable analog voltage.

### debugging habits

When debugging, verify the pin map, power rails, sensor reads, logic values, and upload path. If the board is installed in a socketed hardware setup that interferes with reprogramming, remove the Nano before uploading when that hardware configuration requires it.

---

Flashcards for this section are as follows:

- common Arduino debugging checks ::@:: Verify the pin map, power rails, sensor reads, logic values, and upload path.
- when the Nano may need to be removed before uploading ::@:: Remove the Nano before uploading when the surrounding socketed hardware interferes with reprogramming.
