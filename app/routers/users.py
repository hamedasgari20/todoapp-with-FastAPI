from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi import Security
from fastapi.security import (
    OAuth2PasswordRequestForm,
)
from sqlalchemy.orm import Session

from app.config import get_settings
from app.db.database import get_db
from app.db.model import UserDB
from app.schemas.user import Token, User, UserCreate
from app.utils.user import create_access_token, get_current_active_user, verify_password, \
    get_password_hash, get_current_user

settings = get_settings()

router = APIRouter()


@router.post("/register", response_model=User, summary="Endpoint to create a new user.")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Endpoint to create a new user."""
    if db.query(UserDB).filter(UserDB.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")

    db_user = UserDB.create(db, username=user.username,
                            hashed_password=get_password_hash(user.password))
    return db_user


@router.post("/token", response_model=Token, summary="Endpoint to get an access token.")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Endpoint to log in and get an access token."""
    user = db.query(UserDB).filter(UserDB.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=User, summary="Endpoint to get user information.")
async def read_users_me(current_user: User = Depends(get_current_user)):
    """Endpoint to get user information."""
    return current_user


