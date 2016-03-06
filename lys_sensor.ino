  int led = 11;
  int ldr = 0;
  int ldrVerdi = 0;
  void setup() {
      pinMode(led, OUTPUT);
      pinMode(ldr, INPUT);
      Serial.begin(9600);
  }

  void loop() {
      ldrVerdi = analogRead(ldr);
      Serial.println(ldrVerdi);
      analogWrite(led, map(ldrVerdi, (0), (1023), (0), (255)));
      delay(500);
  }
