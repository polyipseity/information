const int pinL_PWM = 9;             //pin D9
const int pinR_PWM = 11;            //pin D11

void setup()
{
  pinMode(pinL_PWM, OUTPUT);
  pinMode(pinR_PWM, OUTPUT);
}

void loop()
{
  analogWrite(pinL_PWM, 200);
  analogWrite(pinR_PWM, 100);
}
