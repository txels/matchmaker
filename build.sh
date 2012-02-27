#!/bin/bash
nosetests --with-coverage --cover-html --cover-erase --cover-package=matchmaker matchmaker
(cd docs; make clean html)
flake8 matchmaker || echo "Flake8 errors"
