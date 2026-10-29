.PHONY: check backend frontend

check: backend frontend

backend:
	uv run ruff check .
	uv run mypy
	uv run pytest

frontend:
	cd frontend && npm run lint && npm run typecheck && npm test
