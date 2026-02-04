from fastapi import APIRouter, Query

from app.services.swapi_client import SwapiClient

router = APIRouter()
client = SwapiClient()


@router.get("/")
async def list_people(
    name: str | None = Query(None),
    sort: str = Query("name"),
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
    films = await client.fetch_many(person["films"])

    return {"person": person["name"], "films": films}


@router.get("/{person_id}/species")
async def person_species(person_id: int):
    person = await client.fetch(f"people/{person_id}")
    species = await client.fetch_many(person["species"])

    return {"person": person["name"], "species": species}


@router.get("/{person_id}/starships")
async def person_starships(person_id: int):
    person = await client.fetch(f"people/{person_id}")
    starships = await client.fetch_many(person["starships"])

    return {"person": person["name"], "starships": starships}


@router.get("/{person_id}/vehicles")
async def person_vehicles(person_id: int):
    person = await client.fetch(f"people/{person_id}")
    vehicles = await client.fetch_many(person["vehicles"])

    return {"person": person["name"], "vehicles": vehicles}
