LINTER = flake8
PROJ_DIR = NeedlessYouthUnemployment
COVER_PKG = $(shell pwd)
NOSE_FLAGS = -w $(PROJ_DIR)/Tests --with-coverage --cover-package=.

FORCE:

lint: FORCE
	$(LINTER) app.py;
	$(LINTER) Tests/test_app.py;
	$(LINTER) util/db_builder.py

tests: lint
	rm -f .coverage
	python3 -m "nose" ${NOSE_FLAGS}

