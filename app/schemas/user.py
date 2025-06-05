import uuid

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None


class UserRead(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str | None = None

    class Config:
        from_attributes = True
