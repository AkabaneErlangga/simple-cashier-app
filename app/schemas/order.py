import uuid
from datetime import datetime
from typing import List

from pydantic import BaseModel, RootModel


class OrderProductRead(BaseModel):
    id: uuid.UUID
    product_id: uuid.UUID
    quantity: int
    price_at_time: float
    created_at: datetime


class OrderProductCreate(BaseModel):
    product_id: uuid.UUID
    quantity: int


class OrderRead(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    total_price: float
    created_at: datetime
    updated_at: datetime
    order_products: List[OrderProductRead]

    class Config:
        from_attributes = True


class OrderItemCreate(BaseModel):
    product_ids: uuid.UUID
    quantities: int


class OrderCreate(RootModel):
    root: List[OrderItemCreate] 