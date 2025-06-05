import uuid
from datetime import datetime
from typing import List
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from app.models.order_product import OrderProduct


class ProductBase(SQLModel):
    name: str
    image: str
    description: str | None = None
    price: float
    stock: int
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime | None = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    category_id: int | None = None
    order_products: List[OrderProduct] = Relationship(back_populates="product")
    # You can add relationships here if needed, e.g., to link to a Category model


class ProductPublic(ProductBase):
    id: int
    category_id: int | None = None


class ProductsPublic(SQLModel):
    data: list[ProductPublic]
    count: int


class ProductUpdate(SQLModel):
    name: str | None = None
    image: str | None = None
    description: str | None = None
    price: float | None = None
    stock: int | None = None
    category_id: int | None = None  # Optional field for updating category association
    updated_at: datetime = Field(default_factory=datetime.now)
