#!/bin/bash

black --config pyproject.toml .

flake8 --config setup.cfg .

isort --atomic --case-sensitive --force-alphabetical-sort-within-sections --force-single-line-imports --lines-after-imports 2 --lines-between-types 1 --line-width 79 --skip-glob "build/*" .
