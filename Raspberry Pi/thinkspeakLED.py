import RPi.GPIO as GPIO
import Adafruit_DHT
import urllib.request
from time import sleep

GPIO.setmode(GPIO.BCM)
# Set up the sensor
sensor = Adafruit_DHT.DHT11
pin = 5

while True:
    humidity = 63
    temperature = 35

    if humidity is not None and temperature is not None:
        # Print the temperature and humidity
        print('get reading.')
        # Send data to ThingSpeak
        url = 'https://api.thingspeak.com/update?api_key=7I8TJOZDADDAPLTT&field1={}&field2={}'.format(temperature, humidity)
        urllib.request.urlopen(url)
    else:
        print(f'Temp={0:0.1f}*C Humidity={1:0.1f}%').format(temperature, humidity)
   
    sleep(1)