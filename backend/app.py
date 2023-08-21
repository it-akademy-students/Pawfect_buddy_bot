import os
from flask import Flask, Response, request, jsonify, make_response
from flask_cors import CORS
import sqlite3


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'pawefect_buddy_bot.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        import RPi.GPIO as GPIO
        import time
        from gpiozero import Motor, LED
        # import custom_motor

        # Module GPIO: BOARD ou BCM (numérotation comme la sérigraphie de la carte ou comme le chip) #
        GPIO.setmode(GPIO.BCM)

        # Définition des broches GPIO #
        GPIO_TRIGGER = 16
        GPIO_ECHO = 12

        # Définition des broches en entrées ou en sortie #
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)

        motor = Motor(17, 18)
        motorSwitch = LED(27)

        def toggleSwitch(distance):
            global motorSpeedForward
            if distance >= 4:
                motorSwitch.on()
                motor.forward(1)
            elif distance < 4:
                motorSwitch.off()

        def distance():
            # Mise à l'état haut de la broche Trigger #
            GPIO.output(GPIO_TRIGGER, True)

            # Mise à l'état bas de la broche Trigger aprés 10 µS #
            time.sleep(0.0000001)
            GPIO.output(GPIO_TRIGGER, False)

            StartTime = time.time()
            StopTime = time.time()

            # Enregistrement du temps de départ des ultrasons #
            while GPIO.input(GPIO_ECHO) == 0:
                StartTime = time.time()

            # Enregistrement du temps d'arrivés des ultrasons #
            while GPIO.input(GPIO_ECHO) == 1:
                StopTime = time.time()

            # Calcul de la durée de l'aller-retour des US #
            TimeElapsed = StopTime - StartTime
            # On multiplue la durée par la vitesse du son: 34300 cm/s #
            # et on divise par deux car il s'agit d'un aller et retour. #
            distance = (TimeElapsed * 34300) / 2

            toggleSwitch(distance)

        while True:
            distance()
        return "index"

    @app.route('/test')
    def test():
        connection = sqlite3.connect('./database/database.db')
        connection.row_factory = sqlite3.Row
        users = connection.execute('SELECT * FROM users').fetchall()
        data = []
        for user in users:
            data.append([x for x in user])
        connection.close()
        return data

    @app.route('/servo')
    def servo():
        from scripts.Servo import Servo

        servo = Servo(12.5)
        servo.activate()
        return "ok"
    #def servo():
        #import RPi.GPIO as GPIO
        #import time

        #servoPIN = 24
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(servoPIN, GPIO.OUT)

        #p = GPIO.PWM(servoPIN, 50)
        #p.start(2.5)

        #while True:
        #    p.ChangeDutyCycle(4.5)
        #    time.sleep(0.5)
        #    p.ChangeDutyCycle(6.5)
        #    time.sleep(0.5)
        #    p.ChangeDutyCycle(10.5)
        #    time.sleep(0.5)
        #    p.ChangeDutyCycle(12.5)
        #    time.sleep(0.5)
        #    p.ChangeDutyCycle(10.5)
        #    time.sleep(0.5)
        #    p.ChangeDutyCycle(8.5)
        #    time.sleep(0.5)
        #    p.ChangeDutyCycle(6.5)
        #    time.sleep(0.5)

    return app

# if __name__ == '__main__':
#   os.system("sudo rm -r  ~/.cache/chromium/Default/Cache/*")
#  app.run(debug=True, port=8088, host='0.0.0.0', threaded=True)
# local web server http://192.168.1.200:5000/
# after Port forwarding Manipulation http://xx.xx.xx.xx:5000/