from pydantic import EmailStr, HttpUrl, PostgresDsn, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "GloryGloryMontelli"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    PROJECT_NAME: str = "Cashier App"
    SENTRY_DSN: HttpUrl | None = None
    POSTGRES_SERVER: str 
    POSTGRES_PORT: int 
    POSTGRES_USER: str 
    POSTGRES_PASSWORD: str 
    POSTGRES_DB: str = "cashier-app"

    EMAIL_TEST_USER: EmailStr = "root@akabane.my.id"
    FIRST_SUPERUSER: EmailStr = "root@akabane.my.id"
    FIRST_SUPERUSER_PASSWORD: str = "sakura123"

    model_config = SettingsConfigDict(env_file=".env")

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