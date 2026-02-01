
import httpx

SWAPI_URL = 'https://swapi.dev/api/'


class SwapiService:
    async def fetch(self, endpoint: str = ''):
        try:
            async with httpx.AsyncClient() as client:
                url = f"{SWAPI_URL}{endpoint}/"
                response = await client.get(url)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as exc:
            return {"error": f"HTTP error occurred: {exc.response.status_code} - {exc.response.text}"}
        except Exception as e:
            return {"error": str(e)}
