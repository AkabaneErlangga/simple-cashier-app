from pydantic import EmailStr, HttpUrl, PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    PROJECT_NAME: str = "Cashier App"
    SENTRY_DSN: HttpUrl | None = None
    POSTGRES_SERVER: str = "43.133.132.163"
    POSTGRES_PORT: int = 31067
    POSTGRES_USER: str = "root"
    POSTGRES_PASSWORD: str = "fZ86lhA13HP57W4k9xTEpdJuBiON20Fr"
    POSTGRES_DB: str = "cashier-app"

    EMAIL_TEST_USER: EmailStr = "root@akabane.my.id"
    FIRST_SUPERUSER: EmailStr = "root@akabane.my.id"
    FIRST_SUPERUSER_PASSWORD: str = "sakura123"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()  # type: ignore