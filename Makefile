.PHONY: install
SHELL:=/bin/bash

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

all: install run

install: python-package-install


# install
python-package-install:
	@pip3 install -r docs/requirements/development.txt

# run
run:
	@python3.6 src/manage.py runserver


# docker
docker-up:
	@docker-compose up --build
