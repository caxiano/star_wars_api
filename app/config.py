from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configurações da aplicação, incluindo URLs base e configurações JWT.
    """
    # API
    API_BASE_URL: str = "http://localhost:8000"

    # SWAPI
    SWAPI_BASE_URL: str = "https://swapi.dev/api"

    # JWT
    JWT_SECRET_KEY: str = "POWEROFDATA_SWAPI_PYTHON_DEVELOPER_JUNIOR"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60

    # Adicionar flag de teste para permitir pular operações de rede durante os testes
    TESTING: bool = False
    # Força recriar a pasta data/ no startup
    FORCE_REBUILD_DATA: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
