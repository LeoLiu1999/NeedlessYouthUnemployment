PROJ_DIR = NeedlessYouthUnemployment
LINTER = flake8 --ignore=E501

FORCE:

tests: lint
	cd $(PROJ_DIR); python3 test_app.py

run_local:
	cd $(PROJ_DIR); python3 app.py

prod: tests
	git commit -a
	git push origin main

lint: FORCE
	cd $(PROJ_DIR); $(LINTER) *.py

dev_env: FORCE
	pip3 install --user -r requirements.txt