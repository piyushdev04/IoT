// Define the pin for the soil moisture sensor
#define MOISTURE_SENSOR_PIN A0  // Analog pin A0

void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
}

void loop() {
  // Read the analog value from the sensor
  int sensorValue = analogRead(MOISTURE_SENSOR_PIN);
  
  // Print the sensor value to the Serial Monitor
  Serial.print("Soil Moisture Level: ");
  Serial.println(sensorValue);  // The value will range from 0 (wet) to 1023 (dry)
  
  // Wait for a short period before reading again
  delay(1000);  // Delay for 1 second
}

<!-- 
VCC → 5V
GND → GND
A0 → A0 -->