#from flask import request
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
import sqlite3

class Auth:
    def __init__(self, app) -> None:
        self.jwt=JWTManager(app)

    def login(self, request):
        #connection = sqlite3.connect("../database/database.db")
        #connection.row_factory = sqlite3.Row

        email = request.json.get("email", None)
        password = request.json.get("password", None)
        if email != "test" or password != "test":
            return {
                "message": "Mauvais login ou mot de passe"
            }, 401
        
        access_token = create_access_token(identity=email)
        return {
            "access_token": access_token
        }
