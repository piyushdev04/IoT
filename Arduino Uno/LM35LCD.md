#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // Set the I2C address (adjust if necessary)

const int tempSensorPin = A0;

void setup() {
  lcd.begin(); // Initialize LCD
  lcd.backlight(); // Turn on backlight
  Serial.begin(9600);
}

void loop() {
  float tempC = analogRead(tempSensorPin) * 5.0 / 1023.0 * 100.0;
  float tempF = tempC * 1.8 + 32;

  // Display on LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(tempC, 2);
  lcd.print(" C");
  lcd.setCursor(0, 1);
  lcd.print(tempF, 2);
  lcd.print(" F");

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