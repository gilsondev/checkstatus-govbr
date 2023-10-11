.PHONY: export-diagrams
export-diagrams:
	@docker-compose run --rm plantuml /usr/docs/assets/diagrams/*.puml

.PHONY: setup
setup:
	@pip install pre-commit

.PHONY: api-test
api-test: migrate
	@cd ./api && pytest --cov ./api

.PHONY: api-mypy
api-mypy:
	@cd ./api && mypy .

.PHONY: api-serve
api-serve:
	@uvicorn --app-dir api src.main:app --reload

.PHONY: makemigrations
makemigrations:
	@cd api && alembic revision --autogenerate -m "$(msg)"

.PHONY: migrate
migrate:
	@cd api && DEBUG=True alembic upgrade head && DEBUG=False alembic upgrade head

.PHONY: pipeline-test
pipeline-test: migrate
	@cd ./pipeline && python -m pytest --cov ./ --import-mode=importlib

.PHONY: pipeline-mypy
pipeline-mypy:
	@cd ./pipeline && mypy .

.PHONY: scheduler-test
scheduler-test: migrate
	@cd ./scheduler &&  python -m pytest --cov ./scheduler
