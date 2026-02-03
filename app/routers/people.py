from fastapi import APIRouter, Depends, Query

from app.core.auth import verify_token
from app.services.swapi_client import SwapiClient

router = APIRouter()
client = SwapiClient()


@router.get("/")
async def list_people(
    name: str | None = Query(None),
    sort: str = Query("name"),
    _: bool = Depends(verify_token)
):
    data = await client.fetch("people", params={"search": name} if name else None)

    results = data["results"]
    results.sort(key=lambda x: x.get(sort, ""))

    return {"count": len(results), "results": results}


@router.get("/{person_id}")
async def get_person(person_id: int):
    return await client.fetch(f"people/{person_id}")


@router.get("/{person_id}/films")
async def person_films(person_id: int):
    person = await client.fetch(f"people/{person_id}")
    films = [await client.fetch(url) for url in person["films"]]

    return {
        "person": person["name"],
        "films": films
    }
