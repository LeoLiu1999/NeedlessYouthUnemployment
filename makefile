PROJ_DIR = NeedlessYouthUnemployment
LINTER = flake8
COVER_PKG = $(shell pwd)

FORCE:

tests: lint
	cd $(PROJ_DIR); rm -f .coverage; python3 -m "nose" --exe --verbose --with-coverage --cover-package=$(COVER_PKG)
	#rm .coverage; python3 -m "nose" --exe --verbose --with-coverage --cover-package=$(COVER_PKG)/$(PROJ_DIR)

run_local:
	python3 $(PROJ_DIR)/app.py

prod: tests
	git checkout dev
	git commit -a
	git push origin dev

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