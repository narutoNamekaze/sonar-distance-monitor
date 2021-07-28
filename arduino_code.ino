#include <HCSR04.h>

HCSR04 hc(8, 7);

void setup() {
  Serial.begin(9600);
}

void loop() {
  float distance = hc.dist();
  Serial.println((int) distance);
  delay(1000);
}
