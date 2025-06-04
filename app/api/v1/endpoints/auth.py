from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.api.v1.deps import SessionDep
from app.crud.auths import authenticate

router = APIRouter()


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
    return {"message": "Login successful", "user_id": str(user.id)}
