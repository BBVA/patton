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

require-%:
	$(if $(shell command -v $* 2> /dev/null), , $(error Please install `$*` ***))

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


.PHONY: codecov
codecov: ## push to codecov the coverage
	@pipenv run codecov

.PHONY: version
version:
	@echo 0.0.1 #version

bump-%:
	@pipenv run bumpversion $*
	@git push
	@git push --tags


.PHONY: run
run: require-pipenv ## Run locally a web instance
	@pipenv run python main.py


.PHONY: compose
compose: ## run locally your application
	@docker-compose up -d --build


.PHONY: compose-init
compose-init: ## populate db
	@docker-compose run patton \
		bash -c "bash ./load_assets.sh ; python main.py -r"


.PHONY: repl
repl: require-pipenv ## Run locally a web instance
	@pipenv run ipython


.PHONY: watch
watch: require-ag require-entr ## Reload on code changes
	@ag -l -G py | entr -r make run

.PHONY: recreate
recreate: install ## reinstalls the db
	@pipenv run ./load_assets.sh
	@pipenv run python main.py -r

.PHONY: docs
docs: install-dev ## generate and shows documentation
	@pipenv run make -C docs spelling html
	# Replace files with .md extension with .html extension
	-@find ./docs/_build/ -name '*.html' -exec sed -i 's/\(\w*\)\.md\(W*\)/\1.html\2/g' {} \;
	@python -m webbrowser -t docs/_build/html/index.html
