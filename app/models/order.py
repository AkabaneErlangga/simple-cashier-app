import uuid
from datetime import datetime
from typing import List
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from app.models.order_product import OrderProduct


class OrderBase(SQLModel):
    user_id: UUID
    total_price: float
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime | None = None


class OrderCreate(OrderBase):
    product_ids: List[UUID]
    quantities: List[int]


class Order(OrderBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    order_products: List[OrderProduct] = Relationship(back_populates="order")

