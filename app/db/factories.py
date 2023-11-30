import factory

from app.db.model import Task


class TaskFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Task
