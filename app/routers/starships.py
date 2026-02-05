from fastapi import APIRouter, HTTPException

from app.services.json_store import load_json

router = APIRouter()


@router.get("/")
def list_starships():
    """
    Retorna a lista de espaçonaves.
    """
    data = load_json("starships")

    if not data:
        raise HTTPException(500, "Starships data not available")

    return {"count": len(data), "results": data}


@router.get("/{starship_id}")
def get_starship(starship_id: int):
    """
    Retorna uma espaçonave pelo ID.
    """
    data = load_json("starships")

    for ship in data:
        if ship["id"] == starship_id:
            return ship

    raise HTTPException(404, "Starship not found")


@router.get("/{starship_id}/pilots")
def starship_pilots(starship_id: int):
    """
    Retorna os pilotos de uma espaçonave.
    """
    ship = get_starship(starship_id)
    return {"starship": ship["name"], "pilots": ship["pilots"]}


@router.get("/{starship_id}/films")
def starship_films(starship_id: int):
    """
    Retorna os filmes relacionados a uma espaçonave.
    """
    ship = get_starship(starship_id)
    return {"starship": ship["name"], "films": ship["films"]}
