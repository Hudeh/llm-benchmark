# LLM Benchmark Simulation Api

LLM Benchmark Simulation and Infrastructure Deployment

## Getting Started

### Prerequisites

- Python 3.x
- Docker
- Docker Compose
- Redis
- PostgreSQL

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Hudeh/llm-benchmark.git
    cd llm-benchmark
    ```

### Running the Project

Change the env_sample file name to .env:

1. **Using docker compose**

    ```bash
    docker-compose up --build
    ```

    This command will start the following services:

    FastAPI server on <http://localhost:8000>
    PostgreSQL for the database.
    Redis as the Celery message broker.
    Access the API documentation at <http://localhost:8000/docs>

2. **Run FastAPI Locally**

## Set up a Python virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the FastAPI server

```bash
uvicorn app.main:app --reload

```

## Start Celery worker

```bash
celery -A app.tasks.celery_tasks worker --loglevel=info
```

## Start Celery Beat

```bash
celery -A app.tasks.celery_tasks beat --loglevel=info
```

## Database Migrations

```bash
alembic upgrade head
```
