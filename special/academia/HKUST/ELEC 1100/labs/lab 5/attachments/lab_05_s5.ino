/*
  ELEC1100 Lab#05

  Use sensors to control the motors rotation

*/

// assign meaningful names to those pins that will be used
const int pinL_Sensor = A5;      //pin A5
const int pinR_Sensor = A3;      //pin A3

const int pinL_PWM = 9;          //pin D9
const int pinL_DIR = 10;         //pin D10

const int pinR_PWM = 11;         //pin D11
const int pinR_DIR = 12;         //pin D12

//define variables to be used in script
int leftSensor = 1;
int rightSensor = 1;

// the setup function runs once when you press reset or power the board

void setup ()
{
  // define pins as input and output
  pinMode(pinL_Sensor, INPUT);
  pinMode(pinR_Sensor, INPUT);

  pinMode(pinL_DIR, OUTPUT);
  pinMode(pinR_DIR, OUTPUT);

  pinMode(pinL_PWM, OUTPUT);
  pinMode(pinR_PWM, OUTPUT);

  // initialize output pins
  digitalWrite(pinL_DIR, HIGH);   //forward direction
  digitalWrite(pinR_DIR, HIGH);   //forward direction
  analogWrite(pinL_PWM, 200);    //forward speed
  analogWrite(pinR_PWM, 200);    //forward speed
}

// the loop function runs over and over again forever
void loop() {

  leftSensor = digitalRead(pinL_Sensor);
  rightSensor = digitalRead(pinR_Sensor);

  if ( leftSensor ) {
    digitalWrite(pinL_DIR, HIGH);
  }

  if ( !leftSensor ) {
    digitalWrite(pinL_DIR, LOW);
  }

  if ( rightSensor ) {
    digitalWrite(pinR_DIR, HIGH);
  }

  if ( !rightSensor ) {
    digitalWrite(pinR_DIR, LOW);
  }

}
