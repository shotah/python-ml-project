
# Load environment variables from .env (suppress errors if .env doesn't exist)
-include .env

# Define default values for your variables (optional, but good practice)
HUGGING_FACE_TOKEN ?= ""  # Provide a default if the variable isn't in .env

############################
# UTILS
############################
PHONY: tree
tree:
	tree -a -I .git

PHONY: clean
clean:
	rm -rf ./api/.venv ./api/Pipfile.lock
	rm -rf ./llm/.venv ./llm/Pipfile.lock

############################
# API 
############################
PHONY: api-install
api-install:
	cd ./api && pipenv install

PHONY: api-test
api-test:
	cd ./api && pipenv run pytest


############################
# LLM
############################
PHONY: llm-install
llm-install:
	cd ./llm && pipenv install

PHONY: llm-test
llm-test:
	cd ./llm && pipenv run pytest


PHONY: llm-build
llm-build:
	cd ./llm && docker build --build-arg HUGGING_FACE_TOKEN="$(HUGGING_FACE_TOKEN)" -t llm_test .



############################
# Docker
############################
PHONY: docker-clean
docker-clean:
	docker system prune -a


############################
# Docker compose
############################
PHONY: build
build:
	docker-compose build

PHONY: up
up:
	docker-compose up -d

PHONY: down
down:
	docker-compose down

PHONY: reup
reup:
	docker-compose up -d --build
