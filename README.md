# eduMetricsApi.UFU

Base API built with [FastAPI](https://fastapi.tiangolo.com/) that exposes student resources, connects to a SQL database through SQLAlchemy, and manages schema changes with Alembic migrations.

## Prerequisites

- Python 3.10 or newer
- Recommended: create and activate a virtual environment before installing dependencies

## Installation

```bash
pip install -r requirements.txt
```

Optionally copy `.env.example` to `.env` and adjust the values. By default the project uses an SQLite database stored at `./data/edumetrics.db`.

## Database Migrations

The project ships with Alembic already configured.

```bash
# Apply all migrations
alembic upgrade head

# Create a new revision (example)
alembic revision -m "describe change" --autogenerate
```

## Running the API

```bash
uvicorn app.main:app --reload
```

Once the server is running you can:

- Check the health endpoint: `GET http://127.0.0.1:8000/health`
- Interact with the student endpoints under `http://127.0.0.1:8000/api/students`
- Explore the interactive docs at `http://127.0.0.1:8000/docs`

## Project Structure

```
app/
├── api/              # FastAPI routers and endpoints
├── core/             # Configuration and settings
├── db/               # Database session helpers and model registry
├── models/           # SQLAlchemy models
└── schemas/          # Pydantic schemas
alembic/              # Alembic environment and migrations
requirements.txt      # Python dependencies
```
