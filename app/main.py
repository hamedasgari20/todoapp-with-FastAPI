from fastapi import FastAPI

from app.db.auth import create_db_and_tables
from app.routers.tasks import router as tasks_router
from app.routers.auth import router as auth_router
from app.routers.users import router as user_router

app = FastAPI()

app.include_router(tasks_router, prefix="/task", tags=["task"])
app.include_router(auth_router, prefix="/auth/jwt", tags=["auth"])
app.include_router(user_router, prefix="/user", tags=["user"])


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
