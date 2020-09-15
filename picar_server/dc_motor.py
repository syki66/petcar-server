import RPi.GPIO as gpio
import time

pins = (7, 11, 13, 15)

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(pins[0], gpio.OUT)
    gpio.setup(pins[1], gpio.OUT)
    gpio.setup(pins[2], gpio.OUT)
    gpio.setup(pins[3], gpio.OUT)

def forward(tf):
    init()
    gpio.output(pins[0], True)
    gpio.output(pins[1], False)
    gpio.output(pins[3], True)
    gpio.output(pins[2], False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(pins[0], False)
    gpio.output(pins[1], True)
    gpio.output(pins[3], False)
    gpio.output(pins[2], True)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    init()
    gpio.output(pins[0], True)
    gpio.output(pins[1], False)
    gpio.output(pins[3], True)
    gpio.output(pins[2], True)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    init()
    gpio.output(pins[0], True)
    gpio.output(pins[1], True)
    gpio.output(pins[3], True)
    gpio.output(pins[2], False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    init()
    gpio.output(pins[0], False)
    gpio.output(pins[1], True)
    gpio.output(pins[3], True)
    gpio.output(pins[2], False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    init()
    gpio.output(pins[0], True)
    gpio.output(pins[1], False)
    gpio.output(pins[3], False)
    gpio.output(pins[2], True)
    time.sleep(tf)
    gpio.cleanup()