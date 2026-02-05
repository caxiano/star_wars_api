from fastapi import APIRouter, HTTPException

from app.services.json_store import load_json

router = APIRouter()


@router.get("/")
def list_vehicles():
    """
    Retorna a lista de veículos.
    """
    data = load_json("vehicles")

    if not data:
        raise HTTPException(500, "Vehicles data not available")

    return {"count": len(data), "results": data}


@router.get("/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    """
    Retorna um veículo pelo ID.
    """
    data = load_json("vehicles")

    for vehicle in data:
        if vehicle["id"] == vehicle_id:
            return vehicle

    raise HTTPException(404, "Vehicle not found")


@router.get("/{vehicle_id}/pilots")
def vehicle_pilots(vehicle_id: int):
    """
    Retorna os pilotos de um veículo.
    """
    vehicle = get_vehicle(vehicle_id)
    return {"vehicle": vehicle["name"], "pilots": vehicle["pilots"]}


@router.get("/{vehicle_id}/films")
def vehicle_films(vehicle_id: int):
    """
    Retorna os filmes relacionados a um veículo.
    """
    vehicle = get_vehicle(vehicle_id)
    return {"vehicle": vehicle["name"], "films": vehicle["films"]}
