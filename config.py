from pydantic import BaseSettings


class Settings(BaseSettings):
    ow_key: str

    class Config:
        env_file = ".env"


settings = Settings()
