import RPi.GPIO as GPIO
import time

def led(PINS, status):
    if status == True:
        while(True):
            GPIO.setmode(GPIO.BOARD)
        
            GPIO.setup(PINS[0], GPIO.OUT)
            GPIO.setup(PINS[1], GPIO.OUT)
            GPIO.setup(PINS[2], GPIO.OUT)

            red = GPIO.PWM(PINS[0], 100)
            green = GPIO.PWM(PINS[1], 100)
            blue = GPIO.PWM(PINS[2], 100)
            
            red.start(0)
            green.start(0)
            blue.start(0)

            red.ChangeDutyCycle(100)
            green.ChangeDutyCycle(100)
            blue.ChangeDutyCycle(100)
            time.sleep(1)

            red.stop()
            green.stop()
            blue.stop()

            GPIO.cleanup()

    else:
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(PINS[0], GPIO.OUT)
        GPIO.setup(PINS[1], GPIO.OUT)
        GPIO.setup(PINS[2], GPIO.OUT)

        red = GPIO.PWM(PINS[0], 1)
        green = GPIO.PWM(PINS[1], 1)
        blue = GPIO.PWM(PINS[2], 1)
            
        red.start(0)
        green.start(0)
        blue.start(0)

        red.stop()
        green.stop()
        blue.stop()

        GPIO.cleanup()

    '''
    if status == True:
        GPIO.output(PIN, True)

    else:
        GPIO.cleanup()
    '''
