#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width
#define SCREEN_HEIGHT 64 // OLED display height
#define OLED_RESET    -1 // Reset pin not used
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Pin for temperature sensor
const int tempSensorPin = A0;

// Variables for temperature readings
float tempCelsius = 0.0;
float tempFahrenheit = 0.0;
unsigned long previousMillis = 0;
const unsigned long interval = 2000; // Logging interval (2 seconds)

// Function to read temperature in Celsius
float readTemperature() {
  int sensorValue = analogRead(tempSensorPin);
  return (sensorValue * 5.0 / 1023.0) * 100.0; // Convert to Celsius
}

void setup() {
  // Initialize Serial Monitor
  Serial.begin(9600);

  // Initialize OLED Display
  if (!display.begin(SSD1306_I2C_ADDRESS, 0x3C)) {
    Serial.println(F("OLED initialization failed!"));
    while (true);
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.print("Initializing...");
  display.display();
  delay(2000);
}

void loop() {
  // Read temperature
  tempCelsius = readTemperature();
  tempFahrenheit = tempCelsius * 1.8 + 32;

  // Display values on OLED
  display.clearDisplay();
  display.setCursor(0, 0);
  display.println("Temperature:");
  display.setCursor(0, 10);
  display.print("Celsius: ");
  display.print(tempCelsius, 2);
  display.println(" C");
  display.setCursor(0, 30);
  display.print("Fahrenheit: ");
  display.print(tempFahrenheit, 2);
  display.println(" F");
  display.display();

  // Log data in the Serial Monitor
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    Serial.print("Celsius: ");
    Serial.print(tempCelsius, 2);
    Serial.print(" C, ");
    Serial.print("Fahrenheit: ");
    Serial.print(tempFahrenheit, 2);
    Serial.println(" F");
  }

  delay(500); // Update display frequency
}

<!-- Circuit Connections
I.M35 Sensor:

VCC → 5V on Arduino.
GND → GND on Arduino.
OUT → A0 on Arduino (analog pin to read temperature).
I2C OLED Display:

SDA → A4 (Uno/Nano I2C data line).
SCL → A5 (Uno/Nano I2C clock line).
VCC → 5V.
GND → GND. -->