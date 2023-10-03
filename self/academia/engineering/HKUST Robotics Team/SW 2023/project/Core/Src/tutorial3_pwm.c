#include "main.h"
#include "tim.h"


/* Private variables END */

/* Private function prototypes START */

/* Private function prototypes END */

// Enums are always good
typedef enum {
    BOTH_BTN, BTN1_ONLY, BTN2_ONLY, ALL_OFF,
} ButtonState;

typedef enum {
    BUTTON1, BUTTON2,

    //This trick means the NumButtons will equal how many buttons there are (how many enum values)
    //This works as long as the enum values are simple (count up from 0)
    NUM_BUTTON,
} Button;

typedef enum {
    LED1, LED2, LED3, LED4, NUM_LED,
} LED;

/**
 * @brief read the button state
 * return 1 if the button is pressed;
 * return 0 if the button is released;
 */
static inline uint8_t read_button(Button btn) {
    switch (btn) {
    case BUTTON1:
        return !btn_read(BTN1);
    case BUTTON2:
        return !btn_read(BTN2);
    default:
        return 0;
    }
}

static ButtonState btn_state(void) {
    if (read_button(BUTTON1) && read_button(BUTTON2)) {
        return BOTH_BTN;
    } else if (read_button(BUTTON1)) {
        return BTN1_ONLY;
    } else if (read_button(BUTTON2)) {
        return BTN2_ONLY;
    } else {
        return ALL_OFF;
    }
}


void pwm_init(void) {
	// init the pwm prescaler value and auto-reload value and start the pwm
	/* Your code start here */

	/* Your code end here */
}

void pwm_classwork(void) {
	/* Your code start here */

	/* Your code end here */
}

void pwm_homework(void) {
	/* Your code start here */

	/* Your code end here*/
}
