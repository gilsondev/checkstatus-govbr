FROM python:3.10.9-bullseye AS scheduler-base

ENV PYTHONUNBUFFERED=true
ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt update && apt upgrade -y
RUN apt install -y build-essential libpq-dev python3-dev && rm -rf /etc/apt/source/lists/*

WORKDIR /usr/src/app
COPY . /usr/src/app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry config virtualenvs.create false --local

FROM scheduler-base AS pipeline

RUN poetry install

FROM scheduler-base AS pipeline-local

RUN poetry install --with dev
