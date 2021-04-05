PROJ_DIR = NeedlessYouthUnemployment
LINTER = flake8 --ignore=E501

FORCE:

tests: lint
	cd $(PROJ_DIR); python3 test_app.py

run_local:
	python3 $(PROJ_DIR)/app_new.py

prod: tests
	git commit -a
	git push origin main

lint: FORCE
	cd $(PROJ_DIR); $(LINTER) app.py; $(LINTER) test_app.py

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