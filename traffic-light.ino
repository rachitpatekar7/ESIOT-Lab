int redLight = 13;
int yellowLight = 12;
int greenLight = 11;

void setup() 
{
  pinMode(redLight, OUTPUT);
  pinMode(yellowLight, OUTPUT);
  pinMode(greenLight, OUTPUT);
}

void loop() 
{
  digitalWrite(redLight, HIGH);
  digitalWrite(yellowLight, LOW);
  digitalWrite(greenLight, LOW);
  delay(5000);

  digitalWrite(redLight, LOW);
  digitalWrite(yellowLight, HIGH);
  digitalWrite(greenLight, LOW);
  delay(2000);

  digitalWrite(redLight, LOW);
  digitalWrite(yellowLight, LOW);
  digitalWrite(greenLight, HIGH);
  delay(5000);

  digitalWrite(redLight, LOW);
  digitalWrite(yellowLight, HIGH);
  digitalWrite(greenLight, LOW);
  delay(2000);
}
