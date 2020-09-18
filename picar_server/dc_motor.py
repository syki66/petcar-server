import RPi.GPIO as gpio
import time

#pins = (7, 11, 13, 15)

class DCMotor:
    def __init__(self, pins):
        self.pins = pins

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
        gpio.cleanup()

    def reverse(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], False)
        gpio.output(self.pins[1], True)
        gpio.output(self.pins[3], False)
        gpio.output(self.pins[2], True)
        gpio.cleanup()

    def turn_left(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], True)
        gpio.output(self.pins[1], False)
        gpio.output(self.pins[3], True)
        gpio.output(self.pins[2], True)
        gpio.cleanup()

    def turn_right(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], True)
        gpio.output(self.pins[1], True)
        gpio.output(self.pins[3], True)
        gpio.output(self.pins[2], False)
        gpio.cleanup()

    def pivot_right(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], False)
        gpio.output(self.pins[1], True)
        gpio.output(self.pins[3], True)
        gpio.output(self.pins[2], False)
        time.sleep(1)
        gpio.cleanup()

    def pivot_left(self):
        self.initialize_gpio()
        gpio.output(self.pins[0], True)
        gpio.output(self.pins[1], False)
        gpio.output(self.pins[3], False)
        gpio.output(self.pins[2], True)
        gpio.cleanup()


test = DCMotor((7, 11, 13, 15))

test.pivot_right()