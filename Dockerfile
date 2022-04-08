FROM python:3.9.1-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    ETERLAST_DEBUG=false \
    POETRY_HOME=/home/ether
ENV PATH="${POETRY_HOME}/bin:$PATH"

RUN apt-get update && apt-get install --no-install-recommends -y curl nginx
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py --output get-poetry.py
RUN python get-poetry.py --version 1.1.4 --yes

COPY nginx/server.conf /etc/nginx/sites-enabled/default

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY . .

ENTRYPOINT /app/entrypoint