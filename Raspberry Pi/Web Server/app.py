import RPi.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED pins
ledRed = 13
ledYellow = 19
ledGreen = 26

# Initialize LED states
ledRedStatus = 1
ledYellowStatus = 1
ledGreenStatus = 0

# Setup GPIO pins
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledYellow, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)

# Set initial LED states
GPIO.output(ledRed, GPIO.HIGH)
GPIO.output(ledYellow, GPIO.HIGH)
GPIO.output(ledGreen, GPIO.HIGH)

@app.route("/")
def index():
    # Get current status of LEDs
    ledRedStatus = GPIO.input(ledRed)
    ledYellowStatus = GPIO.input(ledYellow)
    ledGreenStatus = GPIO.input(ledGreen)

    # Pass the LED statuses to the template
    templateData = {
        'ledRed': ledRedStatus,
        'ledYellow': ledYellowStatus,
        'ledGreen': ledGreenStatus,
    }

    return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    # Set actuator based on device name
    if deviceName == "ledRed":
        actuator = ledRed
    elif deviceName == "ledYellow":
        actuator = ledYellow
    elif deviceName == "ledGreen":
        actuator = ledGreen
    else:
        return "Invalid device name", 400

    # Perform action (on/off)
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    elif action == "off":
        GPIO.output(actuator, GPIO.LOW)
    else:
        return "Invalid action", 400

    # Update the LED statuses
    ledRedStatus = GPIO.input(ledRed)
    ledYellowStatus = GPIO.input(ledYellow)
    ledGreenStatus = GPIO.input(ledGreen)

    # Pass the updated LED statuses to the template
    templateData = {
        'ledRed': ledRedStatus,
        'ledYellow': ledYellowStatus,
        'ledGreen': ledGreenStatus,
    }

    return render_template("index.html", **templateData)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)