from fastapi import APIRouter, Depends, Query

from app.core.auth import verify_token
from app.services.swapi_client import SwapiClient

router = APIRouter()
client = SwapiClient()


@router.get("/")
async def list_vehicles(
    name: str | None = Query(None),
    vehicle_class: str | None = Query(None),
    sort: str = Query("name"),
    _: bool = Depends(verify_token)
):
    data = await client.fetch("vehicles", params={"search": name} if name else None)
    results = data["results"]

    if vehicle_class:
        results = [
            v for v in results
            if vehicle_class.lower() in v.get("vehicle_class", "").lower()
        ]

    results.sort(key=lambda x: x.get(sort, ""))
    return {"count": len(results), "results": results}


@router.get("/{vehicle_id}")
async def get_vehicle(vehicle_id: int):
    return await client.fetch(f"vehicles/{vehicle_id}")


@router.get("/{vehicle_id}/films")
async def vehicle_films(vehicle_id: int):
    vehicle = await client.fetch(f"vehicles/{vehicle_id}")
    films = [await client.fetch(url) for url in vehicle["films"]]

    return {
        "vehicle": vehicle["name"],
        "films": films
    }
