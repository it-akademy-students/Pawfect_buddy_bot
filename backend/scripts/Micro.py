import os
import sqlite3

class Micro:
    def activateMicro(self):
        os.system("arecord -vv -D plughw:2,0 --duration=5 > /home/beetroot/Documents/pbb_final/backend/records/audio/test.wav")
        connection = sqlite3.connect('./database/database.db')
        connection.execute('INSERT INTO records (id,path,filename) VALUES (2,"/home/beetroot/Documents/pbb_final/backend/", "toto.wav") ')

        connection.row_factory = sqlite3.Row
        users = connection.execute('SELECT * FROM records').fetchall()
        data = []
        for user in users:
            data.append([x for x in user])
        connection.close()
        return data

