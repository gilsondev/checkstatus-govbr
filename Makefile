.PHONY: export-diagrams
export-diagrams: ## Export diagrams
	@docker-compose run --rm plantuml /usr/docs/assets/diagrams/*.puml

.PHONY: deps
deps: ## Install dependencies
	@echo "\033[0;32mInstalling pre-commit...\033[0m"
	@pip install pre-commit
	@echo "\033[0;32mInstalling API dependencies...\033[0m"
	@cd ./api && poetry install -q
	@echo "\033[0;32mInstalling pipeline dependencies...\033[0m"
	@cd ./pipeline && poetry install -q
	@echo "\033[0;32mInstalling scheduler dependencies...\033[0m"
	@cd ./scheduler && poetry install -q
	@echo "\033[0;32mInstalling frontend dependencies...\033[0m"
	@cd ./frontend && yarn install -s

.PHONY: pre-commit
pre-commit: ## Prepare pre-commit
	@echo "\033[0;32mPreparing pre-commit...\033[0m"
	@pre-commit install

.PHONY: api-test
api-test: migrate ## Run API tests
	@cd ./api && pytest --cov ./api

.PHONY: api-mypy
api-mypy: ## Run mypy on API code
	@cd ./api && mypy .

.PHONY: api-serve
api-serve: ## Serve API
	@uvicorn --app-dir api src.main:app --reload

.PHONY: makemigrations
makemigrations: ## Generate Alembic migration
	@cd api && alembic revision --autogenerate -m "$(msg)"

.PHONY: migrate
migrate: ## Run Alembic migration
	@cd api && DEBUG=True alembic upgrade head && DEBUG=False alembic upgrade head

.PHONY: pipeline-test
pipeline-test: migrate ## Run pipeline tests
	@cd ./pipeline && python -m pytest --cov ./ --import-mode=importlib

.PHONY: pipeline-mypy
pipeline-mypy: ## Run mypy on pipeline code
	@cd ./pipeline && mypy .

.PHONY: scheduler-test
scheduler-test: migrate ## Run scheduler tests
	@cd ./scheduler &&  python -m pytest --cov ./scheduler

.PHONY: web-serve
web-serve: ## Serve frontend
	@cd ./frontend && yarn dev

.PHONY: setup
setup: deps pre-commit ## Install dependencies and prepare pre-commit

help: ## Show help message
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage: make [command] \033[36m\033[0m\n"} /^[$$()% a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
