#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
import servo
from camera_pi import Camera

app = Flask(__name__)

my_servo = servo.Servo()

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


@app.route("/backend")
def backend() :
    return render_template("backend.html")


@app.route("/pitch_add")
def pitch_add() :
    # print("get pitch add")
    my_servo.pitch_add()
    return ""

@app.route("/pitch_decrease")
def pitch_decrease() :
    # print("get pitch decrease")
    my_servo.pitch_decrease()
    return ""

@app.route("/yaw_add")
def yaw_add() :
    # print("get yaw add")
    my_servo.yaw_add()
    return ""

@app.route("/yaw_decrease")
def yaw_decrease() :
    # print("get yaw decrease")
    my_servo.yaw_decrease()
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
