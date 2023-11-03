from fastapi import FastAPI
from fastapi import HTTPException
from app.crud.task import create_task_crud, read_task_crud, update_task_crud, delete_task_crud
from app.db.database import SessionLocal
from app.schemas.task import TaskResponse

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskResponse):
    return create_task_crud(task)


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int):
    task = read_task_crud(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskResponse):
    task = update_task_crud(task_id, updated_task)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int):
    task = delete_task_crud(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
