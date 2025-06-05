import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.order import Order
    from app.models.product import Product


class OrderProduct(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    order_id: uuid.UUID = Field(foreign_key="order.id")
    product_id: uuid.UUID = Field(foreign_key="product.id")
    quantity: int
    price_at_time: float
    created_at: datetime = Field(default_factory=datetime.now)

    # Relationships
    order: "Order" = Relationship(back_populates="order_products")
    product: "Product" = Relationship(back_populates="order_products")
