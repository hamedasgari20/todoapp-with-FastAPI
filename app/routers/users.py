from fastapi import APIRouter

from app.schemas.auth import UserRead, UserUpdate
from app.utils.auth import fastapi_users

router = APIRouter()

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)
