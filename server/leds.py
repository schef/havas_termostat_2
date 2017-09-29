import RPi.GPIO as GPIO
import time

ledStatus = False
ledPin = 18
relayStatus = False
relayPin = 17


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(relayPin, GPIO.OUT)
setRelay(0)
setLed(0)

def test():
    print("LED on")
    GPIO.output(ledPin,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(ledPin,GPIO.LOW)

def setLed(status):
    global ledStatus
    global ledPin
    if(status == ledStatus): return
    ledStatus = status
    if(status):
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        GPIO.output(ledPin, GPIO.LOW)

def setRelay(status):
    global relayStatus
    global relayPin
    status = !status
    if(status == relayStatus): return
    relayStatus = status
    if(status):
        GPIO.output(relayPin, GPIO.HIGH)
    else:
        GPIO.output(relayPin, GPIO.LOW)

