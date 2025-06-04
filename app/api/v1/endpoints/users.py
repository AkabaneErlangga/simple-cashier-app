import uuid

from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.deps import SessionDep
from app.core.utils import convert_to_schema
from app.models.user import User
from app.schemas.user import UserRead

router = APIRouter()


@router.get("/users/{user_id}", response_model=UserRead)
async def get_user(user_id: uuid.UUID, session: SessionDep) -> UserRead:
    """
    Retrieve a user by ID.
    """
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return convert_to_schema(user, UserRead)
