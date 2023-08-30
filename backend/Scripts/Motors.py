import RPi.GPIO as GPIO
from time import sleep

class Motors:
    def __init__(self) -> None:
        GPIO.cleanup() 
        GPIO.setmode(GPIO.BCM)

        self.motor1A = 20 # IN1
        self.motor1B = 16 # IN2
        self.motor1E = 21 # ENI1

        self.motor2A = 13 # IN3
        self.motor2B = 19 # IN4
        self.motor2E = 26 # ENI2

        GPIO.setup(self.motor1A, GPIO.OUT)
        GPIO.setup(self.motor1B, GPIO.OUT)
        GPIO.setup(self.motor1E, GPIO.OUT)

        GPIO.setup(self.motor2A, GPIO.OUT)
        GPIO.setup(self.motor2B, GPIO.OUT)
        GPIO.setup(self.motor2E, GPIO.OUT)


    def avancer(self, activate):
        if activate == 'true':
            GPIO.output(self.motor1A, GPIO.HIGH)
            GPIO.output(self.motor1B, GPIO.LOW)
            GPIO.output(self.motor1E, GPIO.HIGH)

            GPIO.output(self.motor2A, GPIO.LOW)
            GPIO.output(self.motor2B, GPIO.HIGH)
            GPIO.output(self.motor2E, GPIO.HIGH)
        else:
            GPIO.output(self.motor1E, GPIO.LOW)
            GPIO.output(self.motor2E, GPIO.LOW)

        return "ok"


    def reculer(self, activate):
        if activate == 'true':
            GPIO.output(self.motor1A, GPIO.LOW)
            GPIO.output(self.motor1B, GPIO.HIGH)
            GPIO.output(self.motor1E, GPIO.HIGH)

            GPIO.output(self.motor2A, GPIO.HIGH)
            GPIO.output(self.motor2B, GPIO.LOW)
            GPIO.output(self.motor2E, GPIO.HIGH)
        else:
            GPIO.output(self.motor1E, GPIO.LOW)
            GPIO.output(self.motor2E, GPIO.LOW)

        return "ok"


    def gauche(self, activate):
        if activate == 'true':
            GPIO.output(self.motor1A, GPIO.HIGH)
            GPIO.output(self.motor1B, GPIO.LOW)
            GPIO.output(self.motor1E, GPIO.HIGH)

            GPIO.output(self.motor2A, GPIO.HIGH)
            GPIO.output(self.motor2B, GPIO.LOW)
            GPIO.output(self.motor2E, GPIO.HIGH)

        else:
            GPIO.output(self.motor1E, GPIO.LOW)
            GPIO.output(self.motor2E, GPIO.LOW)

        return "ok"

    
    def droite(self, activate):
        if activate == 'true':
            GPIO.output(self.motor1A, GPIO.LOW)
            GPIO.output(self.motor1B, GPIO.HIGH)
            GPIO.output(self.motor1E, GPIO.HIGH)

            GPIO.output(self.motor2A, GPIO.LOW)
            GPIO.output(self.motor2B, GPIO.HIGH)
            GPIO.output(self.motor2E, GPIO.HIGH)
        else:
            GPIO.output(self.motor1E, GPIO.LOW)
            GPIO.output(self.motor2E, GPIO.LOW)

        return "ok"
