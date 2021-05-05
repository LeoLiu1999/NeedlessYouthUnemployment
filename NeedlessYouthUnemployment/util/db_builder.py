# enable control of an sqlite database
import sqlite3
import os
# facilitates CSV I/O
# import csv
from hashlib import sha256

path = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..',
    'data'))
f = os.path.join(path, 'db.db')


def create_db():
    """
    Initializes tables in database.
    """
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        password TEXT,
        PRIMARY KEY(username)
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS positions(
        link TEXT,
        company_name TEXT,
        pos_name TEXT,
        apply_by TEXT,
        salary REAL,
        PRIMARY KEY(link)
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS applications(
        user TEXT,
        link TEXT,
        company_name TEXT,
        pos_name TEXT,
        apply_by TEXT,
        salary REAL,
        status TEXT,
        PRIMARY KEY(user, link)
    )""")

    db.commit()
    db.close()
    return True


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


def remove_user(username, password):
    """
    Attempts to remove a username and password pair from
    the database
    """
    db = sqlite3.connect(f)
    c = db.cursor()
    # Checks if username exists
    command = "SELECT username,password FROM users WHERE username = \'" \
        + username + "\'"
    result = c.execute(command)
    if result.fetchone() is not None:
        encrypt = sha256(password.encode('utf-8')).hexdigest()
        result = c.execute(command)
        if encrypt == result.fetchone()[1]:
            command = "DELETE FROM users WHERE username = \'" \
                + username + "\'"
            c.execute(command)

            db.commit()
            db.close()
            return True
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


def add_pos(link, company, date, pos, sal=None):
    """
    Adds a new position to the database
    Param: All the information needed for a position
    Return: True if successful
    """
    db = sqlite3.connect(f)
    c = db.cursor()

    # Removes entry if it already exists
    c.execute("DELETE FROM positions WHERE link = \'" + link + "\'")

    c.execute("INSERT INTO positions VALUES ('{}', '{}', '{}', '{}', '{}')"
              .format(link, company, pos, date, sal))

    db.commit()
    db.close()
    return True


def del_pos(link):
    """
    Deletes a position from the database
    Param: Position link
    Return: True if successful
    """
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("DELETE FROM positions WHERE link = \'" + link + "\'")
    db.commit()
    db.close()
    return True


def get_all_pos():
    """
    Gets every single position in database
    Returns: List of tuples of every position
    """
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("SELECT * FROM positions")
    positions = c.fetchall()
    db.close()
    return positions


def add_user_app(username, link, company=None, pos=None, date=None, sal=None):
    """
    Deletes an application from the database
    Param: Username, position link
    Return: True if successful, False if app already exists
    """
    db = sqlite3.connect(f)
    c = db.cursor()

    # Tests if entry if it already exists
    c.execute("SELECT * FROM applications WHERE user = '{}' AND link = '{}'"
              .format(username, link))
    record = c.fetchall()

    if (len(record)):
        db.close()
        return False

    # c.execute("SELECT * FROM positions WHERE link = \'" + link + "\'")
    # pos = c.fetchall()
    # link, company, date, pos, sal = pos[0]

    cmd = "INSERT INTO applications VALUES " +\
          "('{}','{}','{}','{}','{}','{}','{}')"
    c.execute(cmd.format(username, link,
              company, pos, date, sal, 'Not Submitted'))

    db.commit()
    db.close()
    return True


def get_user_apps(username):
    """
    Gets the user's applications
    Param: Username
    Return: List of tuples of the user's applications
    """
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("SELECT * FROM applications WHERE user = '{}'".format(username))
    apps = c.fetchall()
    db.close()
    return apps


def del_user_app(username, link):
    """
    Deletes a user's application from the database
    Param: Username, link
    Return: True if successful
    """
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("DELETE FROM applications WHERE user = '{}' AND link = '{}'"
              .format(username, link))
    db.commit()
    db.close()
    return True


if __name__ == "__main__":
    # f = "../data/db.db"
    create_db()
    # add_user("leo", "wat")
    # auth_user("leo", "wat")
