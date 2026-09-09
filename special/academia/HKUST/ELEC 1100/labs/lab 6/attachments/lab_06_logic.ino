/*
  ELEC1100 Your Lab#06 & Project Template

  To program the car tracking the white line on a dark mat

  Group No. (number of your project box):
  Group Member 1 (name & SID):
  Group Member 2 (name & SID):

*/

// assign meaningful names to those pins that will be used

const int pinL_Sensor = A5;      //pin A5: left sensor
const int pinB_Sensor = A4;      //pin A4: bumper sensor
const int pinR_Sensor = A3;      //pin A3: right sensor

const int pinL_PWM = 9;          //pin D9: left motor speed
const int pinL_DIR = 10;         //pin D10: left motor direction

const int pinR_PWM = 11;         //pin D11: right motor speed
const int pinR_DIR = 12;         //pin D12: right motor direction

//define variables to be used in script

int bumperSensor = 1;  // not sensing white
int leftSensor = 1;    // not sensing white
int rightSensor = 1;   // not sensing white

int countBumper = 0;   // bumper sensor not triggered yet

// the setup function runs once when you press reset or power the board

void setup ()
{
  // define pins as input and output
  pinMode(pinB_Sensor, INPUT);
  pinMode(pinL_Sensor, INPUT);
  pinMode(pinR_Sensor, INPUT);

  pinMode(pinL_DIR, OUTPUT);
  pinMode(pinR_DIR, OUTPUT);

  pinMode(pinL_PWM, OUTPUT);
  pinMode(pinR_PWM, OUTPUT);

  // initialize output pins
  digitalWrite(pinL_DIR, HIGH);   //forward direction
  digitalWrite(pinR_DIR, HIGH);   //forward direction
  analogWrite(pinL_PWM, 0);       //stop at the start position
  analogWrite(pinR_PWM, 0);       //stop at the start position
}

// the loop function runs over and over again forever

void loop() {

  // Arduino is reading the sensor measurements
  bumperSensor = digitalRead(pinB_Sensor);
  leftSensor = digitalRead(pinL_Sensor);
  rightSensor = digitalRead(pinR_Sensor);

  // car stops at the start position when bumper sensor no trigger
  if ( bumperSensor && countBumper == 0 ) {
    analogWrite(pinL_PWM, ???);
    analogWrite(pinR_PWM, ???);
  }

  // bumper sensor is triggered at the start position for the 1st time
  else if ( !bumperSensor && countBumper == 0) {
    analogWrite(pinL_PWM, ???);
    analogWrite(pinR_PWM, ???);
    countBumper = countBumper + 1;
    delay(350);     //to let the car leave the start position with no miscount
  }

  // car is tracking on the white line
  else if ( bumperSensor && countBumper == 1)
  {
    if ( !leftSensor && !rightSensor ) {
        analogWrite(pinL_PWM, ???);
        analogWrite(pinR_PWM, ???);
        digitalWrite(pinL_DIR, ???);
        digitalWrite(pinR_DIR, ???);
      }

    if ( !leftSensor && rightSensor ) {
        analogWrite(pinL_PWM, ???);
        analogWrite(pinR_PWM, ???);
        digitalWrite(pinL_DIR, ???);
        digitalWrite(pinR_DIR, ???);
      }

    if ( leftSensor && !rightSensor ) {
        analogWrite(pinL_PWM, ???);
        analogWrite(pinR_PWM, ???);
        digitalWrite(pinL_DIR, ???);
        digitalWrite(pinR_DIR, ???);
      }

    if ( leftSensor && rightSensor ) {
        analogWrite(pinL_PWM, ???);
        analogWrite(pinR_PWM, ???);
        digitalWrite(pinL_DIR, ???);
        digitalWrite(pinR_DIR, ???);
      }
  }
}
