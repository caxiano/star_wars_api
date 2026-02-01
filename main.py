from fastapi import FastAPI

from services.swapi_service import SwapiService

app = FastAPI()
swapi_service = SwapiService()


@app.get("/")
async def root():
    return await swapi_service.fetch()
