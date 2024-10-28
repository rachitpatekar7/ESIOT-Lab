#include <Servo.h>

Servo myServo;

void setup()
{
  myServo.attach(9);
}

void loop() 
{
  for (int angle = 0; angle <= 180; angle += 20) 
  {
    myServo.write(angle);
    delay(500);
  }
  for (int angle = 180; angle >= 0; angle -= 20) 
  {
    myServo.write(angle);
    delay(500);
  }
}
