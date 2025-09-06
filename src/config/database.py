from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_NAME: str
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int = 5432

    class Config:
        env_file = "../.env"


settings = Settings()
