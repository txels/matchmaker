all: test lint docs

test:
	pytest -sv

docs:
	(cd docs; make clean html)

lint:
	flake8 matchmaker || echo "Flake8 errors"

.PHONY: docs lint test
