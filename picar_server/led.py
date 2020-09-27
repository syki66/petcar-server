import RPi.GPIO as GPIO
import time

def led(PIN, status):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.OUT)

    if status == True:
        GPIO.output(PIN, True)

    else:
        GPIO.cleanup()

