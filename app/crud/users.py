from sqlmodel import Session, select

from app.core.security import get_password_hash
from app.models.user import User, UserCreate


def create_user(session: Session, user_create: UserCreate) -> User:
    db_user = User(
        email=user_create.email,
        hashed_password=get_password_hash(user_create.password),
        is_active=user_create.is_active,
        is_superuser=user_create.is_superuser,
        full_name=user_create.full_name,
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user_by_email(session: Session, email: str) -> User | None:
    return session.exec(select(User).where(User.email == email)).first()


def read_user(session: Session, user_id: str) -> User | None:
    return session.get(User, user_id) 