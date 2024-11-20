// Pin definitions for the HC-SR04 ultrasonic sensor
#define TRIG_PIN 9
#define ECHO_PIN 10

// Variables to store duration and distance
long duration;
float distance;

void setup() {
  Serial.begin(9600);  // Start serial communication
  pinMode(TRIG_PIN, OUTPUT);  // Set the Trigger pin as output
  pinMode(ECHO_PIN, INPUT);   // Set the Echo pin as input
  Serial.println("Distance Measurement Using HC-SR04");
  delay(2000);  // Allow the system to settle
}

void loop() {
  // Send a pulse to the trigger pin
  digitalWrite(TRIG_PIN, LOW);  // Ensure the Trigger pin is LOW
  delayMicroseconds(2);         // Wait for a short period
  digitalWrite(TRIG_PIN, HIGH); // Send a 10µs HIGH pulse to trigger the sensor
  delayMicroseconds(10);        
  digitalWrite(TRIG_PIN, LOW);  // Set the trigger pin back to LOW
  
  // Measure the time taken for the Echo to return
  duration = pulseIn(ECHO_PIN, HIGH);  // Read the duration of the pulse

  // Calculate the distance based on the duration
  distance = (duration * 0.0344) / 2;  // Speed of sound is 0.0344 cm/µs

  // Log the data
  Serial.print("Distance: ");
  Serial.print(distance);  // Display the measured distance
  Serial.println(" cm");

  // Optional: Log actual distance from a known reference to compare
  // Example: "Observed Distance: 150 cm"
  float observedDistance = 150.0;  // Actual reference distance for comparison
  Serial.print("Actual Distance: ");
  Serial.print(observedDistance);
  Serial.print(" cm\t");

  Serial.print("Measured Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Log both the actual and observed values (This can be expanded with more values over time)
  Serial.println("-----------");

  // Wait a moment before the next measurement
  delay(1000);  // Wait 1 second before the next measurement
}



<!-- VCC → 5V
GND → GND
Trig → Pin 9
Echo → Pin 10 -->