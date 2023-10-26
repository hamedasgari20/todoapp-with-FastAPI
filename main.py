from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models

app = FastAPI()

# Configure the database connection
DATABASE_URL = "postgresql://user:password@localhost/db"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@app.post("/tasks/", response_model=models.Task)
def create_task(task: models.Task):
    db = SessionLocal()
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task


@app.get("/tasks/{task_id}", response_model=models.Task)
def read_task(task_id: int):
    db = SessionLocal()
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    db.close()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=models.Task)
def update_task(task_id: int, updated_task: models.Task):
    db = SessionLocal()
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        db.close()
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in updated_task.dict().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    db.close()
    return task


@app.delete("/tasks/{task_id}", response_model=models.Task)
def delete_task(task_id: int):
    db = SessionLocal()
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        db.close()
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    db.close()
    return task
