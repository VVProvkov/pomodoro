FROM python:3.12-alpine3.20
WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry install 

COPY gunicorn.conf.py /app/

