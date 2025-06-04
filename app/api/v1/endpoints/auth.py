from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.v1.deps import SessionDep
from app.core.config import settings
from app.core.security import create_access_token
from app.crud.auths import authenticate

router = APIRouter()


access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)


@router.post("/login")
def login(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    """
    User login endpoint.
    """
    user = authenticate(
        session=session,
        email=form_data.username,
        password=form_data.password,
    )
    if not user:
        return {"error": "Invalid credentials"}
    return {"access_token": (create_access_token(str(user.id), access_token_expires))}
