FROM python:3.10.9-bullseye AS api-base

ENV PYTHONUNBUFFERED=true
ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt update && apt upgrade -y
RUN apt install -y build-essential libpq-dev python3-dev && rm -rf /etc/apt/source/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false --local

WORKDIR /usr/src/app
COPY . /usr/src/app
RUN poetry install

FROM api-base AS api

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
