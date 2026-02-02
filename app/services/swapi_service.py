
import httpx

from app.config import settings


class SwapiService:
    async def fetch(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(settings.SWAPI_BASE_URL)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as exc:
            return {"error": f"HTTP error occurred: {exc.response.status_code} - {exc.response.text}"}
        except Exception as e:
            return {"error": str(e)}
