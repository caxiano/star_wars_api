from fastapi import FastAPI

from app.routers.root import router as root_router
from app.services.swapi_service import SwapiService

app = FastAPI(title="Star Wars Interactive API")
swapi_service = SwapiService()

app.include_router(root_router)


@app.get("/")
async def root():
    return await swapi_service.fetch()
