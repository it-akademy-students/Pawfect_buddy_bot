import sqlite3

connection = sqlite3.connect('database.db')

#User table
connection.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL)')
connection.execute('INSERT INTO users VALUES (1, "Toto")')

#Recording table
connection.execute('CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, path TEXT UNIQUE NOT NULL, filename TEXT UNIQUE NOT NULL)')


connection.commit()
connection.close()


#"DROP TABLE IF EXISTS user;"
#"CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL,);"