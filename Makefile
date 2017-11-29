.PHONY: help clean clean-build clean-pyc clean-test
.DEFAULT_GOAL := help


# AutoEnv
ifeq (${CI},) # This ensures the CI skips dotenv
	ENV ?= .env
	ENV_GEN := $(shell ./.env.gen ${ENV} .env.required)
endif


# AutoDoc
define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match: print("%-20s %s" % (match.groups()))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: ## remove all build, test, coverage and Python artifacts
	rm -rf build dist .eggs .cache .tox .coverage htmlcov coverage-reports
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

wipe: ## remove all files and changes not tracked in CVS
	@git clean -f

.PHONY: test
test: install-dev ## run tests quickly with the default Python
	@pipenv run py.test

pipenv: 
	@pip show pipenv -q || (pip install -U pipenv && echo '-----')

.PHONY: install
install: pipenv  ## install production packages
	@pipenv install

install-dev: pipenv  ## install development packages
	@pipenv install --dev

.PHONY: lint
lint: pipenv ## check style
	@pipenv check --style .

.PHONY: licence
license: install-dev ## check license incompatibilities
	@pipenv run yolk -l -f License | grep 'GPL' -B 1

.PHONY: test-coverage
test-coverage: install-dev ## check code coverage
	@pipenv run coverage run --source=patton -m pytest
	@pipenv run coverage report -m # --fail-under 80
	@pipenv run coverage xml -o coverage-reports/report.xml

.PHONY: version
version:
	@echo 0.0.1 #version

.PHONY: docs
docs: install-dev ## generate and shows documentation
	@make -C docs spelling html
	# Replace files with .md extension with .html extension
	@find ./docs/_build/ -name '*.html' -exec sed -i 's/\(\w*\)\.md\(W*\)/\1.html\2/g' {} \;
	@python -m webbrowser -t docs/_build/html/index.html
