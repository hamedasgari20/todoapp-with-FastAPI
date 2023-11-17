from fastapi import APIRouter, Depends

from app.db.auth import User
from app.schemas.auth import UserRead, UserCreate
from app.utils.auth import fastapi_users, auth_backend, current_active_user

router = APIRouter()

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)
router.include_router(
    fastapi_users.get_auth_router(auth_backend)
)

router.include_router(
    fastapi_users.get_reset_password_router(),
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
)


@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
