.PHONY: clean
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

.PHONY: upload-pypi
upload-pypi:
	pip install --upgrade pip setuptools wheel
	pip install twine
	sh deploy/pypi_upload.sh

.PHONY: upload-docker
upload-docker:
	docker login -u $${DOCKER_USER} -p $${DOCKER_PASS}
	docker build -t patton-cli .
	docker tag patton-cli bbvalabs/patton-cli:`cat VERSION`
	docker push bbvalabs/patton-cli:`cat VERSION`
	docker tag patton-cli bbvalabs/patton-cli:latest
	docker push bbvalabs/patton-cli:latest
