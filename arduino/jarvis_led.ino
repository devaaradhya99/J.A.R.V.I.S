void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);

  digitalWrite(13, LOW);
  digitalWrite(12, LOW);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();

    if (c == '1') {
      digitalWrite(13, HIGH);
      digitalWrite(12, LOW);
    }
    else if (c == '0') {
      digitalWrite(13, LOW);
      digitalWrite(12, LOW);
    }
    else if (c == '2') {
      for (int i = 0; i < 3; i++) {
        digitalWrite(12, HIGH);
        delay(200);
        digitalWrite(12, LOW);
        delay(200);
      }
    }
  }
}
