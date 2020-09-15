import RPi.GPIO as gpio
import time
from flask import Flask, render_template, Response
from camera_pi import Camera
from dc_motor import *





app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dc_motor/<int:id>')
def move(id):
    """DC motor control page"""
    t = 0.1
    directions = [forward, reverse, turn_left, turn_right, pivot_left, pivot_right]
    directions[id](t)
    return render_template('dc_motor.html')

@app.route('/camera')
def camera():
    """Video streaming home page."""
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)