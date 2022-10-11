.PHONY: export-diagrams
export-diagrams:
	@docker-compose run --rm plantuml /usr/docs/assets/diagrams/*.puml

.PHONY: api-test
api-test:
	@cd ./api && pytest	

.PHONY: api-mypy
api-mypy:
	@cd ./api && mypy .
