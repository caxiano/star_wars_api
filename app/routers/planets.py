from fastapi import APIRouter, Query

from app.services.swapi_client import SwapiClient

router = APIRouter()
client = SwapiClient()


@router.get("/")
async def list_planets(
    name: str | None = Query(None),
    climate: str | None = Query(None),
    sort: str = Query("name"),
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
    residents = await client.fetch_many(planet["residents"])

    return {"planet": planet["name"], "residents": residents}


@router.get("/{planet_id}/films")
async def planet_films(planet_id: int):
    planet = await client.fetch(f"planets/{planet_id}")
    films = await client.fetch_many(planet["films"])

    return {"planet": planet["name"], "films": films}
