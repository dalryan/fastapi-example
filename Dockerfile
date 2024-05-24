# base stage
FROM python:3.11-slim-buster as base

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED=0
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1
ENV PIPENV_VENV_IN_PROJECT=1
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1
ENV APP_PATH="/opt/app"
ENV VENV_PATH="/opt/app/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

WORKDIR $APP_PATH

# install base dependencies and poetry
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends curl && \
    curl -sSL https://install.python-poetry.org | python3 -

# use a non-root user
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser
RUN chown -R appuser:appgroup $APP_PATH

USER appuser

EXPOSE 8080

# dependencies stage
FROM base as deps

# install code dependencies
COPY --chown=appuser ["pyproject.toml", "poetry.lock", "README.md", "$APP_PATH"]
RUN poetry install --no-root --no-dev

# app stage
FROM deps as app

# just install the api code
COPY --chown=appuser src $APP_PATH/src/
RUN poetry install --only-root

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
