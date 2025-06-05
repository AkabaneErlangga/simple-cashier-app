from sqlmodel import Field, Session, SQLModel, create_engine, select

from app.core.config import settings
from app.crud import users as crud
from app.models.order import Order, OrderCreate
from app.models.order_product import OrderProduct
from app.models.product import Product, ProductCreate
from app.models.user import User, UserCreate

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines

    # This works because the models are already imported and registered from app.models
    SQLModel.metadata.create_all(engine)

    # Create first superuser
    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)
