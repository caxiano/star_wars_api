from fastapi import APIRouter, HTTPException

from app.services.json_store import load_json

router = APIRouter()


@router.get("/")
def list_species():
    """
    Retorna a lista de espécies.
    """
    data = load_json("species")

    if not data:
        raise HTTPException(500, "Species data not available")

    return {"count": len(data), "results": data}


@router.get("/{species_id}")
def get_species(species_id: int):
    """
    Retorna uma espécie pelo ID.
    """
    data = load_json("species")

    for specie in data:
        if specie["id"] == species_id:
            return specie

    raise HTTPException(404, "Specie not found")


@router.get("/{species_id}/people")
def species_people(species_id: int):
    """
    Retorna os personagens de uma espécie.
    """
    specie = get_species(species_id)
    return {"species": specie["name"], "people": specie["people"]}


@router.get("/{species_id}/films")
def species_films(species_id: int):
    """
    Retorna os filmes relacionados a uma espécie.
    """
    specie = get_species(species_id)
    return {"species": specie["name"], "films": specie["films"]}
