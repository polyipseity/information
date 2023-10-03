# Homework

## __Homework__

Before you start doing homework, You may find these defines in `lcd.h` useful:

```C
#define CHAR_WIDTH 8
#define CHAR_HEIGHT 16

#define MAX_WIDTH 128
#define MAX_HEIGHT 160

#define CHAR_MAX_X_VERTICAL 16
#define CHAR_MAX_Y_VERTICAL 10

#define CHAR_MAX_X_HORIZONTAL 20
#define CHAR_MAX_Y_HORIZONTAL 8

#define CHAR_MAX_X 20  // max between CHAR_MAX_X_VERTICAL and CHAR_MAX_X_HORIZONTAL
#define CHAR_MAX_Y 10  // max between CHAR_MAX_Y_VERTICAL and CHAR_MAX_Y_HORIZONTAL
```

### __Edge Triggering vs Level Triggering__

Consider 2 uses for a single button: (choose BTN1 or BTN2)

#### __Q1 Level Triggering__

- While the button is down, print `Hello, (Your name)` on TFT __(@1)__
- While it is not, flash the LED (at least one LED). __(@1)__
- Two actions should not happen simultaneously.
- Hints:
  - In this case every time the loop comes around, we are concerned with the **current state** (or level) of the buttons GPIO Pin
  - The implementation of the button reading here should be obvious and simple

![](qSrTmjr.gif)

> Notice the green button and the green LED

#### __Q2 Edge Triggering__

- We want to print `Hello, (Your name)` for 1 second when the button is clicked (<200 ms), but only once, so holding the button does nothing more. __(@1)__
- When the button is released, we want to flash the LED for 1 second, but again only once. __(@1)__
- The process repeats. i.e. it will print text again if you click the button. __(@1)__
- Keywords:
  - The event of a signal going from low to high is called the ___rising edge___ and the opposite is the ___falling edge___
  - The `gpio_read()` macro gives us the current state, but edge triggering also requires knowledge of the __past state__ as well as some logic
- Hints: How can we design some code that can call a function _only_ when the button is first clicked? (Rising edge)
    
#### __Bonus__

- Create a sprite in the middle of the screen. (Can be in any shape other than simple rectangle) __(@1)__
- It will move to the left for one `CHAR_WIDTH` when `BTN1` is clicked and released,
- move to the right for one `CHAR_WIDTH` when `BTN2` is clicked and released. __(@2 for both short press)__
