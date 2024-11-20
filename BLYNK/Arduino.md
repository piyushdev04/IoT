#define BLYNK_TEMPLATE_ID " TMPL3t1fSyV7B " #define BLYNK_TEMPLATE_NAME "LED4"
#define BLYNK_AUTH_TOKEN "gpgMBGfHN1-pgyWWAZ27xGM3sGUxgnCw" #define BLYNK_PRINT Serial // Define the serial print function to use for debugging
#include <ESP8266_Lib.h> // Include the ESP8266 library (note: this is not the standard ESP8266WiFi library)
#include <BlynkSimpleShieldEsp8266.h> // Include the Blynk Simple Shield ESP8266 library char ssid[] = "John"; // Define the WiFi network SSID
char pass[] = "12345678"; // Define the WiFi network password
#include <SoftwareSerial.h> // Include the SoftwareSerial library for serial communication
SoftwareSerial EspSerial(2, 3); // Initializes software serial on pins 2 (Rx) and 3 (Tx) for communication with the ESP8266 module
#define ESP8266_BAUD 38400 // Defines the baud rate for communication with the ESP8266 module 38400
ESP8266 wifi(&EspSerial); // Creates a wifi object that connects the ESP8266 module to software serial (EspSerial)
void setup() // Setup function, called once at the beginning of the program
{
Serial.begin(115200); // Initialize the serial communication at a baud rate of 115200
EspSerial.begin(ESP8266_BAUD); // Initialize the ESP serial communication at the defined baud rate delay(10); // Adds a delay to ensure proper initialization
Blynk.begin(BLYNK_AUTH_TOKEN, wifi, ssid, pass, "blynk.cloud", 80); // Initialize Blynk with the authentication token, WiFi object, SSID, password, server, and port
}