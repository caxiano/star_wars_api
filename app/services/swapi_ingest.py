import httpx

from app.config import settings


async def fetch_all_pages(resource: str) -> list[dict]:
    """
    Busca todos os dados de um recurso da SWAPI.
    Lida automaticamente com paginação.
    :param resource: Nome do recurso.
    :return: Lista de todos os itens do recurso.
    """
    results: list[dict] = []
    url = f"{settings.SWAPI_BASE_URL.rstrip('/')}/{resource}/"

    # Define o tempo de espera para conexão e resposta
    timeout = httpx.Timeout(10.0, connect=5.0)

    async with httpx.AsyncClient(timeout=timeout) as client:
        while url:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

            results.extend(data["results"])
            url = data["next"]  # None quando acaba

    return results
