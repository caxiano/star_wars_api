from fastapi import APIRouter, Depends, Query

from app.core.auth import verify_token
from app.services.swapi_client import SwapiClient

router = APIRouter()
client = SwapiClient()


@router.get("/")
async def list_planets(
    name: str | None = Query(None),
    climate: str | None = Query(None),
    sort: str = Query("name"),
    _: bool = Depends(verify_token)
):
    data = await client.fetch("planets", params={"search": name} if name else None)
    results = data["results"]

    if climate:
        results = [
            p for p in results
            if climate.lower() in p.get("climate", "").lower()
        ]

    results.sort(key=lambda x: x.get(sort, ""))
    return {"count": len(results), "results": results}


@router.get("/{planet_id}")
async def get_planet(planet_id: int):
    return await client.fetch(f"planets/{planet_id}")


@router.get("/{planet_id}/residents")
async def planet_residents(planet_id: int):
    planet = await client.fetch(f"planets/{planet_id}")
    residents = [await client.fetch(url) for url in planet["residents"]]

    return {
        "planet": planet["name"],
        "residents": residents
    }
