#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

Adafruit_SSD1306 display(128, 64, &Wire, -1);

void setup() {
  Serial.begin(115200);
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    while (true);
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 10);
  display.println(F("Chetan Dalal"));
  display.println(F("22210872"));
  display.println(F("Roll No. 311012"));
  display.display();
}

void loop() {}

<!-- VCC → Connect to 5V on Arduino
GND → Connect to GND on Arduino
SCL (Clock Pin) → Connect to A5
SDA (Data Pin) → Connect to A4 -->