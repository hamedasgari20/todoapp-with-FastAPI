# FastAPI Todo Application
## Overview
This is a simple Todo application built with FastAPI, a modern Python web framework. The application allows users to manage their tasks, including creating, reading, updating, and deleting tasks. It also demonstrates how to use SQLAlchemy for database operations and Alembic for database migrations.


## Project structure
The project is organized as follows:
- **app/:** Contains the main FastAPI application code.
- **main.py:** Defines FastAPI application, endpoints, and request/response models.
- **database.py:** Manages database connections and SQLAlchemy session creation.
- **models.py:** Defines SQLAlchemy models for tasks.
- **alembic/:** Contains Alembic migration scripts and configuration.
- **versions/:** Stores individual migration scripts.
- **env.py:** Alembic configuration file.
- **docker-compose.yml:** Docker Compose file for running the application and PostgreSQL database in containers.
- **alembic.ini:** Alembic configuration file for managing database migrations.
- **requirements.txt:** Lists project dependencies.
- **README.md:** This file.

## Getting Started
To run the Todo application, follow these steps:

1- Clone the repository to your local machine:
```angular2html
git clone https://github.com/hamedasgari20/todoapp-with-FastAPI.git
```

2- Install project dependencies using **pip**:
```angular2html
pip install -r requirements.txt

```

3- Start the application and PostgreSQL database using Docker Compose:
```angular2html
docker-compose up -d
```

4- Create migration file:
```angular2html
alembic revision --autogenerate -m "first migrations"
```

5- Apply the initial database migration using Alembic:
```angular2html
alembic upgrade head
```

6- Start the FastAPI server:
```angular2html
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
The application documentation should now be accessible at http://localhost:8000/docs in your web browser.



## Creating and Applying Migrations
If you need to make changes to the database schema or add new tables, you can create and apply migrations using Alembic. Follow these steps:

1- Create a new migration script:
```angular2html
alembic revision --autogenerate -m "your_migration_name"
```
This generates a new migration script in the **alembic/versions/** directory.

2- Open the newly created migration script and define the database schema changes in the **upgrade()** function. For example, to add a new table, use SQLAlchemy's **create_table** function.

3- Apply the migration to the database:
```angular2html
alembic upgrade head
```
The changes should now be applied to the database.



## Usage
Use the provided API documentation at http://localhost:8000/docs to interact with the Todo application. You can create, retrieve, update, and delete tasks.


## Acknowledgments
- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://www.sqlalchemy.org/
- Alembic: https://alembic.sqlalchemy.org/

I hope you enjoy

##### Hamed Asgari