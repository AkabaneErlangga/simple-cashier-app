import uuid
from datetime import datetime

from sqlmodel import SQLModel


class ProductCreate(SQLModel):
    name: str
    image: str
    description: str | None = None
    price: float
    stock: int


class ProductUpdate(SQLModel):
    name: str | None = None
    image: str | None = None
    description: str | None = None
    price: float | None = None
    stock: int | None = None
    category_id: int | None = None  # Optional field for updating category association


class ProductRead(SQLModel):
    id: uuid.UUID
    name: str
    image: str
    description: str | None = None
    price: float
    stock: int
    category_id: int | None = None
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None

    class Config:
        from_attributes = True
