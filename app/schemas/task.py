from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
