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
    return {"Service is Up"}

app.include_router(api_router) 