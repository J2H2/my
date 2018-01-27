.PHONY: install
SHELL:=/bin/bash

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

all: install-dev run

install: python-package-install

install-dev: python-package-install


# install
python-package-install:
	@pip3 install -r docs/requirements/production.txt

python-package-install-dev:
	@pip3 install -r docs/requirements/development.txt


# run
run:
	@python3.6 src/manage.py runserver


# docker
docker-up:
	@docker-compose up --build
