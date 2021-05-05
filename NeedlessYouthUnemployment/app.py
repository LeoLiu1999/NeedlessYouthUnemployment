"""
This is the file containing all of the routes for the flask app.
"""


from flask import Flask, render_template, flash,\
                  redirect, request, session
from util import db_builder  # noqa: F401

app = Flask(__name__)


app.secret_key = "random string"


@app.route("/")
def home():
    """
    The /home route.

        Returns:
             Rendered template that changes depending on the login status.
    """
    if ("user" in session):
        return render_template("index.html",
                               title="Welcome", status="logged_in")
    else:
        return render_template("index.html",
                               title="Welcome", status="not_logged_in")


@app.route("/login")
def login():
    """
    The /login route.

        Returns:
             Rendered template for logging in
    """
    if ("user" not in session):
        return render_template("login.html", title="Login")
    else:
        return render_template("index.html",
                               title="Welcome", status="logged_in")


@app.route("/auth", methods=["GET", "POST"])
def auth():
    """
    The /auth route.
    This will authenticate the user, and:
    This will NOT return a rendered template.

        Returns:
             Redirect to / or /login as appropriate
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

        Returns:
             Rendered template with a form to register an account.
    """
    return render_template("register.html", title="Register")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    The /signup route.
    This will attempt to create an account for the user.
    This will NOT return a rendered template.

        Returns:
             Redirect to / or /register as appropriate
    """
    form = request.form
    username = form['Username']
    password = form['Password']
    confpass = form['ConfirmPassword']
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

        Returns:
             Rendered template with open internship opportunities.
    """
    if "user" in session:
        logged_in = True
    else:
        logged_in = False

    opportunities_raw = db_builder.get_all_pos()
    if opportunities_raw == []:
        opportunities = None
    else:
        opportunities = []
        for pos_raw in opportunities_raw:
            opportunity = []
            opportunity.append(["Link", pos_raw[0]])
            opportunity.append(["Company", pos_raw[1]])
            opportunity.append(["Position", pos_raw[2]])
            opportunity.append(["Date", pos_raw[3]])
            if (pos_raw[4] == "None"):
                opportunity.append(["Salary", "N/A"])
            else:
                opportunity.append(["Salary", "${:.2f}"
                                   .format(float(pos_raw[4]))])
            opportunities.append(opportunity)

    # opportunities = [[["Link", "https://fakelink.com/bogus.html"],
    #                   ["company", "totally real company"],
    #                   ["date", "Jan 1, 2022"],
    #                   ["pos", "Lorem ipsum generator"],
    #                   ["salary", "$123456"]]]

    return render_template("find.html",
                           title="Find Internships",
                           opportunities=opportunities,
                           logged_in=logged_in)


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    The /add route.
    Adds an internship opportunity to user

        Returns:
            Redirect to /view
    """
    form = request.form

    if "user" not in session:
        return redirect("/view")

    username = session["user"]
    link = form["Link"]
    company = form["Company"]
    position = form["Position"]
    date = form["Date"]
    salary = form["Salary"]

    db_builder.add_user_app(username, link, company,
                            position, date, salary)

    return redirect("/view")


@app.route("/view")
def view():
    """
    The /view route.

        Returns:
             Rendered template with the user's internship applications.
    """
    if "user" not in session:
        return redirect("/")

    applications_raw = db_builder.get_user_apps(session["user"])
    if applications_raw == []:
        applications = None
    else:
        applications = []
        for app_raw in applications_raw:
            application = []
            application.append(["Link", app_raw[1]])
            application.append(["Company", app_raw[2]])
            application.append(["Position", app_raw[3]])
            application.append(["Date", app_raw[4]])
            application.append(["Salary", app_raw[5]])
            application.append(["Status", app_raw[6]])
            applications.append(application)

    # applications = [[["Link", "fake link"],
    #                  ["company", "dummy company"],
    #                  ["position", "Lorem ipsum"],
    #                  ["date", "Jan 1, 2000"]],
    #                 [["Link", "fake link2"],
    #                  ["company", "dummy company2"],
    #                  ["position", "Lorem ipsum2"],
    #                  ["date", "Jan 1, 2001"]]]

    return render_template("view.html",
                           title="Your Applications",
                           applications=applications)


@app.route("/logout")
def logout():
    """
    The /logout route.
    This will log the user out and redirect them to the homepage.

        Returns:
             Redirect to /
    """
    if "user" in session:
        session.pop("user")
    return redirect("/")


if __name__ == "__main__":
    app.debug = True
    app.run()
