from fastapi import APIRouter, Query

from app.services.swapi_client import SwapiClient

router = APIRouter()
client = SwapiClient()


@router.get("/")
async def list_films(
    title: str | None = Query(None),
    sort: str = Query("episode_id"),
):
    data = await client.fetch("films")
    results = data["results"]

    if title:
        results = [f for f in results if title.lower() in f["title"].lower()]

    results.sort(key=lambda x: x.get(sort))
    return {"count": len(results), "results": results}


@router.get("/{film_id}")
async def get_film(film_id: int):
    return await client.fetch(f"films/{film_id}")


@router.get("/{film_id}/characters")
async def film_characters(film_id: int):
    film = await client.fetch(f"films/{film_id}")
    characters = [await client.fetch(url) for url in film["characters"]]

    return {
        "film": film["title"],
        "characters": characters
    }


@router.get("/{film_id}/planets")
async def film_planets(film_id: int):
    film = await client.fetch(f"films/{film_id}")
    planets = [await client.fetch(url) for url in film["planets"]]

    return {"film": film["title"], "planets": planets}


@router.get("/{film_id}/species")
async def film_species(film_id: int):
    film = await client.fetch(f"films/{film_id}")
    species = [await client.fetch(url) for url in film["species"]]

    return {"film": film["title"], "species": species}


@router.get("/{film_id}/starships")
async def film_starships(film_id: int):
    film = await client.fetch(f"films/{film_id}")
    starships = [await client.fetch(url) for url in film["starships"]]

    return {"film": film["title"], "starships": starships}


@router.get("/{film_id}/vehicles")
async def film_vehicles(film_id: int):
    film = await client.fetch(f"films/{film_id}")
    vehicles = [await client.fetch(url) for url in film["vehicles"]]

    return {"film": film["title"], "vehicles": vehicles}
