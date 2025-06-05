from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from app.api.v1.deps import CurrentUser, SessionDep
from app.core.utils import convert_to_schema
from app.models import order
from app.models.order import Order, OrderBase
from app.models.order_product import OrderProduct
from app.models.product import Product
from app.schemas.order import OrderCreate, OrderItemCreate, OrderRead

router = APIRouter()


@router.post("/orders", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
async def create_order(
    order_in: OrderCreate,
    current_user: CurrentUser,
    session: SessionDep,
) -> OrderRead:
    """
    Create a new order.
    """
    # Get products and calculate total
    total_price = 0
    products_with_quantities = []

    for item in order_in.root:
        product = session.get(Product, item.product_ids)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {item.product_ids} not found",
            )
        
        if product.stock < item.quantities:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Not enough stock for product {product.name}",
            )

        total_price += product.price * item.quantities
        products_with_quantities.append((product, item.quantities))

    # Create order base with required fields
    order_base = OrderBase(
        user_id=current_user.id,
        total_price=total_price,
    )

    # Create order first
    order = Order(**order_base.model_dump())

    try:
        # Add order to session to get its ID
        session.add(order)
        session.flush()

        # Create order products with the order's ID
        order_products = []
        for product, quantity in products_with_quantities:
            order_product = OrderProduct(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity,
                price_at_time=product.price,
            )
            order_products.append(order_product)
            session.add(order_product)

        # Update order with products
        order.order_products = order_products

        # Commit all changes
        session.commit()
        session.refresh(order)
        return order
    except Exception as e:
        session.rollback()
        # Log the exception if needed
        print(f"Error creating order: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create order",
        )


@router.get("/orders", response_model=List[OrderRead])
async def get_orders(
    current_user: CurrentUser,
    session: SessionDep,
) -> List[OrderRead]:
    """
    Get all orders for the current user.
    """
    statement = select(Order)
    orders = session.exec(statement).all()
    # return [convert_to_schema(order, OrderRead) for order in orders]
    return orders


@router.get("/orders/{order_id}", response_model=OrderRead)
async def get_order(
    order_id: UUID,
    current_user: CurrentUser,
    session: SessionDep,
) -> OrderRead:
    """
    Get a specific order by ID.
    """
    statement = select(Order).where(
        Order.id == order_id,
        Order.user_id == current_user.id,
        Order.deleted_at == None,
    )
    order = session.exec(statement).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )
    return convert_to_schema(order, OrderRead) 