import os
import time
from flask import Flask, Response, request, jsonify, make_response
from flask_socketio import SocketIO
from threading import Thread
import sqlite3
from flask_cors import CORS
from classes.Auth import Auth
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager


app = Flask(__name__, instance_relative_config=True)
CORS(app, resources={r"/*": {"origins":"http://192.168.1.30:8081"}})
socketio = SocketIO(app, cors_allowed_origins="http://192.168.1.30:8081")

app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'pawefect_buddy_bot.sqlite'),
)


# Lancement du script pour avoir le stream caméra
import subprocess
subprocess.Popen(["python3", "./Scripts/StreamCamera.py"])


# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from Scripts.Servo import Servo
from Scripts.StepMotor import StepMotor
from Scripts.Motors import Motors
from Scripts.Micro import Micro

motors = Motors()
servo = Servo()
stepmotor = StepMotor()
micro = Micro()


def handle_components(action, data = None):
    if action == "tail_move":
        servo.tailMove()

    if action == "give_croquettes":
        stepmotor.giveCroquettes()

    if action == "avancer":
        activate = data
        motors.avancer(activate)
    
    if action == "reculer":
        activate = data
        motors.reculer(activate)
    
    if action == "gauche":
        activate = data
        motors.gauche(activate)

    if action == "droite":
        activate = data
        motors.droite(activate)

    if action == "activate_micro":
        micro.activateMicro()
  
    
        
@socketio.on('tail_move')
def tail_move():
    Thread(target=handle_components, args=("tail_move",), daemon=True).start()


@socketio.on('give_croquettes')
def give_croquettes():
    Thread(target=handle_components, args=("give_croquettes",), daemon=True).start()
    

@socketio.on("reculer")
def avancer(data):
    Thread(target=handle_components, args=("reculer", data,), daemon=True).start()


@socketio.on("avancer")
def reculer(data):
    Thread(target=handle_components, args=("avancer", data,), daemon=True).start()


@socketio.on("gauche")
def gauche(data):
    Thread(target=handle_components, args=("gauche", data,), daemon=True).start()


@socketio.on("droite")
def droite(data):
    Thread(target=handle_components, args=("droite", data,), daemon=True).start()


@socketio.on('activate_micro')
def activate_micro():
    Thread(target=handle_components, args=("activate_micro",), daemon=True).start()


if __name__ == '__main__':
    import RPi.GPIO as GPIO

    GPIO.cleanup()
    socketio.run(app, threaded=True)

#   os.system("sudo rm -r  ~/.cache/chromium/Default/Cache/*")
#  app.run(debug=True, port=8088, host='0.0.0.0', threaded=True)
# local web server http://192.168.1.200:5000/
# after Port forwarding Manipulation http://xx.xx.xx.xx:5000/