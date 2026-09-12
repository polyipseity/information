/*
  ELEC1100 Your Lab#06 & Project Template

  To program the car tracking the white line on a dark mat

  Group No. (number of your project box): 67
  Group Member 1 (name & SID): Kai Kuen Klein (29083088)
  Group Member 2 (name & SID): Suo Xun Xin (24944268)
*/

// Checklist (for humans only):
// 1. Write names and SIDs.
// 2. Ensure screws are tight.
// 3. Ensure battery is almost fully charged.
// 4. Ensure wirings are tight.
// 5. Ensure front stand is forward.
// 6. Ensure all sensors straight downward.
// 7. Tune sensors. The bumper sensor should be more sensitive, but not too sensitive. The far left sensor usually drifts off, check very carefully. Ensure the sensors turn off at exactly the white line edges.
// 8. Ensure the mat is fully clean.

// Considerations (for humans only):
// stage 9 slower? (most likely maybe! or too early trigger)
// backward stage needs to follow line? (no!)
// spinning needs to slightly longer? (maybe!)
// check time

// ========================= TUNABLE SETTINGS (at the top for easy access) =========================

// Mode selection
const int MODE_CONSTANT_PWM = 0;
const int MODE_LINE_TRACK = 1;
const int MODE_MISSION_TASK = 2;

// Which mode to run. Change ONLY this constant to switch behavior.
const int RUN_MODE = 2; // SET TO 2 OR MODE_MISSION_TASK!!!

const int DEBUG_START_AT_STAGE = 3; // SET TO 3!!!!!
// Debug stage stop (mission mode only):
// Any value outside 3..18 = disabled
// N (3..18) = stop completely once stage N is entered
const int DEBUG_STOP_AT_STAGE = 19; // SET TO 19!!!

// Six effective power levels only: stop / quarter / half low / half / full / max
const float POWER_STOP = 0.0;
const float POWER_QUARTER = 0.31; // quarter
const float POWER_QUARTER_HIGH = 0.4; // quarter high
const float POWER_HALF_LOW = 0.47; // half low, 0.5 or 0.55 better?
const float POWER_HALF = 0.63;  // half, 0.67?
const float POWER_HALF_HIGH = 0.70; // half high
const float POWER_FULL_LOW = 0.75; // full low
const float POWER_FULL = 0.84;  // full, 0.85?
const float POWER_MAX = 1.0; // max

// Constant test mode power (choose from POWER_* levels above)
const float CONSTANT_MODE_POWER = POWER_FULL;

// Right motor compensation multiplier (right is slower, so boost its PWM).
// Right PWM = left PWM * RIGHT_PWM_MULTIPLIER when both are commanded at same power.
const float RIGHT_PWM_MULTIPLIER = 1.054;

// Auto-computed max safe left PWM from multiplier (floor so right never exceeds 255).
const int MAX_LEFT_PWM = (int)(255.0 / RIGHT_PWM_MULTIPLIER);

// Global timing scale for mission mode (all state durations multiplied by this value)
const float MISSION_TIME_MULTIPLIER = 1.0;

// Mission timing model:
// - Number labels (1..18) are map TIME POINTS (waypoints).
// - currentState means active TIME INTERVAL [currentState -> currentState+1].
// - Stages 1 and 2 are handled by startup arming + bumper toggle, so mission mode starts at stage 3.
// - So duration/condition arrays are interval-based (indexed by currentState).
// Relative mission interval durations in ms (base time before multiplying by MISSION_TIME_MULTIPLIER)
// Each interval advances only after min duration; it is forced to advance at max duration.
// Keep windows narrow: max - min <= 500 ms.
const unsigned long INTERVAL_MIN_DURATION_MS[19] = {
  0,
  0,   // 1 (startup-handled)
  0,   // 2 (startup-handled)
  1200,  // 3
  2200,  // 4
  4250,  // 5
  1200,  // 6
  1075,  // 7 (self-rotation only)
  800,  // 8 (post-self-rotation causes variation)
  7200,   // 9  (retuned after slow->haßlf mapping)
  0,  // 10
  350,   // 11
  650,   // 12
  1000,   // 13
  2100,   // 14 (retuned after slow->half mapping)
  1000,   // 15
  375,  // 16
  800,  // 17
  100   // 18
};

const unsigned long INTERVAL_MAX_DURATION_MS[19] = {
  0,
  0, // 1 (startup-handled)
  0, // 2 (startup-handled)
  0, // 2000,  // 3
  0, // 3200,  // 4
  0, // 7000,  // 5
  0, // 2000,  // 6
  1175,  // 7 (self-rotation only)
  0, // 1600,  // 8 (post-self-rotation causes variation)
  0, // 13000, // 9  (retuned after slow->half mapping)
  0,  // 10
  700,  // 11
  1150,  // 12
  0, // 2500,  // 13
  4500,   // 14 (retuned after slow->half mapping)
  0, // 2500,  // 15
  0, // 2500,  // 16
  1000, // 17
  1000 // 18
};

// Cumulative time to REACH each stage point (seconds, before global multiplier)
// Stage 1:  0.00 ~ 0.00
// Stage 2:  0.30 ~ 0.50
// Stage 3:  1.00 ~ 1.50
// Stage 4:  3.90 ~ 4.80
// Stage 5:  4.80 ~ 6.00
// Stage 6:  6.80 ~ 8.40
// Stage 7:  8.00 ~ 10.00
// Stage 8:  9.70 ~ 12.10
// Stage 9: 10.90 ~ 13.70
// Stage 10: 11.35 ~ 14.40
// Stage 11: 13.15 ~ 16.60
// Stage 12: 13.85 ~ 17.60
// Stage 13: 14.55 ~ 18.60
// Stage 14: 15.25 ~ 19.60
// Stage 15: 15.80 ~ 20.40
// Stage 16: 16.60 ~ 21.50
// Stage 17: 18.00 ~ 23.30
// Stage 18: 19.20 ~ 24.90
// Mission end (after stage 18 hold): 22.20 ~ 28.30

// Mission actions per state (index 1..18)
// Note: states 1 and 2 are not run in mission mode (handled by startup gate).
const int ACT_STOP = 0;
const int ACT_LINE_TRACK = 1;
const int ACT_SPIN_360_RIGHT = 2;
const int ACT_BACKWARD_FAST = 3;

// Per-state transition condition (checked after min duration; forced by max duration)
const int COND_TIME_ONLY = 0;
const int COND_CENTER_ON_WHITE = 1;
const int COND_JUNCTION_WHITE = 2;  // use left and right sensors only, ignore center (requested junction condition)
const int COND_BUMPER_ON_WHITE = 3;
const int COND_STAGE9_TO_11_WHITE_PATTERN = 4; // special: (center OR right) with far-right on white
const int COND_STAGE14_TO_15_FAR_RIGHT = 5; // special: stage-14 side confirmation (uses far-right sensor)
const int COND_LEFT_ON_WHITE = 6; // special: far-left tracking sensor on white
const int COND_STAGE7_SIDE_ANY_WHITE = 7; // special: any left-side sensor white AND any right-side sensor white
const int COND_STAGE11_TO_12_JUNCTION_WHITE = 8; // use left and right sensors, and also far right sensor
const int COND_JUNCTION_WHITE_STRICT = 9;
const int COND_STAGE7_SIDE_ANY_WHITE_STRICT = 10;
const int COND_STAGE6_TO_7_JUNCTION_WHITE = 11;

// Stage-entry turn hint (used at the beginning of selected stages)
const int TURN_NONE = 0;
const int TURN_LEFT = -1;
const int TURN_RIGHT = 1;

const int STEER_CMD_NONE = 0;
const int STEER_CMD_LEFT = 1;
const int STEER_CMD_RIGHT = 2;
const int STEER_CMD_STRAIGHT = 3;

const int FAR_SENSOR_NONE = 0;
const int FAR_SENSOR_LEFT = 1;
const int FAR_SENSOR_RIGHT = 2;

// Time for entry turn bias at stage start (before normal line tracking resumes)
const unsigned long ENTRY_TURN_DURATION_SHORT_MS = 110;
const unsigned long ENTRY_TURN_DURATION_SHORTER_MS = 150;
const unsigned long ENTRY_TURN_DURATION_MS = 170;
const unsigned long ENTRY_TURN_DURATION_LONGER_MS = 195;
const unsigned long ENTRY_TURN_DURATION_LONG_MS = 250;

// After forced stage-entry turn ends, temporarily block steering in the opposite direction.
const unsigned long POST_FORCED_TURN_DISTRACT_BLOCK_MS = 200;
const unsigned long POST_FORCED_TURN_DISTRACT_BLOCK_SHORT_MS = 100;
const unsigned long POST_FORCED_TURN_DISTRACT_BLOCK_LONG_MS = 350;
const unsigned long POST_FORCED_TURN_MAX_BLOCK_MS = 500;
const unsigned long POST_FORCED_TURN_SINCE_STAGE_BLOCK_MS = 200;
const unsigned long POST_FORCED_TURN_SINCE_STAGE_9_BLOCK_MS = 230;
const unsigned long ENTRY_SENSOR_STEER_BLOCK_MS = 300;
const unsigned long ENTRY_SENSOR_STEER_BLOCK_LONG_MS = 400;
const unsigned long FAR_RIGHT_CORRECTION_POST_CENTER_MS = 175;
const unsigned long FAR_RIGHT_RECENT_WINDOW_MS = 10;
const unsigned long STAGE9_FAR_SENSOR_DIRECTION_LOCK_MS = 500;
const unsigned long STAGE4_FAR_LEFT_FORCE_TURN_MS = 75;
const unsigned long STAGE5_FAR_LEFT_FORCE_TURN_MS = 75;
const unsigned long STAGE6_FAR_LEFT_FORCE_TURN_MS = 100;
const unsigned long COND_STAGE_TO_11_FAR_RIGHT_LAST_SEEN_AT_LEAST_MS = 2100;
const unsigned long COND_STAGE_TO_11_FAR_LEFT_LAST_SEEN_AT_LEAST_MS = 500;
const unsigned long STAGE11_12_FAR_LEFT_FORCE_TURN_MS = 100;
const unsigned long STAGE_11_ADDITIONAL_LEEWAY_DURATION = 200;
const unsigned long STAGE_11_12_BIAS_MIN_MS = 100;
const unsigned long STAGE18_BACKWARD_HOLD_MS = 100;
const unsigned long STEER_COMMAND_DEBOUNCE_MS = 50;
const int STEER_CHANGE_HISTORY_COUNT = 7;
const unsigned long STEER_CHANGE_WINDOW_MS = 600;
const unsigned long STEER_ADAPTIVE_DEBOUNCE_DURATION_MS = 1000;

const int STATE_ACTION[19] = {
  ACT_STOP,
  ACT_STOP,               // 1 (startup-handled)
  ACT_STOP,               // 2 (startup-handled)
  ACT_LINE_TRACK,         // 3
  ACT_LINE_TRACK,         // 4
  ACT_LINE_TRACK,         // 5
  ACT_LINE_TRACK,         // 6
  ACT_SPIN_360_RIGHT,     // 7
  ACT_LINE_TRACK,         // 8
  ACT_LINE_TRACK,         // 9
  ACT_STOP,               // 10 (dummy stage, instant pass-through)
  ACT_LINE_TRACK,         // 11
  ACT_LINE_TRACK,         // 12
  ACT_LINE_TRACK,         // 13
  ACT_LINE_TRACK,         // 14
  ACT_LINE_TRACK,         // 15
  ACT_LINE_TRACK,         // 16
  ACT_BACKWARD_FAST,      // 17
  ACT_STOP                // 18
};

// Stage-beginning transition decision (from map):
// 4:L, 5:R, 6:L, 9:L, 11:R, 12:L, 13:L, 14:R, 15:R, 16:L
const int STAGE_ENTRY_TURN[19] = {
  TURN_NONE,
  TURN_NONE,   // 1
  TURN_NONE,   // 2
  TURN_NONE,   // 3
  TURN_LEFT,   // 4
  TURN_RIGHT,  // 5
  TURN_LEFT,   // 6
  TURN_NONE,   // 7 (dedicated 360 action)
  TURN_NONE,   // 8 (line tracking only)
  TURN_LEFT,   // 9 (begin with left turn)
  TURN_NONE,   // 10
  TURN_RIGHT,  // 11
  TURN_LEFT,   // 12
  TURN_LEFT,   // 13
  TURN_RIGHT,  // 14
  TURN_RIGHT,  // 15
  TURN_LEFT,   // 16
  TURN_NONE,   // 17 (custom bumper/backward logic)
  TURN_NONE    // 18
};

// Interval transition conditions derived from the map's distraction/junction points.
// For COND_JUNCTION_WHITE, decision uses left+right both white (center ignored).
// Index N corresponds to interval [N -> N+1].
const int INTERVAL_TRANSITION_CONDITION[19] = {
  COND_TIME_ONLY,
  COND_TIME_ONLY,        // 1 (startup-handled)
  COND_TIME_ONLY,        // 2 (startup-handled)
  COND_JUNCTION_WHITE,   // 3 -> arrive 4
  COND_JUNCTION_WHITE,   // 4 -> arrive 5
  COND_STAGE6_TO_7_JUNCTION_WHITE,   // 5 -> arrive 6
  COND_STAGE7_SIDE_ANY_WHITE_STRICT,   // 6 -> arrive 7
  COND_CENTER_ON_WHITE, // 7 (self-rotation) -> arrive 8
  COND_STAGE7_SIDE_ANY_WHITE_STRICT,   // 8 -> arrive 9
  COND_STAGE9_TO_11_WHITE_PATTERN, // 9 -> (10 dummy) -> 11
  COND_TIME_ONLY,        // 10 -> arrive 11 (dummy stage, immediate)
  COND_STAGE11_TO_12_JUNCTION_WHITE,   // 11 -> arrive 12
  COND_LEFT_ON_WHITE,   // 12 -> arrive 13
  COND_STAGE7_SIDE_ANY_WHITE_STRICT,    // 13 -> arrive 14
  COND_STAGE14_TO_15_FAR_RIGHT, // 14 -> arrive 15
  COND_STAGE7_SIDE_ANY_WHITE_STRICT,   // 15 -> arrive 16
  COND_BUMPER_ON_WHITE,  // 16 -> arrive 17 (enter reverse stage on bumper)
  COND_LEFT_ON_WHITE,    // 17 -> arrive 18 (far-left sensor on white)
  COND_TIME_ONLY         // 18
};

// ========================= PIN DEFINITIONS =========================

// assign meaningful names to those pins that will be used
const int pinL_Sensor = A5;      //pin A5: left tracking sensor
const int pinB_Sensor = A4;      //pin A4: bumper sensor
const int pinR_Sensor = A3;      //pin A3: right tracking sensor
const int pinC_Sensor = A2;      //pin A2: center tracking sensor
const int pinFR_Sensor = A1;     //pin A1: far-right tracking sensor (stage 9/14 special use)
const int pinFL_Sensor = A0;     //pin A0: far-left tracking sensor (used in COND_LEFT_ON_WHITE)

const int pinL_PWM = 9;          //pin D9: left motor speed
const int pinL_DIR = 10;         //pin D10: left motor direction

const int pinR_PWM = 11;         //pin D11: right motor speed
const int pinR_DIR = 12;         //pin D12: right motor direction

// ========================= VARIABLES =========================

int leftSensor = 1;    // 1 = dark, 0 = white
int bumperSensor = 1;  // 1 = dark, 0 = white (reserved for start/end marker)
int centerSensor = 1;  // 1 = dark, 0 = white
int rightSensor = 1;   // 1 = dark, 0 = white
int farRightSensor = 1; // 1 = dark, 0 = white (used only in stage 9/14 rule)
int farLeftSensor = 1; // 1 = dark, 0 = white (used only in COND_LEFT_ON_WHITE)
unsigned long farRightLastSeenMs = 0;
unsigned long farLeftLastSeenMs = 0;
int stage9LastActiveFarSensor = FAR_SENSOR_LEFT;

bool farRightCorrectionActive = false;
int farRightCorrectionTurn = TURN_NONE;
bool farRightCorrectionCenterSeen = false;
unsigned long farRightCorrectionPostCenterStartMs = 0;

bool stage11_12BiasActive = false;
int stage11_12BiasTurn = TURN_NONE;
unsigned long stage11_12BiasStartMs = 0;

bool stage5FarLeftForceTurnActive = false;
unsigned long stage5FarLeftForceTurnStartMs = 0;

bool stage4FarLeftForceTurnActive = false;
unsigned long stage4FarLeftForceTurnStartMs = 0;

bool stage6FarLeftForceTurnActive = false;
unsigned long stage6FarLeftForceTurnStartMs = 0;

bool stage11_12FarLeftForceTurnActive = false;
unsigned long stage11_12FarLeftForceTurnStartMs = 0;

int currentState = 0;   // mission interval index [currentState -> currentState+1]; set to 3 when mission starts

// line-lost recovery memory: -1 = last correction to left, 1 = right, 0 = none
int lastTurn = 0;

// start gate: all modes stay stopped until start-line arming is done, then bumper toggles from baseline
int bumperBootState = 1;
bool hasStarted = false;
bool startLineArmed = false;
unsigned long startLineSeenSinceMs = 0;

// Require stable placement on start white line before accepting bumper toggle
const unsigned long START_LINE_CONFIRM_MS = 120;

bool missionStateStarted = false;
unsigned long missionStateStartMs = 0;
int lastMissionState = 0;
bool debugStageStopActive = false;
bool postForcedStraightReleased = false;

int steerDebounceCmd = STEER_CMD_NONE;
unsigned long steerDebounceStartMs = 0;
float steerDebounceCruisePower = POWER_STOP;
bool steerDebounceStabilize = false;
int steerDebounceThisDir = 1;
int steerLastRequestedCmd = STEER_CMD_NONE;
unsigned long steerChangeTimes[STEER_CHANGE_HISTORY_COUNT] = {0, 0, 0, 0, 0, 0, 0};
int steerChangeWriteIndex = 0;
int steerChangeCount = 0;
bool steerAdaptiveDebounceActive = false;
unsigned long steerAdaptiveDebounceStartMs = 0;

float clampPower(float p)
{
  if (p < 0.0) return 0.0;
  if (p > 1.0) return 1.0;
  return p;
}

int readBinaryStable(int pin)
{
  // majority vote over 3 reads for binary sensors (0/1)
  int s1 = digitalRead(pin);
  int s2 = digitalRead(pin);
  int s3 = digitalRead(pin);
  int sum = s1 + s2 + s3;
  return (sum >= 2) ? 1 : 0;
}

unsigned long scaledDurationMs(unsigned long baseMs)
{
  return (unsigned long)(baseMs * MISSION_TIME_MULTIPLIER + 0.5);
}

void refreshTrackingSensors()
{
  leftSensor = readBinaryStable(pinL_Sensor);
  centerSensor = readBinaryStable(pinC_Sensor);
  rightSensor = readBinaryStable(pinR_Sensor);
  farRightSensor = readBinaryStable(pinFR_Sensor);
  farLeftSensor = readBinaryStable(pinFL_Sensor);
}

bool areAllTrackingSensorsOnWhite()
{
  return (leftSensor == 0 && centerSensor == 0 && rightSensor == 0);
}

void clearFarRightCorrection()
{
  farRightCorrectionActive = false;
  farRightCorrectionTurn = TURN_NONE;
  farRightCorrectionCenterSeen = false;
  farRightCorrectionPostCenterStartMs = 0;
}

void clearStage11_12BiasLatch()
{
  stage11_12BiasActive = false;
  stage11_12BiasTurn = TURN_NONE;
  stage11_12BiasStartMs = 0;
}

void clearStage5FarLeftForceTurnLatch()
{
  stage5FarLeftForceTurnActive = false;
  stage5FarLeftForceTurnStartMs = 0;
}

void clearStage4FarLeftForceTurnLatch()
{
  stage4FarLeftForceTurnActive = false;
  stage4FarLeftForceTurnStartMs = 0;
}

void startStage4FarLeftForceTurnLatch()
{
  stage4FarLeftForceTurnActive = true;
  stage4FarLeftForceTurnStartMs = millis();
}

void startStage5FarLeftForceTurnLatch()
{
  stage5FarLeftForceTurnActive = true;
  stage5FarLeftForceTurnStartMs = millis();
}

void clearStage6FarLeftForceTurnLatch()
{
  stage6FarLeftForceTurnActive = false;
  stage6FarLeftForceTurnStartMs = 0;
}

void startStage6FarLeftForceTurnLatch()
{
  stage6FarLeftForceTurnActive = true;
  stage6FarLeftForceTurnStartMs = millis();
}

void clearStage11_12FarLeftForceTurnLatch()
{
  stage11_12FarLeftForceTurnActive = false;
  stage11_12FarLeftForceTurnStartMs = 0;
}

void startStage11_12FarLeftForceTurnLatch()
{
  stage11_12FarLeftForceTurnActive = true;
  stage11_12FarLeftForceTurnStartMs = millis();
}

void clearSteerCommandDebounce()
{
  steerDebounceCmd = STEER_CMD_NONE;
  steerDebounceStartMs = 0;
  steerDebounceCruisePower = POWER_STOP;
  steerDebounceStabilize = false;
  steerDebounceThisDir = 1;
  steerLastRequestedCmd = STEER_CMD_NONE;
  for (int i = 0; i < STEER_CHANGE_HISTORY_COUNT; i++) {
    steerChangeTimes[i] = 0;
  }
  steerChangeWriteIndex = 0;
  steerChangeCount = 0;
  steerAdaptiveDebounceActive = false;
  steerAdaptiveDebounceStartMs = 0;
}

void startStage11_12BiasLatch(int turnDir)
{
  stage11_12BiasActive = true;
  stage11_12BiasTurn = turnDir;
  stage11_12BiasStartMs = millis();
}

void startFarRightCorrection(int turnDir)
{
  farRightCorrectionActive = true;
  farRightCorrectionTurn = turnDir;
  // Use fixed correction timing from correction start (no center-sensor dependency).
  farRightCorrectionCenterSeen = true;
  farRightCorrectionPostCenterStartMs = millis();
}

void onMissionStateEnter(int state)
{
  if (DEBUG_STOP_AT_STAGE >= 3 && DEBUG_STOP_AT_STAGE <= 18 && state == DEBUG_STOP_AT_STAGE) {
    debugStageStopActive = true;
  }

  if (state == 9) {
    // Requested: stage 9 starts by assuming far-left was the last active far sensor.
    stage9LastActiveFarSensor = FAR_SENSOR_LEFT;
  }

  postForcedStraightReleased = false;
  clearStage11_12BiasLatch();
  clearStage4FarLeftForceTurnLatch();
  clearStage5FarLeftForceTurnLatch();
  clearStage6FarLeftForceTurnLatch();
  clearStage11_12FarLeftForceTurnLatch();
  clearFarRightCorrection();
  clearSteerCommandDebounce();
}

float getMissionCruisePower(int intervalState)
{
  // Default interval speed is fast.
  // Requested exceptions:
  // - between 5 and 6  => interval state 5 => half
  // - between 9 and 10 => interval state 9 => half low
  // - between 14 and 15 => interval state 14 => half
  if (intervalState == 5) return POWER_HALF_HIGH;
  if (intervalState == 9) return POWER_HALF;
  // if (intervalState == 11) return POWER_HALF;
  if (intervalState == 12) return POWER_FULL_LOW;
  if (intervalState == 14) return POWER_HALF;
  if (intervalState == 17) return POWER_MAX;
  return POWER_FULL;
}

unsigned long getEntryTurnDurationMs(int state)
{
  // Keep 130 ms for stage 13.
  if (state == 13) {
    return ENTRY_TURN_DURATION_SHORT_MS;
  }

  // Keep 140 ms for stages 4, 5, 6.
  if (state == 4 || state == 5 || state == 6) {
    return ENTRY_TURN_DURATION_SHORTER_MS;
  }

  // Keep 150 ms for stages 11, 12, 15.
  if (state == 11 || state == 12 || state == 15) {
    return ENTRY_TURN_DURATION_MS;
  }

  // Keep 200 ms for stages 16.
  if (state == 16) {
    return ENTRY_TURN_DURATION_LONGER_MS;
  }

  // Remaining stages that need stage-entry turning use longer turning.
  return ENTRY_TURN_DURATION_LONG_MS;
}

void setForwardDirection()
{
  digitalWrite(pinL_DIR, HIGH);
  digitalWrite(pinR_DIR, HIGH);
}

void setBackwardDirection()
{
  digitalWrite(pinL_DIR, LOW);
  digitalWrite(pinR_DIR, LOW);
}

void setWheelPower(float leftPower, float rightPower)
{
  // Each power is a normalized command in [0.0, 1.0].
  // Right side uses multiplier-scaled range.
  float leftCmd = clampPower(leftPower);
  float rightCmd = clampPower(rightPower);

  int left = (int)(leftCmd * MAX_LEFT_PWM + 0.5);
  int right = (int)(rightCmd * MAX_LEFT_PWM * RIGHT_PWM_MULTIPLIER + 0.5);

  if (left < 0) left = 0;
  if (left > MAX_LEFT_PWM) left = MAX_LEFT_PWM;
  if (right < 0) right = 0;
  if (right > 255) right = 255;

  analogWrite(pinL_PWM, left);
  analogWrite(pinR_PWM, right);
}

void applyDirectionalCommandWithStability(int leftDir, int rightDir, bool stabilize)
{
  if (stabilize) {
    // Stability trick: precharge both direction lines HIGH, then apply target directions.
    digitalWrite(pinL_DIR, HIGH);
    digitalWrite(pinR_DIR, HIGH);
    digitalWrite(pinL_DIR, leftDir);
    digitalWrite(pinR_DIR, rightDir);
  }
  else {
    // No stability mode: apply target directions twice.
    digitalWrite(pinL_DIR, leftDir);
    digitalWrite(pinR_DIR, rightDir);
    digitalWrite(pinL_DIR, leftDir);
    digitalWrite(pinR_DIR, rightDir);
  }
}

void setSteerLeftForCruiseRaw(float cruisePower, bool stabilize, int thisDir)
{
  // Steering rule:
  // - cruise >= POWER_FULL: left wheel backward uses POWER_QUARTER.
  // - cruise >= POWER_HALF_LOW (but < POWER_FULL): left wheel backward uses POWER_MAX.
  // - otherwise: left wheel backward stays stopped.
  float backwardPower = (cruisePower >= POWER_FULL_LOW) ? POWER_QUARTER : (cruisePower >= POWER_HALF) ? POWER_HALF_LOW : (cruisePower >= POWER_HALF_LOW) ? POWER_HALF_LOW : POWER_STOP;

  applyDirectionalCommandWithStability(thisDir, HIGH, stabilize);
  setWheelPower(backwardPower, cruisePower);
}

void setSteerRightForCruiseRaw(float cruisePower, bool stabilize, int thisDir)
{
  // Steering rule:
  // - cruise >= POWER_FULL: right wheel backward uses POWER_QUARTER.
  // - cruise >= POWER_HALF_LOW (but < POWER_FULL): right wheel backward uses POWER_MAX.
  // - otherwise: right wheel backward stays stopped.
  float backwardPower = (cruisePower >= POWER_FULL_LOW) ? POWER_QUARTER : (cruisePower >= POWER_HALF) ? POWER_HALF_LOW : (cruisePower >= POWER_HALF_LOW) ? POWER_HALF_LOW : POWER_STOP;

  applyDirectionalCommandWithStability(HIGH, thisDir, stabilize);
  setWheelPower(cruisePower, backwardPower);
}

void setSteerStraightForCruiseRaw(float cruisePower, bool stabilize, int thisDir)
{
  applyDirectionalCommandWithStability(thisDir, thisDir, stabilize);
  setWheelPower(cruisePower, cruisePower);
}

void applySteerCommandRaw(int steerCmd, float cruisePower, bool stabilize, int thisDir)
{
  if (steerCmd == STEER_CMD_LEFT) {
    setSteerLeftForCruiseRaw(cruisePower, stabilize, thisDir);
  }
  else if (steerCmd == STEER_CMD_RIGHT) {
    setSteerRightForCruiseRaw(cruisePower, stabilize, thisDir);
  }
  else {
    setSteerStraightForCruiseRaw(cruisePower, stabilize, thisDir);
  }
}

void recordSteerChangeAndUpdateAdaptiveDebounce(unsigned long now)
{
  steerChangeTimes[steerChangeWriteIndex] = now;
  steerChangeWriteIndex = (steerChangeWriteIndex + 1) % STEER_CHANGE_HISTORY_COUNT;

  if (steerChangeCount < STEER_CHANGE_HISTORY_COUNT) {
    steerChangeCount++;
  }

  if (steerChangeCount == STEER_CHANGE_HISTORY_COUNT) {
    int oldestIndex = steerChangeWriteIndex;
    unsigned long oldestOfLastSeven = steerChangeTimes[oldestIndex];
    if ((now - oldestOfLastSeven) <= STEER_CHANGE_WINDOW_MS && !steerAdaptiveDebounceActive) {
      steerAdaptiveDebounceActive = true;
      steerAdaptiveDebounceStartMs = now;
      // Start a fresh short lock immediately under adaptive debounce mode.
      steerDebounceCmd = STEER_CMD_NONE;
      steerDebounceStartMs = 0;
    }
  }
}

void applySteerCommandDebounced(int requestedSteerCmd, float cruisePower, bool stabilize, int thisDir)
{
  unsigned long now = millis();

  if (steerAdaptiveDebounceActive && (now - steerAdaptiveDebounceStartMs) >= STEER_ADAPTIVE_DEBOUNCE_DURATION_MS) {
    steerAdaptiveDebounceActive = false;
  }

  if (steerLastRequestedCmd != STEER_CMD_NONE && requestedSteerCmd != steerLastRequestedCmd) {
    recordSteerChangeAndUpdateAdaptiveDebounce(now);
  }
  steerLastRequestedCmd = requestedSteerCmd;

  if (!steerAdaptiveDebounceActive) {
    // Default behavior: no debounce, apply requested command immediately.
    applySteerCommandRaw(requestedSteerCmd, cruisePower, stabilize, thisDir);
    return;
  }

  bool lockActive = (steerDebounceCmd != STEER_CMD_NONE) && ((now - steerDebounceStartMs) < STEER_COMMAND_DEBOUNCE_MS);

  if (lockActive && requestedSteerCmd != steerDebounceCmd) {
    // Keep forcing the previously selected steer function and its saved parameters
    // until debounce window ends.
    applySteerCommandRaw(steerDebounceCmd, steerDebounceCruisePower, steerDebounceStabilize, steerDebounceThisDir);
    return;
  }

  if (!lockActive || requestedSteerCmd != steerDebounceCmd) {
    steerDebounceCmd = requestedSteerCmd;
    steerDebounceStartMs = now;
    steerDebounceCruisePower = cruisePower;
    steerDebounceStabilize = stabilize;
    steerDebounceThisDir = thisDir;
  }

  applySteerCommandRaw(steerDebounceCmd, steerDebounceCruisePower, steerDebounceStabilize, steerDebounceThisDir);
}

void setSteerLeftForCruise(float cruisePower, bool stabilize, int thisDir = LOW)
{
  applySteerCommandDebounced(STEER_CMD_LEFT, cruisePower, stabilize, thisDir);
}

void setSteerRightForCruise(float cruisePower, bool stabilize, int thisDir = LOW)
{
  applySteerCommandDebounced(STEER_CMD_RIGHT, cruisePower, stabilize, thisDir);
}

void setSteerStraightForCruise(float cruisePower, bool stabilize, int thisDir = HIGH)
{
  applySteerCommandDebounced(STEER_CMD_STRAIGHT, cruisePower, stabilize, thisDir);
}

void setEntryTurnLeftAggressive(bool stabilize)
{
  // Aggressive stage-entry pivot for explicit decision points:
  // left wheel backward + right wheel forward
  applyDirectionalCommandWithStability(LOW, HIGH, false);
  setWheelPower(POWER_FULL, POWER_MAX);
}

void setEntryTurnRightAggressive(bool stabilize)
{
  // Aggressive stage-entry pivot for explicit decision points:
  // left wheel forward + right wheel backward
  applyDirectionalCommandWithStability(HIGH, LOW, false);
  setWheelPower(POWER_MAX, POWER_FULL);
}

void runLineTrackSimple(float cruisePower, int forcedTurn, bool stabilize, bool blockLeftSensorForSteering, bool blockRightSensorForSteering)
{
  refreshTrackingSensors();

  if (farRightSensor == 0) {
    farRightLastSeenMs = millis();
  }
  if (farLeftSensor == 0) {
    farLeftLastSeenMs = millis();
  }

  // Entry steering-bias method: block selected side sensor(s) for steering decisions only.
  int steerLeftSensor = blockLeftSensorForSteering ? 1 : leftSensor;
  int steerRightSensor = blockRightSensorForSteering ? 1 : rightSensor;

  // Optional forced entry-turn for mission decision points.
  // This keeps mode1 and mode2 on the same tracking function.
  if (forcedTurn == TURN_LEFT) {
    clearFarRightCorrection();
    clearSteerCommandDebounce();
    setEntryTurnLeftAggressive(stabilize);
    lastTurn = -1;
    return;
  }
  if (forcedTurn == TURN_RIGHT) {
    clearFarRightCorrection();
    clearSteerCommandDebounce();
    setEntryTurnRightAggressive(stabilize);
    lastTurn = 1;
    return;
  }

  if (currentState != 11 && currentState != 12) {
    clearStage11_12BiasLatch();
  }

  if (stage11_12BiasActive && (currentState == 11 || currentState == 12)) {
    if ((millis() - stage11_12BiasStartMs) < STAGE_11_12_BIAS_MIN_MS) {
      if (stage11_12BiasTurn == TURN_LEFT) {
        setSteerLeftForCruise(cruisePower, stabilize, HIGH);
        lastTurn = -1;
      }
      else if (stage11_12BiasTurn == TURN_RIGHT) {
        setSteerRightForCruise(cruisePower, stabilize, HIGH);
        lastTurn = 1;
      }
      return;
    }
    clearStage11_12BiasLatch();
  }

  if (currentState == 9) {
    // Stage 9: far-right override with latched correction window.
    bool allowStage9FarSensorDirectionChange = missionStateStarted
      && ((millis() - missionStateStartMs) >= scaledDurationMs(STAGE9_FAR_SENSOR_DIRECTION_LOCK_MS));
    if (allowStage9FarSensorDirectionChange) {
      if (farRightSensor == 0) {
        stage9LastActiveFarSensor = FAR_SENSOR_RIGHT;
      }
      else if (farLeftSensor == 0) {
        stage9LastActiveFarSensor = FAR_SENSOR_LEFT;
      }
    }

    if (farRightCorrectionActive) {
      if ((millis() - farRightCorrectionPostCenterStartMs) >= FAR_RIGHT_CORRECTION_POST_CENTER_MS) {
        clearFarRightCorrection();
      }

      if (farRightCorrectionActive) {
        if (farRightCorrectionTurn == TURN_RIGHT) {
          setSteerRightForCruise(cruisePower, stabilize);
          lastTurn = 1;
      }
        else {
          setSteerLeftForCruise(cruisePower, stabilize);
          lastTurn = -1;
        }
        return;
      }
    }

    bool farRightSeenRecently = (farRightLastSeenMs != 0)
      && ((millis() - farRightLastSeenMs) <= scaledDurationMs(FAR_RIGHT_RECENT_WINDOW_MS));
    if (farRightSeenRecently || (FAR_RIGHT_RECENT_WINDOW_MS == 0 && farRightSensor == 0)) {
      startFarRightCorrection(TURN_RIGHT);
      setSteerRightForCruise(cruisePower, stabilize);
      lastTurn = 1;
      return;
    }
    if (leftSensor == 1 && centerSensor == 1 && rightSensor == 1) {
      if (stage9LastActiveFarSensor == FAR_SENSOR_RIGHT) {
        startFarRightCorrection(TURN_RIGHT);
        setSteerRightForCruise(cruisePower, stabilize);
        lastTurn = 1;
      }
      else {
        // FAR_SENSOR_LEFT default also covers FAR_SENSOR_NONE fallback.
        startFarRightCorrection(TURN_LEFT);
        setSteerLeftForCruise(cruisePower, stabilize);
        lastTurn = -1;
      }
      return;
    }
  }
  else {
    clearFarRightCorrection();
  }

  // 0 = white line, 1 = dark background
  if (centerSensor == 0) {
    if (steerLeftSensor == 0 && steerRightSensor == 1) {
      setSteerLeftForCruise(cruisePower, stabilize);
      lastTurn = -1;
    }
    else if (steerLeftSensor == 1 && steerRightSensor == 0) {
      setSteerRightForCruise(cruisePower, stabilize);
      lastTurn = 1;
    }
    else {
      /*
      // Requested stage-specific bias when both near sensors detect white.
      if (currentState == 12) {
        startStage11_12BiasLatch(TURN_LEFT);
        setSteerLeftForCruise(cruisePower, stabilize, HIGH);
        lastTurn = -1;
        return;
      }
      if (currentState == 11) {
        startStage11_12BiasLatch(TURN_RIGHT);
        setSteerRightForCruise(cruisePower, stabilize, HIGH);
        lastTurn = 1;
        return;
      }
      */
      setSteerStraightForCruise(cruisePower, true);
      // keep lastTurn memory while centered to avoid introducing turn bias
    }
  }
  else {
    if (steerLeftSensor == 0 && steerRightSensor == 1) {
      setSteerLeftForCruise(cruisePower, stabilize);
      lastTurn = -1;
    }
    else if (steerLeftSensor == 1 && steerRightSensor == 0) {
      setSteerRightForCruise(cruisePower, stabilize);
      lastTurn = 1;
    }
    else {
      // search by last known direction using cruise-dependent steering rule
      // Requested stage-specific bias when both near sensors detect white.
      /*
      if (currentState == 12) {
        startStage11_12BiasLatch(TURN_LEFT);
        setSteerLeftForCruise(cruisePower, stabilize);
        lastTurn = -1;
        return;
      }
      if (currentState == 11) {
        startStage11_12BiasLatch(TURN_RIGHT);
        setSteerRightForCruise(cruisePower, stabilize);
        lastTurn = 1;
        return;
      }
      */
      // Stage 14 override: when side is ambiguous, ignore lastTurn and go left.
      if (currentState == 14) {
        setSteerLeftForCruise(cruisePower, stabilize);
        lastTurn = -1;
      }
      else if (lastTurn < 0) {
        bool forceLeft = (currentState == 5) && missionStateStarted && ((millis() - missionStateStartMs) >= scaledDurationMs(1500));
        bool noReverse = (currentState == 13 || currentState == 13 || currentState == 16) && missionStateStarted && ((millis() - missionStateStartMs) <= scaledDurationMs(625));
        if (forceLeft || noReverse) {
          setSteerLeftForCruise(cruisePower, stabilize);
        }
        else {
          // Reverse
          setSteerRightForCruise(cruisePower, stabilize);
        }
      }
      else if (lastTurn > 0) {
        bool forceLeft = (currentState == 5) && missionStateStarted && ((millis() - missionStateStartMs) >= scaledDurationMs(1500));
        bool noReverse = (currentState == 13 || currentState == 13 || currentState == 16) && missionStateStarted && ((millis() - missionStateStartMs) <= scaledDurationMs(625));
        if (!forceLeft && noReverse) {
          setSteerRightForCruise(cruisePower, stabilize);
        }
        else {
          // Reverse
          setSteerLeftForCruise(cruisePower, stabilize);
        }
      }
      else {
        // startup/unknown case: avoid hard left bias, keep tracking forward
        setSteerStraightForCruise(cruisePower, true);
      }
    }
  }
}

bool transitionConditionMet(int state)
{
  int cond = INTERVAL_TRANSITION_CONDITION[state];
  if (cond == COND_TIME_ONLY) {
    return true;
  }

  refreshTrackingSensors();
  bumperSensor = readBinaryStable(pinB_Sensor);
  if (cond == COND_CENTER_ON_WHITE) {
    return (centerSensor == 0);
  }
  if (cond == COND_JUNCTION_WHITE) {
    // requested: left and right sensors both white (junction)
    return (leftSensor == 0 && rightSensor == 0) || farLeftSensor == 0 || farRightSensor == 0;
  }
  if (cond == COND_JUNCTION_WHITE_STRICT) {
    // requested: left and right sensors both white (junction)
    return (leftSensor == 0 && rightSensor == 0) || (farLeftSensor == 0 && farRightSensor == 0);
  }
  if (cond == COND_BUMPER_ON_WHITE) {
    return (bumperSensor == 0);
  }
  if (cond == COND_STAGE9_TO_11_WHITE_PATTERN) {
    // requested special transition for 9 -> 11 path:
    // require far-right white AND (center white OR right white)
    if (farRightSensor == 0) return true;
    if ((millis() - farRightLastSeenMs) < COND_STAGE_TO_11_FAR_RIGHT_LAST_SEEN_AT_LEAST_MS) return false;
    if ((millis() - farLeftLastSeenMs) < COND_STAGE_TO_11_FAR_LEFT_LAST_SEEN_AT_LEAST_MS) return false;
    return (leftSensor == 0 && rightSensor == 0) || farLeftSensor == 0;
  }
  if (cond == COND_STAGE6_TO_7_JUNCTION_WHITE) {
    // stage 7: near side sensors OR far right sensors
    // theory: if too fast, likely means the car is straight on
    // left-side sensors: near-left, far-left
    // right-side sensors: near-right, far-right
    return (leftSensor == 0 && rightSensor == 0) || farRightSensor == 0;
  }
  if (cond == COND_STAGE7_SIDE_ANY_WHITE) {
    // stage 7: near side sensors OR far right sensors
    // theory: if too fast, likely means the car is straight on
    // left-side sensors: near-left, far-left
    // right-side sensors: near-right, far-right
    return (leftSensor == 0 && rightSensor == 0) || (farLeftSensor == 0 || farRightSensor == 0);
  }
  if (cond == COND_STAGE7_SIDE_ANY_WHITE_STRICT) {
    // stage 7: near side sensors OR far right sensors
    // theory: if too fast, likely means the car is straight on
    // left-side sensors: near-left, far-left
    // right-side sensors: near-right, far-right
    return (leftSensor == 0 && rightSensor == 0) || (farLeftSensor == 0 && farRightSensor == 0);
  }
  if (cond == COND_STAGE14_TO_15_FAR_RIGHT) {
    // stage 14 -> 15: use far-right sensor confirmation.
    return (farRightSensor == 0);
  }
  if (cond == COND_LEFT_ON_WHITE) {
    return (farLeftSensor == 0);
  }
  if (cond == COND_STAGE11_TO_12_JUNCTION_WHITE) {
    // requested: left and right sensors both white (junction), or far right sensor white, or far left sensor white
    return (leftSensor == 0 && rightSensor == 0) || farRightSensor == 0 || farLeftSensor == 0;
  }

  return true;
}

void runMissionMode()
{
  if (!missionStateStarted) {
    missionStateStarted = true;
    debugStageStopActive = false;
    currentState = DEBUG_START_AT_STAGE;
    missionStateStartMs = millis();
    lastMissionState = currentState;
    onMissionStateEnter(currentState);
  }

  if (currentState < 3 || currentState > 18) {
    currentState = 3;
    missionStateStartMs = millis();
    lastMissionState = currentState;
    onMissionStateEnter(currentState);
  }

  if (currentState != lastMissionState) {
    onMissionStateEnter(currentState);
    lastMissionState = currentState;
  }

  if (debugStageStopActive) {
    setForwardDirection();
    setWheelPower(POWER_STOP, POWER_STOP);
    return;
  }

  int action = STATE_ACTION[currentState];
  unsigned long elapsedInState = millis() - missionStateStartMs;

  if (action == ACT_STOP) {
    if (currentState == 18 && elapsedInState < scaledDurationMs(STAGE18_BACKWARD_HOLD_MS)) {
      // Stage 18: continue forced backward full power briefly before final stop.
      setBackwardDirection();
      setWheelPower(POWER_MAX, POWER_MAX);
    }
    else {
      setForwardDirection();
      setForwardDirection();
      setWheelPower(POWER_STOP, POWER_STOP);
    }
  }
  else if (action == ACT_LINE_TRACK) {
    float cruise = getMissionCruisePower(currentState);
    int entryTurn = STAGE_ENTRY_TURN[currentState];
    bool useEntrySensorBlockMethod = currentState == 11 || currentState == 12;

    bool blockLeftSensorForSteering = false;
    bool blockRightSensorForSteering = false;
    if (useEntrySensorBlockMethod
    && ((currentState == 11 && elapsedInState < scaledDurationMs(ENTRY_SENSOR_STEER_BLOCK_MS))
    || (currentState == 12 && elapsedInState < scaledDurationMs(ENTRY_SENSOR_STEER_BLOCK_LONG_MS)))) {
      if (entryTurn == TURN_LEFT) {
        // force-left by blocking right sensor from steering logic
        blockRightSensorForSteering = true;
      }
      else if (entryTurn == TURN_RIGHT) {
        // force-right by blocking left sensor from steering logic
        blockLeftSensorForSteering = true;
      }
    }

    if (useEntrySensorBlockMethod) {
      // requested for transitions into 11: no aggressive forced-turn pulse.
      entryTurn = TURN_NONE;
    }

    unsigned long entryTurnDur = scaledDurationMs(getEntryTurnDurationMs(currentState));
    unsigned long distractBlockDur = scaledDurationMs(currentState == 13 || currentState == 16 ? POST_FORCED_TURN_DISTRACT_BLOCK_SHORT_MS : currentState == 15 ? POST_FORCED_TURN_DISTRACT_BLOCK_LONG_MS : POST_FORCED_TURN_DISTRACT_BLOCK_MS);
    unsigned long maxStraightBlockDur = scaledDurationMs(POST_FORCED_TURN_MAX_BLOCK_MS);
    unsigned long fixedStage9BlockDur = scaledDurationMs(POST_FORCED_TURN_SINCE_STAGE_9_BLOCK_MS);
    unsigned long fixedStage10PlusBlockDur = scaledDurationMs(POST_FORCED_TURN_SINCE_STAGE_BLOCK_MS);
    bool stabilize = (elapsedInState < entryTurnDur || (currentState != 5 && currentState != 9 && currentState != 11 && currentState != 12 && currentState != 14));

    int forcedTurn = TURN_NONE;
    if (entryTurn != TURN_NONE && elapsedInState < entryTurnDur) {
      forcedTurn = entryTurn;
    }

    // Stage 4 special rule:
    // If far-left sensor detects white, force a left rotation for 75 ms.
    if (currentState == 4) {
      if (!stage4FarLeftForceTurnActive) {
        refreshTrackingSensors();
        if (farLeftSensor == 0) {
          startStage4FarLeftForceTurnLatch();
        }
      }

      if (stage4FarLeftForceTurnActive) {
        if ((millis() - stage4FarLeftForceTurnStartMs) < scaledDurationMs(STAGE4_FAR_LEFT_FORCE_TURN_MS)) {
          forcedTurn = TURN_LEFT;
        }
        else {
          clearStage4FarLeftForceTurnLatch();
        }
      }
    }

    // Stage 5 special rule:
    // After stage-5 minimum transition time is reached, if far-left sensor detects white,
    // force a left turn for 75 ms.
    if (currentState == 5 && elapsedInState >= scaledDurationMs(INTERVAL_MIN_DURATION_MS[5])) {
      if (!stage5FarLeftForceTurnActive) {
        refreshTrackingSensors();
        if (farLeftSensor == 0) {
          startStage5FarLeftForceTurnLatch();
        }
      }

      if (stage5FarLeftForceTurnActive) {
        if ((millis() - stage5FarLeftForceTurnStartMs) < scaledDurationMs(STAGE5_FAR_LEFT_FORCE_TURN_MS)) {
          forcedTurn = TURN_LEFT;
        }
        else {
          clearStage5FarLeftForceTurnLatch();
        }
      }
    }

    bool blockOppositeSteeringAfterTurn = false;
    if (entryTurn != TURN_NONE && elapsedInState >= entryTurnDur && !postForcedStraightReleased) {
      if (currentState >= 9) {
        // Requested: from stage 9 onward, use fixed post-turn blocking only
        // (no sensor-based release).
        if (elapsedInState < (entryTurnDur + (currentState == 9 ? fixedStage9BlockDur : fixedStage10PlusBlockDur))) {
          blockOppositeSteeringAfterTurn = true;
        }
        else {
          postForcedStraightReleased = true;
        }
      }
      else {
        if (elapsedInState >= (entryTurnDur + maxStraightBlockDur)) {
          // Hard cap: must release after max post-turn straight-block duration.
          postForcedStraightReleased = true;
        }
        else if (elapsedInState < (entryTurnDur + distractBlockDur)) {
          blockOppositeSteeringAfterTurn = true;
        }
        else {
          refreshTrackingSensors();
          bool releaseFromStraightBlock = false;
          if (entryTurn == TURN_LEFT) {
            // (center white AND same-side near sensor white) OR same-side far sensor white
            releaseFromStraightBlock = (centerSensor == 0 && leftSensor == 0) || farLeftSensor == 0;
          }
          else if (entryTurn == TURN_RIGHT) {
            // symmetric condition for right forced turn
            releaseFromStraightBlock = (centerSensor == 0 && rightSensor == 0) || farRightSensor == 0;
          }
          else {
            releaseFromStraightBlock = true;
          }

          if (releaseFromStraightBlock) {
            postForcedStraightReleased = true;
          }
          else {
            blockOppositeSteeringAfterTurn = true;
          }
        }
      }
    }

    if (blockOppositeSteeringAfterTurn) {
      clearFarRightCorrection();
      // Keep line-tracking active, but prevent steering opposite to the entry turn.
      if (entryTurn == TURN_LEFT) {
        blockRightSensorForSteering = true;
      }
      else if (entryTurn == TURN_RIGHT) {
        blockLeftSensorForSteering = true;
      }
    }

    // Stage 6 special rule:
    // After stage-entry forced-turn and post-turn blocking have expired,
    // if far-left sensor detects white, force a left turn for 75 ms.
    if (currentState == 6) {
      bool stage6PostEntryWindowOpen = (forcedTurn == TURN_NONE) && !blockOppositeSteeringAfterTurn;
      if (!stage6FarLeftForceTurnActive && stage6PostEntryWindowOpen) {
        refreshTrackingSensors();
        if (farLeftSensor == 0) {
          startStage6FarLeftForceTurnLatch();
        }
      }

      if (stage6FarLeftForceTurnActive) {
        if ((millis() - stage6FarLeftForceTurnStartMs) < scaledDurationMs(STAGE6_FAR_LEFT_FORCE_TURN_MS)) {
          forcedTurn = TURN_LEFT;
        }
        else {
          clearStage6FarLeftForceTurnLatch();
        }
      }
    }

    // Stage 11/12 special rule:
    // For stage 11: After the stage's minimum transition time is reached,
    // For stage 12: Anytime in stage 12,
    // if far-left sensor detects white, force a left turn for 75 ms.
    if ((currentState == 11 && elapsedInState >= scaledDurationMs(INTERVAL_MIN_DURATION_MS[currentState]))
        || currentState == 12) {
      if (!stage11_12FarLeftForceTurnActive) {
        refreshTrackingSensors();
        if (farLeftSensor == 0) {
          startStage11_12FarLeftForceTurnLatch();
        }
      }

      if (stage11_12FarLeftForceTurnActive) {
        if ((millis() - stage11_12FarLeftForceTurnStartMs) < scaledDurationMs(STAGE11_12_FAR_LEFT_FORCE_TURN_MS)) {
          forcedTurn = TURN_LEFT;
        }
        else {
          clearStage11_12FarLeftForceTurnLatch();
        }
      }
    }

    // Stage 11 rule: once min transition time + 200 ms is reached, block right steering
    // for the remainder of the stage by masking the right steering sensor.
    if (currentState == 11 && elapsedInState >= scaledDurationMs(INTERVAL_MIN_DURATION_MS[11] + STAGE_11_ADDITIONAL_LEEWAY_DURATION)) {
      blockRightSensorForSteering = true;
    }

    runLineTrackSimple(cruise, forcedTurn, stabilize, blockLeftSensorForSteering, blockRightSensorForSteering);
  }
  else if (action == ACT_SPIN_360_RIGHT) {
    digitalWrite(pinL_DIR, HIGH);
    digitalWrite(pinR_DIR, LOW);
    setWheelPower(POWER_MAX, POWER_MAX);   // rotation always full
    lastTurn = 1;
  }
  else if (action == ACT_BACKWARD_FAST) {
    // Stage 17: pure reverse motion.
    setBackwardDirection();
    setWheelPower(POWER_MAX, POWER_MAX);
  }
  else {
    setForwardDirection();
    setWheelPower(POWER_STOP, POWER_STOP);
  }

  // State transition logic based on relative duration from last stage change
  if (currentState >= 18) {
    return;
  }

  unsigned long minDur = scaledDurationMs(INTERVAL_MIN_DURATION_MS[currentState]);
  unsigned long maxDur = scaledDurationMs(INTERVAL_MAX_DURATION_MS[currentState]);

  if (elapsedInState < minDur) {
    return;
  }

  int cond = INTERVAL_TRANSITION_CONDITION[currentState];
  bool shouldAdvance = transitionConditionMet(currentState);
  if (!shouldAdvance && maxDur > 0 && elapsedInState >= maxDur) {
    shouldAdvance = true;
  }

  if (shouldAdvance) {
    currentState = currentState + 1;
    if (currentState > 18) {
      currentState = 18;
    }

    // Cleanly skip zero-time dummy states (e.g., stage 10) without executing them.
    while (currentState < 18 &&
           INTERVAL_MIN_DURATION_MS[currentState] == 0 &&
           INTERVAL_MAX_DURATION_MS[currentState] == 0 &&
           INTERVAL_TRANSITION_CONDITION[currentState] == COND_TIME_ONLY &&
           STATE_ACTION[currentState] == ACT_STOP) {
      currentState = currentState + 1;
    }

    missionStateStartMs = millis();
  }
}

// the setup function runs once when you press reset or power the board

void setup ()
{
  // define pins as input and output
  pinMode(pinL_Sensor, INPUT);
  pinMode(pinB_Sensor, INPUT);
  pinMode(pinC_Sensor, INPUT);
  pinMode(pinR_Sensor, INPUT);
  pinMode(pinFR_Sensor, INPUT);
  pinMode(pinFL_Sensor, INPUT);

  pinMode(pinL_DIR, OUTPUT);
  pinMode(pinR_DIR, OUTPUT);

  pinMode(pinL_PWM, OUTPUT);
  pinMode(pinR_PWM, OUTPUT);

  // initialize output pins
  setForwardDirection();
  setWheelPower(0.0, 0.0);

  // record bumper baseline at boot (later compared after start-line arming)
  bumperBootState = readBinaryStable(pinB_Sensor);
  delay(300);
}

// the loop function runs over and over again forever

void loop() {
  // startup sequence:
  // 1) place car so all three tracking sensors are on start white line (arm)
  // 2) toggle bumper once to start the task
  if (!hasStarted) {
    setWheelPower(0.0, 0.0);

    // Step 1: arm only when all three tracking sensors stably detect white
    if (!startLineArmed) {
      refreshTrackingSensors();
      if (areAllTrackingSensorsOnWhite()) {
        if (startLineSeenSinceMs == 0) {
          startLineSeenSinceMs = millis();
        }
        if ((millis() - startLineSeenSinceMs) >= START_LINE_CONFIRM_MS) {
          startLineArmed = true;
          // capture bumper baseline at arming moment
          bumperBootState = readBinaryStable(pinB_Sensor);
        }
      } else {
        startLineSeenSinceMs = 0;
      }
      return;
    }

    // Step 2: after armed, wait for bumper toggle to start
    bumperSensor = readBinaryStable(pinB_Sensor);
    if (bumperSensor != bumperBootState) {
      hasStarted = true;
      delay(120);  // debounce/settle after start trigger
    }
    return;
  }

  // mode 0: constant PWM test
  if (RUN_MODE == MODE_CONSTANT_PWM) {
    setForwardDirection();
    setWheelPower(CONSTANT_MODE_POWER, CONSTANT_MODE_POWER);
    return;
  }

  // mode 1: simple line tracking
  if (RUN_MODE == MODE_LINE_TRACK) {
    setForwardDirection();
    runLineTrackSimple(POWER_FULL, TURN_NONE, true, false, false);
    return;
  }

  // mode 2: mission mode for full project task
  if (RUN_MODE == MODE_MISSION_TASK) {
    runMissionMode();
    return;
  }

  // safety fallback
  setForwardDirection();
  setWheelPower(POWER_STOP, POWER_STOP);
}
