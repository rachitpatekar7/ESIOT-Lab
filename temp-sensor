int buzzer = 7;
float voltage;

void setup() 
{
  pinMode(10, OUTPUT);
  pinMode(7, OUTPUT);
  Serial.begin(9600);
}

void loop() 
{
  float a = analogRead(A0);
  voltage = analogRead(A0) * 0.004882814;
  float temp = (voltage - 0.5) * 100.0;

  if (temp > 10) {
    digitalWrite(10, HIGH);
    tone(buzzer, 600);
  } else {
    digitalWrite(10, LOW);
    noTone(buzzer);
  }

  Serial.print("TEMPERATURE = ");
  Serial.print(temp);
  Serial.print("*C");
  delay(500);
  Serial.println();
}
