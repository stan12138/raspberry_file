#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, request, session, escape, redirect, url_for
# import servo
# from camera_pi import Camera

app = Flask(__name__)

# my_servo = servo.Servo()

@app.route('/')
def index():
    """Video streaming home page."""
    # return render_template('index.html')
    if "user" in session and escape(session["user"])=="stan" :
        return render_template('index.html')
    else :
        session["user"] = "stranger"
        return render_template("login.html")


@app.route("/login", methods=["POST"])
def login() :
    user = request.form["user"]
    password = request.form["password"]
    print(user, password)
    if user=="Stan" and password=="112358" :
        session["user"] = "stan"
        return redirect("/")
    else :
        session["user"] = "stranger"
        return redirect("/")


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    if "user" in session and escape(session["user"])=="stan" :
    """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    else :
        session["user"] = "stranger"
        return render_template("login.html")        


# @app.route("/backend")
# def backend() :
#     return render_template("backend.html")


@app.route("/pitch_add")
def pitch_add() :
    # print("get pitch add")
    if "user" in session and escape(session["user"])=="stan" :
        my_servo.pitch_add(distance=7)
    return ""

@app.route("/pitch_decrease")
def pitch_decrease() :
    # print("get pitch decrease")
    if "user" in session and escape(session["user"])=="stan" :
        my_servo.pitch_decrease(distance=7)
    return ""

@app.route("/yaw_add")
def yaw_add() :
    # print("get yaw add")
    if "user" in session and escape(session["user"])=="stan" :
        my_servo.yaw_add(distance=7)
    return ""

@app.route("/yaw_decrease")
def yaw_decrease() :
    # print("get yaw decrease")
    if "user" in session and escape(session["user"])=="stan" :
        my_servo.yaw_decrease(distance=7)
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
