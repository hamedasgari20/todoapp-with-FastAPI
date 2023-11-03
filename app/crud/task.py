from app.db.database import SessionLocal
from app.models.task import Task
from app.schemas.task import TaskResponse


def read_task_crud(task_id: int):
    """
    Retrieve a task from the database by ID.

    Args:
        task_id (int): The ID of the task to retrieve.

    Returns:
        Task: The task with the specified ID, or None if no such task exists.
    """
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    db.close()
    return task


def create_task_crud(task: TaskResponse):
    """
    Create a new task in the database.

    Args:
        task (TaskResponse): The details of the task to create.

    Returns:
        Task: The newly created task.
    """
    db = SessionLocal()
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task


def update_task_crud(task_id: int, updated_task: TaskResponse):
    """
    Update an existing task in the database.

    Args:
        task_id (int): The ID of the task to update.
        updated_task (TaskResponse): The updated details of the task.

    Returns:
        Task: The updated task, or None if no such task exists.
    """
    db = SessionLocal()
    task = read_task_crud(task_id)
    if task is None:
        db.close()
        return None
    for key, value in updated_task.dict(exclude_unset=True).items():
        setattr(task, key, value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


#
def delete_task_crud(task_id: int):
    """
    Delete a task from the database.

    Args:
        task_id (int): The ID of the task to delete.

    Returns:
        Task: The deleted task, or None if no such task exists.
    """
    db = SessionLocal()
    task = read_task_crud(task_id)
    if task is None:
        db.close()
        return None
    db.delete(task)
    db.commit()
    db.close()
    return task
