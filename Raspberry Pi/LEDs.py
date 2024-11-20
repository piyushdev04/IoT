import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO Library
from time import sleep  # Import the sleep function from the time module

GPIO.setwarnings(False)  # Ignore warnings for now
GPIO.setmode(GPIO.BCM)  # Set GPIO mode to BCM (can also use GPIO.BOARD)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)  # Set pin 12 to be an output pin and set initial value to LOW
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)  # Set pin 18 to be an output pin and set initial value to LOW

while True:  # Run forever
    GPIO.output(12, GPIO.HIGH)  # Turn on pin 12
    GPIO.output(18, GPIO.HIGH)  # Turn on pin 18
    sleep(3)  # Sleep for 3 seconds

    GPIO.output(12, GPIO.LOW)  # Turn off pin 12
    GPIO.output(18, GPIO.LOW)  # Turn off pin 18
    sleep(3)  # Sleep for 3 seconds