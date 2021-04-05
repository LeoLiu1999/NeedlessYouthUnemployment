# Needless Youth Unemployment

---

### Project Description

Needless Youth Unemployment is a 2021 Spring Senior Design project by Leo Liu, Rihui Zheng, Md Abedin, and Kyle Lin.

Deployment can be found [here](https://needless-youth-unemployment.herokuapp.com/).

---

### Requirements

Needless Youth Unemployment was written in Python 3.9 and requires the installation of flask to run, flake8 to test, and gunicorn to deploy. All three required modules can be installed using the [requirements file](requirements.txt).

### Local Launch Instructions

1. Clone the repository from Github.

```sh
# via ssh
git clone git@github.com:LeoLiu1999/NeedlessYouthUnemployment.git

# via https
git clone https://github.com/LeoLiu1999/NeedlessYouthUnemployment.git
```
2. Recommended: Use a virtual environment to install dependencies for the site (Optional).
To learn how to install virtual environment go [here](https://virtualenv.pypa.io/en/latest/installation.html) and to learn how to create a virtual environment go [here](https://virtualenv.pypa.io/en/latest/user_guide.html).
After creating a virtual environment, activate it (on a unix-based system) by running
```sh
$ . <name of virtual environment>/bin/activate
```

3. Navigate to the root directory of this repository and install the dependencies for Needless Youth Unemployment using pip by running
```sh
pip install -r requirements.txt
```

4. Launch the program (on a Unix-based system) using the makefile by running
```sh
make run_local
```

5. Visit the page locally by opening https://localhost:5000 in a web browser.

---

### Make Targets

tests: Target to run the [tests file](NeedlessYouthUnemployment/test_app.py).

run_local: Target to launch the program locally at https://localhost:5000

prod: Target to push all changes to Github. Travis listens to the **main** branch and deploys to the [Heroku app](https://needless-youth-unemployment.herokuapp.com/) if all tests pass.

lint: Target to run the linter, Flake8, to ensure that the code is clean.

dev_env: Target to set up the development environment by installing requirements.

heroku: Target to create a Heroku app if one does not already exist.

---

### Documents

* [Rough sketch of Database layout](Design%20Documents/DPDBUML.PNG)

* [Project Proposal](Design%20Documents/Project%20Proposal.pdf)

* [Project Management Plan](Design%20Documents/Software%20Project%20Management%20Plan.pdf)

* [System Requirements Specification](Design%20Documents/System%20Requirements%20Specification.pdf)
