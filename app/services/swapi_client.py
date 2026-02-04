import asyncio

import httpx

from app.config import settings
from app.core.cache import get_from_cache, set_cache


class SwapiClient:
    def __init__(self):
        self.timeout = httpx.Timeout(10.0)

    async def fetch(self, resource: str, params: dict | None = None) -> dict:
        if resource.startswith("http"):
            url = resource
        else:
            url = f"{settings.SWAPI_BASE_URL.rstrip('/')}/{resource.strip('/')}/"

        cache_key = f"{url}:{params}"

        cached = get_from_cache(cache_key)
        if cached:
            return cached

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(url, params=params or {})
            response.raise_for_status()
            data = response.json()

        set_cache(cache_key, data)
        return data

    async def fetch_many(self, resources: list[str]) -> list[dict]:
        tasks = [self.fetch(resource) for resource in resources]
        return await asyncio.gather(*tasks)
