LINTER = flake8
COVER_PKG = $(shell pwd)
NOSE_FLAGS = -w /Tests --with-coverage --cover-package=.

FORCE:

lint: FORCE
	$(LINTER) app.py;
	$(LINTER) Tests/test_app.py;
	$(LINTER) util/db_builder.py

tests: lint
	rm -f .coverage
	python3 -m "nose" ${NOSE_FLAGS}

