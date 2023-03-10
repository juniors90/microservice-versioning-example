SHELL:=/usr/bin/env bash

PROJECT ?= $(shell git rev-parse --show-toplevel)
DISTRO ?= ubuntu20.04
PYVERS = 3.10.9

.PHONY: black lint coverage unit test chlog
black:
	black entrypoint.py coverage_report.py application/ tests/

lint:
	flake8 entrypoint.py application/ tests/

coverage:
	python -m coverage_report

unit: coverage
	python -m unittest

test: unit


.PHONY: work37 work38 work
work37:
	docker run --pull --rm -it --volume $(PROJECT):/project/ qs5779/python-testing:ubuntu20.04-3.7.16 /bin/bash

work38:
	docker run --pull --rm -it --volume $(PROJECT):/project/ qs5779/python-testing:ubuntu20.04-3.8.16 /bin/bash

work:
	docker run --pull --rm -it --volume $(PROJECT):/project/ qs5779/python-testing:$(DISTRO)-$(PYVERS) /bin/bash

chlog:
	github_changelog_generator -u juniors90 -p microservice-versioning-example
	sed -i -e '/^$$/N;/^\n$$/D' ./CHANGELOG.md
	m2r2 --overwrite --anonymous-references CHANGELOG.md
	sed -i '/This Changelog was automatically generated by/d' ./CHANGELOG.rst

.PHONY: clean clean-build clean-pyc clean-test
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr docs/_build
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr coverage_report
	rm -fr .pytest_cache


.DEFAULT:
	@cd docs && $(MAKE) $@
