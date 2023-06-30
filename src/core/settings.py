from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY = "secret"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7


settings = Settings()
