"""
This is the file containing all of the routes for the flask app.  
"""


from flask import Flask, render_template, flash, redirect, request, session, url_for # noqa: F401
from util import db_builder

app = Flask(__name__)
app.secret_key = "super secret key lmfao"


@app.route("/")
def home():
    """
    The home route. 
    This will return a render template that changes depending on the login status.
    """
    if ("user" in session):
        return render_template("index2.html", title="Welcome", status="logged_in")
    else:
        return render_template("index2.html", title="Welcome", status="not_logged_in")


# @app.route("/login")
# def login():
#     if ("user" not in session):
#         return render_template("login.html", title="Login")
#     else:
#         return render_template("index.html", title="Login", selection=None)


# @app.route("/auth", methods=["GET", "POST"])
# def auth():
#     if "user" in session:
#         return redirect("/")

#     form = request.form
#     username = form["User"]
#     password = form["Pass"]
#     if db_builder.auth_user(username, password):
#         session["user"] = username
#         return redirect("/")
#     else:
#         flash("invalid credentials!")
#         return redirect("/login")


# @app.route("/register")
# def register():
#     return render_template("register.html", title="Register")


# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     form = request.form
#     username = form['User']
#     password = form['Pass']
#     confpass = form['confPass']
#     if password != confpass:
#         flash('The 2 passwords that you entered do not match!')
#         return render_template('register.html')

#     if db_builder.add_user(username, password):
#         return redirect("/")
#     else:
#         flash('That username has already been taken!')
#     return render_template('register.html')


# @app.route("/find")
# def find():
#     return render_template("find.html", title="Find Internships")


# @app.route("/view")
# def create():
#     return render_template("view.html", title="Your applications")


# @app.route("/logout")
# def logout():
#     if "user" in session:
#         session.pop("user")
#     return redirect("/")


if __name__ == "__main__":
    app.debug = True
    app.run()
