#include <Stepper.h>

const int stepsPerRevolution = 200;
Stepper myStepper(stepsPerRevolution);

void setup() 
{
  myStepper.setSpeed(60);
}

void loop() 
{
  myStepper.step(stepsPerRevolution);
  delay(1000);
  myStepper.step(-stepsPerRevolution);
  delay(1000);
}