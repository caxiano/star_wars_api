from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # API
    API_BASE_URL: str = "http://localhost:8000"

    # SWAPI
    SWAPI_BASE_URL: str = "https://swapi.dev/api"

    # JWT
    JWT_SECRET_KEY: str = "POWEROFDATA_SWAPI"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
