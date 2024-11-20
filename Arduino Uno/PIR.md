// Pin definitions
#define PIR_SENSOR_PIN 2  // Pin connected to the PIR sensor's OUT pin
#define LED_PIN 13        // Pin connected to the LED

void setup() {
  pinMode(PIR_SENSOR_PIN, INPUT);  // Set PIR sensor pin as input
  pinMode(LED_PIN, OUTPUT);        // Set LED pin as output
  
  Serial.begin(9600);  // Start serial communication for debugging
  Serial.println("PIR Motion Sensor - Motion Detection");
}

void loop() {
  int pirState = digitalRead(PIR_SENSOR_PIN);  // Read the PIR sensor's output

  if (pirState == HIGH) {  // Motion detected
    digitalWrite(LED_PIN, HIGH);  // Turn on the LED
    Serial.println("Motion Detected!");
  } else {  // No motion
    digitalWrite(LED_PIN, LOW);  // Turn off the LED
    Serial.println("No Motion");
  }

  delay(500);  // Small delay to avoid serial flooding
}

<!-- VCC → 5V
GND → GND
OUT → Pin 2

Anode (long leg) → Pin 13
Cathode (short leg) → GND -->