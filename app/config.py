from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SWAPI_BASE_URL: str = "https://swapi.dev/api"
    API_BASE_URL: str = "http://localhost:8000"
    API_PREFIX: str = "/api"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
