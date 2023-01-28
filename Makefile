.PHONY: export-diagrams
export-diagrams:
	@docker-compose run --rm plantuml /usr/docs/assets/diagrams/*.puml

.PHONY: setup
setup:
	@pip install pre-commit

.PHONY: api-test
api-test:
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
	@cd api && alembic upgrade head

.PHONY: pipeline-test
pipeline-test:
	@cd ./pipeline && PYTHONPATH=src python -m pytest --cov ./pipeline

.PHONY: pipeline-mypy
pipeline-mypy:
	@cd ./pipeline && mypy .
