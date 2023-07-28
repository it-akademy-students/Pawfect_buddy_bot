from flask import Blueprint
import sqlite3


main = Blueprint('main', __name__)


@main.route('/')
def index():
        connection = sqlite3.connect('../database/database.db')
        connection.row_factory = sqlite3.Row
        users = connection.execute('SELECT * FROM users').fetchall()
        data = []
        for user in users:
            data.append([x for x in user])
        connection.close()
        return data

@main.route('/test')
def test():
        connection = sqlite3.connect('../database/database.db')
        connection.row_factory = sqlite3.Row
        users = connection.execute('SELECT * FROM users').fetchall()
        data = []
        for user in users:
            data.append([x for x in user])
        connection.close()
        return data
