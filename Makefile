PORT ?= 8080
PYTHON ?= python3.12

.PHONY: install db run test lint typecheck

install:
	$(PYTHON) -m venv .venv && .venv/bin/pip install --upgrade pip && .venv/bin/pip install -e ".[dev]"

db:
	docker compose up -d postgres

run:
	.venv/bin/uvicorn app.main:create_app --factory --reload --port $(PORT)

test:
	.venv/bin/pytest

lint:
	.venv/bin/ruff check .

typecheck:
	.venv/bin/mypy app
