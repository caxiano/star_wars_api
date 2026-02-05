from app.utils.link_utils import swapi_to_internal


def normalize_planets(
    raw_planets: list[dict],
    people_index: dict[str, str],
    films_index: dict[str, str],
) -> list[dict]:
    """
    Normaliza planetas da SWAPI, incluindo todas as correlações
    com personagens e filmes.
    """
    normalized = []

    # Normalização dos planetas
    for planet in raw_planets:
        normalized.append({
            "id": int(planet["url"].rstrip("/").split("/")[-1]),
            "name": planet["name"],
            "climate": planet["climate"],
            "terrain": planet["terrain"],
            "population": planet["population"],
            "residents": {
                people_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in planet["residents"]
            },
            "films": {
                films_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in planet["films"]
            }
        })

    return normalized
