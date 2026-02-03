from fastapi import APIRouter, Depends, Query

from app.core.auth import verify_token
from app.services.swapi_client import SwapiClient

router = APIRouter()
client = SwapiClient()


@router.get("/")
async def list_films(
    title: str | None = Query(None),
    sort: str = Query("episode_id"),
    _: bool = Depends(verify_token)
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
