from RPi import GPIO
from time import sleep

class Servo :
    def __init__(self, pitch_io=18, yaw_io=17, pitch=10, yaw=10) :

        self.pitch_io = pitch_io
        self.yaw_io = yaw_io

        self.pitch_angle = pitch
        self.yaw_angle = yaw

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.pitch_io, GPIO.OUT)
        GPIO.setup(self.yaw_io, GPIO.OUT)


    def set_angle(self, port, angle) :
        pwm = GPIO.PWM(port, 50)
        pwm.start(8)
        dutycycle = angle/18 + 3
        pwm.ChangeDutyCycle(dutycycle)
        sleep(0.3)
        pwm.stop()

    def pitch_add(self, pitch_io=17, distance=5) :
        self.pitch_angle += distance
        self.pitch_angle = min(max(1, self.pitch_angle), 135)
        self.set_angle(self.pitch_io, self.pitch_angle)
        print(self.pitch_angle)

    def pitch_decrease(self, distance=5) :
        self.pitch_angle -= distance
        self.pitch_angle = min(max(1, self.pitch_angle), 135)        
        self.set_angle(self.pitch_io, self.pitch_angle)
        print(self.pitch_angle)

    def yaw_add(self, distance=5) :
        self.yaw_angle += distance
        self.yaw_angle = min(max(1, self.yaw_angle), 135)
        self.set_angle(self.yaw_io, self.yaw_angle)
        print(self.yaw_angle)

    def yaw_decrease(self, distance=5) :
        self.yaw_angle -= distance
        self.yaw_angle = min(max(1, self.yaw_angle), 135)
        self.set_angle(self.yaw_io, self.yaw_angle)
        print(self.yaw_angle)

    def pitch(self, angle) :
        self.pitch_angle = angle
        self.pitch_angle = min(max(1, self.pitch_angle), 135)        
        self.set_angle(self.pitch_io, self.pitch_angle)

    def yaw(self, angle) :
        self.yaw_angle = angle
        self.yaw_angle = min(max(1, self.yaw_angle), 135)
        self.set_angle(self.yaw_io, self.yaw_angle)

    def stop() :
        GPIO.cleanup()