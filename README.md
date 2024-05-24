# Example FastAPI Project


This is a simple template for FastAPI projects. 
It contains the bare minimum needed to get started developing a modern async Python web API.

## Features

- Simple, extensible API structure with [FastAPI](https://github.com/tiangolo/fastapi)
- Fully asynchronous web server deployed with [Uvicorn](https://github.com/encode/uvicorn)
- Multi-stage Dockerfile for efficient image creation.
- Dependency management and tool config with [Poetry](https://github.com/python-poetry/poetry).
- [Pre-commit](https://github.com/pre-commit/pre-commit) hooks for enforcing standards.
- [Ruff](https://github.com/astral-sh/ruff) for code style and formatting.
- [MyPy](https://github.com/python/mypy) for static type checking.
- Example [sentry](https://github.com/getsentry/sentry) integration with FastAPI hooks.

### To come

- [ ] Example database integration
- [ ] Example auth with JWT
- [ ] Example integration testing with testcontainers

## Getting Started

Make sure you have installed the following:

- Docker
- Poetry
- Pre-commit

### Run it locally

1. Clone this repository:
2. Build the Docker image: `docker build -t my-fastapi-app .`
3. Run the Docker container: `docker run -p 8080:8080 my-fastapi-app`


### Start developing

1. Clone this repository.
2. Install pre-commit hooks: `pre-commit install`
3. Install dependencies: `poetry install`
4. Run the tests: `poetry run pytest tests/`
5. Add new dependencies with Poetry: `poetry add <package>`
6. Run the server locally: `poetry run uvicorn src.main:app --reload`

## Project Structure
The project is structured as follows:
```shell
├── Dockerfile
├── README.md
├── docs
├── mypy.ini
├── poetry.lock
├── pyproject.toml
├── src
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── __init__.py
│   │       ├── api.py
│   │       ├── models.py
│   │       └── routes
│   │           ├── __init__.py
│   │           └── health.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── middleware.py
│   └── main.py
└── tests
    └── test_v1_route_health.py
```

To add a new v1 route/endpoint, create a new module in `src/api/v1/routes` and simply import it in `src/api/v1/api.py`.
To add the v2 version of the route, create a new module in `src/api/v2/routes`, import it in `src/api/v2/api.py`, and add a new versioned route in `src/api/api.py`.