from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # JWT
    SECRET_KEY: str = "super-secret-key-change-this"

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Banco
    DATABASE_URL: str = "sqlite:///./neuroclinic.db"


settings = Settings()