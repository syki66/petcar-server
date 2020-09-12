import RPi.GPIO as gpio
import time
from flask import Flask, render_template, Response
from camera_pi import Camera

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

t = 0.1

directions = [forward, reverse, turn_left, turn_right, pivot_left, pivot_right]


app = Flask(__name__)


@app.route('/dc_motor/<int:id>')
def move(id):
	init()
	directions[id](t)

	return render_template('dc_motor.html')



@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)