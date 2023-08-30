from Scripts.Distance import Distance
from Scripts.Motors import Motors

class AutoMode:
    def __init__(self, activate) -> None:
        self.activate = activate

    def autoActivate(self):
        while self.activate:
            distance = Distance()
            motors = Motors()
            frontDistance = distance.getFrontDistance()
            if frontDistance > 20:
                motors.avancer('true')
            else:
                motors.avancer('false')
                motors.droite('true')
        