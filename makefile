
FORCE:

tests: FORCE
	flake8 *.py
	python3 NeedlessYouthUnemployment/test_app.py

prod: tests
	git commit -a
	git push origin main

dev_env: FORCE
	pip3 install --user -r requirements.txt