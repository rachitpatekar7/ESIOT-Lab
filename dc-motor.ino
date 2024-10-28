int motorPin = 9;

void setup() 
{
  pinMode(motorPin, OUTPUT);
}

void loop() 
{
  analogWrite(motorPin, 255);
  delay(2000);
  analogWrite(motorPin, 0);
  delay(2000);
}
