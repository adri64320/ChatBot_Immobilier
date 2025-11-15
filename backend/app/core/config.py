from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    CORS_ORIGINS: List[str] = ["http://localhost:4200", "http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()