
# Load environment variables from .env (suppress errors if .env doesn't exist)
-include .env

# Define default values for your variables (optional, but good practice)
HUGGING_FACE_TOKEN ?= ""  # Provide a default if the variable isn't in .env
MEMORY_LIMIT ?= 16g # Default value

############################
# UTILS
############################
PHONY: tree
tree:
	tree -a -I .git

.PHONY: clean
clean:
	rm -rf ./api/.venv ./api/Pipfile.lock
	rm -rf ./llm/.venv ./llm/Pipfile.lock
	rm -rf ./webui/frontend/node_modules

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
	cd ./llm && docker build  --no-cache \
	--build-arg HUGGING_FACE_TOKEN="$(HUGGING_FACE_TOKEN)" \
	-t llm_test:latest -f ./dockerfile .

############################
# Web UI
############################

.PHONY: webui-build
webui-build:
	cd webui && \
	npm run build

.PHONY: webui-dev
webui-dev: webui-build
	cd webui && \
	npm run start

.PHONY: webui-install
webui-install:
	cd webui && \
	npm install

.PHONY: webui-test
webui- test:
	cd webui && \
	npm run test

.PHONY: webui-lint
webui-lint:
	cd webui && \
	npm run lint

.PHONY: webui-fix
webui-fix:
	cd webui && \
	npm run fix

.PHONY: webui-upgrade
webui-upgrade:
	cd webui && \
	npm prune && \
	(npm list -g npm-check-updates || npm i npm-check-updates)  && \
	npx ncu -u  && \
	npm update

############################
# Installation and Setup
############################
PYTHON_VERSION := 3.12  # Define PYTHON_VERSION
VENV_DIR := llm/venv	  # Define VENV_DIR

.PHONY: setup
setup: venv requirements webui-install install-npx ## Setup the entire development environment

.PHONY: venv
venv: ## Create Python virtual environment
	@echo "Creating Python virtual environment..."
	python${PYTHON_VERSION} -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"

.PHONY: requirements
requirements: venv ## Install Python requirements
	@echo "Installing Python requirements..."
	$(VENV_DIR)/bin/pip install -r llm/requirements.txt api/requirements.txt # Install requirements for both api and llm
	@echo "Python requirements installed."

.PHONY: install-nodejs-apt
install-nodejs-apt: ## Install Node.js and npm using apt (Ubuntu/Debian)
	@echo "Installing Node.js and npm using apt..."
	sudo apt update
	sudo apt install nodejs npm
	@echo "Node.js and npm installed via apt."

.PHONY: install-npx
install-npx: install-nodejs-apt ## Install npx globally using npm
	@echo "Installing npx globally using npm..."
	sudo npm install -g npx
	@echo "npx installed globally."

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

PHONY: list
list:
	docker-compose ps

.DEFAULT_GOAL := help