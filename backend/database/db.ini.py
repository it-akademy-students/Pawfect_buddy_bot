import sqlite3

connection = sqlite3.connect('database.db')


connection.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL)')
connection.execute('INSERT INTO users VALUES (1, "Toto")')



connection.commit()
connection.close()


#"DROP TABLE IF EXISTS user;"
#"CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL,);"