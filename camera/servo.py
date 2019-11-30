from RPi import GPIO
from time import sleep

class Servo :
    def __init__(self, pitch_io=18, yaw_io=17, pitch=10, yaw=90, pitch_range=(1, 135), yaw_range=(60, 130)) :

        self.pitch_io = pitch_io
        self.yaw_io = yaw_io

        self.pitch_angle = pitch
        self.yaw_angle = yaw

        self.pitch_max = pitch_range[1]
        self.pitch_min = pitch_range[0]
        self.yaw_max = yaw_range[1]
        self.yaw_min = yaw_range[0]

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(self.pitch_io, GPIO.OUT)
        GPIO.setup(self.yaw_io, GPIO.OUT)

        self.pwm1 = GPIO.PWM(self.pitch_io, 100)
        self.pwm2 = GPIO.PWM(self.yaw_io, 100)
        self.pwm1.start(5)
        self.pwm2.start(5)

        # self.pitch(self.pitch_angle)
        # self.yaw(self.yaw_angle)


    def set_angle(self, port, angle) :
        if port==self.pitch_io :
            pwm = self.pwm1
        else :
            pwm = self.pwm2
        dutycycle = angle/10 + 2.5
        pwm.ChangeDutyCycle(dutycycle)

    def pitch_add(self, pitch_io=17, distance=5) :
        self.pitch_angle += distance
        self.pitch_angle = min(max(self.pitch_min, self.pitch_angle), self.pitch_max)
        self.set_angle(self.pitch_io, self.pitch_angle)
        # print(self.pitch_angle)

    def pitch_decrease(self, distance=5) :
        self.pitch_angle -= distance
        self.pitch_angle = min(max(self.pitch_min, self.pitch_angle), self.pitch_max)     
        self.set_angle(self.pitch_io, self.pitch_angle)
        # print(self.pitch_angle)

    def yaw_add(self, distance=5) :
        self.yaw_angle += distance
        self.yaw_angle = min(max(self.yaw_min, self.yaw_angle), self.yaw_max)
        self.set_angle(self.yaw_io, self.yaw_angle)
        # print(self.yaw_angle)

    def yaw_decrease(self, distance=5) :
        self.yaw_angle -= distance
        self.yaw_angle = min(max(self.yaw_min, self.yaw_angle), self.yaw_max)
        self.set_angle(self.yaw_io, self.yaw_angle)
        # print(self.yaw_angle)

    def pitch(self, angle) :
        self.pitch_angle = angle
        self.pitch_angle = min(max(self.pitch_min, self.pitch_angle), self.pitch_max)
        self.set_angle(self.pitch_io, self.pitch_angle)

    def yaw(self, angle) :
        self.yaw_angle = angle
        self.yaw_angle = min(max(self.yaw_min, self.yaw_angle), self.yaw_max)
        self.set_angle(self.yaw_io, self.yaw_angle)

    def stop() :
        GPIO.cleanup()