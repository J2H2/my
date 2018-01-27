.PHONY: install
SHELL:=/bin/bash

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

all: install-dev run

install: python-package-install settings

install-dev: python-package-install-dev settings


# install
python-package-install:
	@pip3 install -r docs/requirements/production.txt

python-package-install-dev:
	@pip3 install -r docs/requirements/development.txt

settings:
	@cp docs/dev/settings/secrets.json ./secrets.json && python3.6 src/script/convert_secret_file.py


# run
run:
	@python3.6 src/manage.py runserver


# docker
docker-up:
	@docker-compose up --build
