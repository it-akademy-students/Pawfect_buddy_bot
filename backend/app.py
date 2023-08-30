import os
import time
from flask import Flask, Response, request, jsonify, make_response
from flask_socketio import SocketIO
import sqlite3
from flask_cors import CORS
#from classes.Cors import Cors
from classes.Auth import Auth
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager


#def create_app(test_config=None):
# create and configure the app
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
#app.run(host= '0.0.0.0')

#if test_config is None:
    # load the instance config, if it exists, when not testing
    #app.config.from_pyfile('config.py', silent=True)
#else:
    # load the test config if passed in
    #app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route("/")
def web_interface():
    html = open("web_interface.html")
    response = html.read().replace('\n', '')
    html.close()
    return response


@app.route("/avancer")
def avancer():
    activate = request.args.get("on")
    from Scripts.Motors import Motors

    motors = Motors()
    return motors.avancer(activate)

@app.route("/reculer")
def reculer():
    activate = request.args.get("on")
    from Scripts.Motors import Motors

    motors = Motors()
    return motors.reculer(activate)

@app.route("/gauche")
def gauche():
    activate = request.args.get("on")
    from Scripts.Motors import Motors

    motors = Motors()
    return motors.gauche(activate)

@app.route("/droite")
def droite():
    activate = request.args.get("on")
    from Scripts.Motors import Motors

    motors = Motors()
    return motors.droite(activate)

@app.route('/activate-micro')
def activateMicro():
    from Scripts.Micro import Micro

    micro = Micro()
    micro.activateMicro()
    return "ok"
    

@app.route('/tail-move')
def tailMove():
    from Scripts.Servo import Servo

    servo = Servo(17)
    servo.tailMove()
    return "ok"

@app.route('/give-croquettes')
def giveCroquettes():
    from Scripts.StepMotor import StepMotor

    stepmotor = StepMotor()
    stepmotor.giveCroquettes()
    return 'ok'

@app.route('/toggle-camera')
def toggleCamera():
    import subprocess
    subprocess.Popen(["python3", "./Scripts/StreamCamera.py"])
    return 'ok'

@app.route('/toggle-automatic-mode')
def toggleAutoMode():
    from Scripts.Distance import Distance
    from Scripts.AutoMode import AutoMode
    front = Distance()
    front_distance = front.getFrontDistance()
    time.sleep(0.2)
    return "Distance mesurée = %.1f cm" % front_distance

    #socketio.run(app)
    #return app


if __name__ == '__main__':
    socketio.run(app)
#   os.system("sudo rm -r  ~/.cache/chromium/Default/Cache/*")
#  app.run(debug=True, port=8088, host='0.0.0.0', threaded=True)
# local web server http://192.168.1.200:5000/
# after Port forwarding Manipulation http://xx.xx.xx.xx:5000/