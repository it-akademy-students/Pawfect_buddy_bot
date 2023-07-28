import os
from flask import Flask, Response, request, jsonify, make_response
from flask_cors import CORS
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


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

    return app

# if __name__ == '__main__':
#   os.system("sudo rm -r  ~/.cache/chromium/Default/Cache/*")
#  app.run(debug=True, port=8088, host='0.0.0.0', threaded=True)
# local web server http://192.168.1.200:5000/
# after Port forwarding Manipulation http://xx.xx.xx.xx:5000/
