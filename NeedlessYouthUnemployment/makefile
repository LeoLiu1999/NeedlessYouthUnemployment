LINTER = flake8
COVER_PKG = $(shell pwd)
NOSE_FLAGS = --with-coverage --verbose --exe --cover-package=.

FORCE:

lint: FORCE
	$(LINTER) app.py;
	$(LINTER) tests/test_app.py;
	$(LINTER) util/db_builder.py

tests: lint
	rm -f .coverage
	python3 -m "nose" ${NOSE_FLAGS}

