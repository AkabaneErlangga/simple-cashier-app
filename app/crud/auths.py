from pydantic import EmailStr

from app.core.security import verify_password
from app.crud.users import get_user_by_email


def authenticate(*, session, email: EmailStr, password: str):
    """
    Authenticate a user with a username and password.
    """

    user = get_user_by_email(session=session, email=email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
