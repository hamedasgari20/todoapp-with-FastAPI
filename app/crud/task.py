from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskResponse


def read_task_crud(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    return task


def create_task_crud(db: Session, task: TaskResponse):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task_crud(db: Session, task_id: int, updated_task: TaskResponse):
    task = read_task_crud(db, task_id)
    if task is None:
        return None
    for key, value in updated_task.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


#
def delete_task_crud(db: Session, task_id: int):
    task = read_task_crud(db, task_id)
    if task is None:
        db.close()
        return None
    db.delete(task)
    db.commit()
    db.close()
    return task
