// Program A [blink-initialize]

#define LED_BUILTIN 1 void setup() {
pinMode(LED_BUILTIN, OUTPUT);
}
void loop() {
digitalWrite(LED_BUILTIN, LOW); // LED on delay(1000);
digitalWrite(LED_BUILTIN, HIGH); // LED off delay(1000);
}

// Program B [Relay]
#define LED_BUILTIN 2 void setup() {
pinMode(LED_BUILTIN, OUTPUT);
pinMode(0, OUTPUT);
}
void loop() {
digitalWrite(LED_BUILTIN, LOW); // Turn the LED on (ESP-01 LED is active low) digitalWrite(0, HIGH);
delay(1000);
digitalWrite(LED_BUILTIN, HIGH); // Turn the LED off digitalWrite(0, LOW);
delay(1000);
}

// Program C [BLYNK]
#define BLYNK_TEMPLATE_ID " TMPL3t1fSyV7B”
#define BLYNK_TEMPLATE_NAME "LED
#define BLYNK_AUTH_TOKEN "PmNE7qJ6bIUHbenpj4VOTQgsG0HDwNl9"
#define BLYNK_PRINT Serial // Define the serial print function to use for debugging #include <ESP8266WiFi.h> // Include the ESP8266 WiFi library
#include <BlynkSimpleEsp8266.h> // Include the Blynk Simple ESP8266 library char ssid[] = "John"; // Define the WiFi network SSID
char pass[] = "12345678"; // Define the WiFi network password
void setup() // Setup function, called once at the beginning of the program
{
Serial.begin(115200); // Initialize the serial communication at a baud rate of 115200 Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass); // Initialize Blynk with the authentication token, WiFi SSID, and password
}
void loop() // Loop function, called repeatedly after setup()
{
Blynk.run(); // Run the Blynk framework to handle incoming and outgoing data
}