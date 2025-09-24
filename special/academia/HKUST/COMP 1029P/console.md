---
aliases:
  - Python console
  - Python consoles
tags:
  - flashcard/active/special/academia/HKUST/COMP_1029P/console
  - language/in/English
---

# Python console

How to control the output?

## print

Note that when you call `print`, even if you have not added newlines to the string, {@{a newline is always printed at the end}@}. To prevent that, {@{pass `end=""` to `print` as well, like `print(value, end="")`}@}. You can also specify {@{nonempty strings}@} for `end`. The effect of `end` is that {@{it will be also be printed after printing the value to be printed}@}. Since {@{`end` is by default a newline `\n`}@}, {@{a newline is always printed at the end}@} when {@{you only do `print(value)`}@}. <!--SR:!2026-03-17,591,330!2028-04-15,1192,350!2027-07-26,987,350!2027-05-05,892,330!2025-10-29,19,339!2025-10-29,19,339!2025-10-29,19,339-->

## clear

{@{A primitive way to clear the console}@} that also {@{works on IDLE}@} is by {@{printing a lot of newlines}@}: <!--SR:!2027-04-02,829,330!2025-10-30,19,344!2025-10-30,19,344-->

```Python
for _ in range(4):
  print("\n" * 25)
```

Note that the above only prints 25 newlines a time. This is because {@{IDLE does not show identical lines}@} if {@{the number of lines printed at once is 50 or more}@}. <!--SR:!2026-09-01,707,330!2025-10-30,19,344-->

If your console is an actual console, then you can use {@{call a system command via `os.system`}@}, which is {@{`cls` on Windows and `clear` on UNIX systems}@}. One can detect {@{whether the current OS is Windows}@} by writing {@{`os.name == "nt"`}@}. <!--SR:!2027-04-16,878,330!2028-04-16,1192,350!2025-10-30,19,344!2025-10-30,19,344-->

```Python
import os
os.system("cls" if os.name == "nt" else "clear")
```

## animation

If you try to make an animation by clearing the screen and then printing different patterns each time, you will find that {@{the animation is too fast}@}. Fortunately, we can make Python wait for a while using {@{`time.sleep`, which accepts a decimal number in seconds}@}: <!--SR:!2027-03-13,812,330!2026-09-26,724,330-->

```Python
import time
print("Waiting...")
time.sleep(0.5)
print("0.5 seconds has elapsed")
```
