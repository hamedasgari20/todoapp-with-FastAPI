from app.db.database import get_db_func as get_db
from app.db.model import Task


def get_first_task():
    with get_db() as db:
        # You can use the db session here
        data = db.query(Task).first()
        return {"title": data.title, "description": data.description}
