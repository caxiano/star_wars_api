import httpx
from fastapi import APIRouter

from app.config import settings
from app.services.swapi_service import SwapiService

router = APIRouter()
swapi_service = SwapiService()


@router.get("/")
async def root():
    return await swapi_service.fetch()


@router.get("/api")
async def api_root():
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.SWAPI_BASE_URL)
        response.raise_for_status()
        swapi_data = response.json()

    return {
        resource: f"{settings.API_BASE_URL}{settings.API_PREFIX}/{resource}"
        for resource in swapi_data.keys()
    }
