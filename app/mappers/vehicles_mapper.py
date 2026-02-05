from app.utils.link_utils import swapi_to_internal


def normalize_vehicles(
    raw_vehicles: list[dict],
    people_index: dict[str, str],
    films_index: dict[str, str],
) -> list[dict]:
    """
    Normaliza veículos da SWAPI, retornando pilotos
    e filmes associados.
    """
    normalized = []

    # Normalização dos veículos
    for vehicle in raw_vehicles:
        normalized.append({
            "id": int(vehicle["url"].rstrip("/").split("/")[-1]),
            "name": vehicle["name"],
            "vehicle_class": vehicle["vehicle_class"],
            "manufacturer": vehicle["manufacturer"],
            "pilots": {
                people_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in vehicle["pilots"]
            },
            "films": {
                films_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in vehicle["films"]
            }
        })

    return normalized
