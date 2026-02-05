import asyncio

import httpx

from app.config import settings


async def fetch_all_pages(resource: str, retries: int = 3, backoff_factor: float = 2.0) -> list[dict]:
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
            # tentativas com backoff exponencial
            for attempt in range(retries):
                try:
                    response = await client.get(url)
                    response.raise_for_status()
                    data = response.json()
                    break
                except (httpx.RequestError, httpx.HTTPStatusError):
                    if attempt + 1 >= retries:
                        raise
                    await asyncio.sleep(backoff_factor ** attempt)

            results.extend(data.get("results", []))
            url = data.get("next")  # None quando acaba

    return results
