import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
from hashlib import sha256
import os
#f = '.'
#f += str(os.environ.get('PYTHONPATH'))
f = "NeedlessYouthUnemployment/data/db.db"

def create_db():
    """
    Initializes a table in database.
    """
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS users( username TEXT, password TEXT)"
    c.execute(command)

def add_user(username, password):
    """
    Attempts to add a username and password pair to the database.
    """
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "SELECT username FROM users WHERE username = \'" + username + "\'" #checks if username already exists
    result = c.execute(command)
    if result.fetchone() == None:
        encrypt = sha256(password.encode('utf-8')).hexdigest() #encrypt password

        command = "INSERT INTO users VALUES('" + username + "','" + encrypt + "')"
        c.execute(command)

        db.commit()
        db.close()
        return True
    else:
        db.close()
        return False

def auth_user(username, password):
    """
    Authenticates a username and password pair.
    Note that this does not differentiate between wrong password and non-existing username
    """
    db = sqlite3.connect(f)
    c = db.cursor()
    entered_password = sha256(password.encode('utf-8')).hexdigest()
    command = "SELECT password FROM users WHERE username = \'" + username + "\'"
    actual_password = c.execute(command).fetchone()
    return (actual_password[0] != None and entered_password == actual_password[0])

if __name__ == "__main__":
    f = "../data/db.db"
    create_db()
    #add_user("leo", "wat")
    #auth_user("leo", "wat")
