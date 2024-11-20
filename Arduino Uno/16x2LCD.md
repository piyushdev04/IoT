#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Set the LCD address (0x27) for a 16x2 display
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // Initialize the LCD
  lcd.begin(16, 2);
  lcd.clear();
}

void loop() {
  // Display the first line
  lcd.setCursor(0, 0);
  lcd.print("Chetan Dalal");

  // Display the second line
  lcd.setCursor(0, 1);
  lcd.print("GR.NO:22210872");
}

<!-- VCC → 5V
GND → GND
SDA → A4
SCL → A5 -->