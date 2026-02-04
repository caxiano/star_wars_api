from fastapi import APIRouter, Query

from app.services.swapi_client import SwapiClient

router = APIRouter()
client = SwapiClient()


@router.get("/")
async def list_species(
    name: str | None = Query(None),
    classification: str | None = Query(None),
    sort: str = Query("name"),
):
    data = await client.fetch("species", params={"search": name} if name else None)

    results = data["results"]

    if classification:
        results = [
            s for s in results
            if s["classification"].lower() == classification.lower()
        ]

    results.sort(key=lambda x: x.get(sort, ""))

    return {"count": len(results), "results": results}


@router.get("/{species_id}")
async def get_species(species_id: int):
    return await client.fetch(f"species/{species_id}")


@router.get("/{species_id}/people")
async def species_people(species_id: int):
    species = await client.fetch(f"species/{species_id}")
    people = await client.fetch_many(species["people"])

    return {"species": species["name"], "people": people}


@router.get("/{species_id}/films")
async def species_films(species_id: int):
    species = await client.fetch(f"species/{species_id}")
    films = await client.fetch_many(species["films"])

    return {"species": species["name"], "films": films}
