from sqlalchemy import Column, Integer, String

from app.models.base import BaseModel


class Task(BaseModel):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
