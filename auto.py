import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk
import random
import math

def initpins():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(10, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
	#GPIO.setup(38, GPIO.OUT)
	#GPIO.setup(37, GPIO.IN)
def reverse(t):
        initpins()
        GPIO.output(8, False)
        GPIO.output(10, True)
        GPIO.output(11, True)
        GPIO.output(12, False)
        time.sleep(t)
        GPIO.cleanup()
def forward(t):
        initpins()
        GPIO.output(8, True)
        GPIO.output(10, False)
        GPIO.output(11, False)
        GPIO.output(12, True)
        time.sleep(t)
        GPIO.cleanup()

def left(t):
    initpins()
    GPIO.output(10, True)
    GPIO.output(8, False)
    GPIO.output(12, True)
    GPIO.output(11, False)
    time.sleep(t)
    GPIO.cleanup()

def right(t):
    initpins()
    GPIO.output(10, False)
    GPIO.output(8, True)
    GPIO.output(12, False)
    GPIO.output(11, True)
    time.sleep(t)
    GPIO.cleanup()

def distance():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(38, GPIO.OUT)
        GPIO.setup(37, GPIO.IN)
	
	GPIO.output(38, False)
	#time.sleep(0.1)
	
	GPIO.output(38, True)
	time.sleep(0.00001)
	GPIO.output(38, False)

	while GPIO.input(37) == False:
		pass
	start = time.time()
	while GPIO.input(37) == True:
		pass
	stop = time.time()
	distance = 17000*(stop-start)
	print(str(distance)+"cm")
	GPIO.cleanup()
	return distance

def rendom():
	i = random.randrange(1,4)
	r = random.randrange(1,7)
	if i == 1:
		right(r*0.33)
	elif i == 2:
		left(r*0.33)
	else:
		reverse(r*0.15)

d=[0,0,0]
i = 3

while True:
	forward(0.1)
	k = random.randrange(1,18)
	if k == 6:
		right(random.randrange(1,4)*0.3)
	elif k == 5:
		left(random.randrange(1,4)*0.3)

	if distance() < 25 :
		rendom()
	if distance() > 500:
		rendom()
	
	d.append(round(distance()))
	print(d[i])
	
	if (d[i] == d[i-1] and d[i] == d[i-2]):
		rendom()
		rendom()
	i=i+1
