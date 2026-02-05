from fastapi import APIRouter, HTTPException

from app.services.json_store import load_json

router = APIRouter()


@router.get("/")
def list_planets():
    """
    Retorna a lista de planetas.
    """
    data = load_json("planets")

    if not data:
        raise HTTPException(500, "Planets data not available")

    return {"count": len(data), "results": data}


@router.get("/{planet_id}")
def get_planet(planet_id: int):
    """
    Retorna um planeta pelo ID.
    """
    data = load_json("planets")

    for planet in data:
        if planet["id"] == planet_id:
            return planet

    raise HTTPException(404, "Planet not found")


@router.get("/{planet_id}/residents")
def planet_residents(planet_id: int):
    """
    Retorna os residentes de um planeta.
    """
    planet = get_planet(planet_id)
    return {"planet": planet["name"], "residents": planet["residents"]}


@router.get("/{planet_id}/films")
def planet_films(planet_id: int):
    """
    Retorna os filmes relacionados a um planeta.
    """
    planet = get_planet(planet_id)
    return {"planet": planet["name"], "films": planet["films"]}
