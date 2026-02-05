from fastapi import APIRouter, HTTPException

from app.services.json_store import load_json

router = APIRouter()


@router.get("/")
def list_films():
    """
    Retorna a lista de filmes.
    """
    data = load_json("films")

    if not data:
        raise HTTPException(500, "Films data not available")

    return {"count": len(data), "results": data}


@router.get("/{film_id}")
def get_film(film_id: int):
    """
    Retorna um filme pelo ID.
    """
    data = load_json("films")

    for film in data:
        if film["id"] == film_id:
            return film

    raise HTTPException(404, "Film not found")


@router.get("/{film_id}/characters")
def film_characters(film_id: int):
    """
    Retorna os personagens de um filme.
    """
    film = get_film(film_id)
    return {"film": film["title"], "characters": film["characters"]}


@router.get("/{film_id}/planets")
def film_planets(film_id: int):
    """
    Retorna os planetas de um filme.
    """
    film = get_film(film_id)
    return {"film": film["title"], "planets": film["planets"]}


@router.get("/{film_id}/starships")
def film_starships(film_id: int):
    """
    Retorna as espaçonaves de um filme.
    """
    film = get_film(film_id)
    return {"film": film["title"], "starships": film["starships"]}
