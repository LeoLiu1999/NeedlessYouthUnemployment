# enable control of an sqlite database
import sqlite3
# facilitates CSV I/O
# import csv
from hashlib import sha256

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
    # checks if username already exists
    command = "SELECT username FROM users WHERE username = \'" \
        + username + "\'"
    result = c.execute(command)
    if result.fetchone() is None:
        # encrypt password
        encrypt = sha256(password.encode('utf-8')).hexdigest()

        command = "INSERT INTO users VALUES('" + username \
            + "','" + encrypt + "')"
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
    Note that this does not differentiate between
    wrong password and non-existing username
    """
    db = sqlite3.connect(f)
    c = db.cursor()
    entered_password = sha256(password.encode('utf-8')).hexdigest()
    command = "SELECT password FROM users WHERE username = \'" \
        + username + "\'"
    actual_password = c.execute(command).fetchone()
    return (actual_password[0] is not None
            and entered_password == actual_password[0])


if __name__ == "__main__":
    f = "../data/db.db"
    create_db()
    # add_user("leo", "wat")
    # auth_user("leo", "wat")
