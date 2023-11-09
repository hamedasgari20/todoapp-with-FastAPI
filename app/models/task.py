from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from app.db.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

    @classmethod
    def get(cls, db: Session, task_id: int):
        task = db.query(cls).filter(cls.id == task_id).first()
        return task

    @classmethod
    def create(cls, db: Session, task_data: dict):
        db_task = cls(**task_data)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    @classmethod
    def update(cls, db: Session, task_id: int, task_data: dict):
        task = db.query(cls).filter(cls.id == task_id).first()
        if task:
            for key, value in task_data.items():
                setattr(task, key, value)
            db.commit()
            db.refresh(task)
        return task

    @classmethod
    def delete(cls, db: Session, task_id: int):
        task = db.query(cls).filter(cls.id == task_id).first()
        if task:
            db.delete(task)
            db.commit()
        return task