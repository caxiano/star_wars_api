from fastapi import APIRouter, HTTPException

from app.services.json_store import load_json

router = APIRouter()


@router.get("/")
def list_people():
    """
    Retorna a lista de personagens.
    """
    data = load_json("people")

    if not data:
        raise HTTPException(500, "People data not available")

    return {"count": len(data), "results": data}


@router.get("/{person_id}")
def get_person(person_id: int):
    """
    Retorna um personagem pelo ID.
    """
    data = load_json("people")

    for person in data:
        if person["id"] == person_id:
            return person

    raise HTTPException(404, "Person not found")


@router.get("/{person_id}/films")
def person_films(person_id: int):
    """
    Retorna os filmes relacionados a um personagem.
    """
    person = get_person(person_id)
    return {"person": person["name"], "films": person["films"]}


@router.get("/{person_id}/starships")
def person_starships(person_id: int):
    """
    Retorna as espaçonaves relacionadas a um personagem.
    """
    person = get_person(person_id)
    return {"person": person["name"], "starships": person["starships"]}


@router.get("/{person_id}/vehicles")
def person_vehicles(person_id: int):
    """
    Retorna os veículos relacionados a um personagem.
    """
    person = get_person(person_id)
    return {"person": person["name"], "vehicles": person["vehicles"]}
