from sqlalchemy.orm import Session

from app.db.database import Base


class BaseModel(Base):
    __abstract__ = True

    @classmethod
    def get(cls, db: Session, model_id: int):
        return db.query(cls).get(model_id)

    @classmethod
    def create(cls, db: Session, **kwargs):
        instance = cls(**kwargs)
        db.add(instance)
        db.commit()
        db.refresh(instance)
        return instance

    def update(self, db: Session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.commit()
        db.refresh(self)
        return self

    def delete(self, db: Session):
        db.delete(self)
        db.commit()
        return self
