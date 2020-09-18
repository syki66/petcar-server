import RPi.GPIO as gpio
import time

#pins = (7, 11, 13, 15)

class DCMotor:
    def __init__(self, pins, sleep_t):
        self.pins = pins
        self.sleep_t = sleep_t

    def initialize_gpio(self):
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.pins[0], gpio.OUT)
        gpio.setup(self.pins[1], gpio.OUT)
        gpio.setup(self.pins[2], gpio.OUT)
        gpio.setup(self.pins[3], gpio.OUT)

    def forward(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], True)
        gpio.output(self.pins[1], False)
        gpio.output(self.pins[3], True)
        gpio.output(self.pins[2], False)
        time.sleep(self.sleep_t)
        gpio.cleanup()

    def reverse(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], False)
        gpio.output(self.pins[1], True)
        gpio.output(self.pins[3], False)
        gpio.output(self.pins[2], True)
        time.sleep(self.sleep_t)
        gpio.cleanup()

    def turn_left(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], True)
        gpio.output(self.pins[1], False)
        gpio.output(self.pins[3], True)
        gpio.output(self.pins[2], True)
        time.sleep(self.sleep_t)
        gpio.cleanup()

    def turn_right(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], True)
        gpio.output(self.pins[1], True)
        gpio.output(self.pins[3], True)
        gpio.output(self.pins[2], False)
        time.sleep(self.sleep_t)
        gpio.cleanup()

    def pivot_right(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], False)
        gpio.output(self.pins[1], True)
        gpio.output(self.pins[3], True)
        gpio.output(self.pins[2], False)
        time.sleep(self.sleep_t)
        gpio.cleanup()

    def pivot_left(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], True)
        gpio.output(self.pins[1], False)
        gpio.output(self.pins[3], False)
        gpio.output(self.pins[2], True)
        time.sleep(self.sleep_t)
        gpio.cleanup()
