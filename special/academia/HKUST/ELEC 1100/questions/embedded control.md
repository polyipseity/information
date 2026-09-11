---
aliases:
    - ELEC 1100 embedded control
    - ELEC1100 embedded control
    - HKUST ELEC 1100 embedded control questions
    - HKUST ELEC1100 embedded control questions
tags:
    - flashcard/active/special/academia/HKUST/ELEC_1100/questions/embedded_control
    - language/in/English
---

# embedded control

- HKUST ELEC 1100

These practice problems are derived from the Arduino-oriented exercise sets, but the numeric thresholds, timing values, and pin choices have been changed. The goal is to preserve the programming idea while avoiding a one-to-one copy of the source handouts.

- topics: Arduino pin configuration; conditional logic; sensor state; millis timing; PWM motor control.

<!-- check: ignore-next-line[header_style]: proper noun -->
## Arduino control-flow and code reasoning

> An Arduino sketch defines `const int ledPin = 6;` and `const int sensorPin = A2;`. What should `setup()` contain so the LED is driven and the sensor is read correctly?
>
> Solution: {@{`pinMode(ledPin, OUTPUT);`}@} and {@{`pinMode(sensorPin, INPUT);`}@} should be {@{placed in `setup()`}@}.

<!-- markdownlint MD028 -->

> A temperature warning system should blink the red LED when `temperature >= 68`, blink the yellow LED when `temperature >= 58` but below 68, and otherwise blink the green LED. Why is `if ... else if ... else` the right structure?
>
> Solution: {@{The conditions}@} are {@{mutually exclusive priority bands}@}, so {@{`if ... else if ... else` ensures only one LED behavior}@} is {@{chosen for each temperature reading}@}.

<!-- markdownlint MD028 -->

> Complete the idea: if a loop keeps a motor turning `while(leftSensor == 0)` but never updates `leftSensor` inside the loop, what goes wrong?
>
> Solution: The decision is {@{made from stale data}@}. Even if the physical sensor {@{changes, the code keeps using the old value}@} and {@{the motor behavior may continue incorrectly}@}.

<!-- markdownlint MD028 -->

> A helper function `void driveMotor(int pwmPin, int dirPin, int speed, int dir)` is introduced. What advantage does this have over writing four separate assignment lines everywhere?
>
> Solution: It packages {@{repeated control logic into one reusable unit}@}, which reduces {@{duplication and makes later debugging or tuning easier}@}.

<!-- markdownlint MD028 -->

> A fan should remain on for 20 seconds after motion disappears. Why is `millis()` usually better than a single `delay(20000)` inside the control logic?
>
> Solution: {@{The advantage of `millis()`}@} is it lets {@{the program keep checking sensors and updating outputs while tracking elapsed time}@}, whereas {@{a long `delay()` blocks the controller}@}.

<!-- markdownlint MD028 -->

> The ELEC 1100 robot uses `A5`, `A4`, and `A3` for left, bumper, and right sensors. Write a short explanation of why the pin map should be kept in named constants instead of raw numeric literals scattered through the code.
>
> Solution: {@{Named constants}@} make {@{the hardware contract explicit}@}, prevent {@{accidental pin swaps, and keep the sketch readable}@} when {@{many sensor and motor signals are used together}@}.

## coding-style practice

> A sketch reads two line sensors. If both sensors read white at startup, the robot should stay still until the bumper sensor is first triggered. What kind of variable is needed in addition to the live sensor readings?
>
> Solution: {@{A state variable or counter such as `countBumper`}@} is needed so the code {@{remembers whether the start event has already happened}@}.

<!-- markdownlint MD028 -->

> A student accidentally writes `if (sensor = HIGH)` instead of `if (sensor == HIGH)`. Why is that dangerous?
>
> Solution: {@{The `=` sign}@} assigns {@{HIGH to `sensor` instead of comparing it}@}, so the condition {@{no longer tests the real reading and the logic becomes incorrect}@}.

<!-- markdownlint MD028 -->

> Extra challenge: the left motor is weaker than the right motor. Give one safe software-only adjustment before changing hardware.
>
> Solution: Use {@{different PWM values for the two motors}@} so {@{the weaker side gets a stronger command to compensate for the mechanical asymmetry}@} or {@{the stronger side is reduced until the robot tracks straight}@}.
