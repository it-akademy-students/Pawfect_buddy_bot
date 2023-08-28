import RPi.GPIO as GPIO
import time


class Servo:
    def __init__(self, pin):
        self.pin = pin

        GPIO.cleanup()    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.p = GPIO.PWM(self.pin, 50) #GPIO17 for PWM with 50Hz
    

    def tailMove(self):
        self.p.start(2.5) #Initialization
        i = 0
        while (i < 5):
            self.p.ChangeDutyCycle(5)
            time.sleep(0.2)
            self.p.ChangeDutyCycle(7.5)
            time.sleep(0.2)
            self.p.ChangeDutyCycle(10)
            time.sleep(0.2)
            self.p.ChangeDutyCycle(7.5)
            time.sleep(0.2)
            i += 1
        
        
