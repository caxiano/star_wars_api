from fastapi import APIRouter, Query

from app.services.swapi_client import SwapiClient

router = APIRouter()
client = SwapiClient()


@router.get("/")
async def list_starships(
    name: str | None = Query(None),
    model: str | None = Query(None),
    sort: str = Query("name"),


):
    data = await client.fetch("starships", params={"search": name} if name else None)
    results = data["results"]

    if model:
        results = [
            s for s in results
            if model.lower() in s.get("model", "").lower()
        ]

    results.sort(key=lambda x: x.get(sort, ""))

    return {"count": len(results), "results": results}


@router.get("/{starship_id}")
async def get_starship(starship_id: int):
    return await client.fetch(f"starships/{starship_id}")


@router.get("/{starship_id}/films")
async def starship_films(starship_id: int):
    starship = await client.fetch(f"starships/{starship_id}")
    films = await client.fetch_many(starship["films"])

    return {"starship": starship["name"], "films": films}


@router.get("/{starship_id}/pilots")
async def starship_pilots(starship_id: int):
    starship = await client.fetch(f"starships/{starship_id}")
    pilots = await client.fetch_many(starship["pilots"])

    return {"starship": starship["name"], "pilots": pilots}
