import RPi.GPIO as gpio
import time
import sys
from pynput import keyboard

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(15, True)
    gpio.output(13, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(15, False)
    gpio.output(13, True)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(15, True)
    gpio.output(13, True)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(15, True)
    gpio.output(13, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(15, True)
    gpio.output(13, False)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(15, False)
    gpio.output(13, True)
    time.sleep(tf)
    gpio.cleanup()

def key_input(event):
    init()
    print 'Key : ', event.char
    key_press = event.char
    sleep_time = 0.03
     
    if key_press.lower() == 'w':
	forward(sleep_time)
    elif key_press.lower() == 's':
	reverse(sleep_time)
    elif key_press.lower() == 'a':
	turn_left(sleep_time)
    elif key_press.lower() == 'd':
	turn_right(sleep_time)
    elif key_press.lower() == 'q':
	pivot_left(sleep_time)
    elif key_press.lower() == 'e':
	pivot_right(sleep_time)
    else:
	pass

'''
command = Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
'''

'''

	init()
	forward(1)
	init()
	reverse(1)
	init()
	pivot_right(1)
'''


def on_press(key):
    try:
	init()
	sleep_time = 0.03
        if (key.char == 'w'):
		forward(sleep_time)
	elif (key.char == 's'):
		reverse(sleep_time)
	elif (key.char == 'a'):
		turn_left(sleep_time)
	elif (key.char == 'd'):
		turn_right(sleep_time)
	elif (key.char == 'q'):
		pivot_left(sleep_time)
	elif (key.char == 'e'):
		pivot_right(sleep_time)
	else:
		pass


    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False



# Collect events until released

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
