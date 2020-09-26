import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servoPIN=16
GPIO.setup(servoPIN, GPIO.OUT)
pwm=GPIO.PWM(servoPIN,50)
pwm.start(12)
time.sleep(1)

pwm.stop()
GPIO.cleanup()