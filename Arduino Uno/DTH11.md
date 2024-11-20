#include <DHT.h>

// Define the DHT pin and sensor type (DHT11 or DHT22)
#define DHTPIN 2        // Data pin connected to D2
#define DHTTYPE DHT22   // Use DHT11 for DHT11 sensor or DHT22 for DHT22 sensor

DHT dht(DHTPIN, DHTTYPE);  // Initialize the DHT sensor

void setup() {
  Serial.begin(9600);  // Start serial communication
  dht.begin();         // Initialize the DHT sensor
}

void loop() {
  // Wait a few seconds between readings
  delay(2000);

  // Read humidity and temperature
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature(); // In Celsius
  
  // Check if the reading failed and try again
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  // Display the values on the Serial Monitor
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" C");
}