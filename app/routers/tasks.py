from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.model import Task
from app.schemas.task import TaskResponse

router = APIRouter()


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskResponse, db: Session = Depends(get_db)):
    task_dict = task.dict()
    task = Task.create(db, **task_dict)
    return task


@router.get("/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = Task.get(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskResponse, db: Session = Depends(get_db)):
    task_dict = updated_task.dict()
    task = Task.get(db, task_id)
    if task is None:
        return {"error": "Task not found"}
    else:
        updated_task = task.update(db, **task_dict)
        return updated_task


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = Task.get(db, task_id)
    if task is None:
        return {"error": "Task not found"}
    else:
        deleted_task = task.delete(db)
        return {"message": "Task deleted successfully"}
