#include <Wire.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

const int tempSensorPin = A0;

void setup() {
  Serial.begin(9600);
  if (!display.begin(SSD1306_I2C_ADDRESS, 0x3C)) {
    while (true); // Halt if OLED initialization fails
  }
  display.clearDisplay();
}

void loop() {
  float tempC = analogRead(tempSensorPin) * 5.0 / 1023.0 * 100.0;
  float tempF = tempC * 1.8 + 32;

  // Display on OLED
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.printf("Temp: %.2f C\n%.2f F", tempC, tempF);
  display.display();

  // Log to Serial Monitor
  Serial.printf("Celsius: %.2f C, Fahrenheit: %.2f F\n", tempC, tempF);

  delay(2000); // Update every 2 seconds
}

<!-- 
VCC → 5V
GND → GND
OUT → A0

SDA → A4
SCL → A5
VCC → 5V
GND → GND -->