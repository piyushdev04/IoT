// Pin definitions for each direction
const int lights[4][3] = {
  {2, 3, 4},  // North: Red, Yellow, Green
  {5, 6, 7},  // South: Red, Yellow, Green
  {8, 9, 10}, // East: Red, Yellow, Green
  {11, 12, 13} // West: Red, Yellow, Green
};

// Timing constants (in milliseconds)
const unsigned long greenTime = 50000; // Green light duration
const unsigned long yellowTime = 7000; // Yellow light duration
const unsigned long redTime = 35000;   // Red light duration

void setup() {
  // Set all light pins as outputs
  for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 3; j++) {
      pinMode(lights[i][j], OUTPUT);
    }
  }
}

void loop() {
  // North-South Green, East-West Red
  setLights(0, HIGH, LOW, LOW); // North
  setLights(1, HIGH, LOW, LOW); // South
  setLights(2, LOW, LOW, HIGH); // East
  setLights(3, LOW, LOW, HIGH); // West
  delay(greenTime);

  setLights(0, LOW, HIGH, LOW); // North
  setLights(1, LOW, HIGH, LOW); // South
  delay(yellowTime);

  setLights(0, LOW, LOW, HIGH); // North
  setLights(1, LOW, LOW, HIGH); // South
  setLights(2, HIGH, LOW, LOW); // East
  setLights(3, HIGH, LOW, LOW); // West
  delay(redTime);

  // East-West Green, North-South Red
  setLights(0, HIGH, LOW, LOW); // North
  setLights(1, HIGH, LOW, LOW); // South
  setLights(2, HIGH, LOW, LOW); // East
  setLights(3, HIGH, LOW, LOW); // West
  delay(greenTime);

  setLights(2, LOW, HIGH, LOW); // East
  setLights(3, LOW, HIGH, LOW); // West
  delay(yellowTime);
}

// Function to set light states for a direction
void setLights(int direction, int redState, int yellowState, int greenState) {
  digitalWrite(lights[direction][0], redState);
  digitalWrite(lights[direction][1], yellowState);
  digitalWrite(lights[direction][2], greenState);
}