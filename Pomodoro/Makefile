run:
	poetry run uvicorn main:app --env-file .local.env

migrate-create:
	alembic revision --autogenerate -m $(MIGRATION)

migrate-apply:
	alembic upgrade head