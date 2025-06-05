from fastapi import APIRouter

from app.api.v1.endpoints import auth, orders, product, users

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(auth.router)
api_router.include_router(product.router)
api_router.include_router(orders.router)