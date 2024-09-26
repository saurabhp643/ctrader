# FastAPI Event-Driven Application

This is a scalable event-driven architecture built using FastAPI for API services and Celery for background task processing. It supports event-based rules evaluation and task scheduling, making it ideal for microservices architectures that need to handle events asynchronously.

## Table of Contents
- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [How it Works](#how-it-works)
- [API Endpoints](#api-endpoints)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Future Improvements](#future-improvements)

## Features
- **FastAPI**: For building REST APIs with support for asynchronous programming.
- **Celery**: For distributed task queue processing.
- **Event-Driven Architecture**: Events trigger background tasks via Celery.
- **Modular Design**: Easy to extend and maintain.
- **Dockerized**: Simplified deployment and scaling using Docker and Docker Compose.

## Architecture Overview
This application follows a modular and event-driven architecture. The main components are:

- **API Layer**: Built using FastAPI, this layer handles client requests. It includes versioned endpoints (/v1) to handle different modules (accounts, rules, events).
- **Event Producer & Consumer**: Celery workers handle background tasks, which are triggered by events produced by the API layer. Events are queued using Redis as a message broker.
- **Database**: PostgreSQL is used as the main data store to persist account information, rules evaluation, and event details.

### Flow
1. A client sends a request to the FastAPI application.
2. Based on the request, an event is produced and sent to a Celery queue.
3. Celery workers consume events and perform background processing (such as rule evaluation or account tasks).
4. Workers may produce new events, triggering additional tasks.
5. Results are stored in the database and can be queried via APIs.

## Project Structure
```bash
fastapi-event-driven-app/
│
├── app/
│   ├── api/                # API layer (request handlers)
│   │   ├── v1/
│   │   │   └── endpoints/  # Endpoints for version 1 of the API
│   │   │       ├── accounts.py
│   │   │       ├── events.py
│   │   │       └── rules.py
│   ├── core/               # Core services like Celery setup and configuration
│   │   ├── config.py       # Application configurations
│   │   ├── event_producer.py # Publishes events to Celery
│   │   ├── event_consumer.py # Event consumers (Celery workers)
│   │   ├── logger.py       # Logging setup
│   │   └── scheduler.py    # Scheduling background tasks
│   ├── models/             # ORM models (e.g., SQLAlchemy or Pydantic)
│   │   ├── account.py
│   │   ├── rule_evaluation.py
│   │   └── events.py
│   ├── workers/            # Celery worker logic for background jobs
│   │   ├── account_worker.py
│   │   ├── rules_worker.py
│   │   └── won_event_worker.py
│   ├── celery_app.py       # Celery app instance setup
│   ├── db.py               # Database setup and connection handling
│   └── __init__.py         # App initialization
│
├── main.py                 # Application entry point
├── Dockerfile              # Dockerfile to build the application image
├── docker-compose.yml      # Docker Compose for running multi-container setup
├── Makefile                # Simple make commands to manage the app
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables
```

## Key Components
- **API**: The FastAPI app exposes REST endpoints that accept requests and trigger background jobs (events).
- **Core**: Contains configurations, event producers/consumers, and logging.
- **Models**: Defines database entities such as Account, RuleEvaluation, and Event.
- **Workers**: Celery workers that execute background tasks like event handling and account operations.
- **Database**: Managed via SQLAlchemy or an ORM for storing and querying data.

## Technologies Used
- **FastAPI**: High-performance Python web framework for APIs.
- **Celery**: Distributed task queue for processing background jobs.
- **Redis**: Message broker for Celery.
- **PostgreSQL**: Relational database.
- **Docker**: For containerization of the application.
- **Uvicorn**: ASGI server for running FastAPI.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Docker
- Docker Compose

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/fastapi-event-driven-app.git
    cd fastapi-event-driven-app
    ```
2. Create a .env file with your environment variables:
    ```bash
    cp .env.example .env
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application using Docker Compose:
    ```bash
    docker-compose up --build
    ```
    This will spin up the following services:
    - FastAPI app on http://localhost:8000
    - Celery worker
    - Redis (Message broker)
    - PostgreSQL (Database)

5. Run Celery worker: In a new terminal window, run:
    ```bash
    docker-compose exec web celery -A app.celery_app worker --loglevel=info
    ```

## How it Works
### 1. Event Production and Consumption
API endpoints such as /accounts or /rules trigger business logic, which in turn produces events. Events are pushed to Redis, acting as the message broker for Celery. Celery workers consume these events, processing them in the background. For example, rules evaluations, account operations, or handling new won events.

### 2. Core Components
- **Event Producer (event_producer.py)**: Publishes events to the message broker.
- **Event Consumer (event_consumer.py)**: Celery workers listening for and processing events.
- **Logger (logger.py)**: Centralized logging for tracking application behavior.
- **Scheduler (scheduler.py)**: Handles periodic tasks, e.g., to evaluate rules every X minutes.

## API Endpoints
- **GET /accounts**: Retrieves account information.
    ```bash
    curl http://localhost:8000/accounts
    ```
- **POST /accounts**: Creates a new account and triggers background tasks.
    ```bash
    curl -X POST http://localhost:8000/accounts -d '{"name": "John Doe"}'
    ```
- **POST /events**: Handles event creation and triggers background workers.
- **POST /rules**: Triggers rule evaluation based on events.

## Running the Application
- **Start FastAPI**:
    ```bash
    make run
    ```
    Alternatively:
    ```bash
    uvicorn main:app --reload
    ```
- **Run Tests**: You can add tests to the tests folder and run them using:
    ```bash
    pytest
    ```

## Future Improvements
- **Scaling Workers**: Scale Celery workers to handle a higher load by running multiple instances.
- **Add More Events**: Expand the event-driven architecture by adding more events and background tasks.
- **Security**: Add JWT authentication for securing the API.
- **Monitoring**: Set up Prometheus or Grafana for monitoring the task queue and application performance.
# ctrader
