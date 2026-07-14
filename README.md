# School Registration API

A modular school management API built with FastAPI and SQLite. This project implements a clean, layered software architecture by partitioning core functionalities into
dedicated directories to ensure maintainability and separation of concerns.


 Project Architecture

* main.py – The application entry point that initializes FastAPI, triggers table setup, and mounts feature routers.
*database.py/ – Manages the transactional SQLite connection context lifecycle (commit/rollback handling).
* routers/ – Layer handling HTTP request configurations and endpoints using isolated FastAPI APIRouter instances.
* schemas/ – Pydantic structural models ensuring strict data validation for incoming JSON payloads.
* repositories/– Data Access Object (DAO) layer containing raw SQL query executions and database transactions.
* models/ – Structural schemas defining database tables initialized during runtime startup.

Getting Started

1. Run the Development Server
Activate your virtual environment and start the service with the following terminal command:


fastapi dev


2. Access the Interactive Documentation
Once the server is running, you can explore, test, and execute live API calls via the automated Swagger UI panel at:

 http://127.0.0.1:8000/docs
