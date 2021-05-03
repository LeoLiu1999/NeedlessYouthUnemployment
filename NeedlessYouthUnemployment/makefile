LINTER = flake8
COVER_PKG = $(shell pwd)

FORCE:

lint: FORCE
	$(LINTER) app.py; $(LINTER) test_app.py; $(LINTER) util/db_builder.py

tests: lint
	rm -f .coverage; python3 -m "nose" --exe --verbose --with-coverage --cover-package=$(COVER_PKG)
	#rm .coverage; python3 -m "nose" --exe --verbose --with-coverage --cover-package=$(COVER_PKG)

