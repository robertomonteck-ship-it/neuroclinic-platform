from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    # Nome do projeto
    PROJECT_NAME: str = "NeuroClinic API"

    # Banco de dados
    DATABASE_URL: str = "sqlite:///./neuroclinic.db"

    # Segurança
    SECRET_KEY: str = "CHANGE_THIS_SECRET_KEY"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Ambiente
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()