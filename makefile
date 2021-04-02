PROJ_DIR = NeedlessYouthUnemployment
LINTER = flake8 --ignore=E501

FORCE:

tests: lint
	python3 test_app.py

run_local:
	python3 $(PROJ_DIR)/app.py

prod: tests
	git commit -a
	git push origin main

lint: FORCE
	cd $(PROJ_DIR); $(LINTER) *.py

dev_env: FORCE
	pip3 install --user -r requirements.txt

heroku:
	# install heroku:
	curl https://cli-assets.heroku.com/install.sh | sh
	heroku login
	heroku apps:create needless-youth-unemployment
	# set up heroku app as remote for this repo
	heroku git:remote -a needless-youth-unemployment
	heroku config:set PYTHONPATH="/app"
	heroku config:set HOME="/app"
