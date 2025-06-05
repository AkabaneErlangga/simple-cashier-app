from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from app.api.v1.deps import CurrentUser, SessionDep
from app.core.utils import convert_to_schema
from app.models.product import Product, ProductCreate
from app.schemas.product import ProductRead

router = APIRouter()


@router.get("/products", response_model=list[ProductRead], tags=["products"])
async def get_products(session: SessionDep) -> list[ProductRead]:
    """
    Retrieve a list of products.
    """
    statement = select(Product).where(Product.deleted_at == None)
    products = session.exec(statement).all()
    return [convert_to_schema(product, ProductRead) for product in products]


@router.get("/products/{product_id}", response_model=ProductRead, tags=["products"])
async def get_product(product_id: UUID, session: SessionDep) -> ProductRead:
    """
    Retrieve a product by its ID.
    """
    statement = select(Product).where(
        Product.id == product_id, Product.deleted_at == None
    )
    product = session.exec(statement).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return convert_to_schema(product, ProductRead)


@router.post(
    "/products",
    response_model=ProductRead,
    status_code=status.HTTP_201_CREATED,
    tags=["products"]
)
async def create_product(
    product_in: ProductCreate, current_user: CurrentUser, session: SessionDep
) -> ProductRead:
    """
    Create a new product.

    Only superusers can create products.
    """
    # Check if user has permission
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to create products",
        )

    # Create product
    product = Product(**product_in.model_dump())

    try:
        session.add(product)
        session.commit()
        session.refresh(product)
        return convert_to_schema(product, ProductRead)
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create product",
        )


@router.put("/products/{product_id}", response_model=ProductRead, tags=["products"])
async def update_product(
    product_id: UUID,
    product: ProductCreate,
    session: SessionDep,
    current_user: CurrentUser,
):
    """
    Update an existing product by its ID.
    """
    statement = select(Product).where(
        Product.id == product_id, Product.deleted_at == None
    )
    existing_product = session.exec(statement).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Update product fields
    for key, value in product.model_dump().items():
        setattr(existing_product, key, value)

    session.add(existing_product)
    session.commit()
    session.refresh(existing_product)

    return convert_to_schema(existing_product, ProductRead)


@router.delete("/products/{product_id}", tags=["products"])
async def delete_product(
    product_id: UUID, session: SessionDep, current_user: CurrentUser
):
    """
    Delete a product by its ID.
    """
    statement = select(Product).where(
        Product.id == product_id, Product.deleted_at == None
    )
    product = session.exec(statement).first()
    if not product:
        raise HTTPException(
            status_code=404, detail="Product not found or already deleted"
        )

    product.deleted_at = datetime.now()
    session.add(product)
    session.commit()
    session.refresh(product)

    return convert_to_schema(product, ProductRead)
