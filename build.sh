#!/bin/bash
nosetests --with-coverage --cover-html --cover-erase --cover-package=matchmaker matchmaker
flake8 matchmaker || echo "Flake8 errors"
