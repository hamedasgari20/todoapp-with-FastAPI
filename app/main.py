from fastapi import FastAPI

from app.routers.tasks import router as tasks_router
from app.routers.users import router as user_router

app = FastAPI()

app.include_router(tasks_router, prefix="/task", tags=["task"])
app.include_router(user_router, prefix="/user", tags=["user"])
