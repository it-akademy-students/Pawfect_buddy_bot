# Import des librairies GPIO et time (temps et conversion) #
import RPi.GPIO as GPIO
import time
#import custom_motor

class Distance:
    def __init__(self) -> None:
        # Module GPIO: BOARD ou BCM (numérotation comme la sérigraphie de la carte ou comme le chip) #
        GPIO.setmode(GPIO.BCM)

        # FRONT SENSOR
        self.FRONT_TRIGGER = 6
        self.FRONT_ECHO = 5
        GPIO.setup(self.FRONT_TRIGGER, GPIO.OUT)
        GPIO.setup(self.FRONT_ECHO, GPIO.IN)

        # FRONT SENSOR
        self.BACK_TRIGGER = 8
        self.BACK_ECHO = 7
        GPIO.setup(self.BACK_TRIGGER, GPIO.OUT)
        GPIO.setup(self.BACK_ECHO, GPIO.IN)


    def getFrontDistance(self):
        # Mise à l'état haut de la broche Trigger #
        GPIO.output(self.FRONT_TRIGGER, True)
    
        # Mise à l'état bas de la broche Trigger aprés 10 µS #
        time.sleep(0.0000001)
        GPIO.output(self.FRONT_TRIGGER, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        # Enregistrement du temps de départ des ultrasons #
        while GPIO.input(self.FRONT_ECHO) == 0:
            StartTime = time.time()
    
        # Enregistrement du temps d'arrivés des ultrasons #
        while GPIO.input(self.FRONT_ECHO) == 1:
            StopTime = time.time()
    
        # Calcul de la durée de l'aller-retour des US #
        TimeElapsed = StopTime - StartTime
        # On multiplue la durée par la vitesse du son: 34300 cm/s #
        # et on divise par deux car il s'agit d'un aller et retour. #
        return (TimeElapsed * 34300) / 2

    def getBackDistance(self):
        # Mise à l'état haut de la broche Trigger #
        GPIO.output(self.BACK_TRIGGER, True)
    
        # Mise à l'état bas de la broche Trigger aprés 10 µS #
        time.sleep(0.0000001)
        GPIO.output(self.BACK_TRIGGER, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        # Enregistrement du temps de départ des ultrasons #
        while GPIO.input(self.BACK_ECHO) == 0:
            StartTime = time.time()
    
        # Enregistrement du temps d'arrivés des ultrasons #
        while GPIO.input(self.BACK_ECHO) == 1:
            StopTime = time.time()
    
        # Calcul de la durée de l'aller-retour des US #
        TimeElapsed = StopTime - StartTime
        # On multiplue la durée par la vitesse du son: 34300 cm/s #
        # et on divise par deux car il s'agit d'un aller et retour. #
        return (TimeElapsed * 34300) / 2
 


