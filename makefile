PROJ_DIR = NeedlessYouthUnemployment
COVER_PKG = $(shell pwd)

FORCE:

tests: FORCE
	cd $(PROJ_DIR); make tests

run_local:
	python3 $(PROJ_DIR)/app.py

prod: tests
	git commit -a
	git push

usr_env:
	pip3 install --user -r requirements.txt

dev_env: FORCE
	pip3 install --user -r dev_requirements.txt

heroku:
	# install heroku:
	curl https://cli-assets.heroku.com/install.sh | sh
	heroku login
	heroku apps:create needless-youth-unemployment
	# set up heroku app as remote for this repo
	heroku git:remote -a needless-youth-unemployment
	heroku config:set PYTHONPATH="/app"
	heroku config:set HOME="/app"

docs:
	cd $(PROJ_DIR); pydoc3 -p 5001 *.py