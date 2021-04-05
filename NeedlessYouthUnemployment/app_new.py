"""
This is the file containing all of the routes for the flask app. 
"""


from flask import Flask, render_template, flash, redirect, request, session, url_for  # noqa: F401
from util import db_builder  # noqa: F401
import os

app = Flask(__name__)

def make_secret_key():
    return os.urandom(32)

app.secret_key = make_secret_key()


@app.route("/")
def home():
    """
    The /home route.
    This will return a rendered template that changes depending on the login status.
    """
    if ("user" in session):
        return render_template("index2.html", title="Welcome", status="logged_in")
    else:
        return render_template("index2.html", title="Welcome", status="not_logged_in")


@app.route("/login")
def login():
    """
    The /login route.
    This will return a rendered template that lets the user log in if they are not logged in already.
    """
    if ("user" not in session):
        return render_template("login2.html", title="Login")
    else:
        return render_template("index2.html", title="Welcome", status="logged_in")


@app.route("/auth", methods=["GET", "POST"])
def auth():
    """
    The /auth route.
    This will authenticate the user, and:
    On successful authentication, redirect to home page.
    On failed login, redirect to /login with message.
    This will NOT return a rendered template.
    """
    if "user" in session:
        return redirect("/")

    form = request.form
    username = form["Username"]
    password = form["Password"]
    if db_builder.auth_user(username, password):
        session["user"] = username
        return redirect("/")
    else:
        flash("invalid credentials!")
        return redirect("/login")


@app.route("/register")
def register():
    """
    The /register route.
    This will return a returned template with a form to register an account.
    """
    return render_template("register2.html", title="Register")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    The /signup route.
    This will create an account for the user, and:
    On successful creation, redirect to home page.
    On failed login, redirect to /register with an appropriate message.
    This will NOT return a rendered template.
    """
    form = request.form
    username = form['Username']
    password = form['Password']
    confpass = form['Confirm-Password']
    if password != confpass:
        flash('The 2 passwords that you entered do not match!')
        return redirect("/register")

    if db_builder.add_user(username, password):
        return redirect("/")
    else:
        flash('That username has already been taken!')
    return redirect("/register")


@app.route("/find")
def find():
    """
    The /view route.
    This will return a returned template with open internship opportunities.
    """
    return render_template("find2.html", title="Find Internships")


@app.route("/view")
def view():
    """
    The /view route.
    This will return a returned template with the user's internship applications.
    """
    return render_template("view2.html", title="Your Applications")


@app.route("/logout")
def logout():
    """
    The /logout route.
    This will log the user out.
    This will NOT return a rendered template.
    """
    if "user" in session:
        session.pop("user")
    return redirect("/")


if __name__ == "__main__":
    app.debug = True
    app.run()
