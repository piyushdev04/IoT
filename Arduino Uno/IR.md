#include <TM1637Display.h>

// Pin definitions for the IR sensor and TM1637 display
#define IR_SENSOR_PIN 2          // IR sensor output connected to Pin 2
#define CLK_PIN 4                // Clock pin for TM1637
#define DIO_PIN 3                // Data pin for TM1637

// Initialize the TM1637 display
TM1637Display display(CLK_PIN, DIO_PIN);

// Variable to store the object count
int objectCount = 0;

void setup() {
  Serial.begin(9600);           // Start serial communication for debugging
  pinMode(IR_SENSOR_PIN, INPUT); // Set IR sensor pin as input

  display.setBrightness(0x0f);  // Set the brightness of the 7-segment display
  display.clear();              // Clear the display at startup
}

void loop() {
  int irState = digitalRead(IR_SENSOR_PIN); // Read the state of the IR sensor

  // If the sensor detects an object (assuming active LOW when object detected)
  if (irState == LOW) {
    objectCount++;                // Increment the object count
    Serial.print("Object Count: "); // Display the count in the serial monitor
    Serial.println(objectCount);
    
    display.showNumberDec(objectCount); // Display the count on the 7-segment display

    delay(500); // Debounce delay to avoid multiple counting for a single object
  }
}

<!-- VCC → 5V
GND → GND
OUT → Pin 2

VCC → 5V
GND → GND
DIO → Pin 3
CLK → Pin 4 -->