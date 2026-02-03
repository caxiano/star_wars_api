import httpx

from app.config import settings


class SwapiClient:
    async def fetch(self, resource: str, params: dict | None = None):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{settings.SWAPI_BASE_URL}/{resource}/", params=params)
            response.raise_for_status()
            return response.json()
