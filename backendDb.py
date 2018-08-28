#  AUTHOR:  Michael O'Brien
#  CREATED:  20 August 2018
#  UPDATED:  28 August 2018
#  DESCRIPTION:  Backend database for Yarn Tracker application

#  Import libraries need for DB
import sqlite3

#  Function to create the database and tables and variable declaration for connection and cursor
def create_table():
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('CREATE TABLE IF NOT EXISTS myYarnProjects(id INTEGER PRIMARY KEY, manufacturer TEXT, colorway TEXT, color  TEXT, weight TEXT, skeins INTEGER, yards INTEGER, grams INTEGER, project TEXT)')
    dbCursorObject.execute('CREATE TABLE IF NOT EXISTS manufacturer(id INTEGER PRIMARY KEY, manufacturer TEXT)')
    dbCursorObject.execute('CREATE TABLE IF NOT EXISTS color(id INTEGER PRIMARY KEY, color  TEXT)')
    dbCursorObject.execute('CREATE TABLE IF NOT EXISTS weight(id INTEGER PRIMARY KEY, weight TEXT)')
    dbConnection.commit()
    dbConnection.close()


#  Functions for myYarnProjects table
def view_data():
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('SELECT * FROM myYarnProjects, manufacturer, color, weight')
    rows = dbCursorObject.fetchall()
    dbConnection.close()
    return rows


def search_data(manufacturer = "", colorway = "", color = "", weight = "", skeins = "", yards = "", grams = "", project = ""):
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('SELECT * FROM  yarntracker WHERE manufacturer LIKE ? OR colorway LIKE ? OR weight LIKE ? OR color LIKE ? OR skeins LIKE ? OR yards LIKE ? OR grams LIKE ? OR project LIKE ?', (manufacturer, colorway, color, weight, skeins, yards, grams, project))


def update_data():
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()


def insert_data():
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()


def delete_data(id):
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()


#  Functions for color table
def view_Color():
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


#  Functions for manufacturer table
def view_Manufacturer():
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('SELECT * FROM manufacturer')
    rows = dbCursorObject.fetchall()
    dbConnection.close()
    return rows


def insert_Manufacturer(manufacturer):
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('INSERT INTO manufacturer VALUES (null, ?)', (manufacturer,))  #  Comma is required when only passing one value
    dbConnection.commit()
    dbConnection.close()


#  Functions for weight table
def view_Weight():
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('SELECT * FROM weight')
    rows = dbCursorObject.fetchall()
    dbConnection.close()
    return rows


def insert_Weight(weight):
    dbConnection = sqlite3.connect('yarntracker.db')
    dbCursorObject = dbConnection.cursor()
    dbCursorObject.execute('INSERT INTO weight VALUES (null, ?)', (weight,))  #  Comma is required when only passing one value
    dbConnection.commit()
    dbConnection.close()


create_table()
#insert_color('Yellow')
#insert_Manufacturer("Yarnspirations")
#insert_Weight('Yowsa')
#print(view_Color())
#print(view_Manufacturer())
#print(view_Weight())
