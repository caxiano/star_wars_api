from urllib.parse import urlparse

from app.config import settings


def swapi_to_internal(url: str) -> str:
    """
    Converte uma URL da SWAPI para a URL interna da API.
    :param url: URL da SWAPI.
    :return: URL interna da API.

    Exemplo: 
    https://swapi.dev/api/people/1/ -> http://localhost:8000/api/people/1/
    """
    path = urlparse(url).path.strip("/")
    return f"{settings.API_BASE_URL}/{path}"
