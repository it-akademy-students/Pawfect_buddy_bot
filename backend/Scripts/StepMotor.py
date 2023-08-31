import RPi.GPIO as GPIO
import time

class StepMotor:
    def __init__(self):
        #GPIO.cleanup()
        self.in1 = 18
        self.in2 = 23
        self.in3 = 24
        self.in4 = 25

        # careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
        self.step_sleep = 0.002

        self.step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°

        self.direction = False # True for clockwise, False for counter-clockwise

        # defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
        self.step_sequence = [[1,0,0,1],
                        [1,0,0,0],
                        [1,1,0,0],
                        [0,1,0,0],
                        [0,1,1,0],
                        [0,0,1,0],
                        [0,0,1,1],
                        [0,0,0,1]]
        # setting up
        GPIO.setmode( GPIO.BCM )
        GPIO.setup( self.in1, GPIO.OUT )
        GPIO.setup( self.in2, GPIO.OUT )
        GPIO.setup( self.in3, GPIO.OUT )
        GPIO.setup( self.in4, GPIO.OUT )

        # initializing
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )

        self.motor_pins = [self.in1, self.in2, self.in3, self.in4]
        self.motor_step_counter = 0

    def cleanup(self):
        GPIO.output( self.in1, GPIO.LOW )
        GPIO.output( self.in2, GPIO.LOW )
        GPIO.output( self.in3, GPIO.LOW )
        GPIO.output( self.in4, GPIO.LOW )
        GPIO.cleanup()
    
    def giveCroquettes(self):
        i = 0
        for i in range(self.step_count):
            for pin in range(0, len(self.motor_pins)):
                GPIO.output( self.motor_pins[pin], self.step_sequence[self.motor_step_counter][pin] )
                if self.direction==True:
                    self.motor_step_counter = (self.motor_step_counter - 1) % 8
                elif self.direction==False:
                    self.motor_step_counter = (self.motor_step_counter + 1) % 8
                time.sleep( self.step_sleep )