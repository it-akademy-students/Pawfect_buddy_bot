import os
import datetime
import sqlite3

class Micro:
    def getRandomFileName(self, basename):
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        return "_".join([basename, suffix])

    def activateMicro(self):
        filename = self.getRandomFileName('voice_record')
        fullpath = "/home/beetroot/Documents/pbb_final/backend/records/audio/"

        os.system("arecord -vv -D plughw:2,0 --duration=5 > " + fullpath + filename +".wav")
        
        #try:
        #    connection = sqlite3.connect('./database/database.db')
        #    cursor = connection.cursor()
        #
        #    query = """INSERT INTO records (path,filename) VALUES (?, ?)"""
        #    data_tuple = (fullpath, filename)
        #    cursor.execute(query, data_tuple)
        #    connection.commit()
        #    cursor.close()
        #
        #    connection.row_factory = sqlite3.Row
        #    users = connection.execute('SELECT * FROM records').fetchall()
        #    data = []
        #    for user in users:
        #        data.append([x for x in user])
        #    connection.close()
        #    return data
        #
        #except sqlite3.Error as error:
        #    print("Failed", error) 
