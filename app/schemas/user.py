from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):
    """Base model representing common user attributes."""
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    """Model representing a user."""
    pass
