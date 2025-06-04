import uuid

from fastapi import APIRouter, HTTPException

from app.api.v1.deps import CurrentUser, SessionDep
from app.core.utils import convert_to_schema
from app.models.user import User
from app.schemas.user import UserRead

router = APIRouter()


@router.get("/users/id/{user_id}", response_model=UserRead)
async def get_user(user_id: uuid.UUID, session: SessionDep) -> UserRead:
    """
    Retrieve a user by ID.
    """
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return convert_to_schema(user, UserRead)


@router.get("/users/me", response_model=UserRead)
async def get_current_user(current_user: CurrentUser, session: SessionDep):
    """
    Get current user.
    """
    return current_user
