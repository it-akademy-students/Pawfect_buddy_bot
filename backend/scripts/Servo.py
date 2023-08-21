import RPi.GPIO as GPIO


class Servo:
    def __init__(self, angle):
        servo_pin = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, GPIO.OUT)
        self.angle = angle
        self.p = GPIO.PWM(servo_pin, 50)

    def activate(self):
        self.p.ChangeDutyCycle(self.angle)
        return 'salut'
