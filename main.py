from typing import Union

from fastapi import FastAPI

from app.api.v1.routers import api_router

app = FastAPI(
    title="Simple Cashier App",
    description="This is a sample Cashier application.",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

app.include_router(api_router) 