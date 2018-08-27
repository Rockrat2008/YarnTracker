

#  Import libraries need for DB
import sqlite3

#  Function to create the database and tables and variable declaration for connection and cursor
def create_table():
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('CREATE TABLE IF NOT EXISTS color(id INTEGER PRIMARY KEY, color  TEXT)')
    dbConnection.commit()
    dbConnection.close()


#  Functions for color table
def view_Color():
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('SELECT * FROM color')
    rows = dbCursorObject.fetchall()
    dbConnection.close()
    return rows


def load_ColorCombobox():
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('SELECT * FROM color')
    rows = dbCursorObject.fetchall()
    dbConnection.close()
    return rows


def update_ColorComboBox(color):
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('INSERT INTO color VALUES (null, ?)', (color,))  #  Comma is required when only passing one value


def insert_color(color):
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('INSERT INTO color VALUES (NULL, ?)', (color,))
    dbConnection.commit()
    dbConnection.close()


create_table()
#insert_color('Brown')
#print(view_Color())
